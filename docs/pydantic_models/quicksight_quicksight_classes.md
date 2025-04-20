# Quicksight Quicksight Classes

# AccountCustomization

### DefaultTheme
- **Type**: typing.Optional[str]

### DefaultEmailCustomizationTemplate
- **Type**: typing.Optional[str]


# AccountInfo

### AccountName
- **Type**: typing.Optional[str]

### Edition
- **Type**: typing.Optional[typing.Literal['ENTERPRISE', 'ENTERPRISE_AND_Q', 'STANDARD']]

### NotificationEmail
- **Type**: typing.Optional[str]

### AuthenticationType
- **Type**: typing.Optional[str]

### AccountSubscriptionStatus
- **Type**: typing.Optional[str]

### IAMIdentityCenterInstanceArn
- **Type**: typing.Optional[str]


# AccountSettings

### AccountName
- **Type**: typing.Optional[str]

### Edition
- **Type**: typing.Optional[typing.Literal['ENTERPRISE', 'ENTERPRISE_AND_Q', 'STANDARD']]

### DefaultNamespace
- **Type**: typing.Optional[str]

### NotificationEmail
- **Type**: typing.Optional[str]

### PublicSharingEnabled
- **Type**: typing.Optional[bool]

### TerminationProtectionEnabled
- **Type**: typing.Optional[bool]


# ActiveIAMPolicyAssignment

### AssignmentName
- **Type**: typing.Optional[str]

### PolicyArn
- **Type**: typing.Optional[str]


# AdHocFilteringOption

### AvailabilityStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# AggFunction

### Aggregation
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'COLUMN', 'COUNT', 'CUSTOM', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'PERCENTILE', 'PTD_AVERAGE', 'PTD_COUNT', 'PTD_DISTINCT_COUNT', 'PTD_MAX', 'PTD_MIN', 'PTD_SUM', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]

### AggregationFunctionParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### Period
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### PeriodField
- **Type**: typing.Optional[str]


# AggFunctionOutput

### Aggregation
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'COLUMN', 'COUNT', 'CUSTOM', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'PERCENTILE', 'PTD_AVERAGE', 'PTD_COUNT', 'PTD_DISTINCT_COUNT', 'PTD_MAX', 'PTD_MIN', 'PTD_SUM', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]

### AggregationFunctionParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### Period
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### PeriodField
- **Type**: typing.Optional[str]


# AggregationFunction

### NumericalAggregationFunction
- **Type**: <class 'NoneType'>

### CategoricalAggregationFunction
- **Type**: typing.Optional[typing.Literal['COUNT', 'DISTINCT_COUNT']]

### DateAggregationFunction
- **Type**: typing.Optional[typing.Literal['COUNT', 'DISTINCT_COUNT', 'MAX', 'MIN']]

### AttributeAggregationFunction
- **Type**: <class 'NoneType'>


# AggregationPartitionBy

### FieldName
- **Type**: typing.Optional[str]

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]


# AggregationSortConfiguration

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### SortDirection
- **Type**: typing.Literal['ASC', 'DESC']
- **Required**: Yes

### AggregationFunction
- **Type**: <class 'NoneType'>


# AmazonElasticsearchParameters

### Domain
- **Type**: <class 'str'>
- **Required**: Yes


# AmazonOpenSearchParameters

### Domain
- **Type**: <class 'str'>
- **Required**: Yes


# Analysis

### AnalysisId
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CREATION_FAILED', 'CREATION_IN_PROGRESS', 'CREATION_SUCCESSFUL', 'DELETED', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']]

### Errors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AnalysisError]]

### DataSetArns
- **Type**: typing.Optional[typing.List[str]]

### ThemeArn
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### Sheets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Sheet]]


# AnalysisDefaults

### DefaultNewSheetConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DefaultNewSheetConfiguration'>
- **Required**: Yes


# AnalysisDefinition

### DataSetIdentifierDeclarations
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataSetIdentifierDeclaration]
- **Required**: Yes

### Sheets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SheetDefinition]]

### CalculatedFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CalculatedField]]

### ParameterDeclarations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ParameterDeclaration]]

### FilterGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterGroup]]

### ColumnConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnConfiguration]]

### AnalysisDefaults
- **Type**: <class 'NoneType'>

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetOptions]

### QueryExecutionOptions
- **Type**: <class 'NoneType'>

### StaticFiles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.StaticFile]]


# AnalysisDefinitionOutput

### DataSetIdentifierDeclarations
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataSetIdentifierDeclaration]
- **Required**: Yes

### Sheets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SheetDefinitionOutput]]

### CalculatedFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CalculatedField]]

### ParameterDeclarations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ParameterDeclarationOutput]]

### FilterGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterGroupOutput]]

### ColumnConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnConfigurationOutput]]

### AnalysisDefaults
- **Type**: <class 'NoneType'>

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetOptions]

### QueryExecutionOptions
- **Type**: <class 'NoneType'>

### StaticFiles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.StaticFile]]


# AnalysisError

### Type
- **Type**: typing.Optional[typing.Literal['ACCESS_DENIED', 'COLUMN_GEOGRAPHIC_ROLE_MISMATCH', 'COLUMN_REPLACEMENT_MISSING', 'COLUMN_TYPE_MISMATCH', 'DATA_SET_NOT_FOUND', 'INTERNAL_FAILURE', 'PARAMETER_NOT_FOUND', 'PARAMETER_TYPE_INVALID', 'PARAMETER_VALUE_INCOMPATIBLE', 'SOURCE_NOT_FOUND']]

### Message
- **Type**: typing.Optional[str]

### ViolatedEntities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Entity]]


# AnalysisSearchFilter

### Operator
- **Type**: typing.Optional[typing.Literal['StringEquals', 'StringLike']]

### Name
- **Type**: typing.Optional[typing.Literal['ANALYSIS_NAME', 'DIRECT_QUICKSIGHT_OWNER', 'DIRECT_QUICKSIGHT_SOLE_OWNER', 'DIRECT_QUICKSIGHT_VIEWER_OR_OWNER', 'QUICKSIGHT_OWNER', 'QUICKSIGHT_USER', 'QUICKSIGHT_VIEWER_OR_OWNER']]

### Value
- **Type**: typing.Optional[str]


# AnalysisSourceEntity

### SourceTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AnalysisSourceTemplate]


# AnalysisSourceTemplate

### DataSetReferences
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataSetReference]
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# AnalysisSummary

### Arn
- **Type**: typing.Optional[str]

### AnalysisId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CREATION_FAILED', 'CREATION_IN_PROGRESS', 'CREATION_SUCCESSFUL', 'DELETED', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]


# Anchor

### AnchorType
- **Type**: typing.Optional[typing.Literal['TODAY']]

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### Offset
- **Type**: typing.Optional[int]


# AnchorDateConfiguration

### AnchorOption
- **Type**: typing.Optional[typing.Literal['NOW']]

### ParameterName
- **Type**: typing.Optional[str]


# AnonymousUserDashboardEmbeddingConfiguration

### InitialDashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### EnabledFeatures
- **Type**: typing.Optional[typing.List[typing.Literal['SHARED_VIEW']]]

### DisabledFeatures
- **Type**: typing.Optional[typing.List[typing.Literal['SHARED_VIEW']]]

### FeatureConfigurations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AnonymousUserDashboardFeatureConfigurations]


# AnonymousUserDashboardFeatureConfigurations

### SharedView
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SharedViewConfigurations]


# AnonymousUserDashboardVisualEmbeddingConfiguration

### InitialDashboardVisualId
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DashboardVisualId'>
- **Required**: Yes


# AnonymousUserEmbeddingExperienceConfiguration

### Dashboard
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AnonymousUserDashboardEmbeddingConfiguration]

### DashboardVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AnonymousUserDashboardVisualEmbeddingConfiguration]

### QSearchBar
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AnonymousUserQSearchBarEmbeddingConfiguration]

### GenerativeQnA
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AnonymousUserGenerativeQnAEmbeddingConfiguration]


# AnonymousUserGenerativeQnAEmbeddingConfiguration

### InitialTopicId
- **Type**: <class 'str'>
- **Required**: Yes


# AnonymousUserQSearchBarEmbeddingConfiguration

### InitialTopicId
- **Type**: <class 'str'>
- **Required**: Yes


# AnonymousUserSnapshotJobResult

### FileGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SnapshotJobResultFileGroup]]


# ApplicationTheme

### BrandColorPalette
- **Type**: <class 'NoneType'>

### BrandElementStyle
- **Type**: <class 'NoneType'>


# ArcAxisConfiguration

### Range
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ArcAxisDisplayRange]

### ReserveRange
- **Type**: typing.Optional[int]


# ArcAxisDisplayRange

### Min
- **Type**: typing.Optional[float]

### Max
- **Type**: typing.Optional[float]


# ArcConfiguration

### ArcAngle
- **Type**: typing.Optional[float]

### ArcThickness
- **Type**: typing.Optional[typing.Literal['LARGE', 'MEDIUM', 'SMALL']]


# ArcOptions

### ArcThickness
- **Type**: typing.Optional[typing.Literal['LARGE', 'MEDIUM', 'SMALL', 'WHOLE']]


# AssetBundleCloudFormationOverridePropertyConfiguration

### ResourceIdOverrideConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleExportJobResourceIdOverrideConfiguration]

### VPCConnections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleExportJobVPCConnectionOverrideProperties]]

### RefreshSchedules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleExportJobRefreshScheduleOverrideProperties]]

### DataSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleExportJobDataSourceOverrideProperties]]

### DataSets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleExportJobDataSetOverrideProperties]]

### Themes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleExportJobThemeOverrideProperties]]

### Analyses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleExportJobAnalysisOverrideProperties]]

### Dashboards
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleExportJobDashboardOverrideProperties]]

### Folders
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleExportJobFolderOverrideProperties]]


# AssetBundleCloudFormationOverridePropertyConfigurationOutput

### ResourceIdOverrideConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleExportJobResourceIdOverrideConfiguration]

### VPCConnections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleExportJobVPCConnectionOverridePropertiesOutput]]

### RefreshSchedules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleExportJobRefreshScheduleOverridePropertiesOutput]]

### DataSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleExportJobDataSourceOverridePropertiesOutput]]

### DataSets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleExportJobDataSetOverridePropertiesOutput]]

### Themes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleExportJobThemeOverridePropertiesOutput]]

### Analyses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleExportJobAnalysisOverridePropertiesOutput]]

### Dashboards
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleExportJobDashboardOverridePropertiesOutput]]

### Folders
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleExportJobFolderOverridePropertiesOutput]]


# AssetBundleExportJobAnalysisOverrideProperties

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.List[typing.Literal['Name']]
- **Required**: Yes


# AssetBundleExportJobAnalysisOverridePropertiesOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.List[typing.Literal['Name']]
- **Required**: Yes


# AssetBundleExportJobDashboardOverrideProperties

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.List[typing.Literal['Name']]
- **Required**: Yes


# AssetBundleExportJobDashboardOverridePropertiesOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.List[typing.Literal['Name']]
- **Required**: Yes


# AssetBundleExportJobDataSetOverrideProperties

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.List[typing.Literal['Name']]
- **Required**: Yes


# AssetBundleExportJobDataSetOverridePropertiesOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.List[typing.Literal['Name']]
- **Required**: Yes


# AssetBundleExportJobDataSourceOverrideProperties

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.List[typing.Literal['Catalog', 'ClusterId', 'DataSetName', 'Database', 'DisableSsl', 'Domain', 'Host', 'InstanceId', 'ManifestFileLocation', 'Name', 'Password', 'Port', 'ProductType', 'RoleArn', 'SecretArn', 'Username', 'Warehouse', 'WorkGroup']]
- **Required**: Yes


# AssetBundleExportJobDataSourceOverridePropertiesOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.List[typing.Literal['Catalog', 'ClusterId', 'DataSetName', 'Database', 'DisableSsl', 'Domain', 'Host', 'InstanceId', 'ManifestFileLocation', 'Name', 'Password', 'Port', 'ProductType', 'RoleArn', 'SecretArn', 'Username', 'Warehouse', 'WorkGroup']]
- **Required**: Yes


# AssetBundleExportJobError

### Arn
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# AssetBundleExportJobFolderOverrideProperties

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.List[typing.Literal['Name', 'ParentFolderArn']]
- **Required**: Yes


# AssetBundleExportJobFolderOverridePropertiesOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.List[typing.Literal['Name', 'ParentFolderArn']]
- **Required**: Yes


# AssetBundleExportJobRefreshScheduleOverrideProperties

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.List[typing.Literal['StartAfterDateTime']]
- **Required**: Yes


# AssetBundleExportJobRefreshScheduleOverridePropertiesOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.List[typing.Literal['StartAfterDateTime']]
- **Required**: Yes


# AssetBundleExportJobResourceIdOverrideConfiguration

### PrefixForAllResources
- **Type**: typing.Optional[bool]


# AssetBundleExportJobSummary

### JobStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'QUEUED_FOR_IMMEDIATE_EXECUTION', 'SUCCESSFUL']]

### Arn
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### AssetBundleExportJobId
- **Type**: typing.Optional[str]

### IncludeAllDependencies
- **Type**: typing.Optional[bool]

### ExportFormat
- **Type**: typing.Optional[typing.Literal['CLOUDFORMATION_JSON', 'QUICKSIGHT_JSON']]

### IncludePermissions
- **Type**: typing.Optional[bool]

### IncludeTags
- **Type**: typing.Optional[bool]


# AssetBundleExportJobThemeOverrideProperties

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.List[typing.Literal['Name']]
- **Required**: Yes


# AssetBundleExportJobThemeOverridePropertiesOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.List[typing.Literal['Name']]
- **Required**: Yes


# AssetBundleExportJobVPCConnectionOverrideProperties

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.List[typing.Literal['DnsResolvers', 'Name', 'RoleArn']]
- **Required**: Yes


# AssetBundleExportJobVPCConnectionOverridePropertiesOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.List[typing.Literal['DnsResolvers', 'Name', 'RoleArn']]
- **Required**: Yes


# AssetBundleExportJobValidationStrategy

### StrictModeForAllResources
- **Type**: typing.Optional[bool]


# AssetBundleExportJobWarning

### Arn
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# AssetBundleImportJobAnalysisOverrideParameters

### AnalysisId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# AssetBundleImportJobAnalysisOverridePermissions

### AnalysisIds
- **Type**: typing.List[str]
- **Required**: Yes

### Permissions
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleResourcePermissions'>
- **Required**: Yes


# AssetBundleImportJobAnalysisOverridePermissionsOutput

### AnalysisIds
- **Type**: typing.List[str]
- **Required**: Yes

### Permissions
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleResourcePermissionsOutput'>
- **Required**: Yes


# AssetBundleImportJobAnalysisOverrideTags

### AnalysisIds
- **Type**: typing.List[str]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Tag]
- **Required**: Yes


# AssetBundleImportJobAnalysisOverrideTagsOutput

### AnalysisIds
- **Type**: typing.List[str]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Tag]
- **Required**: Yes


# AssetBundleImportJobDashboardOverrideParameters

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# AssetBundleImportJobDashboardOverridePermissions

### DashboardIds
- **Type**: typing.List[str]
- **Required**: Yes

### Permissions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleResourcePermissions]

### LinkSharingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleResourceLinkSharingConfiguration]


# AssetBundleImportJobDashboardOverridePermissionsOutput

### DashboardIds
- **Type**: typing.List[str]
- **Required**: Yes

### Permissions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleResourcePermissionsOutput]

### LinkSharingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleResourceLinkSharingConfigurationOutput]


# AssetBundleImportJobDashboardOverrideTags

### DashboardIds
- **Type**: typing.List[str]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Tag]
- **Required**: Yes


# AssetBundleImportJobDashboardOverrideTagsOutput

### DashboardIds
- **Type**: typing.List[str]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Tag]
- **Required**: Yes


# AssetBundleImportJobDataSetOverrideParameters

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# AssetBundleImportJobDataSetOverridePermissions

### DataSetIds
- **Type**: typing.List[str]
- **Required**: Yes

### Permissions
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleResourcePermissions'>
- **Required**: Yes


# AssetBundleImportJobDataSetOverridePermissionsOutput

### DataSetIds
- **Type**: typing.List[str]
- **Required**: Yes

### Permissions
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleResourcePermissionsOutput'>
- **Required**: Yes


# AssetBundleImportJobDataSetOverrideTags

### DataSetIds
- **Type**: typing.List[str]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Tag]
- **Required**: Yes


# AssetBundleImportJobDataSetOverrideTagsOutput

### DataSetIds
- **Type**: typing.List[str]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Tag]
- **Required**: Yes


# AssetBundleImportJobDataSourceCredentialPair

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: <class 'str'>
- **Required**: Yes


# AssetBundleImportJobDataSourceCredentials

### CredentialPair
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobDataSourceCredentialPair]

### SecretArn
- **Type**: typing.Optional[str]


# AssetBundleImportJobDataSourceOverrideParameters

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### DataSourceParameters
- **Type**: <class 'NoneType'>

### VpcConnectionProperties
- **Type**: <class 'NoneType'>

### SslProperties
- **Type**: <class 'NoneType'>

### Credentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobDataSourceCredentials]


# AssetBundleImportJobDataSourceOverrideParametersOutput

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### DataSourceParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataSourceParametersOutput]

### VpcConnectionProperties
- **Type**: <class 'NoneType'>

### SslProperties
- **Type**: <class 'NoneType'>

### Credentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobDataSourceCredentials]


# AssetBundleImportJobDataSourceOverridePermissions

### DataSourceIds
- **Type**: typing.List[str]
- **Required**: Yes

### Permissions
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleResourcePermissions'>
- **Required**: Yes


# AssetBundleImportJobDataSourceOverridePermissionsOutput

### DataSourceIds
- **Type**: typing.List[str]
- **Required**: Yes

### Permissions
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleResourcePermissionsOutput'>
- **Required**: Yes


# AssetBundleImportJobDataSourceOverrideTags

### DataSourceIds
- **Type**: typing.List[str]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Tag]
- **Required**: Yes


# AssetBundleImportJobDataSourceOverrideTagsOutput

### DataSourceIds
- **Type**: typing.List[str]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Tag]
- **Required**: Yes


# AssetBundleImportJobError

### Arn
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# AssetBundleImportJobFolderOverrideParameters

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### ParentFolderArn
- **Type**: typing.Optional[str]


# AssetBundleImportJobFolderOverridePermissions

### FolderIds
- **Type**: typing.List[str]
- **Required**: Yes

### Permissions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleResourcePermissions]


# AssetBundleImportJobFolderOverridePermissionsOutput

### FolderIds
- **Type**: typing.List[str]
- **Required**: Yes

### Permissions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleResourcePermissionsOutput]


# AssetBundleImportJobFolderOverrideTags

### FolderIds
- **Type**: typing.List[str]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Tag]
- **Required**: Yes


# AssetBundleImportJobFolderOverrideTagsOutput

### FolderIds
- **Type**: typing.List[str]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Tag]
- **Required**: Yes


# AssetBundleImportJobOverrideParameters

### ResourceIdOverrideConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobResourceIdOverrideConfiguration]

### VPCConnections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobVPCConnectionOverrideParameters]]

### RefreshSchedules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobRefreshScheduleOverrideParameters]]

### DataSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobDataSourceOverrideParameters]]

### DataSets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobDataSetOverrideParameters]]

### Themes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobThemeOverrideParameters]]

### Analyses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobAnalysisOverrideParameters]]

### Dashboards
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobDashboardOverrideParameters]]

### Folders
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobFolderOverrideParameters]]


# AssetBundleImportJobOverrideParametersOutput

### ResourceIdOverrideConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobResourceIdOverrideConfiguration]

### VPCConnections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobVPCConnectionOverrideParametersOutput]]

### RefreshSchedules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobRefreshScheduleOverrideParametersOutput]]

### DataSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobDataSourceOverrideParametersOutput]]

### DataSets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobDataSetOverrideParameters]]

### Themes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobThemeOverrideParameters]]

### Analyses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobAnalysisOverrideParameters]]

### Dashboards
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobDashboardOverrideParameters]]

### Folders
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobFolderOverrideParameters]]


# AssetBundleImportJobOverridePermissions

### DataSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobDataSourceOverridePermissions]]

### DataSets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobDataSetOverridePermissions]]

### Themes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobThemeOverridePermissions]]

### Analyses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobAnalysisOverridePermissions]]

### Dashboards
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobDashboardOverridePermissions]]

### Folders
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobFolderOverridePermissions]]


# AssetBundleImportJobOverridePermissionsOutput

### DataSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobDataSourceOverridePermissionsOutput]]

### DataSets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobDataSetOverridePermissionsOutput]]

### Themes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobThemeOverridePermissionsOutput]]

### Analyses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobAnalysisOverridePermissionsOutput]]

### Dashboards
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobDashboardOverridePermissionsOutput]]

### Folders
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobFolderOverridePermissionsOutput]]


# AssetBundleImportJobOverrideTags

### VPCConnections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobVPCConnectionOverrideTags]]

### DataSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobDataSourceOverrideTags]]

### DataSets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobDataSetOverrideTags]]

### Themes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobThemeOverrideTags]]

### Analyses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobAnalysisOverrideTags]]

### Dashboards
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobDashboardOverrideTags]]

### Folders
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobFolderOverrideTags]]


# AssetBundleImportJobOverrideTagsOutput

### VPCConnections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobVPCConnectionOverrideTagsOutput]]

### DataSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobDataSourceOverrideTagsOutput]]

### DataSets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobDataSetOverrideTagsOutput]]

### Themes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobThemeOverrideTagsOutput]]

### Analyses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobAnalysisOverrideTagsOutput]]

### Dashboards
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobDashboardOverrideTagsOutput]]

### Folders
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobFolderOverrideTagsOutput]]


# AssetBundleImportJobOverrideValidationStrategy

### StrictModeForAllResources
- **Type**: typing.Optional[bool]


# AssetBundleImportJobRefreshScheduleOverrideParameters

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleId
- **Type**: <class 'str'>
- **Required**: Yes

### StartAfterDateTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# AssetBundleImportJobRefreshScheduleOverrideParametersOutput

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleId
- **Type**: <class 'str'>
- **Required**: Yes

### StartAfterDateTime
- **Type**: typing.Optional[datetime.datetime]


# AssetBundleImportJobResourceIdOverrideConfiguration

### PrefixForAllResources
- **Type**: typing.Optional[str]


# AssetBundleImportJobSummary

### JobStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'FAILED_ROLLBACK_COMPLETED', 'FAILED_ROLLBACK_ERROR', 'FAILED_ROLLBACK_IN_PROGRESS', 'IN_PROGRESS', 'QUEUED_FOR_IMMEDIATE_EXECUTION', 'SUCCESSFUL']]

### Arn
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### AssetBundleImportJobId
- **Type**: typing.Optional[str]

### FailureAction
- **Type**: typing.Optional[typing.Literal['DO_NOTHING', 'ROLLBACK']]


# AssetBundleImportJobThemeOverrideParameters

### ThemeId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# AssetBundleImportJobThemeOverridePermissions

### ThemeIds
- **Type**: typing.List[str]
- **Required**: Yes

### Permissions
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleResourcePermissions'>
- **Required**: Yes


# AssetBundleImportJobThemeOverridePermissionsOutput

### ThemeIds
- **Type**: typing.List[str]
- **Required**: Yes

### Permissions
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleResourcePermissionsOutput'>
- **Required**: Yes


# AssetBundleImportJobThemeOverrideTags

### ThemeIds
- **Type**: typing.List[str]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Tag]
- **Required**: Yes


# AssetBundleImportJobThemeOverrideTagsOutput

### ThemeIds
- **Type**: typing.List[str]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Tag]
- **Required**: Yes


# AssetBundleImportJobVPCConnectionOverrideParameters

### VPCConnectionId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### DnsResolvers
- **Type**: typing.Optional[typing.List[str]]

### RoleArn
- **Type**: typing.Optional[str]


# AssetBundleImportJobVPCConnectionOverrideParametersOutput

### VPCConnectionId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### DnsResolvers
- **Type**: typing.Optional[typing.List[str]]

### RoleArn
- **Type**: typing.Optional[str]


# AssetBundleImportJobVPCConnectionOverrideTags

### VPCConnectionIds
- **Type**: typing.List[str]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Tag]
- **Required**: Yes


# AssetBundleImportJobVPCConnectionOverrideTagsOutput

### VPCConnectionIds
- **Type**: typing.List[str]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Tag]
- **Required**: Yes


# AssetBundleImportJobWarning

### Arn
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# AssetBundleImportSource

### Body
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]

### S3Uri
- **Type**: typing.Optional[str]


# AssetBundleImportSourceDescription

### Body
- **Type**: typing.Optional[str]

### S3Uri
- **Type**: typing.Optional[str]


# AssetBundleResourceLinkSharingConfiguration

### Permissions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleResourcePermissions]


# AssetBundleResourceLinkSharingConfigurationOutput

### Permissions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleResourcePermissionsOutput]


# AssetBundleResourcePermissions

### Principals
- **Type**: typing.List[str]
- **Required**: Yes

### Actions
- **Type**: typing.List[str]
- **Required**: Yes


# AssetBundleResourcePermissionsOutput

### Principals
- **Type**: typing.List[str]
- **Required**: Yes

### Actions
- **Type**: typing.List[str]
- **Required**: Yes


# AssetOptions

### Timezone
- **Type**: typing.Optional[str]

### WeekStart
- **Type**: typing.Optional[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY']]


# AthenaParameters

### WorkGroup
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]


# AttributeAggregationFunction

### SimpleAttributeAggregation
- **Type**: typing.Optional[typing.Literal['UNIQUE_VALUE']]

### ValueForMultipleValues
- **Type**: typing.Optional[str]


# AuroraParameters

### Host
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes


# AuroraPostgreSqlParameters

### Host
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes


# AuthorizedTargetsByService

### Service
- **Type**: typing.Optional[typing.Literal['QBUSINESS', 'REDSHIFT']]

### AuthorizedTargets
- **Type**: typing.Optional[typing.List[str]]


# AwsIotAnalyticsParameters

### DataSetName
- **Type**: <class 'str'>
- **Required**: Yes


# AxisDataOptions

### NumericAxisOptions
- **Type**: <class 'NoneType'>

### DateAxisOptions
- **Type**: <class 'NoneType'>


# AxisDataOptionsOutput

### NumericAxisOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.NumericAxisOptionsOutput]

### DateAxisOptions
- **Type**: <class 'NoneType'>


# AxisDisplayMinMaxRange

### Minimum
- **Type**: typing.Optional[float]

### Maximum
- **Type**: typing.Optional[float]


# AxisDisplayOptions

### TickLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisTickLabelOptions]

### AxisLineVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### GridLineVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### DataOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDataOptions]

### ScrollbarOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ScrollBarOptions]

### AxisOffset
- **Type**: typing.Optional[str]


# AxisDisplayOptionsOutput

### TickLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisTickLabelOptions]

### AxisLineVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### GridLineVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### DataOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDataOptionsOutput]

### ScrollbarOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ScrollBarOptions]

### AxisOffset
- **Type**: typing.Optional[str]


# AxisDisplayRange

### MinMax
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDisplayMinMaxRange]

### DataDriven
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# AxisDisplayRangeOutput

### MinMax
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDisplayMinMaxRange]

### DataDriven
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# AxisLabelOptions

### FontConfiguration
- **Type**: <class 'NoneType'>

### CustomLabel
- **Type**: typing.Optional[str]

### ApplyTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisLabelReferenceOptions]


# AxisLabelReferenceOptions

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes


# AxisLinearScale

### StepCount
- **Type**: typing.Optional[int]

### StepSize
- **Type**: typing.Optional[float]


# AxisLogarithmicScale

### Base
- **Type**: typing.Optional[float]


# AxisScale

### Linear
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisLinearScale]

### Logarithmic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisLogarithmicScale]


# AxisTickLabelOptions

### LabelOptions
- **Type**: <class 'NoneType'>

### RotationAngle
- **Type**: typing.Optional[float]


# BarChartAggregatedFieldWells

### Category
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]

### Colors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### SmallMultiples
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]


# BarChartAggregatedFieldWellsOutput

### Category
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]

### Colors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### SmallMultiples
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]


# BarChartConfiguration

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BarChartFieldWells]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BarChartSortConfiguration]

### Orientation
- **Type**: typing.Optional[typing.Literal['HORIZONTAL', 'VERTICAL']]

### BarsArrangement
- **Type**: typing.Optional[typing.Literal['CLUSTERED', 'STACKED', 'STACKED_PERCENT']]

### VisualPalette
- **Type**: <class 'NoneType'>

### SmallMultiplesOptions
- **Type**: <class 'NoneType'>

### CategoryAxis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDisplayOptions]

### CategoryLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptions]

### ValueAxis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDisplayOptions]

### ValueLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptions]

### ColorLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptions]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LegendOptions]

### DataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataLabelOptions]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TooltipOptions]

### ReferenceLines
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ReferenceLine]]

### ContributionAnalysisDefaults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ContributionAnalysisDefault]]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# BarChartConfigurationOutput

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BarChartFieldWellsOutput]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BarChartSortConfigurationOutput]

### Orientation
- **Type**: typing.Optional[typing.Literal['HORIZONTAL', 'VERTICAL']]

### BarsArrangement
- **Type**: typing.Optional[typing.Literal['CLUSTERED', 'STACKED', 'STACKED_PERCENT']]

### VisualPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualPaletteOutput]

### SmallMultiplesOptions
- **Type**: <class 'NoneType'>

### CategoryAxis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDisplayOptionsOutput]

### CategoryLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptionsOutput]

### ValueAxis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDisplayOptionsOutput]

### ValueLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptionsOutput]

### ColorLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptionsOutput]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LegendOptions]

### DataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataLabelOptionsOutput]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TooltipOptionsOutput]

### ReferenceLines
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ReferenceLine]]

### ContributionAnalysisDefaults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ContributionAnalysisDefaultOutput]]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# BarChartFieldWells

### BarChartAggregatedFieldWells
- **Type**: <class 'NoneType'>


# BarChartFieldWellsOutput

### BarChartAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BarChartAggregatedFieldWellsOutput]


# BarChartSortConfiguration

### CategorySort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### CategoryItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]

### ColorSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### ColorItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]

### SmallMultiplesSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### SmallMultiplesLimitConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]


# BarChartSortConfigurationOutput

### CategorySort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### CategoryItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]

### ColorSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### ColorItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]

### SmallMultiplesSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### SmallMultiplesLimitConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]


# BarChartVisual

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BarChartConfiguration]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomAction]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnHierarchy]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# BarChartVisualOutput

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BarChartConfigurationOutput]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomActionOutput]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnHierarchyOutput]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchCreateTopicReviewedAnswerRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### Answers
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CreateTopicReviewedAnswer]
- **Required**: Yes


# BatchCreateTopicReviewedAnswerResponse

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### SucceededAnswers
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SucceededTopicReviewedAnswer]
- **Required**: Yes

### InvalidAnswers
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.InvalidTopicReviewedAnswer]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDeleteTopicReviewedAnswerRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### AnswerIds
- **Type**: typing.Optional[typing.List[str]]


# BatchDeleteTopicReviewedAnswerResponse

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### SucceededAnswers
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SucceededTopicReviewedAnswer]
- **Required**: Yes

### InvalidAnswers
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.InvalidTopicReviewedAnswer]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# BigQueryParameters

### ProjectId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetRegion
- **Type**: typing.Optional[str]


# BinCountOptions

### Value
- **Type**: typing.Optional[int]


# BinWidthOptions

### Value
- **Type**: typing.Optional[float]

### BinCountLimit
- **Type**: typing.Optional[int]


# BodySectionConfiguration

### SectionId
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BodySectionContent'>
- **Required**: Yes

### Style
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SectionStyle]

### PageBreakConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SectionPageBreakConfiguration]

### RepeatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BodySectionRepeatConfiguration]


# BodySectionConfigurationOutput

### SectionId
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BodySectionContentOutput'>
- **Required**: Yes

### Style
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SectionStyle]

### PageBreakConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SectionPageBreakConfiguration]

### RepeatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BodySectionRepeatConfigurationOutput]


# BodySectionContent

### Layout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SectionLayoutConfiguration]


# BodySectionContentOutput

### Layout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SectionLayoutConfigurationOutput]


# BodySectionDynamicCategoryDimensionConfiguration

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### SortByMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnSort]]


# BodySectionDynamicCategoryDimensionConfigurationOutput

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### SortByMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnSort]]


# BodySectionDynamicNumericDimensionConfiguration

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### SortByMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnSort]]


# BodySectionDynamicNumericDimensionConfigurationOutput

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### SortByMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnSort]]


# BodySectionRepeatConfiguration

### DimensionConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BodySectionRepeatDimensionConfiguration]]

### PageBreakConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BodySectionRepeatPageBreakConfiguration]

### NonRepeatingVisuals
- **Type**: typing.Optional[typing.List[str]]


# BodySectionRepeatConfigurationOutput

### DimensionConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BodySectionRepeatDimensionConfigurationOutput]]

### PageBreakConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BodySectionRepeatPageBreakConfiguration]

### NonRepeatingVisuals
- **Type**: typing.Optional[typing.List[str]]


# BodySectionRepeatDimensionConfiguration

### DynamicCategoryDimensionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BodySectionDynamicCategoryDimensionConfiguration]

### DynamicNumericDimensionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BodySectionDynamicNumericDimensionConfiguration]


# BodySectionRepeatDimensionConfigurationOutput

### DynamicCategoryDimensionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BodySectionDynamicCategoryDimensionConfigurationOutput]

### DynamicNumericDimensionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BodySectionDynamicNumericDimensionConfigurationOutput]


# BodySectionRepeatPageBreakConfiguration

### After
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SectionAfterPageBreak]


# BookmarksConfigurations

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# BorderStyle

### Show
- **Type**: typing.Optional[bool]


# BoxPlotAggregatedFieldWells

### GroupBy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]


# BoxPlotAggregatedFieldWellsOutput

### GroupBy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]


# BoxPlotChartConfiguration

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BoxPlotFieldWells]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BoxPlotSortConfiguration]

### BoxPlotOptions
- **Type**: <class 'NoneType'>

### CategoryAxis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDisplayOptions]

### CategoryLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptions]

### PrimaryYAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDisplayOptions]

### PrimaryYAxisLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptions]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LegendOptions]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TooltipOptions]

### ReferenceLines
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ReferenceLine]]

### VisualPalette
- **Type**: <class 'NoneType'>

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# BoxPlotChartConfigurationOutput

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BoxPlotFieldWellsOutput]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BoxPlotSortConfigurationOutput]

### BoxPlotOptions
- **Type**: <class 'NoneType'>

### CategoryAxis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDisplayOptionsOutput]

### CategoryLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptionsOutput]

### PrimaryYAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDisplayOptionsOutput]

### PrimaryYAxisLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptionsOutput]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LegendOptions]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TooltipOptionsOutput]

### ReferenceLines
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ReferenceLine]]

### VisualPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualPaletteOutput]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# BoxPlotFieldWells

### BoxPlotAggregatedFieldWells
- **Type**: <class 'NoneType'>


# BoxPlotFieldWellsOutput

### BoxPlotAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BoxPlotAggregatedFieldWellsOutput]


# BoxPlotOptions

### StyleOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BoxPlotStyleOptions]

### OutlierVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### AllDataPointsVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# BoxPlotSortConfiguration

### CategorySort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### PaginationConfiguration
- **Type**: <class 'NoneType'>


# BoxPlotSortConfigurationOutput

### CategorySort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### PaginationConfiguration
- **Type**: <class 'NoneType'>


# BoxPlotStyleOptions

### FillStyle
- **Type**: typing.Optional[typing.Literal['SOLID', 'TRANSPARENT']]


# BoxPlotVisual

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BoxPlotChartConfiguration]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomAction]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnHierarchy]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# BoxPlotVisualOutput

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BoxPlotChartConfigurationOutput]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomActionOutput]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnHierarchyOutput]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# BrandColorPalette

### Primary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Palette]

### Secondary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Palette]

### Accent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Palette]

### Measure
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Palette]

### Dimension
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Palette]

### Success
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Palette]

### Info
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Palette]

### Warning
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Palette]

### Danger
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Palette]


# BrandDefinition

### BrandName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ApplicationTheme
- **Type**: <class 'NoneType'>

### LogoConfiguration
- **Type**: <class 'NoneType'>


# BrandDetail

### BrandId
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: typing.Optional[str]

### BrandStatus
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_SUCCEEDED', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### VersionId
- **Type**: typing.Optional[str]

### VersionStatus
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_SUCCEEDED']]

### Errors
- **Type**: typing.Optional[typing.List[str]]

### Logo
- **Type**: <class 'NoneType'>


# BrandElementStyle

### NavbarStyle
- **Type**: <class 'NoneType'>


# BrandSummary

### Arn
- **Type**: typing.Optional[str]

### BrandId
- **Type**: typing.Optional[str]

### BrandName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### BrandStatus
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_SUCCEEDED', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]


# CalculatedColumn

### ColumnName
- **Type**: <class 'str'>
- **Required**: Yes

### ColumnId
- **Type**: <class 'str'>
- **Required**: Yes

### Expression
- **Type**: <class 'str'>
- **Required**: Yes


# CalculatedField

### DataSetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Expression
- **Type**: <class 'str'>
- **Required**: Yes


# CalculatedMeasureField

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### Expression
- **Type**: <class 'str'>
- **Required**: Yes


# CancelIngestionRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### IngestionId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelIngestionResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### IngestionId
- **Type**: <class 'str'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# Capabilities

### ExportToCsv
- **Type**: typing.Optional[typing.Literal['DENY']]

### ExportToExcel
- **Type**: typing.Optional[typing.Literal['DENY']]

### CreateAndUpdateThemes
- **Type**: typing.Optional[typing.Literal['DENY']]

### AddOrRunAnomalyDetectionForAnalyses
- **Type**: typing.Optional[typing.Literal['DENY']]

### ShareAnalyses
- **Type**: typing.Optional[typing.Literal['DENY']]

### CreateAndUpdateDatasets
- **Type**: typing.Optional[typing.Literal['DENY']]

### ShareDatasets
- **Type**: typing.Optional[typing.Literal['DENY']]

### SubscribeDashboardEmailReports
- **Type**: typing.Optional[typing.Literal['DENY']]

### CreateAndUpdateDashboardEmailReports
- **Type**: typing.Optional[typing.Literal['DENY']]

### ShareDashboards
- **Type**: typing.Optional[typing.Literal['DENY']]

### CreateAndUpdateThresholdAlerts
- **Type**: typing.Optional[typing.Literal['DENY']]

### RenameSharedFolders
- **Type**: typing.Optional[typing.Literal['DENY']]

### CreateSharedFolders
- **Type**: typing.Optional[typing.Literal['DENY']]

### CreateAndUpdateDataSources
- **Type**: typing.Optional[typing.Literal['DENY']]

### ShareDataSources
- **Type**: typing.Optional[typing.Literal['DENY']]

### ViewAccountSPICECapacity
- **Type**: typing.Optional[typing.Literal['DENY']]

### CreateSPICEDataset
- **Type**: typing.Optional[typing.Literal['DENY']]


# CascadingControlConfiguration

### SourceControls
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CascadingControlSource]]


# CascadingControlConfigurationOutput

### SourceControls
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CascadingControlSource]]


# CascadingControlSource

### SourceSheetControlId
- **Type**: typing.Optional[str]

### ColumnToMatch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier]


# CastColumnTypeOperation

### ColumnName
- **Type**: <class 'str'>
- **Required**: Yes

### NewColumnType
- **Type**: typing.Literal['DATETIME', 'DECIMAL', 'INTEGER', 'STRING']
- **Required**: Yes

### SubType
- **Type**: typing.Optional[typing.Literal['FIXED', 'FLOAT']]

### Format
- **Type**: typing.Optional[str]


# CategoricalDimensionField

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### HierarchyId
- **Type**: typing.Optional[str]

### FormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.StringFormatConfiguration]


# CategoricalMeasureField

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### AggregationFunction
- **Type**: typing.Optional[typing.Literal['COUNT', 'DISTINCT_COUNT']]

### FormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.StringFormatConfiguration]


# CategoryDrillDownFilter

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### CategoryValues
- **Type**: typing.List[str]
- **Required**: Yes


# CategoryDrillDownFilterOutput

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### CategoryValues
- **Type**: typing.List[str]
- **Required**: Yes


# CategoryFilter

### FilterId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CategoryFilterConfiguration'>
- **Required**: Yes

### DefaultFilterControlConfiguration
- **Type**: <class 'NoneType'>


# CategoryFilterConfiguration

### FilterListConfiguration
- **Type**: <class 'NoneType'>

### CustomFilterListConfiguration
- **Type**: <class 'NoneType'>

### CustomFilterConfiguration
- **Type**: <class 'NoneType'>


# CategoryFilterConfigurationOutput

### FilterListConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterListConfigurationOutput]

### CustomFilterListConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CustomFilterListConfigurationOutput]

### CustomFilterConfiguration
- **Type**: <class 'NoneType'>


# CategoryFilterOutput

### FilterId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CategoryFilterConfigurationOutput'>
- **Required**: Yes

### DefaultFilterControlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DefaultFilterControlConfigurationOutput]


# CategoryInnerFilter

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CategoryFilterConfiguration'>
- **Required**: Yes

### DefaultFilterControlConfiguration
- **Type**: <class 'NoneType'>


# CategoryInnerFilterOutput

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CategoryFilterConfigurationOutput'>
- **Required**: Yes

### DefaultFilterControlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DefaultFilterControlConfigurationOutput]


# CellValueSynonym

### CellValue
- **Type**: typing.Optional[str]

### Synonyms
- **Type**: typing.Optional[typing.List[str]]


# CellValueSynonymOutput

### CellValue
- **Type**: typing.Optional[str]

### Synonyms
- **Type**: typing.Optional[typing.List[str]]


# ChartAxisLabelOptions

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### SortIconVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### AxisLabelOptions
- **Type**: typing.Optional[typing.List[NoneType]]


# ChartAxisLabelOptionsOutput

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### SortIconVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### AxisLabelOptions
- **Type**: typing.Optional[typing.List[NoneType]]


# ClusterMarker

### SimpleClusterMarker
- **Type**: <class 'NoneType'>


# ClusterMarkerConfiguration

### ClusterMarker
- **Type**: <class 'NoneType'>


# CollectiveConstant

### ValueList
- **Type**: typing.Optional[typing.List[str]]


# CollectiveConstantEntry

### ConstantType
- **Type**: typing.Optional[typing.Literal['COLLECTIVE', 'RANGE', 'SINGULAR']]

### Value
- **Type**: typing.Optional[str]


# CollectiveConstantOutput

### ValueList
- **Type**: typing.Optional[typing.List[str]]


# ColorScale

### Colors
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataColor]
- **Required**: Yes

### ColorFillType
- **Type**: typing.Literal['DISCRETE', 'GRADIENT']
- **Required**: Yes

### NullValueColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataColor]


# ColorScaleOutput

### Colors
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataColor]
- **Required**: Yes

### ColorFillType
- **Type**: typing.Literal['DISCRETE', 'GRADIENT']
- **Required**: Yes

### NullValueColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataColor]


# ColorsConfiguration

### CustomColors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CustomColor]]


# ColorsConfigurationOutput

### CustomColors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CustomColor]]


# ColumnConfiguration

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### FormatConfiguration
- **Type**: <class 'NoneType'>

### Role
- **Type**: typing.Optional[typing.Literal['DIMENSION', 'MEASURE']]

### ColorsConfiguration
- **Type**: <class 'NoneType'>


# ColumnConfigurationOutput

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### FormatConfiguration
- **Type**: <class 'NoneType'>

### Role
- **Type**: typing.Optional[typing.Literal['DIMENSION', 'MEASURE']]

### ColorsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColorsConfigurationOutput]


# ColumnDescription

### Text
- **Type**: typing.Optional[str]


# ColumnGroup

### GeoSpatialColumnGroup
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeoSpatialColumnGroup, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeoSpatialColumnGroupOutput, NoneType]


# ColumnGroupColumnSchema

### Name
- **Type**: typing.Optional[str]


# ColumnGroupOutput

### GeoSpatialColumnGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeoSpatialColumnGroupOutput]


# ColumnGroupSchema

### Name
- **Type**: typing.Optional[str]

### ColumnGroupColumnSchemaList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnGroupColumnSchema]]


# ColumnGroupSchemaOutput

### Name
- **Type**: typing.Optional[str]

### ColumnGroupColumnSchemaList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnGroupColumnSchema]]


# ColumnHierarchy

### ExplicitHierarchy
- **Type**: <class 'NoneType'>

### DateTimeHierarchy
- **Type**: <class 'NoneType'>

### PredefinedHierarchy
- **Type**: <class 'NoneType'>


# ColumnHierarchyOutput

### ExplicitHierarchy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ExplicitHierarchyOutput]

### DateTimeHierarchy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DateTimeHierarchyOutput]

### PredefinedHierarchy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PredefinedHierarchyOutput]


# ColumnIdentifier

### DataSetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ColumnName
- **Type**: <class 'str'>
- **Required**: Yes


# ColumnLevelPermissionRule

### Principals
- **Type**: typing.Optional[typing.List[str]]

### ColumnNames
- **Type**: typing.Optional[typing.List[str]]


# ColumnLevelPermissionRuleOutput

### Principals
- **Type**: typing.Optional[typing.List[str]]

### ColumnNames
- **Type**: typing.Optional[typing.List[str]]


# ColumnSchema

### Name
- **Type**: typing.Optional[str]

### DataType
- **Type**: typing.Optional[str]

### GeographicRole
- **Type**: typing.Optional[str]


# ColumnSort

### SortBy
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### Direction
- **Type**: typing.Literal['ASC', 'DESC']
- **Required**: Yes

### AggregationFunction
- **Type**: <class 'NoneType'>


# ColumnTag

### ColumnGeographicRole
- **Type**: typing.Optional[typing.Literal['CITY', 'COUNTRY', 'COUNTY', 'LATITUDE', 'LONGITUDE', 'POSTCODE', 'STATE']]

### ColumnDescription
- **Type**: <class 'NoneType'>


# ColumnTooltipItem

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### Label
- **Type**: typing.Optional[str]

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### Aggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AggregationFunction]

### TooltipTarget
- **Type**: typing.Optional[typing.Literal['BAR', 'BOTH', 'LINE']]


# ComboChartAggregatedFieldWells

### Category
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### BarValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]

### Colors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### LineValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]


# ComboChartAggregatedFieldWellsOutput

### Category
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### BarValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]

### Colors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### LineValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]


# ComboChartConfiguration

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ComboChartFieldWells]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ComboChartSortConfiguration]

### BarsArrangement
- **Type**: typing.Optional[typing.Literal['CLUSTERED', 'STACKED', 'STACKED_PERCENT']]

### CategoryAxis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDisplayOptions]

### CategoryLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptions]

### PrimaryYAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDisplayOptions]

### PrimaryYAxisLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptions]

### SecondaryYAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDisplayOptions]

### SecondaryYAxisLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptions]

### SingleAxisOptions
- **Type**: <class 'NoneType'>

### ColorLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptions]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LegendOptions]

### BarDataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataLabelOptions]

### LineDataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataLabelOptions]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TooltipOptions]

### ReferenceLines
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ReferenceLine]]

### VisualPalette
- **Type**: <class 'NoneType'>

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# ComboChartConfigurationOutput

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ComboChartFieldWellsOutput]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ComboChartSortConfigurationOutput]

### BarsArrangement
- **Type**: typing.Optional[typing.Literal['CLUSTERED', 'STACKED', 'STACKED_PERCENT']]

### CategoryAxis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDisplayOptionsOutput]

### CategoryLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptionsOutput]

### PrimaryYAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDisplayOptionsOutput]

### PrimaryYAxisLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptionsOutput]

### SecondaryYAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDisplayOptionsOutput]

### SecondaryYAxisLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptionsOutput]

### SingleAxisOptions
- **Type**: <class 'NoneType'>

### ColorLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptionsOutput]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LegendOptions]

### BarDataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataLabelOptionsOutput]

### LineDataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataLabelOptionsOutput]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TooltipOptionsOutput]

### ReferenceLines
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ReferenceLine]]

### VisualPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualPaletteOutput]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# ComboChartFieldWells

### ComboChartAggregatedFieldWells
- **Type**: <class 'NoneType'>


# ComboChartFieldWellsOutput

### ComboChartAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ComboChartAggregatedFieldWellsOutput]


# ComboChartSortConfiguration

### CategorySort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### CategoryItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]

### ColorSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### ColorItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]


# ComboChartSortConfigurationOutput

### CategorySort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### CategoryItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]

### ColorSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### ColorItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]


# ComboChartVisual

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ComboChartConfiguration]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomAction]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnHierarchy]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# ComboChartVisualOutput

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ComboChartConfigurationOutput]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomActionOutput]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnHierarchyOutput]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# ComparativeOrder

### UseOrdering
- **Type**: typing.Optional[typing.Literal['GREATER_IS_BETTER', 'LESSER_IS_BETTER', 'SPECIFIED']]

### SpecifedOrder
- **Type**: typing.Optional[typing.List[str]]

### TreatUndefinedSpecifiedValues
- **Type**: typing.Optional[typing.Literal['LEAST', 'MOST']]


# ComparativeOrderOutput

### UseOrdering
- **Type**: typing.Optional[typing.Literal['GREATER_IS_BETTER', 'LESSER_IS_BETTER', 'SPECIFIED']]

### SpecifedOrder
- **Type**: typing.Optional[typing.List[str]]

### TreatUndefinedSpecifiedValues
- **Type**: typing.Optional[typing.Literal['LEAST', 'MOST']]


# ComparisonConfiguration

### ComparisonMethod
- **Type**: typing.Optional[typing.Literal['DIFFERENCE', 'PERCENT', 'PERCENT_DIFFERENCE']]

### ComparisonFormat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ComparisonFormatConfiguration]


# ComparisonFormatConfiguration

### NumberDisplayFormatConfiguration
- **Type**: <class 'NoneType'>

### PercentageDisplayFormatConfiguration
- **Type**: <class 'NoneType'>


# Computation

### TopBottomRanked
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopBottomRankedComputation]

### TopBottomMovers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopBottomMoversComputation]

### TotalAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TotalAggregationComputation]

### MaximumMinimum
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MaximumMinimumComputation]

### MetricComparison
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MetricComparisonComputation]

### PeriodOverPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PeriodOverPeriodComputation]

### PeriodToDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PeriodToDateComputation]

### GrowthRate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GrowthRateComputation]

### UniqueValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.UniqueValuesComputation]

### Forecast
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ForecastComputation]


# ConditionalFormattingColor

### Solid
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingSolidColor]

### Gradient
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingGradientColor]


# ConditionalFormattingColorOutput

### Solid
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingSolidColor]

### Gradient
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingGradientColorOutput]


# ConditionalFormattingCustomIconCondition

### Expression
- **Type**: <class 'str'>
- **Required**: Yes

### IconOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingCustomIconOptions'>
- **Required**: Yes

### Color
- **Type**: typing.Optional[str]

### DisplayConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingIconDisplayConfiguration]


# ConditionalFormattingCustomIconOptions

### Icon
- **Type**: typing.Optional[typing.Literal['ARROW_DOWN', 'ARROW_DOWN_LEFT', 'ARROW_DOWN_RIGHT', 'ARROW_LEFT', 'ARROW_RIGHT', 'ARROW_UP', 'ARROW_UP_LEFT', 'ARROW_UP_RIGHT', 'CARET_DOWN', 'CARET_UP', 'CHECKMARK', 'CIRCLE', 'FACE_DOWN', 'FACE_FLAT', 'FACE_UP', 'FLAG', 'MINUS', 'ONE_BAR', 'PLUS', 'SQUARE', 'THREE_BAR', 'THUMBS_DOWN', 'THUMBS_UP', 'TRIANGLE', 'TWO_BAR', 'X']]

### UnicodeIcon
- **Type**: typing.Optional[str]


# ConditionalFormattingGradientColor

### Expression
- **Type**: <class 'str'>
- **Required**: Yes

### Color
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GradientColor'>
- **Required**: Yes


# ConditionalFormattingGradientColorOutput

### Expression
- **Type**: <class 'str'>
- **Required**: Yes

### Color
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GradientColorOutput'>
- **Required**: Yes


# ConditionalFormattingIcon

### IconSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingIconSet]

### CustomCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingCustomIconCondition]


# ConditionalFormattingIconDisplayConfiguration

### IconDisplayOption
- **Type**: typing.Optional[typing.Literal['ICON_ONLY']]


# ConditionalFormattingIconSet

### Expression
- **Type**: <class 'str'>
- **Required**: Yes

### IconSetType
- **Type**: typing.Optional[typing.Literal['BARS', 'CARET_UP_MINUS_DOWN', 'CHECK_X', 'FLAGS', 'FOUR_COLOR_ARROW', 'FOUR_GRAY_ARROW', 'PLUS_MINUS', 'THREE_CIRCLE', 'THREE_COLOR_ARROW', 'THREE_GRAY_ARROW', 'THREE_SHAPE']]


# ConditionalFormattingSolidColor

### Expression
- **Type**: <class 'str'>
- **Required**: Yes

### Color
- **Type**: typing.Optional[str]


# ContextMenuOption

### AvailabilityStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# ContributionAnalysisDefault

### MeasureFieldId
- **Type**: <class 'str'>
- **Required**: Yes

### ContributorDimensions
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier]
- **Required**: Yes


# ContributionAnalysisDefaultOutput

### MeasureFieldId
- **Type**: <class 'str'>
- **Required**: Yes

### ContributorDimensions
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier]
- **Required**: Yes


# ContributionAnalysisFactor

### FieldName
- **Type**: typing.Optional[str]


# ContributionAnalysisTimeRanges

### StartRange
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicIRFilterOption, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicIRFilterOptionOutput, NoneType]

### EndRange
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicIRFilterOption, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicIRFilterOptionOutput, NoneType]


# ContributionAnalysisTimeRangesOutput

### StartRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicIRFilterOptionOutput]

### EndRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicIRFilterOptionOutput]


# CreateAccountCustomizationRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountCustomization
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AccountCustomization'>
- **Required**: Yes

### Namespace
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Tag]]


# CreateAccountCustomizationResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### AccountCustomization
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AccountCustomization'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAccountSubscriptionRequest

### AuthenticationMethod
- **Type**: typing.Literal['ACTIVE_DIRECTORY', 'IAM_AND_QUICKSIGHT', 'IAM_IDENTITY_CENTER', 'IAM_ONLY']
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountName
- **Type**: <class 'str'>
- **Required**: Yes

### NotificationEmail
- **Type**: <class 'str'>
- **Required**: Yes

### Edition
- **Type**: typing.Optional[typing.Literal['ENTERPRISE', 'ENTERPRISE_AND_Q', 'STANDARD']]

### ActiveDirectoryName
- **Type**: typing.Optional[str]

### Realm
- **Type**: typing.Optional[str]

### DirectoryId
- **Type**: typing.Optional[str]

### AdminGroup
- **Type**: typing.Optional[typing.List[str]]

### AuthorGroup
- **Type**: typing.Optional[typing.List[str]]

### ReaderGroup
- **Type**: typing.Optional[typing.List[str]]

### AdminProGroup
- **Type**: typing.Optional[typing.List[str]]

### AuthorProGroup
- **Type**: typing.Optional[typing.List[str]]

### ReaderProGroup
- **Type**: typing.Optional[typing.List[str]]

### FirstName
- **Type**: typing.Optional[str]

### LastName
- **Type**: typing.Optional[str]

### EmailAddress
- **Type**: typing.Optional[str]

### ContactNumber
- **Type**: typing.Optional[str]

### IAMIdentityCenterInstanceArn
- **Type**: typing.Optional[str]


# CreateAccountSubscriptionResponse

### SignupResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SignupResponse'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAnalysisRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AnalysisId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Parameters, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ParametersOutput, NoneType]

### Permissions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermission, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]]]

### SourceEntity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AnalysisSourceEntity]

### ThemeArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Tag]]

### Definition
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AnalysisDefinition, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AnalysisDefinitionOutput, NoneType]

### ValidationStrategy
- **Type**: <class 'NoneType'>

### FolderArns
- **Type**: typing.Optional[typing.List[str]]


# CreateAnalysisResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AnalysisId
- **Type**: <class 'str'>
- **Required**: Yes

### CreationStatus
- **Type**: typing.Literal['CREATION_FAILED', 'CREATION_IN_PROGRESS', 'CREATION_SUCCESSFUL', 'DELETED', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# CreateBrandRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BrandId
- **Type**: <class 'str'>
- **Required**: Yes

### BrandDefinition
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Tag]]


# CreateBrandResponse

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### BrandDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BrandDetail'>
- **Required**: Yes

### BrandDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BrandDefinition'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# CreateColumnsOperation

### Columns
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CalculatedColumn]
- **Required**: Yes


# CreateColumnsOperationOutput

### Columns
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CalculatedColumn]
- **Required**: Yes


# CreateCustomPermissionsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### CustomPermissionsName
- **Type**: <class 'str'>
- **Required**: Yes

### Capabilities
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Tag]]


# CreateCustomPermissionsResponse

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDashboardRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Parameters, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ParametersOutput, NoneType]

### Permissions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermission, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]]]

### SourceEntity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DashboardSourceEntity]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Tag]]

### VersionDescription
- **Type**: typing.Optional[str]

### DashboardPublishOptions
- **Type**: <class 'NoneType'>

### ThemeArn
- **Type**: typing.Optional[str]

### Definition
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DashboardVersionDefinition, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DashboardVersionDefinitionOutput, NoneType]

### ValidationStrategy
- **Type**: <class 'NoneType'>

### FolderArns
- **Type**: typing.Optional[typing.List[str]]

### LinkSharingConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LinkSharingConfiguration, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LinkSharingConfigurationOutput, NoneType]

### LinkEntities
- **Type**: typing.Optional[typing.List[str]]


# CreateDashboardResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### VersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### CreationStatus
- **Type**: typing.Literal['CREATION_FAILED', 'CREATION_IN_PROGRESS', 'CREATION_SUCCESSFUL', 'DELETED', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDataSetRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PhysicalTableMap
- **Type**: typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PhysicalTable, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PhysicalTableOutput]]
- **Required**: Yes

### ImportMode
- **Type**: typing.Literal['DIRECT_QUERY', 'SPICE']
- **Required**: Yes

### LogicalTableMap
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LogicalTable, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LogicalTableOutput]]]

### ColumnGroups
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnGroup, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnGroupOutput]]]

### FieldFolders
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldFolder, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldFolderOutput]]]

### Permissions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermission, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]]]

### RowLevelPermissionDataSet
- **Type**: <class 'NoneType'>

### RowLevelPermissionTagConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RowLevelPermissionTagConfiguration, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RowLevelPermissionTagConfigurationOutput, NoneType]

### ColumnLevelPermissionRules
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnLevelPermissionRule, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnLevelPermissionRuleOutput]]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Tag]]

### DataSetUsageConfiguration
- **Type**: <class 'NoneType'>

### DatasetParameters
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DatasetParameter, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DatasetParameterOutput]]]

### FolderArns
- **Type**: typing.Optional[typing.List[str]]

### PerformanceConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PerformanceConfiguration, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PerformanceConfigurationOutput, NoneType]


# CreateDataSetResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### IngestionArn
- **Type**: <class 'str'>
- **Required**: Yes

### IngestionId
- **Type**: <class 'str'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDataSourceRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['ADOBE_ANALYTICS', 'AMAZON_ELASTICSEARCH', 'AMAZON_OPENSEARCH', 'ATHENA', 'AURORA', 'AURORA_POSTGRESQL', 'AWS_IOT_ANALYTICS', 'BIGQUERY', 'DATABRICKS', 'EXASOL', 'GITHUB', 'JIRA', 'MARIADB', 'MYSQL', 'ORACLE', 'POSTGRESQL', 'PRESTO', 'REDSHIFT', 'S3', 'SALESFORCE', 'SERVICENOW', 'SNOWFLAKE', 'SPARK', 'SQLSERVER', 'STARBURST', 'TERADATA', 'TIMESTREAM', 'TRINO', 'TWITTER']
- **Required**: Yes

### DataSourceParameters
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataSourceParameters, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataSourceParametersOutput, NoneType]

### Credentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataSourceCredentials]

### Permissions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermission, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]]]

### VpcConnectionProperties
- **Type**: <class 'NoneType'>

### SslProperties
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Tag]]

### FolderArns
- **Type**: typing.Optional[typing.List[str]]


# CreateDataSourceResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### CreationStatus
- **Type**: typing.Literal['CREATION_FAILED', 'CREATION_IN_PROGRESS', 'CREATION_SUCCESSFUL', 'DELETED', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFolderMembershipRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberType
- **Type**: typing.Literal['ANALYSIS', 'DASHBOARD', 'DATASET', 'DATASOURCE', 'TOPIC']
- **Required**: Yes


# CreateFolderMembershipResponse

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### FolderMember
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FolderMember'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFolderRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### FolderType
- **Type**: typing.Optional[typing.Literal['RESTRICTED', 'SHARED']]

### ParentFolderArn
- **Type**: typing.Optional[str]

### Permissions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermission, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Tag]]

### SharingModel
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'NAMESPACE']]


# CreateFolderResponse

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# CreateGroupMembershipRequest

### MemberName
- **Type**: <class 'str'>
- **Required**: Yes

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes


# CreateGroupMembershipResponse

### GroupMember
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GroupMember'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# CreateGroupRequest

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# CreateGroupResponse

### Group
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Group'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# CreateIAMPolicyAssignmentRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AssignmentName
- **Type**: <class 'str'>
- **Required**: Yes

### AssignmentStatus
- **Type**: typing.Literal['DISABLED', 'DRAFT', 'ENABLED']
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyArn
- **Type**: typing.Optional[str]

### Identities
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]


# CreateIAMPolicyAssignmentResponse

### AssignmentName
- **Type**: <class 'str'>
- **Required**: Yes

### AssignmentId
- **Type**: <class 'str'>
- **Required**: Yes

### AssignmentStatus
- **Type**: typing.Literal['DISABLED', 'DRAFT', 'ENABLED']
- **Required**: Yes

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### Identities
- **Type**: typing.Dict[str, typing.List[str]]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# CreateIngestionRequest

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### IngestionId
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### IngestionType
- **Type**: typing.Optional[typing.Literal['FULL_REFRESH', 'INCREMENTAL_REFRESH']]


# CreateIngestionResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### IngestionId
- **Type**: <class 'str'>
- **Required**: Yes

### IngestionStatus
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'FAILED', 'INITIALIZED', 'QUEUED', 'RUNNING']
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# CreateNamespaceRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityStore
- **Type**: typing.Literal['QUICKSIGHT']
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Tag]]


# CreateNamespaceResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CapacityRegion
- **Type**: <class 'str'>
- **Required**: Yes

### CreationStatus
- **Type**: typing.Literal['CREATED', 'CREATING', 'DELETING', 'NON_RETRYABLE_FAILURE', 'RETRYABLE_FAILURE']
- **Required**: Yes

### IdentityStore
- **Type**: typing.Literal['QUICKSIGHT']
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRefreshScheduleRequest

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Schedule
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RefreshSchedule, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RefreshScheduleOutput]
- **Required**: Yes


# CreateRefreshScheduleResponse

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleId
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRoleMembershipRequest

### MemberName
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### Role
- **Type**: typing.Literal['ADMIN', 'ADMIN_PRO', 'AUTHOR', 'AUTHOR_PRO', 'READER', 'READER_PRO']
- **Required**: Yes


# CreateRoleMembershipResponse

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTemplateAliasRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### AliasName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateVersionNumber
- **Type**: <class 'int'>
- **Required**: Yes


# CreateTemplateAliasResponse

### TemplateAlias
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TemplateAlias'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTemplateRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Permissions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermission, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]]]

### SourceEntity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TemplateSourceEntity]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Tag]]

### VersionDescription
- **Type**: typing.Optional[str]

### Definition
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TemplateVersionDefinition, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TemplateVersionDefinitionOutput, NoneType]

### ValidationStrategy
- **Type**: <class 'NoneType'>


# CreateTemplateResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### VersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### CreationStatus
- **Type**: typing.Literal['CREATION_FAILED', 'CREATION_IN_PROGRESS', 'CREATION_SUCCESSFUL', 'DELETED', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# CreateThemeAliasRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ThemeId
- **Type**: <class 'str'>
- **Required**: Yes

### AliasName
- **Type**: <class 'str'>
- **Required**: Yes

### ThemeVersionNumber
- **Type**: <class 'int'>
- **Required**: Yes


# CreateThemeAliasResponse

### ThemeAlias
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ThemeAlias'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# CreateThemeRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ThemeId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### BaseThemeId
- **Type**: <class 'str'>
- **Required**: Yes

### Configuration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ThemeConfiguration, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ThemeConfigurationOutput]
- **Required**: Yes

### VersionDescription
- **Type**: typing.Optional[str]

### Permissions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermission, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Tag]]


# CreateThemeResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### VersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ThemeId
- **Type**: <class 'str'>
- **Required**: Yes

### CreationStatus
- **Type**: typing.Literal['CREATION_FAILED', 'CREATION_IN_PROGRESS', 'CREATION_SUCCESSFUL', 'DELETED', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTopicRefreshScheduleRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### RefreshSchedule
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicRefreshSchedule, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicRefreshScheduleOutput]
- **Required**: Yes

### DatasetName
- **Type**: typing.Optional[str]


# CreateTopicRefreshScheduleResponse

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTopicRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### Topic
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicDetails, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicDetailsOutput]
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Tag]]

### FolderArns
- **Type**: typing.Optional[typing.List[str]]


# CreateTopicResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### RefreshArn
- **Type**: <class 'str'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTopicReviewedAnswer

### AnswerId
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### Question
- **Type**: <class 'str'>
- **Required**: Yes

### Mir
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicIR, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicIROutput, NoneType]

### PrimaryVisual
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicVisual, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicVisualOutput, NoneType]

### Template
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicTemplate, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicTemplateOutput, NoneType]


# CreateVPCConnectionRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### VPCConnectionId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### DnsResolvers
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Tag]]


# CreateVPCConnectionResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### VPCConnectionId
- **Type**: <class 'str'>
- **Required**: Yes

### CreationStatus
- **Type**: typing.Literal['CREATION_FAILED', 'CREATION_IN_PROGRESS', 'CREATION_SUCCESSFUL', 'DELETED', 'DELETION_FAILED', 'DELETION_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']
- **Required**: Yes

### AvailabilityStatus
- **Type**: typing.Literal['AVAILABLE', 'PARTIALLY_AVAILABLE', 'UNAVAILABLE']
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# CredentialPair

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: <class 'str'>
- **Required**: Yes

### AlternateDataSourceParameters
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataSourceParameters, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataSourceParametersOutput]]]


# CurrencyDisplayFormatConfiguration

### Prefix
- **Type**: typing.Optional[str]

### Suffix
- **Type**: typing.Optional[str]

### SeparatorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.NumericSeparatorConfiguration]

### Symbol
- **Type**: typing.Optional[str]

### DecimalPlacesConfiguration
- **Type**: <class 'NoneType'>

### NumberScale
- **Type**: typing.Optional[typing.Literal['AUTO', 'BILLIONS', 'CRORES', 'LAKHS', 'MILLIONS', 'NONE', 'THOUSANDS', 'TRILLIONS']]

### NegativeValueConfiguration
- **Type**: <class 'NoneType'>

### NullValueFormatConfiguration
- **Type**: <class 'NoneType'>


# CustomActionFilterOperation

### SelectedFieldsConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterOperationSelectedFieldsConfiguration'>
- **Required**: Yes

### TargetVisualsConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterOperationTargetVisualsConfiguration'>
- **Required**: Yes


# CustomActionFilterOperationOutput

### SelectedFieldsConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterOperationSelectedFieldsConfigurationOutput'>
- **Required**: Yes

### TargetVisualsConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterOperationTargetVisualsConfigurationOutput'>
- **Required**: Yes


# CustomActionNavigationOperation

### LocalNavigationConfiguration
- **Type**: <class 'NoneType'>


# CustomActionSetParametersOperation

### ParameterValueConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SetParameterValueConfiguration]
- **Required**: Yes


# CustomActionSetParametersOperationOutput

### ParameterValueConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SetParameterValueConfigurationOutput]
- **Required**: Yes


# CustomActionURLOperation

### URLTemplate
- **Type**: <class 'str'>
- **Required**: Yes

### URLTarget
- **Type**: typing.Literal['NEW_TAB', 'NEW_WINDOW', 'SAME_TAB']
- **Required**: Yes


# CustomColor

### Color
- **Type**: <class 'str'>
- **Required**: Yes

### FieldValue
- **Type**: typing.Optional[str]

### SpecialValue
- **Type**: typing.Optional[typing.Literal['EMPTY', 'NULL', 'OTHER']]


# CustomContentConfiguration

### ContentUrl
- **Type**: typing.Optional[str]

### ContentType
- **Type**: typing.Optional[typing.Literal['IMAGE', 'OTHER_EMBEDDED_CONTENT']]

### ImageScaling
- **Type**: typing.Optional[typing.Literal['DO_NOT_SCALE', 'FIT_TO_HEIGHT', 'FIT_TO_WIDTH', 'SCALE_TO_VISUAL']]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# CustomContentVisual

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CustomContentConfiguration]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomAction]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# CustomContentVisualOutput

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CustomContentConfiguration]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomActionOutput]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# CustomFilterConfiguration

### MatchOperator
- **Type**: typing.Literal['CONTAINS', 'DOES_NOT_CONTAIN', 'DOES_NOT_EQUAL', 'ENDS_WITH', 'EQUALS', 'STARTS_WITH']
- **Required**: Yes

### NullOption
- **Type**: typing.Literal['ALL_VALUES', 'NON_NULLS_ONLY', 'NULLS_ONLY']
- **Required**: Yes

### CategoryValue
- **Type**: typing.Optional[str]

### SelectAllOptions
- **Type**: typing.Optional[typing.Literal['FILTER_ALL_VALUES']]

### ParameterName
- **Type**: typing.Optional[str]


# CustomFilterListConfiguration

### MatchOperator
- **Type**: typing.Literal['CONTAINS', 'DOES_NOT_CONTAIN', 'DOES_NOT_EQUAL', 'ENDS_WITH', 'EQUALS', 'STARTS_WITH']
- **Required**: Yes

### NullOption
- **Type**: typing.Literal['ALL_VALUES', 'NON_NULLS_ONLY', 'NULLS_ONLY']
- **Required**: Yes

### CategoryValues
- **Type**: typing.Optional[typing.List[str]]

### SelectAllOptions
- **Type**: typing.Optional[typing.Literal['FILTER_ALL_VALUES']]


# CustomFilterListConfigurationOutput

### MatchOperator
- **Type**: typing.Literal['CONTAINS', 'DOES_NOT_CONTAIN', 'DOES_NOT_EQUAL', 'ENDS_WITH', 'EQUALS', 'STARTS_WITH']
- **Required**: Yes

### NullOption
- **Type**: typing.Literal['ALL_VALUES', 'NON_NULLS_ONLY', 'NULLS_ONLY']
- **Required**: Yes

### CategoryValues
- **Type**: typing.Optional[typing.List[str]]

### SelectAllOptions
- **Type**: typing.Optional[typing.Literal['FILTER_ALL_VALUES']]


# CustomNarrativeOptions

### Narrative
- **Type**: <class 'str'>
- **Required**: Yes


# CustomParameterValues

### StringValues
- **Type**: typing.Optional[typing.List[str]]

### IntegerValues
- **Type**: typing.Optional[typing.List[int]]

### DecimalValues
- **Type**: typing.Optional[typing.List[float]]

### DateTimeValues
- **Type**: typing.Optional[typing.List[typing.Union[datetime.datetime, str]]]


# CustomParameterValuesOutput

### StringValues
- **Type**: typing.Optional[typing.List[str]]

### IntegerValues
- **Type**: typing.Optional[typing.List[int]]

### DecimalValues
- **Type**: typing.Optional[typing.List[float]]

### DateTimeValues
- **Type**: typing.Optional[typing.List[datetime.datetime]]


# CustomPermissions

### Arn
- **Type**: typing.Optional[str]

### CustomPermissionsName
- **Type**: typing.Optional[str]

### Capabilities
- **Type**: <class 'NoneType'>


# CustomSql

### DataSourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SqlQuery
- **Type**: <class 'str'>
- **Required**: Yes

### Columns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.InputColumn]]


# CustomSqlOutput

### DataSourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SqlQuery
- **Type**: <class 'str'>
- **Required**: Yes

### Columns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.InputColumn]]


# CustomValuesConfiguration

### CustomValues
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CustomParameterValues'>
- **Required**: Yes

### IncludeNullValue
- **Type**: typing.Optional[bool]


# CustomValuesConfigurationOutput

### CustomValues
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CustomParameterValuesOutput'>
- **Required**: Yes

### IncludeNullValue
- **Type**: typing.Optional[bool]


# Dashboard

### DashboardId
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DashboardVersion]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastPublishedTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### LinkEntities
- **Type**: typing.Optional[typing.List[str]]


# DashboardError

### Type
- **Type**: typing.Optional[typing.Literal['ACCESS_DENIED', 'COLUMN_GEOGRAPHIC_ROLE_MISMATCH', 'COLUMN_REPLACEMENT_MISSING', 'COLUMN_TYPE_MISMATCH', 'DATA_SET_NOT_FOUND', 'INTERNAL_FAILURE', 'PARAMETER_NOT_FOUND', 'PARAMETER_TYPE_INVALID', 'PARAMETER_VALUE_INCOMPATIBLE', 'SOURCE_NOT_FOUND']]

### Message
- **Type**: typing.Optional[str]

### ViolatedEntities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Entity]]


# DashboardPublishOptions

### AdHocFilteringOption
- **Type**: <class 'NoneType'>

### ExportToCSVOption
- **Type**: <class 'NoneType'>

### SheetControlsOption
- **Type**: <class 'NoneType'>

### VisualPublishOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DashboardVisualPublishOptions]

### SheetLayoutElementMaximizationOption
- **Type**: <class 'NoneType'>

### VisualMenuOption
- **Type**: <class 'NoneType'>

### VisualAxisSortOption
- **Type**: <class 'NoneType'>

### ExportWithHiddenFieldsOption
- **Type**: <class 'NoneType'>

### DataPointDrillUpDownOption
- **Type**: <class 'NoneType'>

### DataPointMenuLabelOption
- **Type**: <class 'NoneType'>

### DataPointTooltipOption
- **Type**: <class 'NoneType'>


# DashboardSearchFilter

### Operator
- **Type**: typing.Literal['StringEquals', 'StringLike']
- **Required**: Yes

### Name
- **Type**: typing.Optional[typing.Literal['DASHBOARD_NAME', 'DIRECT_QUICKSIGHT_OWNER', 'DIRECT_QUICKSIGHT_SOLE_OWNER', 'DIRECT_QUICKSIGHT_VIEWER_OR_OWNER', 'QUICKSIGHT_OWNER', 'QUICKSIGHT_USER', 'QUICKSIGHT_VIEWER_OR_OWNER']]

### Value
- **Type**: typing.Optional[str]


# DashboardSourceEntity

### SourceTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DashboardSourceTemplate]


# DashboardSourceTemplate

### DataSetReferences
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataSetReference]
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# DashboardSummary

### Arn
- **Type**: typing.Optional[str]

### DashboardId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### PublishedVersionNumber
- **Type**: typing.Optional[int]

### LastPublishedTime
- **Type**: typing.Optional[datetime.datetime]


# DashboardVersion

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### Errors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DashboardError]]

### VersionNumber
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['CREATION_FAILED', 'CREATION_IN_PROGRESS', 'CREATION_SUCCESSFUL', 'DELETED', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']]

### Arn
- **Type**: typing.Optional[str]

### SourceEntityArn
- **Type**: typing.Optional[str]

### DataSetArns
- **Type**: typing.Optional[typing.List[str]]

### Description
- **Type**: typing.Optional[str]

### ThemeArn
- **Type**: typing.Optional[str]

### Sheets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Sheet]]


# DashboardVersionDefinition

### DataSetIdentifierDeclarations
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataSetIdentifierDeclaration]
- **Required**: Yes

### Sheets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SheetDefinition]]

### CalculatedFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CalculatedField]]

### ParameterDeclarations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ParameterDeclaration]]

### FilterGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterGroup]]

### ColumnConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnConfiguration]]

### AnalysisDefaults
- **Type**: <class 'NoneType'>

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetOptions]

### StaticFiles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.StaticFile]]


# DashboardVersionDefinitionOutput

### DataSetIdentifierDeclarations
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataSetIdentifierDeclaration]
- **Required**: Yes

### Sheets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SheetDefinitionOutput]]

### CalculatedFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CalculatedField]]

### ParameterDeclarations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ParameterDeclarationOutput]]

### FilterGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterGroupOutput]]

### ColumnConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnConfigurationOutput]]

### AnalysisDefaults
- **Type**: <class 'NoneType'>

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetOptions]

### StaticFiles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.StaticFile]]


# DashboardVersionSummary

### Arn
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### VersionNumber
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['CREATION_FAILED', 'CREATION_IN_PROGRESS', 'CREATION_SUCCESSFUL', 'DELETED', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']]

### SourceEntityArn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# DashboardVisualId

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### SheetId
- **Type**: <class 'str'>
- **Required**: Yes

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes


# DashboardVisualPublishOptions

### ExportHiddenFieldsOption
- **Type**: <class 'NoneType'>


# DashboardVisualResult

### DashboardId
- **Type**: typing.Optional[str]

### DashboardName
- **Type**: typing.Optional[str]

### SheetId
- **Type**: typing.Optional[str]

### SheetName
- **Type**: typing.Optional[str]

### VisualId
- **Type**: typing.Optional[str]

### VisualTitle
- **Type**: typing.Optional[str]

### VisualSubtitle
- **Type**: typing.Optional[str]

### DashboardUrl
- **Type**: typing.Optional[str]


# DataAggregation

### DatasetRowDateGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### DefaultDateColumnName
- **Type**: typing.Optional[str]


# DataBarsOptions

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### PositiveColor
- **Type**: typing.Optional[str]

### NegativeColor
- **Type**: typing.Optional[str]


# DataColor

### Color
- **Type**: typing.Optional[str]

### DataValue
- **Type**: typing.Optional[float]


# DataColorPalette

### Colors
- **Type**: typing.Optional[typing.List[str]]

### MinMaxGradient
- **Type**: typing.Optional[typing.List[str]]

### EmptyFillColor
- **Type**: typing.Optional[str]


# DataColorPaletteOutput

### Colors
- **Type**: typing.Optional[typing.List[str]]

### MinMaxGradient
- **Type**: typing.Optional[typing.List[str]]

### EmptyFillColor
- **Type**: typing.Optional[str]


# DataFieldSeriesItem

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### AxisBinding
- **Type**: typing.Literal['PRIMARY_YAXIS', 'SECONDARY_YAXIS']
- **Required**: Yes

### FieldValue
- **Type**: typing.Optional[str]

### Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LineChartSeriesSettings]


# DataLabelOptions

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### CategoryLabelVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### MeasureLabelVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### DataLabelTypes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataLabelType]]

### Position
- **Type**: typing.Optional[typing.Literal['BOTTOM', 'INSIDE', 'LEFT', 'OUTSIDE', 'RIGHT', 'TOP']]

### LabelContent
- **Type**: typing.Optional[typing.Literal['PERCENT', 'VALUE', 'VALUE_AND_PERCENT']]

### LabelFontConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FontConfiguration]

### LabelColor
- **Type**: typing.Optional[str]

### Overlap
- **Type**: typing.Optional[typing.Literal['DISABLE_OVERLAP', 'ENABLE_OVERLAP']]

### TotalsVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# DataLabelOptionsOutput

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### CategoryLabelVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### MeasureLabelVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### DataLabelTypes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataLabelType]]

### Position
- **Type**: typing.Optional[typing.Literal['BOTTOM', 'INSIDE', 'LEFT', 'OUTSIDE', 'RIGHT', 'TOP']]

### LabelContent
- **Type**: typing.Optional[typing.Literal['PERCENT', 'VALUE', 'VALUE_AND_PERCENT']]

### LabelFontConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FontConfiguration]

### LabelColor
- **Type**: typing.Optional[str]

### Overlap
- **Type**: typing.Optional[typing.Literal['DISABLE_OVERLAP', 'ENABLE_OVERLAP']]

### TotalsVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# DataLabelType

### FieldLabelType
- **Type**: <class 'NoneType'>

### DataPathLabelType
- **Type**: <class 'NoneType'>

### RangeEndsLabelType
- **Type**: <class 'NoneType'>

### MinimumLabelType
- **Type**: <class 'NoneType'>

### MaximumLabelType
- **Type**: <class 'NoneType'>


# DataPathColor

### Element
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataPathValue'>
- **Required**: Yes

### Color
- **Type**: <class 'str'>
- **Required**: Yes

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]


# DataPathLabelType

### FieldId
- **Type**: typing.Optional[str]

### FieldValue
- **Type**: typing.Optional[str]

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# DataPathSort

### Direction
- **Type**: typing.Literal['ASC', 'DESC']
- **Required**: Yes

### SortPaths
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataPathValue]
- **Required**: Yes


# DataPathSortOutput

### Direction
- **Type**: typing.Literal['ASC', 'DESC']
- **Required**: Yes

### SortPaths
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataPathValue]
- **Required**: Yes


# DataPathType

### PivotTableDataPathType
- **Type**: typing.Optional[typing.Literal['COUNT_METRIC_COLUMN', 'EMPTY_COLUMN_HEADER', 'HIERARCHY_ROWS_LAYOUT_COLUMN', 'MULTIPLE_ROW_METRICS_COLUMN']]


# DataPathValue

### FieldId
- **Type**: typing.Optional[str]

### FieldValue
- **Type**: typing.Optional[str]

### DataPathType
- **Type**: <class 'NoneType'>


# DataPointDrillUpDownOption

### AvailabilityStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# DataPointMenuLabelOption

### AvailabilityStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# DataPointTooltipOption

### AvailabilityStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# DataSet

### Arn
- **Type**: typing.Optional[str]

### DataSetId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### PhysicalTableMap
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PhysicalTableOutput]]

### LogicalTableMap
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LogicalTableOutput]]

### OutputColumns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.OutputColumn]]

### ImportMode
- **Type**: typing.Optional[typing.Literal['DIRECT_QUERY', 'SPICE']]

### ConsumedSpiceCapacityInBytes
- **Type**: typing.Optional[int]

### ColumnGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnGroupOutput]]

### FieldFolders
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldFolderOutput]]

### RowLevelPermissionDataSet
- **Type**: <class 'NoneType'>

### RowLevelPermissionTagConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RowLevelPermissionTagConfigurationOutput]

### ColumnLevelPermissionRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnLevelPermissionRuleOutput]]

### DataSetUsageConfiguration
- **Type**: <class 'NoneType'>

### DatasetParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DatasetParameterOutput]]

### PerformanceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PerformanceConfigurationOutput]


# DataSetConfiguration

### Placeholder
- **Type**: typing.Optional[str]

### DataSetSchema
- **Type**: <class 'NoneType'>

### ColumnGroupSchemaList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnGroupSchema]]


# DataSetConfigurationOutput

### Placeholder
- **Type**: typing.Optional[str]

### DataSetSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataSetSchemaOutput]

### ColumnGroupSchemaList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnGroupSchemaOutput]]


# DataSetIdentifierDeclaration

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DataSetReference

### DataSetPlaceholder
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DataSetRefreshProperties

### RefreshConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RefreshConfiguration'>
- **Required**: Yes


# DataSetSchema

### ColumnSchemaList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnSchema]]


# DataSetSchemaOutput

### ColumnSchemaList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnSchema]]


# DataSetSearchFilter

### Operator
- **Type**: typing.Literal['StringEquals', 'StringLike']
- **Required**: Yes

### Name
- **Type**: typing.Literal['DATASET_NAME', 'DIRECT_QUICKSIGHT_OWNER', 'DIRECT_QUICKSIGHT_SOLE_OWNER', 'DIRECT_QUICKSIGHT_VIEWER_OR_OWNER', 'QUICKSIGHT_OWNER', 'QUICKSIGHT_VIEWER_OR_OWNER']
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# DataSetSummary

### Arn
- **Type**: typing.Optional[str]

### DataSetId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### ImportMode
- **Type**: typing.Optional[typing.Literal['DIRECT_QUERY', 'SPICE']]

### RowLevelPermissionDataSet
- **Type**: <class 'NoneType'>

### RowLevelPermissionTagConfigurationApplied
- **Type**: typing.Optional[bool]

### ColumnLevelPermissionRulesApplied
- **Type**: typing.Optional[bool]


# DataSetUsageConfiguration

### DisableUseAsDirectQuerySource
- **Type**: typing.Optional[bool]

### DisableUseAsImportedSource
- **Type**: typing.Optional[bool]


# DataSource

### Arn
- **Type**: typing.Optional[str]

### DataSourceId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['ADOBE_ANALYTICS', 'AMAZON_ELASTICSEARCH', 'AMAZON_OPENSEARCH', 'ATHENA', 'AURORA', 'AURORA_POSTGRESQL', 'AWS_IOT_ANALYTICS', 'BIGQUERY', 'DATABRICKS', 'EXASOL', 'GITHUB', 'JIRA', 'MARIADB', 'MYSQL', 'ORACLE', 'POSTGRESQL', 'PRESTO', 'REDSHIFT', 'S3', 'SALESFORCE', 'SERVICENOW', 'SNOWFLAKE', 'SPARK', 'SQLSERVER', 'STARBURST', 'TERADATA', 'TIMESTREAM', 'TRINO', 'TWITTER']]

### Status
- **Type**: typing.Optional[typing.Literal['CREATION_FAILED', 'CREATION_IN_PROGRESS', 'CREATION_SUCCESSFUL', 'DELETED', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### DataSourceParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataSourceParametersOutput]

### AlternateDataSourceParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataSourceParametersOutput]]

### VpcConnectionProperties
- **Type**: <class 'NoneType'>

### SslProperties
- **Type**: <class 'NoneType'>

### ErrorInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataSourceErrorInfo]

### SecretArn
- **Type**: typing.Optional[str]


# DataSourceCredentials

### CredentialPair
- **Type**: <class 'NoneType'>

### CopySourceArn
- **Type**: typing.Optional[str]

### SecretArn
- **Type**: typing.Optional[str]


# DataSourceErrorInfo

### Type
- **Type**: typing.Optional[typing.Literal['ACCESS_DENIED', 'CONFLICT', 'COPY_SOURCE_NOT_FOUND', 'ENGINE_VERSION_NOT_SUPPORTED', 'GENERIC_SQL_FAILURE', 'TIMEOUT', 'UNKNOWN', 'UNKNOWN_HOST']]

### Message
- **Type**: typing.Optional[str]


# DataSourceParameters

### AmazonElasticsearchParameters
- **Type**: <class 'NoneType'>

### AthenaParameters
- **Type**: <class 'NoneType'>

### AuroraParameters
- **Type**: <class 'NoneType'>

### AuroraPostgreSqlParameters
- **Type**: <class 'NoneType'>

### AwsIotAnalyticsParameters
- **Type**: <class 'NoneType'>

### JiraParameters
- **Type**: <class 'NoneType'>

### MariaDbParameters
- **Type**: <class 'NoneType'>

### MySqlParameters
- **Type**: <class 'NoneType'>

### OracleParameters
- **Type**: <class 'NoneType'>

### PostgreSqlParameters
- **Type**: <class 'NoneType'>

### PrestoParameters
- **Type**: <class 'NoneType'>

### RdsParameters
- **Type**: <class 'NoneType'>

### RedshiftParameters
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RedshiftParameters, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RedshiftParametersOutput, NoneType]

### S3Parameters
- **Type**: <class 'NoneType'>

### ServiceNowParameters
- **Type**: <class 'NoneType'>

### SnowflakeParameters
- **Type**: <class 'NoneType'>

### SparkParameters
- **Type**: <class 'NoneType'>

### SqlServerParameters
- **Type**: <class 'NoneType'>

### TeradataParameters
- **Type**: <class 'NoneType'>

### TwitterParameters
- **Type**: <class 'NoneType'>

### AmazonOpenSearchParameters
- **Type**: <class 'NoneType'>

### ExasolParameters
- **Type**: <class 'NoneType'>

### DatabricksParameters
- **Type**: <class 'NoneType'>

### StarburstParameters
- **Type**: <class 'NoneType'>

### TrinoParameters
- **Type**: <class 'NoneType'>

### BigQueryParameters
- **Type**: <class 'NoneType'>


# DataSourceParametersOutput

### AmazonElasticsearchParameters
- **Type**: <class 'NoneType'>

### AthenaParameters
- **Type**: <class 'NoneType'>

### AuroraParameters
- **Type**: <class 'NoneType'>

### AuroraPostgreSqlParameters
- **Type**: <class 'NoneType'>

### AwsIotAnalyticsParameters
- **Type**: <class 'NoneType'>

### JiraParameters
- **Type**: <class 'NoneType'>

### MariaDbParameters
- **Type**: <class 'NoneType'>

### MySqlParameters
- **Type**: <class 'NoneType'>

### OracleParameters
- **Type**: <class 'NoneType'>

### PostgreSqlParameters
- **Type**: <class 'NoneType'>

### PrestoParameters
- **Type**: <class 'NoneType'>

### RdsParameters
- **Type**: <class 'NoneType'>

### RedshiftParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RedshiftParametersOutput]

### S3Parameters
- **Type**: <class 'NoneType'>

### ServiceNowParameters
- **Type**: <class 'NoneType'>

### SnowflakeParameters
- **Type**: <class 'NoneType'>

### SparkParameters
- **Type**: <class 'NoneType'>

### SqlServerParameters
- **Type**: <class 'NoneType'>

### TeradataParameters
- **Type**: <class 'NoneType'>

### TwitterParameters
- **Type**: <class 'NoneType'>

### AmazonOpenSearchParameters
- **Type**: <class 'NoneType'>

### ExasolParameters
- **Type**: <class 'NoneType'>

### DatabricksParameters
- **Type**: <class 'NoneType'>

### StarburstParameters
- **Type**: <class 'NoneType'>

### TrinoParameters
- **Type**: <class 'NoneType'>

### BigQueryParameters
- **Type**: <class 'NoneType'>


# DataSourceSearchFilter

### Operator
- **Type**: typing.Literal['StringEquals', 'StringLike']
- **Required**: Yes

### Name
- **Type**: typing.Literal['DATASOURCE_NAME', 'DIRECT_QUICKSIGHT_OWNER', 'DIRECT_QUICKSIGHT_SOLE_OWNER', 'DIRECT_QUICKSIGHT_VIEWER_OR_OWNER']
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# DataSourceSummary

### Arn
- **Type**: typing.Optional[str]

### DataSourceId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['ADOBE_ANALYTICS', 'AMAZON_ELASTICSEARCH', 'AMAZON_OPENSEARCH', 'ATHENA', 'AURORA', 'AURORA_POSTGRESQL', 'AWS_IOT_ANALYTICS', 'BIGQUERY', 'DATABRICKS', 'EXASOL', 'GITHUB', 'JIRA', 'MARIADB', 'MYSQL', 'ORACLE', 'POSTGRESQL', 'PRESTO', 'REDSHIFT', 'S3', 'SALESFORCE', 'SERVICENOW', 'SNOWFLAKE', 'SPARK', 'SQLSERVER', 'STARBURST', 'TERADATA', 'TIMESTREAM', 'TRINO', 'TWITTER']]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]


# DatabricksParameters

### Host
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes

### SqlEndpointPath
- **Type**: <class 'str'>
- **Required**: Yes


# DatasetMetadata

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetName
- **Type**: typing.Optional[str]

### DatasetDescription
- **Type**: typing.Optional[str]

### DataAggregation
- **Type**: <class 'NoneType'>

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicFilter]]

### Columns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicColumn]]

### CalculatedFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicCalculatedField]]

### NamedEntities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicNamedEntity]]


# DatasetMetadataOutput

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetName
- **Type**: typing.Optional[str]

### DatasetDescription
- **Type**: typing.Optional[str]

### DataAggregation
- **Type**: <class 'NoneType'>

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicFilterOutput]]

### Columns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicColumnOutput]]

### CalculatedFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicCalculatedFieldOutput]]

### NamedEntities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicNamedEntityOutput]]


# DatasetParameter

### StringDatasetParameter
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.StringDatasetParameter, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.StringDatasetParameterOutput, NoneType]

### DecimalDatasetParameter
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DecimalDatasetParameter, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DecimalDatasetParameterOutput, NoneType]

### IntegerDatasetParameter
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.IntegerDatasetParameter, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.IntegerDatasetParameterOutput, NoneType]

### DateTimeDatasetParameter
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DateTimeDatasetParameter, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DateTimeDatasetParameterOutput, NoneType]


# DatasetParameterOutput

### StringDatasetParameter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.StringDatasetParameterOutput]

### DecimalDatasetParameter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DecimalDatasetParameterOutput]

### IntegerDatasetParameter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.IntegerDatasetParameterOutput]

### DateTimeDatasetParameter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DateTimeDatasetParameterOutput]


# DateAxisOptions

### MissingDateVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# DateDimensionField

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### DateGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### HierarchyId
- **Type**: typing.Optional[str]

### FormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DateTimeFormatConfiguration]


# DateMeasureField

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### AggregationFunction
- **Type**: typing.Optional[typing.Literal['COUNT', 'DISTINCT_COUNT', 'MAX', 'MIN']]

### FormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DateTimeFormatConfiguration]


# DateTimeDatasetParameter

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ValueType
- **Type**: typing.Literal['MULTI_VALUED', 'SINGLE_VALUED']
- **Required**: Yes

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### DefaultValues
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DateTimeDatasetParameterDefaultValues, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DateTimeDatasetParameterDefaultValuesOutput, NoneType]


# DateTimeDatasetParameterDefaultValues

### StaticValues
- **Type**: typing.Optional[typing.List[typing.Union[datetime.datetime, str]]]


# DateTimeDatasetParameterDefaultValuesOutput

### StaticValues
- **Type**: typing.Optional[typing.List[datetime.datetime]]


# DateTimeDatasetParameterOutput

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ValueType
- **Type**: typing.Literal['MULTI_VALUED', 'SINGLE_VALUED']
- **Required**: Yes

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### DefaultValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DateTimeDatasetParameterDefaultValuesOutput]


# DateTimeDefaultValues

### DynamicValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DynamicDefaultValue]

### StaticValues
- **Type**: typing.Optional[typing.List[typing.Union[datetime.datetime, str]]]

### RollingDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RollingDateConfiguration]


# DateTimeDefaultValuesOutput

### DynamicValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DynamicDefaultValue]

### StaticValues
- **Type**: typing.Optional[typing.List[datetime.datetime]]

### RollingDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RollingDateConfiguration]


# DateTimeFormatConfiguration

### DateTimeFormat
- **Type**: typing.Optional[str]

### NullValueFormatConfiguration
- **Type**: <class 'NoneType'>

### NumericFormatConfiguration
- **Type**: <class 'NoneType'>


# DateTimeHierarchy

### HierarchyId
- **Type**: <class 'str'>
- **Required**: Yes

### DrillDownFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DrillDownFilter]]


# DateTimeHierarchyOutput

### HierarchyId
- **Type**: <class 'str'>
- **Required**: Yes

### DrillDownFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DrillDownFilterOutput]]


# DateTimeParameter

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.List[typing.Union[datetime.datetime, str]]
- **Required**: Yes


# DateTimeParameterDeclaration

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DateTimeDefaultValues]

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### ValueWhenUnset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DateTimeValueWhenUnsetConfiguration]

### MappedDataSetParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MappedDataSetParameter]]


# DateTimeParameterDeclarationOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DateTimeDefaultValuesOutput]

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### ValueWhenUnset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DateTimeValueWhenUnsetConfigurationOutput]

### MappedDataSetParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MappedDataSetParameter]]


# DateTimeParameterOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.List[datetime.datetime]
- **Required**: Yes


# DateTimePickerControlDisplayOptions

### TitleOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LabelOptions]

### DateTimeFormat
- **Type**: typing.Optional[str]

### InfoIconLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SheetControlInfoIconLabelOptions]

### HelperTextVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### DateIconVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# DateTimeValueWhenUnsetConfiguration

### ValueWhenUnsetOption
- **Type**: typing.Optional[typing.Literal['NULL', 'RECOMMENDED_VALUE']]

### CustomValue
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# DateTimeValueWhenUnsetConfigurationOutput

### ValueWhenUnsetOption
- **Type**: typing.Optional[typing.Literal['NULL', 'RECOMMENDED_VALUE']]

### CustomValue
- **Type**: typing.Optional[datetime.datetime]


# DecimalDatasetParameter

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ValueType
- **Type**: typing.Literal['MULTI_VALUED', 'SINGLE_VALUED']
- **Required**: Yes

### DefaultValues
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DecimalDatasetParameterDefaultValues, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DecimalDatasetParameterDefaultValuesOutput, NoneType]


# DecimalDatasetParameterDefaultValues

### StaticValues
- **Type**: typing.Optional[typing.List[float]]


# DecimalDatasetParameterDefaultValuesOutput

### StaticValues
- **Type**: typing.Optional[typing.List[float]]


# DecimalDatasetParameterOutput

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ValueType
- **Type**: typing.Literal['MULTI_VALUED', 'SINGLE_VALUED']
- **Required**: Yes

### DefaultValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DecimalDatasetParameterDefaultValuesOutput]


# DecimalDefaultValues

### DynamicValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DynamicDefaultValue]

### StaticValues
- **Type**: typing.Optional[typing.List[float]]


# DecimalDefaultValuesOutput

### DynamicValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DynamicDefaultValue]

### StaticValues
- **Type**: typing.Optional[typing.List[float]]


# DecimalParameter

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.List[float]
- **Required**: Yes


# DecimalParameterDeclaration

### ParameterValueType
- **Type**: typing.Literal['MULTI_VALUED', 'SINGLE_VALUED']
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DecimalDefaultValues]

### ValueWhenUnset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DecimalValueWhenUnsetConfiguration]

### MappedDataSetParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MappedDataSetParameter]]


# DecimalParameterDeclarationOutput

### ParameterValueType
- **Type**: typing.Literal['MULTI_VALUED', 'SINGLE_VALUED']
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DecimalDefaultValuesOutput]

### ValueWhenUnset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DecimalValueWhenUnsetConfiguration]

### MappedDataSetParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MappedDataSetParameter]]


# DecimalParameterOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.List[float]
- **Required**: Yes


# DecimalPlacesConfiguration

### DecimalPlaces
- **Type**: <class 'int'>
- **Required**: Yes


# DecimalValueWhenUnsetConfiguration

### ValueWhenUnsetOption
- **Type**: typing.Optional[typing.Literal['NULL', 'RECOMMENDED_VALUE']]

### CustomValue
- **Type**: typing.Optional[float]


# DefaultDateTimePickerControlOptions

### Type
- **Type**: typing.Optional[typing.Literal['DATE_RANGE', 'SINGLE_VALUED']]

### DisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DateTimePickerControlDisplayOptions]

### CommitMode
- **Type**: typing.Optional[typing.Literal['AUTO', 'MANUAL']]


# DefaultFilterControlConfiguration

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### ControlOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DefaultFilterControlOptions'>
- **Required**: Yes


# DefaultFilterControlConfigurationOutput

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### ControlOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DefaultFilterControlOptionsOutput'>
- **Required**: Yes


# DefaultFilterControlOptions

### DefaultDateTimePickerOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DefaultDateTimePickerControlOptions]

### DefaultListOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DefaultFilterListControlOptions]

### DefaultDropdownOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DefaultFilterDropDownControlOptions]

### DefaultTextFieldOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DefaultTextFieldControlOptions]

### DefaultTextAreaOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DefaultTextAreaControlOptions]

### DefaultSliderOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DefaultSliderControlOptions]

### DefaultRelativeDateTimeOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DefaultRelativeDateTimeControlOptions]


# DefaultFilterControlOptionsOutput

### DefaultDateTimePickerOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DefaultDateTimePickerControlOptions]

### DefaultListOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DefaultFilterListControlOptionsOutput]

### DefaultDropdownOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DefaultFilterDropDownControlOptionsOutput]

### DefaultTextFieldOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DefaultTextFieldControlOptions]

### DefaultTextAreaOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DefaultTextAreaControlOptions]

### DefaultSliderOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DefaultSliderControlOptions]

### DefaultRelativeDateTimeOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DefaultRelativeDateTimeControlOptions]


# DefaultFilterDropDownControlOptions

### DisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DropDownControlDisplayOptions]

### Type
- **Type**: typing.Optional[typing.Literal['MULTI_SELECT', 'SINGLE_SELECT']]

### SelectableValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterSelectableValues]

### CommitMode
- **Type**: typing.Optional[typing.Literal['AUTO', 'MANUAL']]


# DefaultFilterDropDownControlOptionsOutput

### DisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DropDownControlDisplayOptions]

### Type
- **Type**: typing.Optional[typing.Literal['MULTI_SELECT', 'SINGLE_SELECT']]

### SelectableValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterSelectableValuesOutput]

### CommitMode
- **Type**: typing.Optional[typing.Literal['AUTO', 'MANUAL']]


# DefaultFilterListControlOptions

### DisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ListControlDisplayOptions]

### Type
- **Type**: typing.Optional[typing.Literal['MULTI_SELECT', 'SINGLE_SELECT']]

### SelectableValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterSelectableValues]


# DefaultFilterListControlOptionsOutput

### DisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ListControlDisplayOptions]

### Type
- **Type**: typing.Optional[typing.Literal['MULTI_SELECT', 'SINGLE_SELECT']]

### SelectableValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterSelectableValuesOutput]


# DefaultFormatting

### DisplayFormat
- **Type**: typing.Optional[typing.Literal['AUTO', 'CURRENCY', 'DATE', 'NUMBER', 'PERCENT', 'STRING']]

### DisplayFormatOptions
- **Type**: <class 'NoneType'>


# DefaultFreeFormLayoutConfiguration

### CanvasSizeOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FreeFormLayoutCanvasSizeOptions'>
- **Required**: Yes


# DefaultGridLayoutConfiguration

### CanvasSizeOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GridLayoutCanvasSizeOptions'>
- **Required**: Yes


# DefaultInteractiveLayoutConfiguration

### Grid
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DefaultGridLayoutConfiguration]

### FreeForm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DefaultFreeFormLayoutConfiguration]


# DefaultNewSheetConfiguration

### InteractiveLayoutConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DefaultInteractiveLayoutConfiguration]

### PaginatedLayoutConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DefaultPaginatedLayoutConfiguration]

### SheetContentType
- **Type**: typing.Optional[typing.Literal['INTERACTIVE', 'PAGINATED']]


# DefaultPaginatedLayoutConfiguration

### SectionBased
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DefaultSectionBasedLayoutConfiguration]


# DefaultRelativeDateTimeControlOptions

### DisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RelativeDateTimeControlDisplayOptions]

### CommitMode
- **Type**: typing.Optional[typing.Literal['AUTO', 'MANUAL']]


# DefaultSectionBasedLayoutConfiguration

### CanvasSizeOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SectionBasedLayoutCanvasSizeOptions'>
- **Required**: Yes


# DefaultSliderControlOptions

### MaximumValue
- **Type**: <class 'float'>
- **Required**: Yes

### MinimumValue
- **Type**: <class 'float'>
- **Required**: Yes

### StepSize
- **Type**: <class 'float'>
- **Required**: Yes

### DisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SliderControlDisplayOptions]

### Type
- **Type**: typing.Optional[typing.Literal['RANGE', 'SINGLE_POINT']]


# DefaultTextAreaControlOptions

### Delimiter
- **Type**: typing.Optional[str]

### DisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TextAreaControlDisplayOptions]


# DefaultTextFieldControlOptions

### DisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TextFieldControlDisplayOptions]


# DeleteAccountCustomizationRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: typing.Optional[str]


# DeleteAccountCustomizationResponse

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAccountSubscriptionRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAccountSubscriptionResponse

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAnalysisRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AnalysisId
- **Type**: <class 'str'>
- **Required**: Yes

### RecoveryWindowInDays
- **Type**: typing.Optional[int]

### ForceDeleteWithoutRecovery
- **Type**: typing.Optional[bool]


# DeleteAnalysisResponse

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AnalysisId
- **Type**: <class 'str'>
- **Required**: Yes

### DeletionTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteBrandAssignmentRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBrandAssignmentResponse

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteBrandRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BrandId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBrandResponse

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteCustomPermissionsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### CustomPermissionsName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCustomPermissionsResponse

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDashboardRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: typing.Optional[int]


# DeleteDashboardResponse

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDataSetRefreshPropertiesRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataSetRefreshPropertiesResponse

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDataSetRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataSetResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDataSourceRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataSourceResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDefaultQBusinessApplicationRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: typing.Optional[str]


# DeleteDefaultQBusinessApplicationResponse

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteFolderMembershipRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberType
- **Type**: typing.Literal['ANALYSIS', 'DASHBOARD', 'DATASET', 'DATASOURCE', 'TOPIC']
- **Required**: Yes


# DeleteFolderMembershipResponse

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteFolderRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFolderResponse

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteGroupMembershipRequest

### MemberName
- **Type**: <class 'str'>
- **Required**: Yes

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGroupMembershipResponse

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteGroupRequest

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGroupResponse

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteIAMPolicyAssignmentRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AssignmentName
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIAMPolicyAssignmentResponse

### AssignmentName
- **Type**: <class 'str'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteIdentityPropagationConfigRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Service
- **Type**: typing.Literal['QBUSINESS', 'REDSHIFT']
- **Required**: Yes


# DeleteIdentityPropagationConfigResponse

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteNamespaceRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNamespaceResponse

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteRefreshScheduleRequest

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRefreshScheduleResponse

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleId
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteRoleCustomPermissionRequest

### Role
- **Type**: typing.Literal['ADMIN', 'ADMIN_PRO', 'AUTHOR', 'AUTHOR_PRO', 'READER', 'READER_PRO']
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRoleCustomPermissionResponse

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteRoleMembershipRequest

### MemberName
- **Type**: <class 'str'>
- **Required**: Yes

### Role
- **Type**: typing.Literal['ADMIN', 'ADMIN_PRO', 'AUTHOR', 'AUTHOR_PRO', 'READER', 'READER_PRO']
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRoleMembershipResponse

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteTemplateAliasRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### AliasName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTemplateAliasResponse

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### AliasName
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteTemplateRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: typing.Optional[int]


# DeleteTemplateResponse

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteThemeAliasRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ThemeId
- **Type**: <class 'str'>
- **Required**: Yes

### AliasName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteThemeAliasResponse

### AliasName
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ThemeId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteThemeRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ThemeId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: typing.Optional[int]


# DeleteThemeResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ThemeId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteTopicRefreshScheduleRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTopicRefreshScheduleResponse

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteTopicRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTopicResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteUserByPrincipalIdRequest

### PrincipalId
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserByPrincipalIdResponse

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteUserCustomPermissionRequest

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserCustomPermissionResponse

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteUserRequest

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserResponse

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteVPCConnectionRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### VPCConnectionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVPCConnectionResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### VPCConnectionId
- **Type**: <class 'str'>
- **Required**: Yes

### DeletionStatus
- **Type**: typing.Literal['CREATION_FAILED', 'CREATION_IN_PROGRESS', 'CREATION_SUCCESSFUL', 'DELETED', 'DELETION_FAILED', 'DELETION_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']
- **Required**: Yes

### AvailabilityStatus
- **Type**: typing.Literal['AVAILABLE', 'PARTIALLY_AVAILABLE', 'UNAVAILABLE']
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAccountCustomizationRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: typing.Optional[str]

### Resolved
- **Type**: typing.Optional[bool]


# DescribeAccountCustomizationResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### AccountCustomization
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AccountCustomization'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAccountSettingsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAccountSettingsResponse

### AccountSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AccountSettings'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAccountSubscriptionRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAccountSubscriptionResponse

### AccountInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AccountInfo'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAnalysisDefinitionRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AnalysisId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAnalysisDefinitionResponse

### AnalysisId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AnalysisError]
- **Required**: Yes

### ResourceStatus
- **Type**: typing.Literal['CREATION_FAILED', 'CREATION_IN_PROGRESS', 'CREATION_SUCCESSFUL', 'DELETED', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']
- **Required**: Yes

### ThemeArn
- **Type**: <class 'str'>
- **Required**: Yes

### Definition
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AnalysisDefinitionOutput'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAnalysisPermissionsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AnalysisId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAnalysisPermissionsResponse

### AnalysisId
- **Type**: <class 'str'>
- **Required**: Yes

### AnalysisArn
- **Type**: <class 'str'>
- **Required**: Yes

### Permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAnalysisRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AnalysisId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAnalysisResponse

### Analysis
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Analysis'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAssetBundleExportJobRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AssetBundleExportJobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAssetBundleExportJobResponse

### JobStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'QUEUED_FOR_IMMEDIATE_EXECUTION', 'SUCCESSFUL']
- **Required**: Yes

### DownloadUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleExportJobError]
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AssetBundleExportJobId
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArns
- **Type**: typing.List[str]
- **Required**: Yes

### IncludeAllDependencies
- **Type**: <class 'bool'>
- **Required**: Yes

### ExportFormat
- **Type**: typing.Literal['CLOUDFORMATION_JSON', 'QUICKSIGHT_JSON']
- **Required**: Yes

### CloudFormationOverridePropertyConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleCloudFormationOverridePropertyConfigurationOutput'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### IncludePermissions
- **Type**: <class 'bool'>
- **Required**: Yes

### IncludeTags
- **Type**: <class 'bool'>
- **Required**: Yes

### ValidationStrategy
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleExportJobValidationStrategy'>
- **Required**: Yes

### Warnings
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleExportJobWarning]
- **Required**: Yes

### IncludeFolderMemberships
- **Type**: <class 'bool'>
- **Required**: Yes

### IncludeFolderMembers
- **Type**: typing.Literal['NONE', 'ONE_LEVEL', 'RECURSE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAssetBundleImportJobRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AssetBundleImportJobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAssetBundleImportJobResponse

### JobStatus
- **Type**: typing.Literal['FAILED', 'FAILED_ROLLBACK_COMPLETED', 'FAILED_ROLLBACK_ERROR', 'FAILED_ROLLBACK_IN_PROGRESS', 'IN_PROGRESS', 'QUEUED_FOR_IMMEDIATE_EXECUTION', 'SUCCESSFUL']
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobError]
- **Required**: Yes

### RollbackErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobError]
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AssetBundleImportJobId
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AssetBundleImportSource
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportSourceDescription'>
- **Required**: Yes

### OverrideParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobOverrideParametersOutput'>
- **Required**: Yes

### FailureAction
- **Type**: typing.Literal['DO_NOTHING', 'ROLLBACK']
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### OverridePermissions
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobOverridePermissionsOutput'>
- **Required**: Yes

### OverrideTags
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobOverrideTagsOutput'>
- **Required**: Yes

### OverrideValidationStrategy
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobOverrideValidationStrategy'>
- **Required**: Yes

### Warnings
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobWarning]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeBrandAssignmentRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBrandAssignmentResponse

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### BrandArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeBrandPublishedVersionRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BrandId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBrandPublishedVersionResponse

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### BrandDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BrandDetail'>
- **Required**: Yes

### BrandDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BrandDefinition'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeBrandRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BrandId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: typing.Optional[str]


# DescribeBrandResponse

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### BrandDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BrandDetail'>
- **Required**: Yes

### BrandDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BrandDefinition'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeCustomPermissionsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### CustomPermissionsName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCustomPermissionsResponse

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### CustomPermissions
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CustomPermissions'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDashboardDefinitionRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: typing.Optional[int]

### AliasName
- **Type**: typing.Optional[str]


# DescribeDashboardDefinitionResponse

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DashboardError]
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceStatus
- **Type**: typing.Literal['CREATION_FAILED', 'CREATION_IN_PROGRESS', 'CREATION_SUCCESSFUL', 'DELETED', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']
- **Required**: Yes

### ThemeArn
- **Type**: <class 'str'>
- **Required**: Yes

### Definition
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DashboardVersionDefinitionOutput'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardPublishOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DashboardPublishOptions'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDashboardPermissionsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDashboardPermissionsResponse

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardArn
- **Type**: <class 'str'>
- **Required**: Yes

### Permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### LinkSharingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LinkSharingConfigurationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDashboardRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: typing.Optional[int]

### AliasName
- **Type**: typing.Optional[str]


# DescribeDashboardResponse

### Dashboard
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Dashboard'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDashboardSnapshotJobRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotJobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDashboardSnapshotJobResponse

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotJobId
- **Type**: <class 'str'>
- **Required**: Yes

### UserConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SnapshotUserConfigurationRedacted'>
- **Required**: Yes

### SnapshotConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SnapshotConfigurationOutput'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'QUEUED', 'RUNNING']
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDashboardSnapshotJobResultRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotJobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDashboardSnapshotJobResultResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'QUEUED', 'RUNNING']
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Result
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SnapshotJobResult'>
- **Required**: Yes

### ErrorInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SnapshotJobErrorInfo'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDashboardsQAConfigurationRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDashboardsQAConfigurationResponse

### DashboardsQAStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDataSetPermissionsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDataSetPermissionsResponse

### DataSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDataSetRefreshPropertiesRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDataSetRefreshPropertiesResponse

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### DataSetRefreshProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataSetRefreshProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDataSetRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDataSetResponse

### DataSet
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataSet'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDataSourcePermissionsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDataSourcePermissionsResponse

### DataSourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDataSourceRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDataSourceResponse

### DataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataSource'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDefaultQBusinessApplicationRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: typing.Optional[str]


# DescribeDefaultQBusinessApplicationResponse

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeFolderPermissionsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeFolderPermissionsRequestPaginate

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PaginatorConfig]


# DescribeFolderPermissionsResponse

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeFolderRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFolderResolvedPermissionsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeFolderResolvedPermissionsRequestPaginate

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PaginatorConfig]


# DescribeFolderResolvedPermissionsResponse

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeFolderResponse

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### Folder
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Folder'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeGroupMembershipRequest

### MemberName
- **Type**: <class 'str'>
- **Required**: Yes

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeGroupMembershipResponse

### GroupMember
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GroupMember'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeGroupRequest

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeGroupResponse

### Group
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Group'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeIAMPolicyAssignmentRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AssignmentName
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeIAMPolicyAssignmentResponse

### IAMPolicyAssignment
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.IAMPolicyAssignment'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeIngestionRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### IngestionId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeIngestionResponse

### Ingestion
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Ingestion'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeIpRestrictionRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeIpRestrictionResponse

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### IpRestrictionRuleMap
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### VpcIdRestrictionRuleMap
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### VpcEndpointIdRestrictionRuleMap
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeKeyRegistrationRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultKeyOnly
- **Type**: typing.Optional[bool]


# DescribeKeyRegistrationResponse

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### KeyRegistration
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RegisteredCustomerManagedKey]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeNamespaceRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeNamespaceResponse

### Namespace
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.NamespaceInfoV2'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeQPersonalizationConfigurationRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeQPersonalizationConfigurationResponse

### PersonalizationMode
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeQuickSightQSearchConfigurationRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeQuickSightQSearchConfigurationResponse

### QSearchStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRefreshScheduleRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRefreshScheduleResponse

### RefreshSchedule
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RefreshScheduleOutput'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRoleCustomPermissionRequest

### Role
- **Type**: typing.Literal['ADMIN', 'ADMIN_PRO', 'AUTHOR', 'AUTHOR_PRO', 'READER', 'READER_PRO']
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRoleCustomPermissionResponse

### CustomPermissionsName
- **Type**: <class 'str'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTemplateAliasRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### AliasName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTemplateAliasResponse

### TemplateAlias
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TemplateAlias'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTemplateDefinitionRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: typing.Optional[int]

### AliasName
- **Type**: typing.Optional[str]


# DescribeTemplateDefinitionResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TemplateError]
- **Required**: Yes

### ResourceStatus
- **Type**: typing.Literal['CREATION_FAILED', 'CREATION_IN_PROGRESS', 'CREATION_SUCCESSFUL', 'DELETED', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']
- **Required**: Yes

### ThemeArn
- **Type**: <class 'str'>
- **Required**: Yes

### Definition
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TemplateVersionDefinitionOutput'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTemplatePermissionsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTemplatePermissionsResponse

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### Permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTemplateRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: typing.Optional[int]

### AliasName
- **Type**: typing.Optional[str]


# DescribeTemplateResponse

### Template
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Template'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeThemeAliasRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ThemeId
- **Type**: <class 'str'>
- **Required**: Yes

### AliasName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeThemeAliasResponse

### ThemeAlias
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ThemeAlias'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeThemePermissionsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ThemeId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeThemePermissionsResponse

### ThemeId
- **Type**: <class 'str'>
- **Required**: Yes

### ThemeArn
- **Type**: <class 'str'>
- **Required**: Yes

### Permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeThemeRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ThemeId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: typing.Optional[int]

### AliasName
- **Type**: typing.Optional[str]


# DescribeThemeResponse

### Theme
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Theme'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTopicPermissionsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTopicPermissionsResponse

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### Permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTopicRefreshRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### RefreshId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTopicRefreshResponse

### RefreshDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicRefreshDetails'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTopicRefreshScheduleRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTopicRefreshScheduleResponse

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### RefreshSchedule
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicRefreshScheduleOutput'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTopicRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTopicResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### Topic
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicDetailsOutput'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeUserRequest

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeUserResponse

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.User'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeVPCConnectionRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### VPCConnectionId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeVPCConnectionResponse

### VPCConnection
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VPCConnection'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# DestinationParameterValueConfiguration

### CustomValuesConfiguration
- **Type**: <class 'NoneType'>

### SelectAllValueOptions
- **Type**: typing.Optional[typing.Literal['ALL_VALUES']]

### SourceParameterName
- **Type**: typing.Optional[str]

### SourceField
- **Type**: typing.Optional[str]

### SourceColumn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier]


# DestinationParameterValueConfigurationOutput

### CustomValuesConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CustomValuesConfigurationOutput]

### SelectAllValueOptions
- **Type**: typing.Optional[typing.Literal['ALL_VALUES']]

### SourceParameterName
- **Type**: typing.Optional[str]

### SourceField
- **Type**: typing.Optional[str]

### SourceColumn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier]


# DimensionField

### NumericalDimensionField
- **Type**: <class 'NoneType'>

### CategoricalDimensionField
- **Type**: <class 'NoneType'>

### DateDimensionField
- **Type**: <class 'NoneType'>


# DisplayFormatOptions

### UseBlankCellFormat
- **Type**: typing.Optional[bool]

### BlankCellFormat
- **Type**: typing.Optional[str]

### DateFormat
- **Type**: typing.Optional[str]

### DecimalSeparator
- **Type**: typing.Optional[typing.Literal['COMMA', 'DOT']]

### GroupingSeparator
- **Type**: typing.Optional[str]

### UseGrouping
- **Type**: typing.Optional[bool]

### FractionDigits
- **Type**: typing.Optional[int]

### Prefix
- **Type**: typing.Optional[str]

### Suffix
- **Type**: typing.Optional[str]

### UnitScaler
- **Type**: typing.Optional[typing.Literal['AUTO', 'BILLIONS', 'CRORES', 'LAKHS', 'MILLIONS', 'NONE', 'THOUSANDS', 'TRILLIONS']]

### NegativeFormat
- **Type**: <class 'NoneType'>

### CurrencySymbol
- **Type**: typing.Optional[str]


# DonutCenterOptions

### LabelVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# DonutOptions

### ArcOptions
- **Type**: <class 'NoneType'>

### DonutCenterOptions
- **Type**: <class 'NoneType'>


# DrillDownFilter

### NumericEqualityFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.NumericEqualityDrillDownFilter]

### CategoryFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CategoryDrillDownFilter]

### TimeRangeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TimeRangeDrillDownFilter]


# DrillDownFilterOutput

### NumericEqualityFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.NumericEqualityDrillDownFilter]

### CategoryFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CategoryDrillDownFilterOutput]

### TimeRangeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TimeRangeDrillDownFilterOutput]


# DropDownControlDisplayOptions

### SelectAllOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ListControlSelectAllOptions]

### TitleOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LabelOptions]

### InfoIconLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SheetControlInfoIconLabelOptions]


# DynamicDefaultValue

### DefaultValueColumn
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### UserNameColumn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier]

### GroupNameColumn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier]


# EmptyVisual

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomAction]]


# EmptyVisualOutput

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomActionOutput]]


# Entity

### Path
- **Type**: typing.Optional[str]


# ErrorInfo

### Type
- **Type**: typing.Optional[typing.Literal['ACCOUNT_CAPACITY_LIMIT_EXCEEDED', 'CONNECTION_FAILURE', 'CURSOR_NOT_ENABLED', 'CUSTOMER_ERROR', 'DATA_SET_DELETED', 'DATA_SET_NOT_SPICE', 'DATA_SET_SIZE_LIMIT_EXCEEDED', 'DATA_SOURCE_AUTH_FAILED', 'DATA_SOURCE_CONNECTION_FAILED', 'DATA_SOURCE_NOT_FOUND', 'DATA_TOLERANCE_EXCEPTION', 'DUPLICATE_COLUMN_NAMES_FOUND', 'ELASTICSEARCH_CURSOR_NOT_ENABLED', 'FAILURE_TO_ASSUME_ROLE', 'FAILURE_TO_PROCESS_JSON_FILE', 'IAM_ROLE_NOT_AVAILABLE', 'INGESTION_CANCELED', 'INGESTION_SUPERSEDED', 'INTERNAL_SERVICE_ERROR', 'INVALID_DATAPREP_SYNTAX', 'INVALID_DATA_SOURCE_CONFIG', 'INVALID_DATE_FORMAT', 'IOT_DATA_SET_FILE_EMPTY', 'IOT_FILE_NOT_FOUND', 'OAUTH_TOKEN_FAILURE', 'PASSWORD_AUTHENTICATION_FAILURE', 'PERMISSION_DENIED', 'PERMISSION_NOT_FOUND', 'QUERY_TIMEOUT', 'REFRESH_SUPPRESSED_BY_EDIT', 'ROW_SIZE_LIMIT_EXCEEDED', 'S3_FILE_INACCESSIBLE', 'S3_MANIFEST_ERROR', 'S3_UPLOADED_FILE_DELETED', 'SOURCE_API_LIMIT_EXCEEDED_FAILURE', 'SOURCE_RESOURCE_LIMIT_EXCEEDED', 'SPICE_TABLE_NOT_FOUND', 'SQL_EXCEPTION', 'SQL_INVALID_PARAMETER_VALUE', 'SQL_NUMERIC_OVERFLOW', 'SQL_SCHEMA_MISMATCH_ERROR', 'SQL_TABLE_NOT_FOUND', 'SSL_CERTIFICATE_VALIDATION_FAILURE', 'UNRESOLVABLE_HOST', 'UNROUTABLE_HOST']]

### Message
- **Type**: typing.Optional[str]


# ExasolParameters

### Host
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes


# ExcludePeriodConfiguration

### Amount
- **Type**: <class 'int'>
- **Required**: Yes

### Granularity
- **Type**: typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# ExplicitHierarchy

### HierarchyId
- **Type**: <class 'str'>
- **Required**: Yes

### Columns
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier]
- **Required**: Yes

### DrillDownFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DrillDownFilter]]


# ExplicitHierarchyOutput

### HierarchyId
- **Type**: <class 'str'>
- **Required**: Yes

### Columns
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier]
- **Required**: Yes

### DrillDownFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DrillDownFilterOutput]]


# ExportHiddenFieldsOption

### AvailabilityStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# ExportToCSVOption

### AvailabilityStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# ExportWithHiddenFieldsOption

### AvailabilityStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# FailedKeyRegistrationEntry

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### StatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### SenderFault
- **Type**: <class 'bool'>
- **Required**: Yes

### KeyArn
- **Type**: typing.Optional[str]


# FieldBasedTooltip

### AggregationVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### TooltipTitleType
- **Type**: typing.Optional[typing.Literal['NONE', 'PRIMARY_VALUE']]

### TooltipFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TooltipItem]]


# FieldBasedTooltipOutput

### AggregationVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### TooltipTitleType
- **Type**: typing.Optional[typing.Literal['NONE', 'PRIMARY_VALUE']]

### TooltipFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TooltipItem]]


# FieldFolder

### description
- **Type**: typing.Optional[str]

### columns
- **Type**: typing.Optional[typing.List[str]]


# FieldFolderOutput

### description
- **Type**: typing.Optional[str]

### columns
- **Type**: typing.Optional[typing.List[str]]


# FieldLabelType

### FieldId
- **Type**: typing.Optional[str]

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# FieldSeriesItem

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### AxisBinding
- **Type**: typing.Literal['PRIMARY_YAXIS', 'SECONDARY_YAXIS']
- **Required**: Yes

### Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LineChartSeriesSettings]


# FieldSort

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### Direction
- **Type**: typing.Literal['ASC', 'DESC']
- **Required**: Yes


# FieldSortOptions

### FieldSort
- **Type**: <class 'NoneType'>

### ColumnSort
- **Type**: <class 'NoneType'>


# FieldTooltipItem

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### Label
- **Type**: typing.Optional[str]

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### TooltipTarget
- **Type**: typing.Optional[typing.Literal['BAR', 'BOTH', 'LINE']]


# FilledMapAggregatedFieldWells

### Geospatial
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]


# FilledMapAggregatedFieldWellsOutput

### Geospatial
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]


# FilledMapConditionalFormatting

### ConditionalFormattingOptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilledMapConditionalFormattingOption]
- **Required**: Yes


# FilledMapConditionalFormattingOption

### Shape
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilledMapShapeConditionalFormatting'>
- **Required**: Yes


# FilledMapConditionalFormattingOptionOutput

### Shape
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilledMapShapeConditionalFormattingOutput'>
- **Required**: Yes


# FilledMapConditionalFormattingOutput

### ConditionalFormattingOptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilledMapConditionalFormattingOptionOutput]
- **Required**: Yes


# FilledMapConfiguration

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilledMapFieldWells]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilledMapSortConfiguration]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LegendOptions]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TooltipOptions]

### WindowOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialWindowOptions]

### MapStyleOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialMapStyleOptions]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# FilledMapConfigurationOutput

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilledMapFieldWellsOutput]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilledMapSortConfigurationOutput]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LegendOptions]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TooltipOptionsOutput]

### WindowOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialWindowOptions]

### MapStyleOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialMapStyleOptions]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# FilledMapFieldWells

### FilledMapAggregatedFieldWells
- **Type**: <class 'NoneType'>


# FilledMapFieldWellsOutput

### FilledMapAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilledMapAggregatedFieldWellsOutput]


# FilledMapShapeConditionalFormatting

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### Format
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ShapeConditionalFormat]


# FilledMapShapeConditionalFormattingOutput

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### Format
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ShapeConditionalFormatOutput]


# FilledMapSortConfiguration

### CategorySort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]


# FilledMapSortConfigurationOutput

### CategorySort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]


# FilledMapVisual

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilledMapConfiguration]

### ConditionalFormatting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilledMapConditionalFormatting]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnHierarchy]]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomAction]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# FilledMapVisualOutput

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilledMapConfigurationOutput]

### ConditionalFormatting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilledMapConditionalFormattingOutput]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnHierarchyOutput]]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomActionOutput]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# Filter

### CategoryFilter
- **Type**: <class 'NoneType'>

### NumericRangeFilter
- **Type**: <class 'NoneType'>

### NumericEqualityFilter
- **Type**: <class 'NoneType'>

### TimeEqualityFilter
- **Type**: <class 'NoneType'>

### TimeRangeFilter
- **Type**: <class 'NoneType'>

### RelativeDatesFilter
- **Type**: <class 'NoneType'>

### TopBottomFilter
- **Type**: <class 'NoneType'>

### NestedFilter
- **Type**: <class 'NoneType'>


# FilterAggMetrics

### MetricOperand
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Identifier]

### Function
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'COLUMN', 'COUNT', 'CUSTOM', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'PERCENTILE', 'PTD_AVERAGE', 'PTD_COUNT', 'PTD_DISTINCT_COUNT', 'PTD_MAX', 'PTD_MIN', 'PTD_SUM', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]

### SortDirection
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# FilterControl

### DateTimePicker
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterDateTimePickerControl]

### List
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterListControl]

### Dropdown
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterDropDownControl]

### TextField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterTextFieldControl]

### TextArea
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterTextAreaControl]

### Slider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterSliderControl]

### RelativeDateTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterRelativeDateTimeControl]

### CrossSheet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterCrossSheetControl]


# FilterControlOutput

### DateTimePicker
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterDateTimePickerControl]

### List
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterListControlOutput]

### Dropdown
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterDropDownControlOutput]

### TextField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterTextFieldControl]

### TextArea
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterTextAreaControl]

### Slider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterSliderControl]

### RelativeDateTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterRelativeDateTimeControl]

### CrossSheet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterCrossSheetControlOutput]


# FilterCrossSheetControl

### FilterControlId
- **Type**: <class 'str'>
- **Required**: Yes

### SourceFilterId
- **Type**: <class 'str'>
- **Required**: Yes

### CascadingControlConfiguration
- **Type**: <class 'NoneType'>


# FilterCrossSheetControlOutput

### FilterControlId
- **Type**: <class 'str'>
- **Required**: Yes

### SourceFilterId
- **Type**: <class 'str'>
- **Required**: Yes

### CascadingControlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CascadingControlConfigurationOutput]


# FilterDateTimePickerControl

### FilterControlId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### SourceFilterId
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DateTimePickerControlDisplayOptions]

### Type
- **Type**: typing.Optional[typing.Literal['DATE_RANGE', 'SINGLE_VALUED']]

### CommitMode
- **Type**: typing.Optional[typing.Literal['AUTO', 'MANUAL']]


# FilterDropDownControl

### FilterControlId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### SourceFilterId
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DropDownControlDisplayOptions]

### Type
- **Type**: typing.Optional[typing.Literal['MULTI_SELECT', 'SINGLE_SELECT']]

### SelectableValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterSelectableValues]

### CascadingControlConfiguration
- **Type**: <class 'NoneType'>

### CommitMode
- **Type**: typing.Optional[typing.Literal['AUTO', 'MANUAL']]


# FilterDropDownControlOutput

### FilterControlId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### SourceFilterId
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DropDownControlDisplayOptions]

### Type
- **Type**: typing.Optional[typing.Literal['MULTI_SELECT', 'SINGLE_SELECT']]

### SelectableValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterSelectableValuesOutput]

### CascadingControlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CascadingControlConfigurationOutput]

### CommitMode
- **Type**: typing.Optional[typing.Literal['AUTO', 'MANUAL']]


# FilterGroup

### FilterGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Filter]
- **Required**: Yes

### ScopeConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterScopeConfiguration'>
- **Required**: Yes

### CrossDataset
- **Type**: typing.Literal['ALL_DATASETS', 'SINGLE_DATASET']
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# FilterGroupOutput

### FilterGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterOutput]
- **Required**: Yes

### ScopeConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterScopeConfigurationOutput'>
- **Required**: Yes

### CrossDataset
- **Type**: typing.Literal['ALL_DATASETS', 'SINGLE_DATASET']
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# FilterListConfiguration

### MatchOperator
- **Type**: typing.Literal['CONTAINS', 'DOES_NOT_CONTAIN', 'DOES_NOT_EQUAL', 'ENDS_WITH', 'EQUALS', 'STARTS_WITH']
- **Required**: Yes

### CategoryValues
- **Type**: typing.Optional[typing.List[str]]

### SelectAllOptions
- **Type**: typing.Optional[typing.Literal['FILTER_ALL_VALUES']]

### NullOption
- **Type**: typing.Optional[typing.Literal['ALL_VALUES', 'NON_NULLS_ONLY', 'NULLS_ONLY']]


# FilterListConfigurationOutput

### MatchOperator
- **Type**: typing.Literal['CONTAINS', 'DOES_NOT_CONTAIN', 'DOES_NOT_EQUAL', 'ENDS_WITH', 'EQUALS', 'STARTS_WITH']
- **Required**: Yes

### CategoryValues
- **Type**: typing.Optional[typing.List[str]]

### SelectAllOptions
- **Type**: typing.Optional[typing.Literal['FILTER_ALL_VALUES']]

### NullOption
- **Type**: typing.Optional[typing.Literal['ALL_VALUES', 'NON_NULLS_ONLY', 'NULLS_ONLY']]


# FilterListControl

### FilterControlId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### SourceFilterId
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ListControlDisplayOptions]

### Type
- **Type**: typing.Optional[typing.Literal['MULTI_SELECT', 'SINGLE_SELECT']]

### SelectableValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterSelectableValues]

### CascadingControlConfiguration
- **Type**: <class 'NoneType'>


# FilterListControlOutput

### FilterControlId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### SourceFilterId
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ListControlDisplayOptions]

### Type
- **Type**: typing.Optional[typing.Literal['MULTI_SELECT', 'SINGLE_SELECT']]

### SelectableValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterSelectableValuesOutput]

### CascadingControlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CascadingControlConfigurationOutput]


# FilterOperation

### ConditionExpression
- **Type**: <class 'str'>
- **Required**: Yes


# FilterOperationSelectedFieldsConfiguration

### SelectedFields
- **Type**: typing.Optional[typing.List[str]]

### SelectedFieldOptions
- **Type**: typing.Optional[typing.Literal['ALL_FIELDS']]

### SelectedColumns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier]]


# FilterOperationSelectedFieldsConfigurationOutput

### SelectedFields
- **Type**: typing.Optional[typing.List[str]]

### SelectedFieldOptions
- **Type**: typing.Optional[typing.Literal['ALL_FIELDS']]

### SelectedColumns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier]]


# FilterOperationTargetVisualsConfiguration

### SameSheetTargetVisualConfiguration
- **Type**: <class 'NoneType'>


# FilterOperationTargetVisualsConfigurationOutput

### SameSheetTargetVisualConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SameSheetTargetVisualConfigurationOutput]


# FilterOutput

### CategoryFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CategoryFilterOutput]

### NumericRangeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.NumericRangeFilterOutput]

### NumericEqualityFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.NumericEqualityFilterOutput]

### TimeEqualityFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TimeEqualityFilterOutput]

### TimeRangeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TimeRangeFilterOutput]

### RelativeDatesFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RelativeDatesFilterOutput]

### TopBottomFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopBottomFilterOutput]

### NestedFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.NestedFilterOutput]


# FilterRelativeDateTimeControl

### FilterControlId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### SourceFilterId
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RelativeDateTimeControlDisplayOptions]

### CommitMode
- **Type**: typing.Optional[typing.Literal['AUTO', 'MANUAL']]


# FilterScopeConfiguration

### SelectedSheets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SelectedSheetsFilterScopeConfiguration]

### AllSheets
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# FilterScopeConfigurationOutput

### SelectedSheets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SelectedSheetsFilterScopeConfigurationOutput]

### AllSheets
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# FilterSelectableValues

### Values
- **Type**: typing.Optional[typing.List[str]]


# FilterSelectableValuesOutput

### Values
- **Type**: typing.Optional[typing.List[str]]


# FilterSliderControl

### FilterControlId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### SourceFilterId
- **Type**: <class 'str'>
- **Required**: Yes

### MaximumValue
- **Type**: <class 'float'>
- **Required**: Yes

### MinimumValue
- **Type**: <class 'float'>
- **Required**: Yes

### StepSize
- **Type**: <class 'float'>
- **Required**: Yes

### DisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SliderControlDisplayOptions]

### Type
- **Type**: typing.Optional[typing.Literal['RANGE', 'SINGLE_POINT']]


# FilterTextAreaControl

### FilterControlId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### SourceFilterId
- **Type**: <class 'str'>
- **Required**: Yes

### Delimiter
- **Type**: typing.Optional[str]

### DisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TextAreaControlDisplayOptions]


# FilterTextFieldControl

### FilterControlId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### SourceFilterId
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TextFieldControlDisplayOptions]


# Folder

### FolderId
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### FolderType
- **Type**: typing.Optional[typing.Literal['RESTRICTED', 'SHARED']]

### FolderPath
- **Type**: typing.Optional[typing.List[str]]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### SharingModel
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'NAMESPACE']]


# FolderMember

### MemberId
- **Type**: typing.Optional[str]

### MemberType
- **Type**: typing.Optional[typing.Literal['ANALYSIS', 'DASHBOARD', 'DATASET', 'DATASOURCE', 'TOPIC']]


# FolderSearchFilter

### Operator
- **Type**: typing.Optional[typing.Literal['StringEquals', 'StringLike']]

### Name
- **Type**: typing.Optional[typing.Literal['DIRECT_QUICKSIGHT_OWNER', 'DIRECT_QUICKSIGHT_SOLE_OWNER', 'DIRECT_QUICKSIGHT_VIEWER_OR_OWNER', 'FOLDER_NAME', 'PARENT_FOLDER_ARN', 'QUICKSIGHT_OWNER', 'QUICKSIGHT_VIEWER_OR_OWNER']]

### Value
- **Type**: typing.Optional[str]


# FolderSummary

### Arn
- **Type**: typing.Optional[str]

### FolderId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### FolderType
- **Type**: typing.Optional[typing.Literal['RESTRICTED', 'SHARED']]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### SharingModel
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'NAMESPACE']]


# Font

### FontFamily
- **Type**: typing.Optional[str]


# FontConfiguration

### FontSize
- **Type**: <class 'NoneType'>

### FontDecoration
- **Type**: typing.Optional[typing.Literal['NONE', 'UNDERLINE']]

### FontColor
- **Type**: typing.Optional[str]

### FontWeight
- **Type**: <class 'NoneType'>

### FontStyle
- **Type**: typing.Optional[typing.Literal['ITALIC', 'NORMAL']]

### FontFamily
- **Type**: typing.Optional[str]


# FontSize

### Relative
- **Type**: typing.Optional[typing.Literal['EXTRA_LARGE', 'EXTRA_SMALL', 'LARGE', 'MEDIUM', 'SMALL']]

### Absolute
- **Type**: typing.Optional[str]


# FontWeight

### Name
- **Type**: typing.Optional[typing.Literal['BOLD', 'NORMAL']]


# ForecastComputation

### ComputationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Time
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]

### Value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]

### PeriodsForward
- **Type**: typing.Optional[int]

### PeriodsBackward
- **Type**: typing.Optional[int]

### UpperBoundary
- **Type**: typing.Optional[float]

### LowerBoundary
- **Type**: typing.Optional[float]

### PredictionInterval
- **Type**: typing.Optional[int]

### Seasonality
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'CUSTOM']]

### CustomSeasonalityValue
- **Type**: typing.Optional[int]


# ForecastConfiguration

### ForecastProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TimeBasedForecastProperties]

### Scenario
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ForecastScenario]


# ForecastConfigurationOutput

### ForecastProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TimeBasedForecastProperties]

### Scenario
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ForecastScenarioOutput]


# ForecastScenario

### WhatIfPointScenario
- **Type**: <class 'NoneType'>

### WhatIfRangeScenario
- **Type**: <class 'NoneType'>


# ForecastScenarioOutput

### WhatIfPointScenario
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.WhatIfPointScenarioOutput]

### WhatIfRangeScenario
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.WhatIfRangeScenarioOutput]


# FormatConfiguration

### StringFormatConfiguration
- **Type**: <class 'NoneType'>

### NumberFormatConfiguration
- **Type**: <class 'NoneType'>

### DateTimeFormatConfiguration
- **Type**: <class 'NoneType'>


# FreeFormLayoutCanvasSizeOptions

### ScreenCanvasSizeOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FreeFormLayoutScreenCanvasSizeOptions]


# FreeFormLayoutConfiguration

### Elements
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FreeFormLayoutElement]
- **Required**: Yes

### CanvasSizeOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FreeFormLayoutCanvasSizeOptions]


# FreeFormLayoutConfigurationOutput

### Elements
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FreeFormLayoutElementOutput]
- **Required**: Yes

### CanvasSizeOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FreeFormLayoutCanvasSizeOptions]


# FreeFormLayoutElement

### ElementId
- **Type**: <class 'str'>
- **Required**: Yes

### ElementType
- **Type**: typing.Literal['FILTER_CONTROL', 'IMAGE', 'PARAMETER_CONTROL', 'TEXT_BOX', 'VISUAL']
- **Required**: Yes

### XAxisLocation
- **Type**: <class 'str'>
- **Required**: Yes

### YAxisLocation
- **Type**: <class 'str'>
- **Required**: Yes

### Width
- **Type**: <class 'str'>
- **Required**: Yes

### Height
- **Type**: <class 'str'>
- **Required**: Yes

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### RenderingRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SheetElementRenderingRule]]

### BorderStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FreeFormLayoutElementBorderStyle]

### SelectedBorderStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FreeFormLayoutElementBorderStyle]

### BackgroundStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FreeFormLayoutElementBackgroundStyle]

### LoadingAnimation
- **Type**: <class 'NoneType'>


# FreeFormLayoutElementBackgroundStyle

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### Color
- **Type**: typing.Optional[str]


# FreeFormLayoutElementBorderStyle

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### Color
- **Type**: typing.Optional[str]


# FreeFormLayoutElementOutput

### ElementId
- **Type**: <class 'str'>
- **Required**: Yes

### ElementType
- **Type**: typing.Literal['FILTER_CONTROL', 'IMAGE', 'PARAMETER_CONTROL', 'TEXT_BOX', 'VISUAL']
- **Required**: Yes

### XAxisLocation
- **Type**: <class 'str'>
- **Required**: Yes

### YAxisLocation
- **Type**: <class 'str'>
- **Required**: Yes

### Width
- **Type**: <class 'str'>
- **Required**: Yes

### Height
- **Type**: <class 'str'>
- **Required**: Yes

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### RenderingRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SheetElementRenderingRule]]

### BorderStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FreeFormLayoutElementBorderStyle]

### SelectedBorderStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FreeFormLayoutElementBorderStyle]

### BackgroundStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FreeFormLayoutElementBackgroundStyle]

### LoadingAnimation
- **Type**: <class 'NoneType'>


# FreeFormLayoutScreenCanvasSizeOptions

### OptimizedViewPortWidth
- **Type**: <class 'str'>
- **Required**: Yes


# FreeFormSectionLayoutConfiguration

### Elements
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FreeFormLayoutElement]
- **Required**: Yes


# FreeFormSectionLayoutConfigurationOutput

### Elements
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FreeFormLayoutElementOutput]
- **Required**: Yes


# FunnelChartAggregatedFieldWells

### Category
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]


# FunnelChartAggregatedFieldWellsOutput

### Category
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]


# FunnelChartConfiguration

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FunnelChartFieldWells]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FunnelChartSortConfiguration]

### CategoryLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptions]

### ValueLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptions]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TooltipOptions]

### DataLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FunnelChartDataLabelOptions]

### VisualPalette
- **Type**: <class 'NoneType'>

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# FunnelChartConfigurationOutput

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FunnelChartFieldWellsOutput]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FunnelChartSortConfigurationOutput]

### CategoryLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptionsOutput]

### ValueLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptionsOutput]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TooltipOptionsOutput]

### DataLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FunnelChartDataLabelOptions]

### VisualPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualPaletteOutput]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# FunnelChartDataLabelOptions

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### CategoryLabelVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### MeasureLabelVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### Position
- **Type**: typing.Optional[typing.Literal['BOTTOM', 'INSIDE', 'LEFT', 'OUTSIDE', 'RIGHT', 'TOP']]

### LabelFontConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FontConfiguration]

### LabelColor
- **Type**: typing.Optional[str]

### MeasureDataLabelStyle
- **Type**: typing.Optional[typing.Literal['PERCENTAGE_BY_FIRST_STAGE', 'PERCENTAGE_BY_PREVIOUS_STAGE', 'VALUE_AND_PERCENTAGE_BY_FIRST_STAGE', 'VALUE_AND_PERCENTAGE_BY_PREVIOUS_STAGE', 'VALUE_ONLY']]


# FunnelChartFieldWells

### FunnelChartAggregatedFieldWells
- **Type**: <class 'NoneType'>


# FunnelChartFieldWellsOutput

### FunnelChartAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FunnelChartAggregatedFieldWellsOutput]


# FunnelChartSortConfiguration

### CategorySort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### CategoryItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]


# FunnelChartSortConfigurationOutput

### CategorySort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### CategoryItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]


# FunnelChartVisual

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FunnelChartConfiguration]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomAction]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnHierarchy]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# FunnelChartVisualOutput

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FunnelChartConfigurationOutput]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomActionOutput]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnHierarchyOutput]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# GaugeChartArcConditionalFormatting

### ForegroundColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingColor]


# GaugeChartArcConditionalFormattingOutput

### ForegroundColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingColorOutput]


# GaugeChartColorConfiguration

### ForegroundColor
- **Type**: typing.Optional[str]

### BackgroundColor
- **Type**: typing.Optional[str]


# GaugeChartConditionalFormatting

### ConditionalFormattingOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GaugeChartConditionalFormattingOption]]


# GaugeChartConditionalFormattingOption

### PrimaryValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GaugeChartPrimaryValueConditionalFormatting]

### Arc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GaugeChartArcConditionalFormatting]


# GaugeChartConditionalFormattingOptionOutput

### PrimaryValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GaugeChartPrimaryValueConditionalFormattingOutput]

### Arc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GaugeChartArcConditionalFormattingOutput]


# GaugeChartConditionalFormattingOutput

### ConditionalFormattingOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GaugeChartConditionalFormattingOptionOutput]]


# GaugeChartConfiguration

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GaugeChartFieldWells]

### GaugeChartOptions
- **Type**: <class 'NoneType'>

### DataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataLabelOptions]

### TooltipOptions
- **Type**: <class 'NoneType'>

### VisualPalette
- **Type**: <class 'NoneType'>

### ColorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GaugeChartColorConfiguration]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# GaugeChartConfigurationOutput

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GaugeChartFieldWellsOutput]

### GaugeChartOptions
- **Type**: <class 'NoneType'>

### DataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataLabelOptionsOutput]

### TooltipOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TooltipOptionsOutput]

### VisualPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualPaletteOutput]

### ColorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GaugeChartColorConfiguration]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# GaugeChartFieldWells

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]

### TargetValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]


# GaugeChartFieldWellsOutput

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]

### TargetValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]


# GaugeChartOptions

### PrimaryValueDisplayType
- **Type**: typing.Optional[typing.Literal['ACTUAL', 'COMPARISON', 'HIDDEN']]

### Comparison
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ComparisonConfiguration]

### ArcAxis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ArcAxisConfiguration]

### Arc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ArcConfiguration]

### PrimaryValueFontConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FontConfiguration]


# GaugeChartPrimaryValueConditionalFormatting

### TextColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingColor]

### Icon
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingIcon]


# GaugeChartPrimaryValueConditionalFormattingOutput

### TextColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingColorOutput]

### Icon
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingIcon]


# GaugeChartVisual

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GaugeChartConfiguration]

### ConditionalFormatting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GaugeChartConditionalFormatting]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomAction]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# GaugeChartVisualOutput

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GaugeChartConfigurationOutput]

### ConditionalFormatting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GaugeChartConditionalFormattingOutput]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomActionOutput]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# GenerateEmbedUrlForAnonymousUserRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizedResourceArns
- **Type**: typing.List[str]
- **Required**: Yes

### ExperienceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AnonymousUserEmbeddingExperienceConfiguration'>
- **Required**: Yes

### SessionLifetimeInMinutes
- **Type**: typing.Optional[int]

### SessionTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SessionTag]]

### AllowedDomains
- **Type**: typing.Optional[typing.List[str]]


# GenerateEmbedUrlForAnonymousUserResponse

### EmbedUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### AnonymousUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# GenerateEmbedUrlForRegisteredUserRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### UserArn
- **Type**: <class 'str'>
- **Required**: Yes

### ExperienceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RegisteredUserEmbeddingExperienceConfiguration'>
- **Required**: Yes

### SessionLifetimeInMinutes
- **Type**: typing.Optional[int]

### AllowedDomains
- **Type**: typing.Optional[typing.List[str]]


# GenerateEmbedUrlForRegisteredUserResponse

### EmbedUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# GenerateEmbedUrlForRegisteredUserWithIdentityRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ExperienceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RegisteredUserEmbeddingExperienceConfiguration'>
- **Required**: Yes

### SessionLifetimeInMinutes
- **Type**: typing.Optional[int]

### AllowedDomains
- **Type**: typing.Optional[typing.List[str]]


# GenerateEmbedUrlForRegisteredUserWithIdentityResponse

### EmbedUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# GeneratedAnswerResult

### QuestionText
- **Type**: typing.Optional[str]

### AnswerStatus
- **Type**: typing.Optional[typing.Literal['ANSWER_DOWNGRADE', 'ANSWER_GENERATED', 'ANSWER_RETRIEVED']]

### TopicId
- **Type**: typing.Optional[str]

### TopicName
- **Type**: typing.Optional[str]

### Restatement
- **Type**: typing.Optional[str]

### QuestionId
- **Type**: typing.Optional[str]

### AnswerId
- **Type**: typing.Optional[str]

### QuestionUrl
- **Type**: typing.Optional[str]


# GeoSpatialColumnGroup

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Columns
- **Type**: typing.List[str]
- **Required**: Yes

### CountryCode
- **Type**: typing.Optional[typing.Literal['US']]


# GeoSpatialColumnGroupOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Columns
- **Type**: typing.List[str]
- **Required**: Yes

### CountryCode
- **Type**: typing.Optional[typing.Literal['US']]


# GeospatialCategoricalColor

### CategoryDataColors
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialCategoricalDataColor]
- **Required**: Yes

### NullDataVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### NullDataSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialNullDataSettings]

### DefaultOpacity
- **Type**: typing.Optional[float]


# GeospatialCategoricalColorOutput

### CategoryDataColors
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialCategoricalDataColor]
- **Required**: Yes

### NullDataVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### NullDataSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialNullDataSettings]

### DefaultOpacity
- **Type**: typing.Optional[float]


# GeospatialCategoricalDataColor

### Color
- **Type**: <class 'str'>
- **Required**: Yes

### DataValue
- **Type**: <class 'str'>
- **Required**: Yes


# GeospatialCircleRadius

### Radius
- **Type**: typing.Optional[float]


# GeospatialCircleSymbolStyle

### FillColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialColor]

### StrokeColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialColor]

### StrokeWidth
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialLineWidth]

### CircleRadius
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialCircleRadius]


# GeospatialCircleSymbolStyleOutput

### FillColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialColorOutput]

### StrokeColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialColorOutput]

### StrokeWidth
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialLineWidth]

### CircleRadius
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialCircleRadius]


# GeospatialColor

### Solid
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialSolidColor]

### Gradient
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialGradientColor]

### Categorical
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialCategoricalColor]


# GeospatialColorOutput

### Solid
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialSolidColor]

### Gradient
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialGradientColorOutput]

### Categorical
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialCategoricalColorOutput]


# GeospatialCoordinateBounds

### North
- **Type**: <class 'float'>
- **Required**: Yes

### South
- **Type**: <class 'float'>
- **Required**: Yes

### West
- **Type**: <class 'float'>
- **Required**: Yes

### East
- **Type**: <class 'float'>
- **Required**: Yes


# GeospatialDataSourceItem

### StaticFileDataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialStaticFileSource]


# GeospatialGradientColor

### StepColors
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialGradientStepColor]
- **Required**: Yes

### NullDataVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### NullDataSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialNullDataSettings]

### DefaultOpacity
- **Type**: typing.Optional[float]


# GeospatialGradientColorOutput

### StepColors
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialGradientStepColor]
- **Required**: Yes

### NullDataVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### NullDataSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialNullDataSettings]

### DefaultOpacity
- **Type**: typing.Optional[float]


# GeospatialGradientStepColor

### Color
- **Type**: <class 'str'>
- **Required**: Yes

### DataValue
- **Type**: <class 'float'>
- **Required**: Yes


# GeospatialHeatmapColorScale

### Colors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialHeatmapDataColor]]


# GeospatialHeatmapColorScaleOutput

### Colors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialHeatmapDataColor]]


# GeospatialHeatmapConfiguration

### HeatmapColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialHeatmapColorScale]


# GeospatialHeatmapConfigurationOutput

### HeatmapColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialHeatmapColorScaleOutput]


# GeospatialHeatmapDataColor

### Color
- **Type**: <class 'str'>
- **Required**: Yes


# GeospatialLayerColorField

### ColorDimensionsFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### ColorValuesFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]


# GeospatialLayerColorFieldOutput

### ColorDimensionsFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### ColorValuesFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]


# GeospatialLayerDefinition

### PointLayer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialPointLayer]

### LineLayer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialLineLayer]

### PolygonLayer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialPolygonLayer]


# GeospatialLayerDefinitionOutput

### PointLayer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialPointLayerOutput]

### LineLayer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialLineLayerOutput]

### PolygonLayer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialPolygonLayerOutput]


# GeospatialLayerItem

### LayerId
- **Type**: <class 'str'>
- **Required**: Yes

### LayerType
- **Type**: typing.Optional[typing.Literal['LINE', 'POINT', 'POLYGON']]

### DataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialDataSourceItem]

### Label
- **Type**: typing.Optional[str]

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### LayerDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialLayerDefinition]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TooltipOptions]

### JoinDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialLayerJoinDefinition]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LayerCustomAction]]


# GeospatialLayerItemOutput

### LayerId
- **Type**: <class 'str'>
- **Required**: Yes

### LayerType
- **Type**: typing.Optional[typing.Literal['LINE', 'POINT', 'POLYGON']]

### DataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialDataSourceItem]

### Label
- **Type**: typing.Optional[str]

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### LayerDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialLayerDefinitionOutput]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TooltipOptionsOutput]

### JoinDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialLayerJoinDefinitionOutput]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LayerCustomActionOutput]]


# GeospatialLayerJoinDefinition

### ShapeKeyField
- **Type**: typing.Optional[str]

### DatasetKeyField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.UnaggregatedField]

### ColorField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialLayerColorField]


# GeospatialLayerJoinDefinitionOutput

### ShapeKeyField
- **Type**: typing.Optional[str]

### DatasetKeyField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.UnaggregatedField]

### ColorField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialLayerColorFieldOutput]


# GeospatialLayerMapConfiguration

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LegendOptions]

### MapLayers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialLayerItem]]

### MapState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialMapState]

### MapStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialMapStyle]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# GeospatialLayerMapConfigurationOutput

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LegendOptions]

### MapLayers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialLayerItemOutput]]

### MapState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialMapState]

### MapStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialMapStyle]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# GeospatialLineLayer

### Style
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialLineStyle'>
- **Required**: Yes


# GeospatialLineLayerOutput

### Style
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialLineStyleOutput'>
- **Required**: Yes


# GeospatialLineStyle

### LineSymbolStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialLineSymbolStyle]


# GeospatialLineStyleOutput

### LineSymbolStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialLineSymbolStyleOutput]


# GeospatialLineSymbolStyle

### FillColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialColor]

### LineWidth
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialLineWidth]


# GeospatialLineSymbolStyleOutput

### FillColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialColorOutput]

### LineWidth
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialLineWidth]


# GeospatialLineWidth

### LineWidth
- **Type**: typing.Optional[float]


# GeospatialMapAggregatedFieldWells

### Geospatial
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]

### Colors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]


# GeospatialMapAggregatedFieldWellsOutput

### Geospatial
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]

### Colors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]


# GeospatialMapConfiguration

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialMapFieldWells]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LegendOptions]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TooltipOptions]

### WindowOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialWindowOptions]

### MapStyleOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialMapStyleOptions]

### PointStyleOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialPointStyleOptions]

### VisualPalette
- **Type**: <class 'NoneType'>

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# GeospatialMapConfigurationOutput

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialMapFieldWellsOutput]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LegendOptions]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TooltipOptionsOutput]

### WindowOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialWindowOptions]

### MapStyleOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialMapStyleOptions]

### PointStyleOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialPointStyleOptionsOutput]

### VisualPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualPaletteOutput]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# GeospatialMapFieldWells

### GeospatialMapAggregatedFieldWells
- **Type**: <class 'NoneType'>


# GeospatialMapFieldWellsOutput

### GeospatialMapAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialMapAggregatedFieldWellsOutput]


# GeospatialMapState

### Bounds
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialCoordinateBounds]

### MapNavigation
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# GeospatialMapStyle

### BaseMapStyle
- **Type**: typing.Optional[typing.Literal['DARK_GRAY', 'IMAGERY', 'LIGHT_GRAY', 'STREET']]

### BackgroundColor
- **Type**: typing.Optional[str]

### BaseMapVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# GeospatialMapStyleOptions

### BaseMapStyle
- **Type**: typing.Optional[typing.Literal['DARK_GRAY', 'IMAGERY', 'LIGHT_GRAY', 'STREET']]


# GeospatialMapVisual

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialMapConfiguration]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnHierarchy]]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomAction]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# GeospatialMapVisualOutput

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialMapConfigurationOutput]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnHierarchyOutput]]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomActionOutput]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# GeospatialNullDataSettings

### SymbolStyle
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialNullSymbolStyle'>
- **Required**: Yes


# GeospatialNullSymbolStyle

### FillColor
- **Type**: typing.Optional[str]

### StrokeColor
- **Type**: typing.Optional[str]

### StrokeWidth
- **Type**: typing.Optional[float]


# GeospatialPointLayer

### Style
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialPointStyle'>
- **Required**: Yes


# GeospatialPointLayerOutput

### Style
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialPointStyleOutput'>
- **Required**: Yes


# GeospatialPointStyle

### CircleSymbolStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialCircleSymbolStyle]


# GeospatialPointStyleOptions

### SelectedPointStyle
- **Type**: typing.Optional[typing.Literal['CLUSTER', 'HEATMAP', 'POINT']]

### ClusterMarkerConfiguration
- **Type**: <class 'NoneType'>

### HeatmapConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialHeatmapConfiguration]


# GeospatialPointStyleOptionsOutput

### SelectedPointStyle
- **Type**: typing.Optional[typing.Literal['CLUSTER', 'HEATMAP', 'POINT']]

### ClusterMarkerConfiguration
- **Type**: <class 'NoneType'>

### HeatmapConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialHeatmapConfigurationOutput]


# GeospatialPointStyleOutput

### CircleSymbolStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialCircleSymbolStyleOutput]


# GeospatialPolygonLayer

### Style
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialPolygonStyle'>
- **Required**: Yes


# GeospatialPolygonLayerOutput

### Style
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialPolygonStyleOutput'>
- **Required**: Yes


# GeospatialPolygonStyle

### PolygonSymbolStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialPolygonSymbolStyle]


# GeospatialPolygonStyleOutput

### PolygonSymbolStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialPolygonSymbolStyleOutput]


# GeospatialPolygonSymbolStyle

### FillColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialColor]

### StrokeColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialColor]

### StrokeWidth
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialLineWidth]


# GeospatialPolygonSymbolStyleOutput

### FillColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialColorOutput]

### StrokeColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialColorOutput]

### StrokeWidth
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialLineWidth]


# GeospatialSolidColor

### Color
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# GeospatialStaticFileSource

### StaticFileId
- **Type**: <class 'str'>
- **Required**: Yes


# GeospatialWindowOptions

### Bounds
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialCoordinateBounds]

### MapZoomMode
- **Type**: typing.Optional[typing.Literal['AUTO', 'MANUAL']]


# GetDashboardEmbedUrlRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityType
- **Type**: typing.Literal['ANONYMOUS', 'IAM', 'QUICKSIGHT']
- **Required**: Yes

### SessionLifetimeInMinutes
- **Type**: typing.Optional[int]

### UndoRedoDisabled
- **Type**: typing.Optional[bool]

### ResetDisabled
- **Type**: typing.Optional[bool]

### StatePersistenceEnabled
- **Type**: typing.Optional[bool]

### UserArn
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### AdditionalDashboardIds
- **Type**: typing.Optional[typing.List[str]]


# GetDashboardEmbedUrlResponse

### EmbedUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# GetSessionEmbedUrlRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### EntryPoint
- **Type**: typing.Optional[str]

### SessionLifetimeInMinutes
- **Type**: typing.Optional[int]

### UserArn
- **Type**: typing.Optional[str]


# GetSessionEmbedUrlResponse

### EmbedUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# GlobalTableBorderOptions

### UniformBorder
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableBorderOptions]

### SideSpecificBorder
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableSideBorderOptions]


# GradientColor

### Stops
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GradientStop]]


# GradientColorOutput

### Stops
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GradientStop]]


# GradientStop

### GradientOffset
- **Type**: <class 'float'>
- **Required**: Yes

### DataValue
- **Type**: typing.Optional[float]

### Color
- **Type**: typing.Optional[str]


# GridLayoutCanvasSizeOptions

### ScreenCanvasSizeOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GridLayoutScreenCanvasSizeOptions]


# GridLayoutConfiguration

### Elements
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GridLayoutElement]
- **Required**: Yes

### CanvasSizeOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GridLayoutCanvasSizeOptions]


# GridLayoutConfigurationOutput

### Elements
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GridLayoutElement]
- **Required**: Yes

### CanvasSizeOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GridLayoutCanvasSizeOptions]


# GridLayoutElement

### ElementId
- **Type**: <class 'str'>
- **Required**: Yes

### ElementType
- **Type**: typing.Literal['FILTER_CONTROL', 'IMAGE', 'PARAMETER_CONTROL', 'TEXT_BOX', 'VISUAL']
- **Required**: Yes

### ColumnSpan
- **Type**: <class 'int'>
- **Required**: Yes

### RowSpan
- **Type**: <class 'int'>
- **Required**: Yes

### ColumnIndex
- **Type**: typing.Optional[int]

### RowIndex
- **Type**: typing.Optional[int]


# GridLayoutScreenCanvasSizeOptions

### ResizeOption
- **Type**: typing.Literal['FIXED', 'RESPONSIVE']
- **Required**: Yes

### OptimizedViewPortWidth
- **Type**: typing.Optional[str]


# Group

### Arn
- **Type**: typing.Optional[str]

### GroupName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### PrincipalId
- **Type**: typing.Optional[str]


# GroupMember

### Arn
- **Type**: typing.Optional[str]

### MemberName
- **Type**: typing.Optional[str]


# GroupSearchFilter

### Operator
- **Type**: typing.Literal['StartsWith']
- **Required**: Yes

### Name
- **Type**: typing.Literal['GROUP_NAME']
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# GrowthRateComputation

### ComputationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Time
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]

### Value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]

### PeriodSize
- **Type**: typing.Optional[int]


# GutterStyle

### Show
- **Type**: typing.Optional[bool]


# HeaderFooterSectionConfiguration

### SectionId
- **Type**: <class 'str'>
- **Required**: Yes

### Layout
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SectionLayoutConfiguration'>
- **Required**: Yes

### Style
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SectionStyle]


# HeaderFooterSectionConfigurationOutput

### SectionId
- **Type**: <class 'str'>
- **Required**: Yes

### Layout
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SectionLayoutConfigurationOutput'>
- **Required**: Yes

### Style
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SectionStyle]


# HeatMapAggregatedFieldWells

### Rows
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Columns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]


# HeatMapAggregatedFieldWellsOutput

### Rows
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Columns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]


# HeatMapConfiguration

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.HeatMapFieldWells]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.HeatMapSortConfiguration]

### RowLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptions]

### ColumnLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptions]

### ColorScale
- **Type**: <class 'NoneType'>

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LegendOptions]

### DataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataLabelOptions]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TooltipOptions]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# HeatMapConfigurationOutput

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.HeatMapFieldWellsOutput]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.HeatMapSortConfigurationOutput]

### RowLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptionsOutput]

### ColumnLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptionsOutput]

### ColorScale
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColorScaleOutput]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LegendOptions]

### DataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataLabelOptionsOutput]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TooltipOptionsOutput]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# HeatMapFieldWells

### HeatMapAggregatedFieldWells
- **Type**: <class 'NoneType'>


# HeatMapFieldWellsOutput

### HeatMapAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.HeatMapAggregatedFieldWellsOutput]


# HeatMapSortConfiguration

### HeatMapRowSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### HeatMapColumnSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### HeatMapRowItemsLimitConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]

### HeatMapColumnItemsLimitConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]


# HeatMapSortConfigurationOutput

### HeatMapRowSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### HeatMapColumnSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### HeatMapRowItemsLimitConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]

### HeatMapColumnItemsLimitConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]


# HeatMapVisual

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.HeatMapConfiguration]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnHierarchy]]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomAction]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# HeatMapVisualOutput

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.HeatMapConfigurationOutput]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnHierarchyOutput]]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomActionOutput]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# HistogramAggregatedFieldWells

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]


# HistogramAggregatedFieldWellsOutput

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]


# HistogramBinOptions

### SelectedBinType
- **Type**: typing.Optional[typing.Literal['BIN_COUNT', 'BIN_WIDTH']]

### BinCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BinCountOptions]

### BinWidth
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BinWidthOptions]

### StartValue
- **Type**: typing.Optional[float]


# HistogramConfiguration

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.HistogramFieldWells]

### XAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDisplayOptions]

### XAxisLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptions]

### YAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDisplayOptions]

### BinOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.HistogramBinOptions]

### DataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataLabelOptions]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TooltipOptions]

### VisualPalette
- **Type**: <class 'NoneType'>

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# HistogramConfigurationOutput

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.HistogramFieldWellsOutput]

### XAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDisplayOptionsOutput]

### XAxisLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptionsOutput]

### YAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDisplayOptionsOutput]

### BinOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.HistogramBinOptions]

### DataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataLabelOptionsOutput]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TooltipOptionsOutput]

### VisualPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualPaletteOutput]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# HistogramFieldWells

### HistogramAggregatedFieldWells
- **Type**: <class 'NoneType'>


# HistogramFieldWellsOutput

### HistogramAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.HistogramAggregatedFieldWellsOutput]


# HistogramVisual

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.HistogramConfiguration]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomAction]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# HistogramVisualOutput

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.HistogramConfigurationOutput]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomActionOutput]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# IAMPolicyAssignment

### AwsAccountId
- **Type**: typing.Optional[str]

### AssignmentId
- **Type**: typing.Optional[str]

### AssignmentName
- **Type**: typing.Optional[str]

### PolicyArn
- **Type**: typing.Optional[str]

### Identities
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### AssignmentStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'DRAFT', 'ENABLED']]


# IAMPolicyAssignmentSummary

### AssignmentName
- **Type**: typing.Optional[str]

### AssignmentStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'DRAFT', 'ENABLED']]


# Identifier

### Identity
- **Type**: <class 'str'>
- **Required**: Yes


# IdentityCenterConfiguration

### EnableIdentityPropagation
- **Type**: typing.Optional[bool]


# Image

### Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ImageSource]

### GeneratedImageUrl
- **Type**: typing.Optional[str]


# ImageConfiguration

### Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ImageSource]


# ImageCustomAction

### CustomActionId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Trigger
- **Type**: typing.Literal['CLICK', 'MENU']
- **Required**: Yes

### ActionOperations
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ImageCustomActionOperation]
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# ImageCustomActionOperation

### NavigationOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CustomActionNavigationOperation]

### URLOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CustomActionURLOperation]

### SetParametersOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CustomActionSetParametersOperation]


# ImageCustomActionOperationOutput

### NavigationOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CustomActionNavigationOperation]

### URLOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CustomActionURLOperation]

### SetParametersOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CustomActionSetParametersOperationOutput]


# ImageCustomActionOutput

### CustomActionId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Trigger
- **Type**: typing.Literal['CLICK', 'MENU']
- **Required**: Yes

### ActionOperations
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ImageCustomActionOperationOutput]
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# ImageInteractionOptions

### ImageMenuOption
- **Type**: <class 'NoneType'>


# ImageMenuOption

### AvailabilityStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# ImageSet

### Original
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Image'>
- **Required**: Yes

### Height64
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Image]

### Height32
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Image]


# ImageSetConfiguration

### Original
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ImageConfiguration'>
- **Required**: Yes


# ImageSource

### PublicUrl
- **Type**: typing.Optional[str]

### S3Uri
- **Type**: typing.Optional[str]


# ImageStaticFile

### StaticFileId
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.StaticFileSource]


# IncrementalRefresh

### LookbackWindow
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LookbackWindow'>
- **Required**: Yes


# Ingestion

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### IngestionStatus
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'FAILED', 'INITIALIZED', 'QUEUED', 'RUNNING']
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### IngestionId
- **Type**: typing.Optional[str]

### ErrorInfo
- **Type**: <class 'NoneType'>

### RowInfo
- **Type**: <class 'NoneType'>

### QueueInfo
- **Type**: <class 'NoneType'>

### IngestionTimeInSeconds
- **Type**: typing.Optional[int]

### IngestionSizeInBytes
- **Type**: typing.Optional[int]

### RequestSource
- **Type**: typing.Optional[typing.Literal['MANUAL', 'SCHEDULED']]

### RequestType
- **Type**: typing.Optional[typing.Literal['EDIT', 'FULL_REFRESH', 'INCREMENTAL_REFRESH', 'INITIAL_INGESTION']]


# InnerFilter

### CategoryInnerFilter
- **Type**: <class 'NoneType'>


# InnerFilterOutput

### CategoryInnerFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CategoryInnerFilterOutput]


# InputColumn

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['BIT', 'BOOLEAN', 'DATETIME', 'DECIMAL', 'INTEGER', 'JSON', 'STRING']
- **Required**: Yes

### SubType
- **Type**: typing.Optional[typing.Literal['FIXED', 'FLOAT']]


# InsightConfiguration

### Computations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Computation]]

### CustomNarrative
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CustomNarrativeOptions]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# InsightConfigurationOutput

### Computations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Computation]]

### CustomNarrative
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CustomNarrativeOptions]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# InsightVisual

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### InsightConfiguration
- **Type**: <class 'NoneType'>

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomAction]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# InsightVisualOutput

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### InsightConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.InsightConfigurationOutput]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomActionOutput]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# IntegerDatasetParameter

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ValueType
- **Type**: typing.Literal['MULTI_VALUED', 'SINGLE_VALUED']
- **Required**: Yes

### DefaultValues
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.IntegerDatasetParameterDefaultValues, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.IntegerDatasetParameterDefaultValuesOutput, NoneType]


# IntegerDatasetParameterDefaultValues

### StaticValues
- **Type**: typing.Optional[typing.List[int]]


# IntegerDatasetParameterDefaultValuesOutput

### StaticValues
- **Type**: typing.Optional[typing.List[int]]


# IntegerDatasetParameterOutput

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ValueType
- **Type**: typing.Literal['MULTI_VALUED', 'SINGLE_VALUED']
- **Required**: Yes

### DefaultValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.IntegerDatasetParameterDefaultValuesOutput]


# IntegerDefaultValues

### DynamicValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DynamicDefaultValue]

### StaticValues
- **Type**: typing.Optional[typing.List[int]]


# IntegerDefaultValuesOutput

### DynamicValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DynamicDefaultValue]

### StaticValues
- **Type**: typing.Optional[typing.List[int]]


# IntegerParameter

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.List[int]
- **Required**: Yes


# IntegerParameterDeclaration

### ParameterValueType
- **Type**: typing.Literal['MULTI_VALUED', 'SINGLE_VALUED']
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.IntegerDefaultValues]

### ValueWhenUnset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.IntegerValueWhenUnsetConfiguration]

### MappedDataSetParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MappedDataSetParameter]]


# IntegerParameterDeclarationOutput

### ParameterValueType
- **Type**: typing.Literal['MULTI_VALUED', 'SINGLE_VALUED']
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.IntegerDefaultValuesOutput]

### ValueWhenUnset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.IntegerValueWhenUnsetConfiguration]

### MappedDataSetParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MappedDataSetParameter]]


# IntegerParameterOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.List[int]
- **Required**: Yes


# IntegerValueWhenUnsetConfiguration

### ValueWhenUnsetOption
- **Type**: typing.Optional[typing.Literal['NULL', 'RECOMMENDED_VALUE']]

### CustomValue
- **Type**: typing.Optional[int]


# InvalidTopicReviewedAnswer

### AnswerId
- **Type**: typing.Optional[str]

### Error
- **Type**: typing.Optional[typing.Literal['DATASET_DOES_NOT_EXIST', 'DUPLICATED_ANSWER', 'INTERNAL_ERROR', 'INVALID_DATA', 'INVALID_DATASET_ARN', 'MISSING_ANSWER', 'MISSING_REQUIRED_FIELDS']]


# ItemsLimitConfiguration

### ItemsLimit
- **Type**: typing.Optional[int]

### OtherCategories
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]


# JiraParameters

### SiteBaseUrl
- **Type**: <class 'str'>
- **Required**: Yes


# JoinInstruction

### LeftOperand
- **Type**: <class 'str'>
- **Required**: Yes

### RightOperand
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['INNER', 'LEFT', 'OUTER', 'RIGHT']
- **Required**: Yes

### OnClause
- **Type**: <class 'str'>
- **Required**: Yes

### LeftJoinKeyProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.JoinKeyProperties]

### RightJoinKeyProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.JoinKeyProperties]


# JoinKeyProperties

### UniqueKey
- **Type**: typing.Optional[bool]


# KPIActualValueConditionalFormatting

### TextColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingColor]

### Icon
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingIcon]


# KPIActualValueConditionalFormattingOutput

### TextColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingColorOutput]

### Icon
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingIcon]


# KPIComparisonValueConditionalFormatting

### TextColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingColor]

### Icon
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingIcon]


# KPIComparisonValueConditionalFormattingOutput

### TextColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingColorOutput]

### Icon
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingIcon]


# KPIConditionalFormatting

### ConditionalFormattingOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.KPIConditionalFormattingOption]]


# KPIConditionalFormattingOption

### PrimaryValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.KPIPrimaryValueConditionalFormatting]

### ProgressBar
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.KPIProgressBarConditionalFormatting]

### ActualValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.KPIActualValueConditionalFormatting]

### ComparisonValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.KPIComparisonValueConditionalFormatting]


# KPIConditionalFormattingOptionOutput

### PrimaryValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.KPIPrimaryValueConditionalFormattingOutput]

### ProgressBar
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.KPIProgressBarConditionalFormattingOutput]

### ActualValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.KPIActualValueConditionalFormattingOutput]

### ComparisonValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.KPIComparisonValueConditionalFormattingOutput]


# KPIConditionalFormattingOutput

### ConditionalFormattingOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.KPIConditionalFormattingOptionOutput]]


# KPIConfiguration

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.KPIFieldWells]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.KPISortConfiguration]

### KPIOptions
- **Type**: <class 'NoneType'>

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# KPIConfigurationOutput

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.KPIFieldWellsOutput]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.KPISortConfigurationOutput]

### KPIOptions
- **Type**: <class 'NoneType'>

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# KPIFieldWells

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]

### TargetValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]

### TrendGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]


# KPIFieldWellsOutput

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]

### TargetValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]

### TrendGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]


# KPIOptions

### ProgressBar
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ProgressBarOptions]

### TrendArrows
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TrendArrowOptions]

### SecondaryValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SecondaryValueOptions]

### Comparison
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ComparisonConfiguration]

### PrimaryValueDisplayType
- **Type**: typing.Optional[typing.Literal['ACTUAL', 'COMPARISON', 'HIDDEN']]

### PrimaryValueFontConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FontConfiguration]

### SecondaryValueFontConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FontConfiguration]

### Sparkline
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.KPISparklineOptions]

### VisualLayoutOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.KPIVisualLayoutOptions]


# KPIPrimaryValueConditionalFormatting

### TextColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingColor]

### Icon
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingIcon]


# KPIPrimaryValueConditionalFormattingOutput

### TextColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingColorOutput]

### Icon
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingIcon]


# KPIProgressBarConditionalFormatting

### ForegroundColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingColor]


# KPIProgressBarConditionalFormattingOutput

### ForegroundColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingColorOutput]


# KPISortConfiguration

### TrendGroupSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]


# KPISortConfigurationOutput

### TrendGroupSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]


# KPISparklineOptions

### Type
- **Type**: typing.Literal['AREA', 'LINE']
- **Required**: Yes

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### Color
- **Type**: typing.Optional[str]

### TooltipVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# KPIVisual

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.KPIConfiguration]

### ConditionalFormatting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.KPIConditionalFormatting]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomAction]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnHierarchy]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# KPIVisualLayoutOptions

### StandardLayout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.KPIVisualStandardLayout]


# KPIVisualOutput

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.KPIConfigurationOutput]

### ConditionalFormatting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.KPIConditionalFormattingOutput]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomActionOutput]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnHierarchyOutput]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# KPIVisualStandardLayout

### Type
- **Type**: typing.Literal['CLASSIC', 'VERTICAL']
- **Required**: Yes


# LabelOptions

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### FontConfiguration
- **Type**: <class 'NoneType'>

### CustomLabel
- **Type**: typing.Optional[str]


# LayerCustomAction

### CustomActionId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Trigger
- **Type**: typing.Literal['DATA_POINT_CLICK', 'DATA_POINT_MENU']
- **Required**: Yes

### ActionOperations
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LayerCustomActionOperation]
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# LayerCustomActionOperation

### FilterOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CustomActionFilterOperation]

### NavigationOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CustomActionNavigationOperation]

### URLOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CustomActionURLOperation]

### SetParametersOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CustomActionSetParametersOperation]


# LayerCustomActionOperationOutput

### FilterOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CustomActionFilterOperationOutput]

### NavigationOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CustomActionNavigationOperation]

### URLOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CustomActionURLOperation]

### SetParametersOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CustomActionSetParametersOperationOutput]


# LayerCustomActionOutput

### CustomActionId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Trigger
- **Type**: typing.Literal['DATA_POINT_CLICK', 'DATA_POINT_MENU']
- **Required**: Yes

### ActionOperations
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LayerCustomActionOperationOutput]
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# LayerMapVisual

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialLayerMapConfiguration]

### VisualContentAltText
- **Type**: typing.Optional[str]


# LayerMapVisualOutput

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialLayerMapConfigurationOutput]

### VisualContentAltText
- **Type**: typing.Optional[str]


# Layout

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LayoutConfiguration'>
- **Required**: Yes


# LayoutConfiguration

### GridLayout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GridLayoutConfiguration]

### FreeFormLayout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FreeFormLayoutConfiguration]

### SectionBasedLayout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SectionBasedLayoutConfiguration]


# LayoutConfigurationOutput

### GridLayout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GridLayoutConfigurationOutput]

### FreeFormLayout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FreeFormLayoutConfigurationOutput]

### SectionBasedLayout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SectionBasedLayoutConfigurationOutput]


# LayoutOutput

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LayoutConfigurationOutput'>
- **Required**: Yes


# LegendOptions

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LabelOptions]

### Position
- **Type**: typing.Optional[typing.Literal['AUTO', 'BOTTOM', 'RIGHT', 'TOP']]

### Width
- **Type**: typing.Optional[str]

### Height
- **Type**: typing.Optional[str]

### ValueFontConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FontConfiguration]


# LineChartAggregatedFieldWells

### Category
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]

### Colors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### SmallMultiples
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]


# LineChartAggregatedFieldWellsOutput

### Category
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]

### Colors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### SmallMultiples
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]


# LineChartConfiguration

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LineChartFieldWells]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LineChartSortConfiguration]

### ForecastConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ForecastConfiguration]]

### Type
- **Type**: typing.Optional[typing.Literal['AREA', 'LINE', 'STACKED_AREA']]

### SmallMultiplesOptions
- **Type**: <class 'NoneType'>

### XAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDisplayOptions]

### XAxisLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptions]

### PrimaryYAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LineSeriesAxisDisplayOptions]

### PrimaryYAxisLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptions]

### SecondaryYAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LineSeriesAxisDisplayOptions]

### SecondaryYAxisLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptions]

### SingleAxisOptions
- **Type**: <class 'NoneType'>

### DefaultSeriesSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LineChartDefaultSeriesSettings]

### Series
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SeriesItem]]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LegendOptions]

### DataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataLabelOptions]

### ReferenceLines
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ReferenceLine]]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TooltipOptions]

### ContributionAnalysisDefaults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ContributionAnalysisDefault]]

### VisualPalette
- **Type**: <class 'NoneType'>

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# LineChartConfigurationOutput

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LineChartFieldWellsOutput]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LineChartSortConfigurationOutput]

### ForecastConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ForecastConfigurationOutput]]

### Type
- **Type**: typing.Optional[typing.Literal['AREA', 'LINE', 'STACKED_AREA']]

### SmallMultiplesOptions
- **Type**: <class 'NoneType'>

### XAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDisplayOptionsOutput]

### XAxisLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptionsOutput]

### PrimaryYAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LineSeriesAxisDisplayOptionsOutput]

### PrimaryYAxisLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptionsOutput]

### SecondaryYAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LineSeriesAxisDisplayOptionsOutput]

### SecondaryYAxisLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptionsOutput]

### SingleAxisOptions
- **Type**: <class 'NoneType'>

### DefaultSeriesSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LineChartDefaultSeriesSettings]

### Series
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SeriesItem]]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LegendOptions]

### DataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataLabelOptionsOutput]

### ReferenceLines
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ReferenceLine]]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TooltipOptionsOutput]

### ContributionAnalysisDefaults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ContributionAnalysisDefaultOutput]]

### VisualPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualPaletteOutput]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# LineChartDefaultSeriesSettings

### AxisBinding
- **Type**: typing.Optional[typing.Literal['PRIMARY_YAXIS', 'SECONDARY_YAXIS']]

### LineStyleSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LineChartLineStyleSettings]

### MarkerStyleSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LineChartMarkerStyleSettings]


# LineChartFieldWells

### LineChartAggregatedFieldWells
- **Type**: <class 'NoneType'>


# LineChartFieldWellsOutput

### LineChartAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LineChartAggregatedFieldWellsOutput]


# LineChartLineStyleSettings

### LineVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### LineInterpolation
- **Type**: typing.Optional[typing.Literal['LINEAR', 'SMOOTH', 'STEPPED']]

### LineStyle
- **Type**: typing.Optional[typing.Literal['DASHED', 'DOTTED', 'SOLID']]

### LineWidth
- **Type**: typing.Optional[str]


# LineChartMarkerStyleSettings

### MarkerVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### MarkerShape
- **Type**: typing.Optional[typing.Literal['CIRCLE', 'DIAMOND', 'ROUNDED_SQUARE', 'SQUARE', 'TRIANGLE']]

### MarkerSize
- **Type**: typing.Optional[str]

### MarkerColor
- **Type**: typing.Optional[str]


# LineChartSeriesSettings

### LineStyleSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LineChartLineStyleSettings]

### MarkerStyleSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LineChartMarkerStyleSettings]


# LineChartSortConfiguration

### CategorySort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### CategoryItemsLimitConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]

### ColorItemsLimitConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]

### SmallMultiplesSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### SmallMultiplesLimitConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]


# LineChartSortConfigurationOutput

### CategorySort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### CategoryItemsLimitConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]

### ColorItemsLimitConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]

### SmallMultiplesSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### SmallMultiplesLimitConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]


# LineChartVisual

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LineChartConfiguration]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomAction]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnHierarchy]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# LineChartVisualOutput

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LineChartConfigurationOutput]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomActionOutput]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnHierarchyOutput]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# LineSeriesAxisDisplayOptions

### AxisOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDisplayOptions]

### MissingDataConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MissingDataConfiguration]]


# LineSeriesAxisDisplayOptionsOutput

### AxisOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDisplayOptionsOutput]

### MissingDataConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MissingDataConfiguration]]


# LinkSharingConfiguration

### Permissions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermission]]


# LinkSharingConfigurationOutput

### Permissions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]]


# ListAnalysesRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAnalysesRequestPaginate

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PaginatorConfig]


# ListAnalysesResponse

### AnalysisSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AnalysisSummary]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAssetBundleExportJobsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAssetBundleExportJobsRequestPaginate

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PaginatorConfig]


# ListAssetBundleExportJobsResponse

### AssetBundleExportJobSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleExportJobSummary]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAssetBundleImportJobsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAssetBundleImportJobsRequestPaginate

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PaginatorConfig]


# ListAssetBundleImportJobsResponse

### AssetBundleImportJobSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobSummary]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListBrandsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListBrandsRequestPaginate

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PaginatorConfig]


# ListBrandsResponse

### Brands
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BrandSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListControlDisplayOptions

### SearchOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ListControlSearchOptions]

### SelectAllOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ListControlSelectAllOptions]

### TitleOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LabelOptions]

### InfoIconLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SheetControlInfoIconLabelOptions]


# ListControlSearchOptions

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# ListControlSelectAllOptions

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# ListCustomPermissionsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCustomPermissionsRequestPaginate

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PaginatorConfig]


# ListCustomPermissionsResponse

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### CustomPermissionsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CustomPermissions]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDashboardVersionsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDashboardVersionsRequestPaginate

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PaginatorConfig]


# ListDashboardVersionsResponse

### DashboardVersionSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DashboardVersionSummary]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDashboardsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDashboardsRequestPaginate

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PaginatorConfig]


# ListDashboardsResponse

### DashboardSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DashboardSummary]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDataSetsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDataSetsRequestPaginate

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PaginatorConfig]


# ListDataSetsResponse

### DataSetSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataSetSummary]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDataSourcesRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDataSourcesRequestPaginate

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PaginatorConfig]


# ListDataSourcesResponse

### DataSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataSource]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFolderMembersRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListFolderMembersRequestPaginate

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PaginatorConfig]


# ListFolderMembersResponse

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### FolderMemberList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MemberIdArnPair]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFoldersForResourceRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListFoldersForResourceRequestPaginate

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PaginatorConfig]


# ListFoldersForResourceResponse

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### Folders
- **Type**: typing.List[str]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFoldersRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListFoldersRequestPaginate

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PaginatorConfig]


# ListFoldersResponse

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### FolderSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FolderSummary]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGroupMembershipsRequest

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListGroupMembershipsRequestPaginate

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PaginatorConfig]


# ListGroupMembershipsResponse

### GroupMemberList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GroupMember]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGroupsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListGroupsRequestPaginate

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PaginatorConfig]


# ListGroupsResponse

### GroupList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Group]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIAMPolicyAssignmentsForUserRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListIAMPolicyAssignmentsForUserRequestPaginate

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PaginatorConfig]


# ListIAMPolicyAssignmentsForUserResponse

### ActiveAssignments
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ActiveIAMPolicyAssignment]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIAMPolicyAssignmentsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### AssignmentStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'DRAFT', 'ENABLED']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListIAMPolicyAssignmentsRequestPaginate

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### AssignmentStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'DRAFT', 'ENABLED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PaginatorConfig]


# ListIAMPolicyAssignmentsResponse

### IAMPolicyAssignments
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.IAMPolicyAssignmentSummary]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIdentityPropagationConfigsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListIdentityPropagationConfigsResponse

### Services
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AuthorizedTargetsByService]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIngestionsRequest

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListIngestionsRequestPaginate

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PaginatorConfig]


# ListIngestionsResponse

### Ingestions
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Ingestion]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNamespacesRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListNamespacesRequestPaginate

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PaginatorConfig]


# ListNamespacesResponse

### Namespaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.NamespaceInfoV2]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRefreshSchedulesRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes


# ListRefreshSchedulesResponse

### RefreshSchedules
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RefreshScheduleOutput]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# ListRoleMembershipsRequest

### Role
- **Type**: typing.Literal['ADMIN', 'ADMIN_PRO', 'AUTHOR', 'AUTHOR_PRO', 'READER', 'READER_PRO']
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListRoleMembershipsRequestPaginate

### Role
- **Type**: typing.Literal['ADMIN', 'ADMIN_PRO', 'AUTHOR', 'AUTHOR_PRO', 'READER', 'READER_PRO']
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PaginatorConfig]


# ListRoleMembershipsResponse

### MembersList
- **Type**: typing.List[str]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Tag]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# ListTemplateAliasesRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTemplateAliasesRequestPaginate

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PaginatorConfig]


# ListTemplateAliasesResponse

### TemplateAliasList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TemplateAlias]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTemplateVersionsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTemplateVersionsRequestPaginate

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PaginatorConfig]


# ListTemplateVersionsResponse

### TemplateVersionSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TemplateVersionSummary]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTemplatesRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTemplatesRequestPaginate

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PaginatorConfig]


# ListTemplatesResponse

### TemplateSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TemplateSummary]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListThemeAliasesRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ThemeId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListThemeAliasesResponse

### ThemeAliasList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ThemeAlias]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListThemeVersionsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ThemeId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListThemeVersionsRequestPaginate

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ThemeId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PaginatorConfig]


# ListThemeVersionsResponse

### ThemeVersionSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ThemeVersionSummary]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListThemesRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Type
- **Type**: typing.Optional[typing.Literal['ALL', 'CUSTOM', 'QUICKSIGHT']]


# ListThemesRequestPaginate

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Optional[typing.Literal['ALL', 'CUSTOM', 'QUICKSIGHT']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PaginatorConfig]


# ListThemesResponse

### ThemeSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ThemeSummary]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTopicRefreshSchedulesRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes


# ListTopicRefreshSchedulesResponse

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### RefreshSchedules
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicRefreshScheduleSummary]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# ListTopicReviewedAnswersRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes


# ListTopicReviewedAnswersResponse

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### Answers
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicReviewedAnswer]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# ListTopicsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTopicsResponse

### TopicsSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicSummary]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListUserGroupsRequest

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListUserGroupsRequestPaginate

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PaginatorConfig]


# ListUserGroupsResponse

### GroupList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Group]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListUsersRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListUsersRequestPaginate

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PaginatorConfig]


# ListUsersResponse

### UserList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.User]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListVPCConnectionsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListVPCConnectionsResponse

### VPCConnectionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VPCConnectionSummary]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LoadingAnimation

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# LocalNavigationConfiguration

### TargetSheetId
- **Type**: <class 'str'>
- **Required**: Yes


# LogicalTable

### Alias
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LogicalTableSource'>
- **Required**: Yes

### DataTransforms
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TransformOperation, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TransformOperationOutput]]]


# LogicalTableOutput

### Alias
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LogicalTableSource'>
- **Required**: Yes

### DataTransforms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TransformOperationOutput]]


# LogicalTableSource

### JoinInstruction
- **Type**: <class 'NoneType'>

### PhysicalTableId
- **Type**: typing.Optional[str]

### DataSetArn
- **Type**: typing.Optional[str]


# Logo

### AltText
- **Type**: <class 'str'>
- **Required**: Yes

### LogoSet
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LogoSet'>
- **Required**: Yes


# LogoConfiguration

### AltText
- **Type**: <class 'str'>
- **Required**: Yes

### LogoSet
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LogoSetConfiguration'>
- **Required**: Yes


# LogoSet

### Primary
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ImageSet'>
- **Required**: Yes

### Favicon
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ImageSet]


# LogoSetConfiguration

### Primary
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ImageSetConfiguration'>
- **Required**: Yes

### Favicon
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ImageSetConfiguration]


# LongFormatText

### PlainText
- **Type**: typing.Optional[str]

### RichText
- **Type**: typing.Optional[str]


# LookbackWindow

### ColumnName
- **Type**: <class 'str'>
- **Required**: Yes

### Size
- **Type**: <class 'int'>
- **Required**: Yes

### SizeUnit
- **Type**: typing.Literal['DAY', 'HOUR', 'WEEK']
- **Required**: Yes


# ManifestFileLocation

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Key
- **Type**: <class 'str'>
- **Required**: Yes


# MappedDataSetParameter

### DataSetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetParameterName
- **Type**: <class 'str'>
- **Required**: Yes


# MarginStyle

### Show
- **Type**: typing.Optional[bool]


# MariaDbParameters

### Host
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes


# MaximumLabelType

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# MaximumMinimumComputation

### ComputationId
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['MAXIMUM', 'MINIMUM']
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Time
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]

### Value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]


# MeasureField

### NumericalMeasureField
- **Type**: <class 'NoneType'>

### CategoricalMeasureField
- **Type**: <class 'NoneType'>

### DateMeasureField
- **Type**: <class 'NoneType'>

### CalculatedMeasureField
- **Type**: <class 'NoneType'>


# MemberIdArnPair

### MemberId
- **Type**: typing.Optional[str]

### MemberArn
- **Type**: typing.Optional[str]


# MetricComparisonComputation

### ComputationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Time
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]

### FromValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]

### TargetValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]


# MinimumLabelType

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# MissingDataConfiguration

### TreatmentOption
- **Type**: typing.Optional[typing.Literal['INTERPOLATE', 'SHOW_AS_BLANK', 'SHOW_AS_ZERO']]


# MySqlParameters

### Host
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes


# NamedEntityDefinition

### FieldName
- **Type**: typing.Optional[str]

### PropertyName
- **Type**: typing.Optional[str]

### PropertyRole
- **Type**: typing.Optional[typing.Literal['ID', 'PRIMARY']]

### PropertyUsage
- **Type**: typing.Optional[typing.Literal['DIMENSION', 'INHERIT', 'MEASURE']]

### Metric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.NamedEntityDefinitionMetric]


# NamedEntityDefinitionMetric

### Aggregation
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'COUNT', 'CUSTOM', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'PERCENTILE', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]

### AggregationFunctionParameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# NamedEntityDefinitionMetricOutput

### Aggregation
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'COUNT', 'CUSTOM', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'PERCENTILE', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]

### AggregationFunctionParameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# NamedEntityDefinitionOutput

### FieldName
- **Type**: typing.Optional[str]

### PropertyName
- **Type**: typing.Optional[str]

### PropertyRole
- **Type**: typing.Optional[typing.Literal['ID', 'PRIMARY']]

### PropertyUsage
- **Type**: typing.Optional[typing.Literal['DIMENSION', 'INHERIT', 'MEASURE']]

### Metric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.NamedEntityDefinitionMetricOutput]


# NamedEntityRef

### NamedEntityName
- **Type**: typing.Optional[str]


# NamespaceError

### Type
- **Type**: typing.Optional[typing.Literal['INTERNAL_SERVICE_ERROR', 'PERMISSION_DENIED']]

### Message
- **Type**: typing.Optional[str]


# NamespaceInfoV2

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### CapacityRegion
- **Type**: typing.Optional[str]

### CreationStatus
- **Type**: typing.Optional[typing.Literal['CREATED', 'CREATING', 'DELETING', 'NON_RETRYABLE_FAILURE', 'RETRYABLE_FAILURE']]

### IdentityStore
- **Type**: typing.Optional[typing.Literal['QUICKSIGHT']]

### NamespaceError
- **Type**: <class 'NoneType'>

### IamIdentityCenterApplicationArn
- **Type**: typing.Optional[str]

### IamIdentityCenterInstanceArn
- **Type**: typing.Optional[str]


# NavbarStyle

### GlobalNavbar
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Palette]

### ContextualNavbar
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Palette]


# NegativeFormat

### Prefix
- **Type**: typing.Optional[str]

### Suffix
- **Type**: typing.Optional[str]


# NegativeValueConfiguration

### DisplayMode
- **Type**: typing.Literal['NEGATIVE', 'POSITIVE']
- **Required**: Yes


# NestedFilter

### FilterId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### IncludeInnerSet
- **Type**: <class 'bool'>
- **Required**: Yes

### InnerFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.InnerFilter'>
- **Required**: Yes


# NestedFilterOutput

### FilterId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### IncludeInnerSet
- **Type**: <class 'bool'>
- **Required**: Yes

### InnerFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.InnerFilterOutput'>
- **Required**: Yes


# NetworkInterface

### SubnetId
- **Type**: typing.Optional[str]

### AvailabilityZone
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ATTACHMENT_FAILED_ROLLBACK_FAILED', 'AVAILABLE', 'CREATING', 'CREATION_FAILED', 'DELETED', 'DELETING', 'DELETION_FAILED', 'DELETION_SCHEDULED', 'UPDATE_FAILED', 'UPDATING']]

### NetworkInterfaceId
- **Type**: typing.Optional[str]


# NewDefaultValues

### StringStaticValues
- **Type**: typing.Optional[typing.List[str]]

### DecimalStaticValues
- **Type**: typing.Optional[typing.List[float]]

### DateTimeStaticValues
- **Type**: typing.Optional[typing.List[typing.Union[datetime.datetime, str]]]

### IntegerStaticValues
- **Type**: typing.Optional[typing.List[int]]


# NewDefaultValuesOutput

### StringStaticValues
- **Type**: typing.Optional[typing.List[str]]

### DecimalStaticValues
- **Type**: typing.Optional[typing.List[float]]

### DateTimeStaticValues
- **Type**: typing.Optional[typing.List[datetime.datetime]]

### IntegerStaticValues
- **Type**: typing.Optional[typing.List[int]]


# NullValueFormatConfiguration

### NullString
- **Type**: <class 'str'>
- **Required**: Yes


# NumberDisplayFormatConfiguration

### Prefix
- **Type**: typing.Optional[str]

### Suffix
- **Type**: typing.Optional[str]

### SeparatorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.NumericSeparatorConfiguration]

### DecimalPlacesConfiguration
- **Type**: <class 'NoneType'>

### NumberScale
- **Type**: typing.Optional[typing.Literal['AUTO', 'BILLIONS', 'CRORES', 'LAKHS', 'MILLIONS', 'NONE', 'THOUSANDS', 'TRILLIONS']]

### NegativeValueConfiguration
- **Type**: <class 'NoneType'>

### NullValueFormatConfiguration
- **Type**: <class 'NoneType'>


# NumberFormatConfiguration

### FormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.NumericFormatConfiguration]


# NumericAxisOptions

### Scale
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisScale]

### Range
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDisplayRange]


# NumericAxisOptionsOutput

### Scale
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisScale]

### Range
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDisplayRangeOutput]


# NumericEqualityDrillDownFilter

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### Value
- **Type**: <class 'float'>
- **Required**: Yes


# NumericEqualityFilter

### FilterId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### MatchOperator
- **Type**: typing.Literal['DOES_NOT_EQUAL', 'EQUALS']
- **Required**: Yes

### NullOption
- **Type**: typing.Literal['ALL_VALUES', 'NON_NULLS_ONLY', 'NULLS_ONLY']
- **Required**: Yes

### Value
- **Type**: typing.Optional[float]

### SelectAllOptions
- **Type**: typing.Optional[typing.Literal['FILTER_ALL_VALUES']]

### AggregationFunction
- **Type**: <class 'NoneType'>

### ParameterName
- **Type**: typing.Optional[str]

### DefaultFilterControlConfiguration
- **Type**: <class 'NoneType'>


# NumericEqualityFilterOutput

### FilterId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### MatchOperator
- **Type**: typing.Literal['DOES_NOT_EQUAL', 'EQUALS']
- **Required**: Yes

### NullOption
- **Type**: typing.Literal['ALL_VALUES', 'NON_NULLS_ONLY', 'NULLS_ONLY']
- **Required**: Yes

### Value
- **Type**: typing.Optional[float]

### SelectAllOptions
- **Type**: typing.Optional[typing.Literal['FILTER_ALL_VALUES']]

### AggregationFunction
- **Type**: <class 'NoneType'>

### ParameterName
- **Type**: typing.Optional[str]

### DefaultFilterControlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DefaultFilterControlConfigurationOutput]


# NumericFormatConfiguration

### NumberDisplayFormatConfiguration
- **Type**: <class 'NoneType'>

### CurrencyDisplayFormatConfiguration
- **Type**: <class 'NoneType'>

### PercentageDisplayFormatConfiguration
- **Type**: <class 'NoneType'>


# NumericRangeFilter

### FilterId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### NullOption
- **Type**: typing.Literal['ALL_VALUES', 'NON_NULLS_ONLY', 'NULLS_ONLY']
- **Required**: Yes

### IncludeMinimum
- **Type**: typing.Optional[bool]

### IncludeMaximum
- **Type**: typing.Optional[bool]

### RangeMinimum
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.NumericRangeFilterValue]

### RangeMaximum
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.NumericRangeFilterValue]

### SelectAllOptions
- **Type**: typing.Optional[typing.Literal['FILTER_ALL_VALUES']]

### AggregationFunction
- **Type**: <class 'NoneType'>

### DefaultFilterControlConfiguration
- **Type**: <class 'NoneType'>


# NumericRangeFilterOutput

### FilterId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### NullOption
- **Type**: typing.Literal['ALL_VALUES', 'NON_NULLS_ONLY', 'NULLS_ONLY']
- **Required**: Yes

### IncludeMinimum
- **Type**: typing.Optional[bool]

### IncludeMaximum
- **Type**: typing.Optional[bool]

### RangeMinimum
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.NumericRangeFilterValue]

### RangeMaximum
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.NumericRangeFilterValue]

### SelectAllOptions
- **Type**: typing.Optional[typing.Literal['FILTER_ALL_VALUES']]

### AggregationFunction
- **Type**: <class 'NoneType'>

### DefaultFilterControlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DefaultFilterControlConfigurationOutput]


# NumericRangeFilterValue

### StaticValue
- **Type**: typing.Optional[float]

### Parameter
- **Type**: typing.Optional[str]


# NumericSeparatorConfiguration

### DecimalSeparator
- **Type**: typing.Optional[typing.Literal['COMMA', 'DOT', 'SPACE']]

### ThousandsSeparator
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ThousandSeparatorOptions]


# NumericalAggregationFunction

### SimpleNumericalAggregation
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'COUNT', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]

### PercentileAggregation
- **Type**: <class 'NoneType'>


# NumericalDimensionField

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### HierarchyId
- **Type**: typing.Optional[str]

### FormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.NumberFormatConfiguration]


# NumericalMeasureField

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### AggregationFunction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.NumericalAggregationFunction]

### FormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.NumberFormatConfiguration]


# OAuthParameters

### TokenProviderUrl
- **Type**: <class 'str'>
- **Required**: Yes

### OAuthScope
- **Type**: typing.Optional[str]

### IdentityProviderVpcConnectionProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VpcConnectionProperties]

### IdentityProviderResourceUri
- **Type**: typing.Optional[str]


# OracleParameters

### Host
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes


# OutputColumn

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['DATETIME', 'DECIMAL', 'INTEGER', 'STRING']]

### SubType
- **Type**: typing.Optional[typing.Literal['FIXED', 'FLOAT']]


# OverrideDatasetParameterOperation

### ParameterName
- **Type**: <class 'str'>
- **Required**: Yes

### NewParameterName
- **Type**: typing.Optional[str]

### NewDefaultValues
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.NewDefaultValues, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.NewDefaultValuesOutput, NoneType]


# OverrideDatasetParameterOperationOutput

### ParameterName
- **Type**: <class 'str'>
- **Required**: Yes

### NewParameterName
- **Type**: typing.Optional[str]

### NewDefaultValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.NewDefaultValuesOutput]


# PaginationConfiguration

### PageSize
- **Type**: <class 'int'>
- **Required**: Yes

### PageNumber
- **Type**: <class 'int'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Palette

### Foreground
- **Type**: typing.Optional[str]

### Background
- **Type**: typing.Optional[str]


# PanelConfiguration

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PanelTitleOptions]

### BorderVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### BorderThickness
- **Type**: typing.Optional[str]

### BorderStyle
- **Type**: typing.Optional[typing.Literal['DASHED', 'DOTTED', 'SOLID']]

### BorderColor
- **Type**: typing.Optional[str]

### GutterVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### GutterSpacing
- **Type**: typing.Optional[str]

### BackgroundVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### BackgroundColor
- **Type**: typing.Optional[str]


# PanelTitleOptions

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### FontConfiguration
- **Type**: <class 'NoneType'>

### HorizontalTextAlignment
- **Type**: typing.Optional[typing.Literal['AUTO', 'CENTER', 'LEFT', 'RIGHT']]


# ParameterControl

### DateTimePicker
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ParameterDateTimePickerControl]

### List
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ParameterListControl]

### Dropdown
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ParameterDropDownControl]

### TextField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ParameterTextFieldControl]

### TextArea
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ParameterTextAreaControl]

### Slider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ParameterSliderControl]


# ParameterControlOutput

### DateTimePicker
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ParameterDateTimePickerControl]

### List
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ParameterListControlOutput]

### Dropdown
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ParameterDropDownControlOutput]

### TextField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ParameterTextFieldControl]

### TextArea
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ParameterTextAreaControl]

### Slider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ParameterSliderControl]


# ParameterDateTimePickerControl

### ParameterControlId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### SourceParameterName
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DateTimePickerControlDisplayOptions]


# ParameterDeclaration

### StringParameterDeclaration
- **Type**: <class 'NoneType'>

### DecimalParameterDeclaration
- **Type**: <class 'NoneType'>

### IntegerParameterDeclaration
- **Type**: <class 'NoneType'>

### DateTimeParameterDeclaration
- **Type**: <class 'NoneType'>


# ParameterDeclarationOutput

### StringParameterDeclaration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.StringParameterDeclarationOutput]

### DecimalParameterDeclaration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DecimalParameterDeclarationOutput]

### IntegerParameterDeclaration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.IntegerParameterDeclarationOutput]

### DateTimeParameterDeclaration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DateTimeParameterDeclarationOutput]


# ParameterDropDownControl

### ParameterControlId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### SourceParameterName
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DropDownControlDisplayOptions]

### Type
- **Type**: typing.Optional[typing.Literal['MULTI_SELECT', 'SINGLE_SELECT']]

### SelectableValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ParameterSelectableValues]

### CascadingControlConfiguration
- **Type**: <class 'NoneType'>

### CommitMode
- **Type**: typing.Optional[typing.Literal['AUTO', 'MANUAL']]


# ParameterDropDownControlOutput

### ParameterControlId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### SourceParameterName
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DropDownControlDisplayOptions]

### Type
- **Type**: typing.Optional[typing.Literal['MULTI_SELECT', 'SINGLE_SELECT']]

### SelectableValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ParameterSelectableValuesOutput]

### CascadingControlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CascadingControlConfigurationOutput]

### CommitMode
- **Type**: typing.Optional[typing.Literal['AUTO', 'MANUAL']]


# ParameterListControl

### ParameterControlId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### SourceParameterName
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ListControlDisplayOptions]

### Type
- **Type**: typing.Optional[typing.Literal['MULTI_SELECT', 'SINGLE_SELECT']]

### SelectableValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ParameterSelectableValues]

### CascadingControlConfiguration
- **Type**: <class 'NoneType'>


# ParameterListControlOutput

### ParameterControlId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### SourceParameterName
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ListControlDisplayOptions]

### Type
- **Type**: typing.Optional[typing.Literal['MULTI_SELECT', 'SINGLE_SELECT']]

### SelectableValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ParameterSelectableValuesOutput]

### CascadingControlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CascadingControlConfigurationOutput]


# ParameterSelectableValues

### Values
- **Type**: typing.Optional[typing.List[str]]

### LinkToDataSetColumn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier]


# ParameterSelectableValuesOutput

### Values
- **Type**: typing.Optional[typing.List[str]]

### LinkToDataSetColumn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier]


# ParameterSliderControl

### ParameterControlId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### SourceParameterName
- **Type**: <class 'str'>
- **Required**: Yes

### MaximumValue
- **Type**: <class 'float'>
- **Required**: Yes

### MinimumValue
- **Type**: <class 'float'>
- **Required**: Yes

### StepSize
- **Type**: <class 'float'>
- **Required**: Yes

### DisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SliderControlDisplayOptions]


# ParameterTextAreaControl

### ParameterControlId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### SourceParameterName
- **Type**: <class 'str'>
- **Required**: Yes

### Delimiter
- **Type**: typing.Optional[str]

### DisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TextAreaControlDisplayOptions]


# ParameterTextFieldControl

### ParameterControlId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### SourceParameterName
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TextFieldControlDisplayOptions]


# Parameters

### StringParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.StringParameter]]

### IntegerParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.IntegerParameter]]

### DecimalParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DecimalParameter]]

### DateTimeParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DateTimeParameter]]


# ParametersOutput

### StringParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.StringParameterOutput]]

### IntegerParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.IntegerParameterOutput]]

### DecimalParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DecimalParameterOutput]]

### DateTimeParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DateTimeParameterOutput]]


# PercentVisibleRange

### From
- **Type**: typing.Optional[float]

### To
- **Type**: typing.Optional[float]


# PercentageDisplayFormatConfiguration

### Prefix
- **Type**: typing.Optional[str]

### Suffix
- **Type**: typing.Optional[str]

### SeparatorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.NumericSeparatorConfiguration]

### DecimalPlacesConfiguration
- **Type**: <class 'NoneType'>

### NegativeValueConfiguration
- **Type**: <class 'NoneType'>

### NullValueFormatConfiguration
- **Type**: <class 'NoneType'>


# PercentileAggregation

### PercentileValue
- **Type**: typing.Optional[float]


# PerformanceConfiguration

### UniqueKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.UniqueKey]]


# PerformanceConfigurationOutput

### UniqueKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.UniqueKeyOutput]]


# PeriodOverPeriodComputation

### ComputationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Time
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]

### Value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]


# PeriodToDateComputation

### ComputationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Time
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]

### Value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]

### PeriodTimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]


# PhysicalTable

### RelationalTable
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RelationalTable, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RelationalTableOutput, NoneType]

### CustomSql
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CustomSql, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CustomSqlOutput, NoneType]

### S3Source
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.S3Source, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.S3SourceOutput, NoneType]


# PhysicalTableOutput

### RelationalTable
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RelationalTableOutput]

### CustomSql
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CustomSqlOutput]

### S3Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.S3SourceOutput]


# PieChartAggregatedFieldWells

### Category
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]

### SmallMultiples
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]


# PieChartAggregatedFieldWellsOutput

### Category
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]

### SmallMultiples
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]


# PieChartConfiguration

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PieChartFieldWells]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PieChartSortConfiguration]

### DonutOptions
- **Type**: <class 'NoneType'>

### SmallMultiplesOptions
- **Type**: <class 'NoneType'>

### CategoryLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptions]

### ValueLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptions]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LegendOptions]

### DataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataLabelOptions]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TooltipOptions]

### VisualPalette
- **Type**: <class 'NoneType'>

### ContributionAnalysisDefaults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ContributionAnalysisDefault]]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# PieChartConfigurationOutput

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PieChartFieldWellsOutput]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PieChartSortConfigurationOutput]

### DonutOptions
- **Type**: <class 'NoneType'>

### SmallMultiplesOptions
- **Type**: <class 'NoneType'>

### CategoryLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptionsOutput]

### ValueLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptionsOutput]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LegendOptions]

### DataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataLabelOptionsOutput]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TooltipOptionsOutput]

### VisualPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualPaletteOutput]

### ContributionAnalysisDefaults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ContributionAnalysisDefaultOutput]]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# PieChartFieldWells

### PieChartAggregatedFieldWells
- **Type**: <class 'NoneType'>


# PieChartFieldWellsOutput

### PieChartAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PieChartAggregatedFieldWellsOutput]


# PieChartSortConfiguration

### CategorySort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### CategoryItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]

### SmallMultiplesSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### SmallMultiplesLimitConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]


# PieChartSortConfigurationOutput

### CategorySort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### CategoryItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]

### SmallMultiplesSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### SmallMultiplesLimitConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]


# PieChartVisual

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PieChartConfiguration]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomAction]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnHierarchy]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# PieChartVisualOutput

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PieChartConfigurationOutput]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomActionOutput]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnHierarchyOutput]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# PivotFieldSortOptions

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### SortBy
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTableSortBy'>
- **Required**: Yes


# PivotFieldSortOptionsOutput

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### SortBy
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTableSortByOutput'>
- **Required**: Yes


# PivotTableAggregatedFieldWells

### Rows
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Columns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]


# PivotTableAggregatedFieldWellsOutput

### Rows
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Columns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]


# PivotTableCellConditionalFormatting

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### TextFormat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TextConditionalFormat]

### Scope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTableConditionalFormattingScope]

### Scopes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTableConditionalFormattingScope]]


# PivotTableCellConditionalFormattingOutput

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### TextFormat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TextConditionalFormatOutput]

### Scope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTableConditionalFormattingScope]

### Scopes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTableConditionalFormattingScope]]


# PivotTableConditionalFormatting

### ConditionalFormattingOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTableConditionalFormattingOption]]


# PivotTableConditionalFormattingOption

### Cell
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTableCellConditionalFormatting]


# PivotTableConditionalFormattingOptionOutput

### Cell
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTableCellConditionalFormattingOutput]


# PivotTableConditionalFormattingOutput

### ConditionalFormattingOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTableConditionalFormattingOptionOutput]]


# PivotTableConditionalFormattingScope

### Role
- **Type**: typing.Optional[typing.Literal['FIELD', 'FIELD_TOTAL', 'GRAND_TOTAL']]


# PivotTableConfiguration

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTableFieldWells]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTableSortConfiguration]

### TableOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTableOptions]

### TotalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTableTotalOptions]

### FieldOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTableFieldOptions]

### PaginatedReportOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTablePaginatedReportOptions]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# PivotTableConfigurationOutput

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTableFieldWellsOutput]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTableSortConfigurationOutput]

### TableOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTableOptionsOutput]

### TotalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTableTotalOptionsOutput]

### FieldOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTableFieldOptionsOutput]

### PaginatedReportOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTablePaginatedReportOptions]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# PivotTableDataPathOption

### DataPathList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataPathValue]
- **Required**: Yes

### Width
- **Type**: typing.Optional[str]


# PivotTableDataPathOptionOutput

### DataPathList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataPathValue]
- **Required**: Yes

### Width
- **Type**: typing.Optional[str]


# PivotTableFieldCollapseStateOption

### Target
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTableFieldCollapseStateTarget'>
- **Required**: Yes

### State
- **Type**: typing.Optional[typing.Literal['COLLAPSED', 'EXPANDED']]


# PivotTableFieldCollapseStateOptionOutput

### Target
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTableFieldCollapseStateTargetOutput'>
- **Required**: Yes

### State
- **Type**: typing.Optional[typing.Literal['COLLAPSED', 'EXPANDED']]


# PivotTableFieldCollapseStateTarget

### FieldId
- **Type**: typing.Optional[str]

### FieldDataPathValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataPathValue]]


# PivotTableFieldCollapseStateTargetOutput

### FieldId
- **Type**: typing.Optional[str]

### FieldDataPathValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataPathValue]]


# PivotTableFieldOption

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### CustomLabel
- **Type**: typing.Optional[str]

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# PivotTableFieldOptions

### SelectedFieldOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTableFieldOption]]

### DataPathOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTableDataPathOption]]

### CollapseStateOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTableFieldCollapseStateOption]]


# PivotTableFieldOptionsOutput

### SelectedFieldOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTableFieldOption]]

### DataPathOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTableDataPathOptionOutput]]

### CollapseStateOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTableFieldCollapseStateOptionOutput]]


# PivotTableFieldSubtotalOptions

### FieldId
- **Type**: typing.Optional[str]


# PivotTableFieldWells

### PivotTableAggregatedFieldWells
- **Type**: <class 'NoneType'>


# PivotTableFieldWellsOutput

### PivotTableAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTableAggregatedFieldWellsOutput]


# PivotTableOptions

### MetricPlacement
- **Type**: typing.Optional[typing.Literal['COLUMN', 'ROW']]

### SingleMetricVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### ColumnNamesVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### ToggleButtonsVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### ColumnHeaderStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableCellStyle]

### RowHeaderStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableCellStyle]

### CellStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableCellStyle]

### RowFieldNamesStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableCellStyle]

### RowAlternateColorOptions
- **Type**: <class 'NoneType'>

### CollapsedRowDimensionsVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### RowsLayout
- **Type**: typing.Optional[typing.Literal['HIERARCHY', 'TABULAR']]

### RowsLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTableRowsLabelOptions]

### DefaultCellWidth
- **Type**: typing.Optional[str]


# PivotTableOptionsOutput

### MetricPlacement
- **Type**: typing.Optional[typing.Literal['COLUMN', 'ROW']]

### SingleMetricVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### ColumnNamesVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### ToggleButtonsVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### ColumnHeaderStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableCellStyle]

### RowHeaderStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableCellStyle]

### CellStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableCellStyle]

### RowFieldNamesStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableCellStyle]

### RowAlternateColorOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RowAlternateColorOptionsOutput]

### CollapsedRowDimensionsVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### RowsLayout
- **Type**: typing.Optional[typing.Literal['HIERARCHY', 'TABULAR']]

### RowsLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTableRowsLabelOptions]

### DefaultCellWidth
- **Type**: typing.Optional[str]


# PivotTablePaginatedReportOptions

### VerticalOverflowVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### OverflowColumnHeaderVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# PivotTableRowsLabelOptions

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### CustomLabel
- **Type**: typing.Optional[str]


# PivotTableSortBy

### Field
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSort]

### Column
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnSort]

### DataPath
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataPathSort]


# PivotTableSortByOutput

### Field
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSort]

### Column
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnSort]

### DataPath
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataPathSortOutput]


# PivotTableSortConfiguration

### FieldSortOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotFieldSortOptions]]


# PivotTableSortConfigurationOutput

### FieldSortOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotFieldSortOptionsOutput]]


# PivotTableTotalOptions

### RowSubtotalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SubtotalOptions]

### ColumnSubtotalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SubtotalOptions]

### RowTotalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTotalOptions]

### ColumnTotalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTotalOptions]


# PivotTableTotalOptionsOutput

### RowSubtotalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SubtotalOptionsOutput]

### ColumnSubtotalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SubtotalOptionsOutput]

### RowTotalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTotalOptionsOutput]

### ColumnTotalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTotalOptionsOutput]


# PivotTableVisual

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTableConfiguration]

### ConditionalFormatting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTableConditionalFormatting]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomAction]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# PivotTableVisualOutput

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTableConfigurationOutput]

### ConditionalFormatting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTableConditionalFormattingOutput]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomActionOutput]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# PivotTotalOptions

### TotalsVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### Placement
- **Type**: typing.Optional[typing.Literal['AUTO', 'END', 'START']]

### ScrollStatus
- **Type**: typing.Optional[typing.Literal['PINNED', 'SCROLLED']]

### CustomLabel
- **Type**: typing.Optional[str]

### TotalCellStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableCellStyle]

### ValueCellStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableCellStyle]

### MetricHeaderCellStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableCellStyle]

### TotalAggregationOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TotalAggregationOption]]


# PivotTotalOptionsOutput

### TotalsVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### Placement
- **Type**: typing.Optional[typing.Literal['AUTO', 'END', 'START']]

### ScrollStatus
- **Type**: typing.Optional[typing.Literal['PINNED', 'SCROLLED']]

### CustomLabel
- **Type**: typing.Optional[str]

### TotalCellStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableCellStyle]

### ValueCellStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableCellStyle]

### MetricHeaderCellStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableCellStyle]

### TotalAggregationOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TotalAggregationOption]]


# PluginVisual

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### PluginArn
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PluginVisualConfiguration]

### VisualContentAltText
- **Type**: typing.Optional[str]


# PluginVisualConfiguration

### FieldWells
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PluginVisualFieldWell]]

### VisualOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PluginVisualOptions]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PluginVisualSortConfiguration]


# PluginVisualConfigurationOutput

### FieldWells
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PluginVisualFieldWellOutput]]

### VisualOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PluginVisualOptionsOutput]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PluginVisualSortConfigurationOutput]


# PluginVisualFieldWell

### AxisName
- **Type**: typing.Optional[typing.Literal['GROUP_BY', 'VALUE']]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Measures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]

### Unaggregated
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.UnaggregatedField]]


# PluginVisualFieldWellOutput

### AxisName
- **Type**: typing.Optional[typing.Literal['GROUP_BY', 'VALUE']]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Measures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]

### Unaggregated
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.UnaggregatedField]]


# PluginVisualItemsLimitConfiguration

### ItemsLimit
- **Type**: typing.Optional[int]


# PluginVisualOptions

### VisualProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PluginVisualProperty]]


# PluginVisualOptionsOutput

### VisualProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PluginVisualProperty]]


# PluginVisualOutput

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### PluginArn
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PluginVisualConfigurationOutput]

### VisualContentAltText
- **Type**: typing.Optional[str]


# PluginVisualProperty

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# PluginVisualSortConfiguration

### PluginVisualTableQuerySort
- **Type**: <class 'NoneType'>


# PluginVisualSortConfigurationOutput

### PluginVisualTableQuerySort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PluginVisualTableQuerySortOutput]


# PluginVisualTableQuerySort

### RowSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### ItemsLimitConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PluginVisualItemsLimitConfiguration]


# PluginVisualTableQuerySortOutput

### RowSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### ItemsLimitConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PluginVisualItemsLimitConfiguration]


# PostgreSqlParameters

### Host
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes


# PredefinedHierarchy

### HierarchyId
- **Type**: <class 'str'>
- **Required**: Yes

### Columns
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier]
- **Required**: Yes

### DrillDownFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DrillDownFilter]]


# PredefinedHierarchyOutput

### HierarchyId
- **Type**: <class 'str'>
- **Required**: Yes

### Columns
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier]
- **Required**: Yes

### DrillDownFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DrillDownFilterOutput]]


# PredictQAResultsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### QueryText
- **Type**: <class 'str'>
- **Required**: Yes

### IncludeQuickSightQIndex
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### IncludeGeneratedAnswer
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### MaxTopicsToConsider
- **Type**: typing.Optional[int]


# PredictQAResultsResponse

### PrimaryResult
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.QAResult'>
- **Required**: Yes

### AdditionalResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.QAResult]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# PrestoParameters

### Host
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes


# ProgressBarOptions

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# ProjectOperation

### ProjectedColumns
- **Type**: typing.List[str]
- **Required**: Yes


# ProjectOperationOutput

### ProjectedColumns
- **Type**: typing.List[str]
- **Required**: Yes


# PutDataSetRefreshPropertiesRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetRefreshProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataSetRefreshProperties'>
- **Required**: Yes


# PutDataSetRefreshPropertiesResponse

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# QAResult

### ResultType
- **Type**: typing.Optional[typing.Literal['DASHBOARD_VISUAL', 'GENERATED_ANSWER', 'NO_ANSWER']]

### DashboardVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DashboardVisualResult]

### GeneratedAnswer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeneratedAnswerResult]


# QueryExecutionOptions

### QueryExecutionMode
- **Type**: typing.Optional[typing.Literal['AUTO', 'MANUAL']]


# QueueInfo

### WaitingOnIngestion
- **Type**: <class 'str'>
- **Required**: Yes

### QueuedIngestion
- **Type**: <class 'str'>
- **Required**: Yes


# RadarChartAggregatedFieldWells

### Category
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Color
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]


# RadarChartAggregatedFieldWellsOutput

### Category
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Color
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]


# RadarChartAreaStyleSettings

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# RadarChartConfiguration

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RadarChartFieldWells]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RadarChartSortConfiguration]

### Shape
- **Type**: typing.Optional[typing.Literal['CIRCLE', 'POLYGON']]

### BaseSeriesSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RadarChartSeriesSettings]

### StartAngle
- **Type**: typing.Optional[float]

### VisualPalette
- **Type**: <class 'NoneType'>

### AlternateBandColorsVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### AlternateBandEvenColor
- **Type**: typing.Optional[str]

### AlternateBandOddColor
- **Type**: typing.Optional[str]

### CategoryAxis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDisplayOptions]

### CategoryLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptions]

### ColorAxis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDisplayOptions]

### ColorLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptions]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LegendOptions]

### AxesRangeScale
- **Type**: typing.Optional[typing.Literal['AUTO', 'INDEPENDENT', 'SHARED']]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# RadarChartConfigurationOutput

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RadarChartFieldWellsOutput]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RadarChartSortConfigurationOutput]

### Shape
- **Type**: typing.Optional[typing.Literal['CIRCLE', 'POLYGON']]

### BaseSeriesSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RadarChartSeriesSettings]

### StartAngle
- **Type**: typing.Optional[float]

### VisualPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualPaletteOutput]

### AlternateBandColorsVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### AlternateBandEvenColor
- **Type**: typing.Optional[str]

### AlternateBandOddColor
- **Type**: typing.Optional[str]

### CategoryAxis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDisplayOptionsOutput]

### CategoryLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptionsOutput]

### ColorAxis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDisplayOptionsOutput]

### ColorLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptionsOutput]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LegendOptions]

### AxesRangeScale
- **Type**: typing.Optional[typing.Literal['AUTO', 'INDEPENDENT', 'SHARED']]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# RadarChartFieldWells

### RadarChartAggregatedFieldWells
- **Type**: <class 'NoneType'>


# RadarChartFieldWellsOutput

### RadarChartAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RadarChartAggregatedFieldWellsOutput]


# RadarChartSeriesSettings

### AreaStyleSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RadarChartAreaStyleSettings]


# RadarChartSortConfiguration

### CategorySort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### CategoryItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]

### ColorSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### ColorItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]


# RadarChartSortConfigurationOutput

### CategorySort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### CategoryItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]

### ColorSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### ColorItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]


# RadarChartVisual

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RadarChartConfiguration]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomAction]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnHierarchy]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# RadarChartVisualOutput

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RadarChartConfigurationOutput]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomActionOutput]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnHierarchyOutput]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# RangeConstant

### Minimum
- **Type**: typing.Optional[str]

### Maximum
- **Type**: typing.Optional[str]


# RangeEndsLabelType

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# RdsParameters

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes


# RedshiftIAMParameters

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseUser
- **Type**: typing.Optional[str]

### DatabaseGroups
- **Type**: typing.Optional[typing.List[str]]

### AutoCreateDatabaseUser
- **Type**: typing.Optional[bool]


# RedshiftIAMParametersOutput

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseUser
- **Type**: typing.Optional[str]

### DatabaseGroups
- **Type**: typing.Optional[typing.List[str]]

### AutoCreateDatabaseUser
- **Type**: typing.Optional[bool]


# RedshiftParameters

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Host
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### ClusterId
- **Type**: typing.Optional[str]

### IAMParameters
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RedshiftIAMParameters, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RedshiftIAMParametersOutput, NoneType]

### IdentityCenterConfiguration
- **Type**: <class 'NoneType'>


# RedshiftParametersOutput

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Host
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### ClusterId
- **Type**: typing.Optional[str]

### IAMParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RedshiftIAMParametersOutput]

### IdentityCenterConfiguration
- **Type**: <class 'NoneType'>


# ReferenceLine

### DataConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ReferenceLineDataConfiguration'>
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### StyleConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ReferenceLineStyleConfiguration]

### LabelConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ReferenceLineLabelConfiguration]


# ReferenceLineCustomLabelConfiguration

### CustomLabel
- **Type**: <class 'str'>
- **Required**: Yes


# ReferenceLineDataConfiguration

### StaticConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ReferenceLineStaticDataConfiguration]

### DynamicConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ReferenceLineDynamicDataConfiguration]

### AxisBinding
- **Type**: typing.Optional[typing.Literal['PRIMARY_YAXIS', 'SECONDARY_YAXIS']]

### SeriesType
- **Type**: typing.Optional[typing.Literal['BAR', 'LINE']]


# ReferenceLineDynamicDataConfiguration

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### Calculation
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.NumericalAggregationFunction'>
- **Required**: Yes

### MeasureAggregationFunction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AggregationFunction]


# ReferenceLineLabelConfiguration

### ValueLabelConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ReferenceLineValueLabelConfiguration]

### CustomLabelConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ReferenceLineCustomLabelConfiguration]

### FontConfiguration
- **Type**: <class 'NoneType'>

### FontColor
- **Type**: typing.Optional[str]

### HorizontalPosition
- **Type**: typing.Optional[typing.Literal['CENTER', 'LEFT', 'RIGHT']]

### VerticalPosition
- **Type**: typing.Optional[typing.Literal['ABOVE', 'BELOW']]


# ReferenceLineStaticDataConfiguration

### Value
- **Type**: <class 'float'>
- **Required**: Yes


# ReferenceLineStyleConfiguration

### Pattern
- **Type**: typing.Optional[typing.Literal['DASHED', 'DOTTED', 'SOLID']]

### Color
- **Type**: typing.Optional[str]


# ReferenceLineValueLabelConfiguration

### RelativePosition
- **Type**: typing.Optional[typing.Literal['AFTER_CUSTOM_LABEL', 'BEFORE_CUSTOM_LABEL']]

### FormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.NumericFormatConfiguration]


# RefreshConfiguration

### IncrementalRefresh
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.IncrementalRefresh'>
- **Required**: Yes


# RefreshFrequency

### Interval
- **Type**: typing.Literal['DAILY', 'HOURLY', 'MINUTE15', 'MINUTE30', 'MONTHLY', 'WEEKLY']
- **Required**: Yes

### RefreshOnDay
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ScheduleRefreshOnEntity]

### Timezone
- **Type**: typing.Optional[str]

### TimeOfTheDay
- **Type**: typing.Optional[str]


# RefreshSchedule

### ScheduleId
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleFrequency
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RefreshFrequency'>
- **Required**: Yes

### RefreshType
- **Type**: typing.Literal['FULL_REFRESH', 'INCREMENTAL_REFRESH']
- **Required**: Yes

### StartAfterDateTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Arn
- **Type**: typing.Optional[str]


# RefreshScheduleOutput

### ScheduleId
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleFrequency
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RefreshFrequency'>
- **Required**: Yes

### RefreshType
- **Type**: typing.Literal['FULL_REFRESH', 'INCREMENTAL_REFRESH']
- **Required**: Yes

### StartAfterDateTime
- **Type**: typing.Optional[datetime.datetime]

### Arn
- **Type**: typing.Optional[str]


# RegisterUserRequest

### IdentityType
- **Type**: typing.Literal['IAM', 'IAM_IDENTITY_CENTER', 'QUICKSIGHT']
- **Required**: Yes

### Email
- **Type**: <class 'str'>
- **Required**: Yes

### UserRole
- **Type**: typing.Literal['ADMIN', 'ADMIN_PRO', 'AUTHOR', 'AUTHOR_PRO', 'READER', 'READER_PRO', 'RESTRICTED_AUTHOR', 'RESTRICTED_READER']
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### IamArn
- **Type**: typing.Optional[str]

### SessionName
- **Type**: typing.Optional[str]

### UserName
- **Type**: typing.Optional[str]

### CustomPermissionsName
- **Type**: typing.Optional[str]

### ExternalLoginFederationProviderType
- **Type**: typing.Optional[str]

### CustomFederationProviderUrl
- **Type**: typing.Optional[str]

### ExternalLoginId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Tag]]


# RegisterUserResponse

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.User'>
- **Required**: Yes

### UserInvitationUrl
- **Type**: <class 'str'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# RegisteredCustomerManagedKey

### KeyArn
- **Type**: typing.Optional[str]

### DefaultKey
- **Type**: typing.Optional[bool]


# RegisteredUserConsoleFeatureConfigurations

### StatePersistence
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.StatePersistenceConfigurations]

### SharedView
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SharedViewConfigurations]


# RegisteredUserDashboardEmbeddingConfiguration

### InitialDashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureConfigurations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RegisteredUserDashboardFeatureConfigurations]


# RegisteredUserDashboardFeatureConfigurations

### StatePersistence
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.StatePersistenceConfigurations]

### SharedView
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SharedViewConfigurations]

### Bookmarks
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BookmarksConfigurations]


# RegisteredUserDashboardVisualEmbeddingConfiguration

### InitialDashboardVisualId
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DashboardVisualId'>
- **Required**: Yes


# RegisteredUserEmbeddingExperienceConfiguration

### Dashboard
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RegisteredUserDashboardEmbeddingConfiguration]

### QuickSightConsole
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RegisteredUserQuickSightConsoleEmbeddingConfiguration]

### QSearchBar
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RegisteredUserQSearchBarEmbeddingConfiguration]

### DashboardVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RegisteredUserDashboardVisualEmbeddingConfiguration]

### GenerativeQnA
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RegisteredUserGenerativeQnAEmbeddingConfiguration]


# RegisteredUserGenerativeQnAEmbeddingConfiguration

### InitialTopicId
- **Type**: typing.Optional[str]


# RegisteredUserQSearchBarEmbeddingConfiguration

### InitialTopicId
- **Type**: typing.Optional[str]


# RegisteredUserQuickSightConsoleEmbeddingConfiguration

### InitialPath
- **Type**: typing.Optional[str]

### FeatureConfigurations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RegisteredUserConsoleFeatureConfigurations]


# RelationalTable

### DataSourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### InputColumns
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.InputColumn]
- **Required**: Yes

### Catalog
- **Type**: typing.Optional[str]

### Schema
- **Type**: typing.Optional[str]


# RelationalTableOutput

### DataSourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### InputColumns
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.InputColumn]
- **Required**: Yes

### Catalog
- **Type**: typing.Optional[str]

### Schema
- **Type**: typing.Optional[str]


# RelativeDateTimeControlDisplayOptions

### TitleOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LabelOptions]

### DateTimeFormat
- **Type**: typing.Optional[str]

### InfoIconLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SheetControlInfoIconLabelOptions]


# RelativeDatesFilter

### FilterId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### AnchorDateConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AnchorDateConfiguration'>
- **Required**: Yes

### TimeGranularity
- **Type**: typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']
- **Required**: Yes

### RelativeDateType
- **Type**: typing.Literal['LAST', 'NEXT', 'NOW', 'PREVIOUS', 'THIS']
- **Required**: Yes

### NullOption
- **Type**: typing.Literal['ALL_VALUES', 'NON_NULLS_ONLY', 'NULLS_ONLY']
- **Required**: Yes

### MinimumGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### RelativeDateValue
- **Type**: typing.Optional[int]

### ParameterName
- **Type**: typing.Optional[str]

### ExcludePeriodConfiguration
- **Type**: <class 'NoneType'>

### DefaultFilterControlConfiguration
- **Type**: <class 'NoneType'>


# RelativeDatesFilterOutput

### FilterId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### AnchorDateConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AnchorDateConfiguration'>
- **Required**: Yes

### TimeGranularity
- **Type**: typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']
- **Required**: Yes

### RelativeDateType
- **Type**: typing.Literal['LAST', 'NEXT', 'NOW', 'PREVIOUS', 'THIS']
- **Required**: Yes

### NullOption
- **Type**: typing.Literal['ALL_VALUES', 'NON_NULLS_ONLY', 'NULLS_ONLY']
- **Required**: Yes

### MinimumGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### RelativeDateValue
- **Type**: typing.Optional[int]

### ParameterName
- **Type**: typing.Optional[str]

### ExcludePeriodConfiguration
- **Type**: <class 'NoneType'>

### DefaultFilterControlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DefaultFilterControlConfigurationOutput]


# RenameColumnOperation

### ColumnName
- **Type**: <class 'str'>
- **Required**: Yes

### NewColumnName
- **Type**: <class 'str'>
- **Required**: Yes


# ResourcePermission

### Principal
- **Type**: <class 'str'>
- **Required**: Yes

### Actions
- **Type**: typing.List[str]
- **Required**: Yes


# ResourcePermissionOutput

### Principal
- **Type**: <class 'str'>
- **Required**: Yes

### Actions
- **Type**: typing.List[str]
- **Required**: Yes


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


# RestoreAnalysisRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AnalysisId
- **Type**: <class 'str'>
- **Required**: Yes

### RestoreToFolders
- **Type**: typing.Optional[bool]


# RestoreAnalysisResponse

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AnalysisId
- **Type**: <class 'str'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### RestorationFailedFolderArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# RollingDateConfiguration

### Expression
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetIdentifier
- **Type**: typing.Optional[str]


# RowAlternateColorOptions

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### RowAlternateColors
- **Type**: typing.Optional[typing.List[str]]

### UsePrimaryBackgroundColor
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# RowAlternateColorOptionsOutput

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### RowAlternateColors
- **Type**: typing.Optional[typing.List[str]]

### UsePrimaryBackgroundColor
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# RowInfo

### RowsIngested
- **Type**: typing.Optional[int]

### RowsDropped
- **Type**: typing.Optional[int]

### TotalRowsInDataset
- **Type**: typing.Optional[int]


# RowLevelPermissionDataSet

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionPolicy
- **Type**: typing.Literal['DENY_ACCESS', 'GRANT_ACCESS']
- **Required**: Yes

### Namespace
- **Type**: typing.Optional[str]

### FormatVersion
- **Type**: typing.Optional[typing.Literal['VERSION_1', 'VERSION_2']]

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# RowLevelPermissionTagConfiguration

### TagRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RowLevelPermissionTagRule]
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### TagRuleConfigurations
- **Type**: typing.Optional[typing.List[typing.List[str]]]


# RowLevelPermissionTagConfigurationOutput

### TagRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RowLevelPermissionTagRule]
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### TagRuleConfigurations
- **Type**: typing.Optional[typing.List[typing.List[str]]]


# RowLevelPermissionTagRule

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### ColumnName
- **Type**: <class 'str'>
- **Required**: Yes

### TagMultiValueDelimiter
- **Type**: typing.Optional[str]

### MatchAllValue
- **Type**: typing.Optional[str]


# S3BucketConfiguration

### BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### BucketPrefix
- **Type**: <class 'str'>
- **Required**: Yes

### BucketRegion
- **Type**: <class 'str'>
- **Required**: Yes


# S3Parameters

### ManifestFileLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ManifestFileLocation'>
- **Required**: Yes

### RoleArn
- **Type**: typing.Optional[str]


# S3Source

### DataSourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### InputColumns
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.InputColumn]
- **Required**: Yes

### UploadSettings
- **Type**: <class 'NoneType'>


# S3SourceOutput

### DataSourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### InputColumns
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.InputColumn]
- **Required**: Yes

### UploadSettings
- **Type**: <class 'NoneType'>


# SameSheetTargetVisualConfiguration

### TargetVisuals
- **Type**: typing.Optional[typing.List[str]]

### TargetVisualOptions
- **Type**: typing.Optional[typing.Literal['ALL_VISUALS']]


# SameSheetTargetVisualConfigurationOutput

### TargetVisuals
- **Type**: typing.Optional[typing.List[str]]

### TargetVisualOptions
- **Type**: typing.Optional[typing.Literal['ALL_VISUALS']]


# SankeyDiagramAggregatedFieldWells

### Source
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Destination
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Weight
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]


# SankeyDiagramAggregatedFieldWellsOutput

### Source
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Destination
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Weight
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]


# SankeyDiagramChartConfiguration

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SankeyDiagramFieldWells]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SankeyDiagramSortConfiguration]

### DataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataLabelOptions]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# SankeyDiagramChartConfigurationOutput

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SankeyDiagramFieldWellsOutput]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SankeyDiagramSortConfigurationOutput]

### DataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataLabelOptionsOutput]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# SankeyDiagramFieldWells

### SankeyDiagramAggregatedFieldWells
- **Type**: <class 'NoneType'>


# SankeyDiagramFieldWellsOutput

### SankeyDiagramAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SankeyDiagramAggregatedFieldWellsOutput]


# SankeyDiagramSortConfiguration

### WeightSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### SourceItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]

### DestinationItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]


# SankeyDiagramSortConfigurationOutput

### WeightSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### SourceItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]

### DestinationItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]


# SankeyDiagramVisual

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SankeyDiagramChartConfiguration]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomAction]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# SankeyDiagramVisualOutput

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SankeyDiagramChartConfigurationOutput]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomActionOutput]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# ScatterPlotCategoricallyAggregatedFieldWells

### XAxis
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]

### YAxis
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]

### Category
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Size
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]

### Label
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]


# ScatterPlotCategoricallyAggregatedFieldWellsOutput

### XAxis
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]

### YAxis
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]

### Category
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Size
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]

### Label
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]


# ScatterPlotConfiguration

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ScatterPlotFieldWells]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ScatterPlotSortConfiguration]

### XAxisLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptions]

### XAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDisplayOptions]

### YAxisLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptions]

### YAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDisplayOptions]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LegendOptions]

### DataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataLabelOptions]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TooltipOptions]

### VisualPalette
- **Type**: <class 'NoneType'>

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# ScatterPlotConfigurationOutput

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ScatterPlotFieldWellsOutput]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ScatterPlotSortConfiguration]

### XAxisLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptionsOutput]

### XAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDisplayOptionsOutput]

### YAxisLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptionsOutput]

### YAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDisplayOptionsOutput]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LegendOptions]

### DataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataLabelOptionsOutput]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TooltipOptionsOutput]

### VisualPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualPaletteOutput]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# ScatterPlotFieldWells

### ScatterPlotCategoricallyAggregatedFieldWells
- **Type**: <class 'NoneType'>

### ScatterPlotUnaggregatedFieldWells
- **Type**: <class 'NoneType'>


# ScatterPlotFieldWellsOutput

### ScatterPlotCategoricallyAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ScatterPlotCategoricallyAggregatedFieldWellsOutput]

### ScatterPlotUnaggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ScatterPlotUnaggregatedFieldWellsOutput]


# ScatterPlotSortConfiguration

### ScatterPlotLimitConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]


# ScatterPlotUnaggregatedFieldWells

### XAxis
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### YAxis
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Size
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]

### Category
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Label
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]


# ScatterPlotUnaggregatedFieldWellsOutput

### XAxis
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### YAxis
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Size
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]

### Category
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Label
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]


# ScatterPlotVisual

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ScatterPlotConfiguration]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomAction]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnHierarchy]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# ScatterPlotVisualOutput

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ScatterPlotConfigurationOutput]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomActionOutput]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnHierarchyOutput]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# ScheduleRefreshOnEntity

### DayOfWeek
- **Type**: typing.Optional[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY']]

### DayOfMonth
- **Type**: typing.Optional[str]


# ScrollBarOptions

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### VisibleRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisibleRangeOptions]


# SearchAnalysesRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AnalysisSearchFilter]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# SearchAnalysesRequestPaginate

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AnalysisSearchFilter]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PaginatorConfig]


# SearchAnalysesResponse

### AnalysisSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AnalysisSummary]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchDashboardsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DashboardSearchFilter]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# SearchDashboardsRequestPaginate

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DashboardSearchFilter]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PaginatorConfig]


# SearchDashboardsResponse

### DashboardSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DashboardSummary]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchDataSetsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataSetSearchFilter]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# SearchDataSetsRequestPaginate

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataSetSearchFilter]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PaginatorConfig]


# SearchDataSetsResponse

### DataSetSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataSetSummary]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchDataSourcesRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataSourceSearchFilter]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# SearchDataSourcesRequestPaginate

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataSourceSearchFilter]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PaginatorConfig]


# SearchDataSourcesResponse

### DataSourceSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataSourceSummary]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchFoldersRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FolderSearchFilter]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# SearchFoldersRequestPaginate

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FolderSearchFilter]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PaginatorConfig]


# SearchFoldersResponse

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### FolderSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FolderSummary]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchGroupsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GroupSearchFilter]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# SearchGroupsRequestPaginate

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GroupSearchFilter]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PaginatorConfig]


# SearchGroupsResponse

### GroupList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Group]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchTopicsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicSearchFilter]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# SearchTopicsRequestPaginate

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicSearchFilter]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PaginatorConfig]


# SearchTopicsResponse

### TopicSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicSummary]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SecondaryValueOptions

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# SectionAfterPageBreak

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# SectionBasedLayoutCanvasSizeOptions

### PaperCanvasSizeOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SectionBasedLayoutPaperCanvasSizeOptions]


# SectionBasedLayoutConfiguration

### HeaderSections
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.HeaderFooterSectionConfiguration]
- **Required**: Yes

### BodySections
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BodySectionConfiguration]
- **Required**: Yes

### FooterSections
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.HeaderFooterSectionConfiguration]
- **Required**: Yes

### CanvasSizeOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SectionBasedLayoutCanvasSizeOptions'>
- **Required**: Yes


# SectionBasedLayoutConfigurationOutput

### HeaderSections
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.HeaderFooterSectionConfigurationOutput]
- **Required**: Yes

### BodySections
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BodySectionConfigurationOutput]
- **Required**: Yes

### FooterSections
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.HeaderFooterSectionConfigurationOutput]
- **Required**: Yes

### CanvasSizeOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SectionBasedLayoutCanvasSizeOptions'>
- **Required**: Yes


# SectionBasedLayoutPaperCanvasSizeOptions

### PaperSize
- **Type**: typing.Optional[typing.Literal['A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'JIS_B4', 'JIS_B5', 'US_LEGAL', 'US_LETTER', 'US_TABLOID_LEDGER']]

### PaperOrientation
- **Type**: typing.Optional[typing.Literal['LANDSCAPE', 'PORTRAIT']]

### PaperMargin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Spacing]


# SectionLayoutConfiguration

### FreeFormLayout
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FreeFormSectionLayoutConfiguration'>
- **Required**: Yes


# SectionLayoutConfigurationOutput

### FreeFormLayout
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FreeFormSectionLayoutConfigurationOutput'>
- **Required**: Yes


# SectionPageBreakConfiguration

### After
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SectionAfterPageBreak]


# SectionStyle

### Height
- **Type**: typing.Optional[str]

### Padding
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Spacing]


# SelectedSheetsFilterScopeConfiguration

### SheetVisualScopingConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SheetVisualScopingConfiguration]]


# SelectedSheetsFilterScopeConfigurationOutput

### SheetVisualScopingConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SheetVisualScopingConfigurationOutput]]


# SemanticEntityType

### TypeName
- **Type**: typing.Optional[str]

### SubTypeName
- **Type**: typing.Optional[str]

### TypeParameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# SemanticEntityTypeOutput

### TypeName
- **Type**: typing.Optional[str]

### SubTypeName
- **Type**: typing.Optional[str]

### TypeParameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# SemanticType

### TypeName
- **Type**: typing.Optional[str]

### SubTypeName
- **Type**: typing.Optional[str]

### TypeParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### TruthyCellValue
- **Type**: typing.Optional[str]

### TruthyCellValueSynonyms
- **Type**: typing.Optional[typing.List[str]]

### FalseyCellValue
- **Type**: typing.Optional[str]

### FalseyCellValueSynonyms
- **Type**: typing.Optional[typing.List[str]]


# SemanticTypeOutput

### TypeName
- **Type**: typing.Optional[str]

### SubTypeName
- **Type**: typing.Optional[str]

### TypeParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### TruthyCellValue
- **Type**: typing.Optional[str]

### TruthyCellValueSynonyms
- **Type**: typing.Optional[typing.List[str]]

### FalseyCellValue
- **Type**: typing.Optional[str]

### FalseyCellValueSynonyms
- **Type**: typing.Optional[typing.List[str]]


# SeriesItem

### FieldSeriesItem
- **Type**: <class 'NoneType'>

### DataFieldSeriesItem
- **Type**: <class 'NoneType'>


# ServiceNowParameters

### SiteBaseUrl
- **Type**: <class 'str'>
- **Required**: Yes


# SessionTag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# SetParameterValueConfiguration

### DestinationParameterName
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DestinationParameterValueConfiguration'>
- **Required**: Yes


# SetParameterValueConfigurationOutput

### DestinationParameterName
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DestinationParameterValueConfigurationOutput'>
- **Required**: Yes


# ShapeConditionalFormat

### BackgroundColor
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingColor'>
- **Required**: Yes


# ShapeConditionalFormatOutput

### BackgroundColor
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingColorOutput'>
- **Required**: Yes


# SharedViewConfigurations

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# Sheet

### SheetId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Images
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SheetImageOutput]]


# SheetControlInfoIconLabelOptions

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### InfoIconText
- **Type**: typing.Optional[str]


# SheetControlLayout

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SheetControlLayoutConfiguration'>
- **Required**: Yes


# SheetControlLayoutConfiguration

### GridLayout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GridLayoutConfiguration]


# SheetControlLayoutConfigurationOutput

### GridLayout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GridLayoutConfigurationOutput]


# SheetControlLayoutOutput

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SheetControlLayoutConfigurationOutput'>
- **Required**: Yes


# SheetControlsOption

### VisibilityState
- **Type**: typing.Optional[typing.Literal['COLLAPSED', 'EXPANDED']]


# SheetDefinition

### SheetId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ParameterControls
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ParameterControl]]

### FilterControls
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterControl]]

### Visuals
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Visual]]

### TextBoxes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SheetTextBox]]

### Images
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SheetImage]]

### Layouts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Layout]]

### SheetControlLayouts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SheetControlLayout]]

### ContentType
- **Type**: typing.Optional[typing.Literal['INTERACTIVE', 'PAGINATED']]


# SheetDefinitionOutput

### SheetId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ParameterControls
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ParameterControlOutput]]

### FilterControls
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterControlOutput]]

### Visuals
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualOutput]]

### TextBoxes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SheetTextBox]]

### Images
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SheetImageOutput]]

### Layouts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LayoutOutput]]

### SheetControlLayouts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SheetControlLayoutOutput]]

### ContentType
- **Type**: typing.Optional[typing.Literal['INTERACTIVE', 'PAGINATED']]


# SheetElementConfigurationOverrides

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# SheetElementRenderingRule

### Expression
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationOverrides
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SheetElementConfigurationOverrides'>
- **Required**: Yes


# SheetImage

### SheetImageId
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SheetImageSource'>
- **Required**: Yes

### Scaling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SheetImageScalingConfiguration]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SheetImageTooltipConfiguration]

### ImageContentAltText
- **Type**: typing.Optional[str]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ImageInteractionOptions]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ImageCustomAction]]


# SheetImageOutput

### SheetImageId
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SheetImageSource'>
- **Required**: Yes

### Scaling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SheetImageScalingConfiguration]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SheetImageTooltipConfiguration]

### ImageContentAltText
- **Type**: typing.Optional[str]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ImageInteractionOptions]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ImageCustomActionOutput]]


# SheetImageScalingConfiguration

### ScalingType
- **Type**: typing.Optional[typing.Literal['SCALE_NONE', 'SCALE_TO_CONTAINER', 'SCALE_TO_HEIGHT', 'SCALE_TO_WIDTH']]


# SheetImageSource

### SheetImageStaticFileSource
- **Type**: <class 'NoneType'>


# SheetImageStaticFileSource

### StaticFileId
- **Type**: <class 'str'>
- **Required**: Yes


# SheetImageTooltipConfiguration

### TooltipText
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SheetImageTooltipText]

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# SheetImageTooltipText

### PlainText
- **Type**: typing.Optional[str]


# SheetLayoutElementMaximizationOption

### AvailabilityStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# SheetStyle

### Tile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TileStyle]

### TileLayout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TileLayoutStyle]


# SheetTextBox

### SheetTextBoxId
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: typing.Optional[str]


# SheetVisualScopingConfiguration

### SheetId
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Literal['ALL_VISUALS', 'SELECTED_VISUALS']
- **Required**: Yes

### VisualIds
- **Type**: typing.Optional[typing.List[str]]


# SheetVisualScopingConfigurationOutput

### SheetId
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Literal['ALL_VISUALS', 'SELECTED_VISUALS']
- **Required**: Yes

### VisualIds
- **Type**: typing.Optional[typing.List[str]]


# ShortFormatText

### PlainText
- **Type**: typing.Optional[str]

### RichText
- **Type**: typing.Optional[str]


# SignupResponse

### IAMUser
- **Type**: typing.Optional[bool]

### userLoginName
- **Type**: typing.Optional[str]

### accountName
- **Type**: typing.Optional[str]

### directoryType
- **Type**: typing.Optional[str]


# SimpleClusterMarker

### Color
- **Type**: typing.Optional[str]


# SingleAxisOptions

### YAxisOptions
- **Type**: <class 'NoneType'>


# SliderControlDisplayOptions

### TitleOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LabelOptions]

### InfoIconLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SheetControlInfoIconLabelOptions]


# Slot

### SlotId
- **Type**: typing.Optional[str]

### VisualId
- **Type**: typing.Optional[str]


# SmallMultiplesAxisProperties

### Scale
- **Type**: typing.Optional[typing.Literal['INDEPENDENT', 'SHARED']]

### Placement
- **Type**: typing.Optional[typing.Literal['INSIDE', 'OUTSIDE']]


# SmallMultiplesOptions

### MaxVisibleRows
- **Type**: typing.Optional[int]

### MaxVisibleColumns
- **Type**: typing.Optional[int]

### PanelConfiguration
- **Type**: <class 'NoneType'>

### XAxis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SmallMultiplesAxisProperties]

### YAxis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SmallMultiplesAxisProperties]


# SnapshotAnonymousUser

### RowLevelPermissionTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SessionTag]]


# SnapshotAnonymousUserRedacted

### RowLevelPermissionTagKeys
- **Type**: typing.Optional[typing.List[str]]


# SnapshotConfiguration

### FileGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SnapshotFileGroup]
- **Required**: Yes

### DestinationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SnapshotDestinationConfiguration]

### Parameters
- **Type**: <class 'NoneType'>


# SnapshotConfigurationOutput

### FileGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SnapshotFileGroupOutput]
- **Required**: Yes

### DestinationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SnapshotDestinationConfigurationOutput]

### Parameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ParametersOutput]


# SnapshotDestinationConfiguration

### S3Destinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SnapshotS3DestinationConfiguration]]


# SnapshotDestinationConfigurationOutput

### S3Destinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SnapshotS3DestinationConfiguration]]


# SnapshotFile

### SheetSelections
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SnapshotFileSheetSelection]
- **Required**: Yes

### FormatType
- **Type**: typing.Literal['CSV', 'EXCEL', 'PDF']
- **Required**: Yes


# SnapshotFileGroup

### Files
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SnapshotFile]]


# SnapshotFileGroupOutput

### Files
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SnapshotFileOutput]]


# SnapshotFileOutput

### SheetSelections
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SnapshotFileSheetSelectionOutput]
- **Required**: Yes

### FormatType
- **Type**: typing.Literal['CSV', 'EXCEL', 'PDF']
- **Required**: Yes


# SnapshotFileSheetSelection

### SheetId
- **Type**: <class 'str'>
- **Required**: Yes

### SelectionScope
- **Type**: typing.Literal['ALL_VISUALS', 'SELECTED_VISUALS']
- **Required**: Yes

### VisualIds
- **Type**: typing.Optional[typing.List[str]]


# SnapshotFileSheetSelectionOutput

### SheetId
- **Type**: <class 'str'>
- **Required**: Yes

### SelectionScope
- **Type**: typing.Literal['ALL_VISUALS', 'SELECTED_VISUALS']
- **Required**: Yes

### VisualIds
- **Type**: typing.Optional[typing.List[str]]


# SnapshotJobErrorInfo

### ErrorMessage
- **Type**: typing.Optional[str]

### ErrorType
- **Type**: typing.Optional[str]


# SnapshotJobResult

### AnonymousUsers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AnonymousUserSnapshotJobResult]]


# SnapshotJobResultErrorInfo

### ErrorMessage
- **Type**: typing.Optional[str]

### ErrorType
- **Type**: typing.Optional[str]


# SnapshotJobResultFileGroup

### Files
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SnapshotFileOutput]]

### S3Results
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SnapshotJobS3Result]]


# SnapshotJobS3Result

### S3DestinationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SnapshotS3DestinationConfiguration]

### S3Uri
- **Type**: typing.Optional[str]

### ErrorInfo
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SnapshotJobResultErrorInfo]]


# SnapshotS3DestinationConfiguration

### BucketConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.S3BucketConfiguration'>
- **Required**: Yes


# SnapshotUserConfiguration

### AnonymousUsers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SnapshotAnonymousUser]]


# SnapshotUserConfigurationRedacted

### AnonymousUsers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SnapshotAnonymousUserRedacted]]


# SnowflakeParameters

### Host
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Warehouse
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationType
- **Type**: typing.Optional[typing.Literal['PASSWORD', 'TOKEN', 'X509']]

### DatabaseAccessControlRole
- **Type**: typing.Optional[str]

### OAuthParameters
- **Type**: <class 'NoneType'>


# Spacing

### Top
- **Type**: typing.Optional[str]

### Bottom
- **Type**: typing.Optional[str]

### Left
- **Type**: typing.Optional[str]

### Right
- **Type**: typing.Optional[str]


# SparkParameters

### Host
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes


# SpatialStaticFile

### StaticFileId
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.StaticFileSource]


# SqlServerParameters

### Host
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes


# SslProperties

### DisableSsl
- **Type**: typing.Optional[bool]


# StarburstParameters

### Host
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### ProductType
- **Type**: typing.Optional[typing.Literal['ENTERPRISE', 'GALAXY']]

### DatabaseAccessControlRole
- **Type**: typing.Optional[str]

### AuthenticationType
- **Type**: typing.Optional[typing.Literal['PASSWORD', 'TOKEN', 'X509']]

### OAuthParameters
- **Type**: <class 'NoneType'>


# StartAssetBundleExportJobRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AssetBundleExportJobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArns
- **Type**: typing.List[str]
- **Required**: Yes

### ExportFormat
- **Type**: typing.Literal['CLOUDFORMATION_JSON', 'QUICKSIGHT_JSON']
- **Required**: Yes

### IncludeAllDependencies
- **Type**: typing.Optional[bool]

### CloudFormationOverridePropertyConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleCloudFormationOverridePropertyConfiguration, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleCloudFormationOverridePropertyConfigurationOutput, NoneType]

### IncludePermissions
- **Type**: typing.Optional[bool]

### IncludeTags
- **Type**: typing.Optional[bool]

### ValidationStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleExportJobValidationStrategy]

### IncludeFolderMemberships
- **Type**: typing.Optional[bool]

### IncludeFolderMembers
- **Type**: typing.Optional[typing.Literal['NONE', 'ONE_LEVEL', 'RECURSE']]


# StartAssetBundleExportJobResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AssetBundleExportJobId
- **Type**: <class 'str'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# StartAssetBundleImportJobRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AssetBundleImportJobId
- **Type**: <class 'str'>
- **Required**: Yes

### AssetBundleImportSource
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportSource'>
- **Required**: Yes

### OverrideParameters
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobOverrideParameters, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobOverrideParametersOutput, NoneType]

### FailureAction
- **Type**: typing.Optional[typing.Literal['DO_NOTHING', 'ROLLBACK']]

### OverridePermissions
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobOverridePermissions, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobOverridePermissionsOutput, NoneType]

### OverrideTags
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobOverrideTags, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobOverrideTagsOutput, NoneType]

### OverrideValidationStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetBundleImportJobOverrideValidationStrategy]


# StartAssetBundleImportJobResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AssetBundleImportJobId
- **Type**: <class 'str'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# StartDashboardSnapshotJobRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotJobId
- **Type**: <class 'str'>
- **Required**: Yes

### UserConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SnapshotUserConfiguration'>
- **Required**: Yes

### SnapshotConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SnapshotConfiguration, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SnapshotConfigurationOutput]
- **Required**: Yes


# StartDashboardSnapshotJobResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotJobId
- **Type**: <class 'str'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# StartDashboardSnapshotJobScheduleRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleId
- **Type**: <class 'str'>
- **Required**: Yes


# StartDashboardSnapshotJobScheduleResponse

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# StatePersistenceConfigurations

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# StaticFile

### ImageStaticFile
- **Type**: <class 'NoneType'>

### SpatialStaticFile
- **Type**: <class 'NoneType'>


# StaticFileS3SourceOptions

### BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectKey
- **Type**: <class 'str'>
- **Required**: Yes

### Region
- **Type**: <class 'str'>
- **Required**: Yes


# StaticFileSource

### UrlOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.StaticFileUrlSourceOptions]

### S3Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.StaticFileS3SourceOptions]


# StaticFileUrlSourceOptions

### Url
- **Type**: <class 'str'>
- **Required**: Yes


# StringDatasetParameter

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ValueType
- **Type**: typing.Literal['MULTI_VALUED', 'SINGLE_VALUED']
- **Required**: Yes

### DefaultValues
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.StringDatasetParameterDefaultValues, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.StringDatasetParameterDefaultValuesOutput, NoneType]


# StringDatasetParameterDefaultValues

### StaticValues
- **Type**: typing.Optional[typing.List[str]]


# StringDatasetParameterDefaultValuesOutput

### StaticValues
- **Type**: typing.Optional[typing.List[str]]


# StringDatasetParameterOutput

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ValueType
- **Type**: typing.Literal['MULTI_VALUED', 'SINGLE_VALUED']
- **Required**: Yes

### DefaultValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.StringDatasetParameterDefaultValuesOutput]


# StringDefaultValues

### DynamicValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DynamicDefaultValue]

### StaticValues
- **Type**: typing.Optional[typing.List[str]]


# StringDefaultValuesOutput

### DynamicValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DynamicDefaultValue]

### StaticValues
- **Type**: typing.Optional[typing.List[str]]


# StringFormatConfiguration

### NullValueFormatConfiguration
- **Type**: <class 'NoneType'>

### NumericFormatConfiguration
- **Type**: <class 'NoneType'>


# StringParameter

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# StringParameterDeclaration

### ParameterValueType
- **Type**: typing.Literal['MULTI_VALUED', 'SINGLE_VALUED']
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.StringDefaultValues]

### ValueWhenUnset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.StringValueWhenUnsetConfiguration]

### MappedDataSetParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MappedDataSetParameter]]


# StringParameterDeclarationOutput

### ParameterValueType
- **Type**: typing.Literal['MULTI_VALUED', 'SINGLE_VALUED']
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.StringDefaultValuesOutput]

### ValueWhenUnset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.StringValueWhenUnsetConfiguration]

### MappedDataSetParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MappedDataSetParameter]]


# StringParameterOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# StringValueWhenUnsetConfiguration

### ValueWhenUnsetOption
- **Type**: typing.Optional[typing.Literal['NULL', 'RECOMMENDED_VALUE']]

### CustomValue
- **Type**: typing.Optional[str]


# SubtotalOptions

### TotalsVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### CustomLabel
- **Type**: typing.Optional[str]

### FieldLevel
- **Type**: typing.Optional[typing.Literal['ALL', 'CUSTOM', 'LAST']]

### FieldLevelOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTableFieldSubtotalOptions]]

### TotalCellStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableCellStyle]

### ValueCellStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableCellStyle]

### MetricHeaderCellStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableCellStyle]

### StyleTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableStyleTarget]]


# SubtotalOptionsOutput

### TotalsVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### CustomLabel
- **Type**: typing.Optional[str]

### FieldLevel
- **Type**: typing.Optional[typing.Literal['ALL', 'CUSTOM', 'LAST']]

### FieldLevelOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTableFieldSubtotalOptions]]

### TotalCellStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableCellStyle]

### ValueCellStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableCellStyle]

### MetricHeaderCellStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableCellStyle]

### StyleTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableStyleTarget]]


# SucceededTopicReviewedAnswer

### AnswerId
- **Type**: typing.Optional[str]


# SuccessfulKeyRegistrationEntry

### KeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### StatusCode
- **Type**: <class 'int'>
- **Required**: Yes


# TableAggregatedFieldWells

### GroupBy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]


# TableAggregatedFieldWellsOutput

### GroupBy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]


# TableBorderOptions

### Color
- **Type**: typing.Optional[str]

### Thickness
- **Type**: typing.Optional[int]

### Style
- **Type**: typing.Optional[typing.Literal['NONE', 'SOLID']]


# TableCellConditionalFormatting

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### TextFormat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TextConditionalFormat]


# TableCellConditionalFormattingOutput

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### TextFormat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TextConditionalFormatOutput]


# TableCellImageSizingConfiguration

### TableCellImageScalingConfiguration
- **Type**: typing.Optional[typing.Literal['DO_NOT_SCALE', 'FIT_TO_CELL_HEIGHT', 'FIT_TO_CELL_WIDTH']]


# TableCellStyle

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### FontConfiguration
- **Type**: <class 'NoneType'>

### TextWrap
- **Type**: typing.Optional[typing.Literal['NONE', 'WRAP']]

### HorizontalTextAlignment
- **Type**: typing.Optional[typing.Literal['AUTO', 'CENTER', 'LEFT', 'RIGHT']]

### VerticalTextAlignment
- **Type**: typing.Optional[typing.Literal['AUTO', 'BOTTOM', 'MIDDLE', 'TOP']]

### BackgroundColor
- **Type**: typing.Optional[str]

### Height
- **Type**: typing.Optional[int]

### Border
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GlobalTableBorderOptions]


# TableConditionalFormatting

### ConditionalFormattingOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableConditionalFormattingOption]]


# TableConditionalFormattingOption

### Cell
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableCellConditionalFormatting]

### Row
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableRowConditionalFormatting]


# TableConditionalFormattingOptionOutput

### Cell
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableCellConditionalFormattingOutput]

### Row
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableRowConditionalFormattingOutput]


# TableConditionalFormattingOutput

### ConditionalFormattingOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableConditionalFormattingOptionOutput]]


# TableConfiguration

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableFieldWells]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableSortConfiguration]

### TableOptions
- **Type**: <class 'NoneType'>

### TotalOptions
- **Type**: <class 'NoneType'>

### FieldOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableFieldOptions]

### PaginatedReportOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TablePaginatedReportOptions]

### TableInlineVisualizations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableInlineVisualization]]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# TableConfigurationOutput

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableFieldWellsOutput]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableSortConfigurationOutput]

### TableOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableOptionsOutput]

### TotalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TotalOptionsOutput]

### FieldOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableFieldOptionsOutput]

### PaginatedReportOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TablePaginatedReportOptions]

### TableInlineVisualizations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableInlineVisualization]]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# TableFieldCustomIconContent

### Icon
- **Type**: typing.Optional[typing.Literal['LINK']]


# TableFieldCustomTextContent

### FontConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FontConfiguration'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# TableFieldImageConfiguration

### SizingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableCellImageSizingConfiguration]


# TableFieldLinkConfiguration

### Target
- **Type**: typing.Literal['NEW_TAB', 'NEW_WINDOW', 'SAME_TAB']
- **Required**: Yes

### Content
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableFieldLinkContentConfiguration'>
- **Required**: Yes


# TableFieldLinkContentConfiguration

### CustomTextContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableFieldCustomTextContent]

### CustomIconContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableFieldCustomIconContent]


# TableFieldOption

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### Width
- **Type**: typing.Optional[str]

### CustomLabel
- **Type**: typing.Optional[str]

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### URLStyling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableFieldURLConfiguration]


# TableFieldOptions

### SelectedFieldOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableFieldOption]]

### Order
- **Type**: typing.Optional[typing.List[str]]

### PinnedFieldOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TablePinnedFieldOptions]


# TableFieldOptionsOutput

### SelectedFieldOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableFieldOption]]

### Order
- **Type**: typing.Optional[typing.List[str]]

### PinnedFieldOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TablePinnedFieldOptionsOutput]


# TableFieldURLConfiguration

### LinkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableFieldLinkConfiguration]

### ImageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableFieldImageConfiguration]


# TableFieldWells

### TableAggregatedFieldWells
- **Type**: <class 'NoneType'>

### TableUnaggregatedFieldWells
- **Type**: <class 'NoneType'>


# TableFieldWellsOutput

### TableAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableAggregatedFieldWellsOutput]

### TableUnaggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableUnaggregatedFieldWellsOutput]


# TableInlineVisualization

### DataBars
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataBarsOptions]


# TableOptions

### Orientation
- **Type**: typing.Optional[typing.Literal['HORIZONTAL', 'VERTICAL']]

### HeaderStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableCellStyle]

### CellStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableCellStyle]

### RowAlternateColorOptions
- **Type**: <class 'NoneType'>


# TableOptionsOutput

### Orientation
- **Type**: typing.Optional[typing.Literal['HORIZONTAL', 'VERTICAL']]

### HeaderStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableCellStyle]

### CellStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableCellStyle]

### RowAlternateColorOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RowAlternateColorOptionsOutput]


# TablePaginatedReportOptions

### VerticalOverflowVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### OverflowColumnHeaderVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# TablePinnedFieldOptions

### PinnedLeftFields
- **Type**: typing.Optional[typing.List[str]]


# TablePinnedFieldOptionsOutput

### PinnedLeftFields
- **Type**: typing.Optional[typing.List[str]]


# TableRowConditionalFormatting

### BackgroundColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingColor]

### TextColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingColor]


# TableRowConditionalFormattingOutput

### BackgroundColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingColorOutput]

### TextColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingColorOutput]


# TableSideBorderOptions

### InnerVertical
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableBorderOptions]

### InnerHorizontal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableBorderOptions]

### Left
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableBorderOptions]

### Right
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableBorderOptions]

### Top
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableBorderOptions]

### Bottom
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableBorderOptions]


# TableSortConfiguration

### RowSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### PaginationConfiguration
- **Type**: <class 'NoneType'>


# TableSortConfigurationOutput

### RowSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### PaginationConfiguration
- **Type**: <class 'NoneType'>


# TableStyleTarget

### CellType
- **Type**: typing.Literal['METRIC_HEADER', 'TOTAL', 'VALUE']
- **Required**: Yes


# TableUnaggregatedFieldWells

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.UnaggregatedField]]


# TableUnaggregatedFieldWellsOutput

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.UnaggregatedField]]


# TableVisual

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableConfiguration]

### ConditionalFormatting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableConditionalFormatting]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomAction]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# TableVisualOutput

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableConfigurationOutput]

### ConditionalFormatting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableConditionalFormattingOutput]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomActionOutput]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagColumnOperation

### ColumnName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnTag]
- **Required**: Yes


# TagColumnOperationOutput

### ColumnName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnTag]
- **Required**: Yes


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Tag]
- **Required**: Yes


# TagResourceResponse

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# Template

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TemplateVersion]

### TemplateId
- **Type**: typing.Optional[str]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]


# TemplateAlias

### AliasName
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### TemplateVersionNumber
- **Type**: typing.Optional[int]


# TemplateError

### Type
- **Type**: typing.Optional[typing.Literal['ACCESS_DENIED', 'DATA_SET_NOT_FOUND', 'INTERNAL_FAILURE', 'SOURCE_NOT_FOUND']]

### Message
- **Type**: typing.Optional[str]

### ViolatedEntities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Entity]]


# TemplateSourceAnalysis

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetReferences
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataSetReference]
- **Required**: Yes


# TemplateSourceEntity

### SourceAnalysis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TemplateSourceAnalysis]

### SourceTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TemplateSourceTemplate]


# TemplateSourceTemplate

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# TemplateSummary

### Arn
- **Type**: typing.Optional[str]

### TemplateId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### LatestVersionNumber
- **Type**: typing.Optional[int]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]


# TemplateVersion

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### Errors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TemplateError]]

### VersionNumber
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['CREATION_FAILED', 'CREATION_IN_PROGRESS', 'CREATION_SUCCESSFUL', 'DELETED', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']]

### DataSetConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataSetConfigurationOutput]]

### Description
- **Type**: typing.Optional[str]

### SourceEntityArn
- **Type**: typing.Optional[str]

### ThemeArn
- **Type**: typing.Optional[str]

### Sheets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Sheet]]


# TemplateVersionDefinition

### DataSetConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataSetConfiguration]
- **Required**: Yes

### Sheets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SheetDefinition]]

### CalculatedFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CalculatedField]]

### ParameterDeclarations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ParameterDeclaration]]

### FilterGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterGroup]]

### ColumnConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnConfiguration]]

### AnalysisDefaults
- **Type**: <class 'NoneType'>

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetOptions]

### QueryExecutionOptions
- **Type**: <class 'NoneType'>

### StaticFiles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.StaticFile]]


# TemplateVersionDefinitionOutput

### DataSetConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataSetConfigurationOutput]
- **Required**: Yes

### Sheets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SheetDefinitionOutput]]

### CalculatedFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CalculatedField]]

### ParameterDeclarations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ParameterDeclarationOutput]]

### FilterGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterGroupOutput]]

### ColumnConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnConfigurationOutput]]

### AnalysisDefaults
- **Type**: <class 'NoneType'>

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AssetOptions]

### QueryExecutionOptions
- **Type**: <class 'NoneType'>

### StaticFiles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.StaticFile]]


# TemplateVersionSummary

### Arn
- **Type**: typing.Optional[str]

### VersionNumber
- **Type**: typing.Optional[int]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['CREATION_FAILED', 'CREATION_IN_PROGRESS', 'CREATION_SUCCESSFUL', 'DELETED', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']]

### Description
- **Type**: typing.Optional[str]


# TeradataParameters

### Host
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes


# TextAreaControlDisplayOptions

### TitleOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LabelOptions]

### PlaceholderOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TextControlPlaceholderOptions]

### InfoIconLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SheetControlInfoIconLabelOptions]


# TextConditionalFormat

### BackgroundColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingColor]

### TextColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingColor]

### Icon
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingIcon]


# TextConditionalFormatOutput

### BackgroundColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingColorOutput]

### TextColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingColorOutput]

### Icon
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ConditionalFormattingIcon]


# TextControlPlaceholderOptions

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# TextFieldControlDisplayOptions

### TitleOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LabelOptions]

### PlaceholderOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TextControlPlaceholderOptions]

### InfoIconLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SheetControlInfoIconLabelOptions]


# Theme

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ThemeId
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ThemeVersion]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### Type
- **Type**: typing.Optional[typing.Literal['ALL', 'CUSTOM', 'QUICKSIGHT']]


# ThemeAlias

### Arn
- **Type**: typing.Optional[str]

### AliasName
- **Type**: typing.Optional[str]

### ThemeVersionNumber
- **Type**: typing.Optional[int]


# ThemeConfiguration

### DataColorPalette
- **Type**: <class 'NoneType'>

### UIColorPalette
- **Type**: <class 'NoneType'>

### Sheet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SheetStyle]

### Typography
- **Type**: <class 'NoneType'>


# ThemeConfigurationOutput

### DataColorPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataColorPaletteOutput]

### UIColorPalette
- **Type**: <class 'NoneType'>

### Sheet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SheetStyle]

### Typography
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TypographyOutput]


# ThemeError

### Type
- **Type**: typing.Optional[typing.Literal['INTERNAL_FAILURE']]

### Message
- **Type**: typing.Optional[str]


# ThemeSummary

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ThemeId
- **Type**: typing.Optional[str]

### LatestVersionNumber
- **Type**: typing.Optional[int]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]


# ThemeVersion

### VersionNumber
- **Type**: typing.Optional[int]

### Arn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### BaseThemeId
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ThemeConfigurationOutput]

### Errors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ThemeError]]

### Status
- **Type**: typing.Optional[typing.Literal['CREATION_FAILED', 'CREATION_IN_PROGRESS', 'CREATION_SUCCESSFUL', 'DELETED', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']]


# ThemeVersionSummary

### VersionNumber
- **Type**: typing.Optional[int]

### Arn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['CREATION_FAILED', 'CREATION_IN_PROGRESS', 'CREATION_SUCCESSFUL', 'DELETED', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']]


# ThousandSeparatorOptions

### Symbol
- **Type**: typing.Optional[typing.Literal['COMMA', 'DOT', 'SPACE']]

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### GroupingStyle
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'LAKHS']]


# TileLayoutStyle

### Gutter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GutterStyle]

### Margin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MarginStyle]


# TileStyle

### Border
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BorderStyle]


# TimeBasedForecastProperties

### PeriodsForward
- **Type**: typing.Optional[int]

### PeriodsBackward
- **Type**: typing.Optional[int]

### UpperBoundary
- **Type**: typing.Optional[float]

### LowerBoundary
- **Type**: typing.Optional[float]

### PredictionInterval
- **Type**: typing.Optional[int]

### Seasonality
- **Type**: typing.Optional[int]


# TimeEqualityFilter

### FilterId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### Value
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ParameterName
- **Type**: typing.Optional[str]

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### RollingDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RollingDateConfiguration]

### DefaultFilterControlConfiguration
- **Type**: <class 'NoneType'>


# TimeEqualityFilterOutput

### FilterId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[datetime.datetime]

### ParameterName
- **Type**: typing.Optional[str]

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### RollingDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RollingDateConfiguration]

### DefaultFilterControlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DefaultFilterControlConfigurationOutput]


# TimeRangeDrillDownFilter

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### RangeMinimum
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### RangeMaximum
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### TimeGranularity
- **Type**: typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']
- **Required**: Yes


# TimeRangeDrillDownFilterOutput

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### RangeMinimum
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RangeMaximum
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TimeGranularity
- **Type**: typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']
- **Required**: Yes


# TimeRangeFilter

### FilterId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### NullOption
- **Type**: typing.Literal['ALL_VALUES', 'NON_NULLS_ONLY', 'NULLS_ONLY']
- **Required**: Yes

### IncludeMinimum
- **Type**: typing.Optional[bool]

### IncludeMaximum
- **Type**: typing.Optional[bool]

### RangeMinimumValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TimeRangeFilterValue]

### RangeMaximumValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TimeRangeFilterValue]

### ExcludePeriodConfiguration
- **Type**: <class 'NoneType'>

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### DefaultFilterControlConfiguration
- **Type**: <class 'NoneType'>


# TimeRangeFilterOutput

### FilterId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### NullOption
- **Type**: typing.Literal['ALL_VALUES', 'NON_NULLS_ONLY', 'NULLS_ONLY']
- **Required**: Yes

### IncludeMinimum
- **Type**: typing.Optional[bool]

### IncludeMaximum
- **Type**: typing.Optional[bool]

### RangeMinimumValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TimeRangeFilterValueOutput]

### RangeMaximumValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TimeRangeFilterValueOutput]

### ExcludePeriodConfiguration
- **Type**: <class 'NoneType'>

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### DefaultFilterControlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DefaultFilterControlConfigurationOutput]


# TimeRangeFilterValue

### StaticValue
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### RollingDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RollingDateConfiguration]

### Parameter
- **Type**: typing.Optional[str]


# TimeRangeFilterValueOutput

### StaticValue
- **Type**: typing.Optional[datetime.datetime]

### RollingDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RollingDateConfiguration]

### Parameter
- **Type**: typing.Optional[str]


# TooltipItem

### FieldTooltipItem
- **Type**: <class 'NoneType'>

### ColumnTooltipItem
- **Type**: <class 'NoneType'>


# TooltipOptions

### TooltipVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### SelectedTooltipType
- **Type**: typing.Optional[typing.Literal['BASIC', 'DETAILED']]

### FieldBasedTooltip
- **Type**: <class 'NoneType'>


# TooltipOptionsOutput

### TooltipVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### SelectedTooltipType
- **Type**: typing.Optional[typing.Literal['BASIC', 'DETAILED']]

### FieldBasedTooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldBasedTooltipOutput]


# TopBottomFilter

### FilterId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### AggregationSortConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AggregationSortConfiguration]
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### ParameterName
- **Type**: typing.Optional[str]

### DefaultFilterControlConfiguration
- **Type**: <class 'NoneType'>


# TopBottomFilterOutput

### FilterId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### AggregationSortConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AggregationSortConfiguration]
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### ParameterName
- **Type**: typing.Optional[str]

### DefaultFilterControlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DefaultFilterControlConfigurationOutput]


# TopBottomMoversComputation

### ComputationId
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['BOTTOM', 'TOP']
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Time
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]

### Category
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]

### Value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]

### MoverSize
- **Type**: typing.Optional[int]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ABSOLUTE_DIFFERENCE', 'PERCENT_DIFFERENCE']]


# TopBottomRankedComputation

### ComputationId
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['BOTTOM', 'TOP']
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Category
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]

### Value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]

### ResultSize
- **Type**: typing.Optional[int]


# TopicCalculatedField

### CalculatedFieldName
- **Type**: <class 'str'>
- **Required**: Yes

### Expression
- **Type**: <class 'str'>
- **Required**: Yes

### CalculatedFieldDescription
- **Type**: typing.Optional[str]

### CalculatedFieldSynonyms
- **Type**: typing.Optional[typing.List[str]]

### IsIncludedInTopic
- **Type**: typing.Optional[bool]

### DisableIndexing
- **Type**: typing.Optional[bool]

### ColumnDataRole
- **Type**: typing.Optional[typing.Literal['DIMENSION', 'MEASURE']]

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### DefaultFormatting
- **Type**: <class 'NoneType'>

### Aggregation
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'COUNT', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]

### ComparativeOrder
- **Type**: <class 'NoneType'>

### SemanticType
- **Type**: <class 'NoneType'>

### AllowedAggregations
- **Type**: typing.Optional[typing.List[typing.Literal['AVERAGE', 'COUNT', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'PERCENTILE', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]]

### NotAllowedAggregations
- **Type**: typing.Optional[typing.List[typing.Literal['AVERAGE', 'COUNT', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'PERCENTILE', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]]

### NeverAggregateInFilter
- **Type**: typing.Optional[bool]

### CellValueSynonyms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CellValueSynonym]]

### NonAdditive
- **Type**: typing.Optional[bool]


# TopicCalculatedFieldOutput

### CalculatedFieldName
- **Type**: <class 'str'>
- **Required**: Yes

### Expression
- **Type**: <class 'str'>
- **Required**: Yes

### CalculatedFieldDescription
- **Type**: typing.Optional[str]

### CalculatedFieldSynonyms
- **Type**: typing.Optional[typing.List[str]]

### IsIncludedInTopic
- **Type**: typing.Optional[bool]

### DisableIndexing
- **Type**: typing.Optional[bool]

### ColumnDataRole
- **Type**: typing.Optional[typing.Literal['DIMENSION', 'MEASURE']]

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### DefaultFormatting
- **Type**: <class 'NoneType'>

### Aggregation
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'COUNT', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]

### ComparativeOrder
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ComparativeOrderOutput]

### SemanticType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SemanticTypeOutput]

### AllowedAggregations
- **Type**: typing.Optional[typing.List[typing.Literal['AVERAGE', 'COUNT', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'PERCENTILE', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]]

### NotAllowedAggregations
- **Type**: typing.Optional[typing.List[typing.Literal['AVERAGE', 'COUNT', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'PERCENTILE', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]]

### NeverAggregateInFilter
- **Type**: typing.Optional[bool]

### CellValueSynonyms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CellValueSynonymOutput]]

### NonAdditive
- **Type**: typing.Optional[bool]


# TopicCategoryFilter

### CategoryFilterFunction
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EXACT']]

### CategoryFilterType
- **Type**: typing.Optional[typing.Literal['CUSTOM_FILTER', 'CUSTOM_FILTER_LIST', 'FILTER_LIST']]

### Constant
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicCategoryFilterConstant]

### Inverse
- **Type**: typing.Optional[bool]


# TopicCategoryFilterConstant

### ConstantType
- **Type**: typing.Optional[typing.Literal['COLLECTIVE', 'RANGE', 'SINGULAR']]

### SingularConstant
- **Type**: typing.Optional[str]

### CollectiveConstant
- **Type**: <class 'NoneType'>


# TopicCategoryFilterConstantOutput

### ConstantType
- **Type**: typing.Optional[typing.Literal['COLLECTIVE', 'RANGE', 'SINGULAR']]

### SingularConstant
- **Type**: typing.Optional[str]

### CollectiveConstant
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CollectiveConstantOutput]


# TopicCategoryFilterOutput

### CategoryFilterFunction
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EXACT']]

### CategoryFilterType
- **Type**: typing.Optional[typing.Literal['CUSTOM_FILTER', 'CUSTOM_FILTER_LIST', 'FILTER_LIST']]

### Constant
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicCategoryFilterConstantOutput]

### Inverse
- **Type**: typing.Optional[bool]


# TopicColumn

### ColumnName
- **Type**: <class 'str'>
- **Required**: Yes

### ColumnFriendlyName
- **Type**: typing.Optional[str]

### ColumnDescription
- **Type**: typing.Optional[str]

### ColumnSynonyms
- **Type**: typing.Optional[typing.List[str]]

### ColumnDataRole
- **Type**: typing.Optional[typing.Literal['DIMENSION', 'MEASURE']]

### Aggregation
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'COUNT', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]

### IsIncludedInTopic
- **Type**: typing.Optional[bool]

### DisableIndexing
- **Type**: typing.Optional[bool]

### ComparativeOrder
- **Type**: <class 'NoneType'>

### SemanticType
- **Type**: <class 'NoneType'>

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### AllowedAggregations
- **Type**: typing.Optional[typing.List[typing.Literal['AVERAGE', 'COUNT', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'PERCENTILE', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]]

### NotAllowedAggregations
- **Type**: typing.Optional[typing.List[typing.Literal['AVERAGE', 'COUNT', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'PERCENTILE', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]]

### DefaultFormatting
- **Type**: <class 'NoneType'>

### NeverAggregateInFilter
- **Type**: typing.Optional[bool]

### CellValueSynonyms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CellValueSynonym]]

### NonAdditive
- **Type**: typing.Optional[bool]


# TopicColumnOutput

### ColumnName
- **Type**: <class 'str'>
- **Required**: Yes

### ColumnFriendlyName
- **Type**: typing.Optional[str]

### ColumnDescription
- **Type**: typing.Optional[str]

### ColumnSynonyms
- **Type**: typing.Optional[typing.List[str]]

### ColumnDataRole
- **Type**: typing.Optional[typing.Literal['DIMENSION', 'MEASURE']]

### Aggregation
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'COUNT', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]

### IsIncludedInTopic
- **Type**: typing.Optional[bool]

### DisableIndexing
- **Type**: typing.Optional[bool]

### ComparativeOrder
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ComparativeOrderOutput]

### SemanticType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SemanticTypeOutput]

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### AllowedAggregations
- **Type**: typing.Optional[typing.List[typing.Literal['AVERAGE', 'COUNT', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'PERCENTILE', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]]

### NotAllowedAggregations
- **Type**: typing.Optional[typing.List[typing.Literal['AVERAGE', 'COUNT', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'PERCENTILE', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]]

### DefaultFormatting
- **Type**: <class 'NoneType'>

### NeverAggregateInFilter
- **Type**: typing.Optional[bool]

### CellValueSynonyms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CellValueSynonymOutput]]

### NonAdditive
- **Type**: typing.Optional[bool]


# TopicConfigOptions

### QBusinessInsightsEnabled
- **Type**: typing.Optional[bool]


# TopicConstantValue

### ConstantType
- **Type**: typing.Optional[typing.Literal['COLLECTIVE', 'RANGE', 'SINGULAR']]

### Value
- **Type**: typing.Optional[str]

### Minimum
- **Type**: typing.Optional[str]

### Maximum
- **Type**: typing.Optional[str]

### ValueList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CollectiveConstantEntry]]


# TopicConstantValueOutput

### ConstantType
- **Type**: typing.Optional[typing.Literal['COLLECTIVE', 'RANGE', 'SINGULAR']]

### Value
- **Type**: typing.Optional[str]

### Minimum
- **Type**: typing.Optional[str]

### Maximum
- **Type**: typing.Optional[str]

### ValueList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CollectiveConstantEntry]]


# TopicDateRangeFilter

### Inclusive
- **Type**: typing.Optional[bool]

### Constant
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicRangeFilterConstant]


# TopicDetails

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### UserExperienceVersion
- **Type**: typing.Optional[typing.Literal['LEGACY', 'NEW_READER_EXPERIENCE']]

### DataSets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DatasetMetadata]]

### ConfigOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicConfigOptions]


# TopicDetailsOutput

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### UserExperienceVersion
- **Type**: typing.Optional[typing.Literal['LEGACY', 'NEW_READER_EXPERIENCE']]

### DataSets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DatasetMetadataOutput]]

### ConfigOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicConfigOptions]


# TopicFilter

### FilterName
- **Type**: <class 'str'>
- **Required**: Yes

### OperandFieldName
- **Type**: <class 'str'>
- **Required**: Yes

### FilterDescription
- **Type**: typing.Optional[str]

### FilterClass
- **Type**: typing.Optional[typing.Literal['CONDITIONAL_VALUE_FILTER', 'ENFORCED_VALUE_FILTER', 'NAMED_VALUE_FILTER']]

### FilterSynonyms
- **Type**: typing.Optional[typing.List[str]]

### FilterType
- **Type**: typing.Optional[typing.Literal['CATEGORY_FILTER', 'DATE_RANGE_FILTER', 'NUMERIC_EQUALITY_FILTER', 'NUMERIC_RANGE_FILTER', 'RELATIVE_DATE_FILTER']]

### CategoryFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicCategoryFilter]

### NumericEqualityFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicNumericEqualityFilter]

### NumericRangeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicNumericRangeFilter]

### DateRangeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicDateRangeFilter]

### RelativeDateFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicRelativeDateFilter]


# TopicFilterOutput

### FilterName
- **Type**: <class 'str'>
- **Required**: Yes

### OperandFieldName
- **Type**: <class 'str'>
- **Required**: Yes

### FilterDescription
- **Type**: typing.Optional[str]

### FilterClass
- **Type**: typing.Optional[typing.Literal['CONDITIONAL_VALUE_FILTER', 'ENFORCED_VALUE_FILTER', 'NAMED_VALUE_FILTER']]

### FilterSynonyms
- **Type**: typing.Optional[typing.List[str]]

### FilterType
- **Type**: typing.Optional[typing.Literal['CATEGORY_FILTER', 'DATE_RANGE_FILTER', 'NUMERIC_EQUALITY_FILTER', 'NUMERIC_RANGE_FILTER', 'RELATIVE_DATE_FILTER']]

### CategoryFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicCategoryFilterOutput]

### NumericEqualityFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicNumericEqualityFilter]

### NumericRangeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicNumericRangeFilter]

### DateRangeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicDateRangeFilter]

### RelativeDateFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicRelativeDateFilter]


# TopicIR

### Metrics
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicIRMetric, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicIRMetricOutput]]]

### GroupByList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicIRGroupBy]]

### Filters
- **Type**: typing.Optional[typing.List[typing.List[typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicIRFilterOption, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicIRFilterOptionOutput]]]]

### Sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicSortClause]

### ContributionAnalysis
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicIRContributionAnalysis, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicIRContributionAnalysisOutput, NoneType]

### Visual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualOptions]


# TopicIRComparisonMethod

### Type
- **Type**: typing.Optional[typing.Literal['DIFF', 'DIFF_AS_PERC', 'MOVING_AVERAGE', 'PERCENT_OF_TOTAL', 'PERC_DIFF', 'POP_CURRENT_DIFF', 'POP_CURRENT_DIFF_AS_PERC', 'POP_OVERTIME_DIFF', 'POP_OVERTIME_DIFF_AS_PERC', 'RUNNING_SUM']]

### Period
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### WindowSize
- **Type**: typing.Optional[int]


# TopicIRContributionAnalysis

### Factors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ContributionAnalysisFactor]]

### TimeRanges
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ContributionAnalysisTimeRanges, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ContributionAnalysisTimeRangesOutput, NoneType]

### Direction
- **Type**: typing.Optional[typing.Literal['DECREASE', 'INCREASE', 'NEUTRAL']]

### SortType
- **Type**: typing.Optional[typing.Literal['ABSOLUTE_DIFFERENCE', 'CONTRIBUTION_PERCENTAGE', 'DEVIATION_FROM_EXPECTED', 'PERCENTAGE_DIFFERENCE']]


# TopicIRContributionAnalysisOutput

### Factors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ContributionAnalysisFactor]]

### TimeRanges
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ContributionAnalysisTimeRangesOutput]

### Direction
- **Type**: typing.Optional[typing.Literal['DECREASE', 'INCREASE', 'NEUTRAL']]

### SortType
- **Type**: typing.Optional[typing.Literal['ABSOLUTE_DIFFERENCE', 'CONTRIBUTION_PERCENTAGE', 'DEVIATION_FROM_EXPECTED', 'PERCENTAGE_DIFFERENCE']]


# TopicIRFilterOption

### FilterType
- **Type**: typing.Optional[typing.Literal['ACCEPT_ALL_FILTER', 'CATEGORY_FILTER', 'DATE_RANGE_FILTER', 'EQUALS', 'NUMERIC_EQUALITY_FILTER', 'NUMERIC_RANGE_FILTER', 'RANK_LIMIT_FILTER', 'RELATIVE_DATE_FILTER', 'TOP_BOTTOM_FILTER']]

### FilterClass
- **Type**: typing.Optional[typing.Literal['CONDITIONAL_VALUE_FILTER', 'ENFORCED_VALUE_FILTER', 'NAMED_VALUE_FILTER']]

### OperandField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Identifier]

### Function
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'CONTAINS_STRING', 'ENDS_WITH', 'EXACT', 'LAST', 'NEXT', 'NOW', 'PREVIOUS', 'STARTS_WITH', 'THIS']]

### Constant
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicConstantValue, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicConstantValueOutput, NoneType]

### Inverse
- **Type**: typing.Optional[bool]

### NullFilter
- **Type**: typing.Optional[typing.Literal['ALL_VALUES', 'NON_NULLS_ONLY', 'NULLS_ONLY']]

### Aggregation
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'COLUMN', 'COUNT', 'CUSTOM', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'PERCENTILE', 'PTD_AVERAGE', 'PTD_COUNT', 'PTD_DISTINCT_COUNT', 'PTD_MAX', 'PTD_MIN', 'PTD_SUM', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]

### AggregationFunctionParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### AggregationPartitionBy
- **Type**: typing.Optional[typing.List[NoneType]]

### Range
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicConstantValue, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicConstantValueOutput, NoneType]

### Inclusive
- **Type**: typing.Optional[bool]

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### LastNextOffset
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicConstantValue, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicConstantValueOutput, NoneType]

### AggMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterAggMetrics]]

### TopBottomLimit
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicConstantValue, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicConstantValueOutput, NoneType]

### SortDirection
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### Anchor
- **Type**: <class 'NoneType'>


# TopicIRFilterOptionOutput

### FilterType
- **Type**: typing.Optional[typing.Literal['ACCEPT_ALL_FILTER', 'CATEGORY_FILTER', 'DATE_RANGE_FILTER', 'EQUALS', 'NUMERIC_EQUALITY_FILTER', 'NUMERIC_RANGE_FILTER', 'RANK_LIMIT_FILTER', 'RELATIVE_DATE_FILTER', 'TOP_BOTTOM_FILTER']]

### FilterClass
- **Type**: typing.Optional[typing.Literal['CONDITIONAL_VALUE_FILTER', 'ENFORCED_VALUE_FILTER', 'NAMED_VALUE_FILTER']]

### OperandField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Identifier]

### Function
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'CONTAINS_STRING', 'ENDS_WITH', 'EXACT', 'LAST', 'NEXT', 'NOW', 'PREVIOUS', 'STARTS_WITH', 'THIS']]

### Constant
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicConstantValueOutput]

### Inverse
- **Type**: typing.Optional[bool]

### NullFilter
- **Type**: typing.Optional[typing.Literal['ALL_VALUES', 'NON_NULLS_ONLY', 'NULLS_ONLY']]

### Aggregation
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'COLUMN', 'COUNT', 'CUSTOM', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'PERCENTILE', 'PTD_AVERAGE', 'PTD_COUNT', 'PTD_DISTINCT_COUNT', 'PTD_MAX', 'PTD_MIN', 'PTD_SUM', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]

### AggregationFunctionParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### AggregationPartitionBy
- **Type**: typing.Optional[typing.List[NoneType]]

### Range
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicConstantValueOutput]

### Inclusive
- **Type**: typing.Optional[bool]

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### LastNextOffset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicConstantValueOutput]

### AggMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilterAggMetrics]]

### TopBottomLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicConstantValueOutput]

### SortDirection
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### Anchor
- **Type**: <class 'NoneType'>


# TopicIRGroupBy

### FieldName
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Identifier]

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### Sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicSortClause]

### DisplayFormat
- **Type**: typing.Optional[typing.Literal['AUTO', 'CURRENCY', 'DATE', 'NUMBER', 'PERCENT', 'STRING']]

### DisplayFormatOptions
- **Type**: <class 'NoneType'>

### NamedEntity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.NamedEntityRef]


# TopicIRMetric

### MetricId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Identifier]

### Function
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AggFunction, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AggFunctionOutput, NoneType]

### Operands
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Identifier]]

### ComparisonMethod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicIRComparisonMethod]

### Expression
- **Type**: typing.Optional[str]

### CalculatedFieldReferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Identifier]]

### DisplayFormat
- **Type**: typing.Optional[typing.Literal['AUTO', 'CURRENCY', 'DATE', 'NUMBER', 'PERCENT', 'STRING']]

### DisplayFormatOptions
- **Type**: <class 'NoneType'>

### NamedEntity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.NamedEntityRef]


# TopicIRMetricOutput

### MetricId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Identifier]

### Function
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AggFunctionOutput]

### Operands
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Identifier]]

### ComparisonMethod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicIRComparisonMethod]

### Expression
- **Type**: typing.Optional[str]

### CalculatedFieldReferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Identifier]]

### DisplayFormat
- **Type**: typing.Optional[typing.Literal['AUTO', 'CURRENCY', 'DATE', 'NUMBER', 'PERCENT', 'STRING']]

### DisplayFormatOptions
- **Type**: <class 'NoneType'>

### NamedEntity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.NamedEntityRef]


# TopicIROutput

### Metrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicIRMetricOutput]]

### GroupByList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicIRGroupBy]]

### Filters
- **Type**: typing.Optional[typing.List[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicIRFilterOptionOutput]]]

### Sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicSortClause]

### ContributionAnalysis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicIRContributionAnalysisOutput]

### Visual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualOptions]


# TopicNamedEntity

### EntityName
- **Type**: <class 'str'>
- **Required**: Yes

### EntityDescription
- **Type**: typing.Optional[str]

### EntitySynonyms
- **Type**: typing.Optional[typing.List[str]]

### SemanticEntityType
- **Type**: <class 'NoneType'>

### Definition
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.NamedEntityDefinition]]


# TopicNamedEntityOutput

### EntityName
- **Type**: <class 'str'>
- **Required**: Yes

### EntityDescription
- **Type**: typing.Optional[str]

### EntitySynonyms
- **Type**: typing.Optional[typing.List[str]]

### SemanticEntityType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SemanticEntityTypeOutput]

### Definition
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.NamedEntityDefinitionOutput]]


# TopicNumericEqualityFilter

### Constant
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicSingularFilterConstant]

### Aggregation
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'COUNT', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'NO_AGGREGATION', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]


# TopicNumericRangeFilter

### Inclusive
- **Type**: typing.Optional[bool]

### Constant
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicRangeFilterConstant]

### Aggregation
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'COUNT', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'NO_AGGREGATION', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]


# TopicRangeFilterConstant

### ConstantType
- **Type**: typing.Optional[typing.Literal['COLLECTIVE', 'RANGE', 'SINGULAR']]

### RangeConstant
- **Type**: <class 'NoneType'>


# TopicRefreshDetails

### RefreshArn
- **Type**: typing.Optional[str]

### RefreshId
- **Type**: typing.Optional[str]

### RefreshStatus
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'FAILED', 'INITIALIZED', 'RUNNING']]


# TopicRefreshSchedule

### IsEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### BasedOnSpiceSchedule
- **Type**: <class 'bool'>
- **Required**: Yes

### StartingAt
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Timezone
- **Type**: typing.Optional[str]

### RepeatAt
- **Type**: typing.Optional[str]

### TopicScheduleType
- **Type**: typing.Optional[typing.Literal['DAILY', 'HOURLY', 'MONTHLY', 'WEEKLY']]


# TopicRefreshScheduleOutput

### IsEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### BasedOnSpiceSchedule
- **Type**: <class 'bool'>
- **Required**: Yes

### StartingAt
- **Type**: typing.Optional[datetime.datetime]

### Timezone
- **Type**: typing.Optional[str]

### RepeatAt
- **Type**: typing.Optional[str]

### TopicScheduleType
- **Type**: typing.Optional[typing.Literal['DAILY', 'HOURLY', 'MONTHLY', 'WEEKLY']]


# TopicRefreshScheduleSummary

### DatasetId
- **Type**: typing.Optional[str]

### DatasetArn
- **Type**: typing.Optional[str]

### DatasetName
- **Type**: typing.Optional[str]

### RefreshSchedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicRefreshScheduleOutput]


# TopicRelativeDateFilter

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### RelativeDateFilterFunction
- **Type**: typing.Optional[typing.Literal['LAST', 'NEXT', 'NOW', 'PREVIOUS', 'THIS']]

### Constant
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicSingularFilterConstant]


# TopicReviewedAnswer

### AnswerId
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### Question
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: typing.Optional[str]

### Mir
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicIROutput]

### PrimaryVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicVisualOutput]

### Template
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicTemplateOutput]


# TopicSearchFilter

### Operator
- **Type**: typing.Literal['StringEquals', 'StringLike']
- **Required**: Yes

### Name
- **Type**: typing.Literal['DIRECT_QUICKSIGHT_OWNER', 'DIRECT_QUICKSIGHT_SOLE_OWNER', 'DIRECT_QUICKSIGHT_VIEWER_OR_OWNER', 'QUICKSIGHT_OWNER', 'QUICKSIGHT_USER', 'QUICKSIGHT_VIEWER_OR_OWNER', 'TOPIC_NAME']
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TopicSingularFilterConstant

### ConstantType
- **Type**: typing.Optional[typing.Literal['COLLECTIVE', 'RANGE', 'SINGULAR']]

### SingularConstant
- **Type**: typing.Optional[str]


# TopicSortClause

### Operand
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Identifier]

### SortDirection
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# TopicSummary

### Arn
- **Type**: typing.Optional[str]

### TopicId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### UserExperienceVersion
- **Type**: typing.Optional[typing.Literal['LEGACY', 'NEW_READER_EXPERIENCE']]


# TopicTemplate

### TemplateType
- **Type**: typing.Optional[str]

### Slots
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Slot]]


# TopicTemplateOutput

### TemplateType
- **Type**: typing.Optional[str]

### Slots
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Slot]]


# TopicVisual

### VisualId
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[typing.Literal['COMPLIMENTARY', 'FALLBACK', 'FRAGMENT', 'MULTI_INTENT', 'PRIMARY']]

### Ir
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicIR, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicIROutput, NoneType]

### SupportingVisuals
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# TopicVisualOutput

### VisualId
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[typing.Literal['COMPLIMENTARY', 'FALLBACK', 'FRAGMENT', 'MULTI_INTENT', 'PRIMARY']]

### Ir
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicIROutput]

### SupportingVisuals
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# TotalAggregationComputation

### ComputationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]


# TotalAggregationFunction

### SimpleTotalAggregationFunction
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'DEFAULT', 'MAX', 'MIN', 'NONE', 'SUM']]


# TotalAggregationOption

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### TotalAggregationFunction
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TotalAggregationFunction'>
- **Required**: Yes


# TotalOptions

### TotalsVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### Placement
- **Type**: typing.Optional[typing.Literal['AUTO', 'END', 'START']]

### ScrollStatus
- **Type**: typing.Optional[typing.Literal['PINNED', 'SCROLLED']]

### CustomLabel
- **Type**: typing.Optional[str]

### TotalCellStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableCellStyle]

### TotalAggregationOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TotalAggregationOption]]


# TotalOptionsOutput

### TotalsVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### Placement
- **Type**: typing.Optional[typing.Literal['AUTO', 'END', 'START']]

### ScrollStatus
- **Type**: typing.Optional[typing.Literal['PINNED', 'SCROLLED']]

### CustomLabel
- **Type**: typing.Optional[str]

### TotalCellStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableCellStyle]

### TotalAggregationOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TotalAggregationOption]]


# TransformOperation

### ProjectOperation
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ProjectOperation, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ProjectOperationOutput, NoneType]

### FilterOperation
- **Type**: <class 'NoneType'>

### CreateColumnsOperation
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CreateColumnsOperation, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CreateColumnsOperationOutput, NoneType]

### RenameColumnOperation
- **Type**: <class 'NoneType'>

### CastColumnTypeOperation
- **Type**: <class 'NoneType'>

### TagColumnOperation
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TagColumnOperation, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TagColumnOperationOutput, NoneType]

### UntagColumnOperation
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.UntagColumnOperation, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.UntagColumnOperationOutput, NoneType]

### OverrideDatasetParameterOperation
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.OverrideDatasetParameterOperation, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.OverrideDatasetParameterOperationOutput, NoneType]


# TransformOperationOutput

### ProjectOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ProjectOperationOutput]

### FilterOperation
- **Type**: <class 'NoneType'>

### CreateColumnsOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CreateColumnsOperationOutput]

### RenameColumnOperation
- **Type**: <class 'NoneType'>

### CastColumnTypeOperation
- **Type**: <class 'NoneType'>

### TagColumnOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TagColumnOperationOutput]

### UntagColumnOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.UntagColumnOperationOutput]

### OverrideDatasetParameterOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.OverrideDatasetParameterOperationOutput]


# TreeMapAggregatedFieldWells

### Groups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Sizes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]

### Colors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]


# TreeMapAggregatedFieldWellsOutput

### Groups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Sizes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]

### Colors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]


# TreeMapConfiguration

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TreeMapFieldWells]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TreeMapSortConfiguration]

### GroupLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptions]

### SizeLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptions]

### ColorLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptions]

### ColorScale
- **Type**: <class 'NoneType'>

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LegendOptions]

### DataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataLabelOptions]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TooltipOptions]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# TreeMapConfigurationOutput

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TreeMapFieldWellsOutput]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TreeMapSortConfigurationOutput]

### GroupLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptionsOutput]

### SizeLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptionsOutput]

### ColorLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptionsOutput]

### ColorScale
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColorScaleOutput]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LegendOptions]

### DataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataLabelOptionsOutput]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TooltipOptionsOutput]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# TreeMapFieldWells

### TreeMapAggregatedFieldWells
- **Type**: <class 'NoneType'>


# TreeMapFieldWellsOutput

### TreeMapAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TreeMapAggregatedFieldWellsOutput]


# TreeMapSortConfiguration

### TreeMapSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### TreeMapGroupItemsLimitConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]


# TreeMapSortConfigurationOutput

### TreeMapSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### TreeMapGroupItemsLimitConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]


# TreeMapVisual

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TreeMapConfiguration]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomAction]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnHierarchy]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# TreeMapVisualOutput

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TreeMapConfigurationOutput]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomActionOutput]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnHierarchyOutput]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# TrendArrowOptions

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# TrinoParameters

### Host
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes


# TwitterParameters

### Query
- **Type**: <class 'str'>
- **Required**: Yes

### MaxRows
- **Type**: <class 'int'>
- **Required**: Yes


# Typography

### FontFamilies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Font]]


# TypographyOutput

### FontFamilies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Font]]


# UIColorPalette

### PrimaryForeground
- **Type**: typing.Optional[str]

### PrimaryBackground
- **Type**: typing.Optional[str]

### SecondaryForeground
- **Type**: typing.Optional[str]

### SecondaryBackground
- **Type**: typing.Optional[str]

### Accent
- **Type**: typing.Optional[str]

### AccentForeground
- **Type**: typing.Optional[str]

### Danger
- **Type**: typing.Optional[str]

### DangerForeground
- **Type**: typing.Optional[str]

### Warning
- **Type**: typing.Optional[str]

### WarningForeground
- **Type**: typing.Optional[str]

### Success
- **Type**: typing.Optional[str]

### SuccessForeground
- **Type**: typing.Optional[str]

### Dimension
- **Type**: typing.Optional[str]

### DimensionForeground
- **Type**: typing.Optional[str]

### Measure
- **Type**: typing.Optional[str]

### MeasureForeground
- **Type**: typing.Optional[str]


# UnaggregatedField

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnIdentifier'>
- **Required**: Yes

### FormatConfiguration
- **Type**: <class 'NoneType'>


# UniqueKey

### ColumnNames
- **Type**: typing.List[str]
- **Required**: Yes


# UniqueKeyOutput

### ColumnNames
- **Type**: typing.List[str]
- **Required**: Yes


# UniqueValuesComputation

### ComputationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Category
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]


# UntagColumnOperation

### ColumnName
- **Type**: <class 'str'>
- **Required**: Yes

### TagNames
- **Type**: typing.List[typing.Literal['COLUMN_DESCRIPTION', 'COLUMN_GEOGRAPHIC_ROLE']]
- **Required**: Yes


# UntagColumnOperationOutput

### ColumnName
- **Type**: <class 'str'>
- **Required**: Yes

### TagNames
- **Type**: typing.List[typing.Literal['COLUMN_DESCRIPTION', 'COLUMN_GEOGRAPHIC_ROLE']]
- **Required**: Yes


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UntagResourceResponse

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAccountCustomizationRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountCustomization
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AccountCustomization'>
- **Required**: Yes

### Namespace
- **Type**: typing.Optional[str]


# UpdateAccountCustomizationResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### AccountCustomization
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AccountCustomization'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAccountSettingsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultNamespace
- **Type**: <class 'str'>
- **Required**: Yes

### NotificationEmail
- **Type**: typing.Optional[str]

### TerminationProtectionEnabled
- **Type**: typing.Optional[bool]


# UpdateAccountSettingsResponse

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAnalysisPermissionsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AnalysisId
- **Type**: <class 'str'>
- **Required**: Yes

### GrantPermissions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermission, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]]]

### RevokePermissions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermission, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]]]


# UpdateAnalysisPermissionsResponse

### AnalysisArn
- **Type**: <class 'str'>
- **Required**: Yes

### AnalysisId
- **Type**: <class 'str'>
- **Required**: Yes

### Permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAnalysisRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AnalysisId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Parameters, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ParametersOutput, NoneType]

### SourceEntity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AnalysisSourceEntity]

### ThemeArn
- **Type**: typing.Optional[str]

### Definition
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AnalysisDefinition, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AnalysisDefinitionOutput, NoneType]

### ValidationStrategy
- **Type**: <class 'NoneType'>


# UpdateAnalysisResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AnalysisId
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateStatus
- **Type**: typing.Literal['CREATION_FAILED', 'CREATION_IN_PROGRESS', 'CREATION_SUCCESSFUL', 'DELETED', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateApplicationWithTokenExchangeGrantRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateApplicationWithTokenExchangeGrantResponse

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateBrandAssignmentRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BrandArn
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateBrandAssignmentResponse

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### BrandArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateBrandPublishedVersionRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BrandId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateBrandPublishedVersionResponse

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateBrandRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BrandId
- **Type**: <class 'str'>
- **Required**: Yes

### BrandDefinition
- **Type**: <class 'NoneType'>


# UpdateBrandResponse

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### BrandDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BrandDetail'>
- **Required**: Yes

### BrandDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BrandDefinition'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateCustomPermissionsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### CustomPermissionsName
- **Type**: <class 'str'>
- **Required**: Yes

### Capabilities
- **Type**: <class 'NoneType'>


# UpdateCustomPermissionsResponse

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDashboardLinksRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### LinkEntities
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateDashboardLinksResponse

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### DashboardArn
- **Type**: <class 'str'>
- **Required**: Yes

### LinkEntities
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDashboardPermissionsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### GrantPermissions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermission, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]]]

### RevokePermissions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermission, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]]]

### GrantLinkPermissions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermission, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]]]

### RevokeLinkPermissions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermission, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]]]


# UpdateDashboardPermissionsResponse

### DashboardArn
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### Permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### LinkSharingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LinkSharingConfigurationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDashboardPublishedVersionRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: <class 'int'>
- **Required**: Yes


# UpdateDashboardPublishedVersionResponse

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDashboardRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SourceEntity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DashboardSourceEntity]

### Parameters
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Parameters, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ParametersOutput, NoneType]

### VersionDescription
- **Type**: typing.Optional[str]

### DashboardPublishOptions
- **Type**: <class 'NoneType'>

### ThemeArn
- **Type**: typing.Optional[str]

### Definition
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DashboardVersionDefinition, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DashboardVersionDefinitionOutput, NoneType]

### ValidationStrategy
- **Type**: <class 'NoneType'>


# UpdateDashboardResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### VersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### CreationStatus
- **Type**: typing.Literal['CREATION_FAILED', 'CREATION_IN_PROGRESS', 'CREATION_SUCCESSFUL', 'DELETED', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDashboardsQAConfigurationRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardsQAStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# UpdateDashboardsQAConfigurationResponse

### DashboardsQAStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDataSetPermissionsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### GrantPermissions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermission, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]]]

### RevokePermissions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermission, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]]]


# UpdateDataSetPermissionsResponse

### DataSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDataSetRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PhysicalTableMap
- **Type**: typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PhysicalTable, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PhysicalTableOutput]]
- **Required**: Yes

### ImportMode
- **Type**: typing.Literal['DIRECT_QUERY', 'SPICE']
- **Required**: Yes

### LogicalTableMap
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LogicalTable, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LogicalTableOutput]]]

### ColumnGroups
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnGroup, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnGroupOutput]]]

### FieldFolders
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldFolder, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldFolderOutput]]]

### RowLevelPermissionDataSet
- **Type**: <class 'NoneType'>

### RowLevelPermissionTagConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RowLevelPermissionTagConfiguration, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RowLevelPermissionTagConfigurationOutput, NoneType]

### ColumnLevelPermissionRules
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnLevelPermissionRule, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnLevelPermissionRuleOutput]]]

### DataSetUsageConfiguration
- **Type**: <class 'NoneType'>

### DatasetParameters
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DatasetParameter, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DatasetParameterOutput]]]

### PerformanceConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PerformanceConfiguration, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PerformanceConfigurationOutput, NoneType]


# UpdateDataSetResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### IngestionArn
- **Type**: <class 'str'>
- **Required**: Yes

### IngestionId
- **Type**: <class 'str'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDataSourcePermissionsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### GrantPermissions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermission, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]]]

### RevokePermissions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermission, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]]]


# UpdateDataSourcePermissionsResponse

### DataSourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDataSourceRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceParameters
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataSourceParameters, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataSourceParametersOutput, NoneType]

### Credentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataSourceCredentials]

### VpcConnectionProperties
- **Type**: <class 'NoneType'>

### SslProperties
- **Type**: <class 'NoneType'>


# UpdateDataSourceResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateStatus
- **Type**: typing.Literal['CREATION_FAILED', 'CREATION_IN_PROGRESS', 'CREATION_SUCCESSFUL', 'DELETED', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDefaultQBusinessApplicationRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: typing.Optional[str]


# UpdateDefaultQBusinessApplicationResponse

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFolderPermissionsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes

### GrantPermissions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermission, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]]]

### RevokePermissions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermission, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]]]


# UpdateFolderPermissionsResponse

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes

### Permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFolderRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateFolderResponse

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateGroupRequest

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateGroupResponse

### Group
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.Group'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateIAMPolicyAssignmentRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AssignmentName
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### AssignmentStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'DRAFT', 'ENABLED']]

### PolicyArn
- **Type**: typing.Optional[str]

### Identities
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]


# UpdateIAMPolicyAssignmentResponse

### AssignmentName
- **Type**: <class 'str'>
- **Required**: Yes

### AssignmentId
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### Identities
- **Type**: typing.Dict[str, typing.List[str]]
- **Required**: Yes

### AssignmentStatus
- **Type**: typing.Literal['DISABLED', 'DRAFT', 'ENABLED']
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateIdentityPropagationConfigRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Service
- **Type**: typing.Literal['QBUSINESS', 'REDSHIFT']
- **Required**: Yes

### AuthorizedTargets
- **Type**: typing.Optional[typing.List[str]]


# UpdateIdentityPropagationConfigResponse

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateIpRestrictionRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### IpRestrictionRuleMap
- **Type**: typing.Optional[typing.Dict[str, str]]

### VpcIdRestrictionRuleMap
- **Type**: typing.Optional[typing.Dict[str, str]]

### VpcEndpointIdRestrictionRuleMap
- **Type**: typing.Optional[typing.Dict[str, str]]

### Enabled
- **Type**: typing.Optional[bool]


# UpdateIpRestrictionResponse

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateKeyRegistrationRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### KeyRegistration
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RegisteredCustomerManagedKey]
- **Required**: Yes


# UpdateKeyRegistrationResponse

### FailedKeyRegistration
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FailedKeyRegistrationEntry]
- **Required**: Yes

### SuccessfulKeyRegistration
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SuccessfulKeyRegistrationEntry]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePublicSharingSettingsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PublicSharingEnabled
- **Type**: typing.Optional[bool]


# UpdatePublicSharingSettingsResponse

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateQPersonalizationConfigurationRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PersonalizationMode
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# UpdateQPersonalizationConfigurationResponse

### PersonalizationMode
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateQuickSightQSearchConfigurationRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### QSearchStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# UpdateQuickSightQSearchConfigurationResponse

### QSearchStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRefreshScheduleRequest

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Schedule
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RefreshSchedule, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RefreshScheduleOutput]
- **Required**: Yes


# UpdateRefreshScheduleResponse

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleId
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRoleCustomPermissionRequest

### CustomPermissionsName
- **Type**: <class 'str'>
- **Required**: Yes

### Role
- **Type**: typing.Literal['ADMIN', 'ADMIN_PRO', 'AUTHOR', 'AUTHOR_PRO', 'READER', 'READER_PRO']
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateRoleCustomPermissionResponse

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSPICECapacityConfigurationRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PurchaseMode
- **Type**: typing.Literal['AUTO_PURCHASE', 'MANUAL']
- **Required**: Yes


# UpdateSPICECapacityConfigurationResponse

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTemplateAliasRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### AliasName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateVersionNumber
- **Type**: <class 'int'>
- **Required**: Yes


# UpdateTemplateAliasResponse

### TemplateAlias
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TemplateAlias'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTemplatePermissionsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### GrantPermissions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermission, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]]]

### RevokePermissions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermission, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]]]


# UpdateTemplatePermissionsResponse

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### Permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTemplateRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### SourceEntity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TemplateSourceEntity]

### VersionDescription
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Definition
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TemplateVersionDefinition, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TemplateVersionDefinitionOutput, NoneType]

### ValidationStrategy
- **Type**: <class 'NoneType'>


# UpdateTemplateResponse

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### VersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationStatus
- **Type**: typing.Literal['CREATION_FAILED', 'CREATION_IN_PROGRESS', 'CREATION_SUCCESSFUL', 'DELETED', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateThemeAliasRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ThemeId
- **Type**: <class 'str'>
- **Required**: Yes

### AliasName
- **Type**: <class 'str'>
- **Required**: Yes

### ThemeVersionNumber
- **Type**: <class 'int'>
- **Required**: Yes


# UpdateThemeAliasResponse

### ThemeAlias
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ThemeAlias'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateThemePermissionsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ThemeId
- **Type**: <class 'str'>
- **Required**: Yes

### GrantPermissions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermission, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]]]

### RevokePermissions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermission, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]]]


# UpdateThemePermissionsResponse

### ThemeId
- **Type**: <class 'str'>
- **Required**: Yes

### ThemeArn
- **Type**: <class 'str'>
- **Required**: Yes

### Permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateThemeRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ThemeId
- **Type**: <class 'str'>
- **Required**: Yes

### BaseThemeId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### VersionDescription
- **Type**: typing.Optional[str]

### Configuration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ThemeConfiguration, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ThemeConfigurationOutput, NoneType]


# UpdateThemeResponse

### ThemeId
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### VersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationStatus
- **Type**: typing.Literal['CREATION_FAILED', 'CREATION_IN_PROGRESS', 'CREATION_SUCCESSFUL', 'DELETED', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTopicPermissionsRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### GrantPermissions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermission, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]]]

### RevokePermissions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermission, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]]]


# UpdateTopicPermissionsResponse

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### Permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResourcePermissionOutput]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTopicRefreshScheduleRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetId
- **Type**: <class 'str'>
- **Required**: Yes

### RefreshSchedule
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicRefreshSchedule, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicRefreshScheduleOutput]
- **Required**: Yes


# UpdateTopicRefreshScheduleResponse

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTopicRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### Topic
- **Type**: typing.Union[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicDetails, aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TopicDetailsOutput]
- **Required**: Yes


# UpdateTopicResponse

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### RefreshArn
- **Type**: <class 'str'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateUserCustomPermissionRequest

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### CustomPermissionsName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateUserCustomPermissionResponse

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateUserRequest

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### Email
- **Type**: <class 'str'>
- **Required**: Yes

### Role
- **Type**: typing.Literal['ADMIN', 'ADMIN_PRO', 'AUTHOR', 'AUTHOR_PRO', 'READER', 'READER_PRO', 'RESTRICTED_AUTHOR', 'RESTRICTED_READER']
- **Required**: Yes

### CustomPermissionsName
- **Type**: typing.Optional[str]

### UnapplyCustomPermissions
- **Type**: typing.Optional[bool]

### ExternalLoginFederationProviderType
- **Type**: typing.Optional[str]

### CustomFederationProviderUrl
- **Type**: typing.Optional[str]

### ExternalLoginId
- **Type**: typing.Optional[str]


# UpdateUserResponse

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.User'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateVPCConnectionRequest

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### VPCConnectionId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### DnsResolvers
- **Type**: typing.Optional[typing.List[str]]


# UpdateVPCConnectionResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### VPCConnectionId
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateStatus
- **Type**: typing.Literal['CREATION_FAILED', 'CREATION_IN_PROGRESS', 'CREATION_SUCCESSFUL', 'DELETED', 'DELETION_FAILED', 'DELETION_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']
- **Required**: Yes

### AvailabilityStatus
- **Type**: typing.Literal['AVAILABLE', 'PARTIALLY_AVAILABLE', 'UNAVAILABLE']
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ResponseMetadata'>
- **Required**: Yes


# UploadSettings

### Format
- **Type**: typing.Optional[typing.Literal['CLF', 'CSV', 'ELF', 'JSON', 'TSV', 'XLSX']]

### StartFromRow
- **Type**: typing.Optional[int]

### ContainsHeader
- **Type**: typing.Optional[bool]

### TextQualifier
- **Type**: typing.Optional[typing.Literal['DOUBLE_QUOTE', 'SINGLE_QUOTE']]

### Delimiter
- **Type**: typing.Optional[str]


# User

### Arn
- **Type**: typing.Optional[str]

### UserName
- **Type**: typing.Optional[str]

### Email
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[typing.Literal['ADMIN', 'ADMIN_PRO', 'AUTHOR', 'AUTHOR_PRO', 'READER', 'READER_PRO', 'RESTRICTED_AUTHOR', 'RESTRICTED_READER']]

### IdentityType
- **Type**: typing.Optional[typing.Literal['IAM', 'IAM_IDENTITY_CENTER', 'QUICKSIGHT']]

### Active
- **Type**: typing.Optional[bool]

### PrincipalId
- **Type**: typing.Optional[str]

### CustomPermissionsName
- **Type**: typing.Optional[str]

### ExternalLoginFederationProviderType
- **Type**: typing.Optional[str]

### ExternalLoginFederationProviderUrl
- **Type**: typing.Optional[str]

### ExternalLoginId
- **Type**: typing.Optional[str]


# VPCConnection

### VPCConnectionId
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### VPCId
- **Type**: typing.Optional[str]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### DnsResolvers
- **Type**: typing.Optional[typing.List[str]]

### Status
- **Type**: typing.Optional[typing.Literal['CREATION_FAILED', 'CREATION_IN_PROGRESS', 'CREATION_SUCCESSFUL', 'DELETED', 'DELETION_FAILED', 'DELETION_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']]

### AvailabilityStatus
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'PARTIALLY_AVAILABLE', 'UNAVAILABLE']]

### NetworkInterfaces
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.NetworkInterface]]

### RoleArn
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]


# VPCConnectionSummary

### VPCConnectionId
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### VPCId
- **Type**: typing.Optional[str]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### DnsResolvers
- **Type**: typing.Optional[typing.List[str]]

### Status
- **Type**: typing.Optional[typing.Literal['CREATION_FAILED', 'CREATION_IN_PROGRESS', 'CREATION_SUCCESSFUL', 'DELETED', 'DELETION_FAILED', 'DELETION_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']]

### AvailabilityStatus
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'PARTIALLY_AVAILABLE', 'UNAVAILABLE']]

### NetworkInterfaces
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.NetworkInterface]]

### RoleArn
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]


# ValidationStrategy

### Mode
- **Type**: typing.Literal['LENIENT', 'STRICT']
- **Required**: Yes


# VisibleRangeOptions

### PercentRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PercentVisibleRange]


# Visual

### TableVisual
- **Type**: <class 'NoneType'>

### PivotTableVisual
- **Type**: <class 'NoneType'>

### BarChartVisual
- **Type**: <class 'NoneType'>

### KPIVisual
- **Type**: <class 'NoneType'>

### PieChartVisual
- **Type**: <class 'NoneType'>

### GaugeChartVisual
- **Type**: <class 'NoneType'>

### LineChartVisual
- **Type**: <class 'NoneType'>

### HeatMapVisual
- **Type**: <class 'NoneType'>

### TreeMapVisual
- **Type**: <class 'NoneType'>

### GeospatialMapVisual
- **Type**: <class 'NoneType'>

### FilledMapVisual
- **Type**: <class 'NoneType'>

### LayerMapVisual
- **Type**: <class 'NoneType'>

### FunnelChartVisual
- **Type**: <class 'NoneType'>

### ScatterPlotVisual
- **Type**: <class 'NoneType'>

### ComboChartVisual
- **Type**: <class 'NoneType'>

### BoxPlotVisual
- **Type**: <class 'NoneType'>

### WaterfallVisual
- **Type**: <class 'NoneType'>

### HistogramVisual
- **Type**: <class 'NoneType'>

### WordCloudVisual
- **Type**: <class 'NoneType'>

### InsightVisual
- **Type**: <class 'NoneType'>

### SankeyDiagramVisual
- **Type**: <class 'NoneType'>

### CustomContentVisual
- **Type**: <class 'NoneType'>

### EmptyVisual
- **Type**: <class 'NoneType'>

### RadarChartVisual
- **Type**: <class 'NoneType'>

### PluginVisual
- **Type**: <class 'NoneType'>


# VisualAxisSortOption

### AvailabilityStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# VisualCustomAction

### CustomActionId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Trigger
- **Type**: typing.Literal['DATA_POINT_CLICK', 'DATA_POINT_MENU']
- **Required**: Yes

### ActionOperations
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomActionOperation]
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# VisualCustomActionOperation

### FilterOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CustomActionFilterOperation]

### NavigationOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CustomActionNavigationOperation]

### URLOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CustomActionURLOperation]

### SetParametersOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CustomActionSetParametersOperation]


# VisualCustomActionOperationOutput

### FilterOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CustomActionFilterOperationOutput]

### NavigationOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CustomActionNavigationOperation]

### URLOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CustomActionURLOperation]

### SetParametersOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CustomActionSetParametersOperationOutput]


# VisualCustomActionOutput

### CustomActionId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Trigger
- **Type**: typing.Literal['DATA_POINT_CLICK', 'DATA_POINT_MENU']
- **Required**: Yes

### ActionOperations
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomActionOperationOutput]
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# VisualInteractionOptions

### VisualMenuOption
- **Type**: <class 'NoneType'>

### ContextMenuOption
- **Type**: <class 'NoneType'>


# VisualMenuOption

### AvailabilityStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# VisualOptions

### type
- **Type**: typing.Optional[str]


# VisualOutput

### TableVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TableVisualOutput]

### PivotTableVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PivotTableVisualOutput]

### BarChartVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BarChartVisualOutput]

### KPIVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.KPIVisualOutput]

### PieChartVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PieChartVisualOutput]

### GaugeChartVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GaugeChartVisualOutput]

### LineChartVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LineChartVisualOutput]

### HeatMapVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.HeatMapVisualOutput]

### TreeMapVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.TreeMapVisualOutput]

### GeospatialMapVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.GeospatialMapVisualOutput]

### FilledMapVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FilledMapVisualOutput]

### LayerMapVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LayerMapVisualOutput]

### FunnelChartVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FunnelChartVisualOutput]

### ScatterPlotVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ScatterPlotVisualOutput]

### ComboChartVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ComboChartVisualOutput]

### BoxPlotVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.BoxPlotVisualOutput]

### WaterfallVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.WaterfallVisualOutput]

### HistogramVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.HistogramVisualOutput]

### WordCloudVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.WordCloudVisualOutput]

### InsightVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.InsightVisualOutput]

### SankeyDiagramVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.SankeyDiagramVisualOutput]

### CustomContentVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.CustomContentVisualOutput]

### EmptyVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.EmptyVisualOutput]

### RadarChartVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.RadarChartVisualOutput]

### PluginVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.PluginVisualOutput]


# VisualPalette

### ChartColor
- **Type**: typing.Optional[str]

### ColorMap
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataPathColor]]


# VisualPaletteOutput

### ChartColor
- **Type**: typing.Optional[str]

### ColorMap
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataPathColor]]


# VisualSubtitleLabelOptions

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### FormatText
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LongFormatText]


# VisualTitleLabelOptions

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### FormatText
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ShortFormatText]


# VpcConnectionProperties

### VpcConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes


# WaterfallChartAggregatedFieldWells

### Categories
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]

### Breakdowns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]


# WaterfallChartAggregatedFieldWellsOutput

### Categories
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]

### Breakdowns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]


# WaterfallChartColorConfiguration

### GroupColorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.WaterfallChartGroupColorConfiguration]


# WaterfallChartConfiguration

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.WaterfallChartFieldWells]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.WaterfallChartSortConfiguration]

### WaterfallChartOptions
- **Type**: <class 'NoneType'>

### CategoryAxisLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptions]

### CategoryAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDisplayOptions]

### PrimaryYAxisLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptions]

### PrimaryYAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDisplayOptions]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LegendOptions]

### DataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataLabelOptions]

### VisualPalette
- **Type**: <class 'NoneType'>

### ColorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.WaterfallChartColorConfiguration]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# WaterfallChartConfigurationOutput

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.WaterfallChartFieldWellsOutput]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.WaterfallChartSortConfigurationOutput]

### WaterfallChartOptions
- **Type**: <class 'NoneType'>

### CategoryAxisLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptionsOutput]

### CategoryAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDisplayOptionsOutput]

### PrimaryYAxisLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptionsOutput]

### PrimaryYAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.AxisDisplayOptionsOutput]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.LegendOptions]

### DataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DataLabelOptionsOutput]

### VisualPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualPaletteOutput]

### ColorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.WaterfallChartColorConfiguration]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# WaterfallChartFieldWells

### WaterfallChartAggregatedFieldWells
- **Type**: <class 'NoneType'>


# WaterfallChartFieldWellsOutput

### WaterfallChartAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.WaterfallChartAggregatedFieldWellsOutput]


# WaterfallChartGroupColorConfiguration

### PositiveBarColor
- **Type**: typing.Optional[str]

### NegativeBarColor
- **Type**: typing.Optional[str]

### TotalBarColor
- **Type**: typing.Optional[str]


# WaterfallChartOptions

### TotalBarLabel
- **Type**: typing.Optional[str]


# WaterfallChartSortConfiguration

### CategorySort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### BreakdownItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]


# WaterfallChartSortConfigurationOutput

### CategorySort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]

### BreakdownItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]


# WaterfallVisual

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.WaterfallChartConfiguration]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomAction]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnHierarchy]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# WaterfallVisualOutput

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.WaterfallChartConfigurationOutput]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomActionOutput]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnHierarchyOutput]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# WhatIfPointScenario

### Date
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### Value
- **Type**: <class 'float'>
- **Required**: Yes


# WhatIfPointScenarioOutput

### Date
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Value
- **Type**: <class 'float'>
- **Required**: Yes


# WhatIfRangeScenario

### StartDate
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndDate
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### Value
- **Type**: <class 'float'>
- **Required**: Yes


# WhatIfRangeScenarioOutput

### StartDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Value
- **Type**: <class 'float'>
- **Required**: Yes


# WordCloudAggregatedFieldWells

### GroupBy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Size
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]


# WordCloudAggregatedFieldWellsOutput

### GroupBy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.DimensionField]]

### Size
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.MeasureField]]


# WordCloudChartConfiguration

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.WordCloudFieldWells]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.WordCloudSortConfiguration]

### CategoryLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptions]

### WordCloudOptions
- **Type**: <class 'NoneType'>

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# WordCloudChartConfigurationOutput

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.WordCloudFieldWellsOutput]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.WordCloudSortConfigurationOutput]

### CategoryLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ChartAxisLabelOptionsOutput]

### WordCloudOptions
- **Type**: <class 'NoneType'>

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualInteractionOptions]


# WordCloudFieldWells

### WordCloudAggregatedFieldWells
- **Type**: <class 'NoneType'>


# WordCloudFieldWellsOutput

### WordCloudAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.WordCloudAggregatedFieldWellsOutput]


# WordCloudOptions

### WordOrientation
- **Type**: typing.Optional[typing.Literal['HORIZONTAL', 'HORIZONTAL_AND_VERTICAL']]

### WordScaling
- **Type**: typing.Optional[typing.Literal['EMPHASIZE', 'NORMAL']]

### CloudLayout
- **Type**: typing.Optional[typing.Literal['FLUID', 'NORMAL']]

### WordCasing
- **Type**: typing.Optional[typing.Literal['EXISTING_CASE', 'LOWER_CASE']]

### WordPadding
- **Type**: typing.Optional[typing.Literal['LARGE', 'MEDIUM', 'NONE', 'SMALL']]

### MaximumStringLength
- **Type**: typing.Optional[int]


# WordCloudSortConfiguration

### CategoryItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]

### CategorySort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]


# WordCloudSortConfigurationOutput

### CategoryItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ItemsLimitConfiguration]

### CategorySort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.FieldSortOptions]]


# WordCloudVisual

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.WordCloudChartConfiguration]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomAction]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnHierarchy]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# WordCloudVisualOutput

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualTitleLabelOptions]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualSubtitleLabelOptions]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.WordCloudChartConfigurationOutput]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.VisualCustomActionOutput]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight.quicksight_classes.ColumnHierarchyOutput]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# YAxisOptions

### YAxis
- **Type**: typing.Literal['PRIMARY_Y_AXIS']
- **Required**: Yes



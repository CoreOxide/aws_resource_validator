# Quicksight Classes

# AccountCustomizationTypeDef

### DefaultTheme
- **Type**: typing.Optional[str]

### DefaultEmailCustomizationTemplate
- **Type**: typing.Optional[str]


# AccountInfoTypeDef

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


# AccountSettingsTypeDef

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


# ActiveIAMPolicyAssignmentTypeDef

### AssignmentName
- **Type**: typing.Optional[str]

### PolicyArn
- **Type**: typing.Optional[str]


# AdHocFilteringOptionTypeDef

### AvailabilityStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# AggFunctionOutputTypeDef

### Aggregation
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'COLUMN', 'COUNT', 'CUSTOM', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'PERCENTILE', 'PTD_AVERAGE', 'PTD_COUNT', 'PTD_DISTINCT_COUNT', 'PTD_MAX', 'PTD_MIN', 'PTD_SUM', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]

### AggregationFunctionParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### Period
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### PeriodField
- **Type**: typing.Optional[str]


# AggFunctionTypeDef

### Aggregation
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'COLUMN', 'COUNT', 'CUSTOM', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'PERCENTILE', 'PTD_AVERAGE', 'PTD_COUNT', 'PTD_DISTINCT_COUNT', 'PTD_MAX', 'PTD_MIN', 'PTD_SUM', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]

### AggregationFunctionParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Period
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### PeriodField
- **Type**: typing.Optional[str]


# AggFunctionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AggregationFunctionTypeDef

### NumericalAggregationFunction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NumericalAggregationFunctionTypeDef]

### CategoricalAggregationFunction
- **Type**: typing.Optional[typing.Literal['COUNT', 'DISTINCT_COUNT']]

### DateAggregationFunction
- **Type**: typing.Optional[typing.Literal['COUNT', 'DISTINCT_COUNT', 'MAX', 'MIN']]

### AttributeAggregationFunction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AttributeAggregationFunctionTypeDef]


# AggregationPartitionByTypeDef

### FieldName
- **Type**: typing.Optional[str]

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]


# AggregationSortConfigurationTypeDef

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes

### SortDirection
- **Type**: typing.Literal['ASC', 'DESC']
- **Required**: Yes

### AggregationFunction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AggregationFunctionTypeDef]


# AmazonElasticsearchParametersTypeDef

### Domain
- **Type**: <class 'str'>
- **Required**: Yes


# AmazonOpenSearchParametersTypeDef

### Domain
- **Type**: <class 'str'>
- **Required**: Yes


# AnalysisDefaultsTypeDef

### DefaultNewSheetConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.DefaultNewSheetConfigurationTypeDef'>
- **Required**: Yes


# AnalysisDefinitionOutputTypeDef

### DataSetIdentifierDeclarations
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DataSetIdentifierDeclarationTypeDef]
- **Required**: Yes

### Sheets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.SheetDefinitionOutputTypeDef]]

### CalculatedFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.CalculatedFieldTypeDef]]

### ParameterDeclarations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ParameterDeclarationOutputTypeDef]]

### FilterGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.FilterGroupOutputTypeDef]]

### ColumnConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ColumnConfigurationOutputTypeDef]]

### AnalysisDefaults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AnalysisDefaultsTypeDef]

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AssetOptionsTypeDef]

### QueryExecutionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.QueryExecutionOptionsTypeDef]

### StaticFiles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.StaticFileTypeDef]]


# AnalysisDefinitionTypeDef

### DataSetIdentifierDeclarations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DataSetIdentifierDeclarationTypeDef]
- **Required**: Yes

### Sheets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.SheetDefinitionTypeDef]]

### CalculatedFields
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.CalculatedFieldTypeDef]]

### ParameterDeclarations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ParameterDeclarationTypeDef]]

### FilterGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.FilterGroupTypeDef]]

### ColumnConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ColumnConfigurationTypeDef]]

### AnalysisDefaults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AnalysisDefaultsTypeDef]

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AssetOptionsTypeDef]

### QueryExecutionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.QueryExecutionOptionsTypeDef]

### StaticFiles
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.StaticFileTypeDef]]


# AnalysisDefinitionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AnalysisErrorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AnalysisSearchFilterTypeDef

### Operator
- **Type**: typing.Optional[typing.Literal['StringEquals', 'StringLike']]

### Name
- **Type**: typing.Optional[typing.Literal['ANALYSIS_NAME', 'DIRECT_QUICKSIGHT_OWNER', 'DIRECT_QUICKSIGHT_SOLE_OWNER', 'DIRECT_QUICKSIGHT_VIEWER_OR_OWNER', 'QUICKSIGHT_OWNER', 'QUICKSIGHT_USER', 'QUICKSIGHT_VIEWER_OR_OWNER']]

### Value
- **Type**: typing.Optional[str]


# AnalysisSourceEntityTypeDef

### SourceTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AnalysisSourceTemplateTypeDef]


# AnalysisSourceTemplateTypeDef

### DataSetReferences
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DataSetReferenceTypeDef]
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# AnalysisSummaryTypeDef

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


# AnalysisTypeDef

### AnalysisId
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CREATION_FAILED', 'CREATION_IN_PROGRESS', 'CREATION_SUCCESSFUL', 'DELETED', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']]

### Errors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AnalysisErrorTypeDef]]

### DataSetArns
- **Type**: typing.Optional[typing.List[str]]

### ThemeArn
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### Sheets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.SheetTypeDef]]


# AnchorDateConfigurationTypeDef

### AnchorOption
- **Type**: typing.Optional[typing.Literal['NOW']]

### ParameterName
- **Type**: typing.Optional[str]


# AnchorTypeDef

### AnchorType
- **Type**: typing.Optional[typing.Literal['TODAY']]

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### Offset
- **Type**: typing.Optional[int]


# AnonymousUserDashboardEmbeddingConfigurationTypeDef

### InitialDashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### EnabledFeatures
- **Type**: typing.Optional[typing.Sequence[typing.Literal['SHARED_VIEW']]]

### DisabledFeatures
- **Type**: typing.Optional[typing.Sequence[typing.Literal['SHARED_VIEW']]]

### FeatureConfigurations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AnonymousUserDashboardFeatureConfigurationsTypeDef]


# AnonymousUserDashboardFeatureConfigurationsTypeDef

### SharedView
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SharedViewConfigurationsTypeDef]


# AnonymousUserDashboardVisualEmbeddingConfigurationTypeDef

### InitialDashboardVisualId
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.DashboardVisualIdTypeDef'>
- **Required**: Yes


# AnonymousUserEmbeddingExperienceConfigurationTypeDef

### Dashboard
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AnonymousUserDashboardEmbeddingConfigurationTypeDef]

### DashboardVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AnonymousUserDashboardVisualEmbeddingConfigurationTypeDef]

### QSearchBar
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AnonymousUserQSearchBarEmbeddingConfigurationTypeDef]

### GenerativeQnA
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AnonymousUserGenerativeQnAEmbeddingConfigurationTypeDef]


# AnonymousUserGenerativeQnAEmbeddingConfigurationTypeDef

### InitialTopicId
- **Type**: <class 'str'>
- **Required**: Yes


# AnonymousUserQSearchBarEmbeddingConfigurationTypeDef

### InitialTopicId
- **Type**: <class 'str'>
- **Required**: Yes


# AnonymousUserSnapshotJobResultTypeDef

### FileGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.SnapshotJobResultFileGroupTypeDef]]


# ApplicationThemeTypeDef

### BrandColorPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BrandColorPaletteTypeDef]

### BrandElementStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BrandElementStyleTypeDef]


# ArcAxisConfigurationTypeDef

### Range
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ArcAxisDisplayRangeTypeDef]

### ReserveRange
- **Type**: typing.Optional[int]


# ArcAxisDisplayRangeTypeDef

### Min
- **Type**: typing.Optional[float]

### Max
- **Type**: typing.Optional[float]


# ArcConfigurationTypeDef

### ArcAngle
- **Type**: typing.Optional[float]

### ArcThickness
- **Type**: typing.Optional[typing.Literal['LARGE', 'MEDIUM', 'SMALL']]


# ArcOptionsTypeDef

### ArcThickness
- **Type**: typing.Optional[typing.Literal['LARGE', 'MEDIUM', 'SMALL', 'WHOLE']]


# AssetBundleCloudFormationOverridePropertyConfigurationOutputTypeDef

### ResourceIdOverrideConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleExportJobResourceIdOverrideConfigurationTypeDef]

### VPCConnections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleExportJobVPCConnectionOverridePropertiesOutputTypeDef]]

### RefreshSchedules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleExportJobRefreshScheduleOverridePropertiesOutputTypeDef]]

### DataSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleExportJobDataSourceOverridePropertiesOutputTypeDef]]

### DataSets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleExportJobDataSetOverridePropertiesOutputTypeDef]]

### Themes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleExportJobThemeOverridePropertiesOutputTypeDef]]

### Analyses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleExportJobAnalysisOverridePropertiesOutputTypeDef]]

### Dashboards
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleExportJobDashboardOverridePropertiesOutputTypeDef]]

### Folders
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleExportJobFolderOverridePropertiesOutputTypeDef]]


# AssetBundleCloudFormationOverridePropertyConfigurationTypeDef

### ResourceIdOverrideConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleExportJobResourceIdOverrideConfigurationTypeDef]

### VPCConnections
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleExportJobVPCConnectionOverridePropertiesTypeDef]]

### RefreshSchedules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleExportJobRefreshScheduleOverridePropertiesTypeDef]]

### DataSources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleExportJobDataSourceOverridePropertiesTypeDef]]

### DataSets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleExportJobDataSetOverridePropertiesTypeDef]]

### Themes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleExportJobThemeOverridePropertiesTypeDef]]

### Analyses
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleExportJobAnalysisOverridePropertiesTypeDef]]

### Dashboards
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleExportJobDashboardOverridePropertiesTypeDef]]

### Folders
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleExportJobFolderOverridePropertiesTypeDef]]


# AssetBundleCloudFormationOverridePropertyConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssetBundleExportJobAnalysisOverridePropertiesOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.List[typing.Literal['Name']]
- **Required**: Yes


# AssetBundleExportJobAnalysisOverridePropertiesTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.Sequence[typing.Literal['Name']]
- **Required**: Yes


# AssetBundleExportJobDashboardOverridePropertiesOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.List[typing.Literal['Name']]
- **Required**: Yes


# AssetBundleExportJobDashboardOverridePropertiesTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.Sequence[typing.Literal['Name']]
- **Required**: Yes


# AssetBundleExportJobDataSetOverridePropertiesOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.List[typing.Literal['Name']]
- **Required**: Yes


# AssetBundleExportJobDataSetOverridePropertiesTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.Sequence[typing.Literal['Name']]
- **Required**: Yes


# AssetBundleExportJobDataSourceOverridePropertiesOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.List[typing.Literal['Catalog', 'ClusterId', 'DataSetName', 'Database', 'DisableSsl', 'Domain', 'Host', 'InstanceId', 'ManifestFileLocation', 'Name', 'Password', 'Port', 'ProductType', 'RoleArn', 'SecretArn', 'Username', 'Warehouse', 'WorkGroup']]
- **Required**: Yes


# AssetBundleExportJobDataSourceOverridePropertiesTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.Sequence[typing.Literal['Catalog', 'ClusterId', 'DataSetName', 'Database', 'DisableSsl', 'Domain', 'Host', 'InstanceId', 'ManifestFileLocation', 'Name', 'Password', 'Port', 'ProductType', 'RoleArn', 'SecretArn', 'Username', 'Warehouse', 'WorkGroup']]
- **Required**: Yes


# AssetBundleExportJobErrorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssetBundleExportJobFolderOverridePropertiesOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.List[typing.Literal['Name', 'ParentFolderArn']]
- **Required**: Yes


# AssetBundleExportJobFolderOverridePropertiesTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.Sequence[typing.Literal['Name', 'ParentFolderArn']]
- **Required**: Yes


# AssetBundleExportJobRefreshScheduleOverridePropertiesOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.List[typing.Literal['StartAfterDateTime']]
- **Required**: Yes


# AssetBundleExportJobRefreshScheduleOverridePropertiesTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.Sequence[typing.Literal['StartAfterDateTime']]
- **Required**: Yes


# AssetBundleExportJobResourceIdOverrideConfigurationTypeDef

### PrefixForAllResources
- **Type**: typing.Optional[bool]


# AssetBundleExportJobSummaryTypeDef

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


# AssetBundleExportJobThemeOverridePropertiesOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.List[typing.Literal['Name']]
- **Required**: Yes


# AssetBundleExportJobThemeOverridePropertiesTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.Sequence[typing.Literal['Name']]
- **Required**: Yes


# AssetBundleExportJobVPCConnectionOverridePropertiesOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.List[typing.Literal['DnsResolvers', 'Name', 'RoleArn']]
- **Required**: Yes


# AssetBundleExportJobVPCConnectionOverridePropertiesTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.Sequence[typing.Literal['DnsResolvers', 'Name', 'RoleArn']]
- **Required**: Yes


# AssetBundleExportJobValidationStrategyTypeDef

### StrictModeForAllResources
- **Type**: typing.Optional[bool]


# AssetBundleExportJobWarningTypeDef

### Arn
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# AssetBundleImportJobAnalysisOverrideParametersTypeDef

### AnalysisId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# AssetBundleImportJobAnalysisOverridePermissionsOutputTypeDef

### AnalysisIds
- **Type**: typing.List[str]
- **Required**: Yes

### Permissions
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleResourcePermissionsOutputTypeDef'>
- **Required**: Yes


# AssetBundleImportJobAnalysisOverridePermissionsTypeDef

### AnalysisIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Permissions
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleResourcePermissionsTypeDef'>
- **Required**: Yes


# AssetBundleImportJobAnalysisOverrideTagsOutputTypeDef

### AnalysisIds
- **Type**: typing.List[str]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.TagTypeDef]
- **Required**: Yes


# AssetBundleImportJobAnalysisOverrideTagsTypeDef

### AnalysisIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TagTypeDef]
- **Required**: Yes


# AssetBundleImportJobDashboardOverrideParametersTypeDef

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# AssetBundleImportJobDashboardOverridePermissionsOutputTypeDef

### DashboardIds
- **Type**: typing.List[str]
- **Required**: Yes

### Permissions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleResourcePermissionsOutputTypeDef]

### LinkSharingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleResourceLinkSharingConfigurationOutputTypeDef]


# AssetBundleImportJobDashboardOverridePermissionsTypeDef

### DashboardIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Permissions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleResourcePermissionsTypeDef]

### LinkSharingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleResourceLinkSharingConfigurationTypeDef]


# AssetBundleImportJobDashboardOverrideTagsOutputTypeDef

### DashboardIds
- **Type**: typing.List[str]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.TagTypeDef]
- **Required**: Yes


# AssetBundleImportJobDashboardOverrideTagsTypeDef

### DashboardIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TagTypeDef]
- **Required**: Yes


# AssetBundleImportJobDataSetOverrideParametersTypeDef

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# AssetBundleImportJobDataSetOverridePermissionsOutputTypeDef

### DataSetIds
- **Type**: typing.List[str]
- **Required**: Yes

### Permissions
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleResourcePermissionsOutputTypeDef'>
- **Required**: Yes


# AssetBundleImportJobDataSetOverridePermissionsTypeDef

### DataSetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Permissions
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleResourcePermissionsTypeDef'>
- **Required**: Yes


# AssetBundleImportJobDataSetOverrideTagsOutputTypeDef

### DataSetIds
- **Type**: typing.List[str]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.TagTypeDef]
- **Required**: Yes


# AssetBundleImportJobDataSetOverrideTagsTypeDef

### DataSetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TagTypeDef]
- **Required**: Yes


# AssetBundleImportJobDataSourceCredentialPairTypeDef

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: <class 'str'>
- **Required**: Yes


# AssetBundleImportJobDataSourceCredentialsTypeDef

### CredentialPair
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobDataSourceCredentialPairTypeDef]

### SecretArn
- **Type**: typing.Optional[str]


# AssetBundleImportJobDataSourceOverrideParametersOutputTypeDef

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### DataSourceParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataSourceParametersOutputTypeDef]

### VpcConnectionProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VpcConnectionPropertiesTypeDef]

### SslProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SslPropertiesTypeDef]

### Credentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobDataSourceCredentialsTypeDef]


# AssetBundleImportJobDataSourceOverrideParametersTypeDef

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### DataSourceParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataSourceParametersTypeDef]

### VpcConnectionProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VpcConnectionPropertiesTypeDef]

### SslProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SslPropertiesTypeDef]

### Credentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobDataSourceCredentialsTypeDef]


# AssetBundleImportJobDataSourceOverridePermissionsOutputTypeDef

### DataSourceIds
- **Type**: typing.List[str]
- **Required**: Yes

### Permissions
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleResourcePermissionsOutputTypeDef'>
- **Required**: Yes


# AssetBundleImportJobDataSourceOverridePermissionsTypeDef

### DataSourceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Permissions
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleResourcePermissionsTypeDef'>
- **Required**: Yes


# AssetBundleImportJobDataSourceOverrideTagsOutputTypeDef

### DataSourceIds
- **Type**: typing.List[str]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.TagTypeDef]
- **Required**: Yes


# AssetBundleImportJobDataSourceOverrideTagsTypeDef

### DataSourceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TagTypeDef]
- **Required**: Yes


# AssetBundleImportJobErrorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssetBundleImportJobFolderOverrideParametersTypeDef

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### ParentFolderArn
- **Type**: typing.Optional[str]


# AssetBundleImportJobFolderOverridePermissionsOutputTypeDef

### FolderIds
- **Type**: typing.List[str]
- **Required**: Yes

### Permissions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleResourcePermissionsOutputTypeDef]


# AssetBundleImportJobFolderOverridePermissionsTypeDef

### FolderIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Permissions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleResourcePermissionsTypeDef]


# AssetBundleImportJobFolderOverrideTagsOutputTypeDef

### FolderIds
- **Type**: typing.List[str]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.TagTypeDef]
- **Required**: Yes


# AssetBundleImportJobFolderOverrideTagsTypeDef

### FolderIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TagTypeDef]
- **Required**: Yes


# AssetBundleImportJobOverrideParametersOutputTypeDef

### ResourceIdOverrideConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobResourceIdOverrideConfigurationTypeDef]

### VPCConnections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobVPCConnectionOverrideParametersOutputTypeDef]]

### RefreshSchedules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobRefreshScheduleOverrideParametersOutputTypeDef]]

### DataSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobDataSourceOverrideParametersOutputTypeDef]]

### DataSets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobDataSetOverrideParametersTypeDef]]

### Themes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobThemeOverrideParametersTypeDef]]

### Analyses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobAnalysisOverrideParametersTypeDef]]

### Dashboards
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobDashboardOverrideParametersTypeDef]]

### Folders
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobFolderOverrideParametersTypeDef]]


# AssetBundleImportJobOverrideParametersTypeDef

### ResourceIdOverrideConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobResourceIdOverrideConfigurationTypeDef]

### VPCConnections
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobVPCConnectionOverrideParametersTypeDef]]

### RefreshSchedules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobRefreshScheduleOverrideParametersTypeDef]]

### DataSources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobDataSourceOverrideParametersTypeDef]]

### DataSets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobDataSetOverrideParametersTypeDef]]

### Themes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobThemeOverrideParametersTypeDef]]

### Analyses
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobAnalysisOverrideParametersTypeDef]]

### Dashboards
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobDashboardOverrideParametersTypeDef]]

### Folders
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobFolderOverrideParametersTypeDef]]


# AssetBundleImportJobOverrideParametersUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssetBundleImportJobOverridePermissionsOutputTypeDef

### DataSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobDataSourceOverridePermissionsOutputTypeDef]]

### DataSets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobDataSetOverridePermissionsOutputTypeDef]]

### Themes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobThemeOverridePermissionsOutputTypeDef]]

### Analyses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobAnalysisOverridePermissionsOutputTypeDef]]

### Dashboards
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobDashboardOverridePermissionsOutputTypeDef]]

### Folders
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobFolderOverridePermissionsOutputTypeDef]]


# AssetBundleImportJobOverridePermissionsTypeDef

### DataSources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobDataSourceOverridePermissionsTypeDef]]

### DataSets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobDataSetOverridePermissionsTypeDef]]

### Themes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobThemeOverridePermissionsTypeDef]]

### Analyses
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobAnalysisOverridePermissionsTypeDef]]

### Dashboards
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobDashboardOverridePermissionsTypeDef]]

### Folders
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobFolderOverridePermissionsTypeDef]]


# AssetBundleImportJobOverridePermissionsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssetBundleImportJobOverrideTagsOutputTypeDef

### VPCConnections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobVPCConnectionOverrideTagsOutputTypeDef]]

### DataSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobDataSourceOverrideTagsOutputTypeDef]]

### DataSets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobDataSetOverrideTagsOutputTypeDef]]

### Themes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobThemeOverrideTagsOutputTypeDef]]

### Analyses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobAnalysisOverrideTagsOutputTypeDef]]

### Dashboards
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobDashboardOverrideTagsOutputTypeDef]]

### Folders
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobFolderOverrideTagsOutputTypeDef]]


# AssetBundleImportJobOverrideTagsTypeDef

### VPCConnections
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobVPCConnectionOverrideTagsTypeDef]]

### DataSources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobDataSourceOverrideTagsTypeDef]]

### DataSets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobDataSetOverrideTagsTypeDef]]

### Themes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobThemeOverrideTagsTypeDef]]

### Analyses
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobAnalysisOverrideTagsTypeDef]]

### Dashboards
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobDashboardOverrideTagsTypeDef]]

### Folders
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobFolderOverrideTagsTypeDef]]


# AssetBundleImportJobOverrideTagsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssetBundleImportJobOverrideValidationStrategyTypeDef

### StrictModeForAllResources
- **Type**: typing.Optional[bool]


# AssetBundleImportJobRefreshScheduleOverrideParametersOutputTypeDef

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleId
- **Type**: <class 'str'>
- **Required**: Yes

### StartAfterDateTime
- **Type**: typing.Optional[datetime.datetime]


# AssetBundleImportJobRefreshScheduleOverrideParametersTypeDef

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleId
- **Type**: <class 'str'>
- **Required**: Yes

### StartAfterDateTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TimestampTypeDef]


# AssetBundleImportJobResourceIdOverrideConfigurationTypeDef

### PrefixForAllResources
- **Type**: typing.Optional[str]


# AssetBundleImportJobSummaryTypeDef

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


# AssetBundleImportJobThemeOverrideParametersTypeDef

### ThemeId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# AssetBundleImportJobThemeOverridePermissionsOutputTypeDef

### ThemeIds
- **Type**: typing.List[str]
- **Required**: Yes

### Permissions
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleResourcePermissionsOutputTypeDef'>
- **Required**: Yes


# AssetBundleImportJobThemeOverridePermissionsTypeDef

### ThemeIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Permissions
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleResourcePermissionsTypeDef'>
- **Required**: Yes


# AssetBundleImportJobThemeOverrideTagsOutputTypeDef

### ThemeIds
- **Type**: typing.List[str]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.TagTypeDef]
- **Required**: Yes


# AssetBundleImportJobThemeOverrideTagsTypeDef

### ThemeIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TagTypeDef]
- **Required**: Yes


# AssetBundleImportJobVPCConnectionOverrideParametersOutputTypeDef

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


# AssetBundleImportJobVPCConnectionOverrideParametersTypeDef

### VPCConnectionId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### SubnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### DnsResolvers
- **Type**: typing.Optional[typing.Sequence[str]]

### RoleArn
- **Type**: typing.Optional[str]


# AssetBundleImportJobVPCConnectionOverrideTagsOutputTypeDef

### VPCConnectionIds
- **Type**: typing.List[str]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.TagTypeDef]
- **Required**: Yes


# AssetBundleImportJobVPCConnectionOverrideTagsTypeDef

### VPCConnectionIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TagTypeDef]
- **Required**: Yes


# AssetBundleImportJobWarningTypeDef

### Arn
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# AssetBundleImportSourceDescriptionTypeDef

### Body
- **Type**: typing.Optional[str]

### S3Uri
- **Type**: typing.Optional[str]


# AssetBundleImportSourceTypeDef

### Body
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BlobTypeDef]

### S3Uri
- **Type**: typing.Optional[str]


# AssetBundleResourceLinkSharingConfigurationOutputTypeDef

### Permissions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleResourcePermissionsOutputTypeDef]


# AssetBundleResourceLinkSharingConfigurationTypeDef

### Permissions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleResourcePermissionsTypeDef]


# AssetBundleResourcePermissionsOutputTypeDef

### Principals
- **Type**: typing.List[str]
- **Required**: Yes

### Actions
- **Type**: typing.List[str]
- **Required**: Yes


# AssetBundleResourcePermissionsTypeDef

### Principals
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Actions
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AssetOptionsTypeDef

### Timezone
- **Type**: typing.Optional[str]

### WeekStart
- **Type**: typing.Optional[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY']]


# AthenaParametersTypeDef

### WorkGroup
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]


# AttributeAggregationFunctionTypeDef

### SimpleAttributeAggregation
- **Type**: typing.Optional[typing.Literal['UNIQUE_VALUE']]

### ValueForMultipleValues
- **Type**: typing.Optional[str]


# AuroraParametersTypeDef

### Host
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes


# AuroraPostgreSqlParametersTypeDef

### Host
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes


# AuthorizedTargetsByServiceTypeDef

### Service
- **Type**: typing.Optional[typing.Literal['QBUSINESS', 'REDSHIFT']]

### AuthorizedTargets
- **Type**: typing.Optional[typing.List[str]]


# AwsIotAnalyticsParametersTypeDef

### DataSetName
- **Type**: <class 'str'>
- **Required**: Yes


# AxisDataOptionsOutputTypeDef

### NumericAxisOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NumericAxisOptionsOutputTypeDef]

### DateAxisOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DateAxisOptionsTypeDef]


# AxisDataOptionsTypeDef

### NumericAxisOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NumericAxisOptionsTypeDef]

### DateAxisOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DateAxisOptionsTypeDef]


# AxisDisplayMinMaxRangeTypeDef

### Minimum
- **Type**: typing.Optional[float]

### Maximum
- **Type**: typing.Optional[float]


# AxisDisplayOptionsOutputTypeDef

### TickLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisTickLabelOptionsTypeDef]

### AxisLineVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### GridLineVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### DataOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisDataOptionsOutputTypeDef]

### ScrollbarOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ScrollBarOptionsTypeDef]

### AxisOffset
- **Type**: typing.Optional[str]


# AxisDisplayOptionsTypeDef

### TickLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisTickLabelOptionsTypeDef]

### AxisLineVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### GridLineVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### DataOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisDataOptionsTypeDef]

### ScrollbarOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ScrollBarOptionsTypeDef]

### AxisOffset
- **Type**: typing.Optional[str]


# AxisDisplayRangeOutputTypeDef

### MinMax
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisDisplayMinMaxRangeTypeDef]

### DataDriven
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# AxisDisplayRangeTypeDef

### MinMax
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisDisplayMinMaxRangeTypeDef]

### DataDriven
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# AxisLabelOptionsTypeDef

### FontConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FontConfigurationTypeDef]

### CustomLabel
- **Type**: typing.Optional[str]

### ApplyTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisLabelReferenceOptionsTypeDef]


# AxisLabelReferenceOptionsTypeDef

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes


# AxisLinearScaleTypeDef

### StepCount
- **Type**: typing.Optional[int]

### StepSize
- **Type**: typing.Optional[float]


# AxisLogarithmicScaleTypeDef

### Base
- **Type**: typing.Optional[float]


# AxisScaleTypeDef

### Linear
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisLinearScaleTypeDef]

### Logarithmic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisLogarithmicScaleTypeDef]


# AxisTickLabelOptionsTypeDef

### LabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LabelOptionsTypeDef]

### RotationAngle
- **Type**: typing.Optional[float]


# BarChartAggregatedFieldWellsOutputTypeDef

### Category
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]

### Colors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### SmallMultiples
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]


# BarChartAggregatedFieldWellsTypeDef

### Category
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Values
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]

### Colors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### SmallMultiples
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]


# BarChartConfigurationOutputTypeDef

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BarChartFieldWellsOutputTypeDef]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BarChartSortConfigurationOutputTypeDef]

### Orientation
- **Type**: typing.Optional[typing.Literal['HORIZONTAL', 'VERTICAL']]

### BarsArrangement
- **Type**: typing.Optional[typing.Literal['CLUSTERED', 'STACKED', 'STACKED_PERCENT']]

### VisualPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualPaletteOutputTypeDef]

### SmallMultiplesOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SmallMultiplesOptionsTypeDef]

### CategoryAxis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisDisplayOptionsOutputTypeDef]

### CategoryLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsOutputTypeDef]

### ValueAxis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisDisplayOptionsOutputTypeDef]

### ValueLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsOutputTypeDef]

### ColorLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsOutputTypeDef]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LegendOptionsTypeDef]

### DataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataLabelOptionsOutputTypeDef]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TooltipOptionsOutputTypeDef]

### ReferenceLines
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ReferenceLineTypeDef]]

### ContributionAnalysisDefaults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ContributionAnalysisDefaultOutputTypeDef]]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# BarChartConfigurationTypeDef

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BarChartFieldWellsTypeDef]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BarChartSortConfigurationTypeDef]

### Orientation
- **Type**: typing.Optional[typing.Literal['HORIZONTAL', 'VERTICAL']]

### BarsArrangement
- **Type**: typing.Optional[typing.Literal['CLUSTERED', 'STACKED', 'STACKED_PERCENT']]

### VisualPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualPaletteTypeDef]

### SmallMultiplesOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SmallMultiplesOptionsTypeDef]

### CategoryAxis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisDisplayOptionsTypeDef]

### CategoryLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsTypeDef]

### ValueAxis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisDisplayOptionsTypeDef]

### ValueLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsTypeDef]

### ColorLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsTypeDef]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LegendOptionsTypeDef]

### DataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataLabelOptionsTypeDef]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TooltipOptionsTypeDef]

### ReferenceLines
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ReferenceLineTypeDef]]

### ContributionAnalysisDefaults
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ContributionAnalysisDefaultTypeDef]]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# BarChartFieldWellsOutputTypeDef

### BarChartAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BarChartAggregatedFieldWellsOutputTypeDef]


# BarChartFieldWellsTypeDef

### BarChartAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BarChartAggregatedFieldWellsTypeDef]


# BarChartSortConfigurationOutputTypeDef

### CategorySort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### CategoryItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]

### ColorSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### ColorItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]

### SmallMultiplesSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### SmallMultiplesLimitConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]


# BarChartSortConfigurationTypeDef

### CategorySort
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### CategoryItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]

### ColorSort
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### ColorItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]

### SmallMultiplesSort
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### SmallMultiplesLimitConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]


# BarChartVisualOutputTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BarChartConfigurationOutputTypeDef]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionOutputTypeDef]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ColumnHierarchyOutputTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# BarChartVisualTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BarChartConfigurationTypeDef]

### Actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionTypeDef]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ColumnHierarchyTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchCreateTopicReviewedAnswerRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### Answers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.CreateTopicReviewedAnswerTypeDef]
- **Required**: Yes


# BatchCreateTopicReviewedAnswerResponseTypeDef

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### SucceededAnswers
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.SucceededTopicReviewedAnswerTypeDef]
- **Required**: Yes

### InvalidAnswers
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.InvalidTopicReviewedAnswerTypeDef]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchDeleteTopicReviewedAnswerRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### AnswerIds
- **Type**: typing.Optional[typing.Sequence[str]]


# BatchDeleteTopicReviewedAnswerResponseTypeDef

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### SucceededAnswers
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.SucceededTopicReviewedAnswerTypeDef]
- **Required**: Yes

### InvalidAnswers
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.InvalidTopicReviewedAnswerTypeDef]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BigQueryParametersTypeDef

### ProjectId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetRegion
- **Type**: typing.Optional[str]


# BinCountOptionsTypeDef

### Value
- **Type**: typing.Optional[int]


# BinWidthOptionsTypeDef

### Value
- **Type**: typing.Optional[float]

### BinCountLimit
- **Type**: typing.Optional[int]


# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BodySectionConfigurationOutputTypeDef

### SectionId
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.BodySectionContentOutputTypeDef'>
- **Required**: Yes

### Style
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SectionStyleTypeDef]

### PageBreakConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SectionPageBreakConfigurationTypeDef]

### RepeatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BodySectionRepeatConfigurationOutputTypeDef]


# BodySectionConfigurationTypeDef

### SectionId
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.BodySectionContentTypeDef'>
- **Required**: Yes

### Style
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SectionStyleTypeDef]

### PageBreakConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SectionPageBreakConfigurationTypeDef]

### RepeatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BodySectionRepeatConfigurationTypeDef]


# BodySectionContentOutputTypeDef

### Layout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SectionLayoutConfigurationOutputTypeDef]


# BodySectionContentTypeDef

### Layout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SectionLayoutConfigurationTypeDef]


# BodySectionDynamicCategoryDimensionConfigurationOutputTypeDef

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### SortByMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ColumnSortTypeDef]]


# BodySectionDynamicCategoryDimensionConfigurationTypeDef

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### SortByMetrics
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ColumnSortTypeDef]]


# BodySectionDynamicNumericDimensionConfigurationOutputTypeDef

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### SortByMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ColumnSortTypeDef]]


# BodySectionDynamicNumericDimensionConfigurationTypeDef

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### SortByMetrics
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ColumnSortTypeDef]]


# BodySectionRepeatConfigurationOutputTypeDef

### DimensionConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.BodySectionRepeatDimensionConfigurationOutputTypeDef]]

### PageBreakConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BodySectionRepeatPageBreakConfigurationTypeDef]

### NonRepeatingVisuals
- **Type**: typing.Optional[typing.List[str]]


# BodySectionRepeatConfigurationTypeDef

### DimensionConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.BodySectionRepeatDimensionConfigurationTypeDef]]

### PageBreakConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BodySectionRepeatPageBreakConfigurationTypeDef]

### NonRepeatingVisuals
- **Type**: typing.Optional[typing.Sequence[str]]


# BodySectionRepeatDimensionConfigurationOutputTypeDef

### DynamicCategoryDimensionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BodySectionDynamicCategoryDimensionConfigurationOutputTypeDef]

### DynamicNumericDimensionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BodySectionDynamicNumericDimensionConfigurationOutputTypeDef]


# BodySectionRepeatDimensionConfigurationTypeDef

### DynamicCategoryDimensionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BodySectionDynamicCategoryDimensionConfigurationTypeDef]

### DynamicNumericDimensionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BodySectionDynamicNumericDimensionConfigurationTypeDef]


# BodySectionRepeatPageBreakConfigurationTypeDef

### After
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SectionAfterPageBreakTypeDef]


# BookmarksConfigurationsTypeDef

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# BorderStyleTypeDef

### Show
- **Type**: typing.Optional[bool]


# BoxPlotAggregatedFieldWellsOutputTypeDef

### GroupBy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]


# BoxPlotAggregatedFieldWellsTypeDef

### GroupBy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Values
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]


# BoxPlotChartConfigurationOutputTypeDef

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BoxPlotFieldWellsOutputTypeDef]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BoxPlotSortConfigurationOutputTypeDef]

### BoxPlotOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BoxPlotOptionsTypeDef]

### CategoryAxis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisDisplayOptionsOutputTypeDef]

### CategoryLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsOutputTypeDef]

### PrimaryYAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisDisplayOptionsOutputTypeDef]

### PrimaryYAxisLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsOutputTypeDef]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LegendOptionsTypeDef]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TooltipOptionsOutputTypeDef]

### ReferenceLines
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ReferenceLineTypeDef]]

### VisualPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualPaletteOutputTypeDef]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# BoxPlotChartConfigurationTypeDef

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BoxPlotFieldWellsTypeDef]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BoxPlotSortConfigurationTypeDef]

### BoxPlotOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BoxPlotOptionsTypeDef]

### CategoryAxis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisDisplayOptionsTypeDef]

### CategoryLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsTypeDef]

### PrimaryYAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisDisplayOptionsTypeDef]

### PrimaryYAxisLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsTypeDef]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LegendOptionsTypeDef]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TooltipOptionsTypeDef]

### ReferenceLines
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ReferenceLineTypeDef]]

### VisualPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualPaletteTypeDef]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# BoxPlotFieldWellsOutputTypeDef

### BoxPlotAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BoxPlotAggregatedFieldWellsOutputTypeDef]


# BoxPlotFieldWellsTypeDef

### BoxPlotAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BoxPlotAggregatedFieldWellsTypeDef]


# BoxPlotOptionsTypeDef

### StyleOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BoxPlotStyleOptionsTypeDef]

### OutlierVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### AllDataPointsVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# BoxPlotSortConfigurationOutputTypeDef

### CategorySort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### PaginationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaginationConfigurationTypeDef]


# BoxPlotSortConfigurationTypeDef

### CategorySort
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### PaginationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaginationConfigurationTypeDef]


# BoxPlotStyleOptionsTypeDef

### FillStyle
- **Type**: typing.Optional[typing.Literal['SOLID', 'TRANSPARENT']]


# BoxPlotVisualOutputTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BoxPlotChartConfigurationOutputTypeDef]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionOutputTypeDef]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ColumnHierarchyOutputTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# BoxPlotVisualTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BoxPlotChartConfigurationTypeDef]

### Actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionTypeDef]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ColumnHierarchyTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# BrandColorPaletteTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BrandDefinitionTypeDef

### BrandName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ApplicationTheme
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ApplicationThemeTypeDef]

### LogoConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LogoConfigurationTypeDef]


# BrandDetailTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LogoTypeDef]


# BrandElementStyleTypeDef

### NavbarStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NavbarStyleTypeDef]


# BrandSummaryTypeDef

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


# CalculatedColumnTypeDef

### ColumnName
- **Type**: <class 'str'>
- **Required**: Yes

### ColumnId
- **Type**: <class 'str'>
- **Required**: Yes

### Expression
- **Type**: <class 'str'>
- **Required**: Yes


# CalculatedFieldTypeDef

### DataSetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Expression
- **Type**: <class 'str'>
- **Required**: Yes


# CalculatedMeasureFieldTypeDef

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### Expression
- **Type**: <class 'str'>
- **Required**: Yes


# CancelIngestionRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### IngestionId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelIngestionResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CapabilitiesTypeDef

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


# CascadingControlConfigurationOutputTypeDef

### SourceControls
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.CascadingControlSourceTypeDef]]


# CascadingControlConfigurationTypeDef

### SourceControls
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.CascadingControlSourceTypeDef]]


# CascadingControlSourceTypeDef

### SourceSheetControlId
- **Type**: typing.Optional[str]

### ColumnToMatch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef]


# CastColumnTypeOperationTypeDef

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


# CategoricalDimensionFieldTypeDef

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes

### HierarchyId
- **Type**: typing.Optional[str]

### FormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.StringFormatConfigurationTypeDef]


# CategoricalMeasureFieldTypeDef

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes

### AggregationFunction
- **Type**: typing.Optional[typing.Literal['COUNT', 'DISTINCT_COUNT']]

### FormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.StringFormatConfigurationTypeDef]


# CategoryDrillDownFilterOutputTypeDef

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes

### CategoryValues
- **Type**: typing.List[str]
- **Required**: Yes


# CategoryDrillDownFilterTypeDef

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes

### CategoryValues
- **Type**: typing.Sequence[str]
- **Required**: Yes


# CategoryFilterConfigurationOutputTypeDef

### FilterListConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FilterListConfigurationOutputTypeDef]

### CustomFilterListConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CustomFilterListConfigurationOutputTypeDef]

### CustomFilterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CustomFilterConfigurationTypeDef]


# CategoryFilterConfigurationTypeDef

### FilterListConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FilterListConfigurationTypeDef]

### CustomFilterListConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CustomFilterListConfigurationTypeDef]

### CustomFilterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CustomFilterConfigurationTypeDef]


# CategoryFilterOutputTypeDef

### FilterId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.CategoryFilterConfigurationOutputTypeDef'>
- **Required**: Yes

### DefaultFilterControlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultFilterControlConfigurationOutputTypeDef]


# CategoryFilterTypeDef

### FilterId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.CategoryFilterConfigurationTypeDef'>
- **Required**: Yes

### DefaultFilterControlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultFilterControlConfigurationTypeDef]


# CategoryInnerFilterOutputTypeDef

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.CategoryFilterConfigurationOutputTypeDef'>
- **Required**: Yes

### DefaultFilterControlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultFilterControlConfigurationOutputTypeDef]


# CategoryInnerFilterTypeDef

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.CategoryFilterConfigurationTypeDef'>
- **Required**: Yes

### DefaultFilterControlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultFilterControlConfigurationTypeDef]


# CellValueSynonymOutputTypeDef

### CellValue
- **Type**: typing.Optional[str]

### Synonyms
- **Type**: typing.Optional[typing.List[str]]


# CellValueSynonymTypeDef

### CellValue
- **Type**: typing.Optional[str]

### Synonyms
- **Type**: typing.Optional[typing.Sequence[str]]


# ChartAxisLabelOptionsOutputTypeDef

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### SortIconVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### AxisLabelOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AxisLabelOptionsTypeDef]]


# ChartAxisLabelOptionsTypeDef

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### SortIconVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### AxisLabelOptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.AxisLabelOptionsTypeDef]]


# ClusterMarkerConfigurationTypeDef

### ClusterMarker
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ClusterMarkerTypeDef]


# ClusterMarkerTypeDef

### SimpleClusterMarker
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SimpleClusterMarkerTypeDef]


# CollectiveConstantEntryTypeDef

### ConstantType
- **Type**: typing.Optional[typing.Literal['COLLECTIVE', 'RANGE', 'SINGULAR']]

### Value
- **Type**: typing.Optional[str]


# CollectiveConstantOutputTypeDef

### ValueList
- **Type**: typing.Optional[typing.List[str]]


# CollectiveConstantTypeDef

### ValueList
- **Type**: typing.Optional[typing.Sequence[str]]


# ColorScaleOutputTypeDef

### Colors
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DataColorTypeDef]
- **Required**: Yes

### ColorFillType
- **Type**: typing.Literal['DISCRETE', 'GRADIENT']
- **Required**: Yes

### NullValueColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataColorTypeDef]


# ColorScaleTypeDef

### Colors
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DataColorTypeDef]
- **Required**: Yes

### ColorFillType
- **Type**: typing.Literal['DISCRETE', 'GRADIENT']
- **Required**: Yes

### NullValueColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataColorTypeDef]


# ColorsConfigurationOutputTypeDef

### CustomColors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.CustomColorTypeDef]]


# ColorsConfigurationTypeDef

### CustomColors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.CustomColorTypeDef]]


# ColumnConfigurationOutputTypeDef

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes

### FormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FormatConfigurationTypeDef]

### Role
- **Type**: typing.Optional[typing.Literal['DIMENSION', 'MEASURE']]

### ColorsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ColorsConfigurationOutputTypeDef]


# ColumnConfigurationTypeDef

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes

### FormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FormatConfigurationTypeDef]

### Role
- **Type**: typing.Optional[typing.Literal['DIMENSION', 'MEASURE']]

### ColorsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ColorsConfigurationTypeDef]


# ColumnDescriptionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ColumnGroupColumnSchemaTypeDef

### Name
- **Type**: typing.Optional[str]


# ColumnGroupOutputTypeDef

### GeoSpatialColumnGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeoSpatialColumnGroupOutputTypeDef]


# ColumnGroupSchemaOutputTypeDef

### Name
- **Type**: typing.Optional[str]

### ColumnGroupColumnSchemaList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ColumnGroupColumnSchemaTypeDef]]


# ColumnGroupSchemaTypeDef

### Name
- **Type**: typing.Optional[str]

### ColumnGroupColumnSchemaList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ColumnGroupColumnSchemaTypeDef]]


# ColumnGroupTypeDef

### GeoSpatialColumnGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeoSpatialColumnGroupUnionTypeDef]


# ColumnGroupUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ColumnHierarchyOutputTypeDef

### ExplicitHierarchy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ExplicitHierarchyOutputTypeDef]

### DateTimeHierarchy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DateTimeHierarchyOutputTypeDef]

### PredefinedHierarchy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PredefinedHierarchyOutputTypeDef]


# ColumnHierarchyTypeDef

### ExplicitHierarchy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ExplicitHierarchyTypeDef]

### DateTimeHierarchy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DateTimeHierarchyTypeDef]

### PredefinedHierarchy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PredefinedHierarchyTypeDef]


# ColumnIdentifierTypeDef

### DataSetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ColumnName
- **Type**: <class 'str'>
- **Required**: Yes


# ColumnLevelPermissionRuleOutputTypeDef

### Principals
- **Type**: typing.Optional[typing.List[str]]

### ColumnNames
- **Type**: typing.Optional[typing.List[str]]


# ColumnLevelPermissionRuleTypeDef

### Principals
- **Type**: typing.Optional[typing.Sequence[str]]

### ColumnNames
- **Type**: typing.Optional[typing.Sequence[str]]


# ColumnLevelPermissionRuleUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ColumnSchemaTypeDef

### Name
- **Type**: typing.Optional[str]

### DataType
- **Type**: typing.Optional[str]

### GeographicRole
- **Type**: typing.Optional[str]


# ColumnSortTypeDef

### SortBy
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes

### Direction
- **Type**: typing.Literal['ASC', 'DESC']
- **Required**: Yes

### AggregationFunction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AggregationFunctionTypeDef]


# ColumnTagTypeDef

### ColumnGeographicRole
- **Type**: typing.Optional[typing.Literal['CITY', 'COUNTRY', 'COUNTY', 'LATITUDE', 'LONGITUDE', 'POSTCODE', 'STATE']]

### ColumnDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ColumnDescriptionTypeDef]


# ColumnTooltipItemTypeDef

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes

### Label
- **Type**: typing.Optional[str]

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### Aggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AggregationFunctionTypeDef]

### TooltipTarget
- **Type**: typing.Optional[typing.Literal['BAR', 'BOTH', 'LINE']]


# ComboChartAggregatedFieldWellsOutputTypeDef

### Category
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### BarValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]

### Colors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### LineValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]


# ComboChartAggregatedFieldWellsTypeDef

### Category
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### BarValues
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]

### Colors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### LineValues
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]


# ComboChartConfigurationOutputTypeDef

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ComboChartFieldWellsOutputTypeDef]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ComboChartSortConfigurationOutputTypeDef]

### BarsArrangement
- **Type**: typing.Optional[typing.Literal['CLUSTERED', 'STACKED', 'STACKED_PERCENT']]

### CategoryAxis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisDisplayOptionsOutputTypeDef]

### CategoryLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsOutputTypeDef]

### PrimaryYAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisDisplayOptionsOutputTypeDef]

### PrimaryYAxisLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsOutputTypeDef]

### SecondaryYAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisDisplayOptionsOutputTypeDef]

### SecondaryYAxisLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsOutputTypeDef]

### SingleAxisOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SingleAxisOptionsTypeDef]

### ColorLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsOutputTypeDef]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LegendOptionsTypeDef]

### BarDataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataLabelOptionsOutputTypeDef]

### LineDataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataLabelOptionsOutputTypeDef]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TooltipOptionsOutputTypeDef]

### ReferenceLines
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ReferenceLineTypeDef]]

### VisualPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualPaletteOutputTypeDef]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# ComboChartConfigurationTypeDef

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ComboChartFieldWellsTypeDef]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ComboChartSortConfigurationTypeDef]

### BarsArrangement
- **Type**: typing.Optional[typing.Literal['CLUSTERED', 'STACKED', 'STACKED_PERCENT']]

### CategoryAxis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisDisplayOptionsTypeDef]

### CategoryLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsTypeDef]

### PrimaryYAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisDisplayOptionsTypeDef]

### PrimaryYAxisLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsTypeDef]

### SecondaryYAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisDisplayOptionsTypeDef]

### SecondaryYAxisLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsTypeDef]

### SingleAxisOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SingleAxisOptionsTypeDef]

### ColorLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsTypeDef]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LegendOptionsTypeDef]

### BarDataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataLabelOptionsTypeDef]

### LineDataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataLabelOptionsTypeDef]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TooltipOptionsTypeDef]

### ReferenceLines
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ReferenceLineTypeDef]]

### VisualPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualPaletteTypeDef]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# ComboChartFieldWellsOutputTypeDef

### ComboChartAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ComboChartAggregatedFieldWellsOutputTypeDef]


# ComboChartFieldWellsTypeDef

### ComboChartAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ComboChartAggregatedFieldWellsTypeDef]


# ComboChartSortConfigurationOutputTypeDef

### CategorySort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### CategoryItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]

### ColorSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### ColorItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]


# ComboChartSortConfigurationTypeDef

### CategorySort
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### CategoryItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]

### ColorSort
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### ColorItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]


# ComboChartVisualOutputTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ComboChartConfigurationOutputTypeDef]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionOutputTypeDef]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ColumnHierarchyOutputTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# ComboChartVisualTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ComboChartConfigurationTypeDef]

### Actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionTypeDef]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ColumnHierarchyTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# ComparativeOrderOutputTypeDef

### UseOrdering
- **Type**: typing.Optional[typing.Literal['GREATER_IS_BETTER', 'LESSER_IS_BETTER', 'SPECIFIED']]

### SpecifedOrder
- **Type**: typing.Optional[typing.List[str]]

### TreatUndefinedSpecifiedValues
- **Type**: typing.Optional[typing.Literal['LEAST', 'MOST']]


# ComparativeOrderTypeDef

### UseOrdering
- **Type**: typing.Optional[typing.Literal['GREATER_IS_BETTER', 'LESSER_IS_BETTER', 'SPECIFIED']]

### SpecifedOrder
- **Type**: typing.Optional[typing.Sequence[str]]

### TreatUndefinedSpecifiedValues
- **Type**: typing.Optional[typing.Literal['LEAST', 'MOST']]


# ComparisonConfigurationTypeDef

### ComparisonMethod
- **Type**: typing.Optional[typing.Literal['DIFFERENCE', 'PERCENT', 'PERCENT_DIFFERENCE']]

### ComparisonFormat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ComparisonFormatConfigurationTypeDef]


# ComparisonFormatConfigurationTypeDef

### NumberDisplayFormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NumberDisplayFormatConfigurationTypeDef]

### PercentageDisplayFormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PercentageDisplayFormatConfigurationTypeDef]


# ComputationTypeDef

### TopBottomRanked
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopBottomRankedComputationTypeDef]

### TopBottomMovers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopBottomMoversComputationTypeDef]

### TotalAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TotalAggregationComputationTypeDef]

### MaximumMinimum
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.MaximumMinimumComputationTypeDef]

### MetricComparison
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.MetricComparisonComputationTypeDef]

### PeriodOverPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PeriodOverPeriodComputationTypeDef]

### PeriodToDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PeriodToDateComputationTypeDef]

### GrowthRate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GrowthRateComputationTypeDef]

### UniqueValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.UniqueValuesComputationTypeDef]

### Forecast
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ForecastComputationTypeDef]


# ConditionalFormattingColorOutputTypeDef

### Solid
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingSolidColorTypeDef]

### Gradient
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingGradientColorOutputTypeDef]


# ConditionalFormattingColorTypeDef

### Solid
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingSolidColorTypeDef]

### Gradient
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingGradientColorTypeDef]


# ConditionalFormattingCustomIconConditionTypeDef

### Expression
- **Type**: <class 'str'>
- **Required**: Yes

### IconOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingCustomIconOptionsTypeDef'>
- **Required**: Yes

### Color
- **Type**: typing.Optional[str]

### DisplayConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingIconDisplayConfigurationTypeDef]


# ConditionalFormattingCustomIconOptionsTypeDef

### Icon
- **Type**: typing.Optional[typing.Literal['ARROW_DOWN', 'ARROW_DOWN_LEFT', 'ARROW_DOWN_RIGHT', 'ARROW_LEFT', 'ARROW_RIGHT', 'ARROW_UP', 'ARROW_UP_LEFT', 'ARROW_UP_RIGHT', 'CARET_DOWN', 'CARET_UP', 'CHECKMARK', 'CIRCLE', 'FACE_DOWN', 'FACE_FLAT', 'FACE_UP', 'FLAG', 'MINUS', 'ONE_BAR', 'PLUS', 'SQUARE', 'THREE_BAR', 'THUMBS_DOWN', 'THUMBS_UP', 'TRIANGLE', 'TWO_BAR', 'X']]

### UnicodeIcon
- **Type**: typing.Optional[str]


# ConditionalFormattingGradientColorOutputTypeDef

### Expression
- **Type**: <class 'str'>
- **Required**: Yes

### Color
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.GradientColorOutputTypeDef'>
- **Required**: Yes


# ConditionalFormattingGradientColorTypeDef

### Expression
- **Type**: <class 'str'>
- **Required**: Yes

### Color
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.GradientColorTypeDef'>
- **Required**: Yes


# ConditionalFormattingIconDisplayConfigurationTypeDef

### IconDisplayOption
- **Type**: typing.Optional[typing.Literal['ICON_ONLY']]


# ConditionalFormattingIconSetTypeDef

### Expression
- **Type**: <class 'str'>
- **Required**: Yes

### IconSetType
- **Type**: typing.Optional[typing.Literal['BARS', 'CARET_UP_MINUS_DOWN', 'CHECK_X', 'FLAGS', 'FOUR_COLOR_ARROW', 'FOUR_GRAY_ARROW', 'PLUS_MINUS', 'THREE_CIRCLE', 'THREE_COLOR_ARROW', 'THREE_GRAY_ARROW', 'THREE_SHAPE']]


# ConditionalFormattingIconTypeDef

### IconSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingIconSetTypeDef]

### CustomCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingCustomIconConditionTypeDef]


# ConditionalFormattingSolidColorTypeDef

### Expression
- **Type**: <class 'str'>
- **Required**: Yes

### Color
- **Type**: typing.Optional[str]


# ContextMenuOptionTypeDef

### AvailabilityStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# ContributionAnalysisDefaultOutputTypeDef

### MeasureFieldId
- **Type**: <class 'str'>
- **Required**: Yes

### ContributorDimensions
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef]
- **Required**: Yes


# ContributionAnalysisDefaultTypeDef

### MeasureFieldId
- **Type**: <class 'str'>
- **Required**: Yes

### ContributorDimensions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef]
- **Required**: Yes


# ContributionAnalysisFactorTypeDef

### FieldName
- **Type**: typing.Optional[str]


# ContributionAnalysisTimeRangesOutputTypeDef

### StartRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicIRFilterOptionOutputTypeDef]

### EndRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicIRFilterOptionOutputTypeDef]


# ContributionAnalysisTimeRangesTypeDef

### StartRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicIRFilterOptionUnionTypeDef]

### EndRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicIRFilterOptionUnionTypeDef]


# ContributionAnalysisTimeRangesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAccountCustomizationRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountCustomization
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.AccountCustomizationTypeDef'>
- **Required**: Yes

### Namespace
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TagTypeDef]]


# CreateAccountCustomizationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.AccountCustomizationTypeDef'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAccountSubscriptionRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[str]]

### AuthorGroup
- **Type**: typing.Optional[typing.Sequence[str]]

### ReaderGroup
- **Type**: typing.Optional[typing.Sequence[str]]

### AdminProGroup
- **Type**: typing.Optional[typing.Sequence[str]]

### AuthorProGroup
- **Type**: typing.Optional[typing.Sequence[str]]

### ReaderProGroup
- **Type**: typing.Optional[typing.Sequence[str]]

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


# CreateAccountSubscriptionResponseTypeDef

### SignupResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.SignupResponseTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAnalysisRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ParametersUnionTypeDef]

### Permissions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionUnionTypeDef]]

### SourceEntity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AnalysisSourceEntityTypeDef]

### ThemeArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TagTypeDef]]

### Definition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AnalysisDefinitionUnionTypeDef]

### ValidationStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ValidationStrategyTypeDef]

### FolderArns
- **Type**: typing.Optional[typing.Sequence[str]]


# CreateAnalysisResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateBrandRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BrandId
- **Type**: <class 'str'>
- **Required**: Yes

### BrandDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BrandDefinitionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TagTypeDef]]


# CreateBrandResponseTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### BrandDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.BrandDetailTypeDef'>
- **Required**: Yes

### BrandDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.BrandDefinitionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateColumnsOperationOutputTypeDef

### Columns
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.CalculatedColumnTypeDef]
- **Required**: Yes


# CreateColumnsOperationTypeDef

### Columns
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.CalculatedColumnTypeDef]
- **Required**: Yes


# CreateColumnsOperationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateCustomPermissionsRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### CustomPermissionsName
- **Type**: <class 'str'>
- **Required**: Yes

### Capabilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CapabilitiesTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TagTypeDef]]


# CreateCustomPermissionsResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDashboardRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ParametersUnionTypeDef]

### Permissions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionUnionTypeDef]]

### SourceEntity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DashboardSourceEntityTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TagTypeDef]]

### VersionDescription
- **Type**: typing.Optional[str]

### DashboardPublishOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DashboardPublishOptionsTypeDef]

### ThemeArn
- **Type**: typing.Optional[str]

### Definition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DashboardVersionDefinitionUnionTypeDef]

### ValidationStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ValidationStrategyTypeDef]

### FolderArns
- **Type**: typing.Optional[typing.Sequence[str]]

### LinkSharingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LinkSharingConfigurationUnionTypeDef]

### LinkEntities
- **Type**: typing.Optional[typing.Sequence[str]]


# CreateDashboardResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDataSetRequestTypeDef

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
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.quicksight_classes.PhysicalTableUnionTypeDef]
- **Required**: Yes

### ImportMode
- **Type**: typing.Literal['DIRECT_QUERY', 'SPICE']
- **Required**: Yes

### LogicalTableMap
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.quicksight_classes.LogicalTableUnionTypeDef]]

### ColumnGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ColumnGroupUnionTypeDef]]

### FieldFolders
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.quicksight_classes.FieldFolderUnionTypeDef]]

### Permissions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionUnionTypeDef]]

### RowLevelPermissionDataSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RowLevelPermissionDataSetTypeDef]

### RowLevelPermissionTagConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RowLevelPermissionTagConfigurationUnionTypeDef]

### ColumnLevelPermissionRules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ColumnLevelPermissionRuleUnionTypeDef]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TagTypeDef]]

### DataSetUsageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataSetUsageConfigurationTypeDef]

### DatasetParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DatasetParameterUnionTypeDef]]

### FolderArns
- **Type**: typing.Optional[typing.Sequence[str]]

### PerformanceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PerformanceConfigurationUnionTypeDef]


# CreateDataSetResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDataSourceResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFolderMembershipRequestTypeDef

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


# CreateFolderMembershipResponseTypeDef

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### FolderMember
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.FolderMemberTypeDef'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFolderRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionUnionTypeDef]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TagTypeDef]]

### SharingModel
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'NAMESPACE']]


# CreateFolderResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateGroupMembershipRequestTypeDef

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


# CreateGroupMembershipResponseTypeDef

### GroupMember
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.GroupMemberTypeDef'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateGroupRequestTypeDef

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


# CreateGroupResponseTypeDef

### Group
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.GroupTypeDef'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateIAMPolicyAssignmentRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]


# CreateIAMPolicyAssignmentResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateIngestionRequestTypeDef

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


# CreateIngestionResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateNamespaceRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TagTypeDef]]


# CreateNamespaceResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRefreshScheduleRequestTypeDef

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Schedule
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.RefreshScheduleUnionTypeDef'>
- **Required**: Yes


# CreateRefreshScheduleResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRoleMembershipRequestTypeDef

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


# CreateRoleMembershipResponseTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTemplateAliasRequestTypeDef

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


# CreateTemplateAliasResponseTypeDef

### TemplateAlias
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.TemplateAliasTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTemplateRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Permissions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionUnionTypeDef]]

### SourceEntity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TemplateSourceEntityTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TagTypeDef]]

### VersionDescription
- **Type**: typing.Optional[str]

### Definition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TemplateVersionDefinitionUnionTypeDef]

### ValidationStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ValidationStrategyTypeDef]


# CreateTemplateResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateThemeAliasRequestTypeDef

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


# CreateThemeAliasResponseTypeDef

### ThemeAlias
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ThemeAliasTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateThemeRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ThemeConfigurationUnionTypeDef'>
- **Required**: Yes

### VersionDescription
- **Type**: typing.Optional[str]

### Permissions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionUnionTypeDef]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TagTypeDef]]


# CreateThemeResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTopicRefreshScheduleRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.TopicRefreshScheduleUnionTypeDef'>
- **Required**: Yes

### DatasetName
- **Type**: typing.Optional[str]


# CreateTopicRefreshScheduleResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTopicRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### Topic
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.TopicDetailsUnionTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TagTypeDef]]

### FolderArns
- **Type**: typing.Optional[typing.Sequence[str]]


# CreateTopicResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTopicReviewedAnswerTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicIRUnionTypeDef]

### PrimaryVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicVisualUnionTypeDef]

### Template
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicTemplateUnionTypeDef]


# CreateVPCConnectionRequestTypeDef

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
- **Type**: typing.Sequence[str]
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### DnsResolvers
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TagTypeDef]]


# CreateVPCConnectionResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CredentialPairTypeDef

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: <class 'str'>
- **Required**: Yes

### AlternateDataSourceParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DataSourceParametersUnionTypeDef]]


# CurrencyDisplayFormatConfigurationTypeDef

### Prefix
- **Type**: typing.Optional[str]

### Suffix
- **Type**: typing.Optional[str]

### SeparatorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NumericSeparatorConfigurationTypeDef]

### Symbol
- **Type**: typing.Optional[str]

### DecimalPlacesConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DecimalPlacesConfigurationTypeDef]

### NumberScale
- **Type**: typing.Optional[typing.Literal['AUTO', 'BILLIONS', 'CRORES', 'LAKHS', 'MILLIONS', 'NONE', 'THOUSANDS', 'TRILLIONS']]

### NegativeValueConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NegativeValueConfigurationTypeDef]

### NullValueFormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NullValueFormatConfigurationTypeDef]


# CustomActionFilterOperationOutputTypeDef

### SelectedFieldsConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.FilterOperationSelectedFieldsConfigurationOutputTypeDef'>
- **Required**: Yes

### TargetVisualsConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.FilterOperationTargetVisualsConfigurationOutputTypeDef'>
- **Required**: Yes


# CustomActionFilterOperationTypeDef

### SelectedFieldsConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.FilterOperationSelectedFieldsConfigurationTypeDef'>
- **Required**: Yes

### TargetVisualsConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.FilterOperationTargetVisualsConfigurationTypeDef'>
- **Required**: Yes


# CustomActionNavigationOperationTypeDef

### LocalNavigationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LocalNavigationConfigurationTypeDef]


# CustomActionSetParametersOperationOutputTypeDef

### ParameterValueConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.SetParameterValueConfigurationOutputTypeDef]
- **Required**: Yes


# CustomActionSetParametersOperationTypeDef

### ParameterValueConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.SetParameterValueConfigurationTypeDef]
- **Required**: Yes


# CustomActionURLOperationTypeDef

### URLTemplate
- **Type**: <class 'str'>
- **Required**: Yes

### URLTarget
- **Type**: typing.Literal['NEW_TAB', 'NEW_WINDOW', 'SAME_TAB']
- **Required**: Yes


# CustomColorTypeDef

### Color
- **Type**: <class 'str'>
- **Required**: Yes

### FieldValue
- **Type**: typing.Optional[str]

### SpecialValue
- **Type**: typing.Optional[typing.Literal['EMPTY', 'NULL', 'OTHER']]


# CustomContentConfigurationTypeDef

### ContentUrl
- **Type**: typing.Optional[str]

### ContentType
- **Type**: typing.Optional[typing.Literal['IMAGE', 'OTHER_EMBEDDED_CONTENT']]

### ImageScaling
- **Type**: typing.Optional[typing.Literal['DO_NOT_SCALE', 'FIT_TO_HEIGHT', 'FIT_TO_WIDTH', 'SCALE_TO_VISUAL']]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# CustomContentVisualOutputTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CustomContentConfigurationTypeDef]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionOutputTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# CustomContentVisualTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CustomContentConfigurationTypeDef]

### Actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# CustomFilterConfigurationTypeDef

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


# CustomFilterListConfigurationOutputTypeDef

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


# CustomFilterListConfigurationTypeDef

### MatchOperator
- **Type**: typing.Literal['CONTAINS', 'DOES_NOT_CONTAIN', 'DOES_NOT_EQUAL', 'ENDS_WITH', 'EQUALS', 'STARTS_WITH']
- **Required**: Yes

### NullOption
- **Type**: typing.Literal['ALL_VALUES', 'NON_NULLS_ONLY', 'NULLS_ONLY']
- **Required**: Yes

### CategoryValues
- **Type**: typing.Optional[typing.Sequence[str]]

### SelectAllOptions
- **Type**: typing.Optional[typing.Literal['FILTER_ALL_VALUES']]


# CustomNarrativeOptionsTypeDef

### Narrative
- **Type**: <class 'str'>
- **Required**: Yes


# CustomParameterValuesOutputTypeDef

### StringValues
- **Type**: typing.Optional[typing.List[str]]

### IntegerValues
- **Type**: typing.Optional[typing.List[int]]

### DecimalValues
- **Type**: typing.Optional[typing.List[float]]

### DateTimeValues
- **Type**: typing.Optional[typing.List[datetime.datetime]]


# CustomParameterValuesTypeDef

### StringValues
- **Type**: typing.Optional[typing.Sequence[str]]

### IntegerValues
- **Type**: typing.Optional[typing.Sequence[int]]

### DecimalValues
- **Type**: typing.Optional[typing.Sequence[float]]

### DateTimeValues
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TimestampTypeDef]]


# CustomPermissionsTypeDef

### Arn
- **Type**: typing.Optional[str]

### CustomPermissionsName
- **Type**: typing.Optional[str]

### Capabilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CapabilitiesTypeDef]


# CustomSqlOutputTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.InputColumnTypeDef]]


# CustomSqlTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.InputColumnTypeDef]]


# CustomSqlUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CustomValuesConfigurationOutputTypeDef

### CustomValues
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.CustomParameterValuesOutputTypeDef'>
- **Required**: Yes

### IncludeNullValue
- **Type**: typing.Optional[bool]


# CustomValuesConfigurationTypeDef

### CustomValues
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.CustomParameterValuesTypeDef'>
- **Required**: Yes

### IncludeNullValue
- **Type**: typing.Optional[bool]


# DashboardErrorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DashboardPublishOptionsTypeDef

### AdHocFilteringOption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AdHocFilteringOptionTypeDef]

### ExportToCSVOption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ExportToCSVOptionTypeDef]

### SheetControlsOption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SheetControlsOptionTypeDef]

### VisualPublishOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DashboardVisualPublishOptionsTypeDef]

### SheetLayoutElementMaximizationOption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SheetLayoutElementMaximizationOptionTypeDef]

### VisualMenuOption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualMenuOptionTypeDef]

### VisualAxisSortOption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualAxisSortOptionTypeDef]

### ExportWithHiddenFieldsOption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ExportWithHiddenFieldsOptionTypeDef]

### DataPointDrillUpDownOption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataPointDrillUpDownOptionTypeDef]

### DataPointMenuLabelOption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataPointMenuLabelOptionTypeDef]

### DataPointTooltipOption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataPointTooltipOptionTypeDef]


# DashboardSearchFilterTypeDef

### Operator
- **Type**: typing.Literal['StringEquals', 'StringLike']
- **Required**: Yes

### Name
- **Type**: typing.Optional[typing.Literal['DASHBOARD_NAME', 'DIRECT_QUICKSIGHT_OWNER', 'DIRECT_QUICKSIGHT_SOLE_OWNER', 'DIRECT_QUICKSIGHT_VIEWER_OR_OWNER', 'QUICKSIGHT_OWNER', 'QUICKSIGHT_USER', 'QUICKSIGHT_VIEWER_OR_OWNER']]

### Value
- **Type**: typing.Optional[str]


# DashboardSourceEntityTypeDef

### SourceTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DashboardSourceTemplateTypeDef]


# DashboardSourceTemplateTypeDef

### DataSetReferences
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DataSetReferenceTypeDef]
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# DashboardSummaryTypeDef

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


# DashboardTypeDef

### DashboardId
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DashboardVersionTypeDef]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastPublishedTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### LinkEntities
- **Type**: typing.Optional[typing.List[str]]


# DashboardVersionDefinitionOutputTypeDef

### DataSetIdentifierDeclarations
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DataSetIdentifierDeclarationTypeDef]
- **Required**: Yes

### Sheets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.SheetDefinitionOutputTypeDef]]

### CalculatedFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.CalculatedFieldTypeDef]]

### ParameterDeclarations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ParameterDeclarationOutputTypeDef]]

### FilterGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.FilterGroupOutputTypeDef]]

### ColumnConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ColumnConfigurationOutputTypeDef]]

### AnalysisDefaults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AnalysisDefaultsTypeDef]

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AssetOptionsTypeDef]

### StaticFiles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.StaticFileTypeDef]]


# DashboardVersionDefinitionTypeDef

### DataSetIdentifierDeclarations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DataSetIdentifierDeclarationTypeDef]
- **Required**: Yes

### Sheets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.SheetDefinitionTypeDef]]

### CalculatedFields
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.CalculatedFieldTypeDef]]

### ParameterDeclarations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ParameterDeclarationTypeDef]]

### FilterGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.FilterGroupTypeDef]]

### ColumnConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ColumnConfigurationTypeDef]]

### AnalysisDefaults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AnalysisDefaultsTypeDef]

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AssetOptionsTypeDef]

### StaticFiles
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.StaticFileTypeDef]]


# DashboardVersionDefinitionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DashboardVersionSummaryTypeDef

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


# DashboardVersionTypeDef

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### Errors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DashboardErrorTypeDef]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.SheetTypeDef]]


# DashboardVisualIdTypeDef

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### SheetId
- **Type**: <class 'str'>
- **Required**: Yes

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes


# DashboardVisualPublishOptionsTypeDef

### ExportHiddenFieldsOption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ExportHiddenFieldsOptionTypeDef]


# DashboardVisualResultTypeDef

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


# DataAggregationTypeDef

### DatasetRowDateGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### DefaultDateColumnName
- **Type**: typing.Optional[str]


# DataBarsOptionsTypeDef

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### PositiveColor
- **Type**: typing.Optional[str]

### NegativeColor
- **Type**: typing.Optional[str]


# DataColorPaletteOutputTypeDef

### Colors
- **Type**: typing.Optional[typing.List[str]]

### MinMaxGradient
- **Type**: typing.Optional[typing.List[str]]

### EmptyFillColor
- **Type**: typing.Optional[str]


# DataColorPaletteTypeDef

### Colors
- **Type**: typing.Optional[typing.Sequence[str]]

### MinMaxGradient
- **Type**: typing.Optional[typing.Sequence[str]]

### EmptyFillColor
- **Type**: typing.Optional[str]


# DataColorTypeDef

### Color
- **Type**: typing.Optional[str]

### DataValue
- **Type**: typing.Optional[float]


# DataFieldSeriesItemTypeDef

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### AxisBinding
- **Type**: typing.Literal['PRIMARY_YAXIS', 'SECONDARY_YAXIS']
- **Required**: Yes

### FieldValue
- **Type**: typing.Optional[str]

### Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LineChartSeriesSettingsTypeDef]


# DataLabelOptionsOutputTypeDef

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### CategoryLabelVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### MeasureLabelVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### DataLabelTypes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DataLabelTypeTypeDef]]

### Position
- **Type**: typing.Optional[typing.Literal['BOTTOM', 'INSIDE', 'LEFT', 'OUTSIDE', 'RIGHT', 'TOP']]

### LabelContent
- **Type**: typing.Optional[typing.Literal['PERCENT', 'VALUE', 'VALUE_AND_PERCENT']]

### LabelFontConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FontConfigurationTypeDef]

### LabelColor
- **Type**: typing.Optional[str]

### Overlap
- **Type**: typing.Optional[typing.Literal['DISABLE_OVERLAP', 'ENABLE_OVERLAP']]

### TotalsVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# DataLabelOptionsTypeDef

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### CategoryLabelVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### MeasureLabelVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### DataLabelTypes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DataLabelTypeTypeDef]]

### Position
- **Type**: typing.Optional[typing.Literal['BOTTOM', 'INSIDE', 'LEFT', 'OUTSIDE', 'RIGHT', 'TOP']]

### LabelContent
- **Type**: typing.Optional[typing.Literal['PERCENT', 'VALUE', 'VALUE_AND_PERCENT']]

### LabelFontConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FontConfigurationTypeDef]

### LabelColor
- **Type**: typing.Optional[str]

### Overlap
- **Type**: typing.Optional[typing.Literal['DISABLE_OVERLAP', 'ENABLE_OVERLAP']]

### TotalsVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# DataLabelTypeTypeDef

### FieldLabelType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FieldLabelTypeTypeDef]

### DataPathLabelType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataPathLabelTypeTypeDef]

### RangeEndsLabelType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RangeEndsLabelTypeTypeDef]

### MinimumLabelType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.MinimumLabelTypeTypeDef]

### MaximumLabelType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.MaximumLabelTypeTypeDef]


# DataPathColorTypeDef

### Element
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.DataPathValueTypeDef'>
- **Required**: Yes

### Color
- **Type**: <class 'str'>
- **Required**: Yes

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]


# DataPathLabelTypeTypeDef

### FieldId
- **Type**: typing.Optional[str]

### FieldValue
- **Type**: typing.Optional[str]

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# DataPathSortOutputTypeDef

### Direction
- **Type**: typing.Literal['ASC', 'DESC']
- **Required**: Yes

### SortPaths
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DataPathValueTypeDef]
- **Required**: Yes


# DataPathSortTypeDef

### Direction
- **Type**: typing.Literal['ASC', 'DESC']
- **Required**: Yes

### SortPaths
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DataPathValueTypeDef]
- **Required**: Yes


# DataPathTypeTypeDef

### PivotTableDataPathType
- **Type**: typing.Optional[typing.Literal['COUNT_METRIC_COLUMN', 'EMPTY_COLUMN_HEADER', 'HIERARCHY_ROWS_LAYOUT_COLUMN', 'MULTIPLE_ROW_METRICS_COLUMN']]


# DataPathValueTypeDef

### FieldId
- **Type**: typing.Optional[str]

### FieldValue
- **Type**: typing.Optional[str]

### DataPathType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataPathTypeTypeDef]


# DataPointDrillUpDownOptionTypeDef

### AvailabilityStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# DataPointMenuLabelOptionTypeDef

### AvailabilityStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# DataPointTooltipOptionTypeDef

### AvailabilityStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# DataSetConfigurationOutputTypeDef

### Placeholder
- **Type**: typing.Optional[str]

### DataSetSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataSetSchemaOutputTypeDef]

### ColumnGroupSchemaList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ColumnGroupSchemaOutputTypeDef]]


# DataSetConfigurationTypeDef

### Placeholder
- **Type**: typing.Optional[str]

### DataSetSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataSetSchemaTypeDef]

### ColumnGroupSchemaList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ColumnGroupSchemaTypeDef]]


# DataSetIdentifierDeclarationTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DataSetReferenceTypeDef

### DataSetPlaceholder
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DataSetRefreshPropertiesTypeDef

### RefreshConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.RefreshConfigurationTypeDef'>
- **Required**: Yes


# DataSetSchemaOutputTypeDef

### ColumnSchemaList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ColumnSchemaTypeDef]]


# DataSetSchemaTypeDef

### ColumnSchemaList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ColumnSchemaTypeDef]]


# DataSetSearchFilterTypeDef

### Operator
- **Type**: typing.Literal['StringEquals', 'StringLike']
- **Required**: Yes

### Name
- **Type**: typing.Literal['DATASET_NAME', 'DIRECT_QUICKSIGHT_OWNER', 'DIRECT_QUICKSIGHT_SOLE_OWNER', 'DIRECT_QUICKSIGHT_VIEWER_OR_OWNER', 'QUICKSIGHT_OWNER', 'QUICKSIGHT_VIEWER_OR_OWNER']
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# DataSetSummaryTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RowLevelPermissionDataSetTypeDef]

### RowLevelPermissionTagConfigurationApplied
- **Type**: typing.Optional[bool]

### ColumnLevelPermissionRulesApplied
- **Type**: typing.Optional[bool]


# DataSetTypeDef

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
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.quicksight_classes.PhysicalTableOutputTypeDef]]

### LogicalTableMap
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.quicksight_classes.LogicalTableOutputTypeDef]]

### OutputColumns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.OutputColumnTypeDef]]

### ImportMode
- **Type**: typing.Optional[typing.Literal['DIRECT_QUERY', 'SPICE']]

### ConsumedSpiceCapacityInBytes
- **Type**: typing.Optional[int]

### ColumnGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ColumnGroupOutputTypeDef]]

### FieldFolders
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.quicksight_classes.FieldFolderOutputTypeDef]]

### RowLevelPermissionDataSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RowLevelPermissionDataSetTypeDef]

### RowLevelPermissionTagConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RowLevelPermissionTagConfigurationOutputTypeDef]

### ColumnLevelPermissionRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ColumnLevelPermissionRuleOutputTypeDef]]

### DataSetUsageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataSetUsageConfigurationTypeDef]

### DatasetParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DatasetParameterOutputTypeDef]]

### PerformanceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PerformanceConfigurationOutputTypeDef]


# DataSetUsageConfigurationTypeDef

### DisableUseAsDirectQuerySource
- **Type**: typing.Optional[bool]

### DisableUseAsImportedSource
- **Type**: typing.Optional[bool]


# DataSourceCredentialsTypeDef

### CredentialPair
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CredentialPairTypeDef]

### CopySourceArn
- **Type**: typing.Optional[str]

### SecretArn
- **Type**: typing.Optional[str]


# DataSourceParametersOutputTypeDef

### AmazonElasticsearchParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AmazonElasticsearchParametersTypeDef]

### AthenaParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AthenaParametersTypeDef]

### AuroraParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AuroraParametersTypeDef]

### AuroraPostgreSqlParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AuroraPostgreSqlParametersTypeDef]

### AwsIotAnalyticsParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AwsIotAnalyticsParametersTypeDef]

### JiraParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.JiraParametersTypeDef]

### MariaDbParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.MariaDbParametersTypeDef]

### MySqlParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.MySqlParametersTypeDef]

### OracleParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.OracleParametersTypeDef]

### PostgreSqlParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PostgreSqlParametersTypeDef]

### PrestoParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PrestoParametersTypeDef]

### RdsParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RdsParametersTypeDef]

### RedshiftParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RedshiftParametersOutputTypeDef]

### S3Parameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.S3ParametersTypeDef]

### ServiceNowParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ServiceNowParametersTypeDef]

### SnowflakeParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SnowflakeParametersTypeDef]

### SparkParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SparkParametersTypeDef]

### SqlServerParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SqlServerParametersTypeDef]

### TeradataParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TeradataParametersTypeDef]

### TwitterParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TwitterParametersTypeDef]

### AmazonOpenSearchParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AmazonOpenSearchParametersTypeDef]

### ExasolParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ExasolParametersTypeDef]

### DatabricksParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DatabricksParametersTypeDef]

### StarburstParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.StarburstParametersTypeDef]

### TrinoParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TrinoParametersTypeDef]

### BigQueryParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BigQueryParametersTypeDef]


# DataSourceParametersTypeDef

### AmazonElasticsearchParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AmazonElasticsearchParametersTypeDef]

### AthenaParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AthenaParametersTypeDef]

### AuroraParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AuroraParametersTypeDef]

### AuroraPostgreSqlParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AuroraPostgreSqlParametersTypeDef]

### AwsIotAnalyticsParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AwsIotAnalyticsParametersTypeDef]

### JiraParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.JiraParametersTypeDef]

### MariaDbParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.MariaDbParametersTypeDef]

### MySqlParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.MySqlParametersTypeDef]

### OracleParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.OracleParametersTypeDef]

### PostgreSqlParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PostgreSqlParametersTypeDef]

### PrestoParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PrestoParametersTypeDef]

### RdsParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RdsParametersTypeDef]

### RedshiftParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RedshiftParametersUnionTypeDef]

### S3Parameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.S3ParametersTypeDef]

### ServiceNowParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ServiceNowParametersTypeDef]

### SnowflakeParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SnowflakeParametersTypeDef]

### SparkParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SparkParametersTypeDef]

### SqlServerParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SqlServerParametersTypeDef]

### TeradataParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TeradataParametersTypeDef]

### TwitterParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TwitterParametersTypeDef]

### AmazonOpenSearchParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AmazonOpenSearchParametersTypeDef]

### ExasolParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ExasolParametersTypeDef]

### DatabricksParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DatabricksParametersTypeDef]

### StarburstParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.StarburstParametersTypeDef]

### TrinoParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TrinoParametersTypeDef]

### BigQueryParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BigQueryParametersTypeDef]


# DataSourceParametersUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataSourceSearchFilterTypeDef

### Operator
- **Type**: typing.Literal['StringEquals', 'StringLike']
- **Required**: Yes

### Name
- **Type**: typing.Literal['DATASOURCE_NAME', 'DIRECT_QUICKSIGHT_OWNER', 'DIRECT_QUICKSIGHT_SOLE_OWNER', 'DIRECT_QUICKSIGHT_VIEWER_OR_OWNER']
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# DataSourceSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataSourceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DatabricksParametersTypeDef

### Host
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes

### SqlEndpointPath
- **Type**: <class 'str'>
- **Required**: Yes


# DatasetMetadataOutputTypeDef

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetName
- **Type**: typing.Optional[str]

### DatasetDescription
- **Type**: typing.Optional[str]

### DataAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataAggregationTypeDef]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.TopicFilterOutputTypeDef]]

### Columns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.TopicColumnOutputTypeDef]]

### CalculatedFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.TopicCalculatedFieldOutputTypeDef]]

### NamedEntities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.TopicNamedEntityOutputTypeDef]]


# DatasetMetadataTypeDef

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetName
- **Type**: typing.Optional[str]

### DatasetDescription
- **Type**: typing.Optional[str]

### DataAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataAggregationTypeDef]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TopicFilterTypeDef]]

### Columns
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TopicColumnTypeDef]]

### CalculatedFields
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TopicCalculatedFieldTypeDef]]

### NamedEntities
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TopicNamedEntityTypeDef]]


# DatasetParameterOutputTypeDef

### StringDatasetParameter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.StringDatasetParameterOutputTypeDef]

### DecimalDatasetParameter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DecimalDatasetParameterOutputTypeDef]

### IntegerDatasetParameter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.IntegerDatasetParameterOutputTypeDef]

### DateTimeDatasetParameter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DateTimeDatasetParameterOutputTypeDef]


# DatasetParameterTypeDef

### StringDatasetParameter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.StringDatasetParameterUnionTypeDef]

### DecimalDatasetParameter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DecimalDatasetParameterUnionTypeDef]

### IntegerDatasetParameter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.IntegerDatasetParameterUnionTypeDef]

### DateTimeDatasetParameter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DateTimeDatasetParameterUnionTypeDef]


# DatasetParameterUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DateAxisOptionsTypeDef

### MissingDateVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# DateDimensionFieldTypeDef

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes

### DateGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### HierarchyId
- **Type**: typing.Optional[str]

### FormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DateTimeFormatConfigurationTypeDef]


# DateMeasureFieldTypeDef

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes

### AggregationFunction
- **Type**: typing.Optional[typing.Literal['COUNT', 'DISTINCT_COUNT', 'MAX', 'MIN']]

### FormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DateTimeFormatConfigurationTypeDef]


# DateTimeDatasetParameterDefaultValuesOutputTypeDef

### StaticValues
- **Type**: typing.Optional[typing.List[datetime.datetime]]


# DateTimeDatasetParameterDefaultValuesTypeDef

### StaticValues
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TimestampTypeDef]]


# DateTimeDatasetParameterDefaultValuesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DateTimeDatasetParameterOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DateTimeDatasetParameterDefaultValuesOutputTypeDef]


# DateTimeDatasetParameterTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DateTimeDatasetParameterDefaultValuesUnionTypeDef]


# DateTimeDatasetParameterUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DateTimeDefaultValuesOutputTypeDef

### DynamicValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DynamicDefaultValueTypeDef]

### StaticValues
- **Type**: typing.Optional[typing.List[datetime.datetime]]

### RollingDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RollingDateConfigurationTypeDef]


# DateTimeDefaultValuesTypeDef

### DynamicValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DynamicDefaultValueTypeDef]

### StaticValues
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TimestampTypeDef]]

### RollingDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RollingDateConfigurationTypeDef]


# DateTimeFormatConfigurationTypeDef

### DateTimeFormat
- **Type**: typing.Optional[str]

### NullValueFormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NullValueFormatConfigurationTypeDef]

### NumericFormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NumericFormatConfigurationTypeDef]


# DateTimeHierarchyOutputTypeDef

### HierarchyId
- **Type**: <class 'str'>
- **Required**: Yes

### DrillDownFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DrillDownFilterOutputTypeDef]]


# DateTimeHierarchyTypeDef

### HierarchyId
- **Type**: <class 'str'>
- **Required**: Yes

### DrillDownFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DrillDownFilterTypeDef]]


# DateTimeParameterDeclarationOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DateTimeDefaultValuesOutputTypeDef]

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### ValueWhenUnset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DateTimeValueWhenUnsetConfigurationOutputTypeDef]

### MappedDataSetParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.MappedDataSetParameterTypeDef]]


# DateTimeParameterDeclarationTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DateTimeDefaultValuesTypeDef]

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### ValueWhenUnset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DateTimeValueWhenUnsetConfigurationTypeDef]

### MappedDataSetParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.MappedDataSetParameterTypeDef]]


# DateTimeParameterOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.List[datetime.datetime]
- **Required**: Yes


# DateTimeParameterTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TimestampTypeDef]
- **Required**: Yes


# DateTimePickerControlDisplayOptionsTypeDef

### TitleOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LabelOptionsTypeDef]

### DateTimeFormat
- **Type**: typing.Optional[str]

### InfoIconLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SheetControlInfoIconLabelOptionsTypeDef]

### HelperTextVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### DateIconVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# DateTimeValueWhenUnsetConfigurationOutputTypeDef

### ValueWhenUnsetOption
- **Type**: typing.Optional[typing.Literal['NULL', 'RECOMMENDED_VALUE']]

### CustomValue
- **Type**: typing.Optional[datetime.datetime]


# DateTimeValueWhenUnsetConfigurationTypeDef

### ValueWhenUnsetOption
- **Type**: typing.Optional[typing.Literal['NULL', 'RECOMMENDED_VALUE']]

### CustomValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TimestampTypeDef]


# DecimalDatasetParameterDefaultValuesOutputTypeDef

### StaticValues
- **Type**: typing.Optional[typing.List[float]]


# DecimalDatasetParameterDefaultValuesTypeDef

### StaticValues
- **Type**: typing.Optional[typing.Sequence[float]]


# DecimalDatasetParameterDefaultValuesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DecimalDatasetParameterOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DecimalDatasetParameterDefaultValuesOutputTypeDef]


# DecimalDatasetParameterTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DecimalDatasetParameterDefaultValuesUnionTypeDef]


# DecimalDatasetParameterUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DecimalDefaultValuesOutputTypeDef

### DynamicValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DynamicDefaultValueTypeDef]

### StaticValues
- **Type**: typing.Optional[typing.List[float]]


# DecimalDefaultValuesTypeDef

### DynamicValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DynamicDefaultValueTypeDef]

### StaticValues
- **Type**: typing.Optional[typing.Sequence[float]]


# DecimalParameterDeclarationOutputTypeDef

### ParameterValueType
- **Type**: typing.Literal['MULTI_VALUED', 'SINGLE_VALUED']
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DecimalDefaultValuesOutputTypeDef]

### ValueWhenUnset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DecimalValueWhenUnsetConfigurationTypeDef]

### MappedDataSetParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.MappedDataSetParameterTypeDef]]


# DecimalParameterDeclarationTypeDef

### ParameterValueType
- **Type**: typing.Literal['MULTI_VALUED', 'SINGLE_VALUED']
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DecimalDefaultValuesTypeDef]

### ValueWhenUnset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DecimalValueWhenUnsetConfigurationTypeDef]

### MappedDataSetParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.MappedDataSetParameterTypeDef]]


# DecimalParameterOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.List[float]
- **Required**: Yes


# DecimalParameterTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.Sequence[float]
- **Required**: Yes


# DecimalPlacesConfigurationTypeDef

### DecimalPlaces
- **Type**: <class 'int'>
- **Required**: Yes


# DecimalValueWhenUnsetConfigurationTypeDef

### ValueWhenUnsetOption
- **Type**: typing.Optional[typing.Literal['NULL', 'RECOMMENDED_VALUE']]

### CustomValue
- **Type**: typing.Optional[float]


# DefaultDateTimePickerControlOptionsTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DefaultFilterControlConfigurationOutputTypeDef

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### ControlOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.DefaultFilterControlOptionsOutputTypeDef'>
- **Required**: Yes


# DefaultFilterControlConfigurationTypeDef

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### ControlOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.DefaultFilterControlOptionsTypeDef'>
- **Required**: Yes


# DefaultFilterControlOptionsOutputTypeDef

### DefaultDateTimePickerOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultDateTimePickerControlOptionsTypeDef]

### DefaultListOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultFilterListControlOptionsOutputTypeDef]

### DefaultDropdownOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultFilterDropDownControlOptionsOutputTypeDef]

### DefaultTextFieldOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultTextFieldControlOptionsTypeDef]

### DefaultTextAreaOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultTextAreaControlOptionsTypeDef]

### DefaultSliderOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultSliderControlOptionsTypeDef]

### DefaultRelativeDateTimeOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultRelativeDateTimeControlOptionsTypeDef]


# DefaultFilterControlOptionsTypeDef

### DefaultDateTimePickerOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultDateTimePickerControlOptionsTypeDef]

### DefaultListOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultFilterListControlOptionsTypeDef]

### DefaultDropdownOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultFilterDropDownControlOptionsTypeDef]

### DefaultTextFieldOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultTextFieldControlOptionsTypeDef]

### DefaultTextAreaOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultTextAreaControlOptionsTypeDef]

### DefaultSliderOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultSliderControlOptionsTypeDef]

### DefaultRelativeDateTimeOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultRelativeDateTimeControlOptionsTypeDef]


# DefaultFilterDropDownControlOptionsOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DefaultFilterDropDownControlOptionsTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DefaultFilterListControlOptionsOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DefaultFilterListControlOptionsTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DefaultFormattingTypeDef

### DisplayFormat
- **Type**: typing.Optional[typing.Literal['AUTO', 'CURRENCY', 'DATE', 'NUMBER', 'PERCENT', 'STRING']]

### DisplayFormatOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DisplayFormatOptionsTypeDef]


# DefaultFreeFormLayoutConfigurationTypeDef

### CanvasSizeOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.FreeFormLayoutCanvasSizeOptionsTypeDef'>
- **Required**: Yes


# DefaultGridLayoutConfigurationTypeDef

### CanvasSizeOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.GridLayoutCanvasSizeOptionsTypeDef'>
- **Required**: Yes


# DefaultInteractiveLayoutConfigurationTypeDef

### Grid
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultGridLayoutConfigurationTypeDef]

### FreeForm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultFreeFormLayoutConfigurationTypeDef]


# DefaultNewSheetConfigurationTypeDef

### InteractiveLayoutConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultInteractiveLayoutConfigurationTypeDef]

### PaginatedLayoutConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultPaginatedLayoutConfigurationTypeDef]

### SheetContentType
- **Type**: typing.Optional[typing.Literal['INTERACTIVE', 'PAGINATED']]


# DefaultPaginatedLayoutConfigurationTypeDef

### SectionBased
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultSectionBasedLayoutConfigurationTypeDef]


# DefaultRelativeDateTimeControlOptionsTypeDef

### DisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RelativeDateTimeControlDisplayOptionsTypeDef]

### CommitMode
- **Type**: typing.Optional[typing.Literal['AUTO', 'MANUAL']]


# DefaultSectionBasedLayoutConfigurationTypeDef

### CanvasSizeOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.SectionBasedLayoutCanvasSizeOptionsTypeDef'>
- **Required**: Yes


# DefaultSliderControlOptionsTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DefaultTextAreaControlOptionsTypeDef

### Delimiter
- **Type**: typing.Optional[str]

### DisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TextAreaControlDisplayOptionsTypeDef]


# DefaultTextFieldControlOptionsTypeDef

### DisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TextFieldControlDisplayOptionsTypeDef]


# DeleteAccountCustomizationRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: typing.Optional[str]


# DeleteAccountCustomizationResponseTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAccountSubscriptionRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAccountSubscriptionResponseTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAnalysisRequestTypeDef

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


# DeleteAnalysisResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteBrandAssignmentRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBrandAssignmentResponseTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteBrandRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BrandId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBrandResponseTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteCustomPermissionsRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### CustomPermissionsName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCustomPermissionsResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDashboardRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: typing.Optional[int]


# DeleteDashboardResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDataSetRefreshPropertiesRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataSetRefreshPropertiesResponseTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDataSetRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataSetResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDataSourceRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataSourceResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDefaultQBusinessApplicationRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: typing.Optional[str]


# DeleteDefaultQBusinessApplicationResponseTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteFolderMembershipRequestTypeDef

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


# DeleteFolderMembershipResponseTypeDef

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteFolderRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFolderResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteGroupMembershipRequestTypeDef

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


# DeleteGroupMembershipResponseTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteGroupRequestTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGroupResponseTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteIAMPolicyAssignmentRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AssignmentName
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIAMPolicyAssignmentResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteIdentityPropagationConfigRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Service
- **Type**: typing.Literal['QBUSINESS', 'REDSHIFT']
- **Required**: Yes


# DeleteIdentityPropagationConfigResponseTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteNamespaceRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNamespaceResponseTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteRefreshScheduleRequestTypeDef

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRefreshScheduleResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteRoleCustomPermissionRequestTypeDef

### Role
- **Type**: typing.Literal['ADMIN', 'ADMIN_PRO', 'AUTHOR', 'AUTHOR_PRO', 'READER', 'READER_PRO']
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRoleCustomPermissionResponseTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteRoleMembershipRequestTypeDef

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


# DeleteRoleMembershipResponseTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteTemplateAliasRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### AliasName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTemplateAliasResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteTemplateRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: typing.Optional[int]


# DeleteTemplateResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteThemeAliasRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ThemeId
- **Type**: <class 'str'>
- **Required**: Yes

### AliasName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteThemeAliasResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteThemeRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ThemeId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: typing.Optional[int]


# DeleteThemeResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteTopicRefreshScheduleRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTopicRefreshScheduleResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteTopicRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTopicResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteUserByPrincipalIdRequestTypeDef

### PrincipalId
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserByPrincipalIdResponseTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteUserCustomPermissionRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserCustomPermissionResponseTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteUserRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserResponseTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteVPCConnectionRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### VPCConnectionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVPCConnectionResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAccountCustomizationRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: typing.Optional[str]

### Resolved
- **Type**: typing.Optional[bool]


# DescribeAccountCustomizationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.AccountCustomizationTypeDef'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAccountSettingsRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAccountSettingsResponseTypeDef

### AccountSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.AccountSettingsTypeDef'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAccountSubscriptionRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAccountSubscriptionResponseTypeDef

### AccountInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.AccountInfoTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAnalysisDefinitionRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AnalysisId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAnalysisDefinitionResponseTypeDef

### AnalysisId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AnalysisErrorTypeDef]
- **Required**: Yes

### ResourceStatus
- **Type**: typing.Literal['CREATION_FAILED', 'CREATION_IN_PROGRESS', 'CREATION_SUCCESSFUL', 'DELETED', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']
- **Required**: Yes

### ThemeArn
- **Type**: <class 'str'>
- **Required**: Yes

### Definition
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.AnalysisDefinitionOutputTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAnalysisPermissionsRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AnalysisId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAnalysisPermissionsResponseTypeDef

### AnalysisId
- **Type**: <class 'str'>
- **Required**: Yes

### AnalysisArn
- **Type**: <class 'str'>
- **Required**: Yes

### Permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionOutputTypeDef]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAnalysisRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AnalysisId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAnalysisResponseTypeDef

### Analysis
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.AnalysisTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAssetBundleExportJobRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AssetBundleExportJobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAssetBundleExportJobResponseTypeDef

### JobStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'QUEUED_FOR_IMMEDIATE_EXECUTION', 'SUCCESSFUL']
- **Required**: Yes

### DownloadUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleExportJobErrorTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleCloudFormationOverridePropertyConfigurationOutputTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleExportJobValidationStrategyTypeDef'>
- **Required**: Yes

### Warnings
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleExportJobWarningTypeDef]
- **Required**: Yes

### IncludeFolderMemberships
- **Type**: <class 'bool'>
- **Required**: Yes

### IncludeFolderMembers
- **Type**: typing.Literal['NONE', 'ONE_LEVEL', 'RECURSE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAssetBundleImportJobRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AssetBundleImportJobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAssetBundleImportJobResponseTypeDef

### JobStatus
- **Type**: typing.Literal['FAILED', 'FAILED_ROLLBACK_COMPLETED', 'FAILED_ROLLBACK_ERROR', 'FAILED_ROLLBACK_IN_PROGRESS', 'IN_PROGRESS', 'QUEUED_FOR_IMMEDIATE_EXECUTION', 'SUCCESSFUL']
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobErrorTypeDef]
- **Required**: Yes

### RollbackErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobErrorTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportSourceDescriptionTypeDef'>
- **Required**: Yes

### OverrideParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobOverrideParametersOutputTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobOverridePermissionsOutputTypeDef'>
- **Required**: Yes

### OverrideTags
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobOverrideTagsOutputTypeDef'>
- **Required**: Yes

### OverrideValidationStrategy
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobOverrideValidationStrategyTypeDef'>
- **Required**: Yes

### Warnings
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobWarningTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeBrandAssignmentRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBrandAssignmentResponseTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### BrandArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeBrandPublishedVersionRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BrandId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBrandPublishedVersionResponseTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### BrandDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.BrandDetailTypeDef'>
- **Required**: Yes

### BrandDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.BrandDefinitionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeBrandRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BrandId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: typing.Optional[str]


# DescribeBrandResponseTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### BrandDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.BrandDetailTypeDef'>
- **Required**: Yes

### BrandDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.BrandDefinitionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeCustomPermissionsRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### CustomPermissionsName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCustomPermissionsResponseTypeDef

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### CustomPermissions
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.CustomPermissionsTypeDef'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDashboardDefinitionRequestTypeDef

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


# DescribeDashboardDefinitionResponseTypeDef

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DashboardErrorTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.DashboardVersionDefinitionOutputTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardPublishOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.DashboardPublishOptionsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDashboardPermissionsRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDashboardPermissionsResponseTypeDef

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardArn
- **Type**: <class 'str'>
- **Required**: Yes

### Permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionOutputTypeDef]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### LinkSharingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.LinkSharingConfigurationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDashboardRequestTypeDef

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


# DescribeDashboardResponseTypeDef

### Dashboard
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.DashboardTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDashboardSnapshotJobRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotJobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDashboardSnapshotJobResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.SnapshotUserConfigurationRedactedTypeDef'>
- **Required**: Yes

### SnapshotConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.SnapshotConfigurationOutputTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDashboardSnapshotJobResultRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotJobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDashboardSnapshotJobResultResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.SnapshotJobResultTypeDef'>
- **Required**: Yes

### ErrorInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.SnapshotJobErrorInfoTypeDef'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDashboardsQAConfigurationRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDashboardsQAConfigurationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDataSetPermissionsRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDataSetPermissionsResponseTypeDef

### DataSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionOutputTypeDef]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDataSetRefreshPropertiesRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDataSetRefreshPropertiesResponseTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### DataSetRefreshProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.DataSetRefreshPropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDataSetRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDataSetResponseTypeDef

### DataSet
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.DataSetTypeDef'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDataSourcePermissionsRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDataSourcePermissionsResponseTypeDef

### DataSourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionOutputTypeDef]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDataSourceRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDataSourceResponseTypeDef

### DataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.DataSourceTypeDef'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDefaultQBusinessApplicationRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: typing.Optional[str]


# DescribeDefaultQBusinessApplicationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFolderPermissionsRequestPaginateTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaginatorConfigTypeDef]


# DescribeFolderPermissionsRequestTypeDef

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


# DescribeFolderPermissionsResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionOutputTypeDef]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeFolderRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFolderResolvedPermissionsRequestPaginateTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaginatorConfigTypeDef]


# DescribeFolderResolvedPermissionsRequestTypeDef

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


# DescribeFolderResolvedPermissionsResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionOutputTypeDef]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeFolderResponseTypeDef

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### Folder
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.FolderTypeDef'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeGroupMembershipRequestTypeDef

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


# DescribeGroupMembershipResponseTypeDef

### GroupMember
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.GroupMemberTypeDef'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeGroupRequestTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeGroupResponseTypeDef

### Group
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.GroupTypeDef'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeIAMPolicyAssignmentRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AssignmentName
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeIAMPolicyAssignmentResponseTypeDef

### IAMPolicyAssignment
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.IAMPolicyAssignmentTypeDef'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeIngestionRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### IngestionId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeIngestionResponseTypeDef

### Ingestion
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.IngestionTypeDef'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeIpRestrictionRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeIpRestrictionResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeKeyRegistrationRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultKeyOnly
- **Type**: typing.Optional[bool]


# DescribeKeyRegistrationResponseTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### KeyRegistration
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.RegisteredCustomerManagedKeyTypeDef]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeNamespaceRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeNamespaceResponseTypeDef

### Namespace
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.NamespaceInfoV2TypeDef'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeQPersonalizationConfigurationRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeQPersonalizationConfigurationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeQuickSightQSearchConfigurationRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeQuickSightQSearchConfigurationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRefreshScheduleRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRefreshScheduleResponseTypeDef

### RefreshSchedule
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.RefreshScheduleOutputTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRoleCustomPermissionRequestTypeDef

### Role
- **Type**: typing.Literal['ADMIN', 'ADMIN_PRO', 'AUTHOR', 'AUTHOR_PRO', 'READER', 'READER_PRO']
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRoleCustomPermissionResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTemplateAliasRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### AliasName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTemplateAliasResponseTypeDef

### TemplateAlias
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.TemplateAliasTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTemplateDefinitionRequestTypeDef

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


# DescribeTemplateDefinitionResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.TemplateErrorTypeDef]
- **Required**: Yes

### ResourceStatus
- **Type**: typing.Literal['CREATION_FAILED', 'CREATION_IN_PROGRESS', 'CREATION_SUCCESSFUL', 'DELETED', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']
- **Required**: Yes

### ThemeArn
- **Type**: <class 'str'>
- **Required**: Yes

### Definition
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.TemplateVersionDefinitionOutputTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTemplatePermissionsRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTemplatePermissionsResponseTypeDef

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### Permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionOutputTypeDef]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTemplateRequestTypeDef

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


# DescribeTemplateResponseTypeDef

### Template
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.TemplateTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeThemeAliasRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ThemeId
- **Type**: <class 'str'>
- **Required**: Yes

### AliasName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeThemeAliasResponseTypeDef

### ThemeAlias
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ThemeAliasTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeThemePermissionsRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ThemeId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeThemePermissionsResponseTypeDef

### ThemeId
- **Type**: <class 'str'>
- **Required**: Yes

### ThemeArn
- **Type**: <class 'str'>
- **Required**: Yes

### Permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionOutputTypeDef]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeThemeRequestTypeDef

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


# DescribeThemeResponseTypeDef

### Theme
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ThemeTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTopicPermissionsRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTopicPermissionsResponseTypeDef

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### Permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionOutputTypeDef]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTopicRefreshRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### RefreshId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTopicRefreshResponseTypeDef

### RefreshDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.TopicRefreshDetailsTypeDef'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTopicRefreshScheduleRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTopicRefreshScheduleResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.TopicRefreshScheduleOutputTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTopicRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTopicResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### Topic
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.TopicDetailsOutputTypeDef'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeUserRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeUserResponseTypeDef

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.UserTypeDef'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeVPCConnectionRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### VPCConnectionId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeVPCConnectionResponseTypeDef

### VPCConnection
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.VPCConnectionTypeDef'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DestinationParameterValueConfigurationOutputTypeDef

### CustomValuesConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CustomValuesConfigurationOutputTypeDef]

### SelectAllValueOptions
- **Type**: typing.Optional[typing.Literal['ALL_VALUES']]

### SourceParameterName
- **Type**: typing.Optional[str]

### SourceField
- **Type**: typing.Optional[str]

### SourceColumn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef]


# DestinationParameterValueConfigurationTypeDef

### CustomValuesConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CustomValuesConfigurationTypeDef]

### SelectAllValueOptions
- **Type**: typing.Optional[typing.Literal['ALL_VALUES']]

### SourceParameterName
- **Type**: typing.Optional[str]

### SourceField
- **Type**: typing.Optional[str]

### SourceColumn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef]


# DimensionFieldTypeDef

### NumericalDimensionField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NumericalDimensionFieldTypeDef]

### CategoricalDimensionField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CategoricalDimensionFieldTypeDef]

### DateDimensionField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DateDimensionFieldTypeDef]


# DisplayFormatOptionsTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NegativeFormatTypeDef]

### CurrencySymbol
- **Type**: typing.Optional[str]


# DonutCenterOptionsTypeDef

### LabelVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# DonutOptionsTypeDef

### ArcOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ArcOptionsTypeDef]

### DonutCenterOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DonutCenterOptionsTypeDef]


# DrillDownFilterOutputTypeDef

### NumericEqualityFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NumericEqualityDrillDownFilterTypeDef]

### CategoryFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CategoryDrillDownFilterOutputTypeDef]

### TimeRangeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TimeRangeDrillDownFilterOutputTypeDef]


# DrillDownFilterTypeDef

### NumericEqualityFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NumericEqualityDrillDownFilterTypeDef]

### CategoryFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CategoryDrillDownFilterTypeDef]

### TimeRangeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TimeRangeDrillDownFilterTypeDef]


# DropDownControlDisplayOptionsTypeDef

### SelectAllOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ListControlSelectAllOptionsTypeDef]

### TitleOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LabelOptionsTypeDef]

### InfoIconLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SheetControlInfoIconLabelOptionsTypeDef]


# DynamicDefaultValueTypeDef

### DefaultValueColumn
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes

### UserNameColumn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef]

### GroupNameColumn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef]


# EmptyVisualOutputTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionOutputTypeDef]]


# EmptyVisualTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionTypeDef]]


# EntityTypeDef

### Path
- **Type**: typing.Optional[str]


# ErrorInfoTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ExasolParametersTypeDef

### Host
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes


# ExcludePeriodConfigurationTypeDef

### Amount
- **Type**: <class 'int'>
- **Required**: Yes

### Granularity
- **Type**: typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# ExplicitHierarchyOutputTypeDef

### HierarchyId
- **Type**: <class 'str'>
- **Required**: Yes

### Columns
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef]
- **Required**: Yes

### DrillDownFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DrillDownFilterOutputTypeDef]]


# ExplicitHierarchyTypeDef

### HierarchyId
- **Type**: <class 'str'>
- **Required**: Yes

### Columns
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef]
- **Required**: Yes

### DrillDownFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DrillDownFilterTypeDef]]


# ExportHiddenFieldsOptionTypeDef

### AvailabilityStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# ExportToCSVOptionTypeDef

### AvailabilityStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# ExportWithHiddenFieldsOptionTypeDef

### AvailabilityStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# FailedKeyRegistrationEntryTypeDef

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


# FieldBasedTooltipOutputTypeDef

### AggregationVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### TooltipTitleType
- **Type**: typing.Optional[typing.Literal['NONE', 'PRIMARY_VALUE']]

### TooltipFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.TooltipItemTypeDef]]


# FieldBasedTooltipTypeDef

### AggregationVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### TooltipTitleType
- **Type**: typing.Optional[typing.Literal['NONE', 'PRIMARY_VALUE']]

### TooltipFields
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TooltipItemTypeDef]]


# FieldFolderOutputTypeDef

### description
- **Type**: typing.Optional[str]

### columns
- **Type**: typing.Optional[typing.List[str]]


# FieldFolderTypeDef

### description
- **Type**: typing.Optional[str]

### columns
- **Type**: typing.Optional[typing.Sequence[str]]


# FieldFolderUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FieldLabelTypeTypeDef

### FieldId
- **Type**: typing.Optional[str]

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# FieldSeriesItemTypeDef

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### AxisBinding
- **Type**: typing.Literal['PRIMARY_YAXIS', 'SECONDARY_YAXIS']
- **Required**: Yes

### Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LineChartSeriesSettingsTypeDef]


# FieldSortOptionsTypeDef

### FieldSort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortTypeDef]

### ColumnSort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ColumnSortTypeDef]


# FieldSortTypeDef

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### Direction
- **Type**: typing.Literal['ASC', 'DESC']
- **Required**: Yes


# FieldTooltipItemTypeDef

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### Label
- **Type**: typing.Optional[str]

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### TooltipTarget
- **Type**: typing.Optional[typing.Literal['BAR', 'BOTH', 'LINE']]


# FilledMapAggregatedFieldWellsOutputTypeDef

### Geospatial
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]


# FilledMapAggregatedFieldWellsTypeDef

### Geospatial
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Values
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]


# FilledMapConditionalFormattingOptionOutputTypeDef

### Shape
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.FilledMapShapeConditionalFormattingOutputTypeDef'>
- **Required**: Yes


# FilledMapConditionalFormattingOptionTypeDef

### Shape
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.FilledMapShapeConditionalFormattingTypeDef'>
- **Required**: Yes


# FilledMapConditionalFormattingOutputTypeDef

### ConditionalFormattingOptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.FilledMapConditionalFormattingOptionOutputTypeDef]
- **Required**: Yes


# FilledMapConditionalFormattingTypeDef

### ConditionalFormattingOptions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.FilledMapConditionalFormattingOptionTypeDef]
- **Required**: Yes


# FilledMapConfigurationOutputTypeDef

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FilledMapFieldWellsOutputTypeDef]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FilledMapSortConfigurationOutputTypeDef]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LegendOptionsTypeDef]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TooltipOptionsOutputTypeDef]

### WindowOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialWindowOptionsTypeDef]

### MapStyleOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialMapStyleOptionsTypeDef]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# FilledMapConfigurationTypeDef

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FilledMapFieldWellsTypeDef]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FilledMapSortConfigurationTypeDef]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LegendOptionsTypeDef]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TooltipOptionsTypeDef]

### WindowOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialWindowOptionsTypeDef]

### MapStyleOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialMapStyleOptionsTypeDef]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# FilledMapFieldWellsOutputTypeDef

### FilledMapAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FilledMapAggregatedFieldWellsOutputTypeDef]


# FilledMapFieldWellsTypeDef

### FilledMapAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FilledMapAggregatedFieldWellsTypeDef]


# FilledMapShapeConditionalFormattingOutputTypeDef

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### Format
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ShapeConditionalFormatOutputTypeDef]


# FilledMapShapeConditionalFormattingTypeDef

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### Format
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ShapeConditionalFormatTypeDef]


# FilledMapSortConfigurationOutputTypeDef

### CategorySort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]


# FilledMapSortConfigurationTypeDef

### CategorySort
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]


# FilledMapVisualOutputTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FilledMapConfigurationOutputTypeDef]

### ConditionalFormatting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FilledMapConditionalFormattingOutputTypeDef]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ColumnHierarchyOutputTypeDef]]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionOutputTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# FilledMapVisualTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FilledMapConfigurationTypeDef]

### ConditionalFormatting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FilledMapConditionalFormattingTypeDef]

### ColumnHierarchies
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ColumnHierarchyTypeDef]]

### Actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# FilterAggMetricsTypeDef

### MetricOperand
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.IdentifierTypeDef]

### Function
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'COLUMN', 'COUNT', 'CUSTOM', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'PERCENTILE', 'PTD_AVERAGE', 'PTD_COUNT', 'PTD_DISTINCT_COUNT', 'PTD_MAX', 'PTD_MIN', 'PTD_SUM', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]

### SortDirection
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# FilterControlOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FilterControlTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FilterCrossSheetControlOutputTypeDef

### FilterControlId
- **Type**: <class 'str'>
- **Required**: Yes

### SourceFilterId
- **Type**: <class 'str'>
- **Required**: Yes

### CascadingControlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CascadingControlConfigurationOutputTypeDef]


# FilterCrossSheetControlTypeDef

### FilterControlId
- **Type**: <class 'str'>
- **Required**: Yes

### SourceFilterId
- **Type**: <class 'str'>
- **Required**: Yes

### CascadingControlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CascadingControlConfigurationTypeDef]


# FilterGroupOutputTypeDef

### FilterGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.FilterOutputTypeDef]
- **Required**: Yes

### ScopeConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.FilterScopeConfigurationOutputTypeDef'>
- **Required**: Yes

### CrossDataset
- **Type**: typing.Literal['ALL_DATASETS', 'SINGLE_DATASET']
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# FilterGroupTypeDef

### FilterGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.FilterTypeDef]
- **Required**: Yes

### ScopeConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.FilterScopeConfigurationTypeDef'>
- **Required**: Yes

### CrossDataset
- **Type**: typing.Literal['ALL_DATASETS', 'SINGLE_DATASET']
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# FilterListConfigurationOutputTypeDef

### MatchOperator
- **Type**: typing.Literal['CONTAINS', 'DOES_NOT_CONTAIN', 'DOES_NOT_EQUAL', 'ENDS_WITH', 'EQUALS', 'STARTS_WITH']
- **Required**: Yes

### CategoryValues
- **Type**: typing.Optional[typing.List[str]]

### SelectAllOptions
- **Type**: typing.Optional[typing.Literal['FILTER_ALL_VALUES']]

### NullOption
- **Type**: typing.Optional[typing.Literal['ALL_VALUES', 'NON_NULLS_ONLY', 'NULLS_ONLY']]


# FilterListConfigurationTypeDef

### MatchOperator
- **Type**: typing.Literal['CONTAINS', 'DOES_NOT_CONTAIN', 'DOES_NOT_EQUAL', 'ENDS_WITH', 'EQUALS', 'STARTS_WITH']
- **Required**: Yes

### CategoryValues
- **Type**: typing.Optional[typing.Sequence[str]]

### SelectAllOptions
- **Type**: typing.Optional[typing.Literal['FILTER_ALL_VALUES']]

### NullOption
- **Type**: typing.Optional[typing.Literal['ALL_VALUES', 'NON_NULLS_ONLY', 'NULLS_ONLY']]


# FilterOperationSelectedFieldsConfigurationOutputTypeDef

### SelectedFields
- **Type**: typing.Optional[typing.List[str]]

### SelectedFieldOptions
- **Type**: typing.Optional[typing.Literal['ALL_FIELDS']]

### SelectedColumns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef]]


# FilterOperationSelectedFieldsConfigurationTypeDef

### SelectedFields
- **Type**: typing.Optional[typing.Sequence[str]]

### SelectedFieldOptions
- **Type**: typing.Optional[typing.Literal['ALL_FIELDS']]

### SelectedColumns
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef]]


# FilterOperationTargetVisualsConfigurationOutputTypeDef

### SameSheetTargetVisualConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SameSheetTargetVisualConfigurationOutputTypeDef]


# FilterOperationTargetVisualsConfigurationTypeDef

### SameSheetTargetVisualConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SameSheetTargetVisualConfigurationTypeDef]


# FilterOperationTypeDef

### ConditionExpression
- **Type**: <class 'str'>
- **Required**: Yes


# FilterOutputTypeDef

### CategoryFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CategoryFilterOutputTypeDef]

### NumericRangeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NumericRangeFilterOutputTypeDef]

### NumericEqualityFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NumericEqualityFilterOutputTypeDef]

### TimeEqualityFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TimeEqualityFilterOutputTypeDef]

### TimeRangeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TimeRangeFilterOutputTypeDef]

### RelativeDatesFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RelativeDatesFilterOutputTypeDef]

### TopBottomFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopBottomFilterOutputTypeDef]

### NestedFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NestedFilterOutputTypeDef]


# FilterRelativeDateTimeControlTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RelativeDateTimeControlDisplayOptionsTypeDef]

### CommitMode
- **Type**: typing.Optional[typing.Literal['AUTO', 'MANUAL']]


# FilterScopeConfigurationOutputTypeDef

### SelectedSheets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SelectedSheetsFilterScopeConfigurationOutputTypeDef]

### AllSheets
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# FilterScopeConfigurationTypeDef

### SelectedSheets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SelectedSheetsFilterScopeConfigurationTypeDef]

### AllSheets
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# FilterSelectableValuesOutputTypeDef

### Values
- **Type**: typing.Optional[typing.List[str]]


# FilterSelectableValuesTypeDef

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# FilterTextAreaControlTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TextAreaControlDisplayOptionsTypeDef]


# FilterTextFieldControlTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TextFieldControlDisplayOptionsTypeDef]


# FilterTypeDef

### CategoryFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CategoryFilterTypeDef]

### NumericRangeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NumericRangeFilterTypeDef]

### NumericEqualityFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NumericEqualityFilterTypeDef]

### TimeEqualityFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TimeEqualityFilterTypeDef]

### TimeRangeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TimeRangeFilterTypeDef]

### RelativeDatesFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RelativeDatesFilterTypeDef]

### TopBottomFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopBottomFilterTypeDef]

### NestedFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NestedFilterTypeDef]


# FolderMemberTypeDef

### MemberId
- **Type**: typing.Optional[str]

### MemberType
- **Type**: typing.Optional[typing.Literal['ANALYSIS', 'DASHBOARD', 'DATASET', 'DATASOURCE', 'TOPIC']]


# FolderSearchFilterTypeDef

### Operator
- **Type**: typing.Optional[typing.Literal['StringEquals', 'StringLike']]

### Name
- **Type**: typing.Optional[typing.Literal['DIRECT_QUICKSIGHT_OWNER', 'DIRECT_QUICKSIGHT_SOLE_OWNER', 'DIRECT_QUICKSIGHT_VIEWER_OR_OWNER', 'FOLDER_NAME', 'PARENT_FOLDER_ARN', 'QUICKSIGHT_OWNER', 'QUICKSIGHT_VIEWER_OR_OWNER']]

### Value
- **Type**: typing.Optional[str]


# FolderSummaryTypeDef

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


# FolderTypeDef

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


# FontConfigurationTypeDef

### FontSize
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FontSizeTypeDef]

### FontDecoration
- **Type**: typing.Optional[typing.Literal['NONE', 'UNDERLINE']]

### FontColor
- **Type**: typing.Optional[str]

### FontWeight
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FontWeightTypeDef]

### FontStyle
- **Type**: typing.Optional[typing.Literal['ITALIC', 'NORMAL']]

### FontFamily
- **Type**: typing.Optional[str]


# FontSizeTypeDef

### Relative
- **Type**: typing.Optional[typing.Literal['EXTRA_LARGE', 'EXTRA_SMALL', 'LARGE', 'MEDIUM', 'SMALL']]

### Absolute
- **Type**: typing.Optional[str]


# FontTypeDef

### FontFamily
- **Type**: typing.Optional[str]


# FontWeightTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['BOLD', 'NORMAL']]


# ForecastComputationTypeDef

### ComputationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Time
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]

### Value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]

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


# ForecastConfigurationOutputTypeDef

### ForecastProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TimeBasedForecastPropertiesTypeDef]

### Scenario
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ForecastScenarioOutputTypeDef]


# ForecastConfigurationTypeDef

### ForecastProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TimeBasedForecastPropertiesTypeDef]

### Scenario
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ForecastScenarioTypeDef]


# ForecastScenarioOutputTypeDef

### WhatIfPointScenario
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.WhatIfPointScenarioOutputTypeDef]

### WhatIfRangeScenario
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.WhatIfRangeScenarioOutputTypeDef]


# ForecastScenarioTypeDef

### WhatIfPointScenario
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.WhatIfPointScenarioTypeDef]

### WhatIfRangeScenario
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.WhatIfRangeScenarioTypeDef]


# FormatConfigurationTypeDef

### StringFormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.StringFormatConfigurationTypeDef]

### NumberFormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NumberFormatConfigurationTypeDef]

### DateTimeFormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DateTimeFormatConfigurationTypeDef]


# FreeFormLayoutCanvasSizeOptionsTypeDef

### ScreenCanvasSizeOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FreeFormLayoutScreenCanvasSizeOptionsTypeDef]


# FreeFormLayoutConfigurationOutputTypeDef

### Elements
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.FreeFormLayoutElementOutputTypeDef]
- **Required**: Yes

### CanvasSizeOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FreeFormLayoutCanvasSizeOptionsTypeDef]


# FreeFormLayoutConfigurationTypeDef

### Elements
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.FreeFormLayoutElementTypeDef]
- **Required**: Yes

### CanvasSizeOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FreeFormLayoutCanvasSizeOptionsTypeDef]


# FreeFormLayoutElementBackgroundStyleTypeDef

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### Color
- **Type**: typing.Optional[str]


# FreeFormLayoutElementBorderStyleTypeDef

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### Color
- **Type**: typing.Optional[str]


# FreeFormLayoutElementOutputTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.SheetElementRenderingRuleTypeDef]]

### BorderStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FreeFormLayoutElementBorderStyleTypeDef]

### SelectedBorderStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FreeFormLayoutElementBorderStyleTypeDef]

### BackgroundStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FreeFormLayoutElementBackgroundStyleTypeDef]

### LoadingAnimation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LoadingAnimationTypeDef]


# FreeFormLayoutElementTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.SheetElementRenderingRuleTypeDef]]

### BorderStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FreeFormLayoutElementBorderStyleTypeDef]

### SelectedBorderStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FreeFormLayoutElementBorderStyleTypeDef]

### BackgroundStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FreeFormLayoutElementBackgroundStyleTypeDef]

### LoadingAnimation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LoadingAnimationTypeDef]


# FreeFormLayoutScreenCanvasSizeOptionsTypeDef

### OptimizedViewPortWidth
- **Type**: <class 'str'>
- **Required**: Yes


# FreeFormSectionLayoutConfigurationOutputTypeDef

### Elements
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.FreeFormLayoutElementOutputTypeDef]
- **Required**: Yes


# FreeFormSectionLayoutConfigurationTypeDef

### Elements
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.FreeFormLayoutElementTypeDef]
- **Required**: Yes


# FunnelChartAggregatedFieldWellsOutputTypeDef

### Category
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]


# FunnelChartAggregatedFieldWellsTypeDef

### Category
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Values
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]


# FunnelChartConfigurationOutputTypeDef

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FunnelChartFieldWellsOutputTypeDef]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FunnelChartSortConfigurationOutputTypeDef]

### CategoryLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsOutputTypeDef]

### ValueLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsOutputTypeDef]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TooltipOptionsOutputTypeDef]

### DataLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FunnelChartDataLabelOptionsTypeDef]

### VisualPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualPaletteOutputTypeDef]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# FunnelChartConfigurationTypeDef

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FunnelChartFieldWellsTypeDef]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FunnelChartSortConfigurationTypeDef]

### CategoryLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsTypeDef]

### ValueLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsTypeDef]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TooltipOptionsTypeDef]

### DataLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FunnelChartDataLabelOptionsTypeDef]

### VisualPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualPaletteTypeDef]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# FunnelChartDataLabelOptionsTypeDef

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### CategoryLabelVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### MeasureLabelVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### Position
- **Type**: typing.Optional[typing.Literal['BOTTOM', 'INSIDE', 'LEFT', 'OUTSIDE', 'RIGHT', 'TOP']]

### LabelFontConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FontConfigurationTypeDef]

### LabelColor
- **Type**: typing.Optional[str]

### MeasureDataLabelStyle
- **Type**: typing.Optional[typing.Literal['PERCENTAGE_BY_FIRST_STAGE', 'PERCENTAGE_BY_PREVIOUS_STAGE', 'VALUE_AND_PERCENTAGE_BY_FIRST_STAGE', 'VALUE_AND_PERCENTAGE_BY_PREVIOUS_STAGE', 'VALUE_ONLY']]


# FunnelChartFieldWellsOutputTypeDef

### FunnelChartAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FunnelChartAggregatedFieldWellsOutputTypeDef]


# FunnelChartFieldWellsTypeDef

### FunnelChartAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FunnelChartAggregatedFieldWellsTypeDef]


# FunnelChartSortConfigurationOutputTypeDef

### CategorySort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### CategoryItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]


# FunnelChartSortConfigurationTypeDef

### CategorySort
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### CategoryItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]


# FunnelChartVisualOutputTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FunnelChartConfigurationOutputTypeDef]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionOutputTypeDef]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ColumnHierarchyOutputTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# FunnelChartVisualTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FunnelChartConfigurationTypeDef]

### Actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionTypeDef]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ColumnHierarchyTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# GaugeChartArcConditionalFormattingOutputTypeDef

### ForegroundColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingColorOutputTypeDef]


# GaugeChartArcConditionalFormattingTypeDef

### ForegroundColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingColorTypeDef]


# GaugeChartColorConfigurationTypeDef

### ForegroundColor
- **Type**: typing.Optional[str]

### BackgroundColor
- **Type**: typing.Optional[str]


# GaugeChartConditionalFormattingOptionOutputTypeDef

### PrimaryValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GaugeChartPrimaryValueConditionalFormattingOutputTypeDef]

### Arc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GaugeChartArcConditionalFormattingOutputTypeDef]


# GaugeChartConditionalFormattingOptionTypeDef

### PrimaryValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GaugeChartPrimaryValueConditionalFormattingTypeDef]

### Arc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GaugeChartArcConditionalFormattingTypeDef]


# GaugeChartConditionalFormattingOutputTypeDef

### ConditionalFormattingOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.GaugeChartConditionalFormattingOptionOutputTypeDef]]


# GaugeChartConditionalFormattingTypeDef

### ConditionalFormattingOptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.GaugeChartConditionalFormattingOptionTypeDef]]


# GaugeChartConfigurationOutputTypeDef

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GaugeChartFieldWellsOutputTypeDef]

### GaugeChartOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GaugeChartOptionsTypeDef]

### DataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataLabelOptionsOutputTypeDef]

### TooltipOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TooltipOptionsOutputTypeDef]

### VisualPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualPaletteOutputTypeDef]

### ColorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GaugeChartColorConfigurationTypeDef]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# GaugeChartConfigurationTypeDef

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GaugeChartFieldWellsTypeDef]

### GaugeChartOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GaugeChartOptionsTypeDef]

### DataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataLabelOptionsTypeDef]

### TooltipOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TooltipOptionsTypeDef]

### VisualPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualPaletteTypeDef]

### ColorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GaugeChartColorConfigurationTypeDef]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# GaugeChartFieldWellsOutputTypeDef

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]

### TargetValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]


# GaugeChartFieldWellsTypeDef

### Values
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]

### TargetValues
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]


# GaugeChartOptionsTypeDef

### PrimaryValueDisplayType
- **Type**: typing.Optional[typing.Literal['ACTUAL', 'COMPARISON', 'HIDDEN']]

### Comparison
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ComparisonConfigurationTypeDef]

### ArcAxis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ArcAxisConfigurationTypeDef]

### Arc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ArcConfigurationTypeDef]

### PrimaryValueFontConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FontConfigurationTypeDef]


# GaugeChartPrimaryValueConditionalFormattingOutputTypeDef

### TextColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingColorOutputTypeDef]

### Icon
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingIconTypeDef]


# GaugeChartPrimaryValueConditionalFormattingTypeDef

### TextColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingColorTypeDef]

### Icon
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingIconTypeDef]


# GaugeChartVisualOutputTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GaugeChartConfigurationOutputTypeDef]

### ConditionalFormatting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GaugeChartConditionalFormattingOutputTypeDef]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionOutputTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# GaugeChartVisualTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GaugeChartConfigurationTypeDef]

### ConditionalFormatting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GaugeChartConditionalFormattingTypeDef]

### Actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# GenerateEmbedUrlForAnonymousUserRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizedResourceArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ExperienceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.AnonymousUserEmbeddingExperienceConfigurationTypeDef'>
- **Required**: Yes

### SessionLifetimeInMinutes
- **Type**: typing.Optional[int]

### SessionTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.SessionTagTypeDef]]

### AllowedDomains
- **Type**: typing.Optional[typing.Sequence[str]]


# GenerateEmbedUrlForAnonymousUserResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GenerateEmbedUrlForRegisteredUserRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### UserArn
- **Type**: <class 'str'>
- **Required**: Yes

### ExperienceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.RegisteredUserEmbeddingExperienceConfigurationTypeDef'>
- **Required**: Yes

### SessionLifetimeInMinutes
- **Type**: typing.Optional[int]

### AllowedDomains
- **Type**: typing.Optional[typing.Sequence[str]]


# GenerateEmbedUrlForRegisteredUserResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GenerateEmbedUrlForRegisteredUserWithIdentityRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ExperienceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.RegisteredUserEmbeddingExperienceConfigurationTypeDef'>
- **Required**: Yes

### SessionLifetimeInMinutes
- **Type**: typing.Optional[int]

### AllowedDomains
- **Type**: typing.Optional[typing.Sequence[str]]


# GenerateEmbedUrlForRegisteredUserWithIdentityResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GeneratedAnswerResultTypeDef

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


# GeoSpatialColumnGroupOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Columns
- **Type**: typing.List[str]
- **Required**: Yes

### CountryCode
- **Type**: typing.Optional[typing.Literal['US']]


# GeoSpatialColumnGroupTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Columns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### CountryCode
- **Type**: typing.Optional[typing.Literal['US']]


# GeoSpatialColumnGroupUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GeospatialCategoricalColorOutputTypeDef

### CategoryDataColors
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialCategoricalDataColorTypeDef]
- **Required**: Yes

### NullDataVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### NullDataSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialNullDataSettingsTypeDef]

### DefaultOpacity
- **Type**: typing.Optional[float]


# GeospatialCategoricalColorTypeDef

### CategoryDataColors
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialCategoricalDataColorTypeDef]
- **Required**: Yes

### NullDataVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### NullDataSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialNullDataSettingsTypeDef]

### DefaultOpacity
- **Type**: typing.Optional[float]


# GeospatialCategoricalDataColorTypeDef

### Color
- **Type**: <class 'str'>
- **Required**: Yes

### DataValue
- **Type**: <class 'str'>
- **Required**: Yes


# GeospatialCircleRadiusTypeDef

### Radius
- **Type**: typing.Optional[float]


# GeospatialCircleSymbolStyleOutputTypeDef

### FillColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialColorOutputTypeDef]

### StrokeColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialColorOutputTypeDef]

### StrokeWidth
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialLineWidthTypeDef]

### CircleRadius
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialCircleRadiusTypeDef]


# GeospatialCircleSymbolStyleTypeDef

### FillColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialColorTypeDef]

### StrokeColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialColorTypeDef]

### StrokeWidth
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialLineWidthTypeDef]

### CircleRadius
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialCircleRadiusTypeDef]


# GeospatialColorOutputTypeDef

### Solid
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialSolidColorTypeDef]

### Gradient
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialGradientColorOutputTypeDef]

### Categorical
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialCategoricalColorOutputTypeDef]


# GeospatialColorTypeDef

### Solid
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialSolidColorTypeDef]

### Gradient
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialGradientColorTypeDef]

### Categorical
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialCategoricalColorTypeDef]


# GeospatialCoordinateBoundsTypeDef

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


# GeospatialDataSourceItemTypeDef

### StaticFileDataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialStaticFileSourceTypeDef]


# GeospatialGradientColorOutputTypeDef

### StepColors
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialGradientStepColorTypeDef]
- **Required**: Yes

### NullDataVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### NullDataSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialNullDataSettingsTypeDef]

### DefaultOpacity
- **Type**: typing.Optional[float]


# GeospatialGradientColorTypeDef

### StepColors
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialGradientStepColorTypeDef]
- **Required**: Yes

### NullDataVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### NullDataSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialNullDataSettingsTypeDef]

### DefaultOpacity
- **Type**: typing.Optional[float]


# GeospatialGradientStepColorTypeDef

### Color
- **Type**: <class 'str'>
- **Required**: Yes

### DataValue
- **Type**: <class 'float'>
- **Required**: Yes


# GeospatialHeatmapColorScaleOutputTypeDef

### Colors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialHeatmapDataColorTypeDef]]


# GeospatialHeatmapColorScaleTypeDef

### Colors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialHeatmapDataColorTypeDef]]


# GeospatialHeatmapConfigurationOutputTypeDef

### HeatmapColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialHeatmapColorScaleOutputTypeDef]


# GeospatialHeatmapConfigurationTypeDef

### HeatmapColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialHeatmapColorScaleTypeDef]


# GeospatialHeatmapDataColorTypeDef

### Color
- **Type**: <class 'str'>
- **Required**: Yes


# GeospatialLayerColorFieldOutputTypeDef

### ColorDimensionsFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### ColorValuesFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]


# GeospatialLayerColorFieldTypeDef

### ColorDimensionsFields
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### ColorValuesFields
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]


# GeospatialLayerDefinitionOutputTypeDef

### PointLayer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialPointLayerOutputTypeDef]

### LineLayer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialLineLayerOutputTypeDef]

### PolygonLayer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialPolygonLayerOutputTypeDef]


# GeospatialLayerDefinitionTypeDef

### PointLayer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialPointLayerTypeDef]

### LineLayer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialLineLayerTypeDef]

### PolygonLayer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialPolygonLayerTypeDef]


# GeospatialLayerItemOutputTypeDef

### LayerId
- **Type**: <class 'str'>
- **Required**: Yes

### LayerType
- **Type**: typing.Optional[typing.Literal['LINE', 'POINT', 'POLYGON']]

### DataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialDataSourceItemTypeDef]

### Label
- **Type**: typing.Optional[str]

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### LayerDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialLayerDefinitionOutputTypeDef]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TooltipOptionsOutputTypeDef]

### JoinDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialLayerJoinDefinitionOutputTypeDef]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.LayerCustomActionOutputTypeDef]]


# GeospatialLayerItemTypeDef

### LayerId
- **Type**: <class 'str'>
- **Required**: Yes

### LayerType
- **Type**: typing.Optional[typing.Literal['LINE', 'POINT', 'POLYGON']]

### DataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialDataSourceItemTypeDef]

### Label
- **Type**: typing.Optional[str]

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### LayerDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialLayerDefinitionTypeDef]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TooltipOptionsTypeDef]

### JoinDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialLayerJoinDefinitionTypeDef]

### Actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.LayerCustomActionTypeDef]]


# GeospatialLayerJoinDefinitionOutputTypeDef

### ShapeKeyField
- **Type**: typing.Optional[str]

### DatasetKeyField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.UnaggregatedFieldTypeDef]

### ColorField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialLayerColorFieldOutputTypeDef]


# GeospatialLayerJoinDefinitionTypeDef

### ShapeKeyField
- **Type**: typing.Optional[str]

### DatasetKeyField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.UnaggregatedFieldTypeDef]

### ColorField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialLayerColorFieldTypeDef]


# GeospatialLayerMapConfigurationOutputTypeDef

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LegendOptionsTypeDef]

### MapLayers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialLayerItemOutputTypeDef]]

### MapState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialMapStateTypeDef]

### MapStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialMapStyleTypeDef]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# GeospatialLayerMapConfigurationTypeDef

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LegendOptionsTypeDef]

### MapLayers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialLayerItemTypeDef]]

### MapState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialMapStateTypeDef]

### MapStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialMapStyleTypeDef]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# GeospatialLineLayerOutputTypeDef

### Style
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.GeospatialLineStyleOutputTypeDef'>
- **Required**: Yes


# GeospatialLineLayerTypeDef

### Style
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.GeospatialLineStyleTypeDef'>
- **Required**: Yes


# GeospatialLineStyleOutputTypeDef

### LineSymbolStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialLineSymbolStyleOutputTypeDef]


# GeospatialLineStyleTypeDef

### LineSymbolStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialLineSymbolStyleTypeDef]


# GeospatialLineSymbolStyleOutputTypeDef

### FillColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialColorOutputTypeDef]

### LineWidth
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialLineWidthTypeDef]


# GeospatialLineSymbolStyleTypeDef

### FillColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialColorTypeDef]

### LineWidth
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialLineWidthTypeDef]


# GeospatialLineWidthTypeDef

### LineWidth
- **Type**: typing.Optional[float]


# GeospatialMapAggregatedFieldWellsOutputTypeDef

### Geospatial
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]

### Colors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]


# GeospatialMapAggregatedFieldWellsTypeDef

### Geospatial
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Values
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]

### Colors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]


# GeospatialMapConfigurationOutputTypeDef

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialMapFieldWellsOutputTypeDef]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LegendOptionsTypeDef]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TooltipOptionsOutputTypeDef]

### WindowOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialWindowOptionsTypeDef]

### MapStyleOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialMapStyleOptionsTypeDef]

### PointStyleOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialPointStyleOptionsOutputTypeDef]

### VisualPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualPaletteOutputTypeDef]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# GeospatialMapConfigurationTypeDef

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialMapFieldWellsTypeDef]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LegendOptionsTypeDef]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TooltipOptionsTypeDef]

### WindowOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialWindowOptionsTypeDef]

### MapStyleOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialMapStyleOptionsTypeDef]

### PointStyleOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialPointStyleOptionsTypeDef]

### VisualPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualPaletteTypeDef]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# GeospatialMapFieldWellsOutputTypeDef

### GeospatialMapAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialMapAggregatedFieldWellsOutputTypeDef]


# GeospatialMapFieldWellsTypeDef

### GeospatialMapAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialMapAggregatedFieldWellsTypeDef]


# GeospatialMapStateTypeDef

### Bounds
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialCoordinateBoundsTypeDef]

### MapNavigation
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# GeospatialMapStyleOptionsTypeDef

### BaseMapStyle
- **Type**: typing.Optional[typing.Literal['DARK_GRAY', 'IMAGERY', 'LIGHT_GRAY', 'STREET']]


# GeospatialMapStyleTypeDef

### BaseMapStyle
- **Type**: typing.Optional[typing.Literal['DARK_GRAY', 'IMAGERY', 'LIGHT_GRAY', 'STREET']]

### BackgroundColor
- **Type**: typing.Optional[str]

### BaseMapVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# GeospatialMapVisualOutputTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialMapConfigurationOutputTypeDef]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ColumnHierarchyOutputTypeDef]]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionOutputTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# GeospatialMapVisualTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialMapConfigurationTypeDef]

### ColumnHierarchies
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ColumnHierarchyTypeDef]]

### Actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# GeospatialNullDataSettingsTypeDef

### SymbolStyle
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.GeospatialNullSymbolStyleTypeDef'>
- **Required**: Yes


# GeospatialNullSymbolStyleTypeDef

### FillColor
- **Type**: typing.Optional[str]

### StrokeColor
- **Type**: typing.Optional[str]

### StrokeWidth
- **Type**: typing.Optional[float]


# GeospatialPointLayerOutputTypeDef

### Style
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.GeospatialPointStyleOutputTypeDef'>
- **Required**: Yes


# GeospatialPointLayerTypeDef

### Style
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.GeospatialPointStyleTypeDef'>
- **Required**: Yes


# GeospatialPointStyleOptionsOutputTypeDef

### SelectedPointStyle
- **Type**: typing.Optional[typing.Literal['CLUSTER', 'HEATMAP', 'POINT']]

### ClusterMarkerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ClusterMarkerConfigurationTypeDef]

### HeatmapConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialHeatmapConfigurationOutputTypeDef]


# GeospatialPointStyleOptionsTypeDef

### SelectedPointStyle
- **Type**: typing.Optional[typing.Literal['CLUSTER', 'HEATMAP', 'POINT']]

### ClusterMarkerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ClusterMarkerConfigurationTypeDef]

### HeatmapConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialHeatmapConfigurationTypeDef]


# GeospatialPointStyleOutputTypeDef

### CircleSymbolStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialCircleSymbolStyleOutputTypeDef]


# GeospatialPointStyleTypeDef

### CircleSymbolStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialCircleSymbolStyleTypeDef]


# GeospatialPolygonLayerOutputTypeDef

### Style
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.GeospatialPolygonStyleOutputTypeDef'>
- **Required**: Yes


# GeospatialPolygonLayerTypeDef

### Style
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.GeospatialPolygonStyleTypeDef'>
- **Required**: Yes


# GeospatialPolygonStyleOutputTypeDef

### PolygonSymbolStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialPolygonSymbolStyleOutputTypeDef]


# GeospatialPolygonStyleTypeDef

### PolygonSymbolStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialPolygonSymbolStyleTypeDef]


# GeospatialPolygonSymbolStyleOutputTypeDef

### FillColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialColorOutputTypeDef]

### StrokeColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialColorOutputTypeDef]

### StrokeWidth
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialLineWidthTypeDef]


# GeospatialPolygonSymbolStyleTypeDef

### FillColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialColorTypeDef]

### StrokeColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialColorTypeDef]

### StrokeWidth
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialLineWidthTypeDef]


# GeospatialSolidColorTypeDef

### Color
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# GeospatialStaticFileSourceTypeDef

### StaticFileId
- **Type**: <class 'str'>
- **Required**: Yes


# GeospatialWindowOptionsTypeDef

### Bounds
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialCoordinateBoundsTypeDef]

### MapZoomMode
- **Type**: typing.Optional[typing.Literal['AUTO', 'MANUAL']]


# GetDashboardEmbedUrlRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[str]]


# GetDashboardEmbedUrlResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSessionEmbedUrlRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### EntryPoint
- **Type**: typing.Optional[str]

### SessionLifetimeInMinutes
- **Type**: typing.Optional[int]

### UserArn
- **Type**: typing.Optional[str]


# GetSessionEmbedUrlResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GlobalTableBorderOptionsTypeDef

### UniformBorder
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableBorderOptionsTypeDef]

### SideSpecificBorder
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableSideBorderOptionsTypeDef]


# GradientColorOutputTypeDef

### Stops
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.GradientStopTypeDef]]


# GradientColorTypeDef

### Stops
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.GradientStopTypeDef]]


# GradientStopTypeDef

### GradientOffset
- **Type**: <class 'float'>
- **Required**: Yes

### DataValue
- **Type**: typing.Optional[float]

### Color
- **Type**: typing.Optional[str]


# GridLayoutCanvasSizeOptionsTypeDef

### ScreenCanvasSizeOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GridLayoutScreenCanvasSizeOptionsTypeDef]


# GridLayoutConfigurationOutputTypeDef

### Elements
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.GridLayoutElementTypeDef]
- **Required**: Yes

### CanvasSizeOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GridLayoutCanvasSizeOptionsTypeDef]


# GridLayoutConfigurationTypeDef

### Elements
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.GridLayoutElementTypeDef]
- **Required**: Yes

### CanvasSizeOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GridLayoutCanvasSizeOptionsTypeDef]


# GridLayoutElementTypeDef

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


# GridLayoutScreenCanvasSizeOptionsTypeDef

### ResizeOption
- **Type**: typing.Literal['FIXED', 'RESPONSIVE']
- **Required**: Yes

### OptimizedViewPortWidth
- **Type**: typing.Optional[str]


# GroupMemberTypeDef

### Arn
- **Type**: typing.Optional[str]

### MemberName
- **Type**: typing.Optional[str]


# GroupSearchFilterTypeDef

### Operator
- **Type**: typing.Literal['StartsWith']
- **Required**: Yes

### Name
- **Type**: typing.Literal['GROUP_NAME']
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# GroupTypeDef

### Arn
- **Type**: typing.Optional[str]

### GroupName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### PrincipalId
- **Type**: typing.Optional[str]


# GrowthRateComputationTypeDef

### ComputationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Time
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]

### Value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]

### PeriodSize
- **Type**: typing.Optional[int]


# GutterStyleTypeDef

### Show
- **Type**: typing.Optional[bool]


# HeaderFooterSectionConfigurationOutputTypeDef

### SectionId
- **Type**: <class 'str'>
- **Required**: Yes

### Layout
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.SectionLayoutConfigurationOutputTypeDef'>
- **Required**: Yes

### Style
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SectionStyleTypeDef]


# HeaderFooterSectionConfigurationTypeDef

### SectionId
- **Type**: <class 'str'>
- **Required**: Yes

### Layout
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.SectionLayoutConfigurationTypeDef'>
- **Required**: Yes

### Style
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SectionStyleTypeDef]


# HeatMapAggregatedFieldWellsOutputTypeDef

### Rows
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Columns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]


# HeatMapAggregatedFieldWellsTypeDef

### Rows
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Columns
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Values
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]


# HeatMapConfigurationOutputTypeDef

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.HeatMapFieldWellsOutputTypeDef]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.HeatMapSortConfigurationOutputTypeDef]

### RowLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsOutputTypeDef]

### ColumnLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsOutputTypeDef]

### ColorScale
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ColorScaleOutputTypeDef]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LegendOptionsTypeDef]

### DataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataLabelOptionsOutputTypeDef]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TooltipOptionsOutputTypeDef]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# HeatMapConfigurationTypeDef

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.HeatMapFieldWellsTypeDef]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.HeatMapSortConfigurationTypeDef]

### RowLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsTypeDef]

### ColumnLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsTypeDef]

### ColorScale
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ColorScaleTypeDef]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LegendOptionsTypeDef]

### DataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataLabelOptionsTypeDef]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TooltipOptionsTypeDef]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# HeatMapFieldWellsOutputTypeDef

### HeatMapAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.HeatMapAggregatedFieldWellsOutputTypeDef]


# HeatMapFieldWellsTypeDef

### HeatMapAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.HeatMapAggregatedFieldWellsTypeDef]


# HeatMapSortConfigurationOutputTypeDef

### HeatMapRowSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### HeatMapColumnSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### HeatMapRowItemsLimitConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]

### HeatMapColumnItemsLimitConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]


# HeatMapSortConfigurationTypeDef

### HeatMapRowSort
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### HeatMapColumnSort
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### HeatMapRowItemsLimitConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]

### HeatMapColumnItemsLimitConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]


# HeatMapVisualOutputTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.HeatMapConfigurationOutputTypeDef]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ColumnHierarchyOutputTypeDef]]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionOutputTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# HeatMapVisualTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.HeatMapConfigurationTypeDef]

### ColumnHierarchies
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ColumnHierarchyTypeDef]]

### Actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# HistogramAggregatedFieldWellsOutputTypeDef

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]


# HistogramAggregatedFieldWellsTypeDef

### Values
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]


# HistogramBinOptionsTypeDef

### SelectedBinType
- **Type**: typing.Optional[typing.Literal['BIN_COUNT', 'BIN_WIDTH']]

### BinCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BinCountOptionsTypeDef]

### BinWidth
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BinWidthOptionsTypeDef]

### StartValue
- **Type**: typing.Optional[float]


# HistogramConfigurationOutputTypeDef

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.HistogramFieldWellsOutputTypeDef]

### XAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisDisplayOptionsOutputTypeDef]

### XAxisLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsOutputTypeDef]

### YAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisDisplayOptionsOutputTypeDef]

### BinOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.HistogramBinOptionsTypeDef]

### DataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataLabelOptionsOutputTypeDef]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TooltipOptionsOutputTypeDef]

### VisualPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualPaletteOutputTypeDef]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# HistogramConfigurationTypeDef

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.HistogramFieldWellsTypeDef]

### XAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisDisplayOptionsTypeDef]

### XAxisLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsTypeDef]

### YAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisDisplayOptionsTypeDef]

### BinOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.HistogramBinOptionsTypeDef]

### DataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataLabelOptionsTypeDef]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TooltipOptionsTypeDef]

### VisualPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualPaletteTypeDef]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# HistogramFieldWellsOutputTypeDef

### HistogramAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.HistogramAggregatedFieldWellsOutputTypeDef]


# HistogramFieldWellsTypeDef

### HistogramAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.HistogramAggregatedFieldWellsTypeDef]


# HistogramVisualOutputTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.HistogramConfigurationOutputTypeDef]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionOutputTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# HistogramVisualTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.HistogramConfigurationTypeDef]

### Actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# IAMPolicyAssignmentSummaryTypeDef

### AssignmentName
- **Type**: typing.Optional[str]

### AssignmentStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'DRAFT', 'ENABLED']]


# IAMPolicyAssignmentTypeDef

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


# IdentifierTypeDef

### Identity
- **Type**: <class 'str'>
- **Required**: Yes


# IdentityCenterConfigurationTypeDef

### EnableIdentityPropagation
- **Type**: typing.Optional[bool]


# ImageConfigurationTypeDef

### Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ImageSourceTypeDef]


# ImageCustomActionOperationOutputTypeDef

### NavigationOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CustomActionNavigationOperationTypeDef]

### URLOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CustomActionURLOperationTypeDef]

### SetParametersOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CustomActionSetParametersOperationOutputTypeDef]


# ImageCustomActionOperationTypeDef

### NavigationOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CustomActionNavigationOperationTypeDef]

### URLOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CustomActionURLOperationTypeDef]

### SetParametersOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CustomActionSetParametersOperationTypeDef]


# ImageCustomActionOutputTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ImageCustomActionOperationOutputTypeDef]
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# ImageCustomActionTypeDef

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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ImageCustomActionOperationTypeDef]
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# ImageInteractionOptionsTypeDef

### ImageMenuOption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ImageMenuOptionTypeDef]


# ImageMenuOptionTypeDef

### AvailabilityStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# ImageSetConfigurationTypeDef

### Original
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ImageConfigurationTypeDef'>
- **Required**: Yes


# ImageSetTypeDef

### Original
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ImageTypeDef'>
- **Required**: Yes

### Height64
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ImageTypeDef]

### Height32
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ImageTypeDef]


# ImageSourceTypeDef

### PublicUrl
- **Type**: typing.Optional[str]

### S3Uri
- **Type**: typing.Optional[str]


# ImageStaticFileTypeDef

### StaticFileId
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.StaticFileSourceTypeDef]


# ImageTypeDef

### Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ImageSourceTypeDef]

### GeneratedImageUrl
- **Type**: typing.Optional[str]


# IncrementalRefreshTypeDef

### LookbackWindow
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.LookbackWindowTypeDef'>
- **Required**: Yes


# IngestionTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ErrorInfoTypeDef]

### RowInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RowInfoTypeDef]

### QueueInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.QueueInfoTypeDef]

### IngestionTimeInSeconds
- **Type**: typing.Optional[int]

### IngestionSizeInBytes
- **Type**: typing.Optional[int]

### RequestSource
- **Type**: typing.Optional[typing.Literal['MANUAL', 'SCHEDULED']]

### RequestType
- **Type**: typing.Optional[typing.Literal['EDIT', 'FULL_REFRESH', 'INCREMENTAL_REFRESH', 'INITIAL_INGESTION']]


# InnerFilterOutputTypeDef

### CategoryInnerFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CategoryInnerFilterOutputTypeDef]


# InnerFilterTypeDef

### CategoryInnerFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CategoryInnerFilterTypeDef]


# InputColumnTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InsightConfigurationOutputTypeDef

### Computations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ComputationTypeDef]]

### CustomNarrative
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CustomNarrativeOptionsTypeDef]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# InsightConfigurationTypeDef

### Computations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ComputationTypeDef]]

### CustomNarrative
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CustomNarrativeOptionsTypeDef]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# InsightVisualOutputTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### InsightConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.InsightConfigurationOutputTypeDef]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionOutputTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# InsightVisualTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### InsightConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.InsightConfigurationTypeDef]

### Actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# IntegerDatasetParameterDefaultValuesOutputTypeDef

### StaticValues
- **Type**: typing.Optional[typing.List[int]]


# IntegerDatasetParameterDefaultValuesTypeDef

### StaticValues
- **Type**: typing.Optional[typing.Sequence[int]]


# IntegerDatasetParameterDefaultValuesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IntegerDatasetParameterOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.IntegerDatasetParameterDefaultValuesOutputTypeDef]


# IntegerDatasetParameterTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.IntegerDatasetParameterDefaultValuesUnionTypeDef]


# IntegerDatasetParameterUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IntegerDefaultValuesOutputTypeDef

### DynamicValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DynamicDefaultValueTypeDef]

### StaticValues
- **Type**: typing.Optional[typing.List[int]]


# IntegerDefaultValuesTypeDef

### DynamicValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DynamicDefaultValueTypeDef]

### StaticValues
- **Type**: typing.Optional[typing.Sequence[int]]


# IntegerParameterDeclarationOutputTypeDef

### ParameterValueType
- **Type**: typing.Literal['MULTI_VALUED', 'SINGLE_VALUED']
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.IntegerDefaultValuesOutputTypeDef]

### ValueWhenUnset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.IntegerValueWhenUnsetConfigurationTypeDef]

### MappedDataSetParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.MappedDataSetParameterTypeDef]]


# IntegerParameterDeclarationTypeDef

### ParameterValueType
- **Type**: typing.Literal['MULTI_VALUED', 'SINGLE_VALUED']
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.IntegerDefaultValuesTypeDef]

### ValueWhenUnset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.IntegerValueWhenUnsetConfigurationTypeDef]

### MappedDataSetParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.MappedDataSetParameterTypeDef]]


# IntegerParameterOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.List[int]
- **Required**: Yes


# IntegerParameterTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.Sequence[int]
- **Required**: Yes


# IntegerValueWhenUnsetConfigurationTypeDef

### ValueWhenUnsetOption
- **Type**: typing.Optional[typing.Literal['NULL', 'RECOMMENDED_VALUE']]

### CustomValue
- **Type**: typing.Optional[int]


# InvalidTopicReviewedAnswerTypeDef

### AnswerId
- **Type**: typing.Optional[str]

### Error
- **Type**: typing.Optional[typing.Literal['DATASET_DOES_NOT_EXIST', 'DUPLICATED_ANSWER', 'INTERNAL_ERROR', 'INVALID_DATA', 'INVALID_DATASET_ARN', 'MISSING_ANSWER', 'MISSING_REQUIRED_FIELDS']]


# ItemsLimitConfigurationTypeDef

### ItemsLimit
- **Type**: typing.Optional[int]

### OtherCategories
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]


# JiraParametersTypeDef

### SiteBaseUrl
- **Type**: <class 'str'>
- **Required**: Yes


# JoinInstructionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JoinKeyPropertiesTypeDef

### UniqueKey
- **Type**: typing.Optional[bool]


# KPIActualValueConditionalFormattingOutputTypeDef

### TextColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingColorOutputTypeDef]

### Icon
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingIconTypeDef]


# KPIActualValueConditionalFormattingTypeDef

### TextColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingColorTypeDef]

### Icon
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingIconTypeDef]


# KPIComparisonValueConditionalFormattingOutputTypeDef

### TextColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingColorOutputTypeDef]

### Icon
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingIconTypeDef]


# KPIComparisonValueConditionalFormattingTypeDef

### TextColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingColorTypeDef]

### Icon
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingIconTypeDef]


# KPIConditionalFormattingOptionOutputTypeDef

### PrimaryValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.KPIPrimaryValueConditionalFormattingOutputTypeDef]

### ProgressBar
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.KPIProgressBarConditionalFormattingOutputTypeDef]

### ActualValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.KPIActualValueConditionalFormattingOutputTypeDef]

### ComparisonValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.KPIComparisonValueConditionalFormattingOutputTypeDef]


# KPIConditionalFormattingOptionTypeDef

### PrimaryValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.KPIPrimaryValueConditionalFormattingTypeDef]

### ProgressBar
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.KPIProgressBarConditionalFormattingTypeDef]

### ActualValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.KPIActualValueConditionalFormattingTypeDef]

### ComparisonValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.KPIComparisonValueConditionalFormattingTypeDef]


# KPIConditionalFormattingOutputTypeDef

### ConditionalFormattingOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.KPIConditionalFormattingOptionOutputTypeDef]]


# KPIConditionalFormattingTypeDef

### ConditionalFormattingOptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.KPIConditionalFormattingOptionTypeDef]]


# KPIConfigurationOutputTypeDef

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.KPIFieldWellsOutputTypeDef]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.KPISortConfigurationOutputTypeDef]

### KPIOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.KPIOptionsTypeDef]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# KPIConfigurationTypeDef

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.KPIFieldWellsTypeDef]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.KPISortConfigurationTypeDef]

### KPIOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.KPIOptionsTypeDef]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# KPIFieldWellsOutputTypeDef

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]

### TargetValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]

### TrendGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]


# KPIFieldWellsTypeDef

### Values
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]

### TargetValues
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]

### TrendGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]


# KPIOptionsTypeDef

### ProgressBar
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ProgressBarOptionsTypeDef]

### TrendArrows
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TrendArrowOptionsTypeDef]

### SecondaryValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SecondaryValueOptionsTypeDef]

### Comparison
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ComparisonConfigurationTypeDef]

### PrimaryValueDisplayType
- **Type**: typing.Optional[typing.Literal['ACTUAL', 'COMPARISON', 'HIDDEN']]

### PrimaryValueFontConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FontConfigurationTypeDef]

### SecondaryValueFontConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FontConfigurationTypeDef]

### Sparkline
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.KPISparklineOptionsTypeDef]

### VisualLayoutOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.KPIVisualLayoutOptionsTypeDef]


# KPIPrimaryValueConditionalFormattingOutputTypeDef

### TextColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingColorOutputTypeDef]

### Icon
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingIconTypeDef]


# KPIPrimaryValueConditionalFormattingTypeDef

### TextColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingColorTypeDef]

### Icon
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingIconTypeDef]


# KPIProgressBarConditionalFormattingOutputTypeDef

### ForegroundColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingColorOutputTypeDef]


# KPIProgressBarConditionalFormattingTypeDef

### ForegroundColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingColorTypeDef]


# KPISortConfigurationOutputTypeDef

### TrendGroupSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]


# KPISortConfigurationTypeDef

### TrendGroupSort
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]


# KPISparklineOptionsTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KPIVisualLayoutOptionsTypeDef

### StandardLayout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.KPIVisualStandardLayoutTypeDef]


# KPIVisualOutputTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.KPIConfigurationOutputTypeDef]

### ConditionalFormatting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.KPIConditionalFormattingOutputTypeDef]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionOutputTypeDef]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ColumnHierarchyOutputTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# KPIVisualStandardLayoutTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KPIVisualTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.KPIConfigurationTypeDef]

### ConditionalFormatting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.KPIConditionalFormattingTypeDef]

### Actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionTypeDef]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ColumnHierarchyTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# LabelOptionsTypeDef

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### FontConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FontConfigurationTypeDef]

### CustomLabel
- **Type**: typing.Optional[str]


# LayerCustomActionOperationOutputTypeDef

### FilterOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CustomActionFilterOperationOutputTypeDef]

### NavigationOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CustomActionNavigationOperationTypeDef]

### URLOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CustomActionURLOperationTypeDef]

### SetParametersOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CustomActionSetParametersOperationOutputTypeDef]


# LayerCustomActionOperationTypeDef

### FilterOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CustomActionFilterOperationTypeDef]

### NavigationOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CustomActionNavigationOperationTypeDef]

### URLOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CustomActionURLOperationTypeDef]

### SetParametersOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CustomActionSetParametersOperationTypeDef]


# LayerCustomActionOutputTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.LayerCustomActionOperationOutputTypeDef]
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# LayerCustomActionTypeDef

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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.LayerCustomActionOperationTypeDef]
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# LayerMapVisualOutputTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialLayerMapConfigurationOutputTypeDef]

### VisualContentAltText
- **Type**: typing.Optional[str]


# LayerMapVisualTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialLayerMapConfigurationTypeDef]

### VisualContentAltText
- **Type**: typing.Optional[str]


# LayoutConfigurationOutputTypeDef

### GridLayout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GridLayoutConfigurationOutputTypeDef]

### FreeFormLayout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FreeFormLayoutConfigurationOutputTypeDef]

### SectionBasedLayout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SectionBasedLayoutConfigurationOutputTypeDef]


# LayoutConfigurationTypeDef

### GridLayout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GridLayoutConfigurationTypeDef]

### FreeFormLayout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FreeFormLayoutConfigurationTypeDef]

### SectionBasedLayout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SectionBasedLayoutConfigurationTypeDef]


# LayoutOutputTypeDef

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.LayoutConfigurationOutputTypeDef'>
- **Required**: Yes


# LayoutTypeDef

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.LayoutConfigurationTypeDef'>
- **Required**: Yes


# LegendOptionsTypeDef

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LabelOptionsTypeDef]

### Position
- **Type**: typing.Optional[typing.Literal['AUTO', 'BOTTOM', 'RIGHT', 'TOP']]

### Width
- **Type**: typing.Optional[str]

### Height
- **Type**: typing.Optional[str]

### ValueFontConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FontConfigurationTypeDef]


# LineChartAggregatedFieldWellsOutputTypeDef

### Category
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]

### Colors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### SmallMultiples
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]


# LineChartAggregatedFieldWellsTypeDef

### Category
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Values
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]

### Colors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### SmallMultiples
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]


# LineChartConfigurationOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LineChartConfigurationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LineChartDefaultSeriesSettingsTypeDef

### AxisBinding
- **Type**: typing.Optional[typing.Literal['PRIMARY_YAXIS', 'SECONDARY_YAXIS']]

### LineStyleSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LineChartLineStyleSettingsTypeDef]

### MarkerStyleSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LineChartMarkerStyleSettingsTypeDef]


# LineChartFieldWellsOutputTypeDef

### LineChartAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LineChartAggregatedFieldWellsOutputTypeDef]


# LineChartFieldWellsTypeDef

### LineChartAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LineChartAggregatedFieldWellsTypeDef]


# LineChartLineStyleSettingsTypeDef

### LineVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### LineInterpolation
- **Type**: typing.Optional[typing.Literal['LINEAR', 'SMOOTH', 'STEPPED']]

### LineStyle
- **Type**: typing.Optional[typing.Literal['DASHED', 'DOTTED', 'SOLID']]

### LineWidth
- **Type**: typing.Optional[str]


# LineChartMarkerStyleSettingsTypeDef

### MarkerVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### MarkerShape
- **Type**: typing.Optional[typing.Literal['CIRCLE', 'DIAMOND', 'ROUNDED_SQUARE', 'SQUARE', 'TRIANGLE']]

### MarkerSize
- **Type**: typing.Optional[str]

### MarkerColor
- **Type**: typing.Optional[str]


# LineChartSeriesSettingsTypeDef

### LineStyleSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LineChartLineStyleSettingsTypeDef]

### MarkerStyleSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LineChartMarkerStyleSettingsTypeDef]


# LineChartSortConfigurationOutputTypeDef

### CategorySort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### CategoryItemsLimitConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]

### ColorItemsLimitConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]

### SmallMultiplesSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### SmallMultiplesLimitConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]


# LineChartSortConfigurationTypeDef

### CategorySort
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### CategoryItemsLimitConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]

### ColorItemsLimitConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]

### SmallMultiplesSort
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### SmallMultiplesLimitConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]


# LineChartVisualOutputTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LineChartConfigurationOutputTypeDef]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionOutputTypeDef]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ColumnHierarchyOutputTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# LineChartVisualTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LineChartConfigurationTypeDef]

### Actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionTypeDef]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ColumnHierarchyTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# LineSeriesAxisDisplayOptionsOutputTypeDef

### AxisOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisDisplayOptionsOutputTypeDef]

### MissingDataConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.MissingDataConfigurationTypeDef]]


# LineSeriesAxisDisplayOptionsTypeDef

### AxisOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisDisplayOptionsTypeDef]

### MissingDataConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.MissingDataConfigurationTypeDef]]


# LinkSharingConfigurationOutputTypeDef

### Permissions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionOutputTypeDef]]


# LinkSharingConfigurationTypeDef

### Permissions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionTypeDef]]


# LinkSharingConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListAnalysesRequestPaginateTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaginatorConfigTypeDef]


# ListAnalysesRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAnalysesResponseTypeDef

### AnalysisSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AnalysisSummaryTypeDef]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAssetBundleExportJobsRequestPaginateTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaginatorConfigTypeDef]


# ListAssetBundleExportJobsRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAssetBundleExportJobsResponseTypeDef

### AssetBundleExportJobSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleExportJobSummaryTypeDef]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAssetBundleImportJobsRequestPaginateTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaginatorConfigTypeDef]


# ListAssetBundleImportJobsRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAssetBundleImportJobsResponseTypeDef

### AssetBundleImportJobSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobSummaryTypeDef]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListBrandsRequestPaginateTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaginatorConfigTypeDef]


# ListBrandsRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListBrandsResponseTypeDef

### Brands
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.BrandSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListControlDisplayOptionsTypeDef

### SearchOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ListControlSearchOptionsTypeDef]

### SelectAllOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ListControlSelectAllOptionsTypeDef]

### TitleOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LabelOptionsTypeDef]

### InfoIconLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SheetControlInfoIconLabelOptionsTypeDef]


# ListControlSearchOptionsTypeDef

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# ListControlSelectAllOptionsTypeDef

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# ListCustomPermissionsRequestPaginateTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaginatorConfigTypeDef]


# ListCustomPermissionsRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCustomPermissionsResponseTypeDef

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### CustomPermissionsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.CustomPermissionsTypeDef]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDashboardVersionsRequestPaginateTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaginatorConfigTypeDef]


# ListDashboardVersionsRequestTypeDef

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


# ListDashboardVersionsResponseTypeDef

### DashboardVersionSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DashboardVersionSummaryTypeDef]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDashboardsRequestPaginateTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaginatorConfigTypeDef]


# ListDashboardsRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDashboardsResponseTypeDef

### DashboardSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DashboardSummaryTypeDef]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDataSetsRequestPaginateTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaginatorConfigTypeDef]


# ListDataSetsRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDataSetsResponseTypeDef

### DataSetSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DataSetSummaryTypeDef]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDataSourcesRequestPaginateTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaginatorConfigTypeDef]


# ListDataSourcesRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDataSourcesResponseTypeDef

### DataSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DataSourceTypeDef]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFolderMembersRequestPaginateTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaginatorConfigTypeDef]


# ListFolderMembersRequestTypeDef

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


# ListFolderMembersResponseTypeDef

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### FolderMemberList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.MemberIdArnPairTypeDef]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFoldersForResourceRequestPaginateTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaginatorConfigTypeDef]


# ListFoldersForResourceRequestTypeDef

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


# ListFoldersForResourceResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFoldersRequestPaginateTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaginatorConfigTypeDef]


# ListFoldersRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListFoldersResponseTypeDef

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### FolderSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.FolderSummaryTypeDef]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGroupMembershipsRequestPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaginatorConfigTypeDef]


# ListGroupMembershipsRequestTypeDef

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


# ListGroupMembershipsResponseTypeDef

### GroupMemberList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.GroupMemberTypeDef]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGroupsRequestPaginateTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaginatorConfigTypeDef]


# ListGroupsRequestTypeDef

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


# ListGroupsResponseTypeDef

### GroupList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.GroupTypeDef]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIAMPolicyAssignmentsForUserRequestPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaginatorConfigTypeDef]


# ListIAMPolicyAssignmentsForUserRequestTypeDef

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


# ListIAMPolicyAssignmentsForUserResponseTypeDef

### ActiveAssignments
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ActiveIAMPolicyAssignmentTypeDef]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIAMPolicyAssignmentsRequestPaginateTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### AssignmentStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'DRAFT', 'ENABLED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaginatorConfigTypeDef]


# ListIAMPolicyAssignmentsRequestTypeDef

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


# ListIAMPolicyAssignmentsResponseTypeDef

### IAMPolicyAssignments
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.IAMPolicyAssignmentSummaryTypeDef]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIdentityPropagationConfigsRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListIdentityPropagationConfigsResponseTypeDef

### Services
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AuthorizedTargetsByServiceTypeDef]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIngestionsRequestPaginateTypeDef

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaginatorConfigTypeDef]


# ListIngestionsRequestTypeDef

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


# ListIngestionsResponseTypeDef

### Ingestions
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.IngestionTypeDef]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNamespacesRequestPaginateTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaginatorConfigTypeDef]


# ListNamespacesRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListNamespacesResponseTypeDef

### Namespaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.NamespaceInfoV2TypeDef]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRefreshSchedulesRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes


# ListRefreshSchedulesResponseTypeDef

### RefreshSchedules
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.RefreshScheduleOutputTypeDef]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRoleMembershipsRequestPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaginatorConfigTypeDef]


# ListRoleMembershipsRequestTypeDef

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


# ListRoleMembershipsResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.TagTypeDef]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTemplateAliasesRequestPaginateTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaginatorConfigTypeDef]


# ListTemplateAliasesRequestTypeDef

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


# ListTemplateAliasesResponseTypeDef

### TemplateAliasList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.TemplateAliasTypeDef]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTemplateVersionsRequestPaginateTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaginatorConfigTypeDef]


# ListTemplateVersionsRequestTypeDef

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


# ListTemplateVersionsResponseTypeDef

### TemplateVersionSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.TemplateVersionSummaryTypeDef]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTemplatesRequestPaginateTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaginatorConfigTypeDef]


# ListTemplatesRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTemplatesResponseTypeDef

### TemplateSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.TemplateSummaryTypeDef]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListThemeAliasesRequestTypeDef

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


# ListThemeAliasesResponseTypeDef

### ThemeAliasList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ThemeAliasTypeDef]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListThemeVersionsRequestPaginateTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ThemeId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaginatorConfigTypeDef]


# ListThemeVersionsRequestTypeDef

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


# ListThemeVersionsResponseTypeDef

### ThemeVersionSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ThemeVersionSummaryTypeDef]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListThemesResponseTypeDef

### ThemeSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ThemeSummaryTypeDef]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTopicRefreshSchedulesRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes


# ListTopicRefreshSchedulesResponseTypeDef

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### RefreshSchedules
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.TopicRefreshScheduleSummaryTypeDef]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTopicReviewedAnswersRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes


# ListTopicReviewedAnswersResponseTypeDef

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### Answers
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.TopicReviewedAnswerTypeDef]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTopicsRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTopicsResponseTypeDef

### TopicsSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.TopicSummaryTypeDef]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListUserGroupsRequestPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaginatorConfigTypeDef]


# ListUserGroupsRequestTypeDef

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


# ListUserGroupsResponseTypeDef

### GroupList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.GroupTypeDef]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListUsersRequestPaginateTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaginatorConfigTypeDef]


# ListUsersRequestTypeDef

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


# ListUsersResponseTypeDef

### UserList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.UserTypeDef]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListVPCConnectionsRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListVPCConnectionsResponseTypeDef

### VPCConnectionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.VPCConnectionSummaryTypeDef]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LoadingAnimationTypeDef

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# LocalNavigationConfigurationTypeDef

### TargetSheetId
- **Type**: <class 'str'>
- **Required**: Yes


# LogicalTableOutputTypeDef

### Alias
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.LogicalTableSourceTypeDef'>
- **Required**: Yes

### DataTransforms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.TransformOperationOutputTypeDef]]


# LogicalTableSourceTypeDef

### JoinInstruction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.JoinInstructionTypeDef]

### PhysicalTableId
- **Type**: typing.Optional[str]

### DataSetArn
- **Type**: typing.Optional[str]


# LogicalTableTypeDef

### Alias
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.LogicalTableSourceTypeDef'>
- **Required**: Yes

### DataTransforms
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TransformOperationUnionTypeDef]]


# LogicalTableUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LogoConfigurationTypeDef

### AltText
- **Type**: <class 'str'>
- **Required**: Yes

### LogoSet
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.LogoSetConfigurationTypeDef'>
- **Required**: Yes


# LogoSetConfigurationTypeDef

### Primary
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ImageSetConfigurationTypeDef'>
- **Required**: Yes

### Favicon
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ImageSetConfigurationTypeDef]


# LogoSetTypeDef

### Primary
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ImageSetTypeDef'>
- **Required**: Yes

### Favicon
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ImageSetTypeDef]


# LogoTypeDef

### AltText
- **Type**: <class 'str'>
- **Required**: Yes

### LogoSet
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.LogoSetTypeDef'>
- **Required**: Yes


# LongFormatTextTypeDef

### PlainText
- **Type**: typing.Optional[str]

### RichText
- **Type**: typing.Optional[str]


# LookbackWindowTypeDef

### ColumnName
- **Type**: <class 'str'>
- **Required**: Yes

### Size
- **Type**: <class 'int'>
- **Required**: Yes

### SizeUnit
- **Type**: typing.Literal['DAY', 'HOUR', 'WEEK']
- **Required**: Yes


# ManifestFileLocationTypeDef

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Key
- **Type**: <class 'str'>
- **Required**: Yes


# MappedDataSetParameterTypeDef

### DataSetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetParameterName
- **Type**: <class 'str'>
- **Required**: Yes


# MarginStyleTypeDef

### Show
- **Type**: typing.Optional[bool]


# MariaDbParametersTypeDef

### Host
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes


# MaximumLabelTypeTypeDef

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# MaximumMinimumComputationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MeasureFieldTypeDef

### NumericalMeasureField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NumericalMeasureFieldTypeDef]

### CategoricalMeasureField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CategoricalMeasureFieldTypeDef]

### DateMeasureField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DateMeasureFieldTypeDef]

### CalculatedMeasureField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CalculatedMeasureFieldTypeDef]


# MemberIdArnPairTypeDef

### MemberId
- **Type**: typing.Optional[str]

### MemberArn
- **Type**: typing.Optional[str]


# MetricComparisonComputationTypeDef

### ComputationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Time
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]

### FromValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]

### TargetValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]


# MinimumLabelTypeTypeDef

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# MissingDataConfigurationTypeDef

### TreatmentOption
- **Type**: typing.Optional[typing.Literal['INTERPOLATE', 'SHOW_AS_BLANK', 'SHOW_AS_ZERO']]


# MySqlParametersTypeDef

### Host
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes


# NamedEntityDefinitionMetricOutputTypeDef

### Aggregation
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'COUNT', 'CUSTOM', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'PERCENTILE', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]

### AggregationFunctionParameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# NamedEntityDefinitionMetricTypeDef

### Aggregation
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'COUNT', 'CUSTOM', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'PERCENTILE', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]

### AggregationFunctionParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# NamedEntityDefinitionOutputTypeDef

### FieldName
- **Type**: typing.Optional[str]

### PropertyName
- **Type**: typing.Optional[str]

### PropertyRole
- **Type**: typing.Optional[typing.Literal['ID', 'PRIMARY']]

### PropertyUsage
- **Type**: typing.Optional[typing.Literal['DIMENSION', 'INHERIT', 'MEASURE']]

### Metric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NamedEntityDefinitionMetricOutputTypeDef]


# NamedEntityDefinitionTypeDef

### FieldName
- **Type**: typing.Optional[str]

### PropertyName
- **Type**: typing.Optional[str]

### PropertyRole
- **Type**: typing.Optional[typing.Literal['ID', 'PRIMARY']]

### PropertyUsage
- **Type**: typing.Optional[typing.Literal['DIMENSION', 'INHERIT', 'MEASURE']]

### Metric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NamedEntityDefinitionMetricTypeDef]


# NamedEntityRefTypeDef

### NamedEntityName
- **Type**: typing.Optional[str]


# NamespaceErrorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NamespaceInfoV2TypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NamespaceErrorTypeDef]

### IamIdentityCenterApplicationArn
- **Type**: typing.Optional[str]

### IamIdentityCenterInstanceArn
- **Type**: typing.Optional[str]


# NavbarStyleTypeDef

### GlobalNavbar
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaletteTypeDef]

### ContextualNavbar
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaletteTypeDef]


# NegativeFormatTypeDef

### Prefix
- **Type**: typing.Optional[str]

### Suffix
- **Type**: typing.Optional[str]


# NegativeValueConfigurationTypeDef

### DisplayMode
- **Type**: typing.Literal['NEGATIVE', 'POSITIVE']
- **Required**: Yes


# NestedFilterOutputTypeDef

### FilterId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes

### IncludeInnerSet
- **Type**: <class 'bool'>
- **Required**: Yes

### InnerFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.InnerFilterOutputTypeDef'>
- **Required**: Yes


# NestedFilterTypeDef

### FilterId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes

### IncludeInnerSet
- **Type**: <class 'bool'>
- **Required**: Yes

### InnerFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.InnerFilterTypeDef'>
- **Required**: Yes


# NetworkInterfaceTypeDef

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


# NewDefaultValuesOutputTypeDef

### StringStaticValues
- **Type**: typing.Optional[typing.List[str]]

### DecimalStaticValues
- **Type**: typing.Optional[typing.List[float]]

### DateTimeStaticValues
- **Type**: typing.Optional[typing.List[datetime.datetime]]

### IntegerStaticValues
- **Type**: typing.Optional[typing.List[int]]


# NewDefaultValuesTypeDef

### StringStaticValues
- **Type**: typing.Optional[typing.Sequence[str]]

### DecimalStaticValues
- **Type**: typing.Optional[typing.Sequence[float]]

### DateTimeStaticValues
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TimestampTypeDef]]

### IntegerStaticValues
- **Type**: typing.Optional[typing.Sequence[int]]


# NewDefaultValuesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NullValueFormatConfigurationTypeDef

### NullString
- **Type**: <class 'str'>
- **Required**: Yes


# NumberDisplayFormatConfigurationTypeDef

### Prefix
- **Type**: typing.Optional[str]

### Suffix
- **Type**: typing.Optional[str]

### SeparatorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NumericSeparatorConfigurationTypeDef]

### DecimalPlacesConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DecimalPlacesConfigurationTypeDef]

### NumberScale
- **Type**: typing.Optional[typing.Literal['AUTO', 'BILLIONS', 'CRORES', 'LAKHS', 'MILLIONS', 'NONE', 'THOUSANDS', 'TRILLIONS']]

### NegativeValueConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NegativeValueConfigurationTypeDef]

### NullValueFormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NullValueFormatConfigurationTypeDef]


# NumberFormatConfigurationTypeDef

### FormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NumericFormatConfigurationTypeDef]


# NumericAxisOptionsOutputTypeDef

### Scale
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisScaleTypeDef]

### Range
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisDisplayRangeOutputTypeDef]


# NumericAxisOptionsTypeDef

### Scale
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisScaleTypeDef]

### Range
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisDisplayRangeTypeDef]


# NumericEqualityDrillDownFilterTypeDef

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes

### Value
- **Type**: <class 'float'>
- **Required**: Yes


# NumericEqualityFilterOutputTypeDef

### FilterId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AggregationFunctionTypeDef]

### ParameterName
- **Type**: typing.Optional[str]

### DefaultFilterControlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultFilterControlConfigurationOutputTypeDef]


# NumericEqualityFilterTypeDef

### FilterId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AggregationFunctionTypeDef]

### ParameterName
- **Type**: typing.Optional[str]

### DefaultFilterControlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultFilterControlConfigurationTypeDef]


# NumericFormatConfigurationTypeDef

### NumberDisplayFormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NumberDisplayFormatConfigurationTypeDef]

### CurrencyDisplayFormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CurrencyDisplayFormatConfigurationTypeDef]

### PercentageDisplayFormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PercentageDisplayFormatConfigurationTypeDef]


# NumericRangeFilterOutputTypeDef

### FilterId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes

### NullOption
- **Type**: typing.Literal['ALL_VALUES', 'NON_NULLS_ONLY', 'NULLS_ONLY']
- **Required**: Yes

### IncludeMinimum
- **Type**: typing.Optional[bool]

### IncludeMaximum
- **Type**: typing.Optional[bool]

### RangeMinimum
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NumericRangeFilterValueTypeDef]

### RangeMaximum
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NumericRangeFilterValueTypeDef]

### SelectAllOptions
- **Type**: typing.Optional[typing.Literal['FILTER_ALL_VALUES']]

### AggregationFunction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AggregationFunctionTypeDef]

### DefaultFilterControlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultFilterControlConfigurationOutputTypeDef]


# NumericRangeFilterTypeDef

### FilterId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes

### NullOption
- **Type**: typing.Literal['ALL_VALUES', 'NON_NULLS_ONLY', 'NULLS_ONLY']
- **Required**: Yes

### IncludeMinimum
- **Type**: typing.Optional[bool]

### IncludeMaximum
- **Type**: typing.Optional[bool]

### RangeMinimum
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NumericRangeFilterValueTypeDef]

### RangeMaximum
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NumericRangeFilterValueTypeDef]

### SelectAllOptions
- **Type**: typing.Optional[typing.Literal['FILTER_ALL_VALUES']]

### AggregationFunction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AggregationFunctionTypeDef]

### DefaultFilterControlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultFilterControlConfigurationTypeDef]


# NumericRangeFilterValueTypeDef

### StaticValue
- **Type**: typing.Optional[float]

### Parameter
- **Type**: typing.Optional[str]


# NumericSeparatorConfigurationTypeDef

### DecimalSeparator
- **Type**: typing.Optional[typing.Literal['COMMA', 'DOT', 'SPACE']]

### ThousandsSeparator
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ThousandSeparatorOptionsTypeDef]


# NumericalAggregationFunctionTypeDef

### SimpleNumericalAggregation
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'COUNT', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]

### PercentileAggregation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PercentileAggregationTypeDef]


# NumericalDimensionFieldTypeDef

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes

### HierarchyId
- **Type**: typing.Optional[str]

### FormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NumberFormatConfigurationTypeDef]


# NumericalMeasureFieldTypeDef

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes

### AggregationFunction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NumericalAggregationFunctionTypeDef]

### FormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NumberFormatConfigurationTypeDef]


# OAuthParametersTypeDef

### TokenProviderUrl
- **Type**: <class 'str'>
- **Required**: Yes

### OAuthScope
- **Type**: typing.Optional[str]

### IdentityProviderVpcConnectionProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VpcConnectionPropertiesTypeDef]

### IdentityProviderResourceUri
- **Type**: typing.Optional[str]


# OracleParametersTypeDef

### Host
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes


# OutputColumnTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OverrideDatasetParameterOperationOutputTypeDef

### ParameterName
- **Type**: <class 'str'>
- **Required**: Yes

### NewParameterName
- **Type**: typing.Optional[str]

### NewDefaultValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NewDefaultValuesOutputTypeDef]


# OverrideDatasetParameterOperationTypeDef

### ParameterName
- **Type**: <class 'str'>
- **Required**: Yes

### NewParameterName
- **Type**: typing.Optional[str]

### NewDefaultValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NewDefaultValuesUnionTypeDef]


# OverrideDatasetParameterOperationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PaginationConfigurationTypeDef

### PageSize
- **Type**: <class 'int'>
- **Required**: Yes

### PageNumber
- **Type**: <class 'int'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PaletteTypeDef

### Foreground
- **Type**: typing.Optional[str]

### Background
- **Type**: typing.Optional[str]


# PanelConfigurationTypeDef

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PanelTitleOptionsTypeDef]

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


# PanelTitleOptionsTypeDef

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### FontConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FontConfigurationTypeDef]

### HorizontalTextAlignment
- **Type**: typing.Optional[typing.Literal['AUTO', 'CENTER', 'LEFT', 'RIGHT']]


# ParameterControlOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ParameterControlTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ParameterDateTimePickerControlTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DateTimePickerControlDisplayOptionsTypeDef]


# ParameterDeclarationOutputTypeDef

### StringParameterDeclaration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.StringParameterDeclarationOutputTypeDef]

### DecimalParameterDeclaration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DecimalParameterDeclarationOutputTypeDef]

### IntegerParameterDeclaration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.IntegerParameterDeclarationOutputTypeDef]

### DateTimeParameterDeclaration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DateTimeParameterDeclarationOutputTypeDef]


# ParameterDeclarationTypeDef

### StringParameterDeclaration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.StringParameterDeclarationTypeDef]

### DecimalParameterDeclaration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DecimalParameterDeclarationTypeDef]

### IntegerParameterDeclaration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.IntegerParameterDeclarationTypeDef]

### DateTimeParameterDeclaration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DateTimeParameterDeclarationTypeDef]


# ParameterSelectableValuesOutputTypeDef

### Values
- **Type**: typing.Optional[typing.List[str]]

### LinkToDataSetColumn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef]


# ParameterSelectableValuesTypeDef

### Values
- **Type**: typing.Optional[typing.Sequence[str]]

### LinkToDataSetColumn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef]


# ParameterSliderControlTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SliderControlDisplayOptionsTypeDef]


# ParameterTextAreaControlTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TextAreaControlDisplayOptionsTypeDef]


# ParameterTextFieldControlTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TextFieldControlDisplayOptionsTypeDef]


# ParametersOutputTypeDef

### StringParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.StringParameterOutputTypeDef]]

### IntegerParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.IntegerParameterOutputTypeDef]]

### DecimalParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DecimalParameterOutputTypeDef]]

### DateTimeParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DateTimeParameterOutputTypeDef]]


# ParametersTypeDef

### StringParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.StringParameterTypeDef]]

### IntegerParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.IntegerParameterTypeDef]]

### DecimalParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DecimalParameterTypeDef]]

### DateTimeParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DateTimeParameterTypeDef]]


# ParametersUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PercentVisibleRangeTypeDef

### From
- **Type**: typing.Optional[float]

### To
- **Type**: typing.Optional[float]


# PercentageDisplayFormatConfigurationTypeDef

### Prefix
- **Type**: typing.Optional[str]

### Suffix
- **Type**: typing.Optional[str]

### SeparatorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NumericSeparatorConfigurationTypeDef]

### DecimalPlacesConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DecimalPlacesConfigurationTypeDef]

### NegativeValueConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NegativeValueConfigurationTypeDef]

### NullValueFormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NullValueFormatConfigurationTypeDef]


# PercentileAggregationTypeDef

### PercentileValue
- **Type**: typing.Optional[float]


# PerformanceConfigurationOutputTypeDef

### UniqueKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.UniqueKeyOutputTypeDef]]


# PerformanceConfigurationTypeDef

### UniqueKeys
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.UniqueKeyTypeDef]]


# PerformanceConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PeriodOverPeriodComputationTypeDef

### ComputationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Time
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]

### Value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]


# PeriodToDateComputationTypeDef

### ComputationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Time
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]

### Value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]

### PeriodTimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]


# PhysicalTableOutputTypeDef

### RelationalTable
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RelationalTableOutputTypeDef]

### CustomSql
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CustomSqlOutputTypeDef]

### S3Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.S3SourceOutputTypeDef]


# PhysicalTableTypeDef

### RelationalTable
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RelationalTableUnionTypeDef]

### CustomSql
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CustomSqlUnionTypeDef]

### S3Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.S3SourceUnionTypeDef]


# PhysicalTableUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PieChartAggregatedFieldWellsOutputTypeDef

### Category
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]

### SmallMultiples
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]


# PieChartAggregatedFieldWellsTypeDef

### Category
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Values
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]

### SmallMultiples
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]


# PieChartConfigurationOutputTypeDef

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PieChartFieldWellsOutputTypeDef]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PieChartSortConfigurationOutputTypeDef]

### DonutOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DonutOptionsTypeDef]

### SmallMultiplesOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SmallMultiplesOptionsTypeDef]

### CategoryLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsOutputTypeDef]

### ValueLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsOutputTypeDef]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LegendOptionsTypeDef]

### DataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataLabelOptionsOutputTypeDef]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TooltipOptionsOutputTypeDef]

### VisualPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualPaletteOutputTypeDef]

### ContributionAnalysisDefaults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ContributionAnalysisDefaultOutputTypeDef]]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# PieChartConfigurationTypeDef

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PieChartFieldWellsTypeDef]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PieChartSortConfigurationTypeDef]

### DonutOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DonutOptionsTypeDef]

### SmallMultiplesOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SmallMultiplesOptionsTypeDef]

### CategoryLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsTypeDef]

### ValueLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsTypeDef]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LegendOptionsTypeDef]

### DataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataLabelOptionsTypeDef]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TooltipOptionsTypeDef]

### VisualPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualPaletteTypeDef]

### ContributionAnalysisDefaults
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ContributionAnalysisDefaultTypeDef]]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# PieChartFieldWellsOutputTypeDef

### PieChartAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PieChartAggregatedFieldWellsOutputTypeDef]


# PieChartFieldWellsTypeDef

### PieChartAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PieChartAggregatedFieldWellsTypeDef]


# PieChartSortConfigurationOutputTypeDef

### CategorySort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### CategoryItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]

### SmallMultiplesSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### SmallMultiplesLimitConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]


# PieChartSortConfigurationTypeDef

### CategorySort
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### CategoryItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]

### SmallMultiplesSort
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### SmallMultiplesLimitConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]


# PieChartVisualOutputTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PieChartConfigurationOutputTypeDef]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionOutputTypeDef]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ColumnHierarchyOutputTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# PieChartVisualTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PieChartConfigurationTypeDef]

### Actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionTypeDef]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ColumnHierarchyTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# PivotFieldSortOptionsOutputTypeDef

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### SortBy
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.PivotTableSortByOutputTypeDef'>
- **Required**: Yes


# PivotFieldSortOptionsTypeDef

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### SortBy
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.PivotTableSortByTypeDef'>
- **Required**: Yes


# PivotTableAggregatedFieldWellsOutputTypeDef

### Rows
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Columns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]


# PivotTableAggregatedFieldWellsTypeDef

### Rows
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Columns
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Values
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]


# PivotTableCellConditionalFormattingOutputTypeDef

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### TextFormat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TextConditionalFormatOutputTypeDef]

### Scope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PivotTableConditionalFormattingScopeTypeDef]

### Scopes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.PivotTableConditionalFormattingScopeTypeDef]]


# PivotTableCellConditionalFormattingTypeDef

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### TextFormat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TextConditionalFormatTypeDef]

### Scope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PivotTableConditionalFormattingScopeTypeDef]

### Scopes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.PivotTableConditionalFormattingScopeTypeDef]]


# PivotTableConditionalFormattingOptionOutputTypeDef

### Cell
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PivotTableCellConditionalFormattingOutputTypeDef]


# PivotTableConditionalFormattingOptionTypeDef

### Cell
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PivotTableCellConditionalFormattingTypeDef]


# PivotTableConditionalFormattingOutputTypeDef

### ConditionalFormattingOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.PivotTableConditionalFormattingOptionOutputTypeDef]]


# PivotTableConditionalFormattingScopeTypeDef

### Role
- **Type**: typing.Optional[typing.Literal['FIELD', 'FIELD_TOTAL', 'GRAND_TOTAL']]


# PivotTableConditionalFormattingTypeDef

### ConditionalFormattingOptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.PivotTableConditionalFormattingOptionTypeDef]]


# PivotTableConfigurationOutputTypeDef

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PivotTableFieldWellsOutputTypeDef]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PivotTableSortConfigurationOutputTypeDef]

### TableOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PivotTableOptionsOutputTypeDef]

### TotalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PivotTableTotalOptionsOutputTypeDef]

### FieldOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PivotTableFieldOptionsOutputTypeDef]

### PaginatedReportOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PivotTablePaginatedReportOptionsTypeDef]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# PivotTableConfigurationTypeDef

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PivotTableFieldWellsTypeDef]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PivotTableSortConfigurationTypeDef]

### TableOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PivotTableOptionsTypeDef]

### TotalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PivotTableTotalOptionsTypeDef]

### FieldOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PivotTableFieldOptionsTypeDef]

### PaginatedReportOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PivotTablePaginatedReportOptionsTypeDef]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# PivotTableDataPathOptionOutputTypeDef

### DataPathList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DataPathValueTypeDef]
- **Required**: Yes

### Width
- **Type**: typing.Optional[str]


# PivotTableDataPathOptionTypeDef

### DataPathList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DataPathValueTypeDef]
- **Required**: Yes

### Width
- **Type**: typing.Optional[str]


# PivotTableFieldCollapseStateOptionOutputTypeDef

### Target
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.PivotTableFieldCollapseStateTargetOutputTypeDef'>
- **Required**: Yes

### State
- **Type**: typing.Optional[typing.Literal['COLLAPSED', 'EXPANDED']]


# PivotTableFieldCollapseStateOptionTypeDef

### Target
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.PivotTableFieldCollapseStateTargetTypeDef'>
- **Required**: Yes

### State
- **Type**: typing.Optional[typing.Literal['COLLAPSED', 'EXPANDED']]


# PivotTableFieldCollapseStateTargetOutputTypeDef

### FieldId
- **Type**: typing.Optional[str]

### FieldDataPathValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DataPathValueTypeDef]]


# PivotTableFieldCollapseStateTargetTypeDef

### FieldId
- **Type**: typing.Optional[str]

### FieldDataPathValues
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DataPathValueTypeDef]]


# PivotTableFieldOptionTypeDef

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### CustomLabel
- **Type**: typing.Optional[str]

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# PivotTableFieldOptionsOutputTypeDef

### SelectedFieldOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.PivotTableFieldOptionTypeDef]]

### DataPathOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.PivotTableDataPathOptionOutputTypeDef]]

### CollapseStateOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.PivotTableFieldCollapseStateOptionOutputTypeDef]]


# PivotTableFieldOptionsTypeDef

### SelectedFieldOptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.PivotTableFieldOptionTypeDef]]

### DataPathOptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.PivotTableDataPathOptionTypeDef]]

### CollapseStateOptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.PivotTableFieldCollapseStateOptionTypeDef]]


# PivotTableFieldSubtotalOptionsTypeDef

### FieldId
- **Type**: typing.Optional[str]


# PivotTableFieldWellsOutputTypeDef

### PivotTableAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PivotTableAggregatedFieldWellsOutputTypeDef]


# PivotTableFieldWellsTypeDef

### PivotTableAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PivotTableAggregatedFieldWellsTypeDef]


# PivotTableOptionsOutputTypeDef

### MetricPlacement
- **Type**: typing.Optional[typing.Literal['COLUMN', 'ROW']]

### SingleMetricVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### ColumnNamesVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### ToggleButtonsVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### ColumnHeaderStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableCellStyleTypeDef]

### RowHeaderStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableCellStyleTypeDef]

### CellStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableCellStyleTypeDef]

### RowFieldNamesStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableCellStyleTypeDef]

### RowAlternateColorOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RowAlternateColorOptionsOutputTypeDef]

### CollapsedRowDimensionsVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### RowsLayout
- **Type**: typing.Optional[typing.Literal['HIERARCHY', 'TABULAR']]

### RowsLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PivotTableRowsLabelOptionsTypeDef]

### DefaultCellWidth
- **Type**: typing.Optional[str]


# PivotTableOptionsTypeDef

### MetricPlacement
- **Type**: typing.Optional[typing.Literal['COLUMN', 'ROW']]

### SingleMetricVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### ColumnNamesVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### ToggleButtonsVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### ColumnHeaderStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableCellStyleTypeDef]

### RowHeaderStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableCellStyleTypeDef]

### CellStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableCellStyleTypeDef]

### RowFieldNamesStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableCellStyleTypeDef]

### RowAlternateColorOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RowAlternateColorOptionsTypeDef]

### CollapsedRowDimensionsVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### RowsLayout
- **Type**: typing.Optional[typing.Literal['HIERARCHY', 'TABULAR']]

### RowsLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PivotTableRowsLabelOptionsTypeDef]

### DefaultCellWidth
- **Type**: typing.Optional[str]


# PivotTablePaginatedReportOptionsTypeDef

### VerticalOverflowVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### OverflowColumnHeaderVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# PivotTableRowsLabelOptionsTypeDef

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### CustomLabel
- **Type**: typing.Optional[str]


# PivotTableSortByOutputTypeDef

### Field
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortTypeDef]

### Column
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ColumnSortTypeDef]

### DataPath
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataPathSortOutputTypeDef]


# PivotTableSortByTypeDef

### Field
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortTypeDef]

### Column
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ColumnSortTypeDef]

### DataPath
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataPathSortTypeDef]


# PivotTableSortConfigurationOutputTypeDef

### FieldSortOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.PivotFieldSortOptionsOutputTypeDef]]


# PivotTableSortConfigurationTypeDef

### FieldSortOptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.PivotFieldSortOptionsTypeDef]]


# PivotTableTotalOptionsOutputTypeDef

### RowSubtotalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SubtotalOptionsOutputTypeDef]

### ColumnSubtotalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SubtotalOptionsOutputTypeDef]

### RowTotalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PivotTotalOptionsOutputTypeDef]

### ColumnTotalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PivotTotalOptionsOutputTypeDef]


# PivotTableTotalOptionsTypeDef

### RowSubtotalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SubtotalOptionsTypeDef]

### ColumnSubtotalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SubtotalOptionsTypeDef]

### RowTotalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PivotTotalOptionsTypeDef]

### ColumnTotalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PivotTotalOptionsTypeDef]


# PivotTableVisualOutputTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PivotTableConfigurationOutputTypeDef]

### ConditionalFormatting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PivotTableConditionalFormattingOutputTypeDef]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionOutputTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# PivotTableVisualTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PivotTableConfigurationTypeDef]

### ConditionalFormatting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PivotTableConditionalFormattingTypeDef]

### Actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# PivotTotalOptionsOutputTypeDef

### TotalsVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### Placement
- **Type**: typing.Optional[typing.Literal['AUTO', 'END', 'START']]

### ScrollStatus
- **Type**: typing.Optional[typing.Literal['PINNED', 'SCROLLED']]

### CustomLabel
- **Type**: typing.Optional[str]

### TotalCellStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableCellStyleTypeDef]

### ValueCellStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableCellStyleTypeDef]

### MetricHeaderCellStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableCellStyleTypeDef]

### TotalAggregationOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.TotalAggregationOptionTypeDef]]


# PivotTotalOptionsTypeDef

### TotalsVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### Placement
- **Type**: typing.Optional[typing.Literal['AUTO', 'END', 'START']]

### ScrollStatus
- **Type**: typing.Optional[typing.Literal['PINNED', 'SCROLLED']]

### CustomLabel
- **Type**: typing.Optional[str]

### TotalCellStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableCellStyleTypeDef]

### ValueCellStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableCellStyleTypeDef]

### MetricHeaderCellStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableCellStyleTypeDef]

### TotalAggregationOptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TotalAggregationOptionTypeDef]]


# PluginVisualConfigurationOutputTypeDef

### FieldWells
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.PluginVisualFieldWellOutputTypeDef]]

### VisualOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PluginVisualOptionsOutputTypeDef]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PluginVisualSortConfigurationOutputTypeDef]


# PluginVisualConfigurationTypeDef

### FieldWells
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.PluginVisualFieldWellTypeDef]]

### VisualOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PluginVisualOptionsTypeDef]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PluginVisualSortConfigurationTypeDef]


# PluginVisualFieldWellOutputTypeDef

### AxisName
- **Type**: typing.Optional[typing.Literal['GROUP_BY', 'VALUE']]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Measures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]

### Unaggregated
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.UnaggregatedFieldTypeDef]]


# PluginVisualFieldWellTypeDef

### AxisName
- **Type**: typing.Optional[typing.Literal['GROUP_BY', 'VALUE']]

### Dimensions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Measures
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]

### Unaggregated
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.UnaggregatedFieldTypeDef]]


# PluginVisualItemsLimitConfigurationTypeDef

### ItemsLimit
- **Type**: typing.Optional[int]


# PluginVisualOptionsOutputTypeDef

### VisualProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.PluginVisualPropertyTypeDef]]


# PluginVisualOptionsTypeDef

### VisualProperties
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.PluginVisualPropertyTypeDef]]


# PluginVisualOutputTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### PluginArn
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PluginVisualConfigurationOutputTypeDef]

### VisualContentAltText
- **Type**: typing.Optional[str]


# PluginVisualPropertyTypeDef

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# PluginVisualSortConfigurationOutputTypeDef

### PluginVisualTableQuerySort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PluginVisualTableQuerySortOutputTypeDef]


# PluginVisualSortConfigurationTypeDef

### PluginVisualTableQuerySort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PluginVisualTableQuerySortTypeDef]


# PluginVisualTableQuerySortOutputTypeDef

### RowSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### ItemsLimitConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PluginVisualItemsLimitConfigurationTypeDef]


# PluginVisualTableQuerySortTypeDef

### RowSort
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### ItemsLimitConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PluginVisualItemsLimitConfigurationTypeDef]


# PluginVisualTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### PluginArn
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PluginVisualConfigurationTypeDef]

### VisualContentAltText
- **Type**: typing.Optional[str]


# PostgreSqlParametersTypeDef

### Host
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes


# PredefinedHierarchyOutputTypeDef

### HierarchyId
- **Type**: <class 'str'>
- **Required**: Yes

### Columns
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef]
- **Required**: Yes

### DrillDownFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DrillDownFilterOutputTypeDef]]


# PredefinedHierarchyTypeDef

### HierarchyId
- **Type**: <class 'str'>
- **Required**: Yes

### Columns
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef]
- **Required**: Yes

### DrillDownFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DrillDownFilterTypeDef]]


# PredictQAResultsRequestTypeDef

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


# PredictQAResultsResponseTypeDef

### PrimaryResult
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.QAResultTypeDef'>
- **Required**: Yes

### AdditionalResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.QAResultTypeDef]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PrestoParametersTypeDef

### Host
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes


# ProgressBarOptionsTypeDef

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# ProjectOperationOutputTypeDef

### ProjectedColumns
- **Type**: typing.List[str]
- **Required**: Yes


# ProjectOperationTypeDef

### ProjectedColumns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ProjectOperationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PutDataSetRefreshPropertiesRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetRefreshProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.DataSetRefreshPropertiesTypeDef'>
- **Required**: Yes


# PutDataSetRefreshPropertiesResponseTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# QAResultTypeDef

### ResultType
- **Type**: typing.Optional[typing.Literal['DASHBOARD_VISUAL', 'GENERATED_ANSWER', 'NO_ANSWER']]

### DashboardVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DashboardVisualResultTypeDef]

### GeneratedAnswer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeneratedAnswerResultTypeDef]


# QueryExecutionOptionsTypeDef

### QueryExecutionMode
- **Type**: typing.Optional[typing.Literal['AUTO', 'MANUAL']]


# QueueInfoTypeDef

### WaitingOnIngestion
- **Type**: <class 'str'>
- **Required**: Yes

### QueuedIngestion
- **Type**: <class 'str'>
- **Required**: Yes


# RadarChartAggregatedFieldWellsOutputTypeDef

### Category
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Color
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]


# RadarChartAggregatedFieldWellsTypeDef

### Category
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Color
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Values
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]


# RadarChartAreaStyleSettingsTypeDef

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# RadarChartConfigurationOutputTypeDef

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RadarChartFieldWellsOutputTypeDef]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RadarChartSortConfigurationOutputTypeDef]

### Shape
- **Type**: typing.Optional[typing.Literal['CIRCLE', 'POLYGON']]

### BaseSeriesSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RadarChartSeriesSettingsTypeDef]

### StartAngle
- **Type**: typing.Optional[float]

### VisualPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualPaletteOutputTypeDef]

### AlternateBandColorsVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### AlternateBandEvenColor
- **Type**: typing.Optional[str]

### AlternateBandOddColor
- **Type**: typing.Optional[str]

### CategoryAxis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisDisplayOptionsOutputTypeDef]

### CategoryLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsOutputTypeDef]

### ColorAxis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisDisplayOptionsOutputTypeDef]

### ColorLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsOutputTypeDef]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LegendOptionsTypeDef]

### AxesRangeScale
- **Type**: typing.Optional[typing.Literal['AUTO', 'INDEPENDENT', 'SHARED']]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# RadarChartConfigurationTypeDef

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RadarChartFieldWellsTypeDef]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RadarChartSortConfigurationTypeDef]

### Shape
- **Type**: typing.Optional[typing.Literal['CIRCLE', 'POLYGON']]

### BaseSeriesSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RadarChartSeriesSettingsTypeDef]

### StartAngle
- **Type**: typing.Optional[float]

### VisualPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualPaletteTypeDef]

### AlternateBandColorsVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### AlternateBandEvenColor
- **Type**: typing.Optional[str]

### AlternateBandOddColor
- **Type**: typing.Optional[str]

### CategoryAxis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisDisplayOptionsTypeDef]

### CategoryLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsTypeDef]

### ColorAxis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisDisplayOptionsTypeDef]

### ColorLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsTypeDef]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LegendOptionsTypeDef]

### AxesRangeScale
- **Type**: typing.Optional[typing.Literal['AUTO', 'INDEPENDENT', 'SHARED']]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# RadarChartFieldWellsOutputTypeDef

### RadarChartAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RadarChartAggregatedFieldWellsOutputTypeDef]


# RadarChartFieldWellsTypeDef

### RadarChartAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RadarChartAggregatedFieldWellsTypeDef]


# RadarChartSeriesSettingsTypeDef

### AreaStyleSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RadarChartAreaStyleSettingsTypeDef]


# RadarChartSortConfigurationOutputTypeDef

### CategorySort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### CategoryItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]

### ColorSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### ColorItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]


# RadarChartSortConfigurationTypeDef

### CategorySort
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### CategoryItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]

### ColorSort
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### ColorItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]


# RadarChartVisualOutputTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RadarChartConfigurationOutputTypeDef]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionOutputTypeDef]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ColumnHierarchyOutputTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# RadarChartVisualTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RadarChartConfigurationTypeDef]

### Actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionTypeDef]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ColumnHierarchyTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# RangeConstantTypeDef

### Minimum
- **Type**: typing.Optional[str]

### Maximum
- **Type**: typing.Optional[str]


# RangeEndsLabelTypeTypeDef

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# RdsParametersTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes


# RedshiftIAMParametersOutputTypeDef

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseUser
- **Type**: typing.Optional[str]

### DatabaseGroups
- **Type**: typing.Optional[typing.List[str]]

### AutoCreateDatabaseUser
- **Type**: typing.Optional[bool]


# RedshiftIAMParametersTypeDef

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseUser
- **Type**: typing.Optional[str]

### DatabaseGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### AutoCreateDatabaseUser
- **Type**: typing.Optional[bool]


# RedshiftIAMParametersUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RedshiftParametersOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RedshiftIAMParametersOutputTypeDef]

### IdentityCenterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.IdentityCenterConfigurationTypeDef]


# RedshiftParametersTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RedshiftIAMParametersUnionTypeDef]

### IdentityCenterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.IdentityCenterConfigurationTypeDef]


# RedshiftParametersUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ReferenceLineCustomLabelConfigurationTypeDef

### CustomLabel
- **Type**: <class 'str'>
- **Required**: Yes


# ReferenceLineDataConfigurationTypeDef

### StaticConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ReferenceLineStaticDataConfigurationTypeDef]

### DynamicConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ReferenceLineDynamicDataConfigurationTypeDef]

### AxisBinding
- **Type**: typing.Optional[typing.Literal['PRIMARY_YAXIS', 'SECONDARY_YAXIS']]

### SeriesType
- **Type**: typing.Optional[typing.Literal['BAR', 'LINE']]


# ReferenceLineDynamicDataConfigurationTypeDef

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes

### Calculation
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.NumericalAggregationFunctionTypeDef'>
- **Required**: Yes

### MeasureAggregationFunction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AggregationFunctionTypeDef]


# ReferenceLineLabelConfigurationTypeDef

### ValueLabelConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ReferenceLineValueLabelConfigurationTypeDef]

### CustomLabelConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ReferenceLineCustomLabelConfigurationTypeDef]

### FontConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FontConfigurationTypeDef]

### FontColor
- **Type**: typing.Optional[str]

### HorizontalPosition
- **Type**: typing.Optional[typing.Literal['CENTER', 'LEFT', 'RIGHT']]

### VerticalPosition
- **Type**: typing.Optional[typing.Literal['ABOVE', 'BELOW']]


# ReferenceLineStaticDataConfigurationTypeDef

### Value
- **Type**: <class 'float'>
- **Required**: Yes


# ReferenceLineStyleConfigurationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ReferenceLineTypeDef

### DataConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ReferenceLineDataConfigurationTypeDef'>
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### StyleConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ReferenceLineStyleConfigurationTypeDef]

### LabelConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ReferenceLineLabelConfigurationTypeDef]


# ReferenceLineValueLabelConfigurationTypeDef

### RelativePosition
- **Type**: typing.Optional[typing.Literal['AFTER_CUSTOM_LABEL', 'BEFORE_CUSTOM_LABEL']]

### FormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NumericFormatConfigurationTypeDef]


# RefreshConfigurationTypeDef

### IncrementalRefresh
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.IncrementalRefreshTypeDef'>
- **Required**: Yes


# RefreshFrequencyTypeDef

### Interval
- **Type**: typing.Literal['DAILY', 'HOURLY', 'MINUTE15', 'MINUTE30', 'MONTHLY', 'WEEKLY']
- **Required**: Yes

### RefreshOnDay
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ScheduleRefreshOnEntityTypeDef]

### Timezone
- **Type**: typing.Optional[str]

### TimeOfTheDay
- **Type**: typing.Optional[str]


# RefreshScheduleOutputTypeDef

### ScheduleId
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleFrequency
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.RefreshFrequencyTypeDef'>
- **Required**: Yes

### RefreshType
- **Type**: typing.Literal['FULL_REFRESH', 'INCREMENTAL_REFRESH']
- **Required**: Yes

### StartAfterDateTime
- **Type**: typing.Optional[datetime.datetime]

### Arn
- **Type**: typing.Optional[str]


# RefreshScheduleTypeDef

### ScheduleId
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleFrequency
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.RefreshFrequencyTypeDef'>
- **Required**: Yes

### RefreshType
- **Type**: typing.Literal['FULL_REFRESH', 'INCREMENTAL_REFRESH']
- **Required**: Yes

### StartAfterDateTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TimestampTypeDef]

### Arn
- **Type**: typing.Optional[str]


# RefreshScheduleUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RegisterUserRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TagTypeDef]]


# RegisterUserResponseTypeDef

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.UserTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegisteredCustomerManagedKeyTypeDef

### KeyArn
- **Type**: typing.Optional[str]

### DefaultKey
- **Type**: typing.Optional[bool]


# RegisteredUserConsoleFeatureConfigurationsTypeDef

### StatePersistence
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.StatePersistenceConfigurationsTypeDef]

### SharedView
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SharedViewConfigurationsTypeDef]


# RegisteredUserDashboardEmbeddingConfigurationTypeDef

### InitialDashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureConfigurations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RegisteredUserDashboardFeatureConfigurationsTypeDef]


# RegisteredUserDashboardFeatureConfigurationsTypeDef

### StatePersistence
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.StatePersistenceConfigurationsTypeDef]

### SharedView
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SharedViewConfigurationsTypeDef]

### Bookmarks
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BookmarksConfigurationsTypeDef]


# RegisteredUserDashboardVisualEmbeddingConfigurationTypeDef

### InitialDashboardVisualId
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.DashboardVisualIdTypeDef'>
- **Required**: Yes


# RegisteredUserEmbeddingExperienceConfigurationTypeDef

### Dashboard
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RegisteredUserDashboardEmbeddingConfigurationTypeDef]

### QuickSightConsole
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RegisteredUserQuickSightConsoleEmbeddingConfigurationTypeDef]

### QSearchBar
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RegisteredUserQSearchBarEmbeddingConfigurationTypeDef]

### DashboardVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RegisteredUserDashboardVisualEmbeddingConfigurationTypeDef]

### GenerativeQnA
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RegisteredUserGenerativeQnAEmbeddingConfigurationTypeDef]


# RegisteredUserGenerativeQnAEmbeddingConfigurationTypeDef

### InitialTopicId
- **Type**: typing.Optional[str]


# RegisteredUserQSearchBarEmbeddingConfigurationTypeDef

### InitialTopicId
- **Type**: typing.Optional[str]


# RegisteredUserQuickSightConsoleEmbeddingConfigurationTypeDef

### InitialPath
- **Type**: typing.Optional[str]

### FeatureConfigurations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RegisteredUserConsoleFeatureConfigurationsTypeDef]


# RelationalTableOutputTypeDef

### DataSourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### InputColumns
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.InputColumnTypeDef]
- **Required**: Yes

### Catalog
- **Type**: typing.Optional[str]

### Schema
- **Type**: typing.Optional[str]


# RelationalTableTypeDef

### DataSourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### InputColumns
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.InputColumnTypeDef]
- **Required**: Yes

### Catalog
- **Type**: typing.Optional[str]

### Schema
- **Type**: typing.Optional[str]


# RelationalTableUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RelativeDateTimeControlDisplayOptionsTypeDef

### TitleOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LabelOptionsTypeDef]

### DateTimeFormat
- **Type**: typing.Optional[str]

### InfoIconLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SheetControlInfoIconLabelOptionsTypeDef]


# RelativeDatesFilterOutputTypeDef

### FilterId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes

### AnchorDateConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.AnchorDateConfigurationTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ExcludePeriodConfigurationTypeDef]

### DefaultFilterControlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultFilterControlConfigurationOutputTypeDef]


# RelativeDatesFilterTypeDef

### FilterId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes

### AnchorDateConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.AnchorDateConfigurationTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ExcludePeriodConfigurationTypeDef]

### DefaultFilterControlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultFilterControlConfigurationTypeDef]


# RenameColumnOperationTypeDef

### ColumnName
- **Type**: <class 'str'>
- **Required**: Yes

### NewColumnName
- **Type**: <class 'str'>
- **Required**: Yes


# ResourcePermissionOutputTypeDef

### Principal
- **Type**: <class 'str'>
- **Required**: Yes

### Actions
- **Type**: typing.List[str]
- **Required**: Yes


# ResourcePermissionTypeDef

### Principal
- **Type**: <class 'str'>
- **Required**: Yes

### Actions
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ResourcePermissionUnionTypeDef

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


# RestoreAnalysisRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AnalysisId
- **Type**: <class 'str'>
- **Required**: Yes

### RestoreToFolders
- **Type**: typing.Optional[bool]


# RestoreAnalysisResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RollingDateConfigurationTypeDef

### Expression
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetIdentifier
- **Type**: typing.Optional[str]


# RowAlternateColorOptionsOutputTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### RowAlternateColors
- **Type**: typing.Optional[typing.List[str]]

### UsePrimaryBackgroundColor
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# RowAlternateColorOptionsTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### RowAlternateColors
- **Type**: typing.Optional[typing.Sequence[str]]

### UsePrimaryBackgroundColor
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# RowInfoTypeDef

### RowsIngested
- **Type**: typing.Optional[int]

### RowsDropped
- **Type**: typing.Optional[int]

### TotalRowsInDataset
- **Type**: typing.Optional[int]


# RowLevelPermissionDataSetTypeDef

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


# RowLevelPermissionTagConfigurationOutputTypeDef

### TagRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.RowLevelPermissionTagRuleTypeDef]
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### TagRuleConfigurations
- **Type**: typing.Optional[typing.List[typing.List[str]]]


# RowLevelPermissionTagConfigurationTypeDef

### TagRules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.RowLevelPermissionTagRuleTypeDef]
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### TagRuleConfigurations
- **Type**: typing.Optional[typing.Sequence[typing.Sequence[str]]]


# RowLevelPermissionTagConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RowLevelPermissionTagRuleTypeDef

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


# S3BucketConfigurationTypeDef

### BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### BucketPrefix
- **Type**: <class 'str'>
- **Required**: Yes

### BucketRegion
- **Type**: <class 'str'>
- **Required**: Yes


# S3ParametersTypeDef

### ManifestFileLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ManifestFileLocationTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: typing.Optional[str]


# S3SourceOutputTypeDef

### DataSourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### InputColumns
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.InputColumnTypeDef]
- **Required**: Yes

### UploadSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.UploadSettingsTypeDef]


# S3SourceTypeDef

### DataSourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### InputColumns
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.InputColumnTypeDef]
- **Required**: Yes

### UploadSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.UploadSettingsTypeDef]


# S3SourceUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SameSheetTargetVisualConfigurationOutputTypeDef

### TargetVisuals
- **Type**: typing.Optional[typing.List[str]]

### TargetVisualOptions
- **Type**: typing.Optional[typing.Literal['ALL_VISUALS']]


# SameSheetTargetVisualConfigurationTypeDef

### TargetVisuals
- **Type**: typing.Optional[typing.Sequence[str]]

### TargetVisualOptions
- **Type**: typing.Optional[typing.Literal['ALL_VISUALS']]


# SankeyDiagramAggregatedFieldWellsOutputTypeDef

### Source
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Destination
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Weight
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]


# SankeyDiagramAggregatedFieldWellsTypeDef

### Source
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Destination
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Weight
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]


# SankeyDiagramChartConfigurationOutputTypeDef

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SankeyDiagramFieldWellsOutputTypeDef]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SankeyDiagramSortConfigurationOutputTypeDef]

### DataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataLabelOptionsOutputTypeDef]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# SankeyDiagramChartConfigurationTypeDef

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SankeyDiagramFieldWellsTypeDef]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SankeyDiagramSortConfigurationTypeDef]

### DataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataLabelOptionsTypeDef]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# SankeyDiagramFieldWellsOutputTypeDef

### SankeyDiagramAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SankeyDiagramAggregatedFieldWellsOutputTypeDef]


# SankeyDiagramFieldWellsTypeDef

### SankeyDiagramAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SankeyDiagramAggregatedFieldWellsTypeDef]


# SankeyDiagramSortConfigurationOutputTypeDef

### WeightSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### SourceItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]

### DestinationItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]


# SankeyDiagramSortConfigurationTypeDef

### WeightSort
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### SourceItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]

### DestinationItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]


# SankeyDiagramVisualOutputTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SankeyDiagramChartConfigurationOutputTypeDef]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionOutputTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# SankeyDiagramVisualTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SankeyDiagramChartConfigurationTypeDef]

### Actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# ScatterPlotCategoricallyAggregatedFieldWellsOutputTypeDef

### XAxis
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]

### YAxis
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]

### Category
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Size
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]

### Label
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]


# ScatterPlotCategoricallyAggregatedFieldWellsTypeDef

### XAxis
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]

### YAxis
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]

### Category
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Size
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]

### Label
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]


# ScatterPlotConfigurationOutputTypeDef

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ScatterPlotFieldWellsOutputTypeDef]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ScatterPlotSortConfigurationTypeDef]

### XAxisLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsOutputTypeDef]

### XAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisDisplayOptionsOutputTypeDef]

### YAxisLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsOutputTypeDef]

### YAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisDisplayOptionsOutputTypeDef]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LegendOptionsTypeDef]

### DataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataLabelOptionsOutputTypeDef]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TooltipOptionsOutputTypeDef]

### VisualPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualPaletteOutputTypeDef]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# ScatterPlotConfigurationTypeDef

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ScatterPlotFieldWellsTypeDef]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ScatterPlotSortConfigurationTypeDef]

### XAxisLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsTypeDef]

### XAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisDisplayOptionsTypeDef]

### YAxisLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsTypeDef]

### YAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisDisplayOptionsTypeDef]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LegendOptionsTypeDef]

### DataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataLabelOptionsTypeDef]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TooltipOptionsTypeDef]

### VisualPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualPaletteTypeDef]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# ScatterPlotFieldWellsOutputTypeDef

### ScatterPlotCategoricallyAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ScatterPlotCategoricallyAggregatedFieldWellsOutputTypeDef]

### ScatterPlotUnaggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ScatterPlotUnaggregatedFieldWellsOutputTypeDef]


# ScatterPlotFieldWellsTypeDef

### ScatterPlotCategoricallyAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ScatterPlotCategoricallyAggregatedFieldWellsTypeDef]

### ScatterPlotUnaggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ScatterPlotUnaggregatedFieldWellsTypeDef]


# ScatterPlotSortConfigurationTypeDef

### ScatterPlotLimitConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]


# ScatterPlotUnaggregatedFieldWellsOutputTypeDef

### XAxis
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### YAxis
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Size
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]

### Category
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Label
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]


# ScatterPlotUnaggregatedFieldWellsTypeDef

### XAxis
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### YAxis
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Size
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]

### Category
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Label
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]


# ScatterPlotVisualOutputTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ScatterPlotConfigurationOutputTypeDef]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionOutputTypeDef]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ColumnHierarchyOutputTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# ScatterPlotVisualTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ScatterPlotConfigurationTypeDef]

### Actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionTypeDef]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ColumnHierarchyTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# ScheduleRefreshOnEntityTypeDef

### DayOfWeek
- **Type**: typing.Optional[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY']]

### DayOfMonth
- **Type**: typing.Optional[str]


# ScrollBarOptionsTypeDef

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### VisibleRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisibleRangeOptionsTypeDef]


# SearchAnalysesRequestPaginateTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.AnalysisSearchFilterTypeDef]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaginatorConfigTypeDef]


# SearchAnalysesRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.AnalysisSearchFilterTypeDef]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# SearchAnalysesResponseTypeDef

### AnalysisSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AnalysisSummaryTypeDef]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchDashboardsRequestPaginateTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DashboardSearchFilterTypeDef]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaginatorConfigTypeDef]


# SearchDashboardsRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DashboardSearchFilterTypeDef]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# SearchDashboardsResponseTypeDef

### DashboardSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DashboardSummaryTypeDef]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchDataSetsRequestPaginateTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DataSetSearchFilterTypeDef]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaginatorConfigTypeDef]


# SearchDataSetsRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DataSetSearchFilterTypeDef]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# SearchDataSetsResponseTypeDef

### DataSetSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DataSetSummaryTypeDef]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchDataSourcesRequestPaginateTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DataSourceSearchFilterTypeDef]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaginatorConfigTypeDef]


# SearchDataSourcesRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DataSourceSearchFilterTypeDef]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# SearchDataSourcesResponseTypeDef

### DataSourceSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DataSourceSummaryTypeDef]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchFoldersRequestPaginateTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.FolderSearchFilterTypeDef]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaginatorConfigTypeDef]


# SearchFoldersRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.FolderSearchFilterTypeDef]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# SearchFoldersResponseTypeDef

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### FolderSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.FolderSummaryTypeDef]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchGroupsRequestPaginateTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.GroupSearchFilterTypeDef]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaginatorConfigTypeDef]


# SearchGroupsRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.GroupSearchFilterTypeDef]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# SearchGroupsResponseTypeDef

### GroupList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.GroupTypeDef]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchTopicsRequestPaginateTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TopicSearchFilterTypeDef]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaginatorConfigTypeDef]


# SearchTopicsRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TopicSearchFilterTypeDef]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# SearchTopicsResponseTypeDef

### TopicSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.TopicSummaryTypeDef]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SecondaryValueOptionsTypeDef

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# SectionAfterPageBreakTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# SectionBasedLayoutCanvasSizeOptionsTypeDef

### PaperCanvasSizeOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SectionBasedLayoutPaperCanvasSizeOptionsTypeDef]


# SectionBasedLayoutConfigurationOutputTypeDef

### HeaderSections
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.HeaderFooterSectionConfigurationOutputTypeDef]
- **Required**: Yes

### BodySections
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.BodySectionConfigurationOutputTypeDef]
- **Required**: Yes

### FooterSections
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.HeaderFooterSectionConfigurationOutputTypeDef]
- **Required**: Yes

### CanvasSizeOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.SectionBasedLayoutCanvasSizeOptionsTypeDef'>
- **Required**: Yes


# SectionBasedLayoutConfigurationTypeDef

### HeaderSections
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.HeaderFooterSectionConfigurationTypeDef]
- **Required**: Yes

### BodySections
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.BodySectionConfigurationTypeDef]
- **Required**: Yes

### FooterSections
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.HeaderFooterSectionConfigurationTypeDef]
- **Required**: Yes

### CanvasSizeOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.SectionBasedLayoutCanvasSizeOptionsTypeDef'>
- **Required**: Yes


# SectionBasedLayoutPaperCanvasSizeOptionsTypeDef

### PaperSize
- **Type**: typing.Optional[typing.Literal['A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'JIS_B4', 'JIS_B5', 'US_LEGAL', 'US_LETTER', 'US_TABLOID_LEDGER']]

### PaperOrientation
- **Type**: typing.Optional[typing.Literal['LANDSCAPE', 'PORTRAIT']]

### PaperMargin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SpacingTypeDef]


# SectionLayoutConfigurationOutputTypeDef

### FreeFormLayout
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.FreeFormSectionLayoutConfigurationOutputTypeDef'>
- **Required**: Yes


# SectionLayoutConfigurationTypeDef

### FreeFormLayout
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.FreeFormSectionLayoutConfigurationTypeDef'>
- **Required**: Yes


# SectionPageBreakConfigurationTypeDef

### After
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SectionAfterPageBreakTypeDef]


# SectionStyleTypeDef

### Height
- **Type**: typing.Optional[str]

### Padding
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SpacingTypeDef]


# SelectedSheetsFilterScopeConfigurationOutputTypeDef

### SheetVisualScopingConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.SheetVisualScopingConfigurationOutputTypeDef]]


# SelectedSheetsFilterScopeConfigurationTypeDef

### SheetVisualScopingConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.SheetVisualScopingConfigurationTypeDef]]


# SemanticEntityTypeOutputTypeDef

### TypeName
- **Type**: typing.Optional[str]

### SubTypeName
- **Type**: typing.Optional[str]

### TypeParameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# SemanticEntityTypeTypeDef

### TypeName
- **Type**: typing.Optional[str]

### SubTypeName
- **Type**: typing.Optional[str]

### TypeParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# SemanticTypeOutputTypeDef

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


# SemanticTypeTypeDef

### TypeName
- **Type**: typing.Optional[str]

### SubTypeName
- **Type**: typing.Optional[str]

### TypeParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### TruthyCellValue
- **Type**: typing.Optional[str]

### TruthyCellValueSynonyms
- **Type**: typing.Optional[typing.Sequence[str]]

### FalseyCellValue
- **Type**: typing.Optional[str]

### FalseyCellValueSynonyms
- **Type**: typing.Optional[typing.Sequence[str]]


# SeriesItemTypeDef

### FieldSeriesItem
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FieldSeriesItemTypeDef]

### DataFieldSeriesItem
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataFieldSeriesItemTypeDef]


# ServiceNowParametersTypeDef

### SiteBaseUrl
- **Type**: <class 'str'>
- **Required**: Yes


# SessionTagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# SetParameterValueConfigurationOutputTypeDef

### DestinationParameterName
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.DestinationParameterValueConfigurationOutputTypeDef'>
- **Required**: Yes


# SetParameterValueConfigurationTypeDef

### DestinationParameterName
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.DestinationParameterValueConfigurationTypeDef'>
- **Required**: Yes


# ShapeConditionalFormatOutputTypeDef

### BackgroundColor
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingColorOutputTypeDef'>
- **Required**: Yes


# ShapeConditionalFormatTypeDef

### BackgroundColor
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingColorTypeDef'>
- **Required**: Yes


# SharedViewConfigurationsTypeDef

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# SheetControlInfoIconLabelOptionsTypeDef

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### InfoIconText
- **Type**: typing.Optional[str]


# SheetControlLayoutConfigurationOutputTypeDef

### GridLayout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GridLayoutConfigurationOutputTypeDef]


# SheetControlLayoutConfigurationTypeDef

### GridLayout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GridLayoutConfigurationTypeDef]


# SheetControlLayoutOutputTypeDef

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.SheetControlLayoutConfigurationOutputTypeDef'>
- **Required**: Yes


# SheetControlLayoutTypeDef

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.SheetControlLayoutConfigurationTypeDef'>
- **Required**: Yes


# SheetControlsOptionTypeDef

### VisibilityState
- **Type**: typing.Optional[typing.Literal['COLLAPSED', 'EXPANDED']]


# SheetDefinitionOutputTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ParameterControlOutputTypeDef]]

### FilterControls
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.FilterControlOutputTypeDef]]

### Visuals
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.VisualOutputTypeDef]]

### TextBoxes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.SheetTextBoxTypeDef]]

### Images
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.SheetImageOutputTypeDef]]

### Layouts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.LayoutOutputTypeDef]]

### SheetControlLayouts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.SheetControlLayoutOutputTypeDef]]

### ContentType
- **Type**: typing.Optional[typing.Literal['INTERACTIVE', 'PAGINATED']]


# SheetDefinitionTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ParameterControlTypeDef]]

### FilterControls
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.FilterControlTypeDef]]

### Visuals
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.VisualTypeDef]]

### TextBoxes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.SheetTextBoxTypeDef]]

### Images
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.SheetImageTypeDef]]

### Layouts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.LayoutTypeDef]]

### SheetControlLayouts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.SheetControlLayoutTypeDef]]

### ContentType
- **Type**: typing.Optional[typing.Literal['INTERACTIVE', 'PAGINATED']]


# SheetElementConfigurationOverridesTypeDef

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# SheetElementRenderingRuleTypeDef

### Expression
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationOverrides
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.SheetElementConfigurationOverridesTypeDef'>
- **Required**: Yes


# SheetImageOutputTypeDef

### SheetImageId
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.SheetImageSourceTypeDef'>
- **Required**: Yes

### Scaling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SheetImageScalingConfigurationTypeDef]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SheetImageTooltipConfigurationTypeDef]

### ImageContentAltText
- **Type**: typing.Optional[str]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ImageInteractionOptionsTypeDef]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ImageCustomActionOutputTypeDef]]


# SheetImageScalingConfigurationTypeDef

### ScalingType
- **Type**: typing.Optional[typing.Literal['SCALE_NONE', 'SCALE_TO_CONTAINER', 'SCALE_TO_HEIGHT', 'SCALE_TO_WIDTH']]


# SheetImageSourceTypeDef

### SheetImageStaticFileSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SheetImageStaticFileSourceTypeDef]


# SheetImageStaticFileSourceTypeDef

### StaticFileId
- **Type**: <class 'str'>
- **Required**: Yes


# SheetImageTooltipConfigurationTypeDef

### TooltipText
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SheetImageTooltipTextTypeDef]

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# SheetImageTooltipTextTypeDef

### PlainText
- **Type**: typing.Optional[str]


# SheetImageTypeDef

### SheetImageId
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.SheetImageSourceTypeDef'>
- **Required**: Yes

### Scaling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SheetImageScalingConfigurationTypeDef]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SheetImageTooltipConfigurationTypeDef]

### ImageContentAltText
- **Type**: typing.Optional[str]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ImageInteractionOptionsTypeDef]

### Actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ImageCustomActionTypeDef]]


# SheetLayoutElementMaximizationOptionTypeDef

### AvailabilityStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# SheetStyleTypeDef

### Tile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TileStyleTypeDef]

### TileLayout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TileLayoutStyleTypeDef]


# SheetTextBoxTypeDef

### SheetTextBoxId
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: typing.Optional[str]


# SheetTypeDef

### SheetId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Images
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.SheetImageOutputTypeDef]]


# SheetVisualScopingConfigurationOutputTypeDef

### SheetId
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Literal['ALL_VISUALS', 'SELECTED_VISUALS']
- **Required**: Yes

### VisualIds
- **Type**: typing.Optional[typing.List[str]]


# SheetVisualScopingConfigurationTypeDef

### SheetId
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Literal['ALL_VISUALS', 'SELECTED_VISUALS']
- **Required**: Yes

### VisualIds
- **Type**: typing.Optional[typing.Sequence[str]]


# ShortFormatTextTypeDef

### PlainText
- **Type**: typing.Optional[str]

### RichText
- **Type**: typing.Optional[str]


# SignupResponseTypeDef

### IAMUser
- **Type**: typing.Optional[bool]

### userLoginName
- **Type**: typing.Optional[str]

### accountName
- **Type**: typing.Optional[str]

### directoryType
- **Type**: typing.Optional[str]


# SimpleClusterMarkerTypeDef

### Color
- **Type**: typing.Optional[str]


# SingleAxisOptionsTypeDef

### YAxisOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.YAxisOptionsTypeDef]


# SliderControlDisplayOptionsTypeDef

### TitleOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LabelOptionsTypeDef]

### InfoIconLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SheetControlInfoIconLabelOptionsTypeDef]


# SlotTypeDef

### SlotId
- **Type**: typing.Optional[str]

### VisualId
- **Type**: typing.Optional[str]


# SmallMultiplesAxisPropertiesTypeDef

### Scale
- **Type**: typing.Optional[typing.Literal['INDEPENDENT', 'SHARED']]

### Placement
- **Type**: typing.Optional[typing.Literal['INSIDE', 'OUTSIDE']]


# SmallMultiplesOptionsTypeDef

### MaxVisibleRows
- **Type**: typing.Optional[int]

### MaxVisibleColumns
- **Type**: typing.Optional[int]

### PanelConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PanelConfigurationTypeDef]

### XAxis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SmallMultiplesAxisPropertiesTypeDef]

### YAxis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SmallMultiplesAxisPropertiesTypeDef]


# SnapshotAnonymousUserRedactedTypeDef

### RowLevelPermissionTagKeys
- **Type**: typing.Optional[typing.List[str]]


# SnapshotAnonymousUserTypeDef

### RowLevelPermissionTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.SessionTagTypeDef]]


# SnapshotConfigurationOutputTypeDef

### FileGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.SnapshotFileGroupOutputTypeDef]
- **Required**: Yes

### DestinationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SnapshotDestinationConfigurationOutputTypeDef]

### Parameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ParametersOutputTypeDef]


# SnapshotConfigurationTypeDef

### FileGroups
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.SnapshotFileGroupTypeDef]
- **Required**: Yes

### DestinationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SnapshotDestinationConfigurationTypeDef]

### Parameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ParametersTypeDef]


# SnapshotConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SnapshotDestinationConfigurationOutputTypeDef

### S3Destinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.SnapshotS3DestinationConfigurationTypeDef]]


# SnapshotDestinationConfigurationTypeDef

### S3Destinations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.SnapshotS3DestinationConfigurationTypeDef]]


# SnapshotFileGroupOutputTypeDef

### Files
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.SnapshotFileOutputTypeDef]]


# SnapshotFileGroupTypeDef

### Files
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.SnapshotFileTypeDef]]


# SnapshotFileOutputTypeDef

### SheetSelections
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.SnapshotFileSheetSelectionOutputTypeDef]
- **Required**: Yes

### FormatType
- **Type**: typing.Literal['CSV', 'EXCEL', 'PDF']
- **Required**: Yes


# SnapshotFileSheetSelectionOutputTypeDef

### SheetId
- **Type**: <class 'str'>
- **Required**: Yes

### SelectionScope
- **Type**: typing.Literal['ALL_VISUALS', 'SELECTED_VISUALS']
- **Required**: Yes

### VisualIds
- **Type**: typing.Optional[typing.List[str]]


# SnapshotFileSheetSelectionTypeDef

### SheetId
- **Type**: <class 'str'>
- **Required**: Yes

### SelectionScope
- **Type**: typing.Literal['ALL_VISUALS', 'SELECTED_VISUALS']
- **Required**: Yes

### VisualIds
- **Type**: typing.Optional[typing.Sequence[str]]


# SnapshotFileTypeDef

### SheetSelections
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.SnapshotFileSheetSelectionTypeDef]
- **Required**: Yes

### FormatType
- **Type**: typing.Literal['CSV', 'EXCEL', 'PDF']
- **Required**: Yes


# SnapshotJobErrorInfoTypeDef

### ErrorMessage
- **Type**: typing.Optional[str]

### ErrorType
- **Type**: typing.Optional[str]


# SnapshotJobResultErrorInfoTypeDef

### ErrorMessage
- **Type**: typing.Optional[str]

### ErrorType
- **Type**: typing.Optional[str]


# SnapshotJobResultFileGroupTypeDef

### Files
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.SnapshotFileOutputTypeDef]]

### S3Results
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.SnapshotJobS3ResultTypeDef]]


# SnapshotJobResultTypeDef

### AnonymousUsers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AnonymousUserSnapshotJobResultTypeDef]]


# SnapshotJobS3ResultTypeDef

### S3DestinationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SnapshotS3DestinationConfigurationTypeDef]

### S3Uri
- **Type**: typing.Optional[str]

### ErrorInfo
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.SnapshotJobResultErrorInfoTypeDef]]


# SnapshotS3DestinationConfigurationTypeDef

### BucketConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.S3BucketConfigurationTypeDef'>
- **Required**: Yes


# SnapshotUserConfigurationRedactedTypeDef

### AnonymousUsers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.SnapshotAnonymousUserRedactedTypeDef]]


# SnapshotUserConfigurationTypeDef

### AnonymousUsers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.SnapshotAnonymousUserTypeDef]]


# SnowflakeParametersTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.OAuthParametersTypeDef]


# SpacingTypeDef

### Top
- **Type**: typing.Optional[str]

### Bottom
- **Type**: typing.Optional[str]

### Left
- **Type**: typing.Optional[str]

### Right
- **Type**: typing.Optional[str]


# SparkParametersTypeDef

### Host
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes


# SpatialStaticFileTypeDef

### StaticFileId
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.StaticFileSourceTypeDef]


# SqlServerParametersTypeDef

### Host
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes


# SslPropertiesTypeDef

### DisableSsl
- **Type**: typing.Optional[bool]


# StarburstParametersTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.OAuthParametersTypeDef]


# StartAssetBundleExportJobRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AssetBundleExportJobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ExportFormat
- **Type**: typing.Literal['CLOUDFORMATION_JSON', 'QUICKSIGHT_JSON']
- **Required**: Yes

### IncludeAllDependencies
- **Type**: typing.Optional[bool]

### CloudFormationOverridePropertyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleCloudFormationOverridePropertyConfigurationUnionTypeDef]

### IncludePermissions
- **Type**: typing.Optional[bool]

### IncludeTags
- **Type**: typing.Optional[bool]

### ValidationStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleExportJobValidationStrategyTypeDef]

### IncludeFolderMemberships
- **Type**: typing.Optional[bool]

### IncludeFolderMembers
- **Type**: typing.Optional[typing.Literal['NONE', 'ONE_LEVEL', 'RECURSE']]


# StartAssetBundleExportJobResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartAssetBundleImportJobRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AssetBundleImportJobId
- **Type**: <class 'str'>
- **Required**: Yes

### AssetBundleImportSource
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportSourceTypeDef'>
- **Required**: Yes

### OverrideParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobOverrideParametersUnionTypeDef]

### FailureAction
- **Type**: typing.Optional[typing.Literal['DO_NOTHING', 'ROLLBACK']]

### OverridePermissions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobOverridePermissionsUnionTypeDef]

### OverrideTags
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobOverrideTagsUnionTypeDef]

### OverrideValidationStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AssetBundleImportJobOverrideValidationStrategyTypeDef]


# StartAssetBundleImportJobResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartDashboardSnapshotJobRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.SnapshotUserConfigurationTypeDef'>
- **Required**: Yes

### SnapshotConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.SnapshotConfigurationUnionTypeDef'>
- **Required**: Yes


# StartDashboardSnapshotJobResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartDashboardSnapshotJobScheduleRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleId
- **Type**: <class 'str'>
- **Required**: Yes


# StartDashboardSnapshotJobScheduleResponseTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StatePersistenceConfigurationsTypeDef

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# StaticFileS3SourceOptionsTypeDef

### BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectKey
- **Type**: <class 'str'>
- **Required**: Yes

### Region
- **Type**: <class 'str'>
- **Required**: Yes


# StaticFileSourceTypeDef

### UrlOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.StaticFileUrlSourceOptionsTypeDef]

### S3Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.StaticFileS3SourceOptionsTypeDef]


# StaticFileTypeDef

### ImageStaticFile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ImageStaticFileTypeDef]

### SpatialStaticFile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SpatialStaticFileTypeDef]


# StaticFileUrlSourceOptionsTypeDef

### Url
- **Type**: <class 'str'>
- **Required**: Yes


# StringDatasetParameterDefaultValuesOutputTypeDef

### StaticValues
- **Type**: typing.Optional[typing.List[str]]


# StringDatasetParameterDefaultValuesTypeDef

### StaticValues
- **Type**: typing.Optional[typing.Sequence[str]]


# StringDatasetParameterDefaultValuesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StringDatasetParameterOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.StringDatasetParameterDefaultValuesOutputTypeDef]


# StringDatasetParameterTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.StringDatasetParameterDefaultValuesUnionTypeDef]


# StringDatasetParameterUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StringDefaultValuesOutputTypeDef

### DynamicValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DynamicDefaultValueTypeDef]

### StaticValues
- **Type**: typing.Optional[typing.List[str]]


# StringDefaultValuesTypeDef

### DynamicValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DynamicDefaultValueTypeDef]

### StaticValues
- **Type**: typing.Optional[typing.Sequence[str]]


# StringFormatConfigurationTypeDef

### NullValueFormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NullValueFormatConfigurationTypeDef]

### NumericFormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NumericFormatConfigurationTypeDef]


# StringParameterDeclarationOutputTypeDef

### ParameterValueType
- **Type**: typing.Literal['MULTI_VALUED', 'SINGLE_VALUED']
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.StringDefaultValuesOutputTypeDef]

### ValueWhenUnset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.StringValueWhenUnsetConfigurationTypeDef]

### MappedDataSetParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.MappedDataSetParameterTypeDef]]


# StringParameterDeclarationTypeDef

### ParameterValueType
- **Type**: typing.Literal['MULTI_VALUED', 'SINGLE_VALUED']
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.StringDefaultValuesTypeDef]

### ValueWhenUnset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.StringValueWhenUnsetConfigurationTypeDef]

### MappedDataSetParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.MappedDataSetParameterTypeDef]]


# StringParameterOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# StringParameterTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# StringValueWhenUnsetConfigurationTypeDef

### ValueWhenUnsetOption
- **Type**: typing.Optional[typing.Literal['NULL', 'RECOMMENDED_VALUE']]

### CustomValue
- **Type**: typing.Optional[str]


# SubtotalOptionsOutputTypeDef

### TotalsVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### CustomLabel
- **Type**: typing.Optional[str]

### FieldLevel
- **Type**: typing.Optional[typing.Literal['ALL', 'CUSTOM', 'LAST']]

### FieldLevelOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.PivotTableFieldSubtotalOptionsTypeDef]]

### TotalCellStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableCellStyleTypeDef]

### ValueCellStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableCellStyleTypeDef]

### MetricHeaderCellStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableCellStyleTypeDef]

### StyleTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.TableStyleTargetTypeDef]]


# SubtotalOptionsTypeDef

### TotalsVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### CustomLabel
- **Type**: typing.Optional[str]

### FieldLevel
- **Type**: typing.Optional[typing.Literal['ALL', 'CUSTOM', 'LAST']]

### FieldLevelOptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.PivotTableFieldSubtotalOptionsTypeDef]]

### TotalCellStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableCellStyleTypeDef]

### ValueCellStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableCellStyleTypeDef]

### MetricHeaderCellStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableCellStyleTypeDef]

### StyleTargets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TableStyleTargetTypeDef]]


# SucceededTopicReviewedAnswerTypeDef

### AnswerId
- **Type**: typing.Optional[str]


# SuccessfulKeyRegistrationEntryTypeDef

### KeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### StatusCode
- **Type**: <class 'int'>
- **Required**: Yes


# TableAggregatedFieldWellsOutputTypeDef

### GroupBy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]


# TableAggregatedFieldWellsTypeDef

### GroupBy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Values
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]


# TableBorderOptionsTypeDef

### Color
- **Type**: typing.Optional[str]

### Thickness
- **Type**: typing.Optional[int]

### Style
- **Type**: typing.Optional[typing.Literal['NONE', 'SOLID']]


# TableCellConditionalFormattingOutputTypeDef

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### TextFormat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TextConditionalFormatOutputTypeDef]


# TableCellConditionalFormattingTypeDef

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### TextFormat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TextConditionalFormatTypeDef]


# TableCellImageSizingConfigurationTypeDef

### TableCellImageScalingConfiguration
- **Type**: typing.Optional[typing.Literal['DO_NOT_SCALE', 'FIT_TO_CELL_HEIGHT', 'FIT_TO_CELL_WIDTH']]


# TableCellStyleTypeDef

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### FontConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FontConfigurationTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GlobalTableBorderOptionsTypeDef]


# TableConditionalFormattingOptionOutputTypeDef

### Cell
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableCellConditionalFormattingOutputTypeDef]

### Row
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableRowConditionalFormattingOutputTypeDef]


# TableConditionalFormattingOptionTypeDef

### Cell
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableCellConditionalFormattingTypeDef]

### Row
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableRowConditionalFormattingTypeDef]


# TableConditionalFormattingOutputTypeDef

### ConditionalFormattingOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.TableConditionalFormattingOptionOutputTypeDef]]


# TableConditionalFormattingTypeDef

### ConditionalFormattingOptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TableConditionalFormattingOptionTypeDef]]


# TableConfigurationOutputTypeDef

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableFieldWellsOutputTypeDef]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableSortConfigurationOutputTypeDef]

### TableOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableOptionsOutputTypeDef]

### TotalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TotalOptionsOutputTypeDef]

### FieldOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableFieldOptionsOutputTypeDef]

### PaginatedReportOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TablePaginatedReportOptionsTypeDef]

### TableInlineVisualizations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.TableInlineVisualizationTypeDef]]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# TableConfigurationTypeDef

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableFieldWellsTypeDef]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableSortConfigurationTypeDef]

### TableOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableOptionsTypeDef]

### TotalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TotalOptionsTypeDef]

### FieldOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableFieldOptionsTypeDef]

### PaginatedReportOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TablePaginatedReportOptionsTypeDef]

### TableInlineVisualizations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TableInlineVisualizationTypeDef]]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# TableFieldCustomIconContentTypeDef

### Icon
- **Type**: typing.Optional[typing.Literal['LINK']]


# TableFieldCustomTextContentTypeDef

### FontConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.FontConfigurationTypeDef'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# TableFieldImageConfigurationTypeDef

### SizingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableCellImageSizingConfigurationTypeDef]


# TableFieldLinkConfigurationTypeDef

### Target
- **Type**: typing.Literal['NEW_TAB', 'NEW_WINDOW', 'SAME_TAB']
- **Required**: Yes

### Content
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.TableFieldLinkContentConfigurationTypeDef'>
- **Required**: Yes


# TableFieldLinkContentConfigurationTypeDef

### CustomTextContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableFieldCustomTextContentTypeDef]

### CustomIconContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableFieldCustomIconContentTypeDef]


# TableFieldOptionTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableFieldURLConfigurationTypeDef]


# TableFieldOptionsOutputTypeDef

### SelectedFieldOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.TableFieldOptionTypeDef]]

### Order
- **Type**: typing.Optional[typing.List[str]]

### PinnedFieldOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TablePinnedFieldOptionsOutputTypeDef]


# TableFieldOptionsTypeDef

### SelectedFieldOptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TableFieldOptionTypeDef]]

### Order
- **Type**: typing.Optional[typing.Sequence[str]]

### PinnedFieldOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TablePinnedFieldOptionsTypeDef]


# TableFieldURLConfigurationTypeDef

### LinkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableFieldLinkConfigurationTypeDef]

### ImageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableFieldImageConfigurationTypeDef]


# TableFieldWellsOutputTypeDef

### TableAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableAggregatedFieldWellsOutputTypeDef]

### TableUnaggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableUnaggregatedFieldWellsOutputTypeDef]


# TableFieldWellsTypeDef

### TableAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableAggregatedFieldWellsTypeDef]

### TableUnaggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableUnaggregatedFieldWellsTypeDef]


# TableInlineVisualizationTypeDef

### DataBars
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataBarsOptionsTypeDef]


# TableOptionsOutputTypeDef

### Orientation
- **Type**: typing.Optional[typing.Literal['HORIZONTAL', 'VERTICAL']]

### HeaderStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableCellStyleTypeDef]

### CellStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableCellStyleTypeDef]

### RowAlternateColorOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RowAlternateColorOptionsOutputTypeDef]


# TableOptionsTypeDef

### Orientation
- **Type**: typing.Optional[typing.Literal['HORIZONTAL', 'VERTICAL']]

### HeaderStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableCellStyleTypeDef]

### CellStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableCellStyleTypeDef]

### RowAlternateColorOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RowAlternateColorOptionsTypeDef]


# TablePaginatedReportOptionsTypeDef

### VerticalOverflowVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### OverflowColumnHeaderVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# TablePinnedFieldOptionsOutputTypeDef

### PinnedLeftFields
- **Type**: typing.Optional[typing.List[str]]


# TablePinnedFieldOptionsTypeDef

### PinnedLeftFields
- **Type**: typing.Optional[typing.Sequence[str]]


# TableRowConditionalFormattingOutputTypeDef

### BackgroundColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingColorOutputTypeDef]

### TextColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingColorOutputTypeDef]


# TableRowConditionalFormattingTypeDef

### BackgroundColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingColorTypeDef]

### TextColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingColorTypeDef]


# TableSideBorderOptionsTypeDef

### InnerVertical
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableBorderOptionsTypeDef]

### InnerHorizontal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableBorderOptionsTypeDef]

### Left
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableBorderOptionsTypeDef]

### Right
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableBorderOptionsTypeDef]

### Top
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableBorderOptionsTypeDef]

### Bottom
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableBorderOptionsTypeDef]


# TableSortConfigurationOutputTypeDef

### RowSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### PaginationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaginationConfigurationTypeDef]


# TableSortConfigurationTypeDef

### RowSort
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### PaginationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PaginationConfigurationTypeDef]


# TableStyleTargetTypeDef

### CellType
- **Type**: typing.Literal['METRIC_HEADER', 'TOTAL', 'VALUE']
- **Required**: Yes


# TableUnaggregatedFieldWellsOutputTypeDef

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.UnaggregatedFieldTypeDef]]


# TableUnaggregatedFieldWellsTypeDef

### Values
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.UnaggregatedFieldTypeDef]]


# TableVisualOutputTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableConfigurationOutputTypeDef]

### ConditionalFormatting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableConditionalFormattingOutputTypeDef]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionOutputTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# TableVisualTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableConfigurationTypeDef]

### ConditionalFormatting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableConditionalFormattingTypeDef]

### Actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# TagColumnOperationOutputTypeDef

### ColumnName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ColumnTagTypeDef]
- **Required**: Yes


# TagColumnOperationTypeDef

### ColumnName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ColumnTagTypeDef]
- **Required**: Yes


# TagColumnOperationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TagTypeDef]
- **Required**: Yes


# TagResourceResponseTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TemplateAliasTypeDef

### AliasName
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### TemplateVersionNumber
- **Type**: typing.Optional[int]


# TemplateErrorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TemplateSourceAnalysisTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetReferences
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DataSetReferenceTypeDef]
- **Required**: Yes


# TemplateSourceEntityTypeDef

### SourceAnalysis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TemplateSourceAnalysisTypeDef]

### SourceTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TemplateSourceTemplateTypeDef]


# TemplateSourceTemplateTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# TemplateSummaryTypeDef

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


# TemplateTypeDef

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TemplateVersionTypeDef]

### TemplateId
- **Type**: typing.Optional[str]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]


# TemplateVersionDefinitionOutputTypeDef

### DataSetConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DataSetConfigurationOutputTypeDef]
- **Required**: Yes

### Sheets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.SheetDefinitionOutputTypeDef]]

### CalculatedFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.CalculatedFieldTypeDef]]

### ParameterDeclarations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ParameterDeclarationOutputTypeDef]]

### FilterGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.FilterGroupOutputTypeDef]]

### ColumnConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ColumnConfigurationOutputTypeDef]]

### AnalysisDefaults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AnalysisDefaultsTypeDef]

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AssetOptionsTypeDef]

### QueryExecutionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.QueryExecutionOptionsTypeDef]

### StaticFiles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.StaticFileTypeDef]]


# TemplateVersionDefinitionTypeDef

### DataSetConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DataSetConfigurationTypeDef]
- **Required**: Yes

### Sheets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.SheetDefinitionTypeDef]]

### CalculatedFields
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.CalculatedFieldTypeDef]]

### ParameterDeclarations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ParameterDeclarationTypeDef]]

### FilterGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.FilterGroupTypeDef]]

### ColumnConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ColumnConfigurationTypeDef]]

### AnalysisDefaults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AnalysisDefaultsTypeDef]

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AssetOptionsTypeDef]

### QueryExecutionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.QueryExecutionOptionsTypeDef]

### StaticFiles
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.StaticFileTypeDef]]


# TemplateVersionDefinitionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TemplateVersionSummaryTypeDef

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


# TemplateVersionTypeDef

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### Errors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.TemplateErrorTypeDef]]

### VersionNumber
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['CREATION_FAILED', 'CREATION_IN_PROGRESS', 'CREATION_SUCCESSFUL', 'DELETED', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']]

### DataSetConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DataSetConfigurationOutputTypeDef]]

### Description
- **Type**: typing.Optional[str]

### SourceEntityArn
- **Type**: typing.Optional[str]

### ThemeArn
- **Type**: typing.Optional[str]

### Sheets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.SheetTypeDef]]


# TeradataParametersTypeDef

### Host
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes


# TextAreaControlDisplayOptionsTypeDef

### TitleOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LabelOptionsTypeDef]

### PlaceholderOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TextControlPlaceholderOptionsTypeDef]

### InfoIconLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SheetControlInfoIconLabelOptionsTypeDef]


# TextConditionalFormatOutputTypeDef

### BackgroundColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingColorOutputTypeDef]

### TextColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingColorOutputTypeDef]

### Icon
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingIconTypeDef]


# TextConditionalFormatTypeDef

### BackgroundColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingColorTypeDef]

### TextColor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingColorTypeDef]

### Icon
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ConditionalFormattingIconTypeDef]


# TextControlPlaceholderOptionsTypeDef

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# TextFieldControlDisplayOptionsTypeDef

### TitleOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LabelOptionsTypeDef]

### PlaceholderOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TextControlPlaceholderOptionsTypeDef]

### InfoIconLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SheetControlInfoIconLabelOptionsTypeDef]


# ThemeAliasTypeDef

### Arn
- **Type**: typing.Optional[str]

### AliasName
- **Type**: typing.Optional[str]

### ThemeVersionNumber
- **Type**: typing.Optional[int]


# ThemeConfigurationOutputTypeDef

### DataColorPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataColorPaletteOutputTypeDef]

### UIColorPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.UIColorPaletteTypeDef]

### Sheet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SheetStyleTypeDef]

### Typography
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TypographyOutputTypeDef]


# ThemeConfigurationTypeDef

### DataColorPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataColorPaletteTypeDef]

### UIColorPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.UIColorPaletteTypeDef]

### Sheet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SheetStyleTypeDef]

### Typography
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TypographyTypeDef]


# ThemeConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ThemeErrorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ThemeSummaryTypeDef

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


# ThemeTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ThemeVersionSummaryTypeDef

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


# ThemeVersionTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ThemeConfigurationOutputTypeDef]

### Errors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ThemeErrorTypeDef]]

### Status
- **Type**: typing.Optional[typing.Literal['CREATION_FAILED', 'CREATION_IN_PROGRESS', 'CREATION_SUCCESSFUL', 'DELETED', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']]


# ThousandSeparatorOptionsTypeDef

### Symbol
- **Type**: typing.Optional[typing.Literal['COMMA', 'DOT', 'SPACE']]

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### GroupingStyle
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'LAKHS']]


# TileLayoutStyleTypeDef

### Gutter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GutterStyleTypeDef]

### Margin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.MarginStyleTypeDef]


# TileStyleTypeDef

### Border
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BorderStyleTypeDef]


# TimeBasedForecastPropertiesTypeDef

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


# TimeEqualityFilterOutputTypeDef

### FilterId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[datetime.datetime]

### ParameterName
- **Type**: typing.Optional[str]

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### RollingDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RollingDateConfigurationTypeDef]

### DefaultFilterControlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultFilterControlConfigurationOutputTypeDef]


# TimeEqualityFilterTypeDef

### FilterId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TimestampTypeDef]

### ParameterName
- **Type**: typing.Optional[str]

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### RollingDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RollingDateConfigurationTypeDef]

### DefaultFilterControlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultFilterControlConfigurationTypeDef]


# TimeRangeDrillDownFilterOutputTypeDef

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
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


# TimeRangeDrillDownFilterTypeDef

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes

### RangeMinimum
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.TimestampTypeDef'>
- **Required**: Yes

### RangeMaximum
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.TimestampTypeDef'>
- **Required**: Yes

### TimeGranularity
- **Type**: typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']
- **Required**: Yes


# TimeRangeFilterOutputTypeDef

### FilterId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes

### NullOption
- **Type**: typing.Literal['ALL_VALUES', 'NON_NULLS_ONLY', 'NULLS_ONLY']
- **Required**: Yes

### IncludeMinimum
- **Type**: typing.Optional[bool]

### IncludeMaximum
- **Type**: typing.Optional[bool]

### RangeMinimumValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TimeRangeFilterValueOutputTypeDef]

### RangeMaximumValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TimeRangeFilterValueOutputTypeDef]

### ExcludePeriodConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ExcludePeriodConfigurationTypeDef]

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### DefaultFilterControlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultFilterControlConfigurationOutputTypeDef]


# TimeRangeFilterTypeDef

### FilterId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes

### NullOption
- **Type**: typing.Literal['ALL_VALUES', 'NON_NULLS_ONLY', 'NULLS_ONLY']
- **Required**: Yes

### IncludeMinimum
- **Type**: typing.Optional[bool]

### IncludeMaximum
- **Type**: typing.Optional[bool]

### RangeMinimumValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TimeRangeFilterValueTypeDef]

### RangeMaximumValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TimeRangeFilterValueTypeDef]

### ExcludePeriodConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ExcludePeriodConfigurationTypeDef]

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### DefaultFilterControlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultFilterControlConfigurationTypeDef]


# TimeRangeFilterValueOutputTypeDef

### StaticValue
- **Type**: typing.Optional[datetime.datetime]

### RollingDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RollingDateConfigurationTypeDef]

### Parameter
- **Type**: typing.Optional[str]


# TimeRangeFilterValueTypeDef

### StaticValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TimestampTypeDef]

### RollingDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RollingDateConfigurationTypeDef]

### Parameter
- **Type**: typing.Optional[str]


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TooltipItemTypeDef

### FieldTooltipItem
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FieldTooltipItemTypeDef]

### ColumnTooltipItem
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ColumnTooltipItemTypeDef]


# TooltipOptionsOutputTypeDef

### TooltipVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### SelectedTooltipType
- **Type**: typing.Optional[typing.Literal['BASIC', 'DETAILED']]

### FieldBasedTooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FieldBasedTooltipOutputTypeDef]


# TooltipOptionsTypeDef

### TooltipVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### SelectedTooltipType
- **Type**: typing.Optional[typing.Literal['BASIC', 'DETAILED']]

### FieldBasedTooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FieldBasedTooltipTypeDef]


# TopBottomFilterOutputTypeDef

### FilterId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes

### AggregationSortConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AggregationSortConfigurationTypeDef]
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### ParameterName
- **Type**: typing.Optional[str]

### DefaultFilterControlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultFilterControlConfigurationOutputTypeDef]


# TopBottomFilterTypeDef

### FilterId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes

### AggregationSortConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.AggregationSortConfigurationTypeDef]
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### ParameterName
- **Type**: typing.Optional[str]

### DefaultFilterControlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultFilterControlConfigurationTypeDef]


# TopBottomMoversComputationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TopBottomRankedComputationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TopicCalculatedFieldOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultFormattingTypeDef]

### Aggregation
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'COUNT', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]

### ComparativeOrder
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ComparativeOrderOutputTypeDef]

### SemanticType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SemanticTypeOutputTypeDef]

### AllowedAggregations
- **Type**: typing.Optional[typing.List[typing.Literal['AVERAGE', 'COUNT', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'PERCENTILE', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]]

### NotAllowedAggregations
- **Type**: typing.Optional[typing.List[typing.Literal['AVERAGE', 'COUNT', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'PERCENTILE', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]]

### NeverAggregateInFilter
- **Type**: typing.Optional[bool]

### CellValueSynonyms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.CellValueSynonymOutputTypeDef]]

### NonAdditive
- **Type**: typing.Optional[bool]


# TopicCalculatedFieldTypeDef

### CalculatedFieldName
- **Type**: <class 'str'>
- **Required**: Yes

### Expression
- **Type**: <class 'str'>
- **Required**: Yes

### CalculatedFieldDescription
- **Type**: typing.Optional[str]

### CalculatedFieldSynonyms
- **Type**: typing.Optional[typing.Sequence[str]]

### IsIncludedInTopic
- **Type**: typing.Optional[bool]

### DisableIndexing
- **Type**: typing.Optional[bool]

### ColumnDataRole
- **Type**: typing.Optional[typing.Literal['DIMENSION', 'MEASURE']]

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### DefaultFormatting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultFormattingTypeDef]

### Aggregation
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'COUNT', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]

### ComparativeOrder
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ComparativeOrderTypeDef]

### SemanticType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SemanticTypeTypeDef]

### AllowedAggregations
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AVERAGE', 'COUNT', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'PERCENTILE', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]]

### NotAllowedAggregations
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AVERAGE', 'COUNT', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'PERCENTILE', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]]

### NeverAggregateInFilter
- **Type**: typing.Optional[bool]

### CellValueSynonyms
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.CellValueSynonymTypeDef]]

### NonAdditive
- **Type**: typing.Optional[bool]


# TopicCategoryFilterConstantOutputTypeDef

### ConstantType
- **Type**: typing.Optional[typing.Literal['COLLECTIVE', 'RANGE', 'SINGULAR']]

### SingularConstant
- **Type**: typing.Optional[str]

### CollectiveConstant
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CollectiveConstantOutputTypeDef]


# TopicCategoryFilterConstantTypeDef

### ConstantType
- **Type**: typing.Optional[typing.Literal['COLLECTIVE', 'RANGE', 'SINGULAR']]

### SingularConstant
- **Type**: typing.Optional[str]

### CollectiveConstant
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CollectiveConstantTypeDef]


# TopicCategoryFilterOutputTypeDef

### CategoryFilterFunction
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EXACT']]

### CategoryFilterType
- **Type**: typing.Optional[typing.Literal['CUSTOM_FILTER', 'CUSTOM_FILTER_LIST', 'FILTER_LIST']]

### Constant
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicCategoryFilterConstantOutputTypeDef]

### Inverse
- **Type**: typing.Optional[bool]


# TopicCategoryFilterTypeDef

### CategoryFilterFunction
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EXACT']]

### CategoryFilterType
- **Type**: typing.Optional[typing.Literal['CUSTOM_FILTER', 'CUSTOM_FILTER_LIST', 'FILTER_LIST']]

### Constant
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicCategoryFilterConstantTypeDef]

### Inverse
- **Type**: typing.Optional[bool]


# TopicColumnOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ComparativeOrderOutputTypeDef]

### SemanticType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SemanticTypeOutputTypeDef]

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### AllowedAggregations
- **Type**: typing.Optional[typing.List[typing.Literal['AVERAGE', 'COUNT', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'PERCENTILE', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]]

### NotAllowedAggregations
- **Type**: typing.Optional[typing.List[typing.Literal['AVERAGE', 'COUNT', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'PERCENTILE', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]]

### DefaultFormatting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultFormattingTypeDef]

### NeverAggregateInFilter
- **Type**: typing.Optional[bool]

### CellValueSynonyms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.CellValueSynonymOutputTypeDef]]

### NonAdditive
- **Type**: typing.Optional[bool]


# TopicColumnTypeDef

### ColumnName
- **Type**: <class 'str'>
- **Required**: Yes

### ColumnFriendlyName
- **Type**: typing.Optional[str]

### ColumnDescription
- **Type**: typing.Optional[str]

### ColumnSynonyms
- **Type**: typing.Optional[typing.Sequence[str]]

### ColumnDataRole
- **Type**: typing.Optional[typing.Literal['DIMENSION', 'MEASURE']]

### Aggregation
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'COUNT', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]

### IsIncludedInTopic
- **Type**: typing.Optional[bool]

### DisableIndexing
- **Type**: typing.Optional[bool]

### ComparativeOrder
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ComparativeOrderTypeDef]

### SemanticType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SemanticTypeTypeDef]

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### AllowedAggregations
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AVERAGE', 'COUNT', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'PERCENTILE', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]]

### NotAllowedAggregations
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AVERAGE', 'COUNT', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'PERCENTILE', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]]

### DefaultFormatting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DefaultFormattingTypeDef]

### NeverAggregateInFilter
- **Type**: typing.Optional[bool]

### CellValueSynonyms
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.CellValueSynonymTypeDef]]

### NonAdditive
- **Type**: typing.Optional[bool]


# TopicConfigOptionsTypeDef

### QBusinessInsightsEnabled
- **Type**: typing.Optional[bool]


# TopicConstantValueOutputTypeDef

### ConstantType
- **Type**: typing.Optional[typing.Literal['COLLECTIVE', 'RANGE', 'SINGULAR']]

### Value
- **Type**: typing.Optional[str]

### Minimum
- **Type**: typing.Optional[str]

### Maximum
- **Type**: typing.Optional[str]

### ValueList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.CollectiveConstantEntryTypeDef]]


# TopicConstantValueTypeDef

### ConstantType
- **Type**: typing.Optional[typing.Literal['COLLECTIVE', 'RANGE', 'SINGULAR']]

### Value
- **Type**: typing.Optional[str]

### Minimum
- **Type**: typing.Optional[str]

### Maximum
- **Type**: typing.Optional[str]

### ValueList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.CollectiveConstantEntryTypeDef]]


# TopicConstantValueUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TopicDateRangeFilterTypeDef

### Inclusive
- **Type**: typing.Optional[bool]

### Constant
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicRangeFilterConstantTypeDef]


# TopicDetailsOutputTypeDef

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### UserExperienceVersion
- **Type**: typing.Optional[typing.Literal['LEGACY', 'NEW_READER_EXPERIENCE']]

### DataSets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DatasetMetadataOutputTypeDef]]

### ConfigOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicConfigOptionsTypeDef]


# TopicDetailsTypeDef

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### UserExperienceVersion
- **Type**: typing.Optional[typing.Literal['LEGACY', 'NEW_READER_EXPERIENCE']]

### DataSets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DatasetMetadataTypeDef]]

### ConfigOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicConfigOptionsTypeDef]


# TopicDetailsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TopicFilterOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicCategoryFilterOutputTypeDef]

### NumericEqualityFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicNumericEqualityFilterTypeDef]

### NumericRangeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicNumericRangeFilterTypeDef]

### DateRangeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicDateRangeFilterTypeDef]

### RelativeDateFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicRelativeDateFilterTypeDef]


# TopicFilterTypeDef

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
- **Type**: typing.Optional[typing.Sequence[str]]

### FilterType
- **Type**: typing.Optional[typing.Literal['CATEGORY_FILTER', 'DATE_RANGE_FILTER', 'NUMERIC_EQUALITY_FILTER', 'NUMERIC_RANGE_FILTER', 'RELATIVE_DATE_FILTER']]

### CategoryFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicCategoryFilterTypeDef]

### NumericEqualityFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicNumericEqualityFilterTypeDef]

### NumericRangeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicNumericRangeFilterTypeDef]

### DateRangeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicDateRangeFilterTypeDef]

### RelativeDateFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicRelativeDateFilterTypeDef]


# TopicIRComparisonMethodTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TopicIRContributionAnalysisOutputTypeDef

### Factors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ContributionAnalysisFactorTypeDef]]

### TimeRanges
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ContributionAnalysisTimeRangesOutputTypeDef]

### Direction
- **Type**: typing.Optional[typing.Literal['DECREASE', 'INCREASE', 'NEUTRAL']]

### SortType
- **Type**: typing.Optional[typing.Literal['ABSOLUTE_DIFFERENCE', 'CONTRIBUTION_PERCENTAGE', 'DEVIATION_FROM_EXPECTED', 'PERCENTAGE_DIFFERENCE']]


# TopicIRContributionAnalysisTypeDef

### Factors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ContributionAnalysisFactorTypeDef]]

### TimeRanges
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ContributionAnalysisTimeRangesUnionTypeDef]

### Direction
- **Type**: typing.Optional[typing.Literal['DECREASE', 'INCREASE', 'NEUTRAL']]

### SortType
- **Type**: typing.Optional[typing.Literal['ABSOLUTE_DIFFERENCE', 'CONTRIBUTION_PERCENTAGE', 'DEVIATION_FROM_EXPECTED', 'PERCENTAGE_DIFFERENCE']]


# TopicIRContributionAnalysisUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TopicIRFilterOptionOutputTypeDef

### FilterType
- **Type**: typing.Optional[typing.Literal['ACCEPT_ALL_FILTER', 'CATEGORY_FILTER', 'DATE_RANGE_FILTER', 'EQUALS', 'NUMERIC_EQUALITY_FILTER', 'NUMERIC_RANGE_FILTER', 'RANK_LIMIT_FILTER', 'RELATIVE_DATE_FILTER', 'TOP_BOTTOM_FILTER']]

### FilterClass
- **Type**: typing.Optional[typing.Literal['CONDITIONAL_VALUE_FILTER', 'ENFORCED_VALUE_FILTER', 'NAMED_VALUE_FILTER']]

### OperandField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.IdentifierTypeDef]

### Function
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'CONTAINS_STRING', 'ENDS_WITH', 'EXACT', 'LAST', 'NEXT', 'NOW', 'PREVIOUS', 'STARTS_WITH', 'THIS']]

### Constant
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicConstantValueOutputTypeDef]

### Inverse
- **Type**: typing.Optional[bool]

### NullFilter
- **Type**: typing.Optional[typing.Literal['ALL_VALUES', 'NON_NULLS_ONLY', 'NULLS_ONLY']]

### Aggregation
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'COLUMN', 'COUNT', 'CUSTOM', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'PERCENTILE', 'PTD_AVERAGE', 'PTD_COUNT', 'PTD_DISTINCT_COUNT', 'PTD_MAX', 'PTD_MIN', 'PTD_SUM', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]

### AggregationFunctionParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### AggregationPartitionBy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.AggregationPartitionByTypeDef]]

### Range
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicConstantValueOutputTypeDef]

### Inclusive
- **Type**: typing.Optional[bool]

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### LastNextOffset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicConstantValueOutputTypeDef]

### AggMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.FilterAggMetricsTypeDef]]

### TopBottomLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicConstantValueOutputTypeDef]

### SortDirection
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### Anchor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AnchorTypeDef]


# TopicIRFilterOptionTypeDef

### FilterType
- **Type**: typing.Optional[typing.Literal['ACCEPT_ALL_FILTER', 'CATEGORY_FILTER', 'DATE_RANGE_FILTER', 'EQUALS', 'NUMERIC_EQUALITY_FILTER', 'NUMERIC_RANGE_FILTER', 'RANK_LIMIT_FILTER', 'RELATIVE_DATE_FILTER', 'TOP_BOTTOM_FILTER']]

### FilterClass
- **Type**: typing.Optional[typing.Literal['CONDITIONAL_VALUE_FILTER', 'ENFORCED_VALUE_FILTER', 'NAMED_VALUE_FILTER']]

### OperandField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.IdentifierTypeDef]

### Function
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'CONTAINS_STRING', 'ENDS_WITH', 'EXACT', 'LAST', 'NEXT', 'NOW', 'PREVIOUS', 'STARTS_WITH', 'THIS']]

### Constant
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicConstantValueUnionTypeDef]

### Inverse
- **Type**: typing.Optional[bool]

### NullFilter
- **Type**: typing.Optional[typing.Literal['ALL_VALUES', 'NON_NULLS_ONLY', 'NULLS_ONLY']]

### Aggregation
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'COLUMN', 'COUNT', 'CUSTOM', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'PERCENTILE', 'PTD_AVERAGE', 'PTD_COUNT', 'PTD_DISTINCT_COUNT', 'PTD_MAX', 'PTD_MIN', 'PTD_SUM', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]

### AggregationFunctionParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### AggregationPartitionBy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.AggregationPartitionByTypeDef]]

### Range
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicConstantValueUnionTypeDef]

### Inclusive
- **Type**: typing.Optional[bool]

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MILLISECOND', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### LastNextOffset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicConstantValueUnionTypeDef]

### AggMetrics
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.FilterAggMetricsTypeDef]]

### TopBottomLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicConstantValueUnionTypeDef]

### SortDirection
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### Anchor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AnchorTypeDef]


# TopicIRFilterOptionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TopicIRGroupByTypeDef

### FieldName
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.IdentifierTypeDef]

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### Sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicSortClauseTypeDef]

### DisplayFormat
- **Type**: typing.Optional[typing.Literal['AUTO', 'CURRENCY', 'DATE', 'NUMBER', 'PERCENT', 'STRING']]

### DisplayFormatOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DisplayFormatOptionsTypeDef]

### NamedEntity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NamedEntityRefTypeDef]


# TopicIRMetricOutputTypeDef

### MetricId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.IdentifierTypeDef]

### Function
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AggFunctionOutputTypeDef]

### Operands
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.IdentifierTypeDef]]

### ComparisonMethod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicIRComparisonMethodTypeDef]

### Expression
- **Type**: typing.Optional[str]

### CalculatedFieldReferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.IdentifierTypeDef]]

### DisplayFormat
- **Type**: typing.Optional[typing.Literal['AUTO', 'CURRENCY', 'DATE', 'NUMBER', 'PERCENT', 'STRING']]

### DisplayFormatOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DisplayFormatOptionsTypeDef]

### NamedEntity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NamedEntityRefTypeDef]


# TopicIRMetricTypeDef

### MetricId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.IdentifierTypeDef]

### Function
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AggFunctionUnionTypeDef]

### Operands
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.IdentifierTypeDef]]

### ComparisonMethod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicIRComparisonMethodTypeDef]

### Expression
- **Type**: typing.Optional[str]

### CalculatedFieldReferences
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.IdentifierTypeDef]]

### DisplayFormat
- **Type**: typing.Optional[typing.Literal['AUTO', 'CURRENCY', 'DATE', 'NUMBER', 'PERCENT', 'STRING']]

### DisplayFormatOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DisplayFormatOptionsTypeDef]

### NamedEntity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.NamedEntityRefTypeDef]


# TopicIRMetricUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TopicIROutputTypeDef

### Metrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.TopicIRMetricOutputTypeDef]]

### GroupByList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.TopicIRGroupByTypeDef]]

### Filters
- **Type**: typing.Optional[typing.List[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.TopicIRFilterOptionOutputTypeDef]]]

### Sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicSortClauseTypeDef]

### ContributionAnalysis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicIRContributionAnalysisOutputTypeDef]

### Visual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualOptionsTypeDef]


# TopicIRTypeDef

### Metrics
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TopicIRMetricUnionTypeDef]]

### GroupByList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TopicIRGroupByTypeDef]]

### Filters
- **Type**: typing.Optional[typing.Sequence[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TopicIRFilterOptionUnionTypeDef]]]

### Sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicSortClauseTypeDef]

### ContributionAnalysis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicIRContributionAnalysisUnionTypeDef]

### Visual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualOptionsTypeDef]


# TopicIRUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TopicNamedEntityOutputTypeDef

### EntityName
- **Type**: <class 'str'>
- **Required**: Yes

### EntityDescription
- **Type**: typing.Optional[str]

### EntitySynonyms
- **Type**: typing.Optional[typing.List[str]]

### SemanticEntityType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SemanticEntityTypeOutputTypeDef]

### Definition
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.NamedEntityDefinitionOutputTypeDef]]


# TopicNamedEntityTypeDef

### EntityName
- **Type**: <class 'str'>
- **Required**: Yes

### EntityDescription
- **Type**: typing.Optional[str]

### EntitySynonyms
- **Type**: typing.Optional[typing.Sequence[str]]

### SemanticEntityType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SemanticEntityTypeTypeDef]

### Definition
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.NamedEntityDefinitionTypeDef]]


# TopicNumericEqualityFilterTypeDef

### Constant
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicSingularFilterConstantTypeDef]

### Aggregation
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'COUNT', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'NO_AGGREGATION', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]


# TopicNumericRangeFilterTypeDef

### Inclusive
- **Type**: typing.Optional[bool]

### Constant
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicRangeFilterConstantTypeDef]

### Aggregation
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'COUNT', 'DISTINCT_COUNT', 'MAX', 'MEDIAN', 'MIN', 'NO_AGGREGATION', 'STDEV', 'STDEVP', 'SUM', 'VAR', 'VARP']]


# TopicRangeFilterConstantTypeDef

### ConstantType
- **Type**: typing.Optional[typing.Literal['COLLECTIVE', 'RANGE', 'SINGULAR']]

### RangeConstant
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RangeConstantTypeDef]


# TopicRefreshDetailsTypeDef

### RefreshArn
- **Type**: typing.Optional[str]

### RefreshId
- **Type**: typing.Optional[str]

### RefreshStatus
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'FAILED', 'INITIALIZED', 'RUNNING']]


# TopicRefreshScheduleOutputTypeDef

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


# TopicRefreshScheduleSummaryTypeDef

### DatasetId
- **Type**: typing.Optional[str]

### DatasetArn
- **Type**: typing.Optional[str]

### DatasetName
- **Type**: typing.Optional[str]

### RefreshSchedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicRefreshScheduleOutputTypeDef]


# TopicRefreshScheduleTypeDef

### IsEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### BasedOnSpiceSchedule
- **Type**: <class 'bool'>
- **Required**: Yes

### StartingAt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TimestampTypeDef]

### Timezone
- **Type**: typing.Optional[str]

### RepeatAt
- **Type**: typing.Optional[str]

### TopicScheduleType
- **Type**: typing.Optional[typing.Literal['DAILY', 'HOURLY', 'MONTHLY', 'WEEKLY']]


# TopicRefreshScheduleUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TopicRelativeDateFilterTypeDef

### TimeGranularity
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MINUTE', 'MONTH', 'QUARTER', 'SECOND', 'WEEK', 'YEAR']]

### RelativeDateFilterFunction
- **Type**: typing.Optional[typing.Literal['LAST', 'NEXT', 'NOW', 'PREVIOUS', 'THIS']]

### Constant
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicSingularFilterConstantTypeDef]


# TopicReviewedAnswerTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicIROutputTypeDef]

### PrimaryVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicVisualOutputTypeDef]

### Template
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicTemplateOutputTypeDef]


# TopicSearchFilterTypeDef

### Operator
- **Type**: typing.Literal['StringEquals', 'StringLike']
- **Required**: Yes

### Name
- **Type**: typing.Literal['DIRECT_QUICKSIGHT_OWNER', 'DIRECT_QUICKSIGHT_SOLE_OWNER', 'DIRECT_QUICKSIGHT_VIEWER_OR_OWNER', 'QUICKSIGHT_OWNER', 'QUICKSIGHT_USER', 'QUICKSIGHT_VIEWER_OR_OWNER', 'TOPIC_NAME']
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TopicSingularFilterConstantTypeDef

### ConstantType
- **Type**: typing.Optional[typing.Literal['COLLECTIVE', 'RANGE', 'SINGULAR']]

### SingularConstant
- **Type**: typing.Optional[str]


# TopicSortClauseTypeDef

### Operand
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.IdentifierTypeDef]

### SortDirection
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# TopicSummaryTypeDef

### Arn
- **Type**: typing.Optional[str]

### TopicId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### UserExperienceVersion
- **Type**: typing.Optional[typing.Literal['LEGACY', 'NEW_READER_EXPERIENCE']]


# TopicTemplateOutputTypeDef

### TemplateType
- **Type**: typing.Optional[str]

### Slots
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.SlotTypeDef]]


# TopicTemplateTypeDef

### TemplateType
- **Type**: typing.Optional[str]

### Slots
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.SlotTypeDef]]


# TopicTemplateUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TopicVisualOutputTypeDef

### VisualId
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[typing.Literal['COMPLIMENTARY', 'FALLBACK', 'FRAGMENT', 'MULTI_INTENT', 'PRIMARY']]

### Ir
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicIROutputTypeDef]

### SupportingVisuals
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# TopicVisualTypeDef

### VisualId
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[typing.Literal['COMPLIMENTARY', 'FALLBACK', 'FRAGMENT', 'MULTI_INTENT', 'PRIMARY']]

### Ir
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TopicIRUnionTypeDef]

### SupportingVisuals
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]


# TopicVisualUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TotalAggregationComputationTypeDef

### ComputationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]


# TotalAggregationFunctionTypeDef

### SimpleTotalAggregationFunction
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'DEFAULT', 'MAX', 'MIN', 'NONE', 'SUM']]


# TotalAggregationOptionTypeDef

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### TotalAggregationFunction
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.TotalAggregationFunctionTypeDef'>
- **Required**: Yes


# TotalOptionsOutputTypeDef

### TotalsVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### Placement
- **Type**: typing.Optional[typing.Literal['AUTO', 'END', 'START']]

### ScrollStatus
- **Type**: typing.Optional[typing.Literal['PINNED', 'SCROLLED']]

### CustomLabel
- **Type**: typing.Optional[str]

### TotalCellStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableCellStyleTypeDef]

### TotalAggregationOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.TotalAggregationOptionTypeDef]]


# TotalOptionsTypeDef

### TotalsVisibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### Placement
- **Type**: typing.Optional[typing.Literal['AUTO', 'END', 'START']]

### ScrollStatus
- **Type**: typing.Optional[typing.Literal['PINNED', 'SCROLLED']]

### CustomLabel
- **Type**: typing.Optional[str]

### TotalCellStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableCellStyleTypeDef]

### TotalAggregationOptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.TotalAggregationOptionTypeDef]]


# TransformOperationOutputTypeDef

### ProjectOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ProjectOperationOutputTypeDef]

### FilterOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FilterOperationTypeDef]

### CreateColumnsOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CreateColumnsOperationOutputTypeDef]

### RenameColumnOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RenameColumnOperationTypeDef]

### CastColumnTypeOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CastColumnTypeOperationTypeDef]

### TagColumnOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TagColumnOperationOutputTypeDef]

### UntagColumnOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.UntagColumnOperationOutputTypeDef]

### OverrideDatasetParameterOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.OverrideDatasetParameterOperationOutputTypeDef]


# TransformOperationTypeDef

### ProjectOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ProjectOperationUnionTypeDef]

### FilterOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FilterOperationTypeDef]

### CreateColumnsOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CreateColumnsOperationUnionTypeDef]

### RenameColumnOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RenameColumnOperationTypeDef]

### CastColumnTypeOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CastColumnTypeOperationTypeDef]

### TagColumnOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TagColumnOperationUnionTypeDef]

### UntagColumnOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.UntagColumnOperationUnionTypeDef]

### OverrideDatasetParameterOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.OverrideDatasetParameterOperationUnionTypeDef]


# TransformOperationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TreeMapAggregatedFieldWellsOutputTypeDef

### Groups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Sizes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]

### Colors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]


# TreeMapAggregatedFieldWellsTypeDef

### Groups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Sizes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]

### Colors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]


# TreeMapConfigurationOutputTypeDef

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TreeMapFieldWellsOutputTypeDef]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TreeMapSortConfigurationOutputTypeDef]

### GroupLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsOutputTypeDef]

### SizeLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsOutputTypeDef]

### ColorLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsOutputTypeDef]

### ColorScale
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ColorScaleOutputTypeDef]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LegendOptionsTypeDef]

### DataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataLabelOptionsOutputTypeDef]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TooltipOptionsOutputTypeDef]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# TreeMapConfigurationTypeDef

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TreeMapFieldWellsTypeDef]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TreeMapSortConfigurationTypeDef]

### GroupLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsTypeDef]

### SizeLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsTypeDef]

### ColorLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsTypeDef]

### ColorScale
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ColorScaleTypeDef]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LegendOptionsTypeDef]

### DataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataLabelOptionsTypeDef]

### Tooltip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TooltipOptionsTypeDef]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# TreeMapFieldWellsOutputTypeDef

### TreeMapAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TreeMapAggregatedFieldWellsOutputTypeDef]


# TreeMapFieldWellsTypeDef

### TreeMapAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TreeMapAggregatedFieldWellsTypeDef]


# TreeMapSortConfigurationOutputTypeDef

### TreeMapSort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### TreeMapGroupItemsLimitConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]


# TreeMapSortConfigurationTypeDef

### TreeMapSort
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### TreeMapGroupItemsLimitConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]


# TreeMapVisualOutputTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TreeMapConfigurationOutputTypeDef]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionOutputTypeDef]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ColumnHierarchyOutputTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# TreeMapVisualTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TreeMapConfigurationTypeDef]

### Actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionTypeDef]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ColumnHierarchyTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# TrendArrowOptionsTypeDef

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]


# TrinoParametersTypeDef

### Host
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes


# TwitterParametersTypeDef

### Query
- **Type**: <class 'str'>
- **Required**: Yes

### MaxRows
- **Type**: <class 'int'>
- **Required**: Yes


# TypographyOutputTypeDef

### FontFamilies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.FontTypeDef]]


# TypographyTypeDef

### FontFamilies
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.FontTypeDef]]


# UIColorPaletteTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UnaggregatedFieldTypeDef

### FieldId
- **Type**: <class 'str'>
- **Required**: Yes

### Column
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ColumnIdentifierTypeDef'>
- **Required**: Yes

### FormatConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FormatConfigurationTypeDef]


# UniqueKeyOutputTypeDef

### ColumnNames
- **Type**: typing.List[str]
- **Required**: Yes


# UniqueKeyTypeDef

### ColumnNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UniqueValuesComputationTypeDef

### ComputationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Category
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]


# UntagColumnOperationOutputTypeDef

### ColumnName
- **Type**: <class 'str'>
- **Required**: Yes

### TagNames
- **Type**: typing.List[typing.Literal['COLUMN_DESCRIPTION', 'COLUMN_GEOGRAPHIC_ROLE']]
- **Required**: Yes


# UntagColumnOperationTypeDef

### ColumnName
- **Type**: <class 'str'>
- **Required**: Yes

### TagNames
- **Type**: typing.Sequence[typing.Literal['COLUMN_DESCRIPTION', 'COLUMN_GEOGRAPHIC_ROLE']]
- **Required**: Yes


# UntagColumnOperationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UntagResourceResponseTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAccountCustomizationRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountCustomization
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.AccountCustomizationTypeDef'>
- **Required**: Yes

### Namespace
- **Type**: typing.Optional[str]


# UpdateAccountCustomizationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.AccountCustomizationTypeDef'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAccountSettingsRequestTypeDef

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


# UpdateAccountSettingsResponseTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAnalysisPermissionsRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AnalysisId
- **Type**: <class 'str'>
- **Required**: Yes

### GrantPermissions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionUnionTypeDef]]

### RevokePermissions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionUnionTypeDef]]


# UpdateAnalysisPermissionsResponseTypeDef

### AnalysisArn
- **Type**: <class 'str'>
- **Required**: Yes

### AnalysisId
- **Type**: <class 'str'>
- **Required**: Yes

### Permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionOutputTypeDef]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAnalysisRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ParametersUnionTypeDef]

### SourceEntity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AnalysisSourceEntityTypeDef]

### ThemeArn
- **Type**: typing.Optional[str]

### Definition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AnalysisDefinitionUnionTypeDef]

### ValidationStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ValidationStrategyTypeDef]


# UpdateAnalysisResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateApplicationWithTokenExchangeGrantRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateApplicationWithTokenExchangeGrantResponseTypeDef

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateBrandAssignmentRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BrandArn
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateBrandAssignmentResponseTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### BrandArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateBrandPublishedVersionRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BrandId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateBrandPublishedVersionResponseTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateBrandRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BrandId
- **Type**: <class 'str'>
- **Required**: Yes

### BrandDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BrandDefinitionTypeDef]


# UpdateBrandResponseTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### BrandDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.BrandDetailTypeDef'>
- **Required**: Yes

### BrandDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.BrandDefinitionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateCustomPermissionsRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### CustomPermissionsName
- **Type**: <class 'str'>
- **Required**: Yes

### Capabilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CapabilitiesTypeDef]


# UpdateCustomPermissionsResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDashboardLinksRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### LinkEntities
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDashboardLinksResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDashboardPermissionsRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### GrantPermissions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionUnionTypeDef]]

### RevokePermissions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionUnionTypeDef]]

### GrantLinkPermissions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionUnionTypeDef]]

### RevokeLinkPermissions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionUnionTypeDef]]


# UpdateDashboardPermissionsResponseTypeDef

### DashboardArn
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### Permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionOutputTypeDef]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### LinkSharingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.LinkSharingConfigurationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDashboardPublishedVersionRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: <class 'int'>
- **Required**: Yes


# UpdateDashboardPublishedVersionResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDashboardRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DashboardSourceEntityTypeDef]

### Parameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ParametersUnionTypeDef]

### VersionDescription
- **Type**: typing.Optional[str]

### DashboardPublishOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DashboardPublishOptionsTypeDef]

### ThemeArn
- **Type**: typing.Optional[str]

### Definition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DashboardVersionDefinitionUnionTypeDef]

### ValidationStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ValidationStrategyTypeDef]


# UpdateDashboardResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDashboardsQAConfigurationRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardsQAStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# UpdateDashboardsQAConfigurationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDataSetPermissionsRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### GrantPermissions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionUnionTypeDef]]

### RevokePermissions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionUnionTypeDef]]


# UpdateDataSetPermissionsResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDataSetRequestTypeDef

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
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.quicksight_classes.PhysicalTableUnionTypeDef]
- **Required**: Yes

### ImportMode
- **Type**: typing.Literal['DIRECT_QUERY', 'SPICE']
- **Required**: Yes

### LogicalTableMap
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.quicksight_classes.LogicalTableUnionTypeDef]]

### ColumnGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ColumnGroupUnionTypeDef]]

### FieldFolders
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.quicksight_classes.FieldFolderUnionTypeDef]]

### RowLevelPermissionDataSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RowLevelPermissionDataSetTypeDef]

### RowLevelPermissionTagConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RowLevelPermissionTagConfigurationUnionTypeDef]

### ColumnLevelPermissionRules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ColumnLevelPermissionRuleUnionTypeDef]]

### DataSetUsageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataSetUsageConfigurationTypeDef]

### DatasetParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DatasetParameterUnionTypeDef]]

### PerformanceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PerformanceConfigurationUnionTypeDef]


# UpdateDataSetResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDataSourcePermissionsRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### GrantPermissions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionUnionTypeDef]]

### RevokePermissions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionUnionTypeDef]]


# UpdateDataSourcePermissionsResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDataSourceRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataSourceParametersUnionTypeDef]

### Credentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataSourceCredentialsTypeDef]

### VpcConnectionProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VpcConnectionPropertiesTypeDef]

### SslProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SslPropertiesTypeDef]


# UpdateDataSourceResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDefaultQBusinessApplicationRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: typing.Optional[str]


# UpdateDefaultQBusinessApplicationResponseTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFolderPermissionsRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes

### GrantPermissions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionUnionTypeDef]]

### RevokePermissions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionUnionTypeDef]]


# UpdateFolderPermissionsResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionOutputTypeDef]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFolderRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### FolderId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateFolderResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateGroupRequestTypeDef

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


# UpdateGroupResponseTypeDef

### Group
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.GroupTypeDef'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateIAMPolicyAssignmentRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]


# UpdateIAMPolicyAssignmentResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateIdentityPropagationConfigRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Service
- **Type**: typing.Literal['QBUSINESS', 'REDSHIFT']
- **Required**: Yes

### AuthorizedTargets
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateIdentityPropagationConfigResponseTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateIpRestrictionRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### IpRestrictionRuleMap
- **Type**: typing.Optional[typing.Mapping[str, str]]

### VpcIdRestrictionRuleMap
- **Type**: typing.Optional[typing.Mapping[str, str]]

### VpcEndpointIdRestrictionRuleMap
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Enabled
- **Type**: typing.Optional[bool]


# UpdateIpRestrictionResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateKeyRegistrationRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### KeyRegistration
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.RegisteredCustomerManagedKeyTypeDef]
- **Required**: Yes


# UpdateKeyRegistrationResponseTypeDef

### FailedKeyRegistration
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.FailedKeyRegistrationEntryTypeDef]
- **Required**: Yes

### SuccessfulKeyRegistration
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.SuccessfulKeyRegistrationEntryTypeDef]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePublicSharingSettingsRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PublicSharingEnabled
- **Type**: typing.Optional[bool]


# UpdatePublicSharingSettingsResponseTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateQPersonalizationConfigurationRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PersonalizationMode
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# UpdateQPersonalizationConfigurationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateQuickSightQSearchConfigurationRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### QSearchStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# UpdateQuickSightQSearchConfigurationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRefreshScheduleRequestTypeDef

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Schedule
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.RefreshScheduleUnionTypeDef'>
- **Required**: Yes


# UpdateRefreshScheduleResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRoleCustomPermissionRequestTypeDef

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


# UpdateRoleCustomPermissionResponseTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSPICECapacityConfigurationRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PurchaseMode
- **Type**: typing.Literal['AUTO_PURCHASE', 'MANUAL']
- **Required**: Yes


# UpdateSPICECapacityConfigurationResponseTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTemplateAliasRequestTypeDef

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


# UpdateTemplateAliasResponseTypeDef

### TemplateAlias
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.TemplateAliasTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTemplatePermissionsRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### GrantPermissions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionUnionTypeDef]]

### RevokePermissions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionUnionTypeDef]]


# UpdateTemplatePermissionsResponseTypeDef

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### Permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionOutputTypeDef]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTemplateRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### SourceEntity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TemplateSourceEntityTypeDef]

### VersionDescription
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Definition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TemplateVersionDefinitionUnionTypeDef]

### ValidationStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ValidationStrategyTypeDef]


# UpdateTemplateResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateThemeAliasRequestTypeDef

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


# UpdateThemeAliasResponseTypeDef

### ThemeAlias
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ThemeAliasTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateThemePermissionsRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ThemeId
- **Type**: <class 'str'>
- **Required**: Yes

### GrantPermissions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionUnionTypeDef]]

### RevokePermissions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionUnionTypeDef]]


# UpdateThemePermissionsResponseTypeDef

### ThemeId
- **Type**: <class 'str'>
- **Required**: Yes

### ThemeArn
- **Type**: <class 'str'>
- **Required**: Yes

### Permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionOutputTypeDef]
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateThemeRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ThemeConfigurationUnionTypeDef]


# UpdateThemeResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTopicPermissionsRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### GrantPermissions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionUnionTypeDef]]

### RevokePermissions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionUnionTypeDef]]


# UpdateTopicPermissionsResponseTypeDef

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### Permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ResourcePermissionOutputTypeDef]
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTopicRefreshScheduleRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.TopicRefreshScheduleUnionTypeDef'>
- **Required**: Yes


# UpdateTopicRefreshScheduleResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTopicRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicId
- **Type**: <class 'str'>
- **Required**: Yes

### Topic
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.TopicDetailsUnionTypeDef'>
- **Required**: Yes


# UpdateTopicResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateUserCustomPermissionRequestTypeDef

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


# UpdateUserCustomPermissionResponseTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateUserRequestTypeDef

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


# UpdateUserResponseTypeDef

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.UserTypeDef'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateVPCConnectionRequestTypeDef

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
- **Type**: typing.Sequence[str]
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### DnsResolvers
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateVPCConnectionResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UploadSettingsTypeDef

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


# UserTypeDef

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


# VPCConnectionSummaryTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.NetworkInterfaceTypeDef]]

### RoleArn
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]


# VPCConnectionTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.NetworkInterfaceTypeDef]]

### RoleArn
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]


# ValidationStrategyTypeDef

### Mode
- **Type**: typing.Literal['LENIENT', 'STRICT']
- **Required**: Yes


# VisibleRangeOptionsTypeDef

### PercentRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PercentVisibleRangeTypeDef]


# VisualAxisSortOptionTypeDef

### AvailabilityStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# VisualCustomActionOperationOutputTypeDef

### FilterOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CustomActionFilterOperationOutputTypeDef]

### NavigationOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CustomActionNavigationOperationTypeDef]

### URLOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CustomActionURLOperationTypeDef]

### SetParametersOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CustomActionSetParametersOperationOutputTypeDef]


# VisualCustomActionOperationTypeDef

### FilterOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CustomActionFilterOperationTypeDef]

### NavigationOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CustomActionNavigationOperationTypeDef]

### URLOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CustomActionURLOperationTypeDef]

### SetParametersOperation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CustomActionSetParametersOperationTypeDef]


# VisualCustomActionOutputTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionOperationOutputTypeDef]
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# VisualCustomActionTypeDef

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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionOperationTypeDef]
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# VisualInteractionOptionsTypeDef

### VisualMenuOption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualMenuOptionTypeDef]

### ContextMenuOption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ContextMenuOptionTypeDef]


# VisualMenuOptionTypeDef

### AvailabilityStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# VisualOptionsTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VisualOutputTypeDef

### TableVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableVisualOutputTypeDef]

### PivotTableVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PivotTableVisualOutputTypeDef]

### BarChartVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BarChartVisualOutputTypeDef]

### KPIVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.KPIVisualOutputTypeDef]

### PieChartVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PieChartVisualOutputTypeDef]

### GaugeChartVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GaugeChartVisualOutputTypeDef]

### LineChartVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LineChartVisualOutputTypeDef]

### HeatMapVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.HeatMapVisualOutputTypeDef]

### TreeMapVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TreeMapVisualOutputTypeDef]

### GeospatialMapVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialMapVisualOutputTypeDef]

### FilledMapVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FilledMapVisualOutputTypeDef]

### LayerMapVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LayerMapVisualOutputTypeDef]

### FunnelChartVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FunnelChartVisualOutputTypeDef]

### ScatterPlotVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ScatterPlotVisualOutputTypeDef]

### ComboChartVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ComboChartVisualOutputTypeDef]

### BoxPlotVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BoxPlotVisualOutputTypeDef]

### WaterfallVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.WaterfallVisualOutputTypeDef]

### HistogramVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.HistogramVisualOutputTypeDef]

### WordCloudVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.WordCloudVisualOutputTypeDef]

### InsightVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.InsightVisualOutputTypeDef]

### SankeyDiagramVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SankeyDiagramVisualOutputTypeDef]

### CustomContentVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CustomContentVisualOutputTypeDef]

### EmptyVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.EmptyVisualOutputTypeDef]

### RadarChartVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RadarChartVisualOutputTypeDef]

### PluginVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PluginVisualOutputTypeDef]


# VisualPaletteOutputTypeDef

### ChartColor
- **Type**: typing.Optional[str]

### ColorMap
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DataPathColorTypeDef]]


# VisualPaletteTypeDef

### ChartColor
- **Type**: typing.Optional[str]

### ColorMap
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DataPathColorTypeDef]]


# VisualSubtitleLabelOptionsTypeDef

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### FormatText
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LongFormatTextTypeDef]


# VisualTitleLabelOptionsTypeDef

### Visibility
- **Type**: typing.Optional[typing.Literal['HIDDEN', 'VISIBLE']]

### FormatText
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ShortFormatTextTypeDef]


# VisualTypeDef

### TableVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TableVisualTypeDef]

### PivotTableVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PivotTableVisualTypeDef]

### BarChartVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BarChartVisualTypeDef]

### KPIVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.KPIVisualTypeDef]

### PieChartVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PieChartVisualTypeDef]

### GaugeChartVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GaugeChartVisualTypeDef]

### LineChartVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LineChartVisualTypeDef]

### HeatMapVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.HeatMapVisualTypeDef]

### TreeMapVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.TreeMapVisualTypeDef]

### GeospatialMapVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.GeospatialMapVisualTypeDef]

### FilledMapVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FilledMapVisualTypeDef]

### LayerMapVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LayerMapVisualTypeDef]

### FunnelChartVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.FunnelChartVisualTypeDef]

### ScatterPlotVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ScatterPlotVisualTypeDef]

### ComboChartVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ComboChartVisualTypeDef]

### BoxPlotVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.BoxPlotVisualTypeDef]

### WaterfallVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.WaterfallVisualTypeDef]

### HistogramVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.HistogramVisualTypeDef]

### WordCloudVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.WordCloudVisualTypeDef]

### InsightVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.InsightVisualTypeDef]

### SankeyDiagramVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.SankeyDiagramVisualTypeDef]

### CustomContentVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.CustomContentVisualTypeDef]

### EmptyVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.EmptyVisualTypeDef]

### RadarChartVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.RadarChartVisualTypeDef]

### PluginVisual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.PluginVisualTypeDef]


# VpcConnectionPropertiesTypeDef

### VpcConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes


# WaterfallChartAggregatedFieldWellsOutputTypeDef

### Categories
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]

### Breakdowns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]


# WaterfallChartAggregatedFieldWellsTypeDef

### Categories
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Values
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]

### Breakdowns
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]


# WaterfallChartColorConfigurationTypeDef

### GroupColorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.WaterfallChartGroupColorConfigurationTypeDef]


# WaterfallChartConfigurationOutputTypeDef

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.WaterfallChartFieldWellsOutputTypeDef]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.WaterfallChartSortConfigurationOutputTypeDef]

### WaterfallChartOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.WaterfallChartOptionsTypeDef]

### CategoryAxisLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsOutputTypeDef]

### CategoryAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisDisplayOptionsOutputTypeDef]

### PrimaryYAxisLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsOutputTypeDef]

### PrimaryYAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisDisplayOptionsOutputTypeDef]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LegendOptionsTypeDef]

### DataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataLabelOptionsOutputTypeDef]

### VisualPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualPaletteOutputTypeDef]

### ColorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.WaterfallChartColorConfigurationTypeDef]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# WaterfallChartConfigurationTypeDef

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.WaterfallChartFieldWellsTypeDef]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.WaterfallChartSortConfigurationTypeDef]

### WaterfallChartOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.WaterfallChartOptionsTypeDef]

### CategoryAxisLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsTypeDef]

### CategoryAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisDisplayOptionsTypeDef]

### PrimaryYAxisLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsTypeDef]

### PrimaryYAxisDisplayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.AxisDisplayOptionsTypeDef]

### Legend
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.LegendOptionsTypeDef]

### DataLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.DataLabelOptionsTypeDef]

### VisualPalette
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualPaletteTypeDef]

### ColorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.WaterfallChartColorConfigurationTypeDef]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# WaterfallChartFieldWellsOutputTypeDef

### WaterfallChartAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.WaterfallChartAggregatedFieldWellsOutputTypeDef]


# WaterfallChartFieldWellsTypeDef

### WaterfallChartAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.WaterfallChartAggregatedFieldWellsTypeDef]


# WaterfallChartGroupColorConfigurationTypeDef

### PositiveBarColor
- **Type**: typing.Optional[str]

### NegativeBarColor
- **Type**: typing.Optional[str]

### TotalBarColor
- **Type**: typing.Optional[str]


# WaterfallChartOptionsTypeDef

### TotalBarLabel
- **Type**: typing.Optional[str]


# WaterfallChartSortConfigurationOutputTypeDef

### CategorySort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### BreakdownItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]


# WaterfallChartSortConfigurationTypeDef

### CategorySort
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]

### BreakdownItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]


# WaterfallVisualOutputTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.WaterfallChartConfigurationOutputTypeDef]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionOutputTypeDef]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ColumnHierarchyOutputTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# WaterfallVisualTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.WaterfallChartConfigurationTypeDef]

### Actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionTypeDef]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ColumnHierarchyTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# WhatIfPointScenarioOutputTypeDef

### Date
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Value
- **Type**: <class 'float'>
- **Required**: Yes


# WhatIfPointScenarioTypeDef

### Date
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.TimestampTypeDef'>
- **Required**: Yes

### Value
- **Type**: <class 'float'>
- **Required**: Yes


# WhatIfRangeScenarioOutputTypeDef

### StartDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Value
- **Type**: <class 'float'>
- **Required**: Yes


# WhatIfRangeScenarioTypeDef

### StartDate
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.TimestampTypeDef'>
- **Required**: Yes

### EndDate
- **Type**: <class 'aws_resource_validator.pydantic_models.quicksight_classes.TimestampTypeDef'>
- **Required**: Yes

### Value
- **Type**: <class 'float'>
- **Required**: Yes


# WordCloudAggregatedFieldWellsOutputTypeDef

### GroupBy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Size
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]


# WordCloudAggregatedFieldWellsTypeDef

### GroupBy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.DimensionFieldTypeDef]]

### Size
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.MeasureFieldTypeDef]]


# WordCloudChartConfigurationOutputTypeDef

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.WordCloudFieldWellsOutputTypeDef]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.WordCloudSortConfigurationOutputTypeDef]

### CategoryLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsOutputTypeDef]

### WordCloudOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.WordCloudOptionsTypeDef]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# WordCloudChartConfigurationTypeDef

### FieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.WordCloudFieldWellsTypeDef]

### SortConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.WordCloudSortConfigurationTypeDef]

### CategoryLabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ChartAxisLabelOptionsTypeDef]

### WordCloudOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.WordCloudOptionsTypeDef]

### Interactions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualInteractionOptionsTypeDef]


# WordCloudFieldWellsOutputTypeDef

### WordCloudAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.WordCloudAggregatedFieldWellsOutputTypeDef]


# WordCloudFieldWellsTypeDef

### WordCloudAggregatedFieldWells
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.WordCloudAggregatedFieldWellsTypeDef]


# WordCloudOptionsTypeDef

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


# WordCloudSortConfigurationOutputTypeDef

### CategoryItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]

### CategorySort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]


# WordCloudSortConfigurationTypeDef

### CategoryItemsLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.ItemsLimitConfigurationTypeDef]

### CategorySort
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.FieldSortOptionsTypeDef]]


# WordCloudVisualOutputTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.WordCloudChartConfigurationOutputTypeDef]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionOutputTypeDef]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.quicksight_classes.ColumnHierarchyOutputTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# WordCloudVisualTypeDef

### VisualId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualTitleLabelOptionsTypeDef]

### Subtitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.VisualSubtitleLabelOptionsTypeDef]

### ChartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.quicksight_classes.WordCloudChartConfigurationTypeDef]

### Actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.VisualCustomActionTypeDef]]

### ColumnHierarchies
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.quicksight_classes.ColumnHierarchyTypeDef]]

### VisualContentAltText
- **Type**: typing.Optional[str]


# YAxisOptionsTypeDef

### YAxis
- **Type**: typing.Literal['PRIMARY_Y_AXIS']
- **Required**: Yes



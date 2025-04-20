# Ssmquicksetup Service

### ConfigurationDefinitionInputLocalDeploymentExecutionRoleNameString
- **Type**: string
- **Pattern**: `^[\w+=,.@-]{1,64}$`

### ConfigurationDefinitionInputTypeString
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\-.:/]{3,200}$`

### ConfigurationDefinitionLocalDeploymentExecutionRoleNameString
- **Type**: string
- **Pattern**: `^[\w+=,.@-]{1,64}$`

### ConfigurationDefinitionTypeString
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\-.:/]{3,200}$`

### ConfigurationParametersMapKeyString
- **Type**: string
- **Pattern**: `^[A-Za-z0-9+=@_\/\s-]+$`
- **Min Length**: 1
- **Max Length**: 256

### CreateConfigurationManagerInputDescriptionString
- **Type**: string
- **Pattern**: `^.{0,512}$`

### CreateConfigurationManagerInputNameString
- **Type**: string
- **Pattern**: `^[ A-Za-z0-9._-]{0,120}$`

### DeleteConfigurationManagerInputManagerArnString
- **Type**: string
- **Pattern**: `^arn:aws:ssm-quicksetup:([^:]+):(\d{12}):configuration-manager/[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}$`

### FilterKeyString
- **Type**: string
- **Pattern**: `^[A-Za-z0-9+=@_\/\s-]*$`
- **Min Length**: 0
- **Max Length**: 128

### FilterValuesMemberString
- **Type**: string
- **Pattern**: `^[A-Za-z0-9+=@_\/\s-]*$`
- **Min Length**: 0
- **Max Length**: 256

### GetConfigurationInputConfigurationIdString
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-_/:]{1,100}$`

### GetConfigurationManagerInputManagerArnString
- **Type**: string
- **Pattern**: `^arn:aws:ssm-quicksetup:([^:]+):(\d{12}):configuration-manager/[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}$`
- **Min Length**: 1

### ListConfigurationManagersInputStartingTokenString
- **Type**: string
- **Pattern**: `^[A-Za-z0-9+=@_\/\s-]*$`
- **Min Length**: 0
- **Max Length**: 1024

### ListConfigurationsInputConfigurationDefinitionIdString
- **Type**: string
- **Pattern**: `^[a-z0-9-]{1,20}$`

### ListConfigurationsInputManagerArnString
- **Type**: string
- **Pattern**: `^arn:aws:ssm-quicksetup:([^:]+):(\d{12}):configuration-manager/[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}$`

### ListConfigurationsInputStartingTokenString
- **Type**: string
- **Pattern**: `^[A-Za-z0-9+=@_|\/\s-]*$`
- **Min Length**: 0
- **Max Length**: 1024

### TagEntryKeyString
- **Type**: string
- **Pattern**: `^[A-Za-z0-9 _=@:.+-/]+$`
- **Min Length**: 1
- **Max Length**: 128

### TagEntryValueString
- **Type**: string
- **Pattern**: `^[A-Za-z0-9 _=@:.+-/]+$`
- **Min Length**: 0
- **Max Length**: 256

### TagsMapKeyString
- **Type**: string
- **Pattern**: `^[A-Za-z0-9 _=@:.+-/]+$`
- **Min Length**: 1
- **Max Length**: 128

### TagsMapValueString
- **Type**: string
- **Pattern**: `^[A-Za-z0-9 _=@:.+-/]+$`
- **Min Length**: 0
- **Max Length**: 256

### UpdateConfigurationDefinitionInputIdString
- **Type**: string
- **Pattern**: `^[a-z0-9-]{1,20}$`

### UpdateConfigurationDefinitionInputLocalDeploymentExecutionRoleNameString
- **Type**: string
- **Pattern**: `^[\w+=,.@-]{1,64}$`

### UpdateConfigurationDefinitionInputManagerArnString
- **Type**: string
- **Pattern**: `^arn:aws:ssm-quicksetup:([^:]+):(\d{12}):configuration-manager/[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}$`

### UpdateConfigurationDefinitionInputTypeVersionString
- **Type**: string
- **Pattern**: `^\d{1,3}(\.\d{1,3})?$|^LATEST$`

### UpdateConfigurationManagerInputDescriptionString
- **Type**: string
- **Pattern**: `^.{0,512}$`

### UpdateConfigurationManagerInputManagerArnString
- **Type**: string
- **Pattern**: `^arn:aws:ssm-quicksetup:([^:]+):(\d{12}):configuration-manager/[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}$`

### UpdateConfigurationManagerInputNameString
- **Type**: string
- **Pattern**: `^[ A-Za-z0-9._-]{0,120}$`


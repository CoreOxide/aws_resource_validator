# Cloudformation Classes

# AccountGateResultTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'SKIPPED', 'SUCCEEDED']]

### StatusReason
- **Type**: typing.Optional[str]


# AccountLimitTypeDef

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[int]


# ActivateTypeOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AutoDeploymentTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### RetainStacksOnAccountRemoval
- **Type**: typing.Optional[bool]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchDescribeTypeConfigurationsErrorTypeDef

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]

### TypeConfigurationIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.TypeConfigurationIdentifierTypeDef]


# BatchDescribeTypeConfigurationsInputTypeDef

### TypeConfigurationIdentifiers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cloudformation_classes.TypeConfigurationIdentifierTypeDef]
- **Required**: Yes


# BatchDescribeTypeConfigurationsOutputTypeDef

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.BatchDescribeTypeConfigurationsErrorTypeDef]
- **Required**: Yes

### UnprocessedTypeConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.TypeConfigurationIdentifierTypeDef]
- **Required**: Yes

### TypeConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.TypeConfigurationDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CancelUpdateStackInputStackCancelUpdateTypeDef

### ClientRequestToken
- **Type**: typing.Optional[str]


# CancelUpdateStackInputTypeDef

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# ChangeSetHookResourceTargetDetailsTypeDef

### LogicalResourceId
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### ResourceAction
- **Type**: typing.Optional[typing.Literal['Add', 'Dynamic', 'Import', 'Modify', 'Remove']]


# ChangeSetHookTargetDetailsTypeDef

### TargetType
- **Type**: typing.Optional[typing.Literal['RESOURCE']]

### ResourceTargetDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.ChangeSetHookResourceTargetDetailsTypeDef]


# ChangeSetHookTypeDef

### InvocationPoint
- **Type**: typing.Optional[typing.Literal['PRE_PROVISION']]

### FailureMode
- **Type**: typing.Optional[typing.Literal['FAIL', 'WARN']]

### TypeName
- **Type**: typing.Optional[str]

### TypeVersionId
- **Type**: typing.Optional[str]

### TypeConfigurationVersionId
- **Type**: typing.Optional[str]

### TargetDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.ChangeSetHookTargetDetailsTypeDef]


# ChangeSetSummaryTypeDef

### StackId
- **Type**: typing.Optional[str]

### StackName
- **Type**: typing.Optional[str]

### ChangeSetId
- **Type**: typing.Optional[str]

### ChangeSetName
- **Type**: typing.Optional[str]

### ExecutionStatus
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'EXECUTE_COMPLETE', 'EXECUTE_FAILED', 'EXECUTE_IN_PROGRESS', 'OBSOLETE', 'UNAVAILABLE']]

### Status
- **Type**: typing.Optional[typing.Literal['CREATE_COMPLETE', 'CREATE_IN_PROGRESS', 'CREATE_PENDING', 'DELETE_COMPLETE', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'DELETE_PENDING', 'FAILED']]

### StatusReason
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### Description
- **Type**: typing.Optional[str]

### IncludeNestedStacks
- **Type**: typing.Optional[bool]

### ParentChangeSetId
- **Type**: typing.Optional[str]

### RootChangeSetId
- **Type**: typing.Optional[str]

### ImportExistingResources
- **Type**: typing.Optional[bool]


# ChangeTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ContinueUpdateRollbackInputTypeDef

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: typing.Optional[str]

### ResourcesToSkip
- **Type**: typing.Optional[typing.Sequence[str]]

### ClientRequestToken
- **Type**: typing.Optional[str]


# CreateChangeSetInputTypeDef

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeSetName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateBody
- **Type**: typing.Optional[str]

### TemplateURL
- **Type**: typing.Optional[str]

### UsePreviousTemplate
- **Type**: typing.Optional[bool]

### Parameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudformation_classes.ParameterTypeDef]]

### Capabilities
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CAPABILITY_AUTO_EXPAND', 'CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM']]]

### ResourceTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### RoleARN
- **Type**: typing.Optional[str]

### RollbackConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.RollbackConfigurationUnionTypeDef]

### NotificationARNs
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudformation_classes.TagTypeDef]]

### ClientToken
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ChangeSetType
- **Type**: typing.Optional[typing.Literal['CREATE', 'IMPORT', 'UPDATE']]

### ResourcesToImport
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudformation_classes.ResourceToImportTypeDef]]

### IncludeNestedStacks
- **Type**: typing.Optional[bool]

### OnStackFailure
- **Type**: typing.Optional[typing.Literal['DELETE', 'DO_NOTHING', 'ROLLBACK']]

### ImportExistingResources
- **Type**: typing.Optional[bool]


# CreateChangeSetOutputTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### StackId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateGeneratedTemplateInputTypeDef

### GeneratedTemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### Resources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudformation_classes.ResourceDefinitionTypeDef]]

### StackName
- **Type**: typing.Optional[str]

### TemplateConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.TemplateConfigurationTypeDef]


# CreateGeneratedTemplateOutputTypeDef

### GeneratedTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateStackInputServiceResourceCreateStackTypeDef

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateBody
- **Type**: typing.Optional[str]

### TemplateURL
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudformation_classes.ParameterTypeDef]]

### DisableRollback
- **Type**: typing.Optional[bool]

### RollbackConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.RollbackConfigurationUnionTypeDef]

### TimeoutInMinutes
- **Type**: typing.Optional[int]

### NotificationARNs
- **Type**: typing.Optional[typing.Sequence[str]]

### Capabilities
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CAPABILITY_AUTO_EXPAND', 'CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM']]]

### ResourceTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### RoleARN
- **Type**: typing.Optional[str]

### OnFailure
- **Type**: typing.Optional[typing.Literal['DELETE', 'DO_NOTHING', 'ROLLBACK']]

### StackPolicyBody
- **Type**: typing.Optional[str]

### StackPolicyURL
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudformation_classes.TagTypeDef]]

### ClientRequestToken
- **Type**: typing.Optional[str]

### EnableTerminationProtection
- **Type**: typing.Optional[bool]

### RetainExceptOnCreate
- **Type**: typing.Optional[bool]


# CreateStackInputTypeDef

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateBody
- **Type**: typing.Optional[str]

### TemplateURL
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudformation_classes.ParameterTypeDef]]

### DisableRollback
- **Type**: typing.Optional[bool]

### RollbackConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.RollbackConfigurationUnionTypeDef]

### TimeoutInMinutes
- **Type**: typing.Optional[int]

### NotificationARNs
- **Type**: typing.Optional[typing.Sequence[str]]

### Capabilities
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CAPABILITY_AUTO_EXPAND', 'CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM']]]

### ResourceTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### RoleARN
- **Type**: typing.Optional[str]

### OnFailure
- **Type**: typing.Optional[typing.Literal['DELETE', 'DO_NOTHING', 'ROLLBACK']]

### StackPolicyBody
- **Type**: typing.Optional[str]

### StackPolicyURL
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudformation_classes.TagTypeDef]]

### ClientRequestToken
- **Type**: typing.Optional[str]

### EnableTerminationProtection
- **Type**: typing.Optional[bool]

### RetainExceptOnCreate
- **Type**: typing.Optional[bool]


# CreateStackInstancesInputTypeDef

### StackSetName
- **Type**: <class 'str'>
- **Required**: Yes

### Regions
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Accounts
- **Type**: typing.Optional[typing.Sequence[str]]

### DeploymentTargets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.DeploymentTargetsUnionTypeDef]

### ParameterOverrides
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudformation_classes.ParameterTypeDef]]

### OperationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.StackSetOperationPreferencesUnionTypeDef]

### OperationId
- **Type**: typing.Optional[str]

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]


# CreateStackInstancesOutputTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateStackOutputTypeDef

### StackId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateStackRefactorInputTypeDef

### StackDefinitions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cloudformation_classes.StackDefinitionTypeDef]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### EnableStackCreation
- **Type**: typing.Optional[bool]

### ResourceMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudformation_classes.ResourceMappingTypeDef]]


# CreateStackRefactorOutputTypeDef

### StackRefactorId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateStackSetInputTypeDef

### StackSetName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### TemplateBody
- **Type**: typing.Optional[str]

### TemplateURL
- **Type**: typing.Optional[str]

### StackId
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudformation_classes.ParameterTypeDef]]

### Capabilities
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CAPABILITY_AUTO_EXPAND', 'CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM']]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudformation_classes.TagTypeDef]]

### AdministrationRoleARN
- **Type**: typing.Optional[str]

### ExecutionRoleName
- **Type**: typing.Optional[str]

### PermissionModel
- **Type**: typing.Optional[typing.Literal['SELF_MANAGED', 'SERVICE_MANAGED']]

### AutoDeployment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.AutoDeploymentTypeDef]

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]

### ClientRequestToken
- **Type**: typing.Optional[str]

### ManagedExecution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.ManagedExecutionTypeDef]


# CreateStackSetOutputTypeDef

### StackSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteChangeSetInputTypeDef

### ChangeSetName
- **Type**: <class 'str'>
- **Required**: Yes

### StackName
- **Type**: typing.Optional[str]


# DeleteGeneratedTemplateInputTypeDef

### GeneratedTemplateName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStackInputStackDeleteTypeDef

### RetainResources
- **Type**: typing.Optional[typing.Sequence[str]]

### RoleARN
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]

### DeletionMode
- **Type**: typing.Optional[typing.Literal['FORCE_DELETE_STACK', 'STANDARD']]


# DeleteStackInputTypeDef

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### RetainResources
- **Type**: typing.Optional[typing.Sequence[str]]

### RoleARN
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]

### DeletionMode
- **Type**: typing.Optional[typing.Literal['FORCE_DELETE_STACK', 'STANDARD']]


# DeleteStackInstancesInputTypeDef

### StackSetName
- **Type**: <class 'str'>
- **Required**: Yes

### Regions
- **Type**: typing.Sequence[str]
- **Required**: Yes

### RetainStacks
- **Type**: <class 'bool'>
- **Required**: Yes

### Accounts
- **Type**: typing.Optional[typing.Sequence[str]]

### DeploymentTargets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.DeploymentTargetsUnionTypeDef]

### OperationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.StackSetOperationPreferencesUnionTypeDef]

### OperationId
- **Type**: typing.Optional[str]

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]


# DeleteStackInstancesOutputTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteStackSetInputTypeDef

### StackSetName
- **Type**: <class 'str'>
- **Required**: Yes

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]


# DeploymentTargetsOutputTypeDef

### Accounts
- **Type**: typing.Optional[typing.List[str]]

### AccountsUrl
- **Type**: typing.Optional[str]

### OrganizationalUnitIds
- **Type**: typing.Optional[typing.List[str]]

### AccountFilterType
- **Type**: typing.Optional[typing.Literal['DIFFERENCE', 'INTERSECTION', 'NONE', 'UNION']]


# DeploymentTargetsTypeDef

### Accounts
- **Type**: typing.Optional[typing.Sequence[str]]

### AccountsUrl
- **Type**: typing.Optional[str]

### OrganizationalUnitIds
- **Type**: typing.Optional[typing.Sequence[str]]

### AccountFilterType
- **Type**: typing.Optional[typing.Literal['DIFFERENCE', 'INTERSECTION', 'NONE', 'UNION']]


# DeploymentTargetsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DescribeAccountLimitsInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.PaginatorConfigTypeDef]


# DescribeAccountLimitsInputTypeDef

### NextToken
- **Type**: typing.Optional[str]


# DescribeAccountLimitsOutputTypeDef

### AccountLimits
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.AccountLimitTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeChangeSetHooksInputTypeDef

### ChangeSetName
- **Type**: <class 'str'>
- **Required**: Yes

### StackName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### LogicalResourceId
- **Type**: typing.Optional[str]


# DescribeChangeSetHooksOutputTypeDef

### ChangeSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeSetName
- **Type**: <class 'str'>
- **Required**: Yes

### Hooks
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.ChangeSetHookTypeDef]
- **Required**: Yes

### Status
- **Type**: typing.Literal['PLANNED', 'PLANNING', 'UNAVAILABLE']
- **Required**: Yes

### StackId
- **Type**: <class 'str'>
- **Required**: Yes

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeChangeSetInputPaginateTypeDef

### ChangeSetName
- **Type**: <class 'str'>
- **Required**: Yes

### StackName
- **Type**: typing.Optional[str]

### IncludePropertyValues
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.PaginatorConfigTypeDef]


# DescribeChangeSetInputTypeDef

### ChangeSetName
- **Type**: <class 'str'>
- **Required**: Yes

### StackName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### IncludePropertyValues
- **Type**: typing.Optional[bool]


# DescribeChangeSetInputWaitTypeDef

### ChangeSetName
- **Type**: <class 'str'>
- **Required**: Yes

### StackName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### IncludePropertyValues
- **Type**: typing.Optional[bool]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.WaiterConfigTypeDef]


# DescribeChangeSetOutputTypeDef

### ChangeSetName
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeSetId
- **Type**: <class 'str'>
- **Required**: Yes

### StackId
- **Type**: <class 'str'>
- **Required**: Yes

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.ParameterTypeDef]
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ExecutionStatus
- **Type**: typing.Literal['AVAILABLE', 'EXECUTE_COMPLETE', 'EXECUTE_FAILED', 'EXECUTE_IN_PROGRESS', 'OBSOLETE', 'UNAVAILABLE']
- **Required**: Yes

### Status
- **Type**: typing.Literal['CREATE_COMPLETE', 'CREATE_IN_PROGRESS', 'CREATE_PENDING', 'DELETE_COMPLETE', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'DELETE_PENDING', 'FAILED']
- **Required**: Yes

### StatusReason
- **Type**: <class 'str'>
- **Required**: Yes

### NotificationARNs
- **Type**: typing.List[str]
- **Required**: Yes

### RollbackConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.RollbackConfigurationOutputTypeDef'>
- **Required**: Yes

### Capabilities
- **Type**: typing.List[typing.Literal['CAPABILITY_AUTO_EXPAND', 'CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM']]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.TagTypeDef]
- **Required**: Yes

### Changes
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.ChangeTypeDef]
- **Required**: Yes

### IncludeNestedStacks
- **Type**: <class 'bool'>
- **Required**: Yes

### ParentChangeSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RootChangeSetId
- **Type**: <class 'str'>
- **Required**: Yes

### OnStackFailure
- **Type**: typing.Literal['DELETE', 'DO_NOTHING', 'ROLLBACK']
- **Required**: Yes

### ImportExistingResources
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeGeneratedTemplateInputTypeDef

### GeneratedTemplateName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeGeneratedTemplateOutputTypeDef

### GeneratedTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### GeneratedTemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### Resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.ResourceDetailTypeDef]
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETE', 'CREATE_IN_PROGRESS', 'CREATE_PENDING', 'DELETE_IN_PROGRESS', 'DELETE_PENDING', 'FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_PENDING']
- **Required**: Yes

### StatusReason
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Progress
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.TemplateProgressTypeDef'>
- **Required**: Yes

### StackId
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.TemplateConfigurationTypeDef'>
- **Required**: Yes

### TotalWarnings
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeOrganizationsAccessInputTypeDef

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]


# DescribeOrganizationsAccessOutputTypeDef

### Status
- **Type**: typing.Literal['DISABLED', 'DISABLED_PERMANENTLY', 'ENABLED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePublisherInputTypeDef

### PublisherId
- **Type**: typing.Optional[str]


# DescribePublisherOutputTypeDef

### PublisherId
- **Type**: <class 'str'>
- **Required**: Yes

### PublisherStatus
- **Type**: typing.Literal['UNVERIFIED', 'VERIFIED']
- **Required**: Yes

### IdentityProvider
- **Type**: typing.Literal['AWS_Marketplace', 'Bitbucket', 'GitHub']
- **Required**: Yes

### PublisherProfile
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeResourceScanInputTypeDef

### ResourceScanId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeResourceScanOutputTypeDef

### ResourceScanId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETE', 'EXPIRED', 'FAILED', 'IN_PROGRESS']
- **Required**: Yes

### StatusReason
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### PercentageCompleted
- **Type**: <class 'float'>
- **Required**: Yes

### ResourceTypes
- **Type**: typing.List[str]
- **Required**: Yes

### ResourcesScanned
- **Type**: <class 'int'>
- **Required**: Yes

### ResourcesRead
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeStackDriftDetectionStatusInputTypeDef

### StackDriftDetectionId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeStackDriftDetectionStatusOutputTypeDef

### StackId
- **Type**: <class 'str'>
- **Required**: Yes

### StackDriftDetectionId
- **Type**: <class 'str'>
- **Required**: Yes

### StackDriftStatus
- **Type**: typing.Literal['DRIFTED', 'IN_SYNC', 'NOT_CHECKED', 'UNKNOWN']
- **Required**: Yes

### DetectionStatus
- **Type**: typing.Literal['DETECTION_COMPLETE', 'DETECTION_FAILED', 'DETECTION_IN_PROGRESS']
- **Required**: Yes

### DetectionStatusReason
- **Type**: <class 'str'>
- **Required**: Yes

### DriftedStackResourceCount
- **Type**: <class 'int'>
- **Required**: Yes

### Timestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeStackEventsInputPaginateTypeDef

### StackName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.PaginatorConfigTypeDef]


# DescribeStackEventsInputTypeDef

### StackName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# DescribeStackEventsOutputTypeDef

### StackEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.StackEventTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeStackInstanceInputTypeDef

### StackSetName
- **Type**: <class 'str'>
- **Required**: Yes

### StackInstanceAccount
- **Type**: <class 'str'>
- **Required**: Yes

### StackInstanceRegion
- **Type**: <class 'str'>
- **Required**: Yes

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]


# DescribeStackInstanceOutputTypeDef

### StackInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.StackInstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeStackRefactorInputTypeDef

### StackRefactorId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeStackRefactorInputWaitExtraTypeDef

### StackRefactorId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.WaiterConfigTypeDef]


# DescribeStackRefactorInputWaitTypeDef

### StackRefactorId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.WaiterConfigTypeDef]


# DescribeStackRefactorOutputTypeDef

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### StackRefactorId
- **Type**: <class 'str'>
- **Required**: Yes

### StackIds
- **Type**: typing.List[str]
- **Required**: Yes

### ExecutionStatus
- **Type**: typing.Literal['AVAILABLE', 'EXECUTE_COMPLETE', 'EXECUTE_FAILED', 'EXECUTE_IN_PROGRESS', 'OBSOLETE', 'ROLLBACK_COMPLETE', 'ROLLBACK_FAILED', 'ROLLBACK_IN_PROGRESS', 'UNAVAILABLE']
- **Required**: Yes

### ExecutionStatusReason
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_COMPLETE', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']
- **Required**: Yes

### StatusReason
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeStackResourceDriftsInputTypeDef

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### StackResourceDriftStatusFilters
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DELETED', 'IN_SYNC', 'MODIFIED', 'NOT_CHECKED']]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeStackResourceDriftsOutputTypeDef

### StackResourceDrifts
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.StackResourceDriftTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeStackResourceInputTypeDef

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### LogicalResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeStackResourceOutputTypeDef

### StackResourceDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.StackResourceDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeStackResourcesInputTypeDef

### StackName
- **Type**: typing.Optional[str]

### LogicalResourceId
- **Type**: typing.Optional[str]

### PhysicalResourceId
- **Type**: typing.Optional[str]


# DescribeStackResourcesOutputTypeDef

### StackResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.StackResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeStackSetInputTypeDef

### StackSetName
- **Type**: <class 'str'>
- **Required**: Yes

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]


# DescribeStackSetOperationInputTypeDef

### StackSetName
- **Type**: <class 'str'>
- **Required**: Yes

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]


# DescribeStackSetOperationOutputTypeDef

### StackSetOperation
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.StackSetOperationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeStackSetOutputTypeDef

### StackSet
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.StackSetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeStacksInputPaginateTypeDef

### StackName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.PaginatorConfigTypeDef]


# DescribeStacksInputTypeDef

### StackName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# DescribeStacksInputWaitExtraExtraExtraExtraExtraTypeDef

### StackName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.WaiterConfigTypeDef]


# DescribeStacksInputWaitExtraExtraExtraExtraTypeDef

### StackName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.WaiterConfigTypeDef]


# DescribeStacksInputWaitExtraExtraExtraTypeDef

### StackName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.WaiterConfigTypeDef]


# DescribeStacksInputWaitExtraExtraTypeDef

### StackName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.WaiterConfigTypeDef]


# DescribeStacksInputWaitExtraTypeDef

### StackName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.WaiterConfigTypeDef]


# DescribeStacksInputWaitTypeDef

### StackName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.WaiterConfigTypeDef]


# DescribeStacksOutputTypeDef

### Stacks
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.StackTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeTypeRegistrationInputTypeDef

### RegistrationToken
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTypeRegistrationInputWaitTypeDef

### RegistrationToken
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.WaiterConfigTypeDef]


# DescribeTypeRegistrationOutputTypeDef

### ProgressStatus
- **Type**: typing.Literal['COMPLETE', 'FAILED', 'IN_PROGRESS']
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### TypeArn
- **Type**: <class 'str'>
- **Required**: Yes

### TypeVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetectStackDriftInputTypeDef

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### LogicalResourceIds
- **Type**: typing.Optional[typing.Sequence[str]]


# DetectStackDriftOutputTypeDef

### StackDriftDetectionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetectStackResourceDriftInputTypeDef

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### LogicalResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DetectStackResourceDriftOutputTypeDef

### StackResourceDrift
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.StackResourceDriftTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetectStackSetDriftInputTypeDef

### StackSetName
- **Type**: <class 'str'>
- **Required**: Yes

### OperationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.StackSetOperationPreferencesUnionTypeDef]

### OperationId
- **Type**: typing.Optional[str]

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]


# DetectStackSetDriftOutputTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EstimateTemplateCostInputTypeDef

### TemplateBody
- **Type**: typing.Optional[str]

### TemplateURL
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudformation_classes.ParameterTypeDef]]


# EstimateTemplateCostOutputTypeDef

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExecuteChangeSetInputTypeDef

### ChangeSetName
- **Type**: <class 'str'>
- **Required**: Yes

### StackName
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]

### DisableRollback
- **Type**: typing.Optional[bool]

### RetainExceptOnCreate
- **Type**: typing.Optional[bool]


# ExecuteStackRefactorInputTypeDef

### StackRefactorId
- **Type**: <class 'str'>
- **Required**: Yes


# ExportTypeDef

### ExportingStackId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# GetGeneratedTemplateInputTypeDef

### GeneratedTemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### Format
- **Type**: typing.Optional[typing.Literal['JSON', 'YAML']]


# GetGeneratedTemplateOutputTypeDef

### Status
- **Type**: typing.Literal['COMPLETE', 'CREATE_IN_PROGRESS', 'CREATE_PENDING', 'DELETE_IN_PROGRESS', 'DELETE_PENDING', 'FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_PENDING']
- **Required**: Yes

### TemplateBody
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetStackPolicyInputTypeDef

### StackName
- **Type**: <class 'str'>
- **Required**: Yes


# GetStackPolicyOutputTypeDef

### StackPolicyBody
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTemplateInputTypeDef

### StackName
- **Type**: typing.Optional[str]

### ChangeSetName
- **Type**: typing.Optional[str]

### TemplateStage
- **Type**: typing.Optional[typing.Literal['Original', 'Processed']]


# GetTemplateOutputTypeDef

### TemplateBody
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes

### StagesAvailable
- **Type**: typing.List[typing.Literal['Original', 'Processed']]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTemplateSummaryInputTypeDef

### TemplateBody
- **Type**: typing.Optional[str]

### TemplateURL
- **Type**: typing.Optional[str]

### StackName
- **Type**: typing.Optional[str]

### StackSetName
- **Type**: typing.Optional[str]

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]

### TemplateSummaryConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.TemplateSummaryConfigTypeDef]


# GetTemplateSummaryOutputTypeDef

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.ParameterDeclarationTypeDef]
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Capabilities
- **Type**: typing.List[typing.Literal['CAPABILITY_AUTO_EXPAND', 'CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM']]
- **Required**: Yes

### CapabilitiesReason
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTypes
- **Type**: typing.List[str]
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### Metadata
- **Type**: <class 'str'>
- **Required**: Yes

### DeclaredTransforms
- **Type**: typing.List[str]
- **Required**: Yes

### ResourceIdentifierSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.ResourceIdentifierSummaryTypeDef]
- **Required**: Yes

### Warnings
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.WarningsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HookResultSummaryTypeDef

### InvocationPoint
- **Type**: typing.Optional[typing.Literal['PRE_PROVISION']]

### FailureMode
- **Type**: typing.Optional[typing.Literal['FAIL', 'WARN']]

### TypeName
- **Type**: typing.Optional[str]

### TypeVersionId
- **Type**: typing.Optional[str]

### TypeConfigurationVersionId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['HOOK_COMPLETE_FAILED', 'HOOK_COMPLETE_SUCCEEDED', 'HOOK_FAILED', 'HOOK_IN_PROGRESS']]

### HookStatusReason
- **Type**: typing.Optional[str]


# ImportStacksToStackSetInputTypeDef

### StackSetName
- **Type**: <class 'str'>
- **Required**: Yes

### StackIds
- **Type**: typing.Optional[typing.Sequence[str]]

### StackIdsUrl
- **Type**: typing.Optional[str]

### OrganizationalUnitIds
- **Type**: typing.Optional[typing.Sequence[str]]

### OperationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.StackSetOperationPreferencesUnionTypeDef]

### OperationId
- **Type**: typing.Optional[str]

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]


# ImportStacksToStackSetOutputTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListChangeSetsInputPaginateTypeDef

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.PaginatorConfigTypeDef]


# ListChangeSetsInputTypeDef

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListChangeSetsOutputTypeDef

### Summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.ChangeSetSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListExportsInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.PaginatorConfigTypeDef]


# ListExportsInputTypeDef

### NextToken
- **Type**: typing.Optional[str]


# ListExportsOutputTypeDef

### Exports
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.ExportTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGeneratedTemplatesInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.PaginatorConfigTypeDef]


# ListGeneratedTemplatesInputTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListGeneratedTemplatesOutputTypeDef

### Summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.TemplateSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHookResultsInputTypeDef

### TargetType
- **Type**: typing.Literal['CHANGE_SET', 'CLOUD_CONTROL', 'RESOURCE', 'STACK']
- **Required**: Yes

### TargetId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHookResultsOutputTypeDef

### TargetType
- **Type**: typing.Literal['CHANGE_SET', 'CLOUD_CONTROL', 'RESOURCE', 'STACK']
- **Required**: Yes

### TargetId
- **Type**: <class 'str'>
- **Required**: Yes

### HookResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.HookResultSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListImportsInputPaginateTypeDef

### ExportName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.PaginatorConfigTypeDef]


# ListImportsInputTypeDef

### ExportName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListImportsOutputTypeDef

### Imports
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourceScanRelatedResourcesInputPaginateTypeDef

### ResourceScanId
- **Type**: <class 'str'>
- **Required**: Yes

### Resources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cloudformation_classes.ScannedResourceIdentifierTypeDef]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.PaginatorConfigTypeDef]


# ListResourceScanRelatedResourcesInputTypeDef

### ResourceScanId
- **Type**: <class 'str'>
- **Required**: Yes

### Resources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cloudformation_classes.ScannedResourceIdentifierTypeDef]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListResourceScanRelatedResourcesOutputTypeDef

### RelatedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.ScannedResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourceScanResourcesInputPaginateTypeDef

### ResourceScanId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceIdentifier
- **Type**: typing.Optional[str]

### ResourceTypePrefix
- **Type**: typing.Optional[str]

### TagKey
- **Type**: typing.Optional[str]

### TagValue
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.PaginatorConfigTypeDef]


# ListResourceScanResourcesInputTypeDef

### ResourceScanId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceIdentifier
- **Type**: typing.Optional[str]

### ResourceTypePrefix
- **Type**: typing.Optional[str]

### TagKey
- **Type**: typing.Optional[str]

### TagValue
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListResourceScanResourcesOutputTypeDef

### Resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.ScannedResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourceScansInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.PaginatorConfigTypeDef]


# ListResourceScansInputTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListResourceScansOutputTypeDef

### ResourceScanSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.ResourceScanSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStackInstanceResourceDriftsInputTypeDef

### StackSetName
- **Type**: <class 'str'>
- **Required**: Yes

### StackInstanceAccount
- **Type**: <class 'str'>
- **Required**: Yes

### StackInstanceRegion
- **Type**: <class 'str'>
- **Required**: Yes

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### StackInstanceResourceDriftStatuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DELETED', 'IN_SYNC', 'MODIFIED', 'NOT_CHECKED']]]

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]


# ListStackInstanceResourceDriftsOutputTypeDef

### Summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.StackInstanceResourceDriftsSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStackInstancesInputPaginateTypeDef

### StackSetName
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudformation_classes.StackInstanceFilterTypeDef]]

### StackInstanceAccount
- **Type**: typing.Optional[str]

### StackInstanceRegion
- **Type**: typing.Optional[str]

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.PaginatorConfigTypeDef]


# ListStackInstancesInputTypeDef

### StackSetName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudformation_classes.StackInstanceFilterTypeDef]]

### StackInstanceAccount
- **Type**: typing.Optional[str]

### StackInstanceRegion
- **Type**: typing.Optional[str]

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]


# ListStackInstancesOutputTypeDef

### Summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.StackInstanceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStackRefactorActionsInputPaginateTypeDef

### StackRefactorId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.PaginatorConfigTypeDef]


# ListStackRefactorActionsInputTypeDef

### StackRefactorId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListStackRefactorActionsOutputTypeDef

### StackRefactorActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.StackRefactorActionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStackRefactorsInputPaginateTypeDef

### ExecutionStatusFilter
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AVAILABLE', 'EXECUTE_COMPLETE', 'EXECUTE_FAILED', 'EXECUTE_IN_PROGRESS', 'OBSOLETE', 'ROLLBACK_COMPLETE', 'ROLLBACK_FAILED', 'ROLLBACK_IN_PROGRESS', 'UNAVAILABLE']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.PaginatorConfigTypeDef]


# ListStackRefactorsInputTypeDef

### ExecutionStatusFilter
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AVAILABLE', 'EXECUTE_COMPLETE', 'EXECUTE_FAILED', 'EXECUTE_IN_PROGRESS', 'OBSOLETE', 'ROLLBACK_COMPLETE', 'ROLLBACK_FAILED', 'ROLLBACK_IN_PROGRESS', 'UNAVAILABLE']]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListStackRefactorsOutputTypeDef

### StackRefactorSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.StackRefactorSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStackResourcesInputPaginateTypeDef

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.PaginatorConfigTypeDef]


# ListStackResourcesInputTypeDef

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStackResourcesOutputTypeDef

### StackResourceSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.StackResourceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStackSetAutoDeploymentTargetsInputTypeDef

### StackSetName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]


# ListStackSetAutoDeploymentTargetsOutputTypeDef

### Summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.StackSetAutoDeploymentTargetSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStackSetOperationResultsInputPaginateTypeDef

### StackSetName
- **Type**: <class 'str'>
- **Required**: Yes

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudformation_classes.OperationResultFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.PaginatorConfigTypeDef]


# ListStackSetOperationResultsInputTypeDef

### StackSetName
- **Type**: <class 'str'>
- **Required**: Yes

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudformation_classes.OperationResultFilterTypeDef]]


# ListStackSetOperationResultsOutputTypeDef

### Summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.StackSetOperationResultSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStackSetOperationsInputPaginateTypeDef

### StackSetName
- **Type**: <class 'str'>
- **Required**: Yes

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.PaginatorConfigTypeDef]


# ListStackSetOperationsInputTypeDef

### StackSetName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]


# ListStackSetOperationsOutputTypeDef

### Summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.StackSetOperationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStackSetsInputPaginateTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED']]

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.PaginatorConfigTypeDef]


# ListStackSetsInputTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED']]

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]


# ListStackSetsOutputTypeDef

### Summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.StackSetSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStacksInputPaginateTypeDef

### StackStatusFilter
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_COMPLETE', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'IMPORT_COMPLETE', 'IMPORT_IN_PROGRESS', 'IMPORT_ROLLBACK_COMPLETE', 'IMPORT_ROLLBACK_FAILED', 'IMPORT_ROLLBACK_IN_PROGRESS', 'REVIEW_IN_PROGRESS', 'ROLLBACK_COMPLETE', 'ROLLBACK_FAILED', 'ROLLBACK_IN_PROGRESS', 'UPDATE_COMPLETE', 'UPDATE_COMPLETE_CLEANUP_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_ROLLBACK_COMPLETE', 'UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS', 'UPDATE_ROLLBACK_FAILED', 'UPDATE_ROLLBACK_IN_PROGRESS']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.PaginatorConfigTypeDef]


# ListStacksInputTypeDef

### NextToken
- **Type**: typing.Optional[str]

### StackStatusFilter
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_COMPLETE', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'IMPORT_COMPLETE', 'IMPORT_IN_PROGRESS', 'IMPORT_ROLLBACK_COMPLETE', 'IMPORT_ROLLBACK_FAILED', 'IMPORT_ROLLBACK_IN_PROGRESS', 'REVIEW_IN_PROGRESS', 'ROLLBACK_COMPLETE', 'ROLLBACK_FAILED', 'ROLLBACK_IN_PROGRESS', 'UPDATE_COMPLETE', 'UPDATE_COMPLETE_CLEANUP_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_ROLLBACK_COMPLETE', 'UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS', 'UPDATE_ROLLBACK_FAILED', 'UPDATE_ROLLBACK_IN_PROGRESS']]]


# ListStacksOutputTypeDef

### StackSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.StackSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTypeRegistrationsOutputTypeDef

### RegistrationTokenList
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTypeVersionsOutputTypeDef

### TypeVersionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.TypeVersionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTypesOutputTypeDef

### TypeSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.TypeSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LoggingConfigTypeDef

### LogRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### LogGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# ManagedExecutionTypeDef

### Active
- **Type**: typing.Optional[bool]


# ModuleInfoTypeDef

### TypeHierarchy
- **Type**: typing.Optional[str]

### LogicalIdHierarchy
- **Type**: typing.Optional[str]


# OperationResultFilterTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['OPERATION_RESULT_STATUS']]

### Values
- **Type**: typing.Optional[str]


# OutputTypeDef

### OutputKey
- **Type**: typing.Optional[str]

### OutputValue
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ExportName
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParameterConstraintsTypeDef

### AllowedValues
- **Type**: typing.Optional[typing.List[str]]


# ParameterDeclarationTypeDef

### ParameterKey
- **Type**: typing.Optional[str]

### DefaultValue
- **Type**: typing.Optional[str]

### ParameterType
- **Type**: typing.Optional[str]

### NoEcho
- **Type**: typing.Optional[bool]

### Description
- **Type**: typing.Optional[str]

### ParameterConstraints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.ParameterConstraintsTypeDef]


# ParameterTypeDef

### ParameterKey
- **Type**: typing.Optional[str]

### ParameterValue
- **Type**: typing.Optional[str]

### UsePreviousValue
- **Type**: typing.Optional[bool]

### ResolvedValue
- **Type**: typing.Optional[str]


# PhysicalResourceIdContextKeyValuePairTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# PropertyDifferenceTypeDef

### PropertyPath
- **Type**: <class 'str'>
- **Required**: Yes

### ExpectedValue
- **Type**: <class 'str'>
- **Required**: Yes

### ActualValue
- **Type**: <class 'str'>
- **Required**: Yes

### DifferenceType
- **Type**: typing.Literal['ADD', 'NOT_EQUAL', 'REMOVE']
- **Required**: Yes


# PublishTypeOutputTypeDef

### PublicTypeArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RecordHandlerProgressInputTypeDef

### BearerToken
- **Type**: <class 'str'>
- **Required**: Yes

### OperationStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'PENDING', 'SUCCESS']
- **Required**: Yes

### CurrentOperationStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'PENDING', 'SUCCESS']]

### StatusMessage
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[typing.Literal['AccessDenied', 'AlreadyExists', 'GeneralServiceException', 'HandlerInternalFailure', 'InternalFailure', 'InvalidCredentials', 'InvalidRequest', 'InvalidTypeConfiguration', 'NetworkFailure', 'NonCompliant', 'NotFound', 'NotStabilized', 'NotUpdatable', 'ResourceConflict', 'ServiceInternalError', 'ServiceLimitExceeded', 'Throttling', 'Unknown', 'UnsupportedTarget']]

### ResourceModel
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]


# RegisterPublisherInputTypeDef

### AcceptTermsAndConditions
- **Type**: typing.Optional[bool]

### ConnectionArn
- **Type**: typing.Optional[str]


# RegisterPublisherOutputTypeDef

### PublisherId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegisterTypeOutputTypeDef

### RegistrationToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RequiredActivatedTypeTypeDef

### TypeNameAlias
- **Type**: typing.Optional[str]

### OriginalTypeName
- **Type**: typing.Optional[str]

### PublisherId
- **Type**: typing.Optional[str]

### SupportedMajorVersions
- **Type**: typing.Optional[typing.List[int]]


# ResourceChangeDetailTypeDef

### Target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.ResourceTargetDefinitionTypeDef]

### Evaluation
- **Type**: typing.Optional[typing.Literal['Dynamic', 'Static']]

### ChangeSource
- **Type**: typing.Optional[typing.Literal['Automatic', 'DirectModification', 'ParameterReference', 'ResourceAttribute', 'ResourceReference']]

### CausingEntity
- **Type**: typing.Optional[str]


# ResourceChangeTypeDef

### PolicyAction
- **Type**: typing.Optional[typing.Literal['Delete', 'ReplaceAndDelete', 'ReplaceAndRetain', 'ReplaceAndSnapshot', 'Retain', 'Snapshot']]

### Action
- **Type**: typing.Optional[typing.Literal['Add', 'Dynamic', 'Import', 'Modify', 'Remove']]

### LogicalResourceId
- **Type**: typing.Optional[str]

### PhysicalResourceId
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### Replacement
- **Type**: typing.Optional[typing.Literal['Conditional', 'False', 'True']]

### Scope
- **Type**: typing.Optional[typing.List[typing.Literal['CreationPolicy', 'DeletionPolicy', 'Metadata', 'Properties', 'Tags', 'UpdatePolicy', 'UpdateReplacePolicy']]]

### Details
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.ResourceChangeDetailTypeDef]]

### ChangeSetId
- **Type**: typing.Optional[str]

### ModuleInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.ModuleInfoTypeDef]

### BeforeContext
- **Type**: typing.Optional[str]

### AfterContext
- **Type**: typing.Optional[str]


# ResourceDefinitionTypeDef

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceIdentifier
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### LogicalResourceId
- **Type**: typing.Optional[str]


# ResourceDetailTypeDef

### ResourceType
- **Type**: typing.Optional[str]

### LogicalResourceId
- **Type**: typing.Optional[str]

### ResourceIdentifier
- **Type**: typing.Optional[typing.Dict[str, str]]

### ResourceStatus
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'FAILED', 'IN_PROGRESS', 'PENDING']]

### ResourceStatusReason
- **Type**: typing.Optional[str]

### Warnings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.WarningDetailTypeDef]]


# ResourceIdentifierSummaryTypeDef

### ResourceType
- **Type**: typing.Optional[str]

### LogicalResourceIds
- **Type**: typing.Optional[typing.List[str]]

### ResourceIdentifiers
- **Type**: typing.Optional[typing.List[str]]


# ResourceLocationTypeDef

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### LogicalResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# ResourceMappingTypeDef

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResourceLocationTypeDef'>
- **Required**: Yes

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResourceLocationTypeDef'>
- **Required**: Yes


# ResourceScanSummaryTypeDef

### ResourceScanId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'EXPIRED', 'FAILED', 'IN_PROGRESS']]

### StatusReason
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### PercentageCompleted
- **Type**: typing.Optional[float]


# ResourceTargetDefinitionTypeDef

### Attribute
- **Type**: typing.Optional[typing.Literal['CreationPolicy', 'DeletionPolicy', 'Metadata', 'Properties', 'Tags', 'UpdatePolicy', 'UpdateReplacePolicy']]

### Name
- **Type**: typing.Optional[str]

### RequiresRecreation
- **Type**: typing.Optional[typing.Literal['Always', 'Conditionally', 'Never']]

### Path
- **Type**: typing.Optional[str]

### BeforeValue
- **Type**: typing.Optional[str]

### AfterValue
- **Type**: typing.Optional[str]

### AttributeChangeType
- **Type**: typing.Optional[typing.Literal['Add', 'Modify', 'Remove']]


# ResourceToImportTypeDef

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### LogicalResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceIdentifier
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


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


# RollbackConfigurationOutputTypeDef

### RollbackTriggers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.RollbackTriggerTypeDef]]

### MonitoringTimeInMinutes
- **Type**: typing.Optional[int]


# RollbackConfigurationTypeDef

### RollbackTriggers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudformation_classes.RollbackTriggerTypeDef]]

### MonitoringTimeInMinutes
- **Type**: typing.Optional[int]


# RollbackConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RollbackStackInputTypeDef

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]

### RetainExceptOnCreate
- **Type**: typing.Optional[bool]


# RollbackStackOutputTypeDef

### StackId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RollbackTriggerTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ScannedResourceIdentifierTypeDef

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceIdentifier
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# ScannedResourceTypeDef

### ResourceType
- **Type**: typing.Optional[str]

### ResourceIdentifier
- **Type**: typing.Optional[typing.Dict[str, str]]

### ManagedByStack
- **Type**: typing.Optional[bool]


# SetStackPolicyInputTypeDef

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### StackPolicyBody
- **Type**: typing.Optional[str]

### StackPolicyURL
- **Type**: typing.Optional[str]


# SetTypeConfigurationOutputTypeDef

### ConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SignalResourceInputTypeDef

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### LogicalResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### UniqueId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['FAILURE', 'SUCCESS']
- **Required**: Yes


# StackDefinitionTypeDef

### StackName
- **Type**: typing.Optional[str]

### TemplateBody
- **Type**: typing.Optional[str]

### TemplateURL
- **Type**: typing.Optional[str]


# StackDriftInformationSummaryTypeDef

### StackDriftStatus
- **Type**: typing.Literal['DRIFTED', 'IN_SYNC', 'NOT_CHECKED', 'UNKNOWN']
- **Required**: Yes

### LastCheckTimestamp
- **Type**: typing.Optional[datetime.datetime]


# StackDriftInformationTypeDef

### StackDriftStatus
- **Type**: typing.Literal['DRIFTED', 'IN_SYNC', 'NOT_CHECKED', 'UNKNOWN']
- **Required**: Yes

### LastCheckTimestamp
- **Type**: typing.Optional[datetime.datetime]


# StackEventTypeDef

### StackId
- **Type**: <class 'str'>
- **Required**: Yes

### EventId
- **Type**: <class 'str'>
- **Required**: Yes

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### Timestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LogicalResourceId
- **Type**: typing.Optional[str]

### PhysicalResourceId
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### ResourceStatus
- **Type**: typing.Optional[typing.Literal['CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_COMPLETE', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'DELETE_SKIPPED', 'EXPORT_COMPLETE', 'EXPORT_FAILED', 'EXPORT_IN_PROGRESS', 'EXPORT_ROLLBACK_COMPLETE', 'EXPORT_ROLLBACK_FAILED', 'EXPORT_ROLLBACK_IN_PROGRESS', 'IMPORT_COMPLETE', 'IMPORT_FAILED', 'IMPORT_IN_PROGRESS', 'IMPORT_ROLLBACK_COMPLETE', 'IMPORT_ROLLBACK_FAILED', 'IMPORT_ROLLBACK_IN_PROGRESS', 'ROLLBACK_COMPLETE', 'ROLLBACK_FAILED', 'ROLLBACK_IN_PROGRESS', 'UPDATE_COMPLETE', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_ROLLBACK_COMPLETE', 'UPDATE_ROLLBACK_FAILED', 'UPDATE_ROLLBACK_IN_PROGRESS']]

### ResourceStatusReason
- **Type**: typing.Optional[str]

### ResourceProperties
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]

### HookType
- **Type**: typing.Optional[str]

### HookStatus
- **Type**: typing.Optional[typing.Literal['HOOK_COMPLETE_FAILED', 'HOOK_COMPLETE_SUCCEEDED', 'HOOK_FAILED', 'HOOK_IN_PROGRESS']]

### HookStatusReason
- **Type**: typing.Optional[str]

### HookInvocationPoint
- **Type**: typing.Optional[typing.Literal['PRE_PROVISION']]

### HookFailureMode
- **Type**: typing.Optional[typing.Literal['FAIL', 'WARN']]

### DetailedStatus
- **Type**: typing.Optional[typing.Literal['CONFIGURATION_COMPLETE', 'VALIDATION_FAILED']]


# StackInstanceComprehensiveStatusTypeDef

### DetailedStatus
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'FAILED', 'FAILED_IMPORT', 'INOPERABLE', 'PENDING', 'RUNNING', 'SKIPPED_SUSPENDED_ACCOUNT', 'SUCCEEDED']]


# StackInstanceFilterTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['DETAILED_STATUS', 'DRIFT_STATUS', 'LAST_OPERATION_ID']]

### Values
- **Type**: typing.Optional[str]


# StackInstanceResourceDriftsSummaryTypeDef

### StackId
- **Type**: <class 'str'>
- **Required**: Yes

### LogicalResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### StackResourceDriftStatus
- **Type**: typing.Literal['DELETED', 'IN_SYNC', 'MODIFIED', 'NOT_CHECKED']
- **Required**: Yes

### Timestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### PhysicalResourceId
- **Type**: typing.Optional[str]

### PhysicalResourceIdContext
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.PhysicalResourceIdContextKeyValuePairTypeDef]]

### PropertyDifferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.PropertyDifferenceTypeDef]]


# StackInstanceSummaryTypeDef

### StackSetId
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### Account
- **Type**: typing.Optional[str]

### StackId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CURRENT', 'INOPERABLE', 'OUTDATED']]

### StatusReason
- **Type**: typing.Optional[str]

### StackInstanceStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.StackInstanceComprehensiveStatusTypeDef]

### OrganizationalUnitId
- **Type**: typing.Optional[str]

### DriftStatus
- **Type**: typing.Optional[typing.Literal['DRIFTED', 'IN_SYNC', 'NOT_CHECKED', 'UNKNOWN']]

### LastDriftCheckTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastOperationId
- **Type**: typing.Optional[str]


# StackInstanceTypeDef

### StackSetId
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### Account
- **Type**: typing.Optional[str]

### StackId
- **Type**: typing.Optional[str]

### ParameterOverrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.ParameterTypeDef]]

### Status
- **Type**: typing.Optional[typing.Literal['CURRENT', 'INOPERABLE', 'OUTDATED']]

### StackInstanceStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.StackInstanceComprehensiveStatusTypeDef]

### StatusReason
- **Type**: typing.Optional[str]

### OrganizationalUnitId
- **Type**: typing.Optional[str]

### DriftStatus
- **Type**: typing.Optional[typing.Literal['DRIFTED', 'IN_SYNC', 'NOT_CHECKED', 'UNKNOWN']]

### LastDriftCheckTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastOperationId
- **Type**: typing.Optional[str]


# StackRefactorActionTypeDef

### Action
- **Type**: typing.Optional[typing.Literal['CREATE', 'MOVE']]

### Entity
- **Type**: typing.Optional[typing.Literal['RESOURCE', 'STACK']]

### PhysicalResourceId
- **Type**: typing.Optional[str]

### ResourceIdentifier
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Detection
- **Type**: typing.Optional[typing.Literal['AUTO', 'MANUAL']]

### DetectionReason
- **Type**: typing.Optional[str]

### TagResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.TagTypeDef]]

### UntagResources
- **Type**: typing.Optional[typing.List[str]]

### ResourceMapping
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.ResourceMappingTypeDef]


# StackRefactorSummaryTypeDef

### StackRefactorId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ExecutionStatus
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'EXECUTE_COMPLETE', 'EXECUTE_FAILED', 'EXECUTE_IN_PROGRESS', 'OBSOLETE', 'ROLLBACK_COMPLETE', 'ROLLBACK_FAILED', 'ROLLBACK_IN_PROGRESS', 'UNAVAILABLE']]

### ExecutionStatusReason
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_COMPLETE', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']]

### StatusReason
- **Type**: typing.Optional[str]


# StackResourceDetailTypeDef

### LogicalResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResourceStatus
- **Type**: typing.Literal['CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_COMPLETE', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'DELETE_SKIPPED', 'EXPORT_COMPLETE', 'EXPORT_FAILED', 'EXPORT_IN_PROGRESS', 'EXPORT_ROLLBACK_COMPLETE', 'EXPORT_ROLLBACK_FAILED', 'EXPORT_ROLLBACK_IN_PROGRESS', 'IMPORT_COMPLETE', 'IMPORT_FAILED', 'IMPORT_IN_PROGRESS', 'IMPORT_ROLLBACK_COMPLETE', 'IMPORT_ROLLBACK_FAILED', 'IMPORT_ROLLBACK_IN_PROGRESS', 'ROLLBACK_COMPLETE', 'ROLLBACK_FAILED', 'ROLLBACK_IN_PROGRESS', 'UPDATE_COMPLETE', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_ROLLBACK_COMPLETE', 'UPDATE_ROLLBACK_FAILED', 'UPDATE_ROLLBACK_IN_PROGRESS']
- **Required**: Yes

### StackName
- **Type**: typing.Optional[str]

### StackId
- **Type**: typing.Optional[str]

### PhysicalResourceId
- **Type**: typing.Optional[str]

### ResourceStatusReason
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Metadata
- **Type**: typing.Optional[str]

### DriftInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.StackResourceDriftInformationTypeDef]

### ModuleInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.ModuleInfoTypeDef]


# StackResourceDriftInformationSummaryTypeDef

### StackResourceDriftStatus
- **Type**: typing.Literal['DELETED', 'IN_SYNC', 'MODIFIED', 'NOT_CHECKED']
- **Required**: Yes

### LastCheckTimestamp
- **Type**: typing.Optional[datetime.datetime]


# StackResourceDriftInformationTypeDef

### StackResourceDriftStatus
- **Type**: typing.Literal['DELETED', 'IN_SYNC', 'MODIFIED', 'NOT_CHECKED']
- **Required**: Yes

### LastCheckTimestamp
- **Type**: typing.Optional[datetime.datetime]


# StackResourceDriftTypeDef

### StackId
- **Type**: <class 'str'>
- **Required**: Yes

### LogicalResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### StackResourceDriftStatus
- **Type**: typing.Literal['DELETED', 'IN_SYNC', 'MODIFIED', 'NOT_CHECKED']
- **Required**: Yes

### Timestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### PhysicalResourceId
- **Type**: typing.Optional[str]

### PhysicalResourceIdContext
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.PhysicalResourceIdContextKeyValuePairTypeDef]]

### ExpectedProperties
- **Type**: typing.Optional[str]

### ActualProperties
- **Type**: typing.Optional[str]

### PropertyDifferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.PropertyDifferenceTypeDef]]

### ModuleInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.ModuleInfoTypeDef]


# StackResourceSummaryTypeDef

### LogicalResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResourceStatus
- **Type**: typing.Literal['CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_COMPLETE', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'DELETE_SKIPPED', 'EXPORT_COMPLETE', 'EXPORT_FAILED', 'EXPORT_IN_PROGRESS', 'EXPORT_ROLLBACK_COMPLETE', 'EXPORT_ROLLBACK_FAILED', 'EXPORT_ROLLBACK_IN_PROGRESS', 'IMPORT_COMPLETE', 'IMPORT_FAILED', 'IMPORT_IN_PROGRESS', 'IMPORT_ROLLBACK_COMPLETE', 'IMPORT_ROLLBACK_FAILED', 'IMPORT_ROLLBACK_IN_PROGRESS', 'ROLLBACK_COMPLETE', 'ROLLBACK_FAILED', 'ROLLBACK_IN_PROGRESS', 'UPDATE_COMPLETE', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_ROLLBACK_COMPLETE', 'UPDATE_ROLLBACK_FAILED', 'UPDATE_ROLLBACK_IN_PROGRESS']
- **Required**: Yes

### PhysicalResourceId
- **Type**: typing.Optional[str]

### ResourceStatusReason
- **Type**: typing.Optional[str]

### DriftInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.StackResourceDriftInformationSummaryTypeDef]

### ModuleInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.ModuleInfoTypeDef]


# StackResourceTypeDef

### LogicalResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### Timestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResourceStatus
- **Type**: typing.Literal['CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_COMPLETE', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'DELETE_SKIPPED', 'EXPORT_COMPLETE', 'EXPORT_FAILED', 'EXPORT_IN_PROGRESS', 'EXPORT_ROLLBACK_COMPLETE', 'EXPORT_ROLLBACK_FAILED', 'EXPORT_ROLLBACK_IN_PROGRESS', 'IMPORT_COMPLETE', 'IMPORT_FAILED', 'IMPORT_IN_PROGRESS', 'IMPORT_ROLLBACK_COMPLETE', 'IMPORT_ROLLBACK_FAILED', 'IMPORT_ROLLBACK_IN_PROGRESS', 'ROLLBACK_COMPLETE', 'ROLLBACK_FAILED', 'ROLLBACK_IN_PROGRESS', 'UPDATE_COMPLETE', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_ROLLBACK_COMPLETE', 'UPDATE_ROLLBACK_FAILED', 'UPDATE_ROLLBACK_IN_PROGRESS']
- **Required**: Yes

### StackName
- **Type**: typing.Optional[str]

### StackId
- **Type**: typing.Optional[str]

### PhysicalResourceId
- **Type**: typing.Optional[str]

### ResourceStatusReason
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DriftInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.StackResourceDriftInformationTypeDef]

### ModuleInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.ModuleInfoTypeDef]


# StackSetAutoDeploymentTargetSummaryTypeDef

### OrganizationalUnitId
- **Type**: typing.Optional[str]

### Regions
- **Type**: typing.Optional[typing.List[str]]


# StackSetDriftDetectionDetailsTypeDef

### DriftStatus
- **Type**: typing.Optional[typing.Literal['DRIFTED', 'IN_SYNC', 'NOT_CHECKED']]

### DriftDetectionStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'PARTIAL_SUCCESS', 'STOPPED']]

### LastDriftCheckTimestamp
- **Type**: typing.Optional[datetime.datetime]

### TotalStackInstancesCount
- **Type**: typing.Optional[int]

### DriftedStackInstancesCount
- **Type**: typing.Optional[int]

### InSyncStackInstancesCount
- **Type**: typing.Optional[int]

### InProgressStackInstancesCount
- **Type**: typing.Optional[int]

### FailedStackInstancesCount
- **Type**: typing.Optional[int]


# StackSetOperationPreferencesOutputTypeDef

### RegionConcurrencyType
- **Type**: typing.Optional[typing.Literal['PARALLEL', 'SEQUENTIAL']]

### RegionOrder
- **Type**: typing.Optional[typing.List[str]]

### FailureToleranceCount
- **Type**: typing.Optional[int]

### FailureTolerancePercentage
- **Type**: typing.Optional[int]

### MaxConcurrentCount
- **Type**: typing.Optional[int]

### MaxConcurrentPercentage
- **Type**: typing.Optional[int]

### ConcurrencyMode
- **Type**: typing.Optional[typing.Literal['SOFT_FAILURE_TOLERANCE', 'STRICT_FAILURE_TOLERANCE']]


# StackSetOperationPreferencesTypeDef

### RegionConcurrencyType
- **Type**: typing.Optional[typing.Literal['PARALLEL', 'SEQUENTIAL']]

### RegionOrder
- **Type**: typing.Optional[typing.Sequence[str]]

### FailureToleranceCount
- **Type**: typing.Optional[int]

### FailureTolerancePercentage
- **Type**: typing.Optional[int]

### MaxConcurrentCount
- **Type**: typing.Optional[int]

### MaxConcurrentPercentage
- **Type**: typing.Optional[int]

### ConcurrencyMode
- **Type**: typing.Optional[typing.Literal['SOFT_FAILURE_TOLERANCE', 'STRICT_FAILURE_TOLERANCE']]


# StackSetOperationPreferencesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StackSetOperationResultSummaryTypeDef

### Account
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'FAILED', 'PENDING', 'RUNNING', 'SUCCEEDED']]

### StatusReason
- **Type**: typing.Optional[str]

### AccountGateResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.AccountGateResultTypeDef]

### OrganizationalUnitId
- **Type**: typing.Optional[str]


# StackSetOperationStatusDetailsTypeDef

### FailedStackInstancesCount
- **Type**: typing.Optional[int]


# StackSetOperationSummaryTypeDef

### OperationId
- **Type**: typing.Optional[str]

### Action
- **Type**: typing.Optional[typing.Literal['CREATE', 'DELETE', 'DETECT_DRIFT', 'UPDATE']]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'QUEUED', 'RUNNING', 'STOPPED', 'STOPPING', 'SUCCEEDED']]

### CreationTimestamp
- **Type**: typing.Optional[datetime.datetime]

### EndTimestamp
- **Type**: typing.Optional[datetime.datetime]

### StatusReason
- **Type**: typing.Optional[str]

### StatusDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.StackSetOperationStatusDetailsTypeDef]

### OperationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.StackSetOperationPreferencesOutputTypeDef]


# StackSetOperationTypeDef

### OperationId
- **Type**: typing.Optional[str]

### StackSetId
- **Type**: typing.Optional[str]

### Action
- **Type**: typing.Optional[typing.Literal['CREATE', 'DELETE', 'DETECT_DRIFT', 'UPDATE']]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'QUEUED', 'RUNNING', 'STOPPED', 'STOPPING', 'SUCCEEDED']]

### OperationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.StackSetOperationPreferencesOutputTypeDef]

### RetainStacks
- **Type**: typing.Optional[bool]

### AdministrationRoleARN
- **Type**: typing.Optional[str]

### ExecutionRoleName
- **Type**: typing.Optional[str]

### CreationTimestamp
- **Type**: typing.Optional[datetime.datetime]

### EndTimestamp
- **Type**: typing.Optional[datetime.datetime]

### DeploymentTargets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.DeploymentTargetsOutputTypeDef]

### StackSetDriftDetectionDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.StackSetDriftDetectionDetailsTypeDef]

### StatusReason
- **Type**: typing.Optional[str]

### StatusDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.StackSetOperationStatusDetailsTypeDef]


# StackSetSummaryTypeDef

### StackSetName
- **Type**: typing.Optional[str]

### StackSetId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED']]

### AutoDeployment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.AutoDeploymentTypeDef]

### PermissionModel
- **Type**: typing.Optional[typing.Literal['SELF_MANAGED', 'SERVICE_MANAGED']]

### DriftStatus
- **Type**: typing.Optional[typing.Literal['DRIFTED', 'IN_SYNC', 'NOT_CHECKED', 'UNKNOWN']]

### LastDriftCheckTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ManagedExecution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.ManagedExecutionTypeDef]


# StackSetTypeDef

### StackSetName
- **Type**: typing.Optional[str]

### StackSetId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED']]

### TemplateBody
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.ParameterTypeDef]]

### Capabilities
- **Type**: typing.Optional[typing.List[typing.Literal['CAPABILITY_AUTO_EXPAND', 'CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM']]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.TagTypeDef]]

### StackSetARN
- **Type**: typing.Optional[str]

### AdministrationRoleARN
- **Type**: typing.Optional[str]

### ExecutionRoleName
- **Type**: typing.Optional[str]

### StackSetDriftDetectionDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.StackSetDriftDetectionDetailsTypeDef]

### AutoDeployment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.AutoDeploymentTypeDef]

### PermissionModel
- **Type**: typing.Optional[typing.Literal['SELF_MANAGED', 'SERVICE_MANAGED']]

### OrganizationalUnitIds
- **Type**: typing.Optional[typing.List[str]]

### ManagedExecution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.ManagedExecutionTypeDef]

### Regions
- **Type**: typing.Optional[typing.List[str]]


# StackSummaryTypeDef

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### StackStatus
- **Type**: typing.Literal['CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_COMPLETE', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'IMPORT_COMPLETE', 'IMPORT_IN_PROGRESS', 'IMPORT_ROLLBACK_COMPLETE', 'IMPORT_ROLLBACK_FAILED', 'IMPORT_ROLLBACK_IN_PROGRESS', 'REVIEW_IN_PROGRESS', 'ROLLBACK_COMPLETE', 'ROLLBACK_FAILED', 'ROLLBACK_IN_PROGRESS', 'UPDATE_COMPLETE', 'UPDATE_COMPLETE_CLEANUP_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_ROLLBACK_COMPLETE', 'UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS', 'UPDATE_ROLLBACK_FAILED', 'UPDATE_ROLLBACK_IN_PROGRESS']
- **Required**: Yes

### StackId
- **Type**: typing.Optional[str]

### TemplateDescription
- **Type**: typing.Optional[str]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### DeletionTime
- **Type**: typing.Optional[datetime.datetime]

### StackStatusReason
- **Type**: typing.Optional[str]

### ParentId
- **Type**: typing.Optional[str]

### RootId
- **Type**: typing.Optional[str]

### DriftInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.StackDriftInformationSummaryTypeDef]


# StackTypeDef

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### StackStatus
- **Type**: typing.Literal['CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_COMPLETE', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'IMPORT_COMPLETE', 'IMPORT_IN_PROGRESS', 'IMPORT_ROLLBACK_COMPLETE', 'IMPORT_ROLLBACK_FAILED', 'IMPORT_ROLLBACK_IN_PROGRESS', 'REVIEW_IN_PROGRESS', 'ROLLBACK_COMPLETE', 'ROLLBACK_FAILED', 'ROLLBACK_IN_PROGRESS', 'UPDATE_COMPLETE', 'UPDATE_COMPLETE_CLEANUP_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_ROLLBACK_COMPLETE', 'UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS', 'UPDATE_ROLLBACK_FAILED', 'UPDATE_ROLLBACK_IN_PROGRESS']
- **Required**: Yes

### StackId
- **Type**: typing.Optional[str]

### ChangeSetId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.ParameterTypeDef]]

### DeletionTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### RollbackConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.RollbackConfigurationOutputTypeDef]

### StackStatusReason
- **Type**: typing.Optional[str]

### DisableRollback
- **Type**: typing.Optional[bool]

### NotificationARNs
- **Type**: typing.Optional[typing.List[str]]

### TimeoutInMinutes
- **Type**: typing.Optional[int]

### Capabilities
- **Type**: typing.Optional[typing.List[typing.Literal['CAPABILITY_AUTO_EXPAND', 'CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM']]]

### Outputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.OutputTypeDef]]

### RoleARN
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.TagTypeDef]]

### EnableTerminationProtection
- **Type**: typing.Optional[bool]

### ParentId
- **Type**: typing.Optional[str]

### RootId
- **Type**: typing.Optional[str]

### DriftInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.StackDriftInformationTypeDef]

### RetainExceptOnCreate
- **Type**: typing.Optional[bool]

### DeletionMode
- **Type**: typing.Optional[typing.Literal['FORCE_DELETE_STACK', 'STANDARD']]

### DetailedStatus
- **Type**: typing.Optional[typing.Literal['CONFIGURATION_COMPLETE', 'VALIDATION_FAILED']]


# StartResourceScanInputTypeDef

### ClientRequestToken
- **Type**: typing.Optional[str]


# StartResourceScanOutputTypeDef

### ResourceScanId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopStackSetOperationInputTypeDef

### StackSetName
- **Type**: <class 'str'>
- **Required**: Yes

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TemplateConfigurationTypeDef

### DeletionPolicy
- **Type**: typing.Optional[typing.Literal['DELETE', 'RETAIN']]

### UpdateReplacePolicy
- **Type**: typing.Optional[typing.Literal['DELETE', 'RETAIN']]


# TemplateParameterTypeDef

### ParameterKey
- **Type**: typing.Optional[str]

### DefaultValue
- **Type**: typing.Optional[str]

### NoEcho
- **Type**: typing.Optional[bool]

### Description
- **Type**: typing.Optional[str]


# TemplateProgressTypeDef

### ResourcesSucceeded
- **Type**: typing.Optional[int]

### ResourcesFailed
- **Type**: typing.Optional[int]

### ResourcesProcessing
- **Type**: typing.Optional[int]

### ResourcesPending
- **Type**: typing.Optional[int]


# TemplateSummaryConfigTypeDef

### TreatUnrecognizedResourceTypesAsWarnings
- **Type**: typing.Optional[bool]


# TemplateSummaryTypeDef

### GeneratedTemplateId
- **Type**: typing.Optional[str]

### GeneratedTemplateName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'CREATE_IN_PROGRESS', 'CREATE_PENDING', 'DELETE_IN_PROGRESS', 'DELETE_PENDING', 'FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_PENDING']]

### StatusReason
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### NumberOfResources
- **Type**: typing.Optional[int]


# TestTypeOutputTypeDef

### TypeVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TypeConfigurationDetailsTypeDef

### Arn
- **Type**: typing.Optional[str]

### Alias
- **Type**: typing.Optional[str]

### Configuration
- **Type**: typing.Optional[str]

### LastUpdated
- **Type**: typing.Optional[datetime.datetime]

### TypeArn
- **Type**: typing.Optional[str]

### TypeName
- **Type**: typing.Optional[str]

### IsDefaultConfiguration
- **Type**: typing.Optional[bool]


# TypeConfigurationIdentifierTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TypeFiltersTypeDef

### Category
- **Type**: typing.Optional[typing.Literal['ACTIVATED', 'AWS_TYPES', 'REGISTERED', 'THIRD_PARTY']]

### PublisherId
- **Type**: typing.Optional[str]

### TypeNamePrefix
- **Type**: typing.Optional[str]


# TypeSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TypeVersionSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UpdateGeneratedTemplateInputTypeDef

### GeneratedTemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### NewGeneratedTemplateName
- **Type**: typing.Optional[str]

### AddResources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudformation_classes.ResourceDefinitionTypeDef]]

### RemoveResources
- **Type**: typing.Optional[typing.Sequence[str]]

### RefreshAllResources
- **Type**: typing.Optional[bool]

### TemplateConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.TemplateConfigurationTypeDef]


# UpdateGeneratedTemplateOutputTypeDef

### GeneratedTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateStackInputStackUpdateTypeDef

### TemplateBody
- **Type**: typing.Optional[str]

### TemplateURL
- **Type**: typing.Optional[str]

### UsePreviousTemplate
- **Type**: typing.Optional[bool]

### StackPolicyDuringUpdateBody
- **Type**: typing.Optional[str]

### StackPolicyDuringUpdateURL
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudformation_classes.ParameterTypeDef]]

### Capabilities
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CAPABILITY_AUTO_EXPAND', 'CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM']]]

### ResourceTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### RoleARN
- **Type**: typing.Optional[str]

### RollbackConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.RollbackConfigurationUnionTypeDef]

### StackPolicyBody
- **Type**: typing.Optional[str]

### StackPolicyURL
- **Type**: typing.Optional[str]

### NotificationARNs
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudformation_classes.TagTypeDef]]

### DisableRollback
- **Type**: typing.Optional[bool]

### ClientRequestToken
- **Type**: typing.Optional[str]

### RetainExceptOnCreate
- **Type**: typing.Optional[bool]


# UpdateStackInputTypeDef

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateBody
- **Type**: typing.Optional[str]

### TemplateURL
- **Type**: typing.Optional[str]

### UsePreviousTemplate
- **Type**: typing.Optional[bool]

### StackPolicyDuringUpdateBody
- **Type**: typing.Optional[str]

### StackPolicyDuringUpdateURL
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudformation_classes.ParameterTypeDef]]

### Capabilities
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CAPABILITY_AUTO_EXPAND', 'CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM']]]

### ResourceTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### RoleARN
- **Type**: typing.Optional[str]

### RollbackConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.RollbackConfigurationUnionTypeDef]

### StackPolicyBody
- **Type**: typing.Optional[str]

### StackPolicyURL
- **Type**: typing.Optional[str]

### NotificationARNs
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudformation_classes.TagTypeDef]]

### DisableRollback
- **Type**: typing.Optional[bool]

### ClientRequestToken
- **Type**: typing.Optional[str]

### RetainExceptOnCreate
- **Type**: typing.Optional[bool]


# UpdateStackInstancesInputTypeDef

### StackSetName
- **Type**: <class 'str'>
- **Required**: Yes

### Regions
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Accounts
- **Type**: typing.Optional[typing.Sequence[str]]

### DeploymentTargets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.DeploymentTargetsUnionTypeDef]

### ParameterOverrides
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudformation_classes.ParameterTypeDef]]

### OperationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.StackSetOperationPreferencesUnionTypeDef]

### OperationId
- **Type**: typing.Optional[str]

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]


# UpdateStackInstancesOutputTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateStackOutputTypeDef

### StackId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateStackSetInputTypeDef

### StackSetName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### TemplateBody
- **Type**: typing.Optional[str]

### TemplateURL
- **Type**: typing.Optional[str]

### UsePreviousTemplate
- **Type**: typing.Optional[bool]

### Parameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudformation_classes.ParameterTypeDef]]

### Capabilities
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CAPABILITY_AUTO_EXPAND', 'CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM']]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudformation_classes.TagTypeDef]]

### OperationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.StackSetOperationPreferencesUnionTypeDef]

### AdministrationRoleARN
- **Type**: typing.Optional[str]

### ExecutionRoleName
- **Type**: typing.Optional[str]

### DeploymentTargets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.DeploymentTargetsUnionTypeDef]

### PermissionModel
- **Type**: typing.Optional[typing.Literal['SELF_MANAGED', 'SERVICE_MANAGED']]

### AutoDeployment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.AutoDeploymentTypeDef]

### OperationId
- **Type**: typing.Optional[str]

### Accounts
- **Type**: typing.Optional[typing.Sequence[str]]

### Regions
- **Type**: typing.Optional[typing.Sequence[str]]

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]

### ManagedExecution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation_classes.ManagedExecutionTypeDef]


# UpdateStackSetOutputTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTerminationProtectionInputTypeDef

### EnableTerminationProtection
- **Type**: <class 'bool'>
- **Required**: Yes

### StackName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateTerminationProtectionOutputTypeDef

### StackId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ValidateTemplateInputTypeDef

### TemplateBody
- **Type**: typing.Optional[str]

### TemplateURL
- **Type**: typing.Optional[str]


# ValidateTemplateOutputTypeDef

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation_classes.TemplateParameterTypeDef]
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Capabilities
- **Type**: typing.List[typing.Literal['CAPABILITY_AUTO_EXPAND', 'CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM']]
- **Required**: Yes

### CapabilitiesReason
- **Type**: <class 'str'>
- **Required**: Yes

### DeclaredTransforms
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


# WarningDetailTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WarningsTypeDef

### UnrecognizedResourceTypes
- **Type**: typing.Optional[typing.List[str]]



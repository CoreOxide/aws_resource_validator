# Cloudformation Classes

# AccountGateResult

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'SKIPPED', 'SUCCEEDED']]

### StatusReason
- **Type**: typing.Optional[str]


# AccountLimit

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[int]


# ActivateTypeInput

### Type
- **Type**: typing.Optional[typing.Literal['HOOK', 'MODULE', 'RESOURCE']]

### PublicTypeArn
- **Type**: typing.Optional[str]

### PublisherId
- **Type**: typing.Optional[str]

### TypeName
- **Type**: typing.Optional[str]

### TypeNameAlias
- **Type**: typing.Optional[str]

### AutoUpdate
- **Type**: typing.Optional[bool]

### LoggingConfig
- **Type**: <class 'NoneType'>

### ExecutionRoleArn
- **Type**: typing.Optional[str]

### VersionBump
- **Type**: typing.Optional[typing.Literal['MAJOR', 'MINOR']]

### MajorVersion
- **Type**: typing.Optional[int]


# ActivateTypeOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# AutoDeployment

### Enabled
- **Type**: typing.Optional[bool]

### RetainStacksOnAccountRemoval
- **Type**: typing.Optional[bool]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchDescribeTypeConfigurationsError

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]

### TypeConfigurationIdentifier
- **Type**: <class 'NoneType'>


# BatchDescribeTypeConfigurationsInput

### TypeConfigurationIdentifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.TypeConfigurationIdentifier]
- **Required**: Yes


# BatchDescribeTypeConfigurationsOutput

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.BatchDescribeTypeConfigurationsError]
- **Required**: Yes

### UnprocessedTypeConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.TypeConfigurationIdentifier]
- **Required**: Yes

### TypeConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.TypeConfigurationDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# CancelUpdateStackInput

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# CancelUpdateStackInputStackCancelUpdate

### ClientRequestToken
- **Type**: typing.Optional[str]


# Change

### Type
- **Type**: typing.Optional[typing.Literal['Resource']]

### HookInvocationCount
- **Type**: typing.Optional[int]

### ResourceChange
- **Type**: <class 'NoneType'>


# ChangeSetHook

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ChangeSetHookTargetDetails]


# ChangeSetHookResourceTargetDetails

### LogicalResourceId
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### ResourceAction
- **Type**: typing.Optional[typing.Literal['Add', 'Dynamic', 'Import', 'Modify', 'Remove']]


# ChangeSetHookTargetDetails

### TargetType
- **Type**: typing.Optional[typing.Literal['RESOURCE']]

### ResourceTargetDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ChangeSetHookResourceTargetDetails]


# ChangeSetSummary

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


# ContinueUpdateRollbackInput

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: typing.Optional[str]

### ResourcesToSkip
- **Type**: typing.Optional[typing.List[str]]

### ClientRequestToken
- **Type**: typing.Optional[str]


# CreateChangeSetInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.Parameter]]

### Capabilities
- **Type**: typing.Optional[typing.List[typing.Literal['CAPABILITY_AUTO_EXPAND', 'CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM']]]

### ResourceTypes
- **Type**: typing.Optional[typing.List[str]]

### RoleARN
- **Type**: typing.Optional[str]

### RollbackConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.RollbackConfiguration, aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.RollbackConfigurationOutput, NoneType]

### NotificationARNs
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.Tag]]

### ClientToken
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ChangeSetType
- **Type**: typing.Optional[typing.Literal['CREATE', 'IMPORT', 'UPDATE']]

### ResourcesToImport
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResourceToImport]]

### IncludeNestedStacks
- **Type**: typing.Optional[bool]

### OnStackFailure
- **Type**: typing.Optional[typing.Literal['DELETE', 'DO_NOTHING', 'ROLLBACK']]

### ImportExistingResources
- **Type**: typing.Optional[bool]


# CreateChangeSetOutput

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### StackId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# CreateGeneratedTemplateInput

### GeneratedTemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### Resources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResourceDefinition]]

### StackName
- **Type**: typing.Optional[str]

### TemplateConfiguration
- **Type**: <class 'NoneType'>


# CreateGeneratedTemplateOutput

### GeneratedTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# CreateStackInput

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateBody
- **Type**: typing.Optional[str]

### TemplateURL
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.Parameter]]

### DisableRollback
- **Type**: typing.Optional[bool]

### RollbackConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.RollbackConfiguration, aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.RollbackConfigurationOutput, NoneType]

### TimeoutInMinutes
- **Type**: typing.Optional[int]

### NotificationARNs
- **Type**: typing.Optional[typing.List[str]]

### Capabilities
- **Type**: typing.Optional[typing.List[typing.Literal['CAPABILITY_AUTO_EXPAND', 'CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM']]]

### ResourceTypes
- **Type**: typing.Optional[typing.List[str]]

### RoleARN
- **Type**: typing.Optional[str]

### OnFailure
- **Type**: typing.Optional[typing.Literal['DELETE', 'DO_NOTHING', 'ROLLBACK']]

### StackPolicyBody
- **Type**: typing.Optional[str]

### StackPolicyURL
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.Tag]]

### ClientRequestToken
- **Type**: typing.Optional[str]

### EnableTerminationProtection
- **Type**: typing.Optional[bool]

### RetainExceptOnCreate
- **Type**: typing.Optional[bool]


# CreateStackInputServiceResourceCreateStack

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateBody
- **Type**: typing.Optional[str]

### TemplateURL
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.Parameter]]

### DisableRollback
- **Type**: typing.Optional[bool]

### RollbackConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.RollbackConfiguration, aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.RollbackConfigurationOutput, NoneType]

### TimeoutInMinutes
- **Type**: typing.Optional[int]

### NotificationARNs
- **Type**: typing.Optional[typing.List[str]]

### Capabilities
- **Type**: typing.Optional[typing.List[typing.Literal['CAPABILITY_AUTO_EXPAND', 'CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM']]]

### ResourceTypes
- **Type**: typing.Optional[typing.List[str]]

### RoleARN
- **Type**: typing.Optional[str]

### OnFailure
- **Type**: typing.Optional[typing.Literal['DELETE', 'DO_NOTHING', 'ROLLBACK']]

### StackPolicyBody
- **Type**: typing.Optional[str]

### StackPolicyURL
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.Tag]]

### ClientRequestToken
- **Type**: typing.Optional[str]

### EnableTerminationProtection
- **Type**: typing.Optional[bool]

### RetainExceptOnCreate
- **Type**: typing.Optional[bool]


# CreateStackInstancesInput

### StackSetName
- **Type**: <class 'str'>
- **Required**: Yes

### Regions
- **Type**: typing.List[str]
- **Required**: Yes

### Accounts
- **Type**: typing.Optional[typing.List[str]]

### DeploymentTargets
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.DeploymentTargets, aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.DeploymentTargetsOutput, NoneType]

### ParameterOverrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.Parameter]]

### OperationPreferences
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackSetOperationPreferences, aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackSetOperationPreferencesOutput, NoneType]

### OperationId
- **Type**: typing.Optional[str]

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]


# CreateStackInstancesOutput

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# CreateStackOutput

### StackId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# CreateStackRefactorInput

### StackDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackDefinition]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### EnableStackCreation
- **Type**: typing.Optional[bool]

### ResourceMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResourceMapping]]


# CreateStackRefactorOutput

### StackRefactorId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# CreateStackSetInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.Parameter]]

### Capabilities
- **Type**: typing.Optional[typing.List[typing.Literal['CAPABILITY_AUTO_EXPAND', 'CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM']]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.Tag]]

### AdministrationRoleARN
- **Type**: typing.Optional[str]

### ExecutionRoleName
- **Type**: typing.Optional[str]

### PermissionModel
- **Type**: typing.Optional[typing.Literal['SELF_MANAGED', 'SERVICE_MANAGED']]

### AutoDeployment
- **Type**: <class 'NoneType'>

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]

### ClientRequestToken
- **Type**: typing.Optional[str]

### ManagedExecution
- **Type**: <class 'NoneType'>


# CreateStackSetOutput

### StackSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# DeactivateTypeInput

### TypeName
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['HOOK', 'MODULE', 'RESOURCE']]

### Arn
- **Type**: typing.Optional[str]


# DeleteChangeSetInput

### ChangeSetName
- **Type**: <class 'str'>
- **Required**: Yes

### StackName
- **Type**: typing.Optional[str]


# DeleteGeneratedTemplateInput

### GeneratedTemplateName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStackInput

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### RetainResources
- **Type**: typing.Optional[typing.List[str]]

### RoleARN
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]

### DeletionMode
- **Type**: typing.Optional[typing.Literal['FORCE_DELETE_STACK', 'STANDARD']]


# DeleteStackInputStackDelete

### RetainResources
- **Type**: typing.Optional[typing.List[str]]

### RoleARN
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]

### DeletionMode
- **Type**: typing.Optional[typing.Literal['FORCE_DELETE_STACK', 'STANDARD']]


# DeleteStackInstancesInput

### StackSetName
- **Type**: <class 'str'>
- **Required**: Yes

### Regions
- **Type**: typing.List[str]
- **Required**: Yes

### RetainStacks
- **Type**: <class 'bool'>
- **Required**: Yes

### Accounts
- **Type**: typing.Optional[typing.List[str]]

### DeploymentTargets
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.DeploymentTargets, aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.DeploymentTargetsOutput, NoneType]

### OperationPreferences
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackSetOperationPreferences, aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackSetOperationPreferencesOutput, NoneType]

### OperationId
- **Type**: typing.Optional[str]

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]


# DeleteStackInstancesOutput

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteStackSetInput

### StackSetName
- **Type**: <class 'str'>
- **Required**: Yes

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]


# DeploymentTargets

### Accounts
- **Type**: typing.Optional[typing.List[str]]

### AccountsUrl
- **Type**: typing.Optional[str]

### OrganizationalUnitIds
- **Type**: typing.Optional[typing.List[str]]

### AccountFilterType
- **Type**: typing.Optional[typing.Literal['DIFFERENCE', 'INTERSECTION', 'NONE', 'UNION']]


# DeploymentTargetsOutput

### Accounts
- **Type**: typing.Optional[typing.List[str]]

### AccountsUrl
- **Type**: typing.Optional[str]

### OrganizationalUnitIds
- **Type**: typing.Optional[typing.List[str]]

### AccountFilterType
- **Type**: typing.Optional[typing.Literal['DIFFERENCE', 'INTERSECTION', 'NONE', 'UNION']]


# DeregisterTypeInput

### Arn
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['HOOK', 'MODULE', 'RESOURCE']]

### TypeName
- **Type**: typing.Optional[str]

### VersionId
- **Type**: typing.Optional[str]


# DescribeAccountLimitsInput

### NextToken
- **Type**: typing.Optional[str]


# DescribeAccountLimitsInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.PaginatorConfig]


# DescribeAccountLimitsOutput

### AccountLimits
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.AccountLimit]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeChangeSetHooksInput

### ChangeSetName
- **Type**: <class 'str'>
- **Required**: Yes

### StackName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### LogicalResourceId
- **Type**: typing.Optional[str]


# DescribeChangeSetHooksOutput

### ChangeSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeSetName
- **Type**: <class 'str'>
- **Required**: Yes

### Hooks
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ChangeSetHook]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeChangeSetInput

### ChangeSetName
- **Type**: <class 'str'>
- **Required**: Yes

### StackName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### IncludePropertyValues
- **Type**: typing.Optional[bool]


# DescribeChangeSetInputPaginate

### ChangeSetName
- **Type**: <class 'str'>
- **Required**: Yes

### StackName
- **Type**: typing.Optional[str]

### IncludePropertyValues
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.PaginatorConfig]


# DescribeChangeSetInputWait

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
- **Type**: <class 'NoneType'>


# DescribeChangeSetOutput

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.Parameter]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.RollbackConfigurationOutput'>
- **Required**: Yes

### Capabilities
- **Type**: typing.List[typing.Literal['CAPABILITY_AUTO_EXPAND', 'CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM']]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.Tag]
- **Required**: Yes

### Changes
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.Change]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeGeneratedTemplateInput

### GeneratedTemplateName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeGeneratedTemplateOutput

### GeneratedTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### GeneratedTemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### Resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResourceDetail]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.TemplateProgress'>
- **Required**: Yes

### StackId
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.TemplateConfiguration'>
- **Required**: Yes

### TotalWarnings
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeOrganizationsAccessInput

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]


# DescribeOrganizationsAccessOutput

### Status
- **Type**: typing.Literal['DISABLED', 'DISABLED_PERMANENTLY', 'ENABLED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePublisherInput

### PublisherId
- **Type**: typing.Optional[str]


# DescribePublisherOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeResourceScanInput

### ResourceScanId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeResourceScanOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeStackDriftDetectionStatusInput

### StackDriftDetectionId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeStackDriftDetectionStatusOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeStackEventsInput

### StackName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# DescribeStackEventsInputPaginate

### StackName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.PaginatorConfig]


# DescribeStackEventsOutput

### StackEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackEvent]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeStackInstanceInput

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


# DescribeStackInstanceOutput

### StackInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeStackRefactorInput

### StackRefactorId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeStackRefactorInputWait

### StackRefactorId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeStackRefactorInputWaitExtra

### StackRefactorId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeStackRefactorOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeStackResourceDriftsInput

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### StackResourceDriftStatusFilters
- **Type**: typing.Optional[typing.List[typing.Literal['DELETED', 'IN_SYNC', 'MODIFIED', 'NOT_CHECKED']]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeStackResourceDriftsOutput

### StackResourceDrifts
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackResourceDrift]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeStackResourceInput

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### LogicalResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeStackResourceOutput

### StackResourceDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackResourceDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeStackResourcesInput

### StackName
- **Type**: typing.Optional[str]

### LogicalResourceId
- **Type**: typing.Optional[str]

### PhysicalResourceId
- **Type**: typing.Optional[str]


# DescribeStackResourcesOutput

### StackResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackResource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeStackSetInput

### StackSetName
- **Type**: <class 'str'>
- **Required**: Yes

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]


# DescribeStackSetOperationInput

### StackSetName
- **Type**: <class 'str'>
- **Required**: Yes

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]


# DescribeStackSetOperationOutput

### StackSetOperation
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackSetOperation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeStackSetOutput

### StackSet
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackSet'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeStacksInput

### StackName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# DescribeStacksInputPaginate

### StackName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.PaginatorConfig]


# DescribeStacksInputWait

### StackName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeStacksInputWaitExtra

### StackName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeStacksInputWaitExtraExtra

### StackName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeStacksInputWaitExtraExtraExtra

### StackName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeStacksInputWaitExtraExtraExtraExtra

### StackName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeStacksInputWaitExtraExtraExtraExtraExtra

### StackName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeStacksOutput

### Stacks
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.Stack]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeTypeInput

### Type
- **Type**: typing.Optional[typing.Literal['HOOK', 'MODULE', 'RESOURCE']]

### TypeName
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### VersionId
- **Type**: typing.Optional[str]

### PublisherId
- **Type**: typing.Optional[str]

### PublicVersionNumber
- **Type**: typing.Optional[str]


# DescribeTypeOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['HOOK', 'MODULE', 'RESOURCE']
- **Required**: Yes

### TypeName
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### IsDefaultVersion
- **Type**: <class 'bool'>
- **Required**: Yes

### TypeTestsStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'NOT_TESTED', 'PASSED']
- **Required**: Yes

### TypeTestsStatusDescription
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Schema
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisioningType
- **Type**: typing.Literal['FULLY_MUTABLE', 'IMMUTABLE', 'NON_PROVISIONABLE']
- **Required**: Yes

### DeprecatedStatus
- **Type**: typing.Literal['DEPRECATED', 'LIVE']
- **Required**: Yes

### LoggingConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.LoggingConfig'>
- **Required**: Yes

### RequiredActivatedTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.RequiredActivatedType]
- **Required**: Yes

### ExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Visibility
- **Type**: typing.Literal['PRIVATE', 'PUBLIC']
- **Required**: Yes

### SourceUrl
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentationUrl
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdated
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TimeCreated
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ConfigurationSchema
- **Type**: <class 'str'>
- **Required**: Yes

### PublisherId
- **Type**: <class 'str'>
- **Required**: Yes

### OriginalTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### OriginalTypeArn
- **Type**: <class 'str'>
- **Required**: Yes

### PublicVersionNumber
- **Type**: <class 'str'>
- **Required**: Yes

### LatestPublicVersion
- **Type**: <class 'str'>
- **Required**: Yes

### IsActivated
- **Type**: <class 'bool'>
- **Required**: Yes

### AutoUpdate
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTypeRegistrationInput

### RegistrationToken
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTypeRegistrationInputWait

### RegistrationToken
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeTypeRegistrationOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# DetectStackDriftInput

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### LogicalResourceIds
- **Type**: typing.Optional[typing.List[str]]


# DetectStackDriftOutput

### StackDriftDetectionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# DetectStackResourceDriftInput

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### LogicalResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DetectStackResourceDriftOutput

### StackResourceDrift
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackResourceDrift'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# DetectStackSetDriftInput

### StackSetName
- **Type**: <class 'str'>
- **Required**: Yes

### OperationPreferences
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackSetOperationPreferences, aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackSetOperationPreferencesOutput, NoneType]

### OperationId
- **Type**: typing.Optional[str]

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]


# DetectStackSetDriftOutput

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# EstimateTemplateCostInput

### TemplateBody
- **Type**: typing.Optional[str]

### TemplateURL
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.Parameter]]


# EstimateTemplateCostOutput

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# ExecuteChangeSetInput

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


# ExecuteStackRefactorInput

### StackRefactorId
- **Type**: <class 'str'>
- **Required**: Yes


# Export

### ExportingStackId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# GetGeneratedTemplateInput

### GeneratedTemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### Format
- **Type**: typing.Optional[typing.Literal['JSON', 'YAML']]


# GetGeneratedTemplateOutput

### Status
- **Type**: typing.Literal['COMPLETE', 'CREATE_IN_PROGRESS', 'CREATE_PENDING', 'DELETE_IN_PROGRESS', 'DELETE_PENDING', 'FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_PENDING']
- **Required**: Yes

### TemplateBody
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# GetStackPolicyInput

### StackName
- **Type**: <class 'str'>
- **Required**: Yes


# GetStackPolicyOutput

### StackPolicyBody
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# GetTemplateInput

### StackName
- **Type**: typing.Optional[str]

### ChangeSetName
- **Type**: typing.Optional[str]

### TemplateStage
- **Type**: typing.Optional[typing.Literal['Original', 'Processed']]


# GetTemplateOutput

### TemplateBody
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes

### StagesAvailable
- **Type**: typing.List[typing.Literal['Original', 'Processed']]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# GetTemplateSummaryInput

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
- **Type**: <class 'NoneType'>


# GetTemplateSummaryOutput

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ParameterDeclaration]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResourceIdentifierSummary]
- **Required**: Yes

### Warnings
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.Warnings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# HookResultSummary

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


# ImportStacksToStackSetInput

### StackSetName
- **Type**: <class 'str'>
- **Required**: Yes

### StackIds
- **Type**: typing.Optional[typing.List[str]]

### StackIdsUrl
- **Type**: typing.Optional[str]

### OrganizationalUnitIds
- **Type**: typing.Optional[typing.List[str]]

### OperationPreferences
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackSetOperationPreferences, aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackSetOperationPreferencesOutput, NoneType]

### OperationId
- **Type**: typing.Optional[str]

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]


# ImportStacksToStackSetOutput

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# ListChangeSetsInput

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListChangeSetsInputPaginate

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.PaginatorConfig]


# ListChangeSetsOutput

### Summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ChangeSetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListExportsInput

### NextToken
- **Type**: typing.Optional[str]


# ListExportsInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.PaginatorConfig]


# ListExportsOutput

### Exports
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.Export]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGeneratedTemplatesInput

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListGeneratedTemplatesInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.PaginatorConfig]


# ListGeneratedTemplatesOutput

### Summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.TemplateSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHookResultsInput

### TargetType
- **Type**: typing.Literal['CHANGE_SET', 'CLOUD_CONTROL', 'RESOURCE', 'STACK']
- **Required**: Yes

### TargetId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHookResultsOutput

### TargetType
- **Type**: typing.Literal['CHANGE_SET', 'CLOUD_CONTROL', 'RESOURCE', 'STACK']
- **Required**: Yes

### TargetId
- **Type**: <class 'str'>
- **Required**: Yes

### HookResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.HookResultSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListImportsInput

### ExportName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListImportsInputPaginate

### ExportName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.PaginatorConfig]


# ListImportsOutput

### Imports
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourceScanRelatedResourcesInput

### ResourceScanId
- **Type**: <class 'str'>
- **Required**: Yes

### Resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ScannedResourceIdentifier]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListResourceScanRelatedResourcesInputPaginate

### ResourceScanId
- **Type**: <class 'str'>
- **Required**: Yes

### Resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ScannedResourceIdentifier]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.PaginatorConfig]


# ListResourceScanRelatedResourcesOutput

### RelatedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ScannedResource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourceScanResourcesInput

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


# ListResourceScanResourcesInputPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.PaginatorConfig]


# ListResourceScanResourcesOutput

### Resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ScannedResource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourceScansInput

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListResourceScansInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.PaginatorConfig]


# ListResourceScansOutput

### ResourceScanSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResourceScanSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStackInstanceResourceDriftsInput

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
- **Type**: typing.Optional[typing.List[typing.Literal['DELETED', 'IN_SYNC', 'MODIFIED', 'NOT_CHECKED']]]

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]


# ListStackInstanceResourceDriftsOutput

### Summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackInstanceResourceDriftsSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStackInstancesInput

### StackSetName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackInstanceFilter]]

### StackInstanceAccount
- **Type**: typing.Optional[str]

### StackInstanceRegion
- **Type**: typing.Optional[str]

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]


# ListStackInstancesInputPaginate

### StackSetName
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackInstanceFilter]]

### StackInstanceAccount
- **Type**: typing.Optional[str]

### StackInstanceRegion
- **Type**: typing.Optional[str]

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.PaginatorConfig]


# ListStackInstancesOutput

### Summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackInstanceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStackRefactorActionsInput

### StackRefactorId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListStackRefactorActionsInputPaginate

### StackRefactorId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.PaginatorConfig]


# ListStackRefactorActionsOutput

### StackRefactorActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackRefactorAction]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStackRefactorsInput

### ExecutionStatusFilter
- **Type**: typing.Optional[typing.List[typing.Literal['AVAILABLE', 'EXECUTE_COMPLETE', 'EXECUTE_FAILED', 'EXECUTE_IN_PROGRESS', 'OBSOLETE', 'ROLLBACK_COMPLETE', 'ROLLBACK_FAILED', 'ROLLBACK_IN_PROGRESS', 'UNAVAILABLE']]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListStackRefactorsInputPaginate

### ExecutionStatusFilter
- **Type**: typing.Optional[typing.List[typing.Literal['AVAILABLE', 'EXECUTE_COMPLETE', 'EXECUTE_FAILED', 'EXECUTE_IN_PROGRESS', 'OBSOLETE', 'ROLLBACK_COMPLETE', 'ROLLBACK_FAILED', 'ROLLBACK_IN_PROGRESS', 'UNAVAILABLE']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.PaginatorConfig]


# ListStackRefactorsOutput

### StackRefactorSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackRefactorSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStackResourcesInput

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStackResourcesInputPaginate

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.PaginatorConfig]


# ListStackResourcesOutput

### StackResourceSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackResourceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStackSetAutoDeploymentTargetsInput

### StackSetName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]


# ListStackSetAutoDeploymentTargetsOutput

### Summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackSetAutoDeploymentTargetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStackSetOperationResultsInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.OperationResultFilter]]


# ListStackSetOperationResultsInputPaginate

### StackSetName
- **Type**: <class 'str'>
- **Required**: Yes

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.OperationResultFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.PaginatorConfig]


# ListStackSetOperationResultsOutput

### Summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackSetOperationResultSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStackSetOperationsInput

### StackSetName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]


# ListStackSetOperationsInputPaginate

### StackSetName
- **Type**: <class 'str'>
- **Required**: Yes

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.PaginatorConfig]


# ListStackSetOperationsOutput

### Summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackSetOperationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStackSetsInput

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED']]

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]


# ListStackSetsInputPaginate

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED']]

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.PaginatorConfig]


# ListStackSetsOutput

### Summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackSetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStacksInput

### NextToken
- **Type**: typing.Optional[str]

### StackStatusFilter
- **Type**: typing.Optional[typing.List[typing.Literal['CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_COMPLETE', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'IMPORT_COMPLETE', 'IMPORT_IN_PROGRESS', 'IMPORT_ROLLBACK_COMPLETE', 'IMPORT_ROLLBACK_FAILED', 'IMPORT_ROLLBACK_IN_PROGRESS', 'REVIEW_IN_PROGRESS', 'ROLLBACK_COMPLETE', 'ROLLBACK_FAILED', 'ROLLBACK_IN_PROGRESS', 'UPDATE_COMPLETE', 'UPDATE_COMPLETE_CLEANUP_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_ROLLBACK_COMPLETE', 'UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS', 'UPDATE_ROLLBACK_FAILED', 'UPDATE_ROLLBACK_IN_PROGRESS']]]


# ListStacksInputPaginate

### StackStatusFilter
- **Type**: typing.Optional[typing.List[typing.Literal['CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_COMPLETE', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'IMPORT_COMPLETE', 'IMPORT_IN_PROGRESS', 'IMPORT_ROLLBACK_COMPLETE', 'IMPORT_ROLLBACK_FAILED', 'IMPORT_ROLLBACK_IN_PROGRESS', 'REVIEW_IN_PROGRESS', 'ROLLBACK_COMPLETE', 'ROLLBACK_FAILED', 'ROLLBACK_IN_PROGRESS', 'UPDATE_COMPLETE', 'UPDATE_COMPLETE_CLEANUP_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_ROLLBACK_COMPLETE', 'UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS', 'UPDATE_ROLLBACK_FAILED', 'UPDATE_ROLLBACK_IN_PROGRESS']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.PaginatorConfig]


# ListStacksOutput

### StackSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTypeRegistrationsInput

### Type
- **Type**: typing.Optional[typing.Literal['HOOK', 'MODULE', 'RESOURCE']]

### TypeName
- **Type**: typing.Optional[str]

### TypeArn
- **Type**: typing.Optional[str]

### RegistrationStatusFilter
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'FAILED', 'IN_PROGRESS']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTypeRegistrationsOutput

### RegistrationTokenList
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTypeVersionsInput

### Type
- **Type**: typing.Optional[typing.Literal['HOOK', 'MODULE', 'RESOURCE']]

### TypeName
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### DeprecatedStatus
- **Type**: typing.Optional[typing.Literal['DEPRECATED', 'LIVE']]

### PublisherId
- **Type**: typing.Optional[str]


# ListTypeVersionsOutput

### TypeVersionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.TypeVersionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTypesInput

### Visibility
- **Type**: typing.Optional[typing.Literal['PRIVATE', 'PUBLIC']]

### ProvisioningType
- **Type**: typing.Optional[typing.Literal['FULLY_MUTABLE', 'IMMUTABLE', 'NON_PROVISIONABLE']]

### DeprecatedStatus
- **Type**: typing.Optional[typing.Literal['DEPRECATED', 'LIVE']]

### Type
- **Type**: typing.Optional[typing.Literal['HOOK', 'MODULE', 'RESOURCE']]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.TypeFilters]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTypesInputPaginate

### Visibility
- **Type**: typing.Optional[typing.Literal['PRIVATE', 'PUBLIC']]

### ProvisioningType
- **Type**: typing.Optional[typing.Literal['FULLY_MUTABLE', 'IMMUTABLE', 'NON_PROVISIONABLE']]

### DeprecatedStatus
- **Type**: typing.Optional[typing.Literal['DEPRECATED', 'LIVE']]

### Type
- **Type**: typing.Optional[typing.Literal['HOOK', 'MODULE', 'RESOURCE']]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.TypeFilters]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.PaginatorConfig]


# ListTypesOutput

### TypeSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.TypeSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LoggingConfig

### LogRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### LogGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# ManagedExecution

### Active
- **Type**: typing.Optional[bool]


# ModuleInfo

### TypeHierarchy
- **Type**: typing.Optional[str]

### LogicalIdHierarchy
- **Type**: typing.Optional[str]


# OperationResultFilter

### Name
- **Type**: typing.Optional[typing.Literal['OPERATION_RESULT_STATUS']]

### Values
- **Type**: typing.Optional[str]


# Output

### OutputKey
- **Type**: typing.Optional[str]

### OutputValue
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ExportName
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Parameter

### ParameterKey
- **Type**: typing.Optional[str]

### ParameterValue
- **Type**: typing.Optional[str]

### UsePreviousValue
- **Type**: typing.Optional[bool]

### ResolvedValue
- **Type**: typing.Optional[str]


# ParameterConstraints

### AllowedValues
- **Type**: typing.Optional[typing.List[str]]


# ParameterDeclaration

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
- **Type**: <class 'NoneType'>


# PhysicalResourceIdContextKeyValuePair

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# PropertyDifference

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


# PublishTypeInput

### Type
- **Type**: typing.Optional[typing.Literal['HOOK', 'MODULE', 'RESOURCE']]

### Arn
- **Type**: typing.Optional[str]

### TypeName
- **Type**: typing.Optional[str]

### PublicVersionNumber
- **Type**: typing.Optional[str]


# PublishTypeOutput

### PublicTypeArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# RecordHandlerProgressInput

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


# RegisterPublisherInput

### AcceptTermsAndConditions
- **Type**: typing.Optional[bool]

### ConnectionArn
- **Type**: typing.Optional[str]


# RegisterPublisherOutput

### PublisherId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# RegisterTypeInput

### TypeName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaHandlerPackage
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Optional[typing.Literal['HOOK', 'MODULE', 'RESOURCE']]

### LoggingConfig
- **Type**: <class 'NoneType'>

### ExecutionRoleArn
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]


# RegisterTypeOutput

### RegistrationToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# RequiredActivatedType

### TypeNameAlias
- **Type**: typing.Optional[str]

### OriginalTypeName
- **Type**: typing.Optional[str]

### PublisherId
- **Type**: typing.Optional[str]

### SupportedMajorVersions
- **Type**: typing.Optional[typing.List[int]]


# ResourceChange

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResourceChangeDetail]]

### ChangeSetId
- **Type**: typing.Optional[str]

### ModuleInfo
- **Type**: <class 'NoneType'>

### BeforeContext
- **Type**: typing.Optional[str]

### AfterContext
- **Type**: typing.Optional[str]


# ResourceChangeDetail

### Target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResourceTargetDefinition]

### Evaluation
- **Type**: typing.Optional[typing.Literal['Dynamic', 'Static']]

### ChangeSource
- **Type**: typing.Optional[typing.Literal['Automatic', 'DirectModification', 'ParameterReference', 'ResourceAttribute', 'ResourceReference']]

### CausingEntity
- **Type**: typing.Optional[str]


# ResourceDefinition

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceIdentifier
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### LogicalResourceId
- **Type**: typing.Optional[str]


# ResourceDetail

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.WarningDetail]]


# ResourceIdentifierSummary

### ResourceType
- **Type**: typing.Optional[str]

### LogicalResourceIds
- **Type**: typing.Optional[typing.List[str]]

### ResourceIdentifiers
- **Type**: typing.Optional[typing.List[str]]


# ResourceLocation

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### LogicalResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# ResourceMapping

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResourceLocation'>
- **Required**: Yes

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResourceLocation'>
- **Required**: Yes


# ResourceScanSummary

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


# ResourceTargetDefinition

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


# ResourceToImport

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### LogicalResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceIdentifier
- **Type**: typing.Dict[str, str]
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


# RollbackConfiguration

### RollbackTriggers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.RollbackTrigger]]

### MonitoringTimeInMinutes
- **Type**: typing.Optional[int]


# RollbackConfigurationOutput

### RollbackTriggers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.RollbackTrigger]]

### MonitoringTimeInMinutes
- **Type**: typing.Optional[int]


# RollbackStackInput

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]

### RetainExceptOnCreate
- **Type**: typing.Optional[bool]


# RollbackStackOutput

### StackId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# RollbackTrigger

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: <class 'str'>
- **Required**: Yes


# ScannedResource

### ResourceType
- **Type**: typing.Optional[str]

### ResourceIdentifier
- **Type**: typing.Optional[typing.Dict[str, str]]

### ManagedByStack
- **Type**: typing.Optional[bool]


# ScannedResourceIdentifier

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceIdentifier
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# SetStackPolicyInput

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### StackPolicyBody
- **Type**: typing.Optional[str]

### StackPolicyURL
- **Type**: typing.Optional[str]


# SetTypeConfigurationInput

### Configuration
- **Type**: <class 'str'>
- **Required**: Yes

### TypeArn
- **Type**: typing.Optional[str]

### ConfigurationAlias
- **Type**: typing.Optional[str]

### TypeName
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['HOOK', 'MODULE', 'RESOURCE']]


# SetTypeConfigurationOutput

### ConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# SetaultVersionInput

### Arn
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['HOOK', 'MODULE', 'RESOURCE']]

### TypeName
- **Type**: typing.Optional[str]

### VersionId
- **Type**: typing.Optional[str]


# SignalResourceInput

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


# Stack

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.Parameter]]

### DeletionTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### RollbackConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.RollbackConfigurationOutput]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.Output]]

### RoleARN
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.Tag]]

### EnableTerminationProtection
- **Type**: typing.Optional[bool]

### ParentId
- **Type**: typing.Optional[str]

### RootId
- **Type**: typing.Optional[str]

### DriftInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackDriftInformation]

### RetainExceptOnCreate
- **Type**: typing.Optional[bool]

### DeletionMode
- **Type**: typing.Optional[typing.Literal['FORCE_DELETE_STACK', 'STANDARD']]

### DetailedStatus
- **Type**: typing.Optional[typing.Literal['CONFIGURATION_COMPLETE', 'VALIDATION_FAILED']]


# StackDefinition

### StackName
- **Type**: typing.Optional[str]

### TemplateBody
- **Type**: typing.Optional[str]

### TemplateURL
- **Type**: typing.Optional[str]


# StackDriftInformation

### StackDriftStatus
- **Type**: typing.Literal['DRIFTED', 'IN_SYNC', 'NOT_CHECKED', 'UNKNOWN']
- **Required**: Yes

### LastCheckTimestamp
- **Type**: typing.Optional[datetime.datetime]


# StackDriftInformationSummary

### StackDriftStatus
- **Type**: typing.Literal['DRIFTED', 'IN_SYNC', 'NOT_CHECKED', 'UNKNOWN']
- **Required**: Yes

### LastCheckTimestamp
- **Type**: typing.Optional[datetime.datetime]


# StackEvent

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


# StackInstance

### StackSetId
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### Account
- **Type**: typing.Optional[str]

### StackId
- **Type**: typing.Optional[str]

### ParameterOverrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.Parameter]]

### Status
- **Type**: typing.Optional[typing.Literal['CURRENT', 'INOPERABLE', 'OUTDATED']]

### StackInstanceStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackInstanceComprehensiveStatus]

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


# StackInstanceComprehensiveStatus

### DetailedStatus
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'FAILED', 'FAILED_IMPORT', 'INOPERABLE', 'PENDING', 'RUNNING', 'SKIPPED_SUSPENDED_ACCOUNT', 'SUCCEEDED']]


# StackInstanceFilter

### Name
- **Type**: typing.Optional[typing.Literal['DETAILED_STATUS', 'DRIFT_STATUS', 'LAST_OPERATION_ID']]

### Values
- **Type**: typing.Optional[str]


# StackInstanceResourceDriftsSummary

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.PhysicalResourceIdContextKeyValuePair]]

### PropertyDifferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.PropertyDifference]]


# StackInstanceSummary

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackInstanceComprehensiveStatus]

### OrganizationalUnitId
- **Type**: typing.Optional[str]

### DriftStatus
- **Type**: typing.Optional[typing.Literal['DRIFTED', 'IN_SYNC', 'NOT_CHECKED', 'UNKNOWN']]

### LastDriftCheckTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastOperationId
- **Type**: typing.Optional[str]


# StackRefactorAction

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.Tag]]

### UntagResources
- **Type**: typing.Optional[typing.List[str]]

### ResourceMapping
- **Type**: <class 'NoneType'>


# StackRefactorSummary

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


# StackResource

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackResourceDriftInformation]

### ModuleInfo
- **Type**: <class 'NoneType'>


# StackResourceDetail

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackResourceDriftInformation]

### ModuleInfo
- **Type**: <class 'NoneType'>


# StackResourceDrift

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.PhysicalResourceIdContextKeyValuePair]]

### ExpectedProperties
- **Type**: typing.Optional[str]

### ActualProperties
- **Type**: typing.Optional[str]

### PropertyDifferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.PropertyDifference]]

### ModuleInfo
- **Type**: <class 'NoneType'>


# StackResourceDriftInformation

### StackResourceDriftStatus
- **Type**: typing.Literal['DELETED', 'IN_SYNC', 'MODIFIED', 'NOT_CHECKED']
- **Required**: Yes

### LastCheckTimestamp
- **Type**: typing.Optional[datetime.datetime]


# StackResourceDriftInformationSummary

### StackResourceDriftStatus
- **Type**: typing.Literal['DELETED', 'IN_SYNC', 'MODIFIED', 'NOT_CHECKED']
- **Required**: Yes

### LastCheckTimestamp
- **Type**: typing.Optional[datetime.datetime]


# StackResourceSummary

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackResourceDriftInformationSummary]

### ModuleInfo
- **Type**: <class 'NoneType'>


# StackSet

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.Parameter]]

### Capabilities
- **Type**: typing.Optional[typing.List[typing.Literal['CAPABILITY_AUTO_EXPAND', 'CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM']]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.Tag]]

### StackSetARN
- **Type**: typing.Optional[str]

### AdministrationRoleARN
- **Type**: typing.Optional[str]

### ExecutionRoleName
- **Type**: typing.Optional[str]

### StackSetDriftDetectionDetails
- **Type**: <class 'NoneType'>

### AutoDeployment
- **Type**: <class 'NoneType'>

### PermissionModel
- **Type**: typing.Optional[typing.Literal['SELF_MANAGED', 'SERVICE_MANAGED']]

### OrganizationalUnitIds
- **Type**: typing.Optional[typing.List[str]]

### ManagedExecution
- **Type**: <class 'NoneType'>

### Regions
- **Type**: typing.Optional[typing.List[str]]


# StackSetAutoDeploymentTargetSummary

### OrganizationalUnitId
- **Type**: typing.Optional[str]

### Regions
- **Type**: typing.Optional[typing.List[str]]


# StackSetDriftDetectionDetails

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


# StackSetOperation

### OperationId
- **Type**: typing.Optional[str]

### StackSetId
- **Type**: typing.Optional[str]

### Action
- **Type**: typing.Optional[typing.Literal['CREATE', 'DELETE', 'DETECT_DRIFT', 'UPDATE']]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'QUEUED', 'RUNNING', 'STOPPED', 'STOPPING', 'SUCCEEDED']]

### OperationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackSetOperationPreferencesOutput]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.DeploymentTargetsOutput]

### StackSetDriftDetectionDetails
- **Type**: <class 'NoneType'>

### StatusReason
- **Type**: typing.Optional[str]

### StatusDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackSetOperationStatusDetails]


# StackSetOperationPreferences

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


# StackSetOperationPreferencesOutput

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


# StackSetOperationResultSummary

### Account
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'FAILED', 'PENDING', 'RUNNING', 'SUCCEEDED']]

### StatusReason
- **Type**: typing.Optional[str]

### AccountGateResult
- **Type**: <class 'NoneType'>

### OrganizationalUnitId
- **Type**: typing.Optional[str]


# StackSetOperationStatusDetails

### FailedStackInstancesCount
- **Type**: typing.Optional[int]


# StackSetOperationSummary

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackSetOperationStatusDetails]

### OperationPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackSetOperationPreferencesOutput]


# StackSetSummary

### StackSetName
- **Type**: typing.Optional[str]

### StackSetId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED']]

### AutoDeployment
- **Type**: <class 'NoneType'>

### PermissionModel
- **Type**: typing.Optional[typing.Literal['SELF_MANAGED', 'SERVICE_MANAGED']]

### DriftStatus
- **Type**: typing.Optional[typing.Literal['DRIFTED', 'IN_SYNC', 'NOT_CHECKED', 'UNKNOWN']]

### LastDriftCheckTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ManagedExecution
- **Type**: <class 'NoneType'>


# StackSummary

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackDriftInformationSummary]


# StartResourceScanInput

### ClientRequestToken
- **Type**: typing.Optional[str]


# StartResourceScanOutput

### ResourceScanId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# StopStackSetOperationInput

### StackSetName
- **Type**: <class 'str'>
- **Required**: Yes

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TemplateConfiguration

### DeletionPolicy
- **Type**: typing.Optional[typing.Literal['DELETE', 'RETAIN']]

### UpdateReplacePolicy
- **Type**: typing.Optional[typing.Literal['DELETE', 'RETAIN']]


# TemplateParameter

### ParameterKey
- **Type**: typing.Optional[str]

### DefaultValue
- **Type**: typing.Optional[str]

### NoEcho
- **Type**: typing.Optional[bool]

### Description
- **Type**: typing.Optional[str]


# TemplateProgress

### ResourcesSucceeded
- **Type**: typing.Optional[int]

### ResourcesFailed
- **Type**: typing.Optional[int]

### ResourcesProcessing
- **Type**: typing.Optional[int]

### ResourcesPending
- **Type**: typing.Optional[int]


# TemplateSummary

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


# TemplateSummaryConfig

### TreatUnrecognizedResourceTypesAsWarnings
- **Type**: typing.Optional[bool]


# TestTypeInput

### Arn
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['HOOK', 'MODULE', 'RESOURCE']]

### TypeName
- **Type**: typing.Optional[str]

### VersionId
- **Type**: typing.Optional[str]

### LogDeliveryBucket
- **Type**: typing.Optional[str]


# TestTypeOutput

### TypeVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# TypeConfigurationDetails

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


# TypeConfigurationIdentifier

### TypeArn
- **Type**: typing.Optional[str]

### TypeConfigurationAlias
- **Type**: typing.Optional[str]

### TypeConfigurationArn
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['HOOK', 'MODULE', 'RESOURCE']]

### TypeName
- **Type**: typing.Optional[str]


# TypeFilters

### Category
- **Type**: typing.Optional[typing.Literal['ACTIVATED', 'AWS_TYPES', 'REGISTERED', 'THIRD_PARTY']]

### PublisherId
- **Type**: typing.Optional[str]

### TypeNamePrefix
- **Type**: typing.Optional[str]


# TypeSummary

### Type
- **Type**: typing.Optional[typing.Literal['HOOK', 'MODULE', 'RESOURCE']]

### TypeName
- **Type**: typing.Optional[str]

### DefaultVersionId
- **Type**: typing.Optional[str]

### TypeArn
- **Type**: typing.Optional[str]

### LastUpdated
- **Type**: typing.Optional[datetime.datetime]

### Description
- **Type**: typing.Optional[str]

### PublisherId
- **Type**: typing.Optional[str]

### OriginalTypeName
- **Type**: typing.Optional[str]

### PublicVersionNumber
- **Type**: typing.Optional[str]

### LatestPublicVersion
- **Type**: typing.Optional[str]

### PublisherIdentity
- **Type**: typing.Optional[typing.Literal['AWS_Marketplace', 'Bitbucket', 'GitHub']]

### PublisherName
- **Type**: typing.Optional[str]

### IsActivated
- **Type**: typing.Optional[bool]


# TypeVersionSummary

### Type
- **Type**: typing.Optional[typing.Literal['HOOK', 'MODULE', 'RESOURCE']]

### TypeName
- **Type**: typing.Optional[str]

### VersionId
- **Type**: typing.Optional[str]

### IsDefaultVersion
- **Type**: typing.Optional[bool]

### Arn
- **Type**: typing.Optional[str]

### TimeCreated
- **Type**: typing.Optional[datetime.datetime]

### Description
- **Type**: typing.Optional[str]

### PublicVersionNumber
- **Type**: typing.Optional[str]


# UpdateGeneratedTemplateInput

### GeneratedTemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### NewGeneratedTemplateName
- **Type**: typing.Optional[str]

### AddResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResourceDefinition]]

### RemoveResources
- **Type**: typing.Optional[typing.List[str]]

### RefreshAllResources
- **Type**: typing.Optional[bool]

### TemplateConfiguration
- **Type**: <class 'NoneType'>


# UpdateGeneratedTemplateOutput

### GeneratedTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateStackInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.Parameter]]

### Capabilities
- **Type**: typing.Optional[typing.List[typing.Literal['CAPABILITY_AUTO_EXPAND', 'CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM']]]

### ResourceTypes
- **Type**: typing.Optional[typing.List[str]]

### RoleARN
- **Type**: typing.Optional[str]

### RollbackConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.RollbackConfiguration, aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.RollbackConfigurationOutput, NoneType]

### StackPolicyBody
- **Type**: typing.Optional[str]

### StackPolicyURL
- **Type**: typing.Optional[str]

### NotificationARNs
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.Tag]]

### DisableRollback
- **Type**: typing.Optional[bool]

### ClientRequestToken
- **Type**: typing.Optional[str]

### RetainExceptOnCreate
- **Type**: typing.Optional[bool]


# UpdateStackInputStackUpdate

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.Parameter]]

### Capabilities
- **Type**: typing.Optional[typing.List[typing.Literal['CAPABILITY_AUTO_EXPAND', 'CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM']]]

### ResourceTypes
- **Type**: typing.Optional[typing.List[str]]

### RoleARN
- **Type**: typing.Optional[str]

### RollbackConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.RollbackConfiguration, aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.RollbackConfigurationOutput, NoneType]

### StackPolicyBody
- **Type**: typing.Optional[str]

### StackPolicyURL
- **Type**: typing.Optional[str]

### NotificationARNs
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.Tag]]

### DisableRollback
- **Type**: typing.Optional[bool]

### ClientRequestToken
- **Type**: typing.Optional[str]

### RetainExceptOnCreate
- **Type**: typing.Optional[bool]


# UpdateStackInstancesInput

### StackSetName
- **Type**: <class 'str'>
- **Required**: Yes

### Regions
- **Type**: typing.List[str]
- **Required**: Yes

### Accounts
- **Type**: typing.Optional[typing.List[str]]

### DeploymentTargets
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.DeploymentTargets, aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.DeploymentTargetsOutput, NoneType]

### ParameterOverrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.Parameter]]

### OperationPreferences
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackSetOperationPreferences, aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackSetOperationPreferencesOutput, NoneType]

### OperationId
- **Type**: typing.Optional[str]

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]


# UpdateStackInstancesOutput

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateStackOutput

### StackId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateStackSetInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.Parameter]]

### Capabilities
- **Type**: typing.Optional[typing.List[typing.Literal['CAPABILITY_AUTO_EXPAND', 'CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM']]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.Tag]]

### OperationPreferences
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackSetOperationPreferences, aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.StackSetOperationPreferencesOutput, NoneType]

### AdministrationRoleARN
- **Type**: typing.Optional[str]

### ExecutionRoleName
- **Type**: typing.Optional[str]

### DeploymentTargets
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.DeploymentTargets, aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.DeploymentTargetsOutput, NoneType]

### PermissionModel
- **Type**: typing.Optional[typing.Literal['SELF_MANAGED', 'SERVICE_MANAGED']]

### AutoDeployment
- **Type**: <class 'NoneType'>

### OperationId
- **Type**: typing.Optional[str]

### Accounts
- **Type**: typing.Optional[typing.List[str]]

### Regions
- **Type**: typing.Optional[typing.List[str]]

### CallAs
- **Type**: typing.Optional[typing.Literal['DELEGATED_ADMIN', 'SELF']]

### ManagedExecution
- **Type**: <class 'NoneType'>


# UpdateStackSetOutput

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTerminationProtectionInput

### EnableTerminationProtection
- **Type**: <class 'bool'>
- **Required**: Yes

### StackName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateTerminationProtectionOutput

### StackId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# ValidateTemplateInput

### TemplateBody
- **Type**: typing.Optional[str]

### TemplateURL
- **Type**: typing.Optional[str]


# ValidateTemplateOutput

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.TemplateParameter]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.ResponseMetadata'>
- **Required**: Yes


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


# WarningDetail

### Type
- **Type**: typing.Optional[typing.Literal['MUTUALLY_EXCLUSIVE_PROPERTIES', 'MUTUALLY_EXCLUSIVE_TYPES', 'UNSUPPORTED_PROPERTIES']]

### Properties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudformation.cloudformation_classes.WarningProperty]]


# WarningProperty

### PropertyPath
- **Type**: typing.Optional[str]

### Required
- **Type**: typing.Optional[bool]

### Description
- **Type**: typing.Optional[str]


# Warnings

### UnrecognizedResourceTypes
- **Type**: typing.Optional[typing.List[str]]



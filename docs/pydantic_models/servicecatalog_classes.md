# Servicecatalog Classes

# AcceptPortfolioShareInputTypeDef

### PortfolioId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### PortfolioShareType
- **Type**: typing.Optional[typing.Literal['AWS_ORGANIZATIONS', 'AWS_SERVICECATALOG', 'IMPORTED']]


# AccessLevelFilterTypeDef

### Key
- **Type**: typing.Optional[typing.Literal['Account', 'Role', 'User']]

### Value
- **Type**: typing.Optional[str]


# AssociateBudgetWithResourceInputTypeDef

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociatePrincipalWithPortfolioInputTypeDef

### PortfolioId
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalARN
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalType
- **Type**: typing.Literal['IAM', 'IAM_PATTERN']
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]


# AssociateProductWithPortfolioInputTypeDef

### ProductId
- **Type**: <class 'str'>
- **Required**: Yes

### PortfolioId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### SourcePortfolioId
- **Type**: typing.Optional[str]


# AssociateServiceActionWithProvisioningArtifactInputTypeDef

### ProductId
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisioningArtifactId
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceActionId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### IdempotencyToken
- **Type**: typing.Optional[str]


# AssociateTagOptionWithResourceInputTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### TagOptionId
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchAssociateServiceActionWithProvisioningArtifactInputTypeDef

### ServiceActionAssociations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.servicecatalog_classes.ServiceActionAssociationTypeDef]
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]


# BatchAssociateServiceActionWithProvisioningArtifactOutputTypeDef

### FailedServiceActionAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.FailedServiceActionAssociationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchDisassociateServiceActionFromProvisioningArtifactInputTypeDef

### ServiceActionAssociations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.servicecatalog_classes.ServiceActionAssociationTypeDef]
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]


# BatchDisassociateServiceActionFromProvisioningArtifactOutputTypeDef

### FailedServiceActionAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.FailedServiceActionAssociationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BudgetDetailTypeDef

### BudgetName
- **Type**: typing.Optional[str]


# CloudWatchDashboardTypeDef

### Name
- **Type**: typing.Optional[str]


# CodeStarParametersTypeDef

### ConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Repository
- **Type**: <class 'str'>
- **Required**: Yes

### Branch
- **Type**: <class 'str'>
- **Required**: Yes

### ArtifactPath
- **Type**: <class 'str'>
- **Required**: Yes


# ConstraintDetailTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConstraintSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CopyProductInputTypeDef

### SourceProductArn
- **Type**: <class 'str'>
- **Required**: Yes

### IdempotencyToken
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### TargetProductId
- **Type**: typing.Optional[str]

### TargetProductName
- **Type**: typing.Optional[str]

### SourceProvisioningArtifactIdentifiers
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[typing.Literal['Id'], str]]]

### CopyOptions
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CopyTags']]]


# CopyProductOutputTypeDef

### CopyProductToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateConstraintOutputTypeDef

### ConstraintDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ConstraintDetailTypeDef'>
- **Required**: Yes

### ConstraintParameters
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'FAILED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePortfolioInputTypeDef

### DisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### ProviderName
- **Type**: <class 'str'>
- **Required**: Yes

### IdempotencyToken
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.servicecatalog_classes.TagTypeDef]]


# CreatePortfolioOutputTypeDef

### PortfolioDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.PortfolioDetailTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePortfolioShareInputTypeDef

### PortfolioId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### OrganizationNode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.OrganizationNodeTypeDef]

### ShareTagOptions
- **Type**: typing.Optional[bool]

### SharePrincipals
- **Type**: typing.Optional[bool]


# CreatePortfolioShareOutputTypeDef

### PortfolioShareToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateProductInputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Owner
- **Type**: <class 'str'>
- **Required**: Yes

### ProductType
- **Type**: typing.Literal['CLOUD_FORMATION_TEMPLATE', 'EXTERNAL', 'MARKETPLACE', 'TERRAFORM_CLOUD', 'TERRAFORM_OPEN_SOURCE']
- **Required**: Yes

### IdempotencyToken
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Distributor
- **Type**: typing.Optional[str]

### SupportDescription
- **Type**: typing.Optional[str]

### SupportEmail
- **Type**: typing.Optional[str]

### SupportUrl
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.servicecatalog_classes.TagTypeDef]]

### ProvisioningArtifactParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.ProvisioningArtifactPropertiesTypeDef]

### SourceConnection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.SourceConnectionTypeDef]


# CreateProductOutputTypeDef

### ProductViewDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ProductViewDetailTypeDef'>
- **Required**: Yes

### ProvisioningArtifactDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ProvisioningArtifactDetailTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateProvisionedProductPlanInputTypeDef

### PlanName
- **Type**: <class 'str'>
- **Required**: Yes

### PlanType
- **Type**: typing.Literal['CLOUDFORMATION']
- **Required**: Yes

### ProductId
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisionedProductName
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisioningArtifactId
- **Type**: <class 'str'>
- **Required**: Yes

### IdempotencyToken
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### NotificationArns
- **Type**: typing.Optional[typing.Sequence[str]]

### PathId
- **Type**: typing.Optional[str]

### ProvisioningParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.servicecatalog_classes.UpdateProvisioningParameterTypeDef]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.servicecatalog_classes.TagTypeDef]]


# CreateProvisionedProductPlanOutputTypeDef

### PlanName
- **Type**: <class 'str'>
- **Required**: Yes

### PlanId
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisionProductId
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisionedProductName
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisioningArtifactId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateProvisioningArtifactInputTypeDef

### ProductId
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ProvisioningArtifactPropertiesTypeDef'>
- **Required**: Yes

### IdempotencyToken
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]


# CreateProvisioningArtifactOutputTypeDef

### ProvisioningArtifactDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ProvisioningArtifactDetailTypeDef'>
- **Required**: Yes

### Info
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Status
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'FAILED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateServiceActionInputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DefinitionType
- **Type**: typing.Literal['SSM_AUTOMATION']
- **Required**: Yes

### Definition
- **Type**: typing.Mapping[typing.Literal['AssumeRole', 'Name', 'Parameters', 'Version'], str]
- **Required**: Yes

### IdempotencyToken
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### AcceptLanguage
- **Type**: typing.Optional[str]


# CreateServiceActionOutputTypeDef

### ServiceActionDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ServiceActionDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTagOptionInputTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# CreateTagOptionOutputTypeDef

### TagOptionDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.TagOptionDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteConstraintInputTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]


# DeletePortfolioInputTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]


# DeletePortfolioShareInputTypeDef

### PortfolioId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### OrganizationNode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.OrganizationNodeTypeDef]


# DeletePortfolioShareOutputTypeDef

### PortfolioShareToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteProductInputTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]


# DeleteProvisionedProductPlanInputTypeDef

### PlanId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### IgnoreErrors
- **Type**: typing.Optional[bool]


# DeleteProvisioningArtifactInputTypeDef

### ProductId
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisioningArtifactId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]


# DeleteServiceActionInputTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### IdempotencyToken
- **Type**: typing.Optional[str]


# DeleteTagOptionInputTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeConstraintInputTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]


# DescribeConstraintOutputTypeDef

### ConstraintDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ConstraintDetailTypeDef'>
- **Required**: Yes

### ConstraintParameters
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'FAILED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeCopyProductStatusInputTypeDef

### CopyProductToken
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]


# DescribeCopyProductStatusOutputTypeDef

### CopyProductStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### TargetProductId
- **Type**: <class 'str'>
- **Required**: Yes

### StatusDetail
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePortfolioInputTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]


# DescribePortfolioOutputTypeDef

### PortfolioDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.PortfolioDetailTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.TagTypeDef]
- **Required**: Yes

### TagOptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.TagOptionDetailTypeDef]
- **Required**: Yes

### Budgets
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.BudgetDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePortfolioShareStatusInputTypeDef

### PortfolioShareToken
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePortfolioShareStatusOutputTypeDef

### PortfolioShareToken
- **Type**: <class 'str'>
- **Required**: Yes

### PortfolioId
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationNodeValue
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETED', 'COMPLETED_WITH_ERRORS', 'ERROR', 'IN_PROGRESS', 'NOT_STARTED']
- **Required**: Yes

### ShareDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ShareDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePortfolioSharesOutputTypeDef

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### PortfolioShareDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.PortfolioShareDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeProductAsAdminInputTypeDef

### AcceptLanguage
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### SourcePortfolioId
- **Type**: typing.Optional[str]


# DescribeProductAsAdminOutputTypeDef

### ProductViewDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ProductViewDetailTypeDef'>
- **Required**: Yes

### ProvisioningArtifactSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.ProvisioningArtifactSummaryTypeDef]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.TagTypeDef]
- **Required**: Yes

### TagOptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.TagOptionDetailTypeDef]
- **Required**: Yes

### Budgets
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.BudgetDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeProductInputTypeDef

### AcceptLanguage
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# DescribeProductOutputTypeDef

### ProductViewSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ProductViewSummaryTypeDef'>
- **Required**: Yes

### ProvisioningArtifacts
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.ProvisioningArtifactTypeDef]
- **Required**: Yes

### Budgets
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.BudgetDetailTypeDef]
- **Required**: Yes

### LaunchPaths
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.LaunchPathTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeProductViewInputTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]


# DescribeProductViewOutputTypeDef

### ProductViewSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ProductViewSummaryTypeDef'>
- **Required**: Yes

### ProvisioningArtifacts
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.ProvisioningArtifactTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeProvisionedProductInputTypeDef

### AcceptLanguage
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# DescribeProvisionedProductOutputTypeDef

### ProvisionedProductDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ProvisionedProductDetailTypeDef'>
- **Required**: Yes

### CloudWatchDashboards
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.CloudWatchDashboardTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeProvisionedProductPlanInputTypeDef

### PlanId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]

### PageToken
- **Type**: typing.Optional[str]


# DescribeProvisionedProductPlanOutputTypeDef

### ProvisionedProductPlanDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ProvisionedProductPlanDetailsTypeDef'>
- **Required**: Yes

### ResourceChanges
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.ResourceChangeTypeDef]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeProvisioningArtifactInputTypeDef

### AcceptLanguage
- **Type**: typing.Optional[str]

### ProvisioningArtifactId
- **Type**: typing.Optional[str]

### ProductId
- **Type**: typing.Optional[str]

### ProvisioningArtifactName
- **Type**: typing.Optional[str]

### ProductName
- **Type**: typing.Optional[str]

### Verbose
- **Type**: typing.Optional[bool]

### IncludeProvisioningArtifactParameters
- **Type**: typing.Optional[bool]


# DescribeProvisioningArtifactOutputTypeDef

### ProvisioningArtifactDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ProvisioningArtifactDetailTypeDef'>
- **Required**: Yes

### Info
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Status
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'FAILED']
- **Required**: Yes

### ProvisioningArtifactParameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.ProvisioningArtifactParameterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeProvisioningParametersInputTypeDef

### AcceptLanguage
- **Type**: typing.Optional[str]

### ProductId
- **Type**: typing.Optional[str]

### ProductName
- **Type**: typing.Optional[str]

### ProvisioningArtifactId
- **Type**: typing.Optional[str]

### ProvisioningArtifactName
- **Type**: typing.Optional[str]

### PathId
- **Type**: typing.Optional[str]

### PathName
- **Type**: typing.Optional[str]


# DescribeProvisioningParametersOutputTypeDef

### ProvisioningArtifactParameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.ProvisioningArtifactParameterTypeDef]
- **Required**: Yes

### ConstraintSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.ConstraintSummaryTypeDef]
- **Required**: Yes

### UsageInstructions
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.UsageInstructionTypeDef]
- **Required**: Yes

### TagOptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.TagOptionSummaryTypeDef]
- **Required**: Yes

### ProvisioningArtifactPreferences
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ProvisioningArtifactPreferencesTypeDef'>
- **Required**: Yes

### ProvisioningArtifactOutputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.ProvisioningArtifactOutputTypeDef]
- **Required**: Yes

### ProvisioningArtifactOutputKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.ProvisioningArtifactOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRecordInputTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### PageToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# DescribeRecordOutputTypeDef

### RecordDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.RecordDetailTypeDef'>
- **Required**: Yes

### RecordOutputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.RecordOutputTypeDef]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeServiceActionExecutionParametersInputTypeDef

### ProvisionedProductId
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceActionId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]


# DescribeServiceActionExecutionParametersOutputTypeDef

### ServiceActionParameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.ExecutionParameterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeServiceActionInputTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]


# DescribeServiceActionOutputTypeDef

### ServiceActionDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ServiceActionDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTagOptionInputTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTagOptionOutputTypeDef

### TagOptionDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.TagOptionDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateBudgetFromResourceInputTypeDef

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociatePrincipalFromPortfolioInputTypeDef

### PortfolioId
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalARN
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### PrincipalType
- **Type**: typing.Optional[typing.Literal['IAM', 'IAM_PATTERN']]


# DisassociateProductFromPortfolioInputTypeDef

### ProductId
- **Type**: <class 'str'>
- **Required**: Yes

### PortfolioId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]


# DisassociateServiceActionFromProvisioningArtifactInputTypeDef

### ProductId
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisioningArtifactId
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceActionId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### IdempotencyToken
- **Type**: typing.Optional[str]


# DisassociateTagOptionFromResourceInputTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### TagOptionId
- **Type**: <class 'str'>
- **Required**: Yes


# EngineWorkflowResourceIdentifierTypeDef

### UniqueTag
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.UniqueTagResourceIdentifierTypeDef]


# ExecuteProvisionedProductPlanInputTypeDef

### PlanId
- **Type**: <class 'str'>
- **Required**: Yes

### IdempotencyToken
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]


# ExecuteProvisionedProductPlanOutputTypeDef

### RecordDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.RecordDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExecuteProvisionedProductServiceActionInputTypeDef

### ProvisionedProductId
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceActionId
- **Type**: <class 'str'>
- **Required**: Yes

### ExecuteToken
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]


# ExecuteProvisionedProductServiceActionOutputTypeDef

### RecordDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.RecordDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExecutionParameterTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FailedServiceActionAssociationTypeDef

### ServiceActionId
- **Type**: typing.Optional[str]

### ProductId
- **Type**: typing.Optional[str]

### ProvisioningArtifactId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[typing.Literal['DUPLICATE_RESOURCE', 'INTERNAL_FAILURE', 'INVALID_PARAMETER', 'LIMIT_EXCEEDED', 'RESOURCE_NOT_FOUND', 'THROTTLING']]

### ErrorMessage
- **Type**: typing.Optional[str]


# GetAWSOrganizationsAccessStatusOutputTypeDef

### AccessStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED', 'UNDER_CHANGE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetProvisionedProductOutputsInputTypeDef

### AcceptLanguage
- **Type**: typing.Optional[str]

### ProvisionedProductId
- **Type**: typing.Optional[str]

### ProvisionedProductName
- **Type**: typing.Optional[str]

### OutputKeys
- **Type**: typing.Optional[typing.Sequence[str]]

### PageSize
- **Type**: typing.Optional[int]

### PageToken
- **Type**: typing.Optional[str]


# GetProvisionedProductOutputsOutputTypeDef

### Outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.RecordOutputTypeDef]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImportAsProvisionedProductInputTypeDef

### ProductId
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisioningArtifactId
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisionedProductName
- **Type**: <class 'str'>
- **Required**: Yes

### PhysicalId
- **Type**: <class 'str'>
- **Required**: Yes

### IdempotencyToken
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]


# ImportAsProvisionedProductOutputTypeDef

### RecordDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.RecordDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LastSyncTypeDef

### LastSyncTime
- **Type**: typing.Optional[datetime.datetime]

### LastSyncStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'SUCCEEDED']]

### LastSyncStatusMessage
- **Type**: typing.Optional[str]

### LastSuccessfulSyncTime
- **Type**: typing.Optional[datetime.datetime]

### LastSuccessfulSyncProvisioningArtifactId
- **Type**: typing.Optional[str]


# LaunchPathSummaryTypeDef

### Id
- **Type**: typing.Optional[str]

### ConstraintSummaries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.ConstraintSummaryTypeDef]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.TagTypeDef]]

### Name
- **Type**: typing.Optional[str]


# LaunchPathTypeDef

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# ListAcceptedPortfolioSharesInputPaginateTypeDef

### AcceptLanguage
- **Type**: typing.Optional[str]

### PortfolioShareType
- **Type**: typing.Optional[typing.Literal['AWS_ORGANIZATIONS', 'AWS_SERVICECATALOG', 'IMPORTED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.PaginatorConfigTypeDef]


# ListAcceptedPortfolioSharesInputTypeDef

### AcceptLanguage
- **Type**: typing.Optional[str]

### PageToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]

### PortfolioShareType
- **Type**: typing.Optional[typing.Literal['AWS_ORGANIZATIONS', 'AWS_SERVICECATALOG', 'IMPORTED']]


# ListAcceptedPortfolioSharesOutputTypeDef

### PortfolioDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.PortfolioDetailTypeDef]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListBudgetsForResourceInputTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]

### PageToken
- **Type**: typing.Optional[str]


# ListBudgetsForResourceOutputTypeDef

### Budgets
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.BudgetDetailTypeDef]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListConstraintsForPortfolioInputPaginateTypeDef

### PortfolioId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### ProductId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.PaginatorConfigTypeDef]


# ListConstraintsForPortfolioInputTypeDef

### PortfolioId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### ProductId
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]

### PageToken
- **Type**: typing.Optional[str]


# ListConstraintsForPortfolioOutputTypeDef

### ConstraintDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.ConstraintDetailTypeDef]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLaunchPathsInputPaginateTypeDef

### ProductId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.PaginatorConfigTypeDef]


# ListLaunchPathsInputTypeDef

### ProductId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]

### PageToken
- **Type**: typing.Optional[str]


# ListLaunchPathsOutputTypeDef

### LaunchPathSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.LaunchPathSummaryTypeDef]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListOrganizationPortfolioAccessInputPaginateTypeDef

### PortfolioId
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationNodeType
- **Type**: typing.Literal['ACCOUNT', 'ORGANIZATION', 'ORGANIZATIONAL_UNIT']
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.PaginatorConfigTypeDef]


# ListOrganizationPortfolioAccessInputTypeDef

### PortfolioId
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationNodeType
- **Type**: typing.Literal['ACCOUNT', 'ORGANIZATION', 'ORGANIZATIONAL_UNIT']
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### PageToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListOrganizationPortfolioAccessOutputTypeDef

### OrganizationNodes
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.OrganizationNodeTypeDef]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPortfolioAccessInputTypeDef

### PortfolioId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### OrganizationParentId
- **Type**: typing.Optional[str]

### PageToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListPortfolioAccessOutputTypeDef

### AccountIds
- **Type**: typing.List[str]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPortfoliosForProductInputPaginateTypeDef

### ProductId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.PaginatorConfigTypeDef]


# ListPortfoliosForProductInputTypeDef

### ProductId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### PageToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListPortfoliosForProductOutputTypeDef

### PortfolioDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.PortfolioDetailTypeDef]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPortfoliosInputPaginateTypeDef

### AcceptLanguage
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.PaginatorConfigTypeDef]


# ListPortfoliosInputTypeDef

### AcceptLanguage
- **Type**: typing.Optional[str]

### PageToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListPortfoliosOutputTypeDef

### PortfolioDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.PortfolioDetailTypeDef]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPrincipalsForPortfolioInputPaginateTypeDef

### PortfolioId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.PaginatorConfigTypeDef]


# ListPrincipalsForPortfolioInputTypeDef

### PortfolioId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]

### PageToken
- **Type**: typing.Optional[str]


# ListPrincipalsForPortfolioOutputTypeDef

### Principals
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.PrincipalTypeDef]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListProvisionedProductPlansInputPaginateTypeDef

### AcceptLanguage
- **Type**: typing.Optional[str]

### ProvisionProductId
- **Type**: typing.Optional[str]

### AccessLevelFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.AccessLevelFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.PaginatorConfigTypeDef]


# ListProvisionedProductPlansInputTypeDef

### AcceptLanguage
- **Type**: typing.Optional[str]

### ProvisionProductId
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]

### PageToken
- **Type**: typing.Optional[str]

### AccessLevelFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.AccessLevelFilterTypeDef]


# ListProvisionedProductPlansOutputTypeDef

### ProvisionedProductPlans
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.ProvisionedProductPlanSummaryTypeDef]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListProvisioningArtifactsForServiceActionInputPaginateTypeDef

### ServiceActionId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.PaginatorConfigTypeDef]


# ListProvisioningArtifactsForServiceActionInputTypeDef

### ServiceActionId
- **Type**: <class 'str'>
- **Required**: Yes

### PageSize
- **Type**: typing.Optional[int]

### PageToken
- **Type**: typing.Optional[str]

### AcceptLanguage
- **Type**: typing.Optional[str]


# ListProvisioningArtifactsForServiceActionOutputTypeDef

### ProvisioningArtifactViews
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.ProvisioningArtifactViewTypeDef]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListProvisioningArtifactsInputTypeDef

### ProductId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]


# ListProvisioningArtifactsOutputTypeDef

### ProvisioningArtifactDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.ProvisioningArtifactDetailTypeDef]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRecordHistoryInputPaginateTypeDef

### AcceptLanguage
- **Type**: typing.Optional[str]

### AccessLevelFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.AccessLevelFilterTypeDef]

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.ListRecordHistorySearchFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.PaginatorConfigTypeDef]


# ListRecordHistoryInputTypeDef

### AcceptLanguage
- **Type**: typing.Optional[str]

### AccessLevelFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.AccessLevelFilterTypeDef]

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.ListRecordHistorySearchFilterTypeDef]

### PageSize
- **Type**: typing.Optional[int]

### PageToken
- **Type**: typing.Optional[str]


# ListRecordHistoryOutputTypeDef

### RecordDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.RecordDetailTypeDef]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRecordHistorySearchFilterTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# ListResourcesForTagOptionInputPaginateTypeDef

### TagOptionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.PaginatorConfigTypeDef]


# ListResourcesForTagOptionInputTypeDef

### TagOptionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]

### PageToken
- **Type**: typing.Optional[str]


# ListResourcesForTagOptionOutputTypeDef

### ResourceDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.ResourceDetailTypeDef]
- **Required**: Yes

### PageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListServiceActionsForProvisioningArtifactInputPaginateTypeDef

### ProductId
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisioningArtifactId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.PaginatorConfigTypeDef]


# ListServiceActionsForProvisioningArtifactInputTypeDef

### ProductId
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisioningArtifactId
- **Type**: <class 'str'>
- **Required**: Yes

### PageSize
- **Type**: typing.Optional[int]

### PageToken
- **Type**: typing.Optional[str]

### AcceptLanguage
- **Type**: typing.Optional[str]


# ListServiceActionsForProvisioningArtifactOutputTypeDef

### ServiceActionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.ServiceActionSummaryTypeDef]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListServiceActionsInputPaginateTypeDef

### AcceptLanguage
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.PaginatorConfigTypeDef]


# ListServiceActionsInputTypeDef

### AcceptLanguage
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]

### PageToken
- **Type**: typing.Optional[str]


# ListServiceActionsOutputTypeDef

### ServiceActionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.ServiceActionSummaryTypeDef]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListStackInstancesForProvisionedProductInputTypeDef

### ProvisionedProductId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### PageToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListStackInstancesForProvisionedProductOutputTypeDef

### StackInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.StackInstanceTypeDef]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagOptionsFiltersTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]

### Active
- **Type**: typing.Optional[bool]


# ListTagOptionsInputPaginateTypeDef

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.ListTagOptionsFiltersTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.PaginatorConfigTypeDef]


# ListTagOptionsInputTypeDef

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.ListTagOptionsFiltersTypeDef]

### PageSize
- **Type**: typing.Optional[int]

### PageToken
- **Type**: typing.Optional[str]


# ListTagOptionsOutputTypeDef

### TagOptionDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.TagOptionDetailTypeDef]
- **Required**: Yes

### PageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# NotifyProvisionProductEngineWorkflowResultInputTypeDef

### WorkflowToken
- **Type**: <class 'str'>
- **Required**: Yes

### RecordId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['FAILED', 'SUCCEEDED']
- **Required**: Yes

### IdempotencyToken
- **Type**: <class 'str'>
- **Required**: Yes

### FailureReason
- **Type**: typing.Optional[str]

### ResourceIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.EngineWorkflowResourceIdentifierTypeDef]

### Outputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.servicecatalog_classes.RecordOutputTypeDef]]


# NotifyTerminateProvisionedProductEngineWorkflowResultInputTypeDef

### WorkflowToken
- **Type**: <class 'str'>
- **Required**: Yes

### RecordId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['FAILED', 'SUCCEEDED']
- **Required**: Yes

### IdempotencyToken
- **Type**: <class 'str'>
- **Required**: Yes

### FailureReason
- **Type**: typing.Optional[str]


# NotifyUpdateProvisionedProductEngineWorkflowResultInputTypeDef

### WorkflowToken
- **Type**: <class 'str'>
- **Required**: Yes

### RecordId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['FAILED', 'SUCCEEDED']
- **Required**: Yes

### IdempotencyToken
- **Type**: <class 'str'>
- **Required**: Yes

### FailureReason
- **Type**: typing.Optional[str]

### Outputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.servicecatalog_classes.RecordOutputTypeDef]]


# OrganizationNodeTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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

### AllowedPattern
- **Type**: typing.Optional[str]

### ConstraintDescription
- **Type**: typing.Optional[str]

### MaxLength
- **Type**: typing.Optional[str]

### MinLength
- **Type**: typing.Optional[str]

### MaxValue
- **Type**: typing.Optional[str]

### MinValue
- **Type**: typing.Optional[str]


# PortfolioDetailTypeDef

### Id
- **Type**: typing.Optional[str]

### ARN
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### ProviderName
- **Type**: typing.Optional[str]


# PortfolioShareDetailTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PrincipalTypeDef

### PrincipalARN
- **Type**: typing.Optional[str]

### PrincipalType
- **Type**: typing.Optional[typing.Literal['IAM', 'IAM_PATTERN']]


# ProductViewAggregationValueTypeDef

### Value
- **Type**: typing.Optional[str]

### ApproximateCount
- **Type**: typing.Optional[int]


# ProductViewDetailTypeDef

### ProductViewSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.ProductViewSummaryTypeDef]

### Status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'FAILED']]

### ProductARN
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### SourceConnection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.SourceConnectionDetailTypeDef]


# ProductViewSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProvisionProductInputTypeDef

### ProvisionedProductName
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisionToken
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### ProductId
- **Type**: typing.Optional[str]

### ProductName
- **Type**: typing.Optional[str]

### ProvisioningArtifactId
- **Type**: typing.Optional[str]

### ProvisioningArtifactName
- **Type**: typing.Optional[str]

### PathId
- **Type**: typing.Optional[str]

### PathName
- **Type**: typing.Optional[str]

### ProvisioningParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.servicecatalog_classes.ProvisioningParameterTypeDef]]

### ProvisioningPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.ProvisioningPreferencesTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.servicecatalog_classes.TagTypeDef]]

### NotificationArns
- **Type**: typing.Optional[typing.Sequence[str]]


# ProvisionProductOutputTypeDef

### RecordDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.RecordDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ProvisionedProductAttributeTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProvisionedProductDetailTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProvisionedProductPlanDetailsTypeDef

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### PathId
- **Type**: typing.Optional[str]

### ProductId
- **Type**: typing.Optional[str]

### PlanName
- **Type**: typing.Optional[str]

### PlanId
- **Type**: typing.Optional[str]

### ProvisionProductId
- **Type**: typing.Optional[str]

### ProvisionProductName
- **Type**: typing.Optional[str]

### PlanType
- **Type**: typing.Optional[typing.Literal['CLOUDFORMATION']]

### ProvisioningArtifactId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_SUCCESS', 'EXECUTE_FAILED', 'EXECUTE_IN_PROGRESS', 'EXECUTE_SUCCESS']]

### UpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### NotificationArns
- **Type**: typing.Optional[typing.List[str]]

### ProvisioningParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.UpdateProvisioningParameterTypeDef]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.TagTypeDef]]

### StatusMessage
- **Type**: typing.Optional[str]


# ProvisionedProductPlanSummaryTypeDef

### PlanName
- **Type**: typing.Optional[str]

### PlanId
- **Type**: typing.Optional[str]

### ProvisionProductId
- **Type**: typing.Optional[str]

### ProvisionProductName
- **Type**: typing.Optional[str]

### PlanType
- **Type**: typing.Optional[typing.Literal['CLOUDFORMATION']]

### ProvisioningArtifactId
- **Type**: typing.Optional[str]


# ProvisioningArtifactDetailTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProvisioningArtifactOutputTypeDef

### Key
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# ProvisioningArtifactParameterTypeDef

### ParameterKey
- **Type**: typing.Optional[str]

### DefaultValue
- **Type**: typing.Optional[str]

### ParameterType
- **Type**: typing.Optional[str]

### IsNoEcho
- **Type**: typing.Optional[bool]

### Description
- **Type**: typing.Optional[str]

### ParameterConstraints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.ParameterConstraintsTypeDef]


# ProvisioningArtifactPreferencesTypeDef

### StackSetAccounts
- **Type**: typing.Optional[typing.List[str]]

### StackSetRegions
- **Type**: typing.Optional[typing.List[str]]


# ProvisioningArtifactPropertiesTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProvisioningArtifactSummaryTypeDef

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### ProvisioningArtifactMetadata
- **Type**: typing.Optional[typing.Dict[str, str]]


# ProvisioningArtifactTypeDef

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### Guidance
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'DEPRECATED']]


# ProvisioningArtifactViewTypeDef

### ProductViewSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.ProductViewSummaryTypeDef]

### ProvisioningArtifact
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.ProvisioningArtifactTypeDef]


# ProvisioningParameterTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# ProvisioningPreferencesTypeDef

### StackSetAccounts
- **Type**: typing.Optional[typing.Sequence[str]]

### StackSetRegions
- **Type**: typing.Optional[typing.Sequence[str]]

### StackSetFailureToleranceCount
- **Type**: typing.Optional[int]

### StackSetFailureTolerancePercentage
- **Type**: typing.Optional[int]

### StackSetMaxConcurrencyCount
- **Type**: typing.Optional[int]

### StackSetMaxConcurrencyPercentage
- **Type**: typing.Optional[int]


# RecordDetailTypeDef

### RecordId
- **Type**: typing.Optional[str]

### ProvisionedProductName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CREATED', 'FAILED', 'IN_PROGRESS', 'IN_PROGRESS_IN_ERROR', 'SUCCEEDED']]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### ProvisionedProductType
- **Type**: typing.Optional[str]

### RecordType
- **Type**: typing.Optional[str]

### ProvisionedProductId
- **Type**: typing.Optional[str]

### ProductId
- **Type**: typing.Optional[str]

### ProvisioningArtifactId
- **Type**: typing.Optional[str]

### PathId
- **Type**: typing.Optional[str]

### RecordErrors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.RecordErrorTypeDef]]

### RecordTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.RecordTagTypeDef]]

### LaunchRoleArn
- **Type**: typing.Optional[str]


# RecordErrorTypeDef

### Code
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# RecordOutputTypeDef

### OutputKey
- **Type**: typing.Optional[str]

### OutputValue
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# RecordTagTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# RejectPortfolioShareInputTypeDef

### PortfolioId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### PortfolioShareType
- **Type**: typing.Optional[typing.Literal['AWS_ORGANIZATIONS', 'AWS_SERVICECATALOG', 'IMPORTED']]


# ResourceChangeDetailTypeDef

### Target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.ResourceTargetDefinitionTypeDef]

### Evaluation
- **Type**: typing.Optional[typing.Literal['DYNAMIC', 'STATIC']]

### CausingEntity
- **Type**: typing.Optional[str]


# ResourceChangeTypeDef

### Action
- **Type**: typing.Optional[typing.Literal['ADD', 'MODIFY', 'REMOVE']]

### LogicalResourceId
- **Type**: typing.Optional[str]

### PhysicalResourceId
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### Replacement
- **Type**: typing.Optional[typing.Literal['CONDITIONAL', 'FALSE', 'TRUE']]

### Scope
- **Type**: typing.Optional[typing.List[typing.Literal['CREATIONPOLICY', 'DELETIONPOLICY', 'METADATA', 'PROPERTIES', 'TAGS', 'UPDATEPOLICY']]]

### Details
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.ResourceChangeDetailTypeDef]]


# ResourceDetailTypeDef

### Id
- **Type**: typing.Optional[str]

### ARN
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]


# ResourceTargetDefinitionTypeDef

### Attribute
- **Type**: typing.Optional[typing.Literal['CREATIONPOLICY', 'DELETIONPOLICY', 'METADATA', 'PROPERTIES', 'TAGS', 'UPDATEPOLICY']]

### Name
- **Type**: typing.Optional[str]

### RequiresRecreation
- **Type**: typing.Optional[typing.Literal['ALWAYS', 'CONDITIONALLY', 'NEVER']]


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


# ScanProvisionedProductsInputPaginateTypeDef

### AcceptLanguage
- **Type**: typing.Optional[str]

### AccessLevelFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.AccessLevelFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.PaginatorConfigTypeDef]


# ScanProvisionedProductsInputTypeDef

### AcceptLanguage
- **Type**: typing.Optional[str]

### AccessLevelFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.AccessLevelFilterTypeDef]

### PageSize
- **Type**: typing.Optional[int]

### PageToken
- **Type**: typing.Optional[str]


# ScanProvisionedProductsOutputTypeDef

### ProvisionedProducts
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.ProvisionedProductDetailTypeDef]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SearchProductsAsAdminInputPaginateTypeDef

### AcceptLanguage
- **Type**: typing.Optional[str]

### PortfolioId
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Mapping[typing.Literal['FullTextSearch', 'Owner', 'ProductType', 'SourceProductId'], typing.Sequence[str]]]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationDate', 'Title', 'VersionCount']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### ProductSource
- **Type**: typing.Optional[typing.Literal['ACCOUNT']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.PaginatorConfigTypeDef]


# SearchProductsAsAdminInputTypeDef

### AcceptLanguage
- **Type**: typing.Optional[str]

### PortfolioId
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Mapping[typing.Literal['FullTextSearch', 'Owner', 'ProductType', 'SourceProductId'], typing.Sequence[str]]]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationDate', 'Title', 'VersionCount']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PageToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]

### ProductSource
- **Type**: typing.Optional[typing.Literal['ACCOUNT']]


# SearchProductsAsAdminOutputTypeDef

### ProductViewDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.ProductViewDetailTypeDef]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SearchProductsInputTypeDef

### AcceptLanguage
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Mapping[typing.Literal['FullTextSearch', 'Owner', 'ProductType', 'SourceProductId'], typing.Sequence[str]]]

### PageSize
- **Type**: typing.Optional[int]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationDate', 'Title', 'VersionCount']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PageToken
- **Type**: typing.Optional[str]


# SearchProductsOutputTypeDef

### ProductViewSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.ProductViewSummaryTypeDef]
- **Required**: Yes

### ProductViewAggregations
- **Type**: typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.ProductViewAggregationValueTypeDef]]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SearchProvisionedProductsInputTypeDef

### AcceptLanguage
- **Type**: typing.Optional[str]

### AccessLevelFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.AccessLevelFilterTypeDef]

### Filters
- **Type**: typing.Optional[typing.Mapping[typing.Literal['SearchQuery'], typing.Sequence[str]]]

### SortBy
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PageSize
- **Type**: typing.Optional[int]

### PageToken
- **Type**: typing.Optional[str]


# SearchProvisionedProductsOutputTypeDef

### ProvisionedProducts
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.ProvisionedProductAttributeTypeDef]
- **Required**: Yes

### TotalResultsCount
- **Type**: <class 'int'>
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ServiceActionAssociationTypeDef

### ServiceActionId
- **Type**: <class 'str'>
- **Required**: Yes

### ProductId
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisioningArtifactId
- **Type**: <class 'str'>
- **Required**: Yes


# ServiceActionDetailTypeDef

### ServiceActionSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.ServiceActionSummaryTypeDef]

### Definition
- **Type**: typing.Optional[typing.Dict[typing.Literal['AssumeRole', 'Name', 'Parameters', 'Version'], str]]


# ServiceActionSummaryTypeDef

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DefinitionType
- **Type**: typing.Optional[typing.Literal['SSM_AUTOMATION']]


# ShareDetailsTypeDef

### SuccessfulShares
- **Type**: typing.Optional[typing.List[str]]

### ShareErrors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.ShareErrorTypeDef]]


# ShareErrorTypeDef

### Accounts
- **Type**: typing.Optional[typing.List[str]]

### Message
- **Type**: typing.Optional[str]

### Error
- **Type**: typing.Optional[str]


# SourceConnectionDetailTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SourceConnectionParametersTypeDef

### CodeStar
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.CodeStarParametersTypeDef]


# SourceConnectionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StackInstanceTypeDef

### Account
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### StackInstanceStatus
- **Type**: typing.Optional[typing.Literal['CURRENT', 'INOPERABLE', 'OUTDATED']]


# TagOptionDetailTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]

### Active
- **Type**: typing.Optional[bool]

### Id
- **Type**: typing.Optional[str]

### Owner
- **Type**: typing.Optional[str]


# TagOptionSummaryTypeDef

### Key
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TerminateProvisionedProductInputTypeDef

### TerminateToken
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisionedProductName
- **Type**: typing.Optional[str]

### ProvisionedProductId
- **Type**: typing.Optional[str]

### IgnoreErrors
- **Type**: typing.Optional[bool]

### AcceptLanguage
- **Type**: typing.Optional[str]

### RetainPhysicalResources
- **Type**: typing.Optional[bool]


# TerminateProvisionedProductOutputTypeDef

### RecordDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.RecordDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UniqueTagResourceIdentifierTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# UpdateConstraintInputTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[str]


# UpdateConstraintOutputTypeDef

### ConstraintDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ConstraintDetailTypeDef'>
- **Required**: Yes

### ConstraintParameters
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'FAILED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePortfolioInputTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ProviderName
- **Type**: typing.Optional[str]

### AddTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.servicecatalog_classes.TagTypeDef]]

### RemoveTags
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdatePortfolioOutputTypeDef

### PortfolioDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.PortfolioDetailTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePortfolioShareInputTypeDef

### PortfolioId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### OrganizationNode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.OrganizationNodeTypeDef]

### ShareTagOptions
- **Type**: typing.Optional[bool]

### SharePrincipals
- **Type**: typing.Optional[bool]


# UpdatePortfolioShareOutputTypeDef

### PortfolioShareToken
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETED', 'COMPLETED_WITH_ERRORS', 'ERROR', 'IN_PROGRESS', 'NOT_STARTED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateProductInputTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Owner
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Distributor
- **Type**: typing.Optional[str]

### SupportDescription
- **Type**: typing.Optional[str]

### SupportEmail
- **Type**: typing.Optional[str]

### SupportUrl
- **Type**: typing.Optional[str]

### AddTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.servicecatalog_classes.TagTypeDef]]

### RemoveTags
- **Type**: typing.Optional[typing.Sequence[str]]

### SourceConnection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.SourceConnectionTypeDef]


# UpdateProductOutputTypeDef

### ProductViewDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ProductViewDetailTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateProvisionedProductInputTypeDef

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### ProvisionedProductName
- **Type**: typing.Optional[str]

### ProvisionedProductId
- **Type**: typing.Optional[str]

### ProductId
- **Type**: typing.Optional[str]

### ProductName
- **Type**: typing.Optional[str]

### ProvisioningArtifactId
- **Type**: typing.Optional[str]

### ProvisioningArtifactName
- **Type**: typing.Optional[str]

### PathId
- **Type**: typing.Optional[str]

### PathName
- **Type**: typing.Optional[str]

### ProvisioningParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.servicecatalog_classes.UpdateProvisioningParameterTypeDef]]

### ProvisioningPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_classes.UpdateProvisioningPreferencesTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.servicecatalog_classes.TagTypeDef]]


# UpdateProvisionedProductOutputTypeDef

### RecordDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.RecordDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateProvisionedProductPropertiesInputTypeDef

### ProvisionedProductId
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisionedProductProperties
- **Type**: typing.Mapping[typing.Literal['LAUNCH_ROLE', 'OWNER'], str]
- **Required**: Yes

### IdempotencyToken
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]


# UpdateProvisionedProductPropertiesOutputTypeDef

### ProvisionedProductId
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisionedProductProperties
- **Type**: typing.Dict[typing.Literal['LAUNCH_ROLE', 'OWNER'], str]
- **Required**: Yes

### RecordId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CREATED', 'FAILED', 'IN_PROGRESS', 'IN_PROGRESS_IN_ERROR', 'SUCCEEDED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateProvisioningArtifactInputTypeDef

### ProductId
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisioningArtifactId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Active
- **Type**: typing.Optional[bool]

### Guidance
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'DEPRECATED']]


# UpdateProvisioningArtifactOutputTypeDef

### ProvisioningArtifactDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ProvisioningArtifactDetailTypeDef'>
- **Required**: Yes

### Info
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Status
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'FAILED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateProvisioningParameterTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]

### UsePreviousValue
- **Type**: typing.Optional[bool]


# UpdateProvisioningPreferencesTypeDef

### StackSetAccounts
- **Type**: typing.Optional[typing.Sequence[str]]

### StackSetRegions
- **Type**: typing.Optional[typing.Sequence[str]]

### StackSetFailureToleranceCount
- **Type**: typing.Optional[int]

### StackSetFailureTolerancePercentage
- **Type**: typing.Optional[int]

### StackSetMaxConcurrencyCount
- **Type**: typing.Optional[int]

### StackSetMaxConcurrencyPercentage
- **Type**: typing.Optional[int]

### StackSetOperationType
- **Type**: typing.Optional[typing.Literal['CREATE', 'DELETE', 'UPDATE']]


# UpdateServiceActionInputTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Definition
- **Type**: typing.Optional[typing.Mapping[typing.Literal['AssumeRole', 'Name', 'Parameters', 'Version'], str]]

### Description
- **Type**: typing.Optional[str]

### AcceptLanguage
- **Type**: typing.Optional[str]


# UpdateServiceActionOutputTypeDef

### ServiceActionDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ServiceActionDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTagOptionInputTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]

### Active
- **Type**: typing.Optional[bool]


# UpdateTagOptionOutputTypeDef

### TagOptionDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.TagOptionDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UsageInstructionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">


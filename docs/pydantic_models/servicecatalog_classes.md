# Servicecatalog Classes

# AcceptPortfolioShareInput

### PortfolioId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### PortfolioShareType
- **Type**: typing.Optional[typing.Literal['AWS_ORGANIZATIONS', 'AWS_SERVICECATALOG', 'IMPORTED']]


# AccessLevelFilter

### Key
- **Type**: typing.Optional[typing.Literal['Account', 'Role', 'User']]

### Value
- **Type**: typing.Optional[str]


# AssociateBudgetWithResourceInput

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociatePrincipalWithPortfolioInput

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


# AssociateProductWithPortfolioInput

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


# AssociateServiceActionWithProvisioningArtifactInput

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


# AssociateTagOptionWithResourceInput

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### TagOptionId
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchAssociateServiceActionWithProvisioningArtifactInput

### ServiceActionAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ServiceActionAssociation]
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]


# BatchAssociateServiceActionWithProvisioningArtifactOutput

### FailedServiceActionAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.FailedServiceActionAssociation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDisassociateServiceActionFromProvisioningArtifactInput

### ServiceActionAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ServiceActionAssociation]
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]


# BatchDisassociateServiceActionFromProvisioningArtifactOutput

### FailedServiceActionAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.FailedServiceActionAssociation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# BudgetDetail

### BudgetName
- **Type**: typing.Optional[str]


# CloudWatchDashboard

### Name
- **Type**: typing.Optional[str]


# CodeStarParameters

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


# ConstraintDetail

### ConstraintId
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Owner
- **Type**: typing.Optional[str]

### ProductId
- **Type**: typing.Optional[str]

### PortfolioId
- **Type**: typing.Optional[str]


# ConstraintSummary

### Type
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# CopyProductInput

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
- **Type**: typing.Optional[typing.List[typing.Dict[typing.Literal['Id'], str]]]

### CopyOptions
- **Type**: typing.Optional[typing.List[typing.Literal['CopyTags']]]


# CopyProductOutput

### CopyProductToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# CreateConstraintInput

### PortfolioId
- **Type**: <class 'str'>
- **Required**: Yes

### ProductId
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: <class 'str'>
- **Required**: Yes

### IdempotencyToken
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# CreateConstraintOutput

### ConstraintDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ConstraintDetail'>
- **Required**: Yes

### ConstraintParameters
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'FAILED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePortfolioInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.Tag]]


# CreatePortfolioOutput

### PortfolioDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.PortfolioDetail'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePortfolioShareInput

### PortfolioId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### OrganizationNode
- **Type**: <class 'NoneType'>

### ShareTagOptions
- **Type**: typing.Optional[bool]

### SharePrincipals
- **Type**: typing.Optional[bool]


# CreatePortfolioShareOutput

### PortfolioShareToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# CreateProductInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.Tag]]

### ProvisioningArtifactParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ProvisioningArtifactProperties]

### SourceConnection
- **Type**: <class 'NoneType'>


# CreateProductOutput

### ProductViewDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ProductViewDetail'>
- **Required**: Yes

### ProvisioningArtifactDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ProvisioningArtifactDetail'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# CreateProvisionedProductPlanInput

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
- **Type**: typing.Optional[typing.List[str]]

### PathId
- **Type**: typing.Optional[str]

### ProvisioningParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.UpdateProvisioningParameter]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.Tag]]


# CreateProvisionedProductPlanOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# CreateProvisioningArtifactInput

### ProductId
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ProvisioningArtifactProperties'>
- **Required**: Yes

### IdempotencyToken
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]


# CreateProvisioningArtifactOutput

### ProvisioningArtifactDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ProvisioningArtifactDetail'>
- **Required**: Yes

### Info
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Status
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'FAILED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# CreateServiceActionInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DefinitionType
- **Type**: typing.Literal['SSM_AUTOMATION']
- **Required**: Yes

### Definition
- **Type**: typing.Dict[typing.Literal['AssumeRole', 'Name', 'Parameters', 'Version'], str]
- **Required**: Yes

### IdempotencyToken
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### AcceptLanguage
- **Type**: typing.Optional[str]


# CreateServiceActionOutput

### ServiceActionDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ServiceActionDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTagOptionInput

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# CreateTagOptionOutput

### TagOptionDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.TagOptionDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteConstraintInput

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]


# DeletePortfolioInput

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]


# DeletePortfolioShareInput

### PortfolioId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### OrganizationNode
- **Type**: <class 'NoneType'>


# DeletePortfolioShareOutput

### PortfolioShareToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteProductInput

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]


# DeleteProvisionedProductPlanInput

### PlanId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### IgnoreErrors
- **Type**: typing.Optional[bool]


# DeleteProvisioningArtifactInput

### ProductId
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisioningArtifactId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]


# DeleteServiceActionInput

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### IdempotencyToken
- **Type**: typing.Optional[str]


# DeleteTagOptionInput

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeConstraintInput

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]


# DescribeConstraintOutput

### ConstraintDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ConstraintDetail'>
- **Required**: Yes

### ConstraintParameters
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'FAILED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeCopyProductStatusInput

### CopyProductToken
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]


# DescribeCopyProductStatusOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePortfolioInput

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]


# DescribePortfolioOutput

### PortfolioDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.PortfolioDetail'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.Tag]
- **Required**: Yes

### TagOptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.TagOptionDetail]
- **Required**: Yes

### Budgets
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.BudgetDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePortfolioShareStatusInput

### PortfolioShareToken
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePortfolioShareStatusOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ShareDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePortfolioSharesInput

### PortfolioId
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['ACCOUNT', 'ORGANIZATION', 'ORGANIZATIONAL_UNIT', 'ORGANIZATION_MEMBER_ACCOUNT']
- **Required**: Yes

### PageToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# DescribePortfolioSharesOutput

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### PortfolioShareDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.PortfolioShareDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeProductAsAdminInput

### AcceptLanguage
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### SourcePortfolioId
- **Type**: typing.Optional[str]


# DescribeProductAsAdminOutput

### ProductViewDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ProductViewDetail'>
- **Required**: Yes

### ProvisioningArtifactSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ProvisioningArtifactSummary]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.Tag]
- **Required**: Yes

### TagOptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.TagOptionDetail]
- **Required**: Yes

### Budgets
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.BudgetDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeProductInput

### AcceptLanguage
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# DescribeProductOutput

### ProductViewSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ProductViewSummary'>
- **Required**: Yes

### ProvisioningArtifacts
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ProvisioningArtifact]
- **Required**: Yes

### Budgets
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.BudgetDetail]
- **Required**: Yes

### LaunchPaths
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.LaunchPath]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeProductViewInput

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]


# DescribeProductViewOutput

### ProductViewSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ProductViewSummary'>
- **Required**: Yes

### ProvisioningArtifacts
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ProvisioningArtifact]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeProvisionedProductInput

### AcceptLanguage
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# DescribeProvisionedProductOutput

### ProvisionedProductDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ProvisionedProductDetail'>
- **Required**: Yes

### CloudWatchDashboards
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.CloudWatchDashboard]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeProvisionedProductPlanInput

### PlanId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]

### PageToken
- **Type**: typing.Optional[str]


# DescribeProvisionedProductPlanOutput

### ProvisionedProductPlanDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ProvisionedProductPlanDetails'>
- **Required**: Yes

### ResourceChanges
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResourceChange]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeProvisioningArtifactInput

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


# DescribeProvisioningArtifactOutput

### ProvisioningArtifactDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ProvisioningArtifactDetail'>
- **Required**: Yes

### Info
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Status
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'FAILED']
- **Required**: Yes

### ProvisioningArtifactParameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ProvisioningArtifactParameter]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeProvisioningParametersInput

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


# DescribeProvisioningParametersOutput

### ProvisioningArtifactParameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ProvisioningArtifactParameter]
- **Required**: Yes

### ConstraintSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ConstraintSummary]
- **Required**: Yes

### UsageInstructions
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.UsageInstruction]
- **Required**: Yes

### TagOptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.TagOptionSummary]
- **Required**: Yes

### ProvisioningArtifactPreferences
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ProvisioningArtifactPreferences'>
- **Required**: Yes

### ProvisioningArtifactOutputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ProvisioningArtifactOutput]
- **Required**: Yes

### ProvisioningArtifactOutputKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ProvisioningArtifactOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRecordInput

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### PageToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# DescribeRecordOutput

### RecordDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.RecordDetail'>
- **Required**: Yes

### RecordOutputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.RecordOutput]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeServiceActionExecutionParametersInput

### ProvisionedProductId
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceActionId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]


# DescribeServiceActionExecutionParametersOutput

### ServiceActionParameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ExecutionParameter]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeServiceActionInput

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]


# DescribeServiceActionOutput

### ServiceActionDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ServiceActionDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTagOptionInput

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTagOptionOutput

### TagOptionDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.TagOptionDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateBudgetFromResourceInput

### BudgetName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociatePrincipalFromPortfolioInput

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


# DisassociateProductFromPortfolioInput

### ProductId
- **Type**: <class 'str'>
- **Required**: Yes

### PortfolioId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]


# DisassociateServiceActionFromProvisioningArtifactInput

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


# DisassociateTagOptionFromResourceInput

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### TagOptionId
- **Type**: <class 'str'>
- **Required**: Yes


# EngineWorkflowResourceIdentifier

### UniqueTag
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.UniqueTagResourceIdentifier]


# ExecuteProvisionedProductPlanInput

### PlanId
- **Type**: <class 'str'>
- **Required**: Yes

### IdempotencyToken
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]


# ExecuteProvisionedProductPlanOutput

### RecordDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.RecordDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# ExecuteProvisionedProductServiceActionInput

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
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]


# ExecuteProvisionedProductServiceActionOutput

### RecordDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.RecordDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# ExecutionParameter

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### DefaultValues
- **Type**: typing.Optional[typing.List[str]]


# FailedServiceActionAssociation

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


# GetAWSOrganizationsAccessStatusOutput

### AccessStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED', 'UNDER_CHANGE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# GetProvisionedProductOutputsInput

### AcceptLanguage
- **Type**: typing.Optional[str]

### ProvisionedProductId
- **Type**: typing.Optional[str]

### ProvisionedProductName
- **Type**: typing.Optional[str]

### OutputKeys
- **Type**: typing.Optional[typing.List[str]]

### PageSize
- **Type**: typing.Optional[int]

### PageToken
- **Type**: typing.Optional[str]


# GetProvisionedProductOutputsOutput

### Outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.RecordOutput]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# ImportAsProvisionedProductInput

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


# ImportAsProvisionedProductOutput

### RecordDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.RecordDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# LastSync

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


# LaunchPath

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# LaunchPathSummary

### Id
- **Type**: typing.Optional[str]

### ConstraintSummaries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ConstraintSummary]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.Tag]]

### Name
- **Type**: typing.Optional[str]


# ListAcceptedPortfolioSharesInput

### AcceptLanguage
- **Type**: typing.Optional[str]

### PageToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]

### PortfolioShareType
- **Type**: typing.Optional[typing.Literal['AWS_ORGANIZATIONS', 'AWS_SERVICECATALOG', 'IMPORTED']]


# ListAcceptedPortfolioSharesInputPaginate

### AcceptLanguage
- **Type**: typing.Optional[str]

### PortfolioShareType
- **Type**: typing.Optional[typing.Literal['AWS_ORGANIZATIONS', 'AWS_SERVICECATALOG', 'IMPORTED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.PaginatorConfig]


# ListAcceptedPortfolioSharesOutput

### PortfolioDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.PortfolioDetail]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# ListBudgetsForResourceInput

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]

### PageToken
- **Type**: typing.Optional[str]


# ListBudgetsForResourceOutput

### Budgets
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.BudgetDetail]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# ListConstraintsForPortfolioInput

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


# ListConstraintsForPortfolioInputPaginate

### PortfolioId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### ProductId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.PaginatorConfig]


# ListConstraintsForPortfolioOutput

### ConstraintDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ConstraintDetail]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# ListLaunchPathsInput

### ProductId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]

### PageToken
- **Type**: typing.Optional[str]


# ListLaunchPathsInputPaginate

### ProductId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.PaginatorConfig]


# ListLaunchPathsOutput

### LaunchPathSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.LaunchPathSummary]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# ListOrganizationPortfolioAccessInput

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


# ListOrganizationPortfolioAccessInputPaginate

### PortfolioId
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationNodeType
- **Type**: typing.Literal['ACCOUNT', 'ORGANIZATION', 'ORGANIZATIONAL_UNIT']
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.PaginatorConfig]


# ListOrganizationPortfolioAccessOutput

### OrganizationNodes
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.OrganizationNode]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# ListPortfolioAccessInput

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


# ListPortfolioAccessOutput

### AccountIds
- **Type**: typing.List[str]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# ListPortfoliosForProductInput

### ProductId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### PageToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListPortfoliosForProductInputPaginate

### ProductId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.PaginatorConfig]


# ListPortfoliosForProductOutput

### PortfolioDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.PortfolioDetail]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# ListPortfoliosInput

### AcceptLanguage
- **Type**: typing.Optional[str]

### PageToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListPortfoliosInputPaginate

### AcceptLanguage
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.PaginatorConfig]


# ListPortfoliosOutput

### PortfolioDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.PortfolioDetail]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# ListPrincipalsForPortfolioInput

### PortfolioId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]

### PageToken
- **Type**: typing.Optional[str]


# ListPrincipalsForPortfolioInputPaginate

### PortfolioId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.PaginatorConfig]


# ListPrincipalsForPortfolioOutput

### Principals
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.Principal]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# ListProvisionedProductPlansInput

### AcceptLanguage
- **Type**: typing.Optional[str]

### ProvisionProductId
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]

### PageToken
- **Type**: typing.Optional[str]

### AccessLevelFilter
- **Type**: <class 'NoneType'>


# ListProvisionedProductPlansInputPaginate

### AcceptLanguage
- **Type**: typing.Optional[str]

### ProvisionProductId
- **Type**: typing.Optional[str]

### AccessLevelFilter
- **Type**: <class 'NoneType'>

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.PaginatorConfig]


# ListProvisionedProductPlansOutput

### ProvisionedProductPlans
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ProvisionedProductPlanSummary]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# ListProvisioningArtifactsForServiceActionInput

### ServiceActionId
- **Type**: <class 'str'>
- **Required**: Yes

### PageSize
- **Type**: typing.Optional[int]

### PageToken
- **Type**: typing.Optional[str]

### AcceptLanguage
- **Type**: typing.Optional[str]


# ListProvisioningArtifactsForServiceActionInputPaginate

### ServiceActionId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.PaginatorConfig]


# ListProvisioningArtifactsForServiceActionOutput

### ProvisioningArtifactViews
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ProvisioningArtifactView]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# ListProvisioningArtifactsInput

### ProductId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]


# ListProvisioningArtifactsOutput

### ProvisioningArtifactDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ProvisioningArtifactDetail]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# ListRecordHistoryInput

### AcceptLanguage
- **Type**: typing.Optional[str]

### AccessLevelFilter
- **Type**: <class 'NoneType'>

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ListRecordHistorySearchFilter]

### PageSize
- **Type**: typing.Optional[int]

### PageToken
- **Type**: typing.Optional[str]


# ListRecordHistoryInputPaginate

### AcceptLanguage
- **Type**: typing.Optional[str]

### AccessLevelFilter
- **Type**: <class 'NoneType'>

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ListRecordHistorySearchFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.PaginatorConfig]


# ListRecordHistoryOutput

### RecordDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.RecordDetail]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# ListRecordHistorySearchFilter

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# ListResourcesForTagOptionInput

### TagOptionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]

### PageToken
- **Type**: typing.Optional[str]


# ListResourcesForTagOptionInputPaginate

### TagOptionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.PaginatorConfig]


# ListResourcesForTagOptionOutput

### ResourceDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResourceDetail]
- **Required**: Yes

### PageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# ListServiceActionsForProvisioningArtifactInput

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


# ListServiceActionsForProvisioningArtifactInputPaginate

### ProductId
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisioningArtifactId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.PaginatorConfig]


# ListServiceActionsForProvisioningArtifactOutput

### ServiceActionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ServiceActionSummary]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# ListServiceActionsInput

### AcceptLanguage
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]

### PageToken
- **Type**: typing.Optional[str]


# ListServiceActionsInputPaginate

### AcceptLanguage
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.PaginatorConfig]


# ListServiceActionsOutput

### ServiceActionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ServiceActionSummary]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# ListStackInstancesForProvisionedProductInput

### ProvisionedProductId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### PageToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListStackInstancesForProvisionedProductOutput

### StackInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.StackInstance]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# ListTagOptionsFilters

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]

### Active
- **Type**: typing.Optional[bool]


# ListTagOptionsInput

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ListTagOptionsFilters]

### PageSize
- **Type**: typing.Optional[int]

### PageToken
- **Type**: typing.Optional[str]


# ListTagOptionsInputPaginate

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ListTagOptionsFilters]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.PaginatorConfig]


# ListTagOptionsOutput

### TagOptionDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.TagOptionDetail]
- **Required**: Yes

### PageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# NotifyProvisionProductEngineWorkflowResultInput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.EngineWorkflowResourceIdentifier]

### Outputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.RecordOutput]]


# NotifyTerminateProvisionedProductEngineWorkflowResultInput

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


# NotifyUpdateProvisionedProductEngineWorkflowResultInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.RecordOutput]]


# OrganizationNode

### Type
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'ORGANIZATION', 'ORGANIZATIONAL_UNIT']]

### Value
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParameterConstraints

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


# PortfolioDetail

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


# PortfolioShareDetail

### PrincipalId
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'ORGANIZATION', 'ORGANIZATIONAL_UNIT', 'ORGANIZATION_MEMBER_ACCOUNT']]

### Accepted
- **Type**: typing.Optional[bool]

### ShareTagOptions
- **Type**: typing.Optional[bool]

### SharePrincipals
- **Type**: typing.Optional[bool]


# Principal

### PrincipalARN
- **Type**: typing.Optional[str]

### PrincipalType
- **Type**: typing.Optional[typing.Literal['IAM', 'IAM_PATTERN']]


# ProductViewAggregationValue

### Value
- **Type**: typing.Optional[str]

### ApproximateCount
- **Type**: typing.Optional[int]


# ProductViewDetail

### ProductViewSummary
- **Type**: <class 'NoneType'>

### Status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'FAILED']]

### ProductARN
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### SourceConnection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.SourceConnectionDetail]


# ProductViewSummary

### Id
- **Type**: typing.Optional[str]

### ProductId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Owner
- **Type**: typing.Optional[str]

### ShortDescription
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['CLOUD_FORMATION_TEMPLATE', 'EXTERNAL', 'MARKETPLACE', 'TERRAFORM_CLOUD', 'TERRAFORM_OPEN_SOURCE']]

### Distributor
- **Type**: typing.Optional[str]

### HasDefaultPath
- **Type**: typing.Optional[bool]

### SupportEmail
- **Type**: typing.Optional[str]

### SupportDescription
- **Type**: typing.Optional[str]

### SupportUrl
- **Type**: typing.Optional[str]


# ProvisionProductInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ProvisioningParameter]]

### ProvisioningPreferences
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.Tag]]

### NotificationArns
- **Type**: typing.Optional[typing.List[str]]


# ProvisionProductOutput

### RecordDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.RecordDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# ProvisionedProductAttribute

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'ERROR', 'PLAN_IN_PROGRESS', 'TAINTED', 'UNDER_CHANGE']]

### StatusMessage
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### IdempotencyToken
- **Type**: typing.Optional[str]

### LastRecordId
- **Type**: typing.Optional[str]

### LastProvisioningRecordId
- **Type**: typing.Optional[str]

### LastSuccessfulProvisioningRecordId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.Tag]]

### PhysicalId
- **Type**: typing.Optional[str]

### ProductId
- **Type**: typing.Optional[str]

### ProductName
- **Type**: typing.Optional[str]

### ProvisioningArtifactId
- **Type**: typing.Optional[str]

### ProvisioningArtifactName
- **Type**: typing.Optional[str]

### UserArn
- **Type**: typing.Optional[str]

### UserArnSession
- **Type**: typing.Optional[str]


# ProvisionedProductDetail

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'ERROR', 'PLAN_IN_PROGRESS', 'TAINTED', 'UNDER_CHANGE']]

### StatusMessage
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### IdempotencyToken
- **Type**: typing.Optional[str]

### LastRecordId
- **Type**: typing.Optional[str]

### LastProvisioningRecordId
- **Type**: typing.Optional[str]

### LastSuccessfulProvisioningRecordId
- **Type**: typing.Optional[str]

### ProductId
- **Type**: typing.Optional[str]

### ProvisioningArtifactId
- **Type**: typing.Optional[str]

### LaunchRoleArn
- **Type**: typing.Optional[str]


# ProvisionedProductPlanDetails

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.UpdateProvisioningParameter]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.Tag]]

### StatusMessage
- **Type**: typing.Optional[str]


# ProvisionedProductPlanSummary

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


# ProvisioningArtifact

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


# ProvisioningArtifactDetail

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['CLOUD_FORMATION_TEMPLATE', 'EXTERNAL', 'MARKETPLACE_AMI', 'MARKETPLACE_CAR', 'TERRAFORM_CLOUD', 'TERRAFORM_OPEN_SOURCE']]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### Active
- **Type**: typing.Optional[bool]

### Guidance
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'DEPRECATED']]

### SourceRevision
- **Type**: typing.Optional[str]


# ProvisioningArtifactOutput

### Key
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# ProvisioningArtifactParameter

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
- **Type**: <class 'NoneType'>


# ProvisioningArtifactPreferences

### StackSetAccounts
- **Type**: typing.Optional[typing.List[str]]

### StackSetRegions
- **Type**: typing.Optional[typing.List[str]]


# ProvisioningArtifactProperties

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Info
- **Type**: typing.Optional[typing.Dict[str, str]]

### Type
- **Type**: typing.Optional[typing.Literal['CLOUD_FORMATION_TEMPLATE', 'EXTERNAL', 'MARKETPLACE_AMI', 'MARKETPLACE_CAR', 'TERRAFORM_CLOUD', 'TERRAFORM_OPEN_SOURCE']]

### DisableTemplateValidation
- **Type**: typing.Optional[bool]


# ProvisioningArtifactSummary

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


# ProvisioningArtifactView

### ProductViewSummary
- **Type**: <class 'NoneType'>

### ProvisioningArtifact
- **Type**: <class 'NoneType'>


# ProvisioningParameter

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# ProvisioningPreferences

### StackSetAccounts
- **Type**: typing.Optional[typing.List[str]]

### StackSetRegions
- **Type**: typing.Optional[typing.List[str]]

### StackSetFailureToleranceCount
- **Type**: typing.Optional[int]

### StackSetFailureTolerancePercentage
- **Type**: typing.Optional[int]

### StackSetMaxConcurrencyCount
- **Type**: typing.Optional[int]

### StackSetMaxConcurrencyPercentage
- **Type**: typing.Optional[int]


# RecordDetail

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.RecordError]]

### RecordTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.RecordTag]]

### LaunchRoleArn
- **Type**: typing.Optional[str]


# RecordError

### Code
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# RecordOutput

### OutputKey
- **Type**: typing.Optional[str]

### OutputValue
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# RecordTag

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# RejectPortfolioShareInput

### PortfolioId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### PortfolioShareType
- **Type**: typing.Optional[typing.Literal['AWS_ORGANIZATIONS', 'AWS_SERVICECATALOG', 'IMPORTED']]


# ResourceChange

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResourceChangeDetail]]


# ResourceChangeDetail

### Target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResourceTargetDefinition]

### Evaluation
- **Type**: typing.Optional[typing.Literal['DYNAMIC', 'STATIC']]

### CausingEntity
- **Type**: typing.Optional[str]


# ResourceDetail

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


# ResourceTargetDefinition

### Attribute
- **Type**: typing.Optional[typing.Literal['CREATIONPOLICY', 'DELETIONPOLICY', 'METADATA', 'PROPERTIES', 'TAGS', 'UPDATEPOLICY']]

### Name
- **Type**: typing.Optional[str]

### RequiresRecreation
- **Type**: typing.Optional[typing.Literal['ALWAYS', 'CONDITIONALLY', 'NEVER']]


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


# ScanProvisionedProductsInput

### AcceptLanguage
- **Type**: typing.Optional[str]

### AccessLevelFilter
- **Type**: <class 'NoneType'>

### PageSize
- **Type**: typing.Optional[int]

### PageToken
- **Type**: typing.Optional[str]


# ScanProvisionedProductsInputPaginate

### AcceptLanguage
- **Type**: typing.Optional[str]

### AccessLevelFilter
- **Type**: <class 'NoneType'>

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.PaginatorConfig]


# ScanProvisionedProductsOutput

### ProvisionedProducts
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ProvisionedProductDetail]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# SearchProductsAsAdminInput

### AcceptLanguage
- **Type**: typing.Optional[str]

### PortfolioId
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Dict[typing.Literal['FullTextSearch', 'Owner', 'ProductType', 'SourceProductId'], typing.List[str]]]

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


# SearchProductsAsAdminInputPaginate

### AcceptLanguage
- **Type**: typing.Optional[str]

### PortfolioId
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Dict[typing.Literal['FullTextSearch', 'Owner', 'ProductType', 'SourceProductId'], typing.List[str]]]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationDate', 'Title', 'VersionCount']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### ProductSource
- **Type**: typing.Optional[typing.Literal['ACCOUNT']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.PaginatorConfig]


# SearchProductsAsAdminOutput

### ProductViewDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ProductViewDetail]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# SearchProductsInput

### AcceptLanguage
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Dict[typing.Literal['FullTextSearch', 'Owner', 'ProductType', 'SourceProductId'], typing.List[str]]]

### PageSize
- **Type**: typing.Optional[int]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationDate', 'Title', 'VersionCount']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PageToken
- **Type**: typing.Optional[str]


# SearchProductsOutput

### ProductViewSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ProductViewSummary]
- **Required**: Yes

### ProductViewAggregations
- **Type**: typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ProductViewAggregationValue]]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# SearchProvisionedProductsInput

### AcceptLanguage
- **Type**: typing.Optional[str]

### AccessLevelFilter
- **Type**: <class 'NoneType'>

### Filters
- **Type**: typing.Optional[typing.Dict[typing.Literal['SearchQuery'], typing.List[str]]]

### SortBy
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PageSize
- **Type**: typing.Optional[int]

### PageToken
- **Type**: typing.Optional[str]


# SearchProvisionedProductsOutput

### ProvisionedProducts
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ProvisionedProductAttribute]
- **Required**: Yes

### TotalResultsCount
- **Type**: <class 'int'>
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# ServiceActionAssociation

### ServiceActionId
- **Type**: <class 'str'>
- **Required**: Yes

### ProductId
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisioningArtifactId
- **Type**: <class 'str'>
- **Required**: Yes


# ServiceActionDetail

### ServiceActionSummary
- **Type**: <class 'NoneType'>

### Definition
- **Type**: typing.Optional[typing.Dict[typing.Literal['AssumeRole', 'Name', 'Parameters', 'Version'], str]]


# ServiceActionSummary

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DefinitionType
- **Type**: typing.Optional[typing.Literal['SSM_AUTOMATION']]


# ShareDetails

### SuccessfulShares
- **Type**: typing.Optional[typing.List[str]]

### ShareErrors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ShareError]]


# ShareError

### Accounts
- **Type**: typing.Optional[typing.List[str]]

### Message
- **Type**: typing.Optional[str]

### Error
- **Type**: typing.Optional[str]


# SourceConnection

### ConnectionParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.SourceConnectionParameters'>
- **Required**: Yes

### Type
- **Type**: typing.Optional[typing.Literal['CODESTAR']]


# SourceConnectionDetail

### Type
- **Type**: typing.Optional[typing.Literal['CODESTAR']]

### ConnectionParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.SourceConnectionParameters]

### LastSync
- **Type**: <class 'NoneType'>


# SourceConnectionParameters

### CodeStar
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.CodeStarParameters]


# StackInstance

### Account
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### StackInstanceStatus
- **Type**: typing.Optional[typing.Literal['CURRENT', 'INOPERABLE', 'OUTDATED']]


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagOptionDetail

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


# TagOptionSummary

### Key
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]


# TerminateProvisionedProductInput

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


# TerminateProvisionedProductOutput

### RecordDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.RecordDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# UniqueTagResourceIdentifier

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# UpdateConstraintInput

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[str]


# UpdateConstraintOutput

### ConstraintDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ConstraintDetail'>
- **Required**: Yes

### ConstraintParameters
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'FAILED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePortfolioInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.Tag]]

### RemoveTags
- **Type**: typing.Optional[typing.List[str]]


# UpdatePortfolioOutput

### PortfolioDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.PortfolioDetail'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePortfolioShareInput

### PortfolioId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### OrganizationNode
- **Type**: <class 'NoneType'>

### ShareTagOptions
- **Type**: typing.Optional[bool]

### SharePrincipals
- **Type**: typing.Optional[bool]


# UpdatePortfolioShareOutput

### PortfolioShareToken
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETED', 'COMPLETED_WITH_ERRORS', 'ERROR', 'IN_PROGRESS', 'NOT_STARTED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateProductInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.Tag]]

### RemoveTags
- **Type**: typing.Optional[typing.List[str]]

### SourceConnection
- **Type**: <class 'NoneType'>


# UpdateProductOutput

### ProductViewDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ProductViewDetail'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateProvisionedProductInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.UpdateProvisioningParameter]]

### ProvisioningPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.UpdateProvisioningPreferences]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.Tag]]


# UpdateProvisionedProductOutput

### RecordDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.RecordDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateProvisionedProductPropertiesInput

### ProvisionedProductId
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisionedProductProperties
- **Type**: typing.Dict[typing.Literal['LAUNCH_ROLE', 'OWNER'], str]
- **Required**: Yes

### IdempotencyToken
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptLanguage
- **Type**: typing.Optional[str]


# UpdateProvisionedProductPropertiesOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateProvisioningArtifactInput

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


# UpdateProvisioningArtifactOutput

### ProvisioningArtifactDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ProvisioningArtifactDetail'>
- **Required**: Yes

### Info
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Status
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'FAILED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateProvisioningParameter

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]

### UsePreviousValue
- **Type**: typing.Optional[bool]


# UpdateProvisioningPreferences

### StackSetAccounts
- **Type**: typing.Optional[typing.List[str]]

### StackSetRegions
- **Type**: typing.Optional[typing.List[str]]

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


# UpdateServiceActionInput

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Definition
- **Type**: typing.Optional[typing.Dict[typing.Literal['AssumeRole', 'Name', 'Parameters', 'Version'], str]]

### Description
- **Type**: typing.Optional[str]

### AcceptLanguage
- **Type**: typing.Optional[str]


# UpdateServiceActionOutput

### ServiceActionDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ServiceActionDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTagOptionInput

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]

### Active
- **Type**: typing.Optional[bool]


# UpdateTagOptionOutput

### TagOptionDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.TagOptionDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_classes.ResponseMetadata'>
- **Required**: Yes


# UsageInstruction

### Type
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]



from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.servicecatalog.servicecatalog_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AcceptPortfolioShareInput(BaseValidatorModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    PortfolioShareType: Optional[PortfolioShareTypeType] = None


class AccessLevelFilter(BaseValidatorModel):
    Key: Optional[AccessLevelFilterKeyType] = None
    Value: Optional[str] = None


class AssociateBudgetWithResourceInput(BaseValidatorModel):
    BudgetName: str
    ResourceId: str


class AssociatePrincipalWithPortfolioInput(BaseValidatorModel):
    PortfolioId: str
    PrincipalARN: str
    PrincipalType: PrincipalTypeType
    AcceptLanguage: Optional[str] = None


class AssociateProductWithPortfolioInput(BaseValidatorModel):
    ProductId: str
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    SourcePortfolioId: Optional[str] = None


class AssociateServiceActionWithProvisioningArtifactInput(BaseValidatorModel):
    ProductId: str
    ProvisioningArtifactId: str
    ServiceActionId: str
    AcceptLanguage: Optional[str] = None
    IdempotencyToken: Optional[str] = None


class AssociateTagOptionWithResourceInput(BaseValidatorModel):
    ResourceId: str
    TagOptionId: str


class ServiceActionAssociation(BaseValidatorModel):
    ServiceActionId: str
    ProductId: str
    ProvisioningArtifactId: str


class FailedServiceActionAssociation(BaseValidatorModel):
    ServiceActionId: Optional[str] = None
    ProductId: Optional[str] = None
    ProvisioningArtifactId: Optional[str] = None
    ErrorCode: Optional[ServiceActionAssociationErrorCodeType] = None
    ErrorMessage: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BudgetDetail(BaseValidatorModel):
    BudgetName: Optional[str] = None


class CloudWatchDashboard(BaseValidatorModel):
    Name: Optional[str] = None


class CodeStarParameters(BaseValidatorModel):
    ConnectionArn: str
    Repository: str
    Branch: str
    ArtifactPath: str


class ConstraintDetail(BaseValidatorModel):
    ConstraintId: Optional[str] = None
    Type: Optional[str] = None
    Description: Optional[str] = None
    Owner: Optional[str] = None
    ProductId: Optional[str] = None
    PortfolioId: Optional[str] = None


class ConstraintSummary(BaseValidatorModel):
    Type: Optional[str] = None
    Description: Optional[str] = None


# This class is the input for the 'copy_product' function.
class CopyProductInput(BaseValidatorModel):
    SourceProductArn: str
    IdempotencyToken: str
    AcceptLanguage: Optional[str] = None
    TargetProductId: Optional[str] = None
    TargetProductName: Optional[str] = None
    SourceProvisioningArtifactIdentifiers: Optional[List[Dict[Literal['Id'], str]]] = None
    CopyOptions: Optional[List[Literal['CopyTags']]] = None


# This class is the input for the 'create_constraint' function.
class CreateConstraintInput(BaseValidatorModel):
    PortfolioId: str
    ProductId: str
    Parameters: str
    Type: str
    IdempotencyToken: str
    AcceptLanguage: Optional[str] = None
    Description: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class PortfolioDetail(BaseValidatorModel):
    Id: Optional[str] = None
    ARN: Optional[str] = None
    DisplayName: Optional[str] = None
    Description: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    ProviderName: Optional[str] = None


class OrganizationNode(BaseValidatorModel):
    Type: Optional[OrganizationNodeTypeType] = None
    Value: Optional[str] = None


class ProvisioningArtifactProperties(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    Info: Optional[Dict[str, str]] = None
    Type: Optional[ProvisioningArtifactTypeType] = None
    DisableTemplateValidation: Optional[bool] = None


class ProvisioningArtifactDetail(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Type: Optional[ProvisioningArtifactTypeType] = None
    CreatedTime: Optional[datetime] = None
    Active: Optional[bool] = None
    Guidance: Optional[ProvisioningArtifactGuidanceType] = None
    SourceRevision: Optional[str] = None


class UpdateProvisioningParameter(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    UsePreviousValue: Optional[bool] = None


# This class is the input for the 'create_service_action' function.
class CreateServiceActionInput(BaseValidatorModel):
    Name: str
    DefinitionType: Literal['SSM_AUTOMATION']
    Definition: Dict[ServiceActionDefinitionKeyType, str]
    IdempotencyToken: str
    Description: Optional[str] = None
    AcceptLanguage: Optional[str] = None


# This class is the input for the 'create_tag_option' function.
class CreateTagOptionInput(BaseValidatorModel):
    Key: str
    Value: str


class TagOptionDetail(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    Active: Optional[bool] = None
    Id: Optional[str] = None
    Owner: Optional[str] = None


class DeleteConstraintInput(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None


class DeletePortfolioInput(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None


class DeleteProductInput(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None


class DeleteProvisionedProductPlanInput(BaseValidatorModel):
    PlanId: str
    AcceptLanguage: Optional[str] = None
    IgnoreErrors: Optional[bool] = None


class DeleteProvisioningArtifactInput(BaseValidatorModel):
    ProductId: str
    ProvisioningArtifactId: str
    AcceptLanguage: Optional[str] = None


class DeleteServiceActionInput(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None
    IdempotencyToken: Optional[str] = None


class DeleteTagOptionInput(BaseValidatorModel):
    Id: str


# This class is the input for the 'describe_constraint' function.
class DescribeConstraintInput(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None


# This class is the input for the 'describe_copy_product_status' function.
class DescribeCopyProductStatusInput(BaseValidatorModel):
    CopyProductToken: str
    AcceptLanguage: Optional[str] = None


# This class is the input for the 'describe_portfolio' function.
class DescribePortfolioInput(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None


# This class is the input for the 'describe_portfolio_share_status' function.
class DescribePortfolioShareStatusInput(BaseValidatorModel):
    PortfolioShareToken: str


# This class is the input for the 'describe_portfolio_shares' function.
class DescribePortfolioSharesInput(BaseValidatorModel):
    PortfolioId: str
    Type: DescribePortfolioShareTypeType
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None


class PortfolioShareDetail(BaseValidatorModel):
    PrincipalId: Optional[str] = None
    Type: Optional[DescribePortfolioShareTypeType] = None
    Accepted: Optional[bool] = None
    ShareTagOptions: Optional[bool] = None
    SharePrincipals: Optional[bool] = None


# This class is the input for the 'describe_product_as_admin' function.
class DescribeProductAsAdminInput(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    SourcePortfolioId: Optional[str] = None


class ProvisioningArtifactSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    ProvisioningArtifactMetadata: Optional[Dict[str, str]] = None


# This class is the input for the 'describe_product' function.
class DescribeProductInput(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None


class LaunchPath(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None


class ProductViewSummary(BaseValidatorModel):
    Id: Optional[str] = None
    ProductId: Optional[str] = None
    Name: Optional[str] = None
    Owner: Optional[str] = None
    ShortDescription: Optional[str] = None
    Type: Optional[ProductTypeType] = None
    Distributor: Optional[str] = None
    HasDefaultPath: Optional[bool] = None
    SupportEmail: Optional[str] = None
    SupportDescription: Optional[str] = None
    SupportUrl: Optional[str] = None


class ProvisioningArtifact(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    Guidance: Optional[ProvisioningArtifactGuidanceType] = None


# This class is the input for the 'describe_product_view' function.
class DescribeProductViewInput(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None


# This class is the input for the 'describe_provisioned_product' function.
class DescribeProvisionedProductInput(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None


class ProvisionedProductDetail(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    Type: Optional[str] = None
    Id: Optional[str] = None
    Status: Optional[ProvisionedProductStatusType] = None
    StatusMessage: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    IdempotencyToken: Optional[str] = None
    LastRecordId: Optional[str] = None
    LastProvisioningRecordId: Optional[str] = None
    LastSuccessfulProvisioningRecordId: Optional[str] = None
    ProductId: Optional[str] = None
    ProvisioningArtifactId: Optional[str] = None
    LaunchRoleArn: Optional[str] = None


# This class is the input for the 'describe_provisioned_product_plan' function.
class DescribeProvisionedProductPlanInput(BaseValidatorModel):
    PlanId: str
    AcceptLanguage: Optional[str] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None


# This class is the input for the 'describe_provisioning_artifact' function.
class DescribeProvisioningArtifactInput(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    ProvisioningArtifactId: Optional[str] = None
    ProductId: Optional[str] = None
    ProvisioningArtifactName: Optional[str] = None
    ProductName: Optional[str] = None
    Verbose: Optional[bool] = None
    IncludeProvisioningArtifactParameters: Optional[bool] = None


# This class is the input for the 'describe_provisioning_parameters' function.
class DescribeProvisioningParametersInput(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    ProductId: Optional[str] = None
    ProductName: Optional[str] = None
    ProvisioningArtifactId: Optional[str] = None
    ProvisioningArtifactName: Optional[str] = None
    PathId: Optional[str] = None
    PathName: Optional[str] = None


class ProvisioningArtifactOutput(BaseValidatorModel):
    Key: Optional[str] = None
    Description: Optional[str] = None


class ProvisioningArtifactPreferences(BaseValidatorModel):
    StackSetAccounts: Optional[List[str]] = None
    StackSetRegions: Optional[List[str]] = None


class TagOptionSummary(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[List[str]] = None


class UsageInstruction(BaseValidatorModel):
    Type: Optional[str] = None
    Value: Optional[str] = None


# This class is the input for the 'describe_record' function.
class DescribeRecordInput(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None


class RecordOutput(BaseValidatorModel):
    OutputKey: Optional[str] = None
    OutputValue: Optional[str] = None
    Description: Optional[str] = None


# This class is the input for the 'describe_service_action_execution_parameters' function.
class DescribeServiceActionExecutionParametersInput(BaseValidatorModel):
    ProvisionedProductId: str
    ServiceActionId: str
    AcceptLanguage: Optional[str] = None


class ExecutionParameter(BaseValidatorModel):
    Name: Optional[str] = None
    Type: Optional[str] = None
    DefaultValues: Optional[List[str]] = None


# This class is the input for the 'describe_service_action' function.
class DescribeServiceActionInput(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None


# This class is the input for the 'describe_tag_option' function.
class DescribeTagOptionInput(BaseValidatorModel):
    Id: str


class DisassociateBudgetFromResourceInput(BaseValidatorModel):
    BudgetName: str
    ResourceId: str


class DisassociatePrincipalFromPortfolioInput(BaseValidatorModel):
    PortfolioId: str
    PrincipalARN: str
    AcceptLanguage: Optional[str] = None
    PrincipalType: Optional[PrincipalTypeType] = None


class DisassociateProductFromPortfolioInput(BaseValidatorModel):
    ProductId: str
    PortfolioId: str
    AcceptLanguage: Optional[str] = None


class DisassociateServiceActionFromProvisioningArtifactInput(BaseValidatorModel):
    ProductId: str
    ProvisioningArtifactId: str
    ServiceActionId: str
    AcceptLanguage: Optional[str] = None
    IdempotencyToken: Optional[str] = None


class DisassociateTagOptionFromResourceInput(BaseValidatorModel):
    ResourceId: str
    TagOptionId: str


class UniqueTagResourceIdentifier(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


# This class is the input for the 'execute_provisioned_product_plan' function.
class ExecuteProvisionedProductPlanInput(BaseValidatorModel):
    PlanId: str
    IdempotencyToken: str
    AcceptLanguage: Optional[str] = None


# This class is the input for the 'execute_provisioned_product_service_action' function.
class ExecuteProvisionedProductServiceActionInput(BaseValidatorModel):
    ProvisionedProductId: str
    ServiceActionId: str
    ExecuteToken: str
    AcceptLanguage: Optional[str] = None
    Parameters: Optional[Dict[str, List[str]]] = None


# This class is the input for the 'get_provisioned_product_outputs' function.
class GetProvisionedProductOutputsInput(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    ProvisionedProductId: Optional[str] = None
    ProvisionedProductName: Optional[str] = None
    OutputKeys: Optional[List[str]] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None


# This class is the input for the 'import_as_provisioned_product' function.
class ImportAsProvisionedProductInput(BaseValidatorModel):
    ProductId: str
    ProvisioningArtifactId: str
    ProvisionedProductName: str
    PhysicalId: str
    IdempotencyToken: str
    AcceptLanguage: Optional[str] = None


class LastSync(BaseValidatorModel):
    LastSyncTime: Optional[datetime] = None
    LastSyncStatus: Optional[LastSyncStatusType] = None
    LastSyncStatusMessage: Optional[str] = None
    LastSuccessfulSyncTime: Optional[datetime] = None
    LastSuccessfulSyncProvisioningArtifactId: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_accepted_portfolio_shares' function.
class ListAcceptedPortfolioSharesInput(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None
    PortfolioShareType: Optional[PortfolioShareTypeType] = None


# This class is the input for the 'list_budgets_for_resource' function.
class ListBudgetsForResourceInput(BaseValidatorModel):
    ResourceId: str
    AcceptLanguage: Optional[str] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None


# This class is the input for the 'list_constraints_for_portfolio' function.
class ListConstraintsForPortfolioInput(BaseValidatorModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    ProductId: Optional[str] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None


# This class is the input for the 'list_launch_paths' function.
class ListLaunchPathsInput(BaseValidatorModel):
    ProductId: str
    AcceptLanguage: Optional[str] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None


# This class is the input for the 'list_organization_portfolio_access' function.
class ListOrganizationPortfolioAccessInput(BaseValidatorModel):
    PortfolioId: str
    OrganizationNodeType: OrganizationNodeTypeType
    AcceptLanguage: Optional[str] = None
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None


# This class is the input for the 'list_portfolio_access' function.
class ListPortfolioAccessInput(BaseValidatorModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    OrganizationParentId: Optional[str] = None
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None


# This class is the input for the 'list_portfolios_for_product' function.
class ListPortfoliosForProductInput(BaseValidatorModel):
    ProductId: str
    AcceptLanguage: Optional[str] = None
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None


# This class is the input for the 'list_portfolios' function.
class ListPortfoliosInput(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None


# This class is the input for the 'list_principals_for_portfolio' function.
class ListPrincipalsForPortfolioInput(BaseValidatorModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None


class Principal(BaseValidatorModel):
    PrincipalARN: Optional[str] = None
    PrincipalType: Optional[PrincipalTypeType] = None


class ProvisionedProductPlanSummary(BaseValidatorModel):
    PlanName: Optional[str] = None
    PlanId: Optional[str] = None
    ProvisionProductId: Optional[str] = None
    ProvisionProductName: Optional[str] = None
    PlanType: Optional[Literal['CLOUDFORMATION']] = None
    ProvisioningArtifactId: Optional[str] = None


# This class is the input for the 'list_provisioning_artifacts_for_service_action' function.
class ListProvisioningArtifactsForServiceActionInput(BaseValidatorModel):
    ServiceActionId: str
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None
    AcceptLanguage: Optional[str] = None


# This class is the input for the 'list_provisioning_artifacts' function.
class ListProvisioningArtifactsInput(BaseValidatorModel):
    ProductId: str
    AcceptLanguage: Optional[str] = None


class ListRecordHistorySearchFilter(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


# This class is the input for the 'list_resources_for_tag_option' function.
class ListResourcesForTagOptionInput(BaseValidatorModel):
    TagOptionId: str
    ResourceType: Optional[str] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None


class ResourceDetail(BaseValidatorModel):
    Id: Optional[str] = None
    ARN: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    CreatedTime: Optional[datetime] = None


# This class is the input for the 'list_service_actions_for_provisioning_artifact' function.
class ListServiceActionsForProvisioningArtifactInput(BaseValidatorModel):
    ProductId: str
    ProvisioningArtifactId: str
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None
    AcceptLanguage: Optional[str] = None


class ServiceActionSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    DefinitionType: Optional[Literal['SSM_AUTOMATION']] = None


# This class is the input for the 'list_service_actions' function.
class ListServiceActionsInput(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None


# This class is the input for the 'list_stack_instances_for_provisioned_product' function.
class ListStackInstancesForProvisionedProductInput(BaseValidatorModel):
    ProvisionedProductId: str
    AcceptLanguage: Optional[str] = None
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None


class StackInstance(BaseValidatorModel):
    Account: Optional[str] = None
    Region: Optional[str] = None
    StackInstanceStatus: Optional[StackInstanceStatusType] = None


class ListTagOptionsFilters(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    Active: Optional[bool] = None


class NotifyTerminateProvisionedProductEngineWorkflowResultInput(BaseValidatorModel):
    WorkflowToken: str
    RecordId: str
    Status: EngineWorkflowStatusType
    IdempotencyToken: str
    FailureReason: Optional[str] = None


class ParameterConstraints(BaseValidatorModel):
    AllowedValues: Optional[List[str]] = None
    AllowedPattern: Optional[str] = None
    ConstraintDescription: Optional[str] = None
    MaxLength: Optional[str] = None
    MinLength: Optional[str] = None
    MaxValue: Optional[str] = None
    MinValue: Optional[str] = None


class ProductViewAggregationValue(BaseValidatorModel):
    Value: Optional[str] = None
    ApproximateCount: Optional[int] = None


class ProvisioningParameter(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class ProvisioningPreferences(BaseValidatorModel):
    StackSetAccounts: Optional[List[str]] = None
    StackSetRegions: Optional[List[str]] = None
    StackSetFailureToleranceCount: Optional[int] = None
    StackSetFailureTolerancePercentage: Optional[int] = None
    StackSetMaxConcurrencyCount: Optional[int] = None
    StackSetMaxConcurrencyPercentage: Optional[int] = None


class RecordError(BaseValidatorModel):
    Code: Optional[str] = None
    Description: Optional[str] = None


class RecordTag(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class RejectPortfolioShareInput(BaseValidatorModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    PortfolioShareType: Optional[PortfolioShareTypeType] = None


class ResourceTargetDefinition(BaseValidatorModel):
    Attribute: Optional[ResourceAttributeType] = None
    Name: Optional[str] = None
    RequiresRecreation: Optional[RequiresRecreationType] = None


# This class is the input for the 'search_products_as_admin' function.
class SearchProductsAsAdminInput(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    PortfolioId: Optional[str] = None
    Filters: Optional[Dict[ProductViewFilterByType, List[str]]] = None
    SortBy: Optional[ProductViewSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None
    ProductSource: Optional[Literal['ACCOUNT']] = None


# This class is the input for the 'search_products' function.
class SearchProductsInput(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    Filters: Optional[Dict[ProductViewFilterByType, List[str]]] = None
    PageSize: Optional[int] = None
    SortBy: Optional[ProductViewSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    PageToken: Optional[str] = None


class ShareError(BaseValidatorModel):
    Accounts: Optional[List[str]] = None
    Message: Optional[str] = None
    Error: Optional[str] = None


# This class is the input for the 'terminate_provisioned_product' function.
class TerminateProvisionedProductInput(BaseValidatorModel):
    TerminateToken: str
    ProvisionedProductName: Optional[str] = None
    ProvisionedProductId: Optional[str] = None
    IgnoreErrors: Optional[bool] = None
    AcceptLanguage: Optional[str] = None
    RetainPhysicalResources: Optional[bool] = None


# This class is the input for the 'update_constraint' function.
class UpdateConstraintInput(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None
    Description: Optional[str] = None
    Parameters: Optional[str] = None


class UpdateProvisioningPreferences(BaseValidatorModel):
    StackSetAccounts: Optional[List[str]] = None
    StackSetRegions: Optional[List[str]] = None
    StackSetFailureToleranceCount: Optional[int] = None
    StackSetFailureTolerancePercentage: Optional[int] = None
    StackSetMaxConcurrencyCount: Optional[int] = None
    StackSetMaxConcurrencyPercentage: Optional[int] = None
    StackSetOperationType: Optional[StackSetOperationTypeType] = None


# This class is the input for the 'update_provisioned_product_properties' function.
class UpdateProvisionedProductPropertiesInput(BaseValidatorModel):
    ProvisionedProductId: str
    ProvisionedProductProperties: Dict[PropertyKeyType, str]
    IdempotencyToken: str
    AcceptLanguage: Optional[str] = None


# This class is the input for the 'update_provisioning_artifact' function.
class UpdateProvisioningArtifactInput(BaseValidatorModel):
    ProductId: str
    ProvisioningArtifactId: str
    AcceptLanguage: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Active: Optional[bool] = None
    Guidance: Optional[ProvisioningArtifactGuidanceType] = None


# This class is the input for the 'update_service_action' function.
class UpdateServiceActionInput(BaseValidatorModel):
    Id: str
    Name: Optional[str] = None
    Definition: Optional[Dict[ServiceActionDefinitionKeyType, str]] = None
    Description: Optional[str] = None
    AcceptLanguage: Optional[str] = None


# This class is the input for the 'update_tag_option' function.
class UpdateTagOptionInput(BaseValidatorModel):
    Id: str
    Value: Optional[str] = None
    Active: Optional[bool] = None


# This class is the input for the 'list_provisioned_product_plans' function.
class ListProvisionedProductPlansInput(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    ProvisionProductId: Optional[str] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None
    AccessLevelFilter: Optional[AccessLevelFilter] = None


# This class is the input for the 'scan_provisioned_products' function.
class ScanProvisionedProductsInput(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    AccessLevelFilter: Optional[AccessLevelFilter] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None


# This class is the input for the 'search_provisioned_products' function.
class SearchProvisionedProductsInput(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    AccessLevelFilter: Optional[AccessLevelFilter] = None
    Filters: Optional[Dict[Literal['SearchQuery'], List[str]]] = None
    SortBy: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None


# This class is the input for the 'batch_associate_service_action_with_provisioning_artifact' function.
class BatchAssociateServiceActionWithProvisioningArtifactInput(BaseValidatorModel):
    ServiceActionAssociations: List[ServiceActionAssociation]
    AcceptLanguage: Optional[str] = None


# This class is the input for the 'batch_disassociate_service_action_from_provisioning_artifact' function.
class BatchDisassociateServiceActionFromProvisioningArtifactInput(BaseValidatorModel):
    ServiceActionAssociations: List[ServiceActionAssociation]
    AcceptLanguage: Optional[str] = None


# This class is the output for the 'batch_associate_service_action_with_provisioning_artifact' function.
class BatchAssociateServiceActionWithProvisioningArtifactOutput(BaseValidatorModel):
    FailedServiceActionAssociations: List[FailedServiceActionAssociation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_disassociate_service_action_from_provisioning_artifact' function.
class BatchDisassociateServiceActionFromProvisioningArtifactOutput(BaseValidatorModel):
    FailedServiceActionAssociations: List[FailedServiceActionAssociation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'copy_product' function.
class CopyProductOutput(BaseValidatorModel):
    CopyProductToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_portfolio_share' function.
class CreatePortfolioShareOutput(BaseValidatorModel):
    PortfolioShareToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_provisioned_product_plan' function.
class CreateProvisionedProductPlanOutput(BaseValidatorModel):
    PlanName: str
    PlanId: str
    ProvisionProductId: str
    ProvisionedProductName: str
    ProvisioningArtifactId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_portfolio_share' function.
class DeletePortfolioShareOutput(BaseValidatorModel):
    PortfolioShareToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_copy_product_status' function.
class DescribeCopyProductStatusOutput(BaseValidatorModel):
    CopyProductStatus: CopyProductStatusType
    TargetProductId: str
    StatusDetail: str
    ResponseMetadata: ResponseMetadata


class GetAWSOrganizationsAccessStatusOutput(BaseValidatorModel):
    AccessStatus: AccessStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_portfolio_access' function.
class ListPortfolioAccessOutput(BaseValidatorModel):
    AccountIds: List[str]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_portfolio_share' function.
class UpdatePortfolioShareOutput(BaseValidatorModel):
    PortfolioShareToken: str
    Status: ShareStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_provisioned_product_properties' function.
class UpdateProvisionedProductPropertiesOutput(BaseValidatorModel):
    ProvisionedProductId: str
    ProvisionedProductProperties: Dict[PropertyKeyType, str]
    RecordId: str
    Status: RecordStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_budgets_for_resource' function.
class ListBudgetsForResourceOutput(BaseValidatorModel):
    Budgets: List[BudgetDetail]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


class SourceConnectionParameters(BaseValidatorModel):
    CodeStar: Optional[CodeStarParameters] = None


# This class is the output for the 'create_constraint' function.
class CreateConstraintOutput(BaseValidatorModel):
    ConstraintDetail: ConstraintDetail
    ConstraintParameters: str
    Status: StatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_constraint' function.
class DescribeConstraintOutput(BaseValidatorModel):
    ConstraintDetail: ConstraintDetail
    ConstraintParameters: str
    Status: StatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_constraints_for_portfolio' function.
class ListConstraintsForPortfolioOutput(BaseValidatorModel):
    ConstraintDetails: List[ConstraintDetail]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_constraint' function.
class UpdateConstraintOutput(BaseValidatorModel):
    ConstraintDetail: ConstraintDetail
    ConstraintParameters: str
    Status: StatusType
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_portfolio' function.
class CreatePortfolioInput(BaseValidatorModel):
    DisplayName: str
    ProviderName: str
    IdempotencyToken: str
    AcceptLanguage: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class LaunchPathSummary(BaseValidatorModel):
    Id: Optional[str] = None
    ConstraintSummaries: Optional[List[ConstraintSummary]] = None
    Tags: Optional[List[Tag]] = None
    Name: Optional[str] = None


class ProvisionedProductAttribute(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    Type: Optional[str] = None
    Id: Optional[str] = None
    Status: Optional[ProvisionedProductStatusType] = None
    StatusMessage: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    IdempotencyToken: Optional[str] = None
    LastRecordId: Optional[str] = None
    LastProvisioningRecordId: Optional[str] = None
    LastSuccessfulProvisioningRecordId: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    PhysicalId: Optional[str] = None
    ProductId: Optional[str] = None
    ProductName: Optional[str] = None
    ProvisioningArtifactId: Optional[str] = None
    ProvisioningArtifactName: Optional[str] = None
    UserArn: Optional[str] = None
    UserArnSession: Optional[str] = None


# This class is the input for the 'update_portfolio' function.
class UpdatePortfolioInput(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None
    DisplayName: Optional[str] = None
    Description: Optional[str] = None
    ProviderName: Optional[str] = None
    AddTags: Optional[List[Tag]] = None
    RemoveTags: Optional[List[str]] = None


# This class is the output for the 'create_portfolio' function.
class CreatePortfolioOutput(BaseValidatorModel):
    PortfolioDetail: PortfolioDetail
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_accepted_portfolio_shares' function.
class ListAcceptedPortfolioSharesOutput(BaseValidatorModel):
    PortfolioDetails: List[PortfolioDetail]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_portfolios_for_product' function.
class ListPortfoliosForProductOutput(BaseValidatorModel):
    PortfolioDetails: List[PortfolioDetail]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_portfolios' function.
class ListPortfoliosOutput(BaseValidatorModel):
    PortfolioDetails: List[PortfolioDetail]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_portfolio' function.
class UpdatePortfolioOutput(BaseValidatorModel):
    PortfolioDetail: PortfolioDetail
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_portfolio_share' function.
class CreatePortfolioShareInput(BaseValidatorModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    AccountId: Optional[str] = None
    OrganizationNode: Optional[OrganizationNode] = None
    ShareTagOptions: Optional[bool] = None
    SharePrincipals: Optional[bool] = None


# This class is the input for the 'delete_portfolio_share' function.
class DeletePortfolioShareInput(BaseValidatorModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    AccountId: Optional[str] = None
    OrganizationNode: Optional[OrganizationNode] = None


# This class is the output for the 'list_organization_portfolio_access' function.
class ListOrganizationPortfolioAccessOutput(BaseValidatorModel):
    OrganizationNodes: List[OrganizationNode]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_portfolio_share' function.
class UpdatePortfolioShareInput(BaseValidatorModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    AccountId: Optional[str] = None
    OrganizationNode: Optional[OrganizationNode] = None
    ShareTagOptions: Optional[bool] = None
    SharePrincipals: Optional[bool] = None


# This class is the input for the 'create_provisioning_artifact' function.
class CreateProvisioningArtifactInput(BaseValidatorModel):
    ProductId: str
    Parameters: ProvisioningArtifactProperties
    IdempotencyToken: str
    AcceptLanguage: Optional[str] = None


# This class is the output for the 'create_provisioning_artifact' function.
class CreateProvisioningArtifactOutput(BaseValidatorModel):
    ProvisioningArtifactDetail: ProvisioningArtifactDetail
    Info: Dict[str, str]
    Status: StatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_provisioning_artifacts' function.
class ListProvisioningArtifactsOutput(BaseValidatorModel):
    ProvisioningArtifactDetails: List[ProvisioningArtifactDetail]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_provisioning_artifact' function.
class UpdateProvisioningArtifactOutput(BaseValidatorModel):
    ProvisioningArtifactDetail: ProvisioningArtifactDetail
    Info: Dict[str, str]
    Status: StatusType
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_provisioned_product_plan' function.
class CreateProvisionedProductPlanInput(BaseValidatorModel):
    PlanName: str
    PlanType: Literal['CLOUDFORMATION']
    ProductId: str
    ProvisionedProductName: str
    ProvisioningArtifactId: str
    IdempotencyToken: str
    AcceptLanguage: Optional[str] = None
    NotificationArns: Optional[List[str]] = None
    PathId: Optional[str] = None
    ProvisioningParameters: Optional[List[UpdateProvisioningParameter]] = None
    Tags: Optional[List[Tag]] = None


class ProvisionedProductPlanDetails(BaseValidatorModel):
    CreatedTime: Optional[datetime] = None
    PathId: Optional[str] = None
    ProductId: Optional[str] = None
    PlanName: Optional[str] = None
    PlanId: Optional[str] = None
    ProvisionProductId: Optional[str] = None
    ProvisionProductName: Optional[str] = None
    PlanType: Optional[Literal['CLOUDFORMATION']] = None
    ProvisioningArtifactId: Optional[str] = None
    Status: Optional[ProvisionedProductPlanStatusType] = None
    UpdatedTime: Optional[datetime] = None
    NotificationArns: Optional[List[str]] = None
    ProvisioningParameters: Optional[List[UpdateProvisioningParameter]] = None
    Tags: Optional[List[Tag]] = None
    StatusMessage: Optional[str] = None


# This class is the output for the 'create_tag_option' function.
class CreateTagOptionOutput(BaseValidatorModel):
    TagOptionDetail: TagOptionDetail
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_portfolio' function.
class DescribePortfolioOutput(BaseValidatorModel):
    PortfolioDetail: PortfolioDetail
    Tags: List[Tag]
    TagOptions: List[TagOptionDetail]
    Budgets: List[BudgetDetail]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_tag_option' function.
class DescribeTagOptionOutput(BaseValidatorModel):
    TagOptionDetail: TagOptionDetail
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tag_options' function.
class ListTagOptionsOutput(BaseValidatorModel):
    TagOptionDetails: List[TagOptionDetail]
    PageToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_tag_option' function.
class UpdateTagOptionOutput(BaseValidatorModel):
    TagOptionDetail: TagOptionDetail
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_portfolio_shares' function.
class DescribePortfolioSharesOutput(BaseValidatorModel):
    NextPageToken: str
    PortfolioShareDetails: List[PortfolioShareDetail]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_product' function.
class DescribeProductOutput(BaseValidatorModel):
    ProductViewSummary: ProductViewSummary
    ProvisioningArtifacts: List[ProvisioningArtifact]
    Budgets: List[BudgetDetail]
    LaunchPaths: List[LaunchPath]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_product_view' function.
class DescribeProductViewOutput(BaseValidatorModel):
    ProductViewSummary: ProductViewSummary
    ProvisioningArtifacts: List[ProvisioningArtifact]
    ResponseMetadata: ResponseMetadata


class ProvisioningArtifactView(BaseValidatorModel):
    ProductViewSummary: Optional[ProductViewSummary] = None
    ProvisioningArtifact: Optional[ProvisioningArtifact] = None


# This class is the output for the 'describe_provisioned_product' function.
class DescribeProvisionedProductOutput(BaseValidatorModel):
    ProvisionedProductDetail: ProvisionedProductDetail
    CloudWatchDashboards: List[CloudWatchDashboard]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'scan_provisioned_products' function.
class ScanProvisionedProductsOutput(BaseValidatorModel):
    ProvisionedProducts: List[ProvisionedProductDetail]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_provisioned_product_outputs' function.
class GetProvisionedProductOutputsOutput(BaseValidatorModel):
    Outputs: List[RecordOutput]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


class NotifyUpdateProvisionedProductEngineWorkflowResultInput(BaseValidatorModel):
    WorkflowToken: str
    RecordId: str
    Status: EngineWorkflowStatusType
    IdempotencyToken: str
    FailureReason: Optional[str] = None
    Outputs: Optional[List[RecordOutput]] = None


# This class is the output for the 'describe_service_action_execution_parameters' function.
class DescribeServiceActionExecutionParametersOutput(BaseValidatorModel):
    ServiceActionParameters: List[ExecutionParameter]
    ResponseMetadata: ResponseMetadata


class EngineWorkflowResourceIdentifier(BaseValidatorModel):
    UniqueTag: Optional[UniqueTagResourceIdentifier] = None


class ListAcceptedPortfolioSharesInputPaginate(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    PortfolioShareType: Optional[PortfolioShareTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListConstraintsForPortfolioInputPaginate(BaseValidatorModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    ProductId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLaunchPathsInputPaginate(BaseValidatorModel):
    ProductId: str
    AcceptLanguage: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOrganizationPortfolioAccessInputPaginate(BaseValidatorModel):
    PortfolioId: str
    OrganizationNodeType: OrganizationNodeTypeType
    AcceptLanguage: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPortfoliosForProductInputPaginate(BaseValidatorModel):
    ProductId: str
    AcceptLanguage: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPortfoliosInputPaginate(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPrincipalsForPortfolioInputPaginate(BaseValidatorModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProvisionedProductPlansInputPaginate(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    ProvisionProductId: Optional[str] = None
    AccessLevelFilter: Optional[AccessLevelFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProvisioningArtifactsForServiceActionInputPaginate(BaseValidatorModel):
    ServiceActionId: str
    AcceptLanguage: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResourcesForTagOptionInputPaginate(BaseValidatorModel):
    TagOptionId: str
    ResourceType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListServiceActionsForProvisioningArtifactInputPaginate(BaseValidatorModel):
    ProductId: str
    ProvisioningArtifactId: str
    AcceptLanguage: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListServiceActionsInputPaginate(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ScanProvisionedProductsInputPaginate(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    AccessLevelFilter: Optional[AccessLevelFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchProductsAsAdminInputPaginate(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    PortfolioId: Optional[str] = None
    Filters: Optional[Dict[ProductViewFilterByType, List[str]]] = None
    SortBy: Optional[ProductViewSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    ProductSource: Optional[Literal['ACCOUNT']] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_principals_for_portfolio' function.
class ListPrincipalsForPortfolioOutput(BaseValidatorModel):
    Principals: List[Principal]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_provisioned_product_plans' function.
class ListProvisionedProductPlansOutput(BaseValidatorModel):
    ProvisionedProductPlans: List[ProvisionedProductPlanSummary]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


class ListRecordHistoryInputPaginate(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    AccessLevelFilter: Optional[AccessLevelFilter] = None
    SearchFilter: Optional[ListRecordHistorySearchFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_record_history' function.
class ListRecordHistoryInput(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    AccessLevelFilter: Optional[AccessLevelFilter] = None
    SearchFilter: Optional[ListRecordHistorySearchFilter] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None


# This class is the output for the 'list_resources_for_tag_option' function.
class ListResourcesForTagOptionOutput(BaseValidatorModel):
    ResourceDetails: List[ResourceDetail]
    PageToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_service_actions_for_provisioning_artifact' function.
class ListServiceActionsForProvisioningArtifactOutput(BaseValidatorModel):
    ServiceActionSummaries: List[ServiceActionSummary]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_service_actions' function.
class ListServiceActionsOutput(BaseValidatorModel):
    ServiceActionSummaries: List[ServiceActionSummary]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


class ServiceActionDetail(BaseValidatorModel):
    ServiceActionSummary: Optional[ServiceActionSummary] = None
    Definition: Optional[Dict[ServiceActionDefinitionKeyType, str]] = None


# This class is the output for the 'list_stack_instances_for_provisioned_product' function.
class ListStackInstancesForProvisionedProductOutput(BaseValidatorModel):
    StackInstances: List[StackInstance]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


class ListTagOptionsInputPaginate(BaseValidatorModel):
    Filters: Optional[ListTagOptionsFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_tag_options' function.
class ListTagOptionsInput(BaseValidatorModel):
    Filters: Optional[ListTagOptionsFilters] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None


class ProvisioningArtifactParameter(BaseValidatorModel):
    ParameterKey: Optional[str] = None
    DefaultValue: Optional[str] = None
    ParameterType: Optional[str] = None
    IsNoEcho: Optional[bool] = None
    Description: Optional[str] = None
    ParameterConstraints: Optional[ParameterConstraints] = None


# This class is the output for the 'search_products' function.
class SearchProductsOutput(BaseValidatorModel):
    ProductViewSummaries: List[ProductViewSummary]
    ProductViewAggregations: Dict[str, List[ProductViewAggregationValue]]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'provision_product' function.
class ProvisionProductInput(BaseValidatorModel):
    ProvisionedProductName: str
    ProvisionToken: str
    AcceptLanguage: Optional[str] = None
    ProductId: Optional[str] = None
    ProductName: Optional[str] = None
    ProvisioningArtifactId: Optional[str] = None
    ProvisioningArtifactName: Optional[str] = None
    PathId: Optional[str] = None
    PathName: Optional[str] = None
    ProvisioningParameters: Optional[List[ProvisioningParameter]] = None
    ProvisioningPreferences: Optional[ProvisioningPreferences] = None
    Tags: Optional[List[Tag]] = None
    NotificationArns: Optional[List[str]] = None


class RecordDetail(BaseValidatorModel):
    RecordId: Optional[str] = None
    ProvisionedProductName: Optional[str] = None
    Status: Optional[RecordStatusType] = None
    CreatedTime: Optional[datetime] = None
    UpdatedTime: Optional[datetime] = None
    ProvisionedProductType: Optional[str] = None
    RecordType: Optional[str] = None
    ProvisionedProductId: Optional[str] = None
    ProductId: Optional[str] = None
    ProvisioningArtifactId: Optional[str] = None
    PathId: Optional[str] = None
    RecordErrors: Optional[List[RecordError]] = None
    RecordTags: Optional[List[RecordTag]] = None
    LaunchRoleArn: Optional[str] = None


class ResourceChangeDetail(BaseValidatorModel):
    Target: Optional[ResourceTargetDefinition] = None
    Evaluation: Optional[EvaluationTypeType] = None
    CausingEntity: Optional[str] = None


class ShareDetails(BaseValidatorModel):
    SuccessfulShares: Optional[List[str]] = None
    ShareErrors: Optional[List[ShareError]] = None


# This class is the input for the 'update_provisioned_product' function.
class UpdateProvisionedProductInput(BaseValidatorModel):
    UpdateToken: str
    AcceptLanguage: Optional[str] = None
    ProvisionedProductName: Optional[str] = None
    ProvisionedProductId: Optional[str] = None
    ProductId: Optional[str] = None
    ProductName: Optional[str] = None
    ProvisioningArtifactId: Optional[str] = None
    ProvisioningArtifactName: Optional[str] = None
    PathId: Optional[str] = None
    PathName: Optional[str] = None
    ProvisioningParameters: Optional[List[UpdateProvisioningParameter]] = None
    ProvisioningPreferences: Optional[UpdateProvisioningPreferences] = None
    Tags: Optional[List[Tag]] = None


class SourceConnectionDetail(BaseValidatorModel):
    Type: Optional[Literal['CODESTAR']] = None
    ConnectionParameters: Optional[SourceConnectionParameters] = None
    LastSync: Optional[LastSync] = None


class SourceConnection(BaseValidatorModel):
    ConnectionParameters: SourceConnectionParameters
    Type: Optional[Literal['CODESTAR']] = None


# This class is the output for the 'list_launch_paths' function.
class ListLaunchPathsOutput(BaseValidatorModel):
    LaunchPathSummaries: List[LaunchPathSummary]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'search_provisioned_products' function.
class SearchProvisionedProductsOutput(BaseValidatorModel):
    ProvisionedProducts: List[ProvisionedProductAttribute]
    TotalResultsCount: int
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_provisioning_artifacts_for_service_action' function.
class ListProvisioningArtifactsForServiceActionOutput(BaseValidatorModel):
    ProvisioningArtifactViews: List[ProvisioningArtifactView]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


class NotifyProvisionProductEngineWorkflowResultInput(BaseValidatorModel):
    WorkflowToken: str
    RecordId: str
    Status: EngineWorkflowStatusType
    IdempotencyToken: str
    FailureReason: Optional[str] = None
    ResourceIdentifier: Optional[EngineWorkflowResourceIdentifier] = None
    Outputs: Optional[List[RecordOutput]] = None


# This class is the output for the 'create_service_action' function.
class CreateServiceActionOutput(BaseValidatorModel):
    ServiceActionDetail: ServiceActionDetail
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_service_action' function.
class DescribeServiceActionOutput(BaseValidatorModel):
    ServiceActionDetail: ServiceActionDetail
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_service_action' function.
class UpdateServiceActionOutput(BaseValidatorModel):
    ServiceActionDetail: ServiceActionDetail
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_provisioning_artifact' function.
class DescribeProvisioningArtifactOutput(BaseValidatorModel):
    ProvisioningArtifactDetail: ProvisioningArtifactDetail
    Info: Dict[str, str]
    Status: StatusType
    ProvisioningArtifactParameters: List[ProvisioningArtifactParameter]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_provisioning_parameters' function.
class DescribeProvisioningParametersOutput(BaseValidatorModel):
    ProvisioningArtifactParameters: List[ProvisioningArtifactParameter]
    ConstraintSummaries: List[ConstraintSummary]
    UsageInstructions: List[UsageInstruction]
    TagOptions: List[TagOptionSummary]
    ProvisioningArtifactPreferences: ProvisioningArtifactPreferences
    ProvisioningArtifactOutputs: List[ProvisioningArtifactOutput]
    ProvisioningArtifactOutputKeys: List[ProvisioningArtifactOutput]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_record' function.
class DescribeRecordOutput(BaseValidatorModel):
    RecordDetail: RecordDetail
    RecordOutputs: List[RecordOutput]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'execute_provisioned_product_plan' function.
class ExecuteProvisionedProductPlanOutput(BaseValidatorModel):
    RecordDetail: RecordDetail
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'execute_provisioned_product_service_action' function.
class ExecuteProvisionedProductServiceActionOutput(BaseValidatorModel):
    RecordDetail: RecordDetail
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'import_as_provisioned_product' function.
class ImportAsProvisionedProductOutput(BaseValidatorModel):
    RecordDetail: RecordDetail
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_record_history' function.
class ListRecordHistoryOutput(BaseValidatorModel):
    RecordDetails: List[RecordDetail]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'provision_product' function.
class ProvisionProductOutput(BaseValidatorModel):
    RecordDetail: RecordDetail
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'terminate_provisioned_product' function.
class TerminateProvisionedProductOutput(BaseValidatorModel):
    RecordDetail: RecordDetail
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_provisioned_product' function.
class UpdateProvisionedProductOutput(BaseValidatorModel):
    RecordDetail: RecordDetail
    ResponseMetadata: ResponseMetadata


class ResourceChange(BaseValidatorModel):
    Action: Optional[ChangeActionType] = None
    LogicalResourceId: Optional[str] = None
    PhysicalResourceId: Optional[str] = None
    ResourceType: Optional[str] = None
    Replacement: Optional[ReplacementType] = None
    Scope: Optional[List[ResourceAttributeType]] = None
    Details: Optional[List[ResourceChangeDetail]] = None


# This class is the output for the 'describe_portfolio_share_status' function.
class DescribePortfolioShareStatusOutput(BaseValidatorModel):
    PortfolioShareToken: str
    PortfolioId: str
    OrganizationNodeValue: str
    Status: ShareStatusType
    ShareDetails: ShareDetails
    ResponseMetadata: ResponseMetadata


class ProductViewDetail(BaseValidatorModel):
    ProductViewSummary: Optional[ProductViewSummary] = None
    Status: Optional[StatusType] = None
    ProductARN: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    SourceConnection: Optional[SourceConnectionDetail] = None


# This class is the input for the 'create_product' function.
class CreateProductInput(BaseValidatorModel):
    Name: str
    Owner: str
    ProductType: ProductTypeType
    IdempotencyToken: str
    AcceptLanguage: Optional[str] = None
    Description: Optional[str] = None
    Distributor: Optional[str] = None
    SupportDescription: Optional[str] = None
    SupportEmail: Optional[str] = None
    SupportUrl: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    ProvisioningArtifactParameters: Optional[ProvisioningArtifactProperties] = None
    SourceConnection: Optional[SourceConnection] = None


# This class is the input for the 'update_product' function.
class UpdateProductInput(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None
    Name: Optional[str] = None
    Owner: Optional[str] = None
    Description: Optional[str] = None
    Distributor: Optional[str] = None
    SupportDescription: Optional[str] = None
    SupportEmail: Optional[str] = None
    SupportUrl: Optional[str] = None
    AddTags: Optional[List[Tag]] = None
    RemoveTags: Optional[List[str]] = None
    SourceConnection: Optional[SourceConnection] = None


# This class is the output for the 'describe_provisioned_product_plan' function.
class DescribeProvisionedProductPlanOutput(BaseValidatorModel):
    ProvisionedProductPlanDetails: ProvisionedProductPlanDetails
    ResourceChanges: List[ResourceChange]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_product' function.
class CreateProductOutput(BaseValidatorModel):
    ProductViewDetail: ProductViewDetail
    ProvisioningArtifactDetail: ProvisioningArtifactDetail
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_product_as_admin' function.
class DescribeProductAsAdminOutput(BaseValidatorModel):
    ProductViewDetail: ProductViewDetail
    ProvisioningArtifactSummaries: List[ProvisioningArtifactSummary]
    Tags: List[Tag]
    TagOptions: List[TagOptionDetail]
    Budgets: List[BudgetDetail]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'search_products_as_admin' function.
class SearchProductsAsAdminOutput(BaseValidatorModel):
    ProductViewDetails: List[ProductViewDetail]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_product' function.
class UpdateProductOutput(BaseValidatorModel):
    ProductViewDetail: ProductViewDetail
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata
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


class CopyProductInput(BaseValidatorModel):
    SourceProductArn: str
    IdempotencyToken: str
    AcceptLanguage: Optional[str] = None
    TargetProductId: Optional[str] = None
    TargetProductName: Optional[str] = None
    SourceProvisioningArtifactIdentifiers: Optional[List[Dict[Literal['Id'], str]]] = None
    CopyOptions: Optional[List[Literal['CopyTags']]] = None


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


class CreateServiceActionInput(BaseValidatorModel):
    Name: str
    DefinitionType: Literal['SSM_AUTOMATION']
    Definition: Dict[ServiceActionDefinitionKeyType, str]
    IdempotencyToken: str
    Description: Optional[str] = None
    AcceptLanguage: Optional[str] = None


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


class DescribeConstraintInput(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None


class DescribeCopyProductStatusInput(BaseValidatorModel):
    CopyProductToken: str
    AcceptLanguage: Optional[str] = None


class DescribePortfolioInput(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None


class DescribePortfolioShareStatusInput(BaseValidatorModel):
    PortfolioShareToken: str


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


class DescribeProductViewInput(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None


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


class DescribeProvisionedProductPlanInput(BaseValidatorModel):
    PlanId: str
    AcceptLanguage: Optional[str] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None


class DescribeProvisioningArtifactInput(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    ProvisioningArtifactId: Optional[str] = None
    ProductId: Optional[str] = None
    ProvisioningArtifactName: Optional[str] = None
    ProductName: Optional[str] = None
    Verbose: Optional[bool] = None
    IncludeProvisioningArtifactParameters: Optional[bool] = None


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


class DescribeRecordInput(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None


class RecordOutput(BaseValidatorModel):
    OutputKey: Optional[str] = None
    OutputValue: Optional[str] = None
    Description: Optional[str] = None


class DescribeServiceActionExecutionParametersInput(BaseValidatorModel):
    ProvisionedProductId: str
    ServiceActionId: str
    AcceptLanguage: Optional[str] = None


class ExecutionParameter(BaseValidatorModel):
    Name: Optional[str] = None
    Type: Optional[str] = None
    DefaultValues: Optional[List[str]] = None


class DescribeServiceActionInput(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None


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


class ExecuteProvisionedProductPlanInput(BaseValidatorModel):
    PlanId: str
    IdempotencyToken: str
    AcceptLanguage: Optional[str] = None


class ExecuteProvisionedProductServiceActionInput(BaseValidatorModel):
    ProvisionedProductId: str
    ServiceActionId: str
    ExecuteToken: str
    AcceptLanguage: Optional[str] = None
    Parameters: Optional[Dict[str, List[str]]] = None


class GetProvisionedProductOutputsInput(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    ProvisionedProductId: Optional[str] = None
    ProvisionedProductName: Optional[str] = None
    OutputKeys: Optional[List[str]] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None


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


class ListAcceptedPortfolioSharesInput(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None
    PortfolioShareType: Optional[PortfolioShareTypeType] = None


class ListBudgetsForResourceInput(BaseValidatorModel):
    ResourceId: str
    AcceptLanguage: Optional[str] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None


class ListConstraintsForPortfolioInput(BaseValidatorModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    ProductId: Optional[str] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None


class ListLaunchPathsInput(BaseValidatorModel):
    ProductId: str
    AcceptLanguage: Optional[str] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None


class ListOrganizationPortfolioAccessInput(BaseValidatorModel):
    PortfolioId: str
    OrganizationNodeType: OrganizationNodeTypeType
    AcceptLanguage: Optional[str] = None
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None


class ListPortfolioAccessInput(BaseValidatorModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    OrganizationParentId: Optional[str] = None
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None


class ListPortfoliosForProductInput(BaseValidatorModel):
    ProductId: str
    AcceptLanguage: Optional[str] = None
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None


class ListPortfoliosInput(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None


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


class ListProvisioningArtifactsForServiceActionInput(BaseValidatorModel):
    ServiceActionId: str
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None
    AcceptLanguage: Optional[str] = None


class ListProvisioningArtifactsInput(BaseValidatorModel):
    ProductId: str
    AcceptLanguage: Optional[str] = None


class ListRecordHistorySearchFilter(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


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


class ListServiceActionsInput(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None


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


class SearchProductsAsAdminInput(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    PortfolioId: Optional[str] = None
    Filters: Optional[Dict[ProductViewFilterByType, List[str]]] = None
    SortBy: Optional[ProductViewSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None
    ProductSource: Optional[Literal['ACCOUNT']] = None


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


class TerminateProvisionedProductInput(BaseValidatorModel):
    TerminateToken: str
    ProvisionedProductName: Optional[str] = None
    ProvisionedProductId: Optional[str] = None
    IgnoreErrors: Optional[bool] = None
    AcceptLanguage: Optional[str] = None
    RetainPhysicalResources: Optional[bool] = None


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


class UpdateProvisionedProductPropertiesInput(BaseValidatorModel):
    ProvisionedProductId: str
    ProvisionedProductProperties: Dict[PropertyKeyType, str]
    IdempotencyToken: str
    AcceptLanguage: Optional[str] = None


class UpdateProvisioningArtifactInput(BaseValidatorModel):
    ProductId: str
    ProvisioningArtifactId: str
    AcceptLanguage: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Active: Optional[bool] = None
    Guidance: Optional[ProvisioningArtifactGuidanceType] = None


class UpdateServiceActionInput(BaseValidatorModel):
    Id: str
    Name: Optional[str] = None
    Definition: Optional[Dict[ServiceActionDefinitionKeyType, str]] = None
    Description: Optional[str] = None
    AcceptLanguage: Optional[str] = None


class UpdateTagOptionInput(BaseValidatorModel):
    Id: str
    Value: Optional[str] = None
    Active: Optional[bool] = None


class ListProvisionedProductPlansInput(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    ProvisionProductId: Optional[str] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None
    AccessLevelFilter: Optional[AccessLevelFilter] = None


class ScanProvisionedProductsInput(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    AccessLevelFilter: Optional[AccessLevelFilter] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None


class SearchProvisionedProductsInput(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    AccessLevelFilter: Optional[AccessLevelFilter] = None
    Filters: Optional[Dict[Literal['SearchQuery'], List[str]]] = None
    SortBy: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None


class BatchAssociateServiceActionWithProvisioningArtifactInput(BaseValidatorModel):
    ServiceActionAssociations: List[ServiceActionAssociation]
    AcceptLanguage: Optional[str] = None


class BatchDisassociateServiceActionFromProvisioningArtifactInput(BaseValidatorModel):
    ServiceActionAssociations: List[ServiceActionAssociation]
    AcceptLanguage: Optional[str] = None


class BatchAssociateServiceActionWithProvisioningArtifactOutput(BaseValidatorModel):
    FailedServiceActionAssociations: List[FailedServiceActionAssociation]
    ResponseMetadata: ResponseMetadata


class BatchDisassociateServiceActionFromProvisioningArtifactOutput(BaseValidatorModel):
    FailedServiceActionAssociations: List[FailedServiceActionAssociation]
    ResponseMetadata: ResponseMetadata


class CopyProductOutput(BaseValidatorModel):
    CopyProductToken: str
    ResponseMetadata: ResponseMetadata


class CreatePortfolioShareOutput(BaseValidatorModel):
    PortfolioShareToken: str
    ResponseMetadata: ResponseMetadata


class CreateProvisionedProductPlanOutput(BaseValidatorModel):
    PlanName: str
    PlanId: str
    ProvisionProductId: str
    ProvisionedProductName: str
    ProvisioningArtifactId: str
    ResponseMetadata: ResponseMetadata


class DeletePortfolioShareOutput(BaseValidatorModel):
    PortfolioShareToken: str
    ResponseMetadata: ResponseMetadata


class DescribeCopyProductStatusOutput(BaseValidatorModel):
    CopyProductStatus: CopyProductStatusType
    TargetProductId: str
    StatusDetail: str
    ResponseMetadata: ResponseMetadata


class GetAWSOrganizationsAccessStatusOutput(BaseValidatorModel):
    AccessStatus: AccessStatusType
    ResponseMetadata: ResponseMetadata


class ListPortfolioAccessOutput(BaseValidatorModel):
    AccountIds: List[str]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


class UpdatePortfolioShareOutput(BaseValidatorModel):
    PortfolioShareToken: str
    Status: ShareStatusType
    ResponseMetadata: ResponseMetadata


class UpdateProvisionedProductPropertiesOutput(BaseValidatorModel):
    ProvisionedProductId: str
    ProvisionedProductProperties: Dict[PropertyKeyType, str]
    RecordId: str
    Status: RecordStatusType
    ResponseMetadata: ResponseMetadata


class ListBudgetsForResourceOutput(BaseValidatorModel):
    Budgets: List[BudgetDetail]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


class SourceConnectionParameters(BaseValidatorModel):
    CodeStar: Optional[CodeStarParameters] = None


class CreateConstraintOutput(BaseValidatorModel):
    ConstraintDetail: ConstraintDetail
    ConstraintParameters: str
    Status: StatusType
    ResponseMetadata: ResponseMetadata


class DescribeConstraintOutput(BaseValidatorModel):
    ConstraintDetail: ConstraintDetail
    ConstraintParameters: str
    Status: StatusType
    ResponseMetadata: ResponseMetadata


class ListConstraintsForPortfolioOutput(BaseValidatorModel):
    ConstraintDetails: List[ConstraintDetail]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


class UpdateConstraintOutput(BaseValidatorModel):
    ConstraintDetail: ConstraintDetail
    ConstraintParameters: str
    Status: StatusType
    ResponseMetadata: ResponseMetadata


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


class UpdatePortfolioInput(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None
    DisplayName: Optional[str] = None
    Description: Optional[str] = None
    ProviderName: Optional[str] = None
    AddTags: Optional[List[Tag]] = None
    RemoveTags: Optional[List[str]] = None


class CreatePortfolioOutput(BaseValidatorModel):
    PortfolioDetail: PortfolioDetail
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class ListAcceptedPortfolioSharesOutput(BaseValidatorModel):
    PortfolioDetails: List[PortfolioDetail]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


class ListPortfoliosForProductOutput(BaseValidatorModel):
    PortfolioDetails: List[PortfolioDetail]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


class ListPortfoliosOutput(BaseValidatorModel):
    PortfolioDetails: List[PortfolioDetail]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


class UpdatePortfolioOutput(BaseValidatorModel):
    PortfolioDetail: PortfolioDetail
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class CreatePortfolioShareInput(BaseValidatorModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    AccountId: Optional[str] = None
    OrganizationNode: Optional[OrganizationNode] = None
    ShareTagOptions: Optional[bool] = None
    SharePrincipals: Optional[bool] = None


class DeletePortfolioShareInput(BaseValidatorModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    AccountId: Optional[str] = None
    OrganizationNode: Optional[OrganizationNode] = None


class ListOrganizationPortfolioAccessOutput(BaseValidatorModel):
    OrganizationNodes: List[OrganizationNode]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


class UpdatePortfolioShareInput(BaseValidatorModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    AccountId: Optional[str] = None
    OrganizationNode: Optional[OrganizationNode] = None
    ShareTagOptions: Optional[bool] = None
    SharePrincipals: Optional[bool] = None


class CreateProvisioningArtifactInput(BaseValidatorModel):
    ProductId: str
    Parameters: ProvisioningArtifactProperties
    IdempotencyToken: str
    AcceptLanguage: Optional[str] = None


class CreateProvisioningArtifactOutput(BaseValidatorModel):
    ProvisioningArtifactDetail: ProvisioningArtifactDetail
    Info: Dict[str, str]
    Status: StatusType
    ResponseMetadata: ResponseMetadata


class ListProvisioningArtifactsOutput(BaseValidatorModel):
    ProvisioningArtifactDetails: List[ProvisioningArtifactDetail]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


class UpdateProvisioningArtifactOutput(BaseValidatorModel):
    ProvisioningArtifactDetail: ProvisioningArtifactDetail
    Info: Dict[str, str]
    Status: StatusType
    ResponseMetadata: ResponseMetadata


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


class CreateTagOptionOutput(BaseValidatorModel):
    TagOptionDetail: TagOptionDetail
    ResponseMetadata: ResponseMetadata


class DescribePortfolioOutput(BaseValidatorModel):
    PortfolioDetail: PortfolioDetail
    Tags: List[Tag]
    TagOptions: List[TagOptionDetail]
    Budgets: List[BudgetDetail]
    ResponseMetadata: ResponseMetadata


class DescribeTagOptionOutput(BaseValidatorModel):
    TagOptionDetail: TagOptionDetail
    ResponseMetadata: ResponseMetadata


class ListTagOptionsOutput(BaseValidatorModel):
    TagOptionDetails: List[TagOptionDetail]
    PageToken: str
    ResponseMetadata: ResponseMetadata


class UpdateTagOptionOutput(BaseValidatorModel):
    TagOptionDetail: TagOptionDetail
    ResponseMetadata: ResponseMetadata


class DescribePortfolioSharesOutput(BaseValidatorModel):
    NextPageToken: str
    PortfolioShareDetails: List[PortfolioShareDetail]
    ResponseMetadata: ResponseMetadata


class DescribeProductOutput(BaseValidatorModel):
    ProductViewSummary: ProductViewSummary
    ProvisioningArtifacts: List[ProvisioningArtifact]
    Budgets: List[BudgetDetail]
    LaunchPaths: List[LaunchPath]
    ResponseMetadata: ResponseMetadata


class DescribeProductViewOutput(BaseValidatorModel):
    ProductViewSummary: ProductViewSummary
    ProvisioningArtifacts: List[ProvisioningArtifact]
    ResponseMetadata: ResponseMetadata


class ProvisioningArtifactView(BaseValidatorModel):
    ProductViewSummary: Optional[ProductViewSummary] = None
    ProvisioningArtifact: Optional[ProvisioningArtifact] = None


class DescribeProvisionedProductOutput(BaseValidatorModel):
    ProvisionedProductDetail: ProvisionedProductDetail
    CloudWatchDashboards: List[CloudWatchDashboard]
    ResponseMetadata: ResponseMetadata


class ScanProvisionedProductsOutput(BaseValidatorModel):
    ProvisionedProducts: List[ProvisionedProductDetail]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


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


class ListPrincipalsForPortfolioOutput(BaseValidatorModel):
    Principals: List[Principal]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


class ListProvisionedProductPlansOutput(BaseValidatorModel):
    ProvisionedProductPlans: List[ProvisionedProductPlanSummary]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


class ListRecordHistoryInputPaginate(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    AccessLevelFilter: Optional[AccessLevelFilter] = None
    SearchFilter: Optional[ListRecordHistorySearchFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRecordHistoryInput(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    AccessLevelFilter: Optional[AccessLevelFilter] = None
    SearchFilter: Optional[ListRecordHistorySearchFilter] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None


class ListResourcesForTagOptionOutput(BaseValidatorModel):
    ResourceDetails: List[ResourceDetail]
    PageToken: str
    ResponseMetadata: ResponseMetadata


class ListServiceActionsForProvisioningArtifactOutput(BaseValidatorModel):
    ServiceActionSummaries: List[ServiceActionSummary]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


class ListServiceActionsOutput(BaseValidatorModel):
    ServiceActionSummaries: List[ServiceActionSummary]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


class ServiceActionDetail(BaseValidatorModel):
    ServiceActionSummary: Optional[ServiceActionSummary] = None
    Definition: Optional[Dict[ServiceActionDefinitionKeyType, str]] = None


class ListStackInstancesForProvisionedProductOutput(BaseValidatorModel):
    StackInstances: List[StackInstance]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


class ListTagOptionsInputPaginate(BaseValidatorModel):
    Filters: Optional[ListTagOptionsFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


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


class SearchProductsOutput(BaseValidatorModel):
    ProductViewSummaries: List[ProductViewSummary]
    ProductViewAggregations: Dict[str, List[ProductViewAggregationValue]]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


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


class ListLaunchPathsOutput(BaseValidatorModel):
    LaunchPathSummaries: List[LaunchPathSummary]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


class SearchProvisionedProductsOutput(BaseValidatorModel):
    ProvisionedProducts: List[ProvisionedProductAttribute]
    TotalResultsCount: int
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


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


class CreateServiceActionOutput(BaseValidatorModel):
    ServiceActionDetail: ServiceActionDetail
    ResponseMetadata: ResponseMetadata


class DescribeServiceActionOutput(BaseValidatorModel):
    ServiceActionDetail: ServiceActionDetail
    ResponseMetadata: ResponseMetadata


class UpdateServiceActionOutput(BaseValidatorModel):
    ServiceActionDetail: ServiceActionDetail
    ResponseMetadata: ResponseMetadata


class DescribeProvisioningArtifactOutput(BaseValidatorModel):
    ProvisioningArtifactDetail: ProvisioningArtifactDetail
    Info: Dict[str, str]
    Status: StatusType
    ProvisioningArtifactParameters: List[ProvisioningArtifactParameter]
    ResponseMetadata: ResponseMetadata


class DescribeProvisioningParametersOutput(BaseValidatorModel):
    ProvisioningArtifactParameters: List[ProvisioningArtifactParameter]
    ConstraintSummaries: List[ConstraintSummary]
    UsageInstructions: List[UsageInstruction]
    TagOptions: List[TagOptionSummary]
    ProvisioningArtifactPreferences: ProvisioningArtifactPreferences
    ProvisioningArtifactOutputs: List[ProvisioningArtifactOutput]
    ProvisioningArtifactOutputKeys: List[ProvisioningArtifactOutput]
    ResponseMetadata: ResponseMetadata


class DescribeRecordOutput(BaseValidatorModel):
    RecordDetail: RecordDetail
    RecordOutputs: List[RecordOutput]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


class ExecuteProvisionedProductPlanOutput(BaseValidatorModel):
    RecordDetail: RecordDetail
    ResponseMetadata: ResponseMetadata


class ExecuteProvisionedProductServiceActionOutput(BaseValidatorModel):
    RecordDetail: RecordDetail
    ResponseMetadata: ResponseMetadata


class ImportAsProvisionedProductOutput(BaseValidatorModel):
    RecordDetail: RecordDetail
    ResponseMetadata: ResponseMetadata


class ListRecordHistoryOutput(BaseValidatorModel):
    RecordDetails: List[RecordDetail]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


class ProvisionProductOutput(BaseValidatorModel):
    RecordDetail: RecordDetail
    ResponseMetadata: ResponseMetadata


class TerminateProvisionedProductOutput(BaseValidatorModel):
    RecordDetail: RecordDetail
    ResponseMetadata: ResponseMetadata


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


class DescribeProvisionedProductPlanOutput(BaseValidatorModel):
    ProvisionedProductPlanDetails: ProvisionedProductPlanDetails
    ResourceChanges: List[ResourceChange]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


class CreateProductOutput(BaseValidatorModel):
    ProductViewDetail: ProductViewDetail
    ProvisioningArtifactDetail: ProvisioningArtifactDetail
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class DescribeProductAsAdminOutput(BaseValidatorModel):
    ProductViewDetail: ProductViewDetail
    ProvisioningArtifactSummaries: List[ProvisioningArtifactSummary]
    Tags: List[Tag]
    TagOptions: List[TagOptionDetail]
    Budgets: List[BudgetDetail]
    ResponseMetadata: ResponseMetadata


class SearchProductsAsAdminOutput(BaseValidatorModel):
    ProductViewDetails: List[ProductViewDetail]
    NextPageToken: str
    ResponseMetadata: ResponseMetadata


class UpdateProductOutput(BaseValidatorModel):
    ProductViewDetail: ProductViewDetail
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata
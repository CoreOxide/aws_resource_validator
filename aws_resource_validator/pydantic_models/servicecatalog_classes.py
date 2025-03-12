from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from botocore.response import StreamingBody
from datetime import datetime
from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Literal
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union
from aws_resource_validator.pydantic_models.servicecatalog_constants import *

class AcceptPortfolioShareInputTypeDef(BaseValidatorModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    PortfolioShareType: Optional[PortfolioShareTypeType] = None


class AccessLevelFilterTypeDef(BaseValidatorModel):
    Key: Optional[AccessLevelFilterKeyType] = None
    Value: Optional[str] = None


class AssociateBudgetWithResourceInputTypeDef(BaseValidatorModel):
    BudgetName: str
    ResourceId: str


class AssociatePrincipalWithPortfolioInputTypeDef(BaseValidatorModel):
    PortfolioId: str
    PrincipalARN: str
    PrincipalType: PrincipalTypeType
    AcceptLanguage: Optional[str] = None


class AssociateProductWithPortfolioInputTypeDef(BaseValidatorModel):
    ProductId: str
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    SourcePortfolioId: Optional[str] = None


class AssociateServiceActionWithProvisioningArtifactInputTypeDef(BaseValidatorModel):
    ProductId: str
    ProvisioningArtifactId: str
    ServiceActionId: str
    AcceptLanguage: Optional[str] = None
    IdempotencyToken: Optional[str] = None


class AssociateTagOptionWithResourceInputTypeDef(BaseValidatorModel):
    ResourceId: str
    TagOptionId: str


class ServiceActionAssociationTypeDef(BaseValidatorModel):
    ServiceActionId: str
    ProductId: str
    ProvisioningArtifactId: str


class FailedServiceActionAssociationTypeDef(BaseValidatorModel):
    ServiceActionId: Optional[str] = None
    ProductId: Optional[str] = None
    ProvisioningArtifactId: Optional[str] = None
    ErrorCode: Optional[ServiceActionAssociationErrorCodeType] = None
    ErrorMessage: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BudgetDetailTypeDef(BaseValidatorModel):
    BudgetName: Optional[str] = None


class CloudWatchDashboardTypeDef(BaseValidatorModel):
    Name: Optional[str] = None


class CodeStarParametersTypeDef(BaseValidatorModel):
    ConnectionArn: str
    Repository: str
    Branch: str
    ArtifactPath: str


class CopyProductInputTypeDef(BaseValidatorModel):
    SourceProductArn: str
    IdempotencyToken: str
    AcceptLanguage: Optional[str] = None
    TargetProductId: Optional[str] = None
    TargetProductName: Optional[str] = None
    SourceProvisioningArtifactIdentifiers: Optional[Sequence[Mapping[Literal["Id"], str]]] = None
    CopyOptions: Optional[Sequence[Literal["CopyTags"]]] = None


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class PortfolioDetailTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    ARN: Optional[str] = None
    DisplayName: Optional[str] = None
    Description: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    ProviderName: Optional[str] = None


class UpdateProvisioningParameterTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    UsePreviousValue: Optional[bool] = None


class CreateServiceActionInputTypeDef(BaseValidatorModel):
    Name: str
    DefinitionType: Literal["SSM_AUTOMATION"]
    Definition: Mapping[ServiceActionDefinitionKeyType, str]
    IdempotencyToken: str
    Description: Optional[str] = None
    AcceptLanguage: Optional[str] = None


class CreateTagOptionInputTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class TagOptionDetailTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    Active: Optional[bool] = None
    Id: Optional[str] = None
    Owner: Optional[str] = None


class DeleteConstraintInputTypeDef(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None


class DeletePortfolioInputTypeDef(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None


class DeleteProductInputTypeDef(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None


class DeleteProvisionedProductPlanInputTypeDef(BaseValidatorModel):
    PlanId: str
    AcceptLanguage: Optional[str] = None
    IgnoreErrors: Optional[bool] = None


class DeleteProvisioningArtifactInputTypeDef(BaseValidatorModel):
    ProductId: str
    ProvisioningArtifactId: str
    AcceptLanguage: Optional[str] = None


class DeleteServiceActionInputTypeDef(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None
    IdempotencyToken: Optional[str] = None


class DeleteTagOptionInputTypeDef(BaseValidatorModel):
    Id: str


class DescribeConstraintInputTypeDef(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None


class DescribeCopyProductStatusInputTypeDef(BaseValidatorModel):
    CopyProductToken: str
    AcceptLanguage: Optional[str] = None


class DescribePortfolioInputTypeDef(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None


class DescribePortfolioShareStatusInputTypeDef(BaseValidatorModel):
    PortfolioShareToken: str


class DescribeProductAsAdminInputTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    SourcePortfolioId: Optional[str] = None


class ProvisioningArtifactSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    ProvisioningArtifactMetadata: Optional[Dict[str, str]] = None


class DescribeProductInputTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None


class LaunchPathTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None


class ProvisioningArtifactTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    Guidance: Optional[ProvisioningArtifactGuidanceType] = None


class DescribeProductViewInputTypeDef(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None


class DescribeProvisionedProductInputTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None


class DescribeProvisionedProductPlanInputTypeDef(BaseValidatorModel):
    PlanId: str
    AcceptLanguage: Optional[str] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None


class DescribeProvisioningArtifactInputTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    ProvisioningArtifactId: Optional[str] = None
    ProductId: Optional[str] = None
    ProvisioningArtifactName: Optional[str] = None
    ProductName: Optional[str] = None
    Verbose: Optional[bool] = None
    IncludeProvisioningArtifactParameters: Optional[bool] = None


class DescribeProvisioningParametersInputTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    ProductId: Optional[str] = None
    ProductName: Optional[str] = None
    ProvisioningArtifactId: Optional[str] = None
    ProvisioningArtifactName: Optional[str] = None
    PathId: Optional[str] = None
    PathName: Optional[str] = None


class ProvisioningArtifactOutputTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Description: Optional[str] = None


class ProvisioningArtifactPreferencesTypeDef(BaseValidatorModel):
    StackSetAccounts: Optional[List[str]] = None
    StackSetRegions: Optional[List[str]] = None


class TagOptionSummaryTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[List[str]] = None


class DescribeRecordInputTypeDef(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None


class RecordOutputTypeDef(BaseValidatorModel):
    OutputKey: Optional[str] = None
    OutputValue: Optional[str] = None
    Description: Optional[str] = None


class DescribeServiceActionExecutionParametersInputTypeDef(BaseValidatorModel):
    ProvisionedProductId: str
    ServiceActionId: str
    AcceptLanguage: Optional[str] = None


class DescribeServiceActionInputTypeDef(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None


class DescribeTagOptionInputTypeDef(BaseValidatorModel):
    Id: str


class DisassociateBudgetFromResourceInputTypeDef(BaseValidatorModel):
    BudgetName: str
    ResourceId: str


class DisassociatePrincipalFromPortfolioInputTypeDef(BaseValidatorModel):
    PortfolioId: str
    PrincipalARN: str
    AcceptLanguage: Optional[str] = None
    PrincipalType: Optional[PrincipalTypeType] = None


class DisassociateProductFromPortfolioInputTypeDef(BaseValidatorModel):
    ProductId: str
    PortfolioId: str
    AcceptLanguage: Optional[str] = None


class DisassociateServiceActionFromProvisioningArtifactInputTypeDef(BaseValidatorModel):
    ProductId: str
    ProvisioningArtifactId: str
    ServiceActionId: str
    AcceptLanguage: Optional[str] = None
    IdempotencyToken: Optional[str] = None


class DisassociateTagOptionFromResourceInputTypeDef(BaseValidatorModel):
    ResourceId: str
    TagOptionId: str


class UniqueTagResourceIdentifierTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class ExecuteProvisionedProductPlanInputTypeDef(BaseValidatorModel):
    PlanId: str
    IdempotencyToken: str
    AcceptLanguage: Optional[str] = None


class ExecuteProvisionedProductServiceActionInputTypeDef(BaseValidatorModel):
    ProvisionedProductId: str
    ServiceActionId: str
    ExecuteToken: str
    AcceptLanguage: Optional[str] = None
    Parameters: Optional[Mapping[str, Sequence[str]]] = None


class GetProvisionedProductOutputsInputTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    ProvisionedProductId: Optional[str] = None
    ProvisionedProductName: Optional[str] = None
    OutputKeys: Optional[Sequence[str]] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None


class ImportAsProvisionedProductInputTypeDef(BaseValidatorModel):
    ProductId: str
    ProvisioningArtifactId: str
    ProvisionedProductName: str
    PhysicalId: str
    IdempotencyToken: str
    AcceptLanguage: Optional[str] = None


class LastSyncTypeDef(BaseValidatorModel):
    LastSyncTime: Optional[datetime] = None
    LastSyncStatus: Optional[LastSyncStatusType] = None
    LastSyncStatusMessage: Optional[str] = None
    LastSuccessfulSyncTime: Optional[datetime] = None
    LastSuccessfulSyncProvisioningArtifactId: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAcceptedPortfolioSharesInputTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None
    PortfolioShareType: Optional[PortfolioShareTypeType] = None


class ListBudgetsForResourceInputTypeDef(BaseValidatorModel):
    ResourceId: str
    AcceptLanguage: Optional[str] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None


class ListConstraintsForPortfolioInputTypeDef(BaseValidatorModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    ProductId: Optional[str] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None


class ListLaunchPathsInputTypeDef(BaseValidatorModel):
    ProductId: str
    AcceptLanguage: Optional[str] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None


class ListOrganizationPortfolioAccessInputTypeDef(BaseValidatorModel):
    PortfolioId: str
    OrganizationNodeType: OrganizationNodeTypeType
    AcceptLanguage: Optional[str] = None
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None


class ListPortfolioAccessInputTypeDef(BaseValidatorModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    OrganizationParentId: Optional[str] = None
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None


class ListPortfoliosForProductInputTypeDef(BaseValidatorModel):
    ProductId: str
    AcceptLanguage: Optional[str] = None
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None


class ListPortfoliosInputTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None


class ListPrincipalsForPortfolioInputTypeDef(BaseValidatorModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None


class PrincipalTypeDef(BaseValidatorModel):
    PrincipalARN: Optional[str] = None
    PrincipalType: Optional[PrincipalTypeType] = None


class ProvisionedProductPlanSummaryTypeDef(BaseValidatorModel):
    PlanName: Optional[str] = None
    PlanId: Optional[str] = None
    ProvisionProductId: Optional[str] = None
    ProvisionProductName: Optional[str] = None
    PlanType: Optional[Literal["CLOUDFORMATION"]] = None
    ProvisioningArtifactId: Optional[str] = None


class ListProvisioningArtifactsForServiceActionInputTypeDef(BaseValidatorModel):
    ServiceActionId: str
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None
    AcceptLanguage: Optional[str] = None


class ListProvisioningArtifactsInputTypeDef(BaseValidatorModel):
    ProductId: str
    AcceptLanguage: Optional[str] = None


class ListRecordHistorySearchFilterTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class ListResourcesForTagOptionInputTypeDef(BaseValidatorModel):
    TagOptionId: str
    ResourceType: Optional[str] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None


class ResourceDetailTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    ARN: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    CreatedTime: Optional[datetime] = None


class ListServiceActionsForProvisioningArtifactInputTypeDef(BaseValidatorModel):
    ProductId: str
    ProvisioningArtifactId: str
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None
    AcceptLanguage: Optional[str] = None


class ServiceActionSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    DefinitionType: Optional[Literal["SSM_AUTOMATION"]] = None


class ListServiceActionsInputTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None


class ListStackInstancesForProvisionedProductInputTypeDef(BaseValidatorModel):
    ProvisionedProductId: str
    AcceptLanguage: Optional[str] = None
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None


class StackInstanceTypeDef(BaseValidatorModel):
    Account: Optional[str] = None
    Region: Optional[str] = None
    StackInstanceStatus: Optional[StackInstanceStatusType] = None


class ListTagOptionsFiltersTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    Active: Optional[bool] = None


class NotifyTerminateProvisionedProductEngineWorkflowResultInputTypeDef(BaseValidatorModel):
    WorkflowToken: str
    RecordId: str
    Status: EngineWorkflowStatusType
    IdempotencyToken: str
    FailureReason: Optional[str] = None


class ParameterConstraintsTypeDef(BaseValidatorModel):
    AllowedValues: Optional[List[str]] = None
    AllowedPattern: Optional[str] = None
    ConstraintDescription: Optional[str] = None
    MaxLength: Optional[str] = None
    MinLength: Optional[str] = None
    MaxValue: Optional[str] = None
    MinValue: Optional[str] = None


class ProductViewAggregationValueTypeDef(BaseValidatorModel):
    Value: Optional[str] = None
    ApproximateCount: Optional[int] = None


class ProvisioningParameterTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class ProvisioningPreferencesTypeDef(BaseValidatorModel):
    StackSetAccounts: Optional[Sequence[str]] = None
    StackSetRegions: Optional[Sequence[str]] = None
    StackSetFailureToleranceCount: Optional[int] = None
    StackSetFailureTolerancePercentage: Optional[int] = None
    StackSetMaxConcurrencyCount: Optional[int] = None
    StackSetMaxConcurrencyPercentage: Optional[int] = None


class RecordErrorTypeDef(BaseValidatorModel):
    Code: Optional[str] = None
    Description: Optional[str] = None


class RecordTagTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class RejectPortfolioShareInputTypeDef(BaseValidatorModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    PortfolioShareType: Optional[PortfolioShareTypeType] = None


class ResourceTargetDefinitionTypeDef(BaseValidatorModel):
    Attribute: Optional[ResourceAttributeType] = None
    Name: Optional[str] = None
    RequiresRecreation: Optional[RequiresRecreationType] = None


class SearchProductsAsAdminInputTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    PortfolioId: Optional[str] = None
    Filters: Optional[Mapping[ProductViewFilterByType, Sequence[str]]] = None
    SortBy: Optional[ProductViewSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None
    ProductSource: Optional[Literal["ACCOUNT"]] = None


class SearchProductsInputTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    Filters: Optional[Mapping[ProductViewFilterByType, Sequence[str]]] = None
    PageSize: Optional[int] = None
    SortBy: Optional[ProductViewSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    PageToken: Optional[str] = None


class ShareErrorTypeDef(BaseValidatorModel):
    Accounts: Optional[List[str]] = None
    Message: Optional[str] = None
    Error: Optional[str] = None


class TerminateProvisionedProductInputTypeDef(BaseValidatorModel):
    TerminateToken: str
    ProvisionedProductName: Optional[str] = None
    ProvisionedProductId: Optional[str] = None
    IgnoreErrors: Optional[bool] = None
    AcceptLanguage: Optional[str] = None
    RetainPhysicalResources: Optional[bool] = None


class UpdateConstraintInputTypeDef(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None
    Description: Optional[str] = None
    Parameters: Optional[str] = None


class UpdateProvisioningPreferencesTypeDef(BaseValidatorModel):
    StackSetAccounts: Optional[Sequence[str]] = None
    StackSetRegions: Optional[Sequence[str]] = None
    StackSetFailureToleranceCount: Optional[int] = None
    StackSetFailureTolerancePercentage: Optional[int] = None
    StackSetMaxConcurrencyCount: Optional[int] = None
    StackSetMaxConcurrencyPercentage: Optional[int] = None
    StackSetOperationType: Optional[StackSetOperationTypeType] = None


class UpdateProvisionedProductPropertiesInputTypeDef(BaseValidatorModel):
    ProvisionedProductId: str
    ProvisionedProductProperties: Mapping[PropertyKeyType, str]
    IdempotencyToken: str
    AcceptLanguage: Optional[str] = None


class UpdateProvisioningArtifactInputTypeDef(BaseValidatorModel):
    ProductId: str
    ProvisioningArtifactId: str
    AcceptLanguage: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Active: Optional[bool] = None
    Guidance: Optional[ProvisioningArtifactGuidanceType] = None


class UpdateServiceActionInputTypeDef(BaseValidatorModel):
    Id: str
    Name: Optional[str] = None
    Definition: Optional[Mapping[ServiceActionDefinitionKeyType, str]] = None
    Description: Optional[str] = None
    AcceptLanguage: Optional[str] = None


class UpdateTagOptionInputTypeDef(BaseValidatorModel):
    Id: str
    Value: Optional[str] = None
    Active: Optional[bool] = None


class ListProvisionedProductPlansInputTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    ProvisionProductId: Optional[str] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None
    AccessLevelFilter: Optional[AccessLevelFilterTypeDef] = None


class ScanProvisionedProductsInputTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    AccessLevelFilter: Optional[AccessLevelFilterTypeDef] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None


class SearchProvisionedProductsInputTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    AccessLevelFilter: Optional[AccessLevelFilterTypeDef] = None
    Filters: Optional[Mapping[Literal["SearchQuery"], Sequence[str]]] = None
    SortBy: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None


class BatchAssociateServiceActionWithProvisioningArtifactInputTypeDef(BaseValidatorModel):
    ServiceActionAssociations: Sequence[ServiceActionAssociationTypeDef]
    AcceptLanguage: Optional[str] = None


class BatchDisassociateServiceActionFromProvisioningArtifactInputTypeDef(BaseValidatorModel):
    ServiceActionAssociations: Sequence[ServiceActionAssociationTypeDef]
    AcceptLanguage: Optional[str] = None


class BatchAssociateServiceActionWithProvisioningArtifactOutputTypeDef(BaseValidatorModel):
    FailedServiceActionAssociations: List[FailedServiceActionAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchDisassociateServiceActionFromProvisioningArtifactOutputTypeDef(BaseValidatorModel):
    FailedServiceActionAssociations: List[FailedServiceActionAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CopyProductOutputTypeDef(BaseValidatorModel):
    CopyProductToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreatePortfolioShareOutputTypeDef(BaseValidatorModel):
    PortfolioShareToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateProvisionedProductPlanOutputTypeDef(BaseValidatorModel):
    PlanName: str
    PlanId: str
    ProvisionProductId: str
    ProvisionedProductName: str
    ProvisioningArtifactId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeletePortfolioShareOutputTypeDef(BaseValidatorModel):
    PortfolioShareToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeCopyProductStatusOutputTypeDef(BaseValidatorModel):
    CopyProductStatus: CopyProductStatusType
    TargetProductId: str
    StatusDetail: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetAWSOrganizationsAccessStatusOutputTypeDef(BaseValidatorModel):
    AccessStatus: AccessStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class ListPortfolioAccessOutputTypeDef(BaseValidatorModel):
    AccountIds: List[str]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePortfolioShareOutputTypeDef(BaseValidatorModel):
    PortfolioShareToken: str
    Status: ShareStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateProvisionedProductPropertiesOutputTypeDef(BaseValidatorModel):
    ProvisionedProductId: str
    ProvisionedProductProperties: Dict[PropertyKeyType, str]
    RecordId: str
    Status: RecordStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class ListBudgetsForResourceOutputTypeDef(BaseValidatorModel):
    Budgets: List[BudgetDetailTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class SourceConnectionParametersTypeDef(BaseValidatorModel):
    CodeStar: Optional[CodeStarParametersTypeDef] = None


class ConstraintDetailTypeDef(BaseValidatorModel):
    pass


class CreateConstraintOutputTypeDef(BaseValidatorModel):
    ConstraintDetail: ConstraintDetailTypeDef
    ConstraintParameters: str
    Status: StatusType
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeConstraintOutputTypeDef(BaseValidatorModel):
    ConstraintDetail: ConstraintDetailTypeDef
    ConstraintParameters: str
    Status: StatusType
    ResponseMetadata: ResponseMetadataTypeDef


class ListConstraintsForPortfolioOutputTypeDef(BaseValidatorModel):
    ConstraintDetails: List[ConstraintDetailTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateConstraintOutputTypeDef(BaseValidatorModel):
    ConstraintDetail: ConstraintDetailTypeDef
    ConstraintParameters: str
    Status: StatusType
    ResponseMetadata: ResponseMetadataTypeDef


class CreatePortfolioInputTypeDef(BaseValidatorModel):
    DisplayName: str
    ProviderName: str
    IdempotencyToken: str
    AcceptLanguage: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class ConstraintSummaryTypeDef(BaseValidatorModel):
    pass


class LaunchPathSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    ConstraintSummaries: Optional[List[ConstraintSummaryTypeDef]] = None
    Tags: Optional[List[TagTypeDef]] = None
    Name: Optional[str] = None


class UpdatePortfolioInputTypeDef(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None
    DisplayName: Optional[str] = None
    Description: Optional[str] = None
    ProviderName: Optional[str] = None
    AddTags: Optional[Sequence[TagTypeDef]] = None
    RemoveTags: Optional[Sequence[str]] = None


class CreatePortfolioOutputTypeDef(BaseValidatorModel):
    PortfolioDetail: PortfolioDetailTypeDef
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListAcceptedPortfolioSharesOutputTypeDef(BaseValidatorModel):
    PortfolioDetails: List[PortfolioDetailTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListPortfoliosForProductOutputTypeDef(BaseValidatorModel):
    PortfolioDetails: List[PortfolioDetailTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListPortfoliosOutputTypeDef(BaseValidatorModel):
    PortfolioDetails: List[PortfolioDetailTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePortfolioOutputTypeDef(BaseValidatorModel):
    PortfolioDetail: PortfolioDetailTypeDef
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class OrganizationNodeTypeDef(BaseValidatorModel):
    pass


class CreatePortfolioShareInputTypeDef(BaseValidatorModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    AccountId: Optional[str] = None
    OrganizationNode: Optional[OrganizationNodeTypeDef] = None
    ShareTagOptions: Optional[bool] = None
    SharePrincipals: Optional[bool] = None


class DeletePortfolioShareInputTypeDef(BaseValidatorModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    AccountId: Optional[str] = None
    OrganizationNode: Optional[OrganizationNodeTypeDef] = None


class ListOrganizationPortfolioAccessOutputTypeDef(BaseValidatorModel):
    OrganizationNodes: List[OrganizationNodeTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePortfolioShareInputTypeDef(BaseValidatorModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    AccountId: Optional[str] = None
    OrganizationNode: Optional[OrganizationNodeTypeDef] = None
    ShareTagOptions: Optional[bool] = None
    SharePrincipals: Optional[bool] = None


class ProvisioningArtifactPropertiesTypeDef(BaseValidatorModel):
    pass


class CreateProvisioningArtifactInputTypeDef(BaseValidatorModel):
    ProductId: str
    Parameters: ProvisioningArtifactPropertiesTypeDef
    IdempotencyToken: str
    AcceptLanguage: Optional[str] = None


class ProvisioningArtifactDetailTypeDef(BaseValidatorModel):
    pass


class CreateProvisioningArtifactOutputTypeDef(BaseValidatorModel):
    ProvisioningArtifactDetail: ProvisioningArtifactDetailTypeDef
    Info: Dict[str, str]
    Status: StatusType
    ResponseMetadata: ResponseMetadataTypeDef


class ListProvisioningArtifactsOutputTypeDef(BaseValidatorModel):
    ProvisioningArtifactDetails: List[ProvisioningArtifactDetailTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateProvisioningArtifactOutputTypeDef(BaseValidatorModel):
    ProvisioningArtifactDetail: ProvisioningArtifactDetailTypeDef
    Info: Dict[str, str]
    Status: StatusType
    ResponseMetadata: ResponseMetadataTypeDef


class CreateProvisionedProductPlanInputTypeDef(BaseValidatorModel):
    PlanName: str
    PlanType: Literal["CLOUDFORMATION"]
    ProductId: str
    ProvisionedProductName: str
    ProvisioningArtifactId: str
    IdempotencyToken: str
    AcceptLanguage: Optional[str] = None
    NotificationArns: Optional[Sequence[str]] = None
    PathId: Optional[str] = None
    ProvisioningParameters: Optional[Sequence[UpdateProvisioningParameterTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class ProvisionedProductPlanDetailsTypeDef(BaseValidatorModel):
    CreatedTime: Optional[datetime] = None
    PathId: Optional[str] = None
    ProductId: Optional[str] = None
    PlanName: Optional[str] = None
    PlanId: Optional[str] = None
    ProvisionProductId: Optional[str] = None
    ProvisionProductName: Optional[str] = None
    PlanType: Optional[Literal["CLOUDFORMATION"]] = None
    ProvisioningArtifactId: Optional[str] = None
    Status: Optional[ProvisionedProductPlanStatusType] = None
    UpdatedTime: Optional[datetime] = None
    NotificationArns: Optional[List[str]] = None
    ProvisioningParameters: Optional[List[UpdateProvisioningParameterTypeDef]] = None
    Tags: Optional[List[TagTypeDef]] = None
    StatusMessage: Optional[str] = None


class CreateTagOptionOutputTypeDef(BaseValidatorModel):
    TagOptionDetail: TagOptionDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribePortfolioOutputTypeDef(BaseValidatorModel):
    PortfolioDetail: PortfolioDetailTypeDef
    Tags: List[TagTypeDef]
    TagOptions: List[TagOptionDetailTypeDef]
    Budgets: List[BudgetDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeTagOptionOutputTypeDef(BaseValidatorModel):
    TagOptionDetail: TagOptionDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagOptionsOutputTypeDef(BaseValidatorModel):
    TagOptionDetails: List[TagOptionDetailTypeDef]
    PageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateTagOptionOutputTypeDef(BaseValidatorModel):
    TagOptionDetail: TagOptionDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PortfolioShareDetailTypeDef(BaseValidatorModel):
    pass


class DescribePortfolioSharesOutputTypeDef(BaseValidatorModel):
    NextPageToken: str
    PortfolioShareDetails: List[PortfolioShareDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ProductViewSummaryTypeDef(BaseValidatorModel):
    pass


class DescribeProductOutputTypeDef(BaseValidatorModel):
    ProductViewSummary: ProductViewSummaryTypeDef
    ProvisioningArtifacts: List[ProvisioningArtifactTypeDef]
    Budgets: List[BudgetDetailTypeDef]
    LaunchPaths: List[LaunchPathTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeProductViewOutputTypeDef(BaseValidatorModel):
    ProductViewSummary: ProductViewSummaryTypeDef
    ProvisioningArtifacts: List[ProvisioningArtifactTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ProvisioningArtifactViewTypeDef(BaseValidatorModel):
    ProductViewSummary: Optional[ProductViewSummaryTypeDef] = None
    ProvisioningArtifact: Optional[ProvisioningArtifactTypeDef] = None


class ProvisionedProductDetailTypeDef(BaseValidatorModel):
    pass


class DescribeProvisionedProductOutputTypeDef(BaseValidatorModel):
    ProvisionedProductDetail: ProvisionedProductDetailTypeDef
    CloudWatchDashboards: List[CloudWatchDashboardTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ScanProvisionedProductsOutputTypeDef(BaseValidatorModel):
    ProvisionedProducts: List[ProvisionedProductDetailTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetProvisionedProductOutputsOutputTypeDef(BaseValidatorModel):
    Outputs: List[RecordOutputTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class NotifyUpdateProvisionedProductEngineWorkflowResultInputTypeDef(BaseValidatorModel):
    WorkflowToken: str
    RecordId: str
    Status: EngineWorkflowStatusType
    IdempotencyToken: str
    FailureReason: Optional[str] = None
    Outputs: Optional[Sequence[RecordOutputTypeDef]] = None


class ExecutionParameterTypeDef(BaseValidatorModel):
    pass


class DescribeServiceActionExecutionParametersOutputTypeDef(BaseValidatorModel):
    ServiceActionParameters: List[ExecutionParameterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class EngineWorkflowResourceIdentifierTypeDef(BaseValidatorModel):
    UniqueTag: Optional[UniqueTagResourceIdentifierTypeDef] = None


class ListAcceptedPortfolioSharesInputPaginateTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    PortfolioShareType: Optional[PortfolioShareTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListConstraintsForPortfolioInputPaginateTypeDef(BaseValidatorModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    ProductId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListLaunchPathsInputPaginateTypeDef(BaseValidatorModel):
    ProductId: str
    AcceptLanguage: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListOrganizationPortfolioAccessInputPaginateTypeDef(BaseValidatorModel):
    PortfolioId: str
    OrganizationNodeType: OrganizationNodeTypeType
    AcceptLanguage: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPortfoliosForProductInputPaginateTypeDef(BaseValidatorModel):
    ProductId: str
    AcceptLanguage: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPortfoliosInputPaginateTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPrincipalsForPortfolioInputPaginateTypeDef(BaseValidatorModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListProvisionedProductPlansInputPaginateTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    ProvisionProductId: Optional[str] = None
    AccessLevelFilter: Optional[AccessLevelFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListProvisioningArtifactsForServiceActionInputPaginateTypeDef(BaseValidatorModel):
    ServiceActionId: str
    AcceptLanguage: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResourcesForTagOptionInputPaginateTypeDef(BaseValidatorModel):
    TagOptionId: str
    ResourceType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListServiceActionsForProvisioningArtifactInputPaginateTypeDef(BaseValidatorModel):
    ProductId: str
    ProvisioningArtifactId: str
    AcceptLanguage: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListServiceActionsInputPaginateTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ScanProvisionedProductsInputPaginateTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    AccessLevelFilter: Optional[AccessLevelFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchProductsAsAdminInputPaginateTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    PortfolioId: Optional[str] = None
    Filters: Optional[Mapping[ProductViewFilterByType, Sequence[str]]] = None
    SortBy: Optional[ProductViewSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    ProductSource: Optional[Literal["ACCOUNT"]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPrincipalsForPortfolioOutputTypeDef(BaseValidatorModel):
    Principals: List[PrincipalTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListProvisionedProductPlansOutputTypeDef(BaseValidatorModel):
    ProvisionedProductPlans: List[ProvisionedProductPlanSummaryTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListRecordHistoryInputPaginateTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    AccessLevelFilter: Optional[AccessLevelFilterTypeDef] = None
    SearchFilter: Optional[ListRecordHistorySearchFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRecordHistoryInputTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    AccessLevelFilter: Optional[AccessLevelFilterTypeDef] = None
    SearchFilter: Optional[ListRecordHistorySearchFilterTypeDef] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None


class ListResourcesForTagOptionOutputTypeDef(BaseValidatorModel):
    ResourceDetails: List[ResourceDetailTypeDef]
    PageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListServiceActionsForProvisioningArtifactOutputTypeDef(BaseValidatorModel):
    ServiceActionSummaries: List[ServiceActionSummaryTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListServiceActionsOutputTypeDef(BaseValidatorModel):
    ServiceActionSummaries: List[ServiceActionSummaryTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class ServiceActionDetailTypeDef(BaseValidatorModel):
    ServiceActionSummary: Optional[ServiceActionSummaryTypeDef] = None
    Definition: Optional[Dict[ServiceActionDefinitionKeyType, str]] = None


class ListStackInstancesForProvisionedProductOutputTypeDef(BaseValidatorModel):
    StackInstances: List[StackInstanceTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagOptionsInputPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[ListTagOptionsFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTagOptionsInputTypeDef(BaseValidatorModel):
    Filters: Optional[ListTagOptionsFiltersTypeDef] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None


class ProvisioningArtifactParameterTypeDef(BaseValidatorModel):
    ParameterKey: Optional[str] = None
    DefaultValue: Optional[str] = None
    ParameterType: Optional[str] = None
    IsNoEcho: Optional[bool] = None
    Description: Optional[str] = None
    ParameterConstraints: Optional[ParameterConstraintsTypeDef] = None


class SearchProductsOutputTypeDef(BaseValidatorModel):
    ProductViewSummaries: List[ProductViewSummaryTypeDef]
    ProductViewAggregations: Dict[str, List[ProductViewAggregationValueTypeDef]]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class ProvisionProductInputTypeDef(BaseValidatorModel):
    ProvisionedProductName: str
    ProvisionToken: str
    AcceptLanguage: Optional[str] = None
    ProductId: Optional[str] = None
    ProductName: Optional[str] = None
    ProvisioningArtifactId: Optional[str] = None
    ProvisioningArtifactName: Optional[str] = None
    PathId: Optional[str] = None
    PathName: Optional[str] = None
    ProvisioningParameters: Optional[Sequence[ProvisioningParameterTypeDef]] = None
    ProvisioningPreferences: Optional[ProvisioningPreferencesTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    NotificationArns: Optional[Sequence[str]] = None


class RecordDetailTypeDef(BaseValidatorModel):
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
    RecordErrors: Optional[List[RecordErrorTypeDef]] = None
    RecordTags: Optional[List[RecordTagTypeDef]] = None
    LaunchRoleArn: Optional[str] = None


class ResourceChangeDetailTypeDef(BaseValidatorModel):
    Target: Optional[ResourceTargetDefinitionTypeDef] = None
    Evaluation: Optional[EvaluationTypeType] = None
    CausingEntity: Optional[str] = None


class ShareDetailsTypeDef(BaseValidatorModel):
    SuccessfulShares: Optional[List[str]] = None
    ShareErrors: Optional[List[ShareErrorTypeDef]] = None


class UpdateProvisionedProductInputTypeDef(BaseValidatorModel):
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
    ProvisioningParameters: Optional[Sequence[UpdateProvisioningParameterTypeDef]] = None
    ProvisioningPreferences: Optional[UpdateProvisioningPreferencesTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class ListLaunchPathsOutputTypeDef(BaseValidatorModel):
    LaunchPathSummaries: List[LaunchPathSummaryTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class ProvisionedProductAttributeTypeDef(BaseValidatorModel):
    pass


class SearchProvisionedProductsOutputTypeDef(BaseValidatorModel):
    ProvisionedProducts: List[ProvisionedProductAttributeTypeDef]
    TotalResultsCount: int
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListProvisioningArtifactsForServiceActionOutputTypeDef(BaseValidatorModel):
    ProvisioningArtifactViews: List[ProvisioningArtifactViewTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class NotifyProvisionProductEngineWorkflowResultInputTypeDef(BaseValidatorModel):
    WorkflowToken: str
    RecordId: str
    Status: EngineWorkflowStatusType
    IdempotencyToken: str
    FailureReason: Optional[str] = None
    ResourceIdentifier: Optional[EngineWorkflowResourceIdentifierTypeDef] = None
    Outputs: Optional[Sequence[RecordOutputTypeDef]] = None


class CreateServiceActionOutputTypeDef(BaseValidatorModel):
    ServiceActionDetail: ServiceActionDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeServiceActionOutputTypeDef(BaseValidatorModel):
    ServiceActionDetail: ServiceActionDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateServiceActionOutputTypeDef(BaseValidatorModel):
    ServiceActionDetail: ServiceActionDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeProvisioningArtifactOutputTypeDef(BaseValidatorModel):
    ProvisioningArtifactDetail: ProvisioningArtifactDetailTypeDef
    Info: Dict[str, str]
    Status: StatusType
    ProvisioningArtifactParameters: List[ProvisioningArtifactParameterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UsageInstructionTypeDef(BaseValidatorModel):
    pass


class DescribeProvisioningParametersOutputTypeDef(BaseValidatorModel):
    ProvisioningArtifactParameters: List[ProvisioningArtifactParameterTypeDef]
    ConstraintSummaries: List[ConstraintSummaryTypeDef]
    UsageInstructions: List[UsageInstructionTypeDef]
    TagOptions: List[TagOptionSummaryTypeDef]
    ProvisioningArtifactPreferences: ProvisioningArtifactPreferencesTypeDef
    ProvisioningArtifactOutputs: List[ProvisioningArtifactOutputTypeDef]
    ProvisioningArtifactOutputKeys: List[ProvisioningArtifactOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeRecordOutputTypeDef(BaseValidatorModel):
    RecordDetail: RecordDetailTypeDef
    RecordOutputs: List[RecordOutputTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class ExecuteProvisionedProductPlanOutputTypeDef(BaseValidatorModel):
    RecordDetail: RecordDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ExecuteProvisionedProductServiceActionOutputTypeDef(BaseValidatorModel):
    RecordDetail: RecordDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ImportAsProvisionedProductOutputTypeDef(BaseValidatorModel):
    RecordDetail: RecordDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListRecordHistoryOutputTypeDef(BaseValidatorModel):
    RecordDetails: List[RecordDetailTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class ProvisionProductOutputTypeDef(BaseValidatorModel):
    RecordDetail: RecordDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class TerminateProvisionedProductOutputTypeDef(BaseValidatorModel):
    RecordDetail: RecordDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateProvisionedProductOutputTypeDef(BaseValidatorModel):
    RecordDetail: RecordDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ResourceChangeTypeDef(BaseValidatorModel):
    Action: Optional[ChangeActionType] = None
    LogicalResourceId: Optional[str] = None
    PhysicalResourceId: Optional[str] = None
    ResourceType: Optional[str] = None
    Replacement: Optional[ReplacementType] = None
    Scope: Optional[List[ResourceAttributeType]] = None
    Details: Optional[List[ResourceChangeDetailTypeDef]] = None


class DescribePortfolioShareStatusOutputTypeDef(BaseValidatorModel):
    PortfolioShareToken: str
    PortfolioId: str
    OrganizationNodeValue: str
    Status: ShareStatusType
    ShareDetails: ShareDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SourceConnectionDetailTypeDef(BaseValidatorModel):
    pass


class ProductViewDetailTypeDef(BaseValidatorModel):
    ProductViewSummary: Optional[ProductViewSummaryTypeDef] = None
    Status: Optional[StatusType] = None
    ProductARN: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    SourceConnection: Optional[SourceConnectionDetailTypeDef] = None


class SourceConnectionTypeDef(BaseValidatorModel):
    pass


class CreateProductInputTypeDef(BaseValidatorModel):
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
    Tags: Optional[Sequence[TagTypeDef]] = None
    ProvisioningArtifactParameters: Optional[ProvisioningArtifactPropertiesTypeDef] = None
    SourceConnection: Optional[SourceConnectionTypeDef] = None


class UpdateProductInputTypeDef(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None
    Name: Optional[str] = None
    Owner: Optional[str] = None
    Description: Optional[str] = None
    Distributor: Optional[str] = None
    SupportDescription: Optional[str] = None
    SupportEmail: Optional[str] = None
    SupportUrl: Optional[str] = None
    AddTags: Optional[Sequence[TagTypeDef]] = None
    RemoveTags: Optional[Sequence[str]] = None
    SourceConnection: Optional[SourceConnectionTypeDef] = None


class DescribeProvisionedProductPlanOutputTypeDef(BaseValidatorModel):
    ProvisionedProductPlanDetails: ProvisionedProductPlanDetailsTypeDef
    ResourceChanges: List[ResourceChangeTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateProductOutputTypeDef(BaseValidatorModel):
    ProductViewDetail: ProductViewDetailTypeDef
    ProvisioningArtifactDetail: ProvisioningArtifactDetailTypeDef
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeProductAsAdminOutputTypeDef(BaseValidatorModel):
    ProductViewDetail: ProductViewDetailTypeDef
    ProvisioningArtifactSummaries: List[ProvisioningArtifactSummaryTypeDef]
    Tags: List[TagTypeDef]
    TagOptions: List[TagOptionDetailTypeDef]
    Budgets: List[BudgetDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class SearchProductsAsAdminOutputTypeDef(BaseValidatorModel):
    ProductViewDetails: List[ProductViewDetailTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateProductOutputTypeDef(BaseValidatorModel):
    ProductViewDetail: ProductViewDetailTypeDef
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef



from datetime import datetime
from pydantic import BaseModel
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

class AcceptPortfolioShareInputRequestTypeDef(BaseModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    PortfolioShareType: Optional[PortfolioShareTypeType] = None

class AccessLevelFilterTypeDef(BaseModel):
    Key: Optional[AccessLevelFilterKeyType] = None
    Value: Optional[str] = None

class AssociateBudgetWithResourceInputRequestTypeDef(BaseModel):
    BudgetName: str
    ResourceId: str

class AssociatePrincipalWithPortfolioInputRequestTypeDef(BaseModel):
    PortfolioId: str
    PrincipalARN: str
    PrincipalType: PrincipalTypeType
    AcceptLanguage: Optional[str] = None

class AssociateProductWithPortfolioInputRequestTypeDef(BaseModel):
    ProductId: str
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    SourcePortfolioId: Optional[str] = None

class AssociateServiceActionWithProvisioningArtifactInputRequestTypeDef(BaseModel):
    ProductId: str
    ProvisioningArtifactId: str
    ServiceActionId: str
    AcceptLanguage: Optional[str] = None
    IdempotencyToken: Optional[str] = None

class AssociateTagOptionWithResourceInputRequestTypeDef(BaseModel):
    ResourceId: str
    TagOptionId: str

class ServiceActionAssociationTypeDef(BaseModel):
    ServiceActionId: str
    ProductId: str
    ProvisioningArtifactId: str

class FailedServiceActionAssociationTypeDef(BaseModel):
    ServiceActionId: Optional[str] = None
    ProductId: Optional[str] = None
    ProvisioningArtifactId: Optional[str] = None
    ErrorCode: Optional[ServiceActionAssociationErrorCodeType] = None
    ErrorMessage: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class BudgetDetailTypeDef(BaseModel):
    BudgetName: Optional[str] = None

class CloudWatchDashboardTypeDef(BaseModel):
    Name: Optional[str] = None

class CodeStarParametersTypeDef(BaseModel):
    ConnectionArn: str
    Repository: str
    Branch: str
    ArtifactPath: str

class ConstraintDetailTypeDef(BaseModel):
    ConstraintId: Optional[str] = None
    Type: Optional[str] = None
    Description: Optional[str] = None
    Owner: Optional[str] = None
    ProductId: Optional[str] = None
    PortfolioId: Optional[str] = None

class ConstraintSummaryTypeDef(BaseModel):
    Type: Optional[str] = None
    Description: Optional[str] = None

class CopyProductInputRequestTypeDef(BaseModel):
    SourceProductArn: str
    IdempotencyToken: str
    AcceptLanguage: Optional[str] = None
    TargetProductId: Optional[str] = None
    TargetProductName: Optional[str] = None
    SourceProvisioningArtifactIdentifiers: Optional[Sequence[Mapping[Literal["Id"], str]]] = None
    CopyOptions: Optional[Sequence[Literal["CopyTags"]]] = None

class CreateConstraintInputRequestTypeDef(BaseModel):
    PortfolioId: str
    ProductId: str
    Parameters: str
    Type: str
    IdempotencyToken: str
    AcceptLanguage: Optional[str] = None
    Description: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class PortfolioDetailTypeDef(BaseModel):
    Id: Optional[str] = None
    ARN: Optional[str] = None
    DisplayName: Optional[str] = None
    Description: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    ProviderName: Optional[str] = None

class OrganizationNodeTypeDef(BaseModel):
    Type: Optional[OrganizationNodeTypeType] = None
    Value: Optional[str] = None

class ProvisioningArtifactPropertiesTypeDef(BaseModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    Info: Optional[Mapping[str, str]] = None
    Type: Optional[ProvisioningArtifactTypeType] = None
    DisableTemplateValidation: Optional[bool] = None

class ProvisioningArtifactDetailTypeDef(BaseModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Type: Optional[ProvisioningArtifactTypeType] = None
    CreatedTime: Optional[datetime] = None
    Active: Optional[bool] = None
    Guidance: Optional[ProvisioningArtifactGuidanceType] = None
    SourceRevision: Optional[str] = None

class UpdateProvisioningParameterTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    UsePreviousValue: Optional[bool] = None

class CreateServiceActionInputRequestTypeDef(BaseModel):
    Name: str
    DefinitionType: Literal["SSM_AUTOMATION"]
    Definition: Mapping[ServiceActionDefinitionKeyType, str]
    IdempotencyToken: str
    Description: Optional[str] = None
    AcceptLanguage: Optional[str] = None

class CreateTagOptionInputRequestTypeDef(BaseModel):
    Key: str
    Value: str

class TagOptionDetailTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    Active: Optional[bool] = None
    Id: Optional[str] = None
    Owner: Optional[str] = None

class DeleteConstraintInputRequestTypeDef(BaseModel):
    Id: str
    AcceptLanguage: Optional[str] = None

class DeletePortfolioInputRequestTypeDef(BaseModel):
    Id: str
    AcceptLanguage: Optional[str] = None

class DeleteProductInputRequestTypeDef(BaseModel):
    Id: str
    AcceptLanguage: Optional[str] = None

class DeleteProvisionedProductPlanInputRequestTypeDef(BaseModel):
    PlanId: str
    AcceptLanguage: Optional[str] = None
    IgnoreErrors: Optional[bool] = None

class DeleteProvisioningArtifactInputRequestTypeDef(BaseModel):
    ProductId: str
    ProvisioningArtifactId: str
    AcceptLanguage: Optional[str] = None

class DeleteServiceActionInputRequestTypeDef(BaseModel):
    Id: str
    AcceptLanguage: Optional[str] = None
    IdempotencyToken: Optional[str] = None

class DeleteTagOptionInputRequestTypeDef(BaseModel):
    Id: str

class DescribeConstraintInputRequestTypeDef(BaseModel):
    Id: str
    AcceptLanguage: Optional[str] = None

class DescribeCopyProductStatusInputRequestTypeDef(BaseModel):
    CopyProductToken: str
    AcceptLanguage: Optional[str] = None

class DescribePortfolioInputRequestTypeDef(BaseModel):
    Id: str
    AcceptLanguage: Optional[str] = None

class DescribePortfolioShareStatusInputRequestTypeDef(BaseModel):
    PortfolioShareToken: str

class DescribePortfolioSharesInputRequestTypeDef(BaseModel):
    PortfolioId: str
    Type: DescribePortfolioShareTypeType
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None

class PortfolioShareDetailTypeDef(BaseModel):
    PrincipalId: Optional[str] = None
    Type: Optional[DescribePortfolioShareTypeType] = None
    Accepted: Optional[bool] = None
    ShareTagOptions: Optional[bool] = None
    SharePrincipals: Optional[bool] = None

class DescribeProductAsAdminInputRequestTypeDef(BaseModel):
    AcceptLanguage: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    SourcePortfolioId: Optional[str] = None

class ProvisioningArtifactSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    ProvisioningArtifactMetadata: Optional[Dict[str, str]] = None

class DescribeProductInputRequestTypeDef(BaseModel):
    AcceptLanguage: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None

class LaunchPathTypeDef(BaseModel):
    Id: Optional[str] = None
    Name: Optional[str] = None

class ProductViewSummaryTypeDef(BaseModel):
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

class ProvisioningArtifactTypeDef(BaseModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    Guidance: Optional[ProvisioningArtifactGuidanceType] = None

class DescribeProductViewInputRequestTypeDef(BaseModel):
    Id: str
    AcceptLanguage: Optional[str] = None

class DescribeProvisionedProductInputRequestTypeDef(BaseModel):
    AcceptLanguage: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None

class ProvisionedProductDetailTypeDef(BaseModel):
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

class DescribeProvisionedProductPlanInputRequestTypeDef(BaseModel):
    PlanId: str
    AcceptLanguage: Optional[str] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None

class DescribeProvisioningArtifactInputRequestTypeDef(BaseModel):
    AcceptLanguage: Optional[str] = None
    ProvisioningArtifactId: Optional[str] = None
    ProductId: Optional[str] = None
    ProvisioningArtifactName: Optional[str] = None
    ProductName: Optional[str] = None
    Verbose: Optional[bool] = None
    IncludeProvisioningArtifactParameters: Optional[bool] = None

class DescribeProvisioningParametersInputRequestTypeDef(BaseModel):
    AcceptLanguage: Optional[str] = None
    ProductId: Optional[str] = None
    ProductName: Optional[str] = None
    ProvisioningArtifactId: Optional[str] = None
    ProvisioningArtifactName: Optional[str] = None
    PathId: Optional[str] = None
    PathName: Optional[str] = None

class ProvisioningArtifactOutputTypeDef(BaseModel):
    Key: Optional[str] = None
    Description: Optional[str] = None

class ProvisioningArtifactPreferencesTypeDef(BaseModel):
    StackSetAccounts: Optional[List[str]] = None
    StackSetRegions: Optional[List[str]] = None

class TagOptionSummaryTypeDef(BaseModel):
    Key: Optional[str] = None
    Values: Optional[List[str]] = None

class UsageInstructionTypeDef(BaseModel):
    Type: Optional[str] = None
    Value: Optional[str] = None

class DescribeRecordInputRequestTypeDef(BaseModel):
    Id: str
    AcceptLanguage: Optional[str] = None
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None

class RecordOutputTypeDef(BaseModel):
    OutputKey: Optional[str] = None
    OutputValue: Optional[str] = None
    Description: Optional[str] = None

class DescribeServiceActionExecutionParametersInputRequestTypeDef(BaseModel):
    ProvisionedProductId: str
    ServiceActionId: str
    AcceptLanguage: Optional[str] = None

class ExecutionParameterTypeDef(BaseModel):
    Name: Optional[str] = None
    Type: Optional[str] = None
    DefaultValues: Optional[List[str]] = None

class DescribeServiceActionInputRequestTypeDef(BaseModel):
    Id: str
    AcceptLanguage: Optional[str] = None

class DescribeTagOptionInputRequestTypeDef(BaseModel):
    Id: str

class DisassociateBudgetFromResourceInputRequestTypeDef(BaseModel):
    BudgetName: str
    ResourceId: str

class DisassociatePrincipalFromPortfolioInputRequestTypeDef(BaseModel):
    PortfolioId: str
    PrincipalARN: str
    AcceptLanguage: Optional[str] = None
    PrincipalType: Optional[PrincipalTypeType] = None

class DisassociateProductFromPortfolioInputRequestTypeDef(BaseModel):
    ProductId: str
    PortfolioId: str
    AcceptLanguage: Optional[str] = None

class DisassociateServiceActionFromProvisioningArtifactInputRequestTypeDef(BaseModel):
    ProductId: str
    ProvisioningArtifactId: str
    ServiceActionId: str
    AcceptLanguage: Optional[str] = None
    IdempotencyToken: Optional[str] = None

class DisassociateTagOptionFromResourceInputRequestTypeDef(BaseModel):
    ResourceId: str
    TagOptionId: str

class UniqueTagResourceIdentifierTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class ExecuteProvisionedProductPlanInputRequestTypeDef(BaseModel):
    PlanId: str
    IdempotencyToken: str
    AcceptLanguage: Optional[str] = None

class ExecuteProvisionedProductServiceActionInputRequestTypeDef(BaseModel):
    ProvisionedProductId: str
    ServiceActionId: str
    ExecuteToken: str
    AcceptLanguage: Optional[str] = None
    Parameters: Optional[Mapping[str, Sequence[str]]] = None

class GetProvisionedProductOutputsInputRequestTypeDef(BaseModel):
    AcceptLanguage: Optional[str] = None
    ProvisionedProductId: Optional[str] = None
    ProvisionedProductName: Optional[str] = None
    OutputKeys: Optional[Sequence[str]] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None

class ImportAsProvisionedProductInputRequestTypeDef(BaseModel):
    ProductId: str
    ProvisioningArtifactId: str
    ProvisionedProductName: str
    PhysicalId: str
    IdempotencyToken: str
    AcceptLanguage: Optional[str] = None

class LastSyncTypeDef(BaseModel):
    LastSyncTime: Optional[datetime] = None
    LastSyncStatus: Optional[LastSyncStatusType] = None
    LastSyncStatusMessage: Optional[str] = None
    LastSuccessfulSyncTime: Optional[datetime] = None
    LastSuccessfulSyncProvisioningArtifactId: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAcceptedPortfolioSharesInputRequestTypeDef(BaseModel):
    AcceptLanguage: Optional[str] = None
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None
    PortfolioShareType: Optional[PortfolioShareTypeType] = None

class ListBudgetsForResourceInputRequestTypeDef(BaseModel):
    ResourceId: str
    AcceptLanguage: Optional[str] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None

class ListConstraintsForPortfolioInputRequestTypeDef(BaseModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    ProductId: Optional[str] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None

class ListLaunchPathsInputRequestTypeDef(BaseModel):
    ProductId: str
    AcceptLanguage: Optional[str] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None

class ListOrganizationPortfolioAccessInputRequestTypeDef(BaseModel):
    PortfolioId: str
    OrganizationNodeType: OrganizationNodeTypeType
    AcceptLanguage: Optional[str] = None
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None

class ListPortfolioAccessInputRequestTypeDef(BaseModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    OrganizationParentId: Optional[str] = None
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None

class ListPortfoliosForProductInputRequestTypeDef(BaseModel):
    ProductId: str
    AcceptLanguage: Optional[str] = None
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None

class ListPortfoliosInputRequestTypeDef(BaseModel):
    AcceptLanguage: Optional[str] = None
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None

class ListPrincipalsForPortfolioInputRequestTypeDef(BaseModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None

class PrincipalTypeDef(BaseModel):
    PrincipalARN: Optional[str] = None
    PrincipalType: Optional[PrincipalTypeType] = None

class ProvisionedProductPlanSummaryTypeDef(BaseModel):
    PlanName: Optional[str] = None
    PlanId: Optional[str] = None
    ProvisionProductId: Optional[str] = None
    ProvisionProductName: Optional[str] = None
    PlanType: Optional[Literal["CLOUDFORMATION"]] = None
    ProvisioningArtifactId: Optional[str] = None

class ListProvisioningArtifactsForServiceActionInputRequestTypeDef(BaseModel):
    ServiceActionId: str
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None
    AcceptLanguage: Optional[str] = None

class ListProvisioningArtifactsInputRequestTypeDef(BaseModel):
    ProductId: str
    AcceptLanguage: Optional[str] = None

class ListRecordHistorySearchFilterTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class ListResourcesForTagOptionInputRequestTypeDef(BaseModel):
    TagOptionId: str
    ResourceType: Optional[str] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None

class ResourceDetailTypeDef(BaseModel):
    Id: Optional[str] = None
    ARN: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    CreatedTime: Optional[datetime] = None

class ListServiceActionsForProvisioningArtifactInputRequestTypeDef(BaseModel):
    ProductId: str
    ProvisioningArtifactId: str
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None
    AcceptLanguage: Optional[str] = None

class ServiceActionSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    DefinitionType: Optional[Literal["SSM_AUTOMATION"]] = None

class ListServiceActionsInputRequestTypeDef(BaseModel):
    AcceptLanguage: Optional[str] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None

class ListStackInstancesForProvisionedProductInputRequestTypeDef(BaseModel):
    ProvisionedProductId: str
    AcceptLanguage: Optional[str] = None
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None

class StackInstanceTypeDef(BaseModel):
    Account: Optional[str] = None
    Region: Optional[str] = None
    StackInstanceStatus: Optional[StackInstanceStatusType] = None

class ListTagOptionsFiltersTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    Active: Optional[bool] = None

class NotifyTerminateProvisionedProductEngineWorkflowResultInputRequestTypeDef(BaseModel):
    WorkflowToken: str
    RecordId: str
    Status: EngineWorkflowStatusType
    IdempotencyToken: str
    FailureReason: Optional[str] = None

class ParameterConstraintsTypeDef(BaseModel):
    AllowedValues: Optional[List[str]] = None
    AllowedPattern: Optional[str] = None
    ConstraintDescription: Optional[str] = None
    MaxLength: Optional[str] = None
    MinLength: Optional[str] = None
    MaxValue: Optional[str] = None
    MinValue: Optional[str] = None

class ProductViewAggregationValueTypeDef(BaseModel):
    Value: Optional[str] = None
    ApproximateCount: Optional[int] = None

class ProvisioningParameterTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class ProvisioningPreferencesTypeDef(BaseModel):
    StackSetAccounts: Optional[Sequence[str]] = None
    StackSetRegions: Optional[Sequence[str]] = None
    StackSetFailureToleranceCount: Optional[int] = None
    StackSetFailureTolerancePercentage: Optional[int] = None
    StackSetMaxConcurrencyCount: Optional[int] = None
    StackSetMaxConcurrencyPercentage: Optional[int] = None

class RecordErrorTypeDef(BaseModel):
    Code: Optional[str] = None
    Description: Optional[str] = None

class RecordTagTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class RejectPortfolioShareInputRequestTypeDef(BaseModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    PortfolioShareType: Optional[PortfolioShareTypeType] = None

class ResourceTargetDefinitionTypeDef(BaseModel):
    Attribute: Optional[ResourceAttributeType] = None
    Name: Optional[str] = None
    RequiresRecreation: Optional[RequiresRecreationType] = None

class SearchProductsAsAdminInputRequestTypeDef(BaseModel):
    AcceptLanguage: Optional[str] = None
    PortfolioId: Optional[str] = None
    Filters: Optional[Mapping[ProductViewFilterByType, Sequence[str]]] = None
    SortBy: Optional[ProductViewSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None
    ProductSource: Optional[Literal["ACCOUNT"]] = None

class SearchProductsInputRequestTypeDef(BaseModel):
    AcceptLanguage: Optional[str] = None
    Filters: Optional[Mapping[ProductViewFilterByType, Sequence[str]]] = None
    PageSize: Optional[int] = None
    SortBy: Optional[ProductViewSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    PageToken: Optional[str] = None

class ShareErrorTypeDef(BaseModel):
    Accounts: Optional[List[str]] = None
    Message: Optional[str] = None
    Error: Optional[str] = None

class TerminateProvisionedProductInputRequestTypeDef(BaseModel):
    TerminateToken: str
    ProvisionedProductName: Optional[str] = None
    ProvisionedProductId: Optional[str] = None
    IgnoreErrors: Optional[bool] = None
    AcceptLanguage: Optional[str] = None
    RetainPhysicalResources: Optional[bool] = None

class UpdateConstraintInputRequestTypeDef(BaseModel):
    Id: str
    AcceptLanguage: Optional[str] = None
    Description: Optional[str] = None
    Parameters: Optional[str] = None

class UpdateProvisioningPreferencesTypeDef(BaseModel):
    StackSetAccounts: Optional[Sequence[str]] = None
    StackSetRegions: Optional[Sequence[str]] = None
    StackSetFailureToleranceCount: Optional[int] = None
    StackSetFailureTolerancePercentage: Optional[int] = None
    StackSetMaxConcurrencyCount: Optional[int] = None
    StackSetMaxConcurrencyPercentage: Optional[int] = None
    StackSetOperationType: Optional[StackSetOperationTypeType] = None

class UpdateProvisionedProductPropertiesInputRequestTypeDef(BaseModel):
    ProvisionedProductId: str
    ProvisionedProductProperties: Mapping[PropertyKeyType, str]
    IdempotencyToken: str
    AcceptLanguage: Optional[str] = None

class UpdateProvisioningArtifactInputRequestTypeDef(BaseModel):
    ProductId: str
    ProvisioningArtifactId: str
    AcceptLanguage: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Active: Optional[bool] = None
    Guidance: Optional[ProvisioningArtifactGuidanceType] = None

class UpdateServiceActionInputRequestTypeDef(BaseModel):
    Id: str
    Name: Optional[str] = None
    Definition: Optional[Mapping[ServiceActionDefinitionKeyType, str]] = None
    Description: Optional[str] = None
    AcceptLanguage: Optional[str] = None

class UpdateTagOptionInputRequestTypeDef(BaseModel):
    Id: str
    Value: Optional[str] = None
    Active: Optional[bool] = None

class ListProvisionedProductPlansInputRequestTypeDef(BaseModel):
    AcceptLanguage: Optional[str] = None
    ProvisionProductId: Optional[str] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None
    AccessLevelFilter: Optional[AccessLevelFilterTypeDef] = None

class ScanProvisionedProductsInputRequestTypeDef(BaseModel):
    AcceptLanguage: Optional[str] = None
    AccessLevelFilter: Optional[AccessLevelFilterTypeDef] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None

class SearchProvisionedProductsInputRequestTypeDef(BaseModel):
    AcceptLanguage: Optional[str] = None
    AccessLevelFilter: Optional[AccessLevelFilterTypeDef] = None
    Filters: Optional[Mapping[Literal["SearchQuery"], Sequence[str]]] = None
    SortBy: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None

class BatchAssociateServiceActionWithProvisioningArtifactInputRequestTypeDef(BaseModel):
    ServiceActionAssociations: Sequence[ServiceActionAssociationTypeDef]
    AcceptLanguage: Optional[str] = None

class BatchDisassociateServiceActionFromProvisioningArtifactInputRequestTypeDef(BaseModel):
    ServiceActionAssociations: Sequence[ServiceActionAssociationTypeDef]
    AcceptLanguage: Optional[str] = None

class BatchAssociateServiceActionWithProvisioningArtifactOutputTypeDef(BaseModel):
    FailedServiceActionAssociations: List[FailedServiceActionAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDisassociateServiceActionFromProvisioningArtifactOutputTypeDef(BaseModel):
    FailedServiceActionAssociations: List[FailedServiceActionAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CopyProductOutputTypeDef(BaseModel):
    CopyProductToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePortfolioShareOutputTypeDef(BaseModel):
    PortfolioShareToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProvisionedProductPlanOutputTypeDef(BaseModel):
    PlanName: str
    PlanId: str
    ProvisionProductId: str
    ProvisionedProductName: str
    ProvisioningArtifactId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePortfolioShareOutputTypeDef(BaseModel):
    PortfolioShareToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCopyProductStatusOutputTypeDef(BaseModel):
    CopyProductStatus: CopyProductStatusType
    TargetProductId: str
    StatusDetail: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAWSOrganizationsAccessStatusOutputTypeDef(BaseModel):
    AccessStatus: AccessStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ListPortfolioAccessOutputTypeDef(BaseModel):
    AccountIds: List[str]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePortfolioShareOutputTypeDef(BaseModel):
    PortfolioShareToken: str
    Status: ShareStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProvisionedProductPropertiesOutputTypeDef(BaseModel):
    ProvisionedProductId: str
    ProvisionedProductProperties: Dict[PropertyKeyType, str]
    RecordId: str
    Status: RecordStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ListBudgetsForResourceOutputTypeDef(BaseModel):
    Budgets: List[BudgetDetailTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SourceConnectionParametersTypeDef(BaseModel):
    CodeStar: Optional[CodeStarParametersTypeDef] = None

class CreateConstraintOutputTypeDef(BaseModel):
    ConstraintDetail: ConstraintDetailTypeDef
    ConstraintParameters: str
    Status: StatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeConstraintOutputTypeDef(BaseModel):
    ConstraintDetail: ConstraintDetailTypeDef
    ConstraintParameters: str
    Status: StatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ListConstraintsForPortfolioOutputTypeDef(BaseModel):
    ConstraintDetails: List[ConstraintDetailTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConstraintOutputTypeDef(BaseModel):
    ConstraintDetail: ConstraintDetailTypeDef
    ConstraintParameters: str
    Status: StatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePortfolioInputRequestTypeDef(BaseModel):
    DisplayName: str
    ProviderName: str
    IdempotencyToken: str
    AcceptLanguage: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class LaunchPathSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    ConstraintSummaries: Optional[List[ConstraintSummaryTypeDef]] = None
    Tags: Optional[List[TagTypeDef]] = None
    Name: Optional[str] = None

class ProvisionedProductAttributeTypeDef(BaseModel):
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
    Tags: Optional[List[TagTypeDef]] = None
    PhysicalId: Optional[str] = None
    ProductId: Optional[str] = None
    ProductName: Optional[str] = None
    ProvisioningArtifactId: Optional[str] = None
    ProvisioningArtifactName: Optional[str] = None
    UserArn: Optional[str] = None
    UserArnSession: Optional[str] = None

class UpdatePortfolioInputRequestTypeDef(BaseModel):
    Id: str
    AcceptLanguage: Optional[str] = None
    DisplayName: Optional[str] = None
    Description: Optional[str] = None
    ProviderName: Optional[str] = None
    AddTags: Optional[Sequence[TagTypeDef]] = None
    RemoveTags: Optional[Sequence[str]] = None

class CreatePortfolioOutputTypeDef(BaseModel):
    PortfolioDetail: PortfolioDetailTypeDef
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAcceptedPortfolioSharesOutputTypeDef(BaseModel):
    PortfolioDetails: List[PortfolioDetailTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPortfoliosForProductOutputTypeDef(BaseModel):
    PortfolioDetails: List[PortfolioDetailTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPortfoliosOutputTypeDef(BaseModel):
    PortfolioDetails: List[PortfolioDetailTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePortfolioOutputTypeDef(BaseModel):
    PortfolioDetail: PortfolioDetailTypeDef
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePortfolioShareInputRequestTypeDef(BaseModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    AccountId: Optional[str] = None
    OrganizationNode: Optional[OrganizationNodeTypeDef] = None
    ShareTagOptions: Optional[bool] = None
    SharePrincipals: Optional[bool] = None

class DeletePortfolioShareInputRequestTypeDef(BaseModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    AccountId: Optional[str] = None
    OrganizationNode: Optional[OrganizationNodeTypeDef] = None

class ListOrganizationPortfolioAccessOutputTypeDef(BaseModel):
    OrganizationNodes: List[OrganizationNodeTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePortfolioShareInputRequestTypeDef(BaseModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    AccountId: Optional[str] = None
    OrganizationNode: Optional[OrganizationNodeTypeDef] = None
    ShareTagOptions: Optional[bool] = None
    SharePrincipals: Optional[bool] = None

class CreateProvisioningArtifactInputRequestTypeDef(BaseModel):
    ProductId: str
    Parameters: ProvisioningArtifactPropertiesTypeDef
    IdempotencyToken: str
    AcceptLanguage: Optional[str] = None

class CreateProvisioningArtifactOutputTypeDef(BaseModel):
    ProvisioningArtifactDetail: ProvisioningArtifactDetailTypeDef
    Info: Dict[str, str]
    Status: StatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ListProvisioningArtifactsOutputTypeDef(BaseModel):
    ProvisioningArtifactDetails: List[ProvisioningArtifactDetailTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProvisioningArtifactOutputTypeDef(BaseModel):
    ProvisioningArtifactDetail: ProvisioningArtifactDetailTypeDef
    Info: Dict[str, str]
    Status: StatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProvisionedProductPlanInputRequestTypeDef(BaseModel):
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

class ProvisionedProductPlanDetailsTypeDef(BaseModel):
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

class CreateTagOptionOutputTypeDef(BaseModel):
    TagOptionDetail: TagOptionDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePortfolioOutputTypeDef(BaseModel):
    PortfolioDetail: PortfolioDetailTypeDef
    Tags: List[TagTypeDef]
    TagOptions: List[TagOptionDetailTypeDef]
    Budgets: List[BudgetDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTagOptionOutputTypeDef(BaseModel):
    TagOptionDetail: TagOptionDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagOptionsOutputTypeDef(BaseModel):
    TagOptionDetails: List[TagOptionDetailTypeDef]
    PageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTagOptionOutputTypeDef(BaseModel):
    TagOptionDetail: TagOptionDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePortfolioSharesOutputTypeDef(BaseModel):
    NextPageToken: str
    PortfolioShareDetails: List[PortfolioShareDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeProductOutputTypeDef(BaseModel):
    ProductViewSummary: ProductViewSummaryTypeDef
    ProvisioningArtifacts: List[ProvisioningArtifactTypeDef]
    Budgets: List[BudgetDetailTypeDef]
    LaunchPaths: List[LaunchPathTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeProductViewOutputTypeDef(BaseModel):
    ProductViewSummary: ProductViewSummaryTypeDef
    ProvisioningArtifacts: List[ProvisioningArtifactTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ProvisioningArtifactViewTypeDef(BaseModel):
    ProductViewSummary: Optional[ProductViewSummaryTypeDef] = None
    ProvisioningArtifact: Optional[ProvisioningArtifactTypeDef] = None

class DescribeProvisionedProductOutputTypeDef(BaseModel):
    ProvisionedProductDetail: ProvisionedProductDetailTypeDef
    CloudWatchDashboards: List[CloudWatchDashboardTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ScanProvisionedProductsOutputTypeDef(BaseModel):
    ProvisionedProducts: List[ProvisionedProductDetailTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetProvisionedProductOutputsOutputTypeDef(BaseModel):
    Outputs: List[RecordOutputTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class NotifyUpdateProvisionedProductEngineWorkflowResultInputRequestTypeDef(BaseModel):
    WorkflowToken: str
    RecordId: str
    Status: EngineWorkflowStatusType
    IdempotencyToken: str
    FailureReason: Optional[str] = None
    Outputs: Optional[Sequence[RecordOutputTypeDef]] = None

class DescribeServiceActionExecutionParametersOutputTypeDef(BaseModel):
    ServiceActionParameters: List[ExecutionParameterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EngineWorkflowResourceIdentifierTypeDef(BaseModel):
    UniqueTag: Optional[UniqueTagResourceIdentifierTypeDef] = None

class ListAcceptedPortfolioSharesInputListAcceptedPortfolioSharesPaginateTypeDef(BaseModel):
    AcceptLanguage: Optional[str] = None
    PortfolioShareType: Optional[PortfolioShareTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConstraintsForPortfolioInputListConstraintsForPortfolioPaginateTypeDef(BaseModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    ProductId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLaunchPathsInputListLaunchPathsPaginateTypeDef(BaseModel):
    ProductId: str
    AcceptLanguage: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOrganizationPortfolioAccessInputListOrganizationPortfolioAccessPaginateTypeDef(BaseModel):
    PortfolioId: str
    OrganizationNodeType: OrganizationNodeTypeType
    AcceptLanguage: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPortfoliosForProductInputListPortfoliosForProductPaginateTypeDef(BaseModel):
    ProductId: str
    AcceptLanguage: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPortfoliosInputListPortfoliosPaginateTypeDef(BaseModel):
    AcceptLanguage: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPrincipalsForPortfolioInputListPrincipalsForPortfolioPaginateTypeDef(BaseModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProvisionedProductPlansInputListProvisionedProductPlansPaginateTypeDef(BaseModel):
    AcceptLanguage: Optional[str] = None
    ProvisionProductId: Optional[str] = None
    AccessLevelFilter: Optional[AccessLevelFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProvisioningArtifactsForServiceActionInputListProvisioningArtifactsForServiceActionPaginateTypeDef(BaseModel):
    ServiceActionId: str
    AcceptLanguage: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourcesForTagOptionInputListResourcesForTagOptionPaginateTypeDef(BaseModel):
    TagOptionId: str
    ResourceType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServiceActionsForProvisioningArtifactInputListServiceActionsForProvisioningArtifactPaginateTypeDef(BaseModel):
    ProductId: str
    ProvisioningArtifactId: str
    AcceptLanguage: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServiceActionsInputListServiceActionsPaginateTypeDef(BaseModel):
    AcceptLanguage: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ScanProvisionedProductsInputScanProvisionedProductsPaginateTypeDef(BaseModel):
    AcceptLanguage: Optional[str] = None
    AccessLevelFilter: Optional[AccessLevelFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchProductsAsAdminInputSearchProductsAsAdminPaginateTypeDef(BaseModel):
    AcceptLanguage: Optional[str] = None
    PortfolioId: Optional[str] = None
    Filters: Optional[Mapping[ProductViewFilterByType, Sequence[str]]] = None
    SortBy: Optional[ProductViewSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    ProductSource: Optional[Literal["ACCOUNT"]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPrincipalsForPortfolioOutputTypeDef(BaseModel):
    Principals: List[PrincipalTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListProvisionedProductPlansOutputTypeDef(BaseModel):
    ProvisionedProductPlans: List[ProvisionedProductPlanSummaryTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRecordHistoryInputListRecordHistoryPaginateTypeDef(BaseModel):
    AcceptLanguage: Optional[str] = None
    AccessLevelFilter: Optional[AccessLevelFilterTypeDef] = None
    SearchFilter: Optional[ListRecordHistorySearchFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRecordHistoryInputRequestTypeDef(BaseModel):
    AcceptLanguage: Optional[str] = None
    AccessLevelFilter: Optional[AccessLevelFilterTypeDef] = None
    SearchFilter: Optional[ListRecordHistorySearchFilterTypeDef] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None

class ListResourcesForTagOptionOutputTypeDef(BaseModel):
    ResourceDetails: List[ResourceDetailTypeDef]
    PageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListServiceActionsForProvisioningArtifactOutputTypeDef(BaseModel):
    ServiceActionSummaries: List[ServiceActionSummaryTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListServiceActionsOutputTypeDef(BaseModel):
    ServiceActionSummaries: List[ServiceActionSummaryTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ServiceActionDetailTypeDef(BaseModel):
    ServiceActionSummary: Optional[ServiceActionSummaryTypeDef] = None
    Definition: Optional[Dict[ServiceActionDefinitionKeyType, str]] = None

class ListStackInstancesForProvisionedProductOutputTypeDef(BaseModel):
    StackInstances: List[StackInstanceTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagOptionsInputListTagOptionsPaginateTypeDef(BaseModel):
    Filters: Optional[ListTagOptionsFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagOptionsInputRequestTypeDef(BaseModel):
    Filters: Optional[ListTagOptionsFiltersTypeDef] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None

class ProvisioningArtifactParameterTypeDef(BaseModel):
    ParameterKey: Optional[str] = None
    DefaultValue: Optional[str] = None
    ParameterType: Optional[str] = None
    IsNoEcho: Optional[bool] = None
    Description: Optional[str] = None
    ParameterConstraints: Optional[ParameterConstraintsTypeDef] = None

class SearchProductsOutputTypeDef(BaseModel):
    ProductViewSummaries: List[ProductViewSummaryTypeDef]
    ProductViewAggregations: Dict[str, List[ProductViewAggregationValueTypeDef]]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ProvisionProductInputRequestTypeDef(BaseModel):
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

class RecordDetailTypeDef(BaseModel):
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

class ResourceChangeDetailTypeDef(BaseModel):
    Target: Optional[ResourceTargetDefinitionTypeDef] = None
    Evaluation: Optional[EvaluationTypeType] = None
    CausingEntity: Optional[str] = None

class ShareDetailsTypeDef(BaseModel):
    SuccessfulShares: Optional[List[str]] = None
    ShareErrors: Optional[List[ShareErrorTypeDef]] = None

class UpdateProvisionedProductInputRequestTypeDef(BaseModel):
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

class SourceConnectionDetailTypeDef(BaseModel):
    Type: Optional[Literal["CODESTAR"]] = None
    ConnectionParameters: Optional[SourceConnectionParametersTypeDef] = None
    LastSync: Optional[LastSyncTypeDef] = None

class SourceConnectionTypeDef(BaseModel):
    ConnectionParameters: SourceConnectionParametersTypeDef
    Type: Optional[Literal["CODESTAR"]] = None

class ListLaunchPathsOutputTypeDef(BaseModel):
    LaunchPathSummaries: List[LaunchPathSummaryTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchProvisionedProductsOutputTypeDef(BaseModel):
    ProvisionedProducts: List[ProvisionedProductAttributeTypeDef]
    TotalResultsCount: int
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListProvisioningArtifactsForServiceActionOutputTypeDef(BaseModel):
    ProvisioningArtifactViews: List[ProvisioningArtifactViewTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class NotifyProvisionProductEngineWorkflowResultInputRequestTypeDef(BaseModel):
    WorkflowToken: str
    RecordId: str
    Status: EngineWorkflowStatusType
    IdempotencyToken: str
    FailureReason: Optional[str] = None
    ResourceIdentifier: Optional[EngineWorkflowResourceIdentifierTypeDef] = None
    Outputs: Optional[Sequence[RecordOutputTypeDef]] = None

class CreateServiceActionOutputTypeDef(BaseModel):
    ServiceActionDetail: ServiceActionDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeServiceActionOutputTypeDef(BaseModel):
    ServiceActionDetail: ServiceActionDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceActionOutputTypeDef(BaseModel):
    ServiceActionDetail: ServiceActionDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeProvisioningArtifactOutputTypeDef(BaseModel):
    ProvisioningArtifactDetail: ProvisioningArtifactDetailTypeDef
    Info: Dict[str, str]
    Status: StatusType
    ProvisioningArtifactParameters: List[ProvisioningArtifactParameterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeProvisioningParametersOutputTypeDef(BaseModel):
    ProvisioningArtifactParameters: List[ProvisioningArtifactParameterTypeDef]
    ConstraintSummaries: List[ConstraintSummaryTypeDef]
    UsageInstructions: List[UsageInstructionTypeDef]
    TagOptions: List[TagOptionSummaryTypeDef]
    ProvisioningArtifactPreferences: ProvisioningArtifactPreferencesTypeDef
    ProvisioningArtifactOutputs: List[ProvisioningArtifactOutputTypeDef]
    ProvisioningArtifactOutputKeys: List[ProvisioningArtifactOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRecordOutputTypeDef(BaseModel):
    RecordDetail: RecordDetailTypeDef
    RecordOutputs: List[RecordOutputTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExecuteProvisionedProductPlanOutputTypeDef(BaseModel):
    RecordDetail: RecordDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExecuteProvisionedProductServiceActionOutputTypeDef(BaseModel):
    RecordDetail: RecordDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ImportAsProvisionedProductOutputTypeDef(BaseModel):
    RecordDetail: RecordDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRecordHistoryOutputTypeDef(BaseModel):
    RecordDetails: List[RecordDetailTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ProvisionProductOutputTypeDef(BaseModel):
    RecordDetail: RecordDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TerminateProvisionedProductOutputTypeDef(BaseModel):
    RecordDetail: RecordDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProvisionedProductOutputTypeDef(BaseModel):
    RecordDetail: RecordDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ResourceChangeTypeDef(BaseModel):
    Action: Optional[ChangeActionType] = None
    LogicalResourceId: Optional[str] = None
    PhysicalResourceId: Optional[str] = None
    ResourceType: Optional[str] = None
    Replacement: Optional[ReplacementType] = None
    Scope: Optional[List[ResourceAttributeType]] = None
    Details: Optional[List[ResourceChangeDetailTypeDef]] = None

class DescribePortfolioShareStatusOutputTypeDef(BaseModel):
    PortfolioShareToken: str
    PortfolioId: str
    OrganizationNodeValue: str
    Status: ShareStatusType
    ShareDetails: ShareDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ProductViewDetailTypeDef(BaseModel):
    ProductViewSummary: Optional[ProductViewSummaryTypeDef] = None
    Status: Optional[StatusType] = None
    ProductARN: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    SourceConnection: Optional[SourceConnectionDetailTypeDef] = None

class CreateProductInputRequestTypeDef(BaseModel):
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

class UpdateProductInputRequestTypeDef(BaseModel):
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

class DescribeProvisionedProductPlanOutputTypeDef(BaseModel):
    ProvisionedProductPlanDetails: ProvisionedProductPlanDetailsTypeDef
    ResourceChanges: List[ResourceChangeTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProductOutputTypeDef(BaseModel):
    ProductViewDetail: ProductViewDetailTypeDef
    ProvisioningArtifactDetail: ProvisioningArtifactDetailTypeDef
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeProductAsAdminOutputTypeDef(BaseModel):
    ProductViewDetail: ProductViewDetailTypeDef
    ProvisioningArtifactSummaries: List[ProvisioningArtifactSummaryTypeDef]
    Tags: List[TagTypeDef]
    TagOptions: List[TagOptionDetailTypeDef]
    Budgets: List[BudgetDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SearchProductsAsAdminOutputTypeDef(BaseModel):
    ProductViewDetails: List[ProductViewDetailTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProductOutputTypeDef(BaseModel):
    ProductViewDetail: ProductViewDetailTypeDef
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


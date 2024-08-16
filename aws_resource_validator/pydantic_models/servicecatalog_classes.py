from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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

class AcceptPortfolioShareInputRequestTypeDef(BaseValidatorModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    PortfolioShareType: Optional[PortfolioShareTypeType] = None

class AccessLevelFilterTypeDef(BaseValidatorModel):
    Key: Optional[AccessLevelFilterKeyType] = None
    Value: Optional[str] = None

class AssociateBudgetWithResourceInputRequestTypeDef(BaseValidatorModel):
    BudgetName: str
    ResourceId: str

class AssociatePrincipalWithPortfolioInputRequestTypeDef(BaseValidatorModel):
    PortfolioId: str
    PrincipalARN: str
    PrincipalType: PrincipalTypeType
    AcceptLanguage: Optional[str] = None

class AssociateProductWithPortfolioInputRequestTypeDef(BaseValidatorModel):
    ProductId: str
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    SourcePortfolioId: Optional[str] = None

class AssociateServiceActionWithProvisioningArtifactInputRequestTypeDef(BaseValidatorModel):
    ProductId: str
    ProvisioningArtifactId: str
    ServiceActionId: str
    AcceptLanguage: Optional[str] = None
    IdempotencyToken: Optional[str] = None

class AssociateTagOptionWithResourceInputRequestTypeDef(BaseValidatorModel):
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
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class BudgetDetailTypeDef(BaseValidatorModel):
    BudgetName: Optional[str] = None

class CloudWatchDashboardTypeDef(BaseValidatorModel):
    Name: Optional[str] = None

class CodeStarParametersTypeDef(BaseValidatorModel):
    ConnectionArn: str
    Repository: str
    Branch: str
    ArtifactPath: str

class ConstraintDetailTypeDef(BaseValidatorModel):
    ConstraintId: Optional[str] = None
    Type: Optional[str] = None
    Description: Optional[str] = None
    Owner: Optional[str] = None
    ProductId: Optional[str] = None
    PortfolioId: Optional[str] = None

class ConstraintSummaryTypeDef(BaseValidatorModel):
    Type: Optional[str] = None
    Description: Optional[str] = None

class CopyProductInputRequestTypeDef(BaseValidatorModel):
    SourceProductArn: str
    IdempotencyToken: str
    AcceptLanguage: Optional[str] = None
    TargetProductId: Optional[str] = None
    TargetProductName: Optional[str] = None
    SourceProvisioningArtifactIdentifiers: Optional[Sequence[Mapping[Literal["Id"], str]]] = None
    CopyOptions: Optional[Sequence[Literal["CopyTags"]]] = None

class CreateConstraintInputRequestTypeDef(BaseValidatorModel):
    PortfolioId: str
    ProductId: str
    Parameters: str
    Type: str
    IdempotencyToken: str
    AcceptLanguage: Optional[str] = None
    Description: Optional[str] = None

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

class OrganizationNodeTypeDef(BaseValidatorModel):
    Type: Optional[OrganizationNodeTypeType] = None
    Value: Optional[str] = None

class ProvisioningArtifactPropertiesTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    Info: Optional[Mapping[str, str]] = None
    Type: Optional[ProvisioningArtifactTypeType] = None
    DisableTemplateValidation: Optional[bool] = None

class ProvisioningArtifactDetailTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Type: Optional[ProvisioningArtifactTypeType] = None
    CreatedTime: Optional[datetime] = None
    Active: Optional[bool] = None
    Guidance: Optional[ProvisioningArtifactGuidanceType] = None
    SourceRevision: Optional[str] = None

class UpdateProvisioningParameterTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    UsePreviousValue: Optional[bool] = None

class CreateServiceActionInputRequestTypeDef(BaseValidatorModel):
    Name: str
    DefinitionType: Literal["SSM_AUTOMATION"]
    Definition: Mapping[ServiceActionDefinitionKeyType, str]
    IdempotencyToken: str
    Description: Optional[str] = None
    AcceptLanguage: Optional[str] = None

class CreateTagOptionInputRequestTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class TagOptionDetailTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    Active: Optional[bool] = None
    Id: Optional[str] = None
    Owner: Optional[str] = None

class DeleteConstraintInputRequestTypeDef(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None

class DeletePortfolioInputRequestTypeDef(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None

class DeleteProductInputRequestTypeDef(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None

class DeleteProvisionedProductPlanInputRequestTypeDef(BaseValidatorModel):
    PlanId: str
    AcceptLanguage: Optional[str] = None
    IgnoreErrors: Optional[bool] = None

class DeleteProvisioningArtifactInputRequestTypeDef(BaseValidatorModel):
    ProductId: str
    ProvisioningArtifactId: str
    AcceptLanguage: Optional[str] = None

class DeleteServiceActionInputRequestTypeDef(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None
    IdempotencyToken: Optional[str] = None

class DeleteTagOptionInputRequestTypeDef(BaseValidatorModel):
    Id: str

class DescribeConstraintInputRequestTypeDef(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None

class DescribeCopyProductStatusInputRequestTypeDef(BaseValidatorModel):
    CopyProductToken: str
    AcceptLanguage: Optional[str] = None

class DescribePortfolioInputRequestTypeDef(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None

class DescribePortfolioShareStatusInputRequestTypeDef(BaseValidatorModel):
    PortfolioShareToken: str

class DescribePortfolioSharesInputRequestTypeDef(BaseValidatorModel):
    PortfolioId: str
    Type: DescribePortfolioShareTypeType
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None

class PortfolioShareDetailTypeDef(BaseValidatorModel):
    PrincipalId: Optional[str] = None
    Type: Optional[DescribePortfolioShareTypeType] = None
    Accepted: Optional[bool] = None
    ShareTagOptions: Optional[bool] = None
    SharePrincipals: Optional[bool] = None

class DescribeProductAsAdminInputRequestTypeDef(BaseValidatorModel):
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

class DescribeProductInputRequestTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None

class LaunchPathTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None

class ProductViewSummaryTypeDef(BaseValidatorModel):
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

class ProvisioningArtifactTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    Guidance: Optional[ProvisioningArtifactGuidanceType] = None

class DescribeProductViewInputRequestTypeDef(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None

class DescribeProvisionedProductInputRequestTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None

class ProvisionedProductDetailTypeDef(BaseValidatorModel):
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

class DescribeProvisionedProductPlanInputRequestTypeDef(BaseValidatorModel):
    PlanId: str
    AcceptLanguage: Optional[str] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None

class DescribeProvisioningArtifactInputRequestTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    ProvisioningArtifactId: Optional[str] = None
    ProductId: Optional[str] = None
    ProvisioningArtifactName: Optional[str] = None
    ProductName: Optional[str] = None
    Verbose: Optional[bool] = None
    IncludeProvisioningArtifactParameters: Optional[bool] = None

class DescribeProvisioningParametersInputRequestTypeDef(BaseValidatorModel):
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

class UsageInstructionTypeDef(BaseValidatorModel):
    Type: Optional[str] = None
    Value: Optional[str] = None

class DescribeRecordInputRequestTypeDef(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None

class RecordOutputTypeDef(BaseValidatorModel):
    OutputKey: Optional[str] = None
    OutputValue: Optional[str] = None
    Description: Optional[str] = None

class DescribeServiceActionExecutionParametersInputRequestTypeDef(BaseValidatorModel):
    ProvisionedProductId: str
    ServiceActionId: str
    AcceptLanguage: Optional[str] = None

class ExecutionParameterTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Type: Optional[str] = None
    DefaultValues: Optional[List[str]] = None

class DescribeServiceActionInputRequestTypeDef(BaseValidatorModel):
    Id: str
    AcceptLanguage: Optional[str] = None

class DescribeTagOptionInputRequestTypeDef(BaseValidatorModel):
    Id: str

class DisassociateBudgetFromResourceInputRequestTypeDef(BaseValidatorModel):
    BudgetName: str
    ResourceId: str

class DisassociatePrincipalFromPortfolioInputRequestTypeDef(BaseValidatorModel):
    PortfolioId: str
    PrincipalARN: str
    AcceptLanguage: Optional[str] = None
    PrincipalType: Optional[PrincipalTypeType] = None

class DisassociateProductFromPortfolioInputRequestTypeDef(BaseValidatorModel):
    ProductId: str
    PortfolioId: str
    AcceptLanguage: Optional[str] = None

class DisassociateServiceActionFromProvisioningArtifactInputRequestTypeDef(BaseValidatorModel):
    ProductId: str
    ProvisioningArtifactId: str
    ServiceActionId: str
    AcceptLanguage: Optional[str] = None
    IdempotencyToken: Optional[str] = None

class DisassociateTagOptionFromResourceInputRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    TagOptionId: str

class UniqueTagResourceIdentifierTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class ExecuteProvisionedProductPlanInputRequestTypeDef(BaseValidatorModel):
    PlanId: str
    IdempotencyToken: str
    AcceptLanguage: Optional[str] = None

class ExecuteProvisionedProductServiceActionInputRequestTypeDef(BaseValidatorModel):
    ProvisionedProductId: str
    ServiceActionId: str
    ExecuteToken: str
    AcceptLanguage: Optional[str] = None
    Parameters: Optional[Mapping[str, Sequence[str]]] = None

class GetProvisionedProductOutputsInputRequestTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    ProvisionedProductId: Optional[str] = None
    ProvisionedProductName: Optional[str] = None
    OutputKeys: Optional[Sequence[str]] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None

class ImportAsProvisionedProductInputRequestTypeDef(BaseValidatorModel):
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

class ListAcceptedPortfolioSharesInputRequestTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None
    PortfolioShareType: Optional[PortfolioShareTypeType] = None

class ListBudgetsForResourceInputRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    AcceptLanguage: Optional[str] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None

class ListConstraintsForPortfolioInputRequestTypeDef(BaseValidatorModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    ProductId: Optional[str] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None

class ListLaunchPathsInputRequestTypeDef(BaseValidatorModel):
    ProductId: str
    AcceptLanguage: Optional[str] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None

class ListOrganizationPortfolioAccessInputRequestTypeDef(BaseValidatorModel):
    PortfolioId: str
    OrganizationNodeType: OrganizationNodeTypeType
    AcceptLanguage: Optional[str] = None
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None

class ListPortfolioAccessInputRequestTypeDef(BaseValidatorModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    OrganizationParentId: Optional[str] = None
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None

class ListPortfoliosForProductInputRequestTypeDef(BaseValidatorModel):
    ProductId: str
    AcceptLanguage: Optional[str] = None
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None

class ListPortfoliosInputRequestTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None

class ListPrincipalsForPortfolioInputRequestTypeDef(BaseValidatorModel):
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

class ListProvisioningArtifactsForServiceActionInputRequestTypeDef(BaseValidatorModel):
    ServiceActionId: str
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None
    AcceptLanguage: Optional[str] = None

class ListProvisioningArtifactsInputRequestTypeDef(BaseValidatorModel):
    ProductId: str
    AcceptLanguage: Optional[str] = None

class ListRecordHistorySearchFilterTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class ListResourcesForTagOptionInputRequestTypeDef(BaseValidatorModel):
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

class ListServiceActionsForProvisioningArtifactInputRequestTypeDef(BaseValidatorModel):
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

class ListServiceActionsInputRequestTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None

class ListStackInstancesForProvisionedProductInputRequestTypeDef(BaseValidatorModel):
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

class NotifyTerminateProvisionedProductEngineWorkflowResultInputRequestTypeDef(BaseValidatorModel):
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

class RejectPortfolioShareInputRequestTypeDef(BaseValidatorModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    PortfolioShareType: Optional[PortfolioShareTypeType] = None

class ResourceTargetDefinitionTypeDef(BaseValidatorModel):
    Attribute: Optional[ResourceAttributeType] = None
    Name: Optional[str] = None
    RequiresRecreation: Optional[RequiresRecreationType] = None

class SearchProductsAsAdminInputRequestTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    PortfolioId: Optional[str] = None
    Filters: Optional[Mapping[ProductViewFilterByType, Sequence[str]]] = None
    SortBy: Optional[ProductViewSortByType] = None
    SortOrder: Optional[SortOrderType] = None
    PageToken: Optional[str] = None
    PageSize: Optional[int] = None
    ProductSource: Optional[Literal["ACCOUNT"]] = None

class SearchProductsInputRequestTypeDef(BaseValidatorModel):
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

class TerminateProvisionedProductInputRequestTypeDef(BaseValidatorModel):
    TerminateToken: str
    ProvisionedProductName: Optional[str] = None
    ProvisionedProductId: Optional[str] = None
    IgnoreErrors: Optional[bool] = None
    AcceptLanguage: Optional[str] = None
    RetainPhysicalResources: Optional[bool] = None

class UpdateConstraintInputRequestTypeDef(BaseValidatorModel):
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

class UpdateProvisionedProductPropertiesInputRequestTypeDef(BaseValidatorModel):
    ProvisionedProductId: str
    ProvisionedProductProperties: Mapping[PropertyKeyType, str]
    IdempotencyToken: str
    AcceptLanguage: Optional[str] = None

class UpdateProvisioningArtifactInputRequestTypeDef(BaseValidatorModel):
    ProductId: str
    ProvisioningArtifactId: str
    AcceptLanguage: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Active: Optional[bool] = None
    Guidance: Optional[ProvisioningArtifactGuidanceType] = None

class UpdateServiceActionInputRequestTypeDef(BaseValidatorModel):
    Id: str
    Name: Optional[str] = None
    Definition: Optional[Mapping[ServiceActionDefinitionKeyType, str]] = None
    Description: Optional[str] = None
    AcceptLanguage: Optional[str] = None

class UpdateTagOptionInputRequestTypeDef(BaseValidatorModel):
    Id: str
    Value: Optional[str] = None
    Active: Optional[bool] = None

class ListProvisionedProductPlansInputRequestTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    ProvisionProductId: Optional[str] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None
    AccessLevelFilter: Optional[AccessLevelFilterTypeDef] = None

class ScanProvisionedProductsInputRequestTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    AccessLevelFilter: Optional[AccessLevelFilterTypeDef] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None

class SearchProvisionedProductsInputRequestTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    AccessLevelFilter: Optional[AccessLevelFilterTypeDef] = None
    Filters: Optional[Mapping[Literal["SearchQuery"], Sequence[str]]] = None
    SortBy: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    PageSize: Optional[int] = None
    PageToken: Optional[str] = None

class BatchAssociateServiceActionWithProvisioningArtifactInputRequestTypeDef(BaseValidatorModel):
    ServiceActionAssociations: Sequence[ServiceActionAssociationTypeDef]
    AcceptLanguage: Optional[str] = None

class BatchDisassociateServiceActionFromProvisioningArtifactInputRequestTypeDef(BaseValidatorModel):
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

class CreatePortfolioInputRequestTypeDef(BaseValidatorModel):
    DisplayName: str
    ProviderName: str
    IdempotencyToken: str
    AcceptLanguage: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class LaunchPathSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    ConstraintSummaries: Optional[List[ConstraintSummaryTypeDef]] = None
    Tags: Optional[List[TagTypeDef]] = None
    Name: Optional[str] = None

class ProvisionedProductAttributeTypeDef(BaseValidatorModel):
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

class UpdatePortfolioInputRequestTypeDef(BaseValidatorModel):
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

class CreatePortfolioShareInputRequestTypeDef(BaseValidatorModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    AccountId: Optional[str] = None
    OrganizationNode: Optional[OrganizationNodeTypeDef] = None
    ShareTagOptions: Optional[bool] = None
    SharePrincipals: Optional[bool] = None

class DeletePortfolioShareInputRequestTypeDef(BaseValidatorModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    AccountId: Optional[str] = None
    OrganizationNode: Optional[OrganizationNodeTypeDef] = None

class ListOrganizationPortfolioAccessOutputTypeDef(BaseValidatorModel):
    OrganizationNodes: List[OrganizationNodeTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePortfolioShareInputRequestTypeDef(BaseValidatorModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    AccountId: Optional[str] = None
    OrganizationNode: Optional[OrganizationNodeTypeDef] = None
    ShareTagOptions: Optional[bool] = None
    SharePrincipals: Optional[bool] = None

class CreateProvisioningArtifactInputRequestTypeDef(BaseValidatorModel):
    ProductId: str
    Parameters: ProvisioningArtifactPropertiesTypeDef
    IdempotencyToken: str
    AcceptLanguage: Optional[str] = None

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

class CreateProvisionedProductPlanInputRequestTypeDef(BaseValidatorModel):
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

class DescribePortfolioSharesOutputTypeDef(BaseValidatorModel):
    NextPageToken: str
    PortfolioShareDetails: List[PortfolioShareDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

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

class NotifyUpdateProvisionedProductEngineWorkflowResultInputRequestTypeDef(BaseValidatorModel):
    WorkflowToken: str
    RecordId: str
    Status: EngineWorkflowStatusType
    IdempotencyToken: str
    FailureReason: Optional[str] = None
    Outputs: Optional[Sequence[RecordOutputTypeDef]] = None

class DescribeServiceActionExecutionParametersOutputTypeDef(BaseValidatorModel):
    ServiceActionParameters: List[ExecutionParameterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EngineWorkflowResourceIdentifierTypeDef(BaseValidatorModel):
    UniqueTag: Optional[UniqueTagResourceIdentifierTypeDef] = None

class ListAcceptedPortfolioSharesInputListAcceptedPortfolioSharesPaginateTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    PortfolioShareType: Optional[PortfolioShareTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConstraintsForPortfolioInputListConstraintsForPortfolioPaginateTypeDef(BaseValidatorModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    ProductId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLaunchPathsInputListLaunchPathsPaginateTypeDef(BaseValidatorModel):
    ProductId: str
    AcceptLanguage: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOrganizationPortfolioAccessInputListOrganizationPortfolioAccessPaginateTypeDef(BaseValidatorModel):
    PortfolioId: str
    OrganizationNodeType: OrganizationNodeTypeType
    AcceptLanguage: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPortfoliosForProductInputListPortfoliosForProductPaginateTypeDef(BaseValidatorModel):
    ProductId: str
    AcceptLanguage: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPortfoliosInputListPortfoliosPaginateTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPrincipalsForPortfolioInputListPrincipalsForPortfolioPaginateTypeDef(BaseValidatorModel):
    PortfolioId: str
    AcceptLanguage: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProvisionedProductPlansInputListProvisionedProductPlansPaginateTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    ProvisionProductId: Optional[str] = None
    AccessLevelFilter: Optional[AccessLevelFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProvisioningArtifactsForServiceActionInputListProvisioningArtifactsForServiceActionPaginateTypeDef(BaseValidatorModel):
    ServiceActionId: str
    AcceptLanguage: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourcesForTagOptionInputListResourcesForTagOptionPaginateTypeDef(BaseValidatorModel):
    TagOptionId: str
    ResourceType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServiceActionsForProvisioningArtifactInputListServiceActionsForProvisioningArtifactPaginateTypeDef(BaseValidatorModel):
    ProductId: str
    ProvisioningArtifactId: str
    AcceptLanguage: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServiceActionsInputListServiceActionsPaginateTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ScanProvisionedProductsInputScanProvisionedProductsPaginateTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    AccessLevelFilter: Optional[AccessLevelFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchProductsAsAdminInputSearchProductsAsAdminPaginateTypeDef(BaseValidatorModel):
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

class ListRecordHistoryInputListRecordHistoryPaginateTypeDef(BaseValidatorModel):
    AcceptLanguage: Optional[str] = None
    AccessLevelFilter: Optional[AccessLevelFilterTypeDef] = None
    SearchFilter: Optional[ListRecordHistorySearchFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRecordHistoryInputRequestTypeDef(BaseValidatorModel):
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

class ListTagOptionsInputListTagOptionsPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[ListTagOptionsFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagOptionsInputRequestTypeDef(BaseValidatorModel):
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

class ProvisionProductInputRequestTypeDef(BaseValidatorModel):
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

class UpdateProvisionedProductInputRequestTypeDef(BaseValidatorModel):
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

class SourceConnectionDetailTypeDef(BaseValidatorModel):
    Type: Optional[Literal["CODESTAR"]] = None
    ConnectionParameters: Optional[SourceConnectionParametersTypeDef] = None
    LastSync: Optional[LastSyncTypeDef] = None

class SourceConnectionTypeDef(BaseValidatorModel):
    ConnectionParameters: SourceConnectionParametersTypeDef
    Type: Optional[Literal["CODESTAR"]] = None

class ListLaunchPathsOutputTypeDef(BaseValidatorModel):
    LaunchPathSummaries: List[LaunchPathSummaryTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchProvisionedProductsOutputTypeDef(BaseValidatorModel):
    ProvisionedProducts: List[ProvisionedProductAttributeTypeDef]
    TotalResultsCount: int
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListProvisioningArtifactsForServiceActionOutputTypeDef(BaseValidatorModel):
    ProvisioningArtifactViews: List[ProvisioningArtifactViewTypeDef]
    NextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class NotifyProvisionProductEngineWorkflowResultInputRequestTypeDef(BaseValidatorModel):
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

class ProductViewDetailTypeDef(BaseValidatorModel):
    ProductViewSummary: Optional[ProductViewSummaryTypeDef] = None
    Status: Optional[StatusType] = None
    ProductARN: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    SourceConnection: Optional[SourceConnectionDetailTypeDef] = None

class CreateProductInputRequestTypeDef(BaseValidatorModel):
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

class UpdateProductInputRequestTypeDef(BaseValidatorModel):
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


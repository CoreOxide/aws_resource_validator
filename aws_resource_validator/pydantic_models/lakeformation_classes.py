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
from aws_resource_validator.pydantic_models.lakeformation_constants import *

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AddObjectInputTypeDef(BaseValidatorModel):
    Uri: str
    ETag: str
    Size: int
    PartitionValues: Optional[Sequence[str]] = None


class AssumeDecoratedRoleWithSAMLRequestTypeDef(BaseValidatorModel):
    SAMLAssertion: str
    RoleArn: str
    PrincipalArn: str
    DurationSeconds: Optional[int] = None


class AuditContextTypeDef(BaseValidatorModel):
    AdditionalAuditContext: Optional[str] = None


class ErrorDetailTypeDef(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class DataLakePrincipalTypeDef(BaseValidatorModel):
    DataLakePrincipalIdentifier: Optional[str] = None


class CancelTransactionRequestTypeDef(BaseValidatorModel):
    TransactionId: str


class CatalogResourceTypeDef(BaseValidatorModel):
    Id: Optional[str] = None


class LFTagPairOutputTypeDef(BaseValidatorModel):
    TagKey: str
    TagValues: List[str]
    CatalogId: Optional[str] = None


class ColumnWildcardOutputTypeDef(BaseValidatorModel):
    ExcludedColumnNames: Optional[List[str]] = None


class ColumnWildcardTypeDef(BaseValidatorModel):
    ExcludedColumnNames: Optional[Sequence[str]] = None


class CommitTransactionRequestTypeDef(BaseValidatorModel):
    TransactionId: str


class ConditionTypeDef(BaseValidatorModel):
    Expression: Optional[str] = None


class CreateLFTagRequestTypeDef(BaseValidatorModel):
    TagKey: str
    TagValues: Sequence[str]
    CatalogId: Optional[str] = None


class RowFilterOutputTypeDef(BaseValidatorModel):
    FilterExpression: Optional[str] = None
    AllRowsWildcard: Optional[Dict[str, Any]] = None


class DataCellsFilterResourceTypeDef(BaseValidatorModel):
    TableCatalogId: Optional[str] = None
    DatabaseName: Optional[str] = None
    TableName: Optional[str] = None
    Name: Optional[str] = None


class RowFilterTypeDef(BaseValidatorModel):
    FilterExpression: Optional[str] = None
    AllRowsWildcard: Optional[Mapping[str, Any]] = None


class DataLocationResourceTypeDef(BaseValidatorModel):
    ResourceArn: str
    CatalogId: Optional[str] = None


class DatabaseResourceTypeDef(BaseValidatorModel):
    Name: str
    CatalogId: Optional[str] = None


class DeleteDataCellsFilterRequestTypeDef(BaseValidatorModel):
    TableCatalogId: Optional[str] = None
    DatabaseName: Optional[str] = None
    TableName: Optional[str] = None
    Name: Optional[str] = None


class DeleteLFTagExpressionRequestTypeDef(BaseValidatorModel):
    Name: str
    CatalogId: Optional[str] = None


class DeleteLFTagRequestTypeDef(BaseValidatorModel):
    TagKey: str
    CatalogId: Optional[str] = None


class DeleteLakeFormationIdentityCenterConfigurationRequestTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None


class DeleteObjectInputTypeDef(BaseValidatorModel):
    Uri: str
    ETag: Optional[str] = None
    PartitionValues: Optional[Sequence[str]] = None


class VirtualObjectTypeDef(BaseValidatorModel):
    Uri: str
    ETag: Optional[str] = None


class DeregisterResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class DescribeLakeFormationIdentityCenterConfigurationRequestTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None


class ExternalFilteringConfigurationOutputTypeDef(BaseValidatorModel):
    Status: EnableStatusType
    AuthorizedTargets: List[str]


class DescribeResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class ResourceInfoTypeDef(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    RoleArn: Optional[str] = None
    LastModified: Optional[datetime] = None
    WithFederation: Optional[bool] = None
    HybridAccessEnabled: Optional[bool] = None


class DescribeTransactionRequestTypeDef(BaseValidatorModel):
    TransactionId: str


class TransactionDescriptionTypeDef(BaseValidatorModel):
    TransactionId: Optional[str] = None
    TransactionStatus: Optional[TransactionStatusType] = None
    TransactionStartTime: Optional[datetime] = None
    TransactionEndTime: Optional[datetime] = None


class DetailsMapTypeDef(BaseValidatorModel):
    ResourceShare: Optional[List[str]] = None


class ExecutionStatisticsTypeDef(BaseValidatorModel):
    AverageExecutionTimeMillis: Optional[int] = None
    DataScannedBytes: Optional[int] = None
    WorkUnitsExecutedCount: Optional[int] = None


class ExtendTransactionRequestTypeDef(BaseValidatorModel):
    TransactionId: Optional[str] = None


class ExternalFilteringConfigurationTypeDef(BaseValidatorModel):
    Status: EnableStatusType
    AuthorizedTargets: Sequence[str]


class FilterConditionTypeDef(BaseValidatorModel):
    Field: Optional[FieldNameStringType] = None
    ComparisonOperator: Optional[ComparisonOperatorType] = None
    StringValueList: Optional[Sequence[str]] = None


class GetDataCellsFilterRequestTypeDef(BaseValidatorModel):
    TableCatalogId: str
    DatabaseName: str
    TableName: str
    Name: str


class GetDataLakeSettingsRequestTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None


class GetEffectivePermissionsForPathRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    CatalogId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetLFTagExpressionRequestTypeDef(BaseValidatorModel):
    Name: str
    CatalogId: Optional[str] = None


class LFTagOutputTypeDef(BaseValidatorModel):
    TagKey: str
    TagValues: List[str]


class GetLFTagRequestTypeDef(BaseValidatorModel):
    TagKey: str
    CatalogId: Optional[str] = None


class GetQueryStateRequestTypeDef(BaseValidatorModel):
    QueryId: str


class GetQueryStatisticsRequestTypeDef(BaseValidatorModel):
    QueryId: str


class PlanningStatisticsTypeDef(BaseValidatorModel):
    EstimatedDataToScanBytes: Optional[int] = None
    PlanningTimeMillis: Optional[int] = None
    QueueTimeMillis: Optional[int] = None
    WorkUnitsGeneratedCount: Optional[int] = None


class PartitionValueListTypeDef(BaseValidatorModel):
    Values: Sequence[str]


class GetWorkUnitResultsRequestTypeDef(BaseValidatorModel):
    QueryId: str
    WorkUnitId: int
    WorkUnitToken: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetWorkUnitsRequestTypeDef(BaseValidatorModel):
    QueryId: str
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class WorkUnitRangeTypeDef(BaseValidatorModel):
    WorkUnitIdMax: int
    WorkUnitIdMin: int
    WorkUnitToken: str


class LFTagExpressionResourceTypeDef(BaseValidatorModel):
    Name: str
    CatalogId: Optional[str] = None


class LFTagKeyResourceOutputTypeDef(BaseValidatorModel):
    TagKey: str
    TagValues: List[str]
    CatalogId: Optional[str] = None


class LFTagKeyResourceTypeDef(BaseValidatorModel):
    TagKey: str
    TagValues: Sequence[str]
    CatalogId: Optional[str] = None


class LFTagPairTypeDef(BaseValidatorModel):
    TagKey: str
    TagValues: Sequence[str]
    CatalogId: Optional[str] = None


class LFTagTypeDef(BaseValidatorModel):
    TagKey: str
    TagValues: Sequence[str]


class ListLFTagExpressionsRequestTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListLFTagsRequestTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None
    ResourceShareType: Optional[ResourceShareTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTableStorageOptimizersRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    StorageOptimizerType: Optional[OptimizerTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class StorageOptimizerTypeDef(BaseValidatorModel):
    StorageOptimizerType: Optional[OptimizerTypeType] = None
    Config: Optional[Dict[str, str]] = None
    ErrorMessage: Optional[str] = None
    Warnings: Optional[str] = None
    LastRunDetails: Optional[str] = None


class ListTransactionsRequestTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None
    StatusFilter: Optional[TransactionStatusFilterType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class TableObjectTypeDef(BaseValidatorModel):
    Uri: Optional[str] = None
    ETag: Optional[str] = None
    Size: Optional[int] = None


class RegisterResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    UseServiceLinkedRole: Optional[bool] = None
    RoleArn: Optional[str] = None
    WithFederation: Optional[bool] = None
    HybridAccessEnabled: Optional[bool] = None


class TableResourceOutputTypeDef(BaseValidatorModel):
    DatabaseName: str
    CatalogId: Optional[str] = None
    Name: Optional[str] = None
    TableWildcard: Optional[Dict[str, Any]] = None


class StartTransactionRequestTypeDef(BaseValidatorModel):
    TransactionType: Optional[TransactionTypeType] = None


class TableResourceTypeDef(BaseValidatorModel):
    DatabaseName: str
    CatalogId: Optional[str] = None
    Name: Optional[str] = None
    TableWildcard: Optional[Mapping[str, Any]] = None


class UpdateLFTagRequestTypeDef(BaseValidatorModel):
    TagKey: str
    CatalogId: Optional[str] = None
    TagValuesToDelete: Optional[Sequence[str]] = None
    TagValuesToAdd: Optional[Sequence[str]] = None


class UpdateResourceRequestTypeDef(BaseValidatorModel):
    RoleArn: str
    ResourceArn: str
    WithFederation: Optional[bool] = None
    HybridAccessEnabled: Optional[bool] = None


class UpdateTableStorageOptimizerRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    StorageOptimizerConfig: Mapping[OptimizerTypeType, Mapping[str, str]]
    CatalogId: Optional[str] = None


class AssumeDecoratedRoleWithSAMLResponseTypeDef(BaseValidatorModel):
    AccessKeyId: str
    SecretAccessKey: str
    SessionToken: str
    Expiration: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class CommitTransactionResponseTypeDef(BaseValidatorModel):
    TransactionStatus: TransactionStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class CreateLakeFormationIdentityCenterConfigurationResponseTypeDef(BaseValidatorModel):
    ApplicationArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetDataLakePrincipalResponseTypeDef(BaseValidatorModel):
    Identity: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetLFTagResponseTypeDef(BaseValidatorModel):
    CatalogId: str
    TagKey: str
    TagValues: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetQueryStateResponseTypeDef(BaseValidatorModel):
    Error: str
    State: QueryStateStringType
    ResponseMetadata: ResponseMetadataTypeDef


class GetTemporaryGluePartitionCredentialsResponseTypeDef(BaseValidatorModel):
    AccessKeyId: str
    SecretAccessKey: str
    SessionToken: str
    Expiration: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class GetTemporaryGlueTableCredentialsResponseTypeDef(BaseValidatorModel):
    AccessKeyId: str
    SecretAccessKey: str
    SessionToken: str
    Expiration: datetime
    VendedS3Path: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetWorkUnitResultsResponseTypeDef(BaseValidatorModel):
    ResultStream: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef


class StartQueryPlanningResponseTypeDef(BaseValidatorModel):
    QueryId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartTransactionResponseTypeDef(BaseValidatorModel):
    TransactionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateTableStorageOptimizerResponseTypeDef(BaseValidatorModel):
    Result: str
    ResponseMetadata: ResponseMetadataTypeDef


class PrincipalPermissionsOutputTypeDef(BaseValidatorModel):
    Principal: Optional[DataLakePrincipalTypeDef] = None
    Permissions: Optional[List[PermissionType]] = None


class PrincipalPermissionsTypeDef(BaseValidatorModel):
    Principal: Optional[DataLakePrincipalTypeDef] = None
    Permissions: Optional[Sequence[PermissionType]] = None


class ColumnLFTagTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    LFTags: Optional[List[LFTagPairOutputTypeDef]] = None


class LFTagErrorTypeDef(BaseValidatorModel):
    LFTag: Optional[LFTagPairOutputTypeDef] = None
    Error: Optional[ErrorDetailTypeDef] = None


class ListLFTagsResponseTypeDef(BaseValidatorModel):
    LFTags: List[LFTagPairOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TableWithColumnsResourceOutputTypeDef(BaseValidatorModel):
    DatabaseName: str
    Name: str
    CatalogId: Optional[str] = None
    ColumnNames: Optional[List[str]] = None
    ColumnWildcard: Optional[ColumnWildcardOutputTypeDef] = None


class DataCellsFilterOutputTypeDef(BaseValidatorModel):
    TableCatalogId: str
    DatabaseName: str
    TableName: str
    Name: str
    RowFilter: Optional[RowFilterOutputTypeDef] = None
    ColumnNames: Optional[List[str]] = None
    ColumnWildcard: Optional[ColumnWildcardOutputTypeDef] = None
    VersionId: Optional[str] = None


class DataCellsFilterTypeDef(BaseValidatorModel):
    TableCatalogId: str
    DatabaseName: str
    TableName: str
    Name: str
    RowFilter: Optional[RowFilterTypeDef] = None
    ColumnNames: Optional[Sequence[str]] = None
    ColumnWildcard: Optional[ColumnWildcardTypeDef] = None
    VersionId: Optional[str] = None


class TaggedDatabaseTypeDef(BaseValidatorModel):
    Database: Optional[DatabaseResourceTypeDef] = None
    LFTags: Optional[List[LFTagPairOutputTypeDef]] = None


class WriteOperationTypeDef(BaseValidatorModel):
    AddObject: Optional[AddObjectInputTypeDef] = None
    DeleteObject: Optional[DeleteObjectInputTypeDef] = None


class DeleteObjectsOnCancelRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    TransactionId: str
    Objects: Sequence[VirtualObjectTypeDef]
    CatalogId: Optional[str] = None


class DescribeLakeFormationIdentityCenterConfigurationResponseTypeDef(BaseValidatorModel):
    CatalogId: str
    InstanceArn: str
    ApplicationArn: str
    ExternalFiltering: ExternalFilteringConfigurationOutputTypeDef
    ShareRecipients: List[DataLakePrincipalTypeDef]
    ResourceShare: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeResourceResponseTypeDef(BaseValidatorModel):
    ResourceInfo: ResourceInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListResourcesResponseTypeDef(BaseValidatorModel):
    ResourceInfoList: List[ResourceInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeTransactionResponseTypeDef(BaseValidatorModel):
    TransactionDescription: TransactionDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListTransactionsResponseTypeDef(BaseValidatorModel):
    Transactions: List[TransactionDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListResourcesRequestTypeDef(BaseValidatorModel):
    FilterConditionList: Optional[Sequence[FilterConditionTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetLFTagExpressionResponseTypeDef(BaseValidatorModel):
    Name: str
    Description: str
    CatalogId: str
    Expression: List[LFTagOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class LFTagExpressionTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    CatalogId: Optional[str] = None
    Expression: Optional[List[LFTagOutputTypeDef]] = None


class LFTagPolicyResourceOutputTypeDef(BaseValidatorModel):
    ResourceType: ResourceTypeType
    CatalogId: Optional[str] = None
    Expression: Optional[List[LFTagOutputTypeDef]] = None
    ExpressionName: Optional[str] = None


class GetQueryStatisticsResponseTypeDef(BaseValidatorModel):
    ExecutionStatistics: ExecutionStatisticsTypeDef
    PlanningStatistics: PlanningStatisticsTypeDef
    QuerySubmissionTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class TimestampTypeDef(BaseValidatorModel):
    pass


class GetTableObjectsRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    TransactionId: Optional[str] = None
    QueryAsOfTime: Optional[TimestampTypeDef] = None
    PartitionPredicate: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class QueryPlanningContextTypeDef(BaseValidatorModel):
    DatabaseName: str
    CatalogId: Optional[str] = None
    QueryAsOfTime: Optional[TimestampTypeDef] = None
    QueryParameters: Optional[Mapping[str, str]] = None
    TransactionId: Optional[str] = None


class QuerySessionContextTypeDef(BaseValidatorModel):
    QueryId: Optional[str] = None
    QueryStartTime: Optional[TimestampTypeDef] = None
    ClusterId: Optional[str] = None
    QueryAuthorizationId: Optional[str] = None
    AdditionalContext: Optional[Mapping[str, str]] = None


class GetTemporaryGluePartitionCredentialsRequestTypeDef(BaseValidatorModel):
    TableArn: str
    Partition: PartitionValueListTypeDef
    Permissions: Optional[Sequence[PermissionType]] = None
    DurationSeconds: Optional[int] = None
    AuditContext: Optional[AuditContextTypeDef] = None
    SupportedPermissionTypes: Optional[Sequence[PermissionTypeType]] = None


class GetWorkUnitsRequestPaginateTypeDef(BaseValidatorModel):
    QueryId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListLFTagExpressionsRequestPaginateTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListLFTagsRequestPaginateTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None
    ResourceShareType: Optional[ResourceShareTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetWorkUnitsResponseTypeDef(BaseValidatorModel):
    QueryId: str
    WorkUnitRanges: List[WorkUnitRangeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTableStorageOptimizersResponseTypeDef(BaseValidatorModel):
    StorageOptimizerList: List[StorageOptimizerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class PartitionObjectsTypeDef(BaseValidatorModel):
    PartitionValues: Optional[List[str]] = None
    Objects: Optional[List[TableObjectTypeDef]] = None


class DataLakeSettingsOutputTypeDef(BaseValidatorModel):
    DataLakeAdmins: Optional[List[DataLakePrincipalTypeDef]] = None
    ReadOnlyAdmins: Optional[List[DataLakePrincipalTypeDef]] = None
    CreateDatabaseDefaultPermissions: Optional[List[PrincipalPermissionsOutputTypeDef]] = None
    CreateTableDefaultPermissions: Optional[List[PrincipalPermissionsOutputTypeDef]] = None
    Parameters: Optional[Dict[str, str]] = None
    TrustedResourceOwners: Optional[List[str]] = None
    AllowExternalDataFiltering: Optional[bool] = None
    AllowFullTableExternalDataAccess: Optional[bool] = None
    ExternalDataFilteringAllowList: Optional[List[DataLakePrincipalTypeDef]] = None
    AuthorizedSessionTagValueList: Optional[List[str]] = None


class DataLakeSettingsTypeDef(BaseValidatorModel):
    DataLakeAdmins: Optional[Sequence[DataLakePrincipalTypeDef]] = None
    ReadOnlyAdmins: Optional[Sequence[DataLakePrincipalTypeDef]] = None
    CreateDatabaseDefaultPermissions: Optional[Sequence[PrincipalPermissionsTypeDef]] = None
    CreateTableDefaultPermissions: Optional[Sequence[PrincipalPermissionsTypeDef]] = None
    Parameters: Optional[Mapping[str, str]] = None
    TrustedResourceOwners: Optional[Sequence[str]] = None
    AllowExternalDataFiltering: Optional[bool] = None
    AllowFullTableExternalDataAccess: Optional[bool] = None
    ExternalDataFilteringAllowList: Optional[Sequence[DataLakePrincipalTypeDef]] = None
    AuthorizedSessionTagValueList: Optional[Sequence[str]] = None


class GetResourceLFTagsResponseTypeDef(BaseValidatorModel):
    LFTagOnDatabase: List[LFTagPairOutputTypeDef]
    LFTagsOnTable: List[LFTagPairOutputTypeDef]
    LFTagsOnColumns: List[ColumnLFTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TaggedTableTypeDef(BaseValidatorModel):
    Table: Optional[TableResourceOutputTypeDef] = None
    LFTagOnDatabase: Optional[List[LFTagPairOutputTypeDef]] = None
    LFTagsOnTable: Optional[List[LFTagPairOutputTypeDef]] = None
    LFTagsOnColumns: Optional[List[ColumnLFTagTypeDef]] = None


class AddLFTagsToResourceResponseTypeDef(BaseValidatorModel):
    Failures: List[LFTagErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class RemoveLFTagsFromResourceResponseTypeDef(BaseValidatorModel):
    Failures: List[LFTagErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ColumnWildcardUnionTypeDef(BaseValidatorModel):
    pass


class TableWithColumnsResourceTypeDef(BaseValidatorModel):
    DatabaseName: str
    Name: str
    CatalogId: Optional[str] = None
    ColumnNames: Optional[Sequence[str]] = None
    ColumnWildcard: Optional[ColumnWildcardUnionTypeDef] = None


class GetDataCellsFilterResponseTypeDef(BaseValidatorModel):
    DataCellsFilter: DataCellsFilterOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListDataCellsFilterResponseTypeDef(BaseValidatorModel):
    DataCellsFilters: List[DataCellsFilterOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class SearchDatabasesByLFTagsResponseTypeDef(BaseValidatorModel):
    DatabaseList: List[TaggedDatabaseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateTableObjectsRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    WriteOperations: Sequence[WriteOperationTypeDef]
    CatalogId: Optional[str] = None
    TransactionId: Optional[str] = None


class ExternalFilteringConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateLakeFormationIdentityCenterConfigurationRequestTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None
    InstanceArn: Optional[str] = None
    ExternalFiltering: Optional[ExternalFilteringConfigurationUnionTypeDef] = None
    ShareRecipients: Optional[Sequence[DataLakePrincipalTypeDef]] = None


class UpdateLakeFormationIdentityCenterConfigurationRequestTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None
    ShareRecipients: Optional[Sequence[DataLakePrincipalTypeDef]] = None
    ApplicationStatus: Optional[ApplicationStatusType] = None
    ExternalFiltering: Optional[ExternalFilteringConfigurationUnionTypeDef] = None


class ListLFTagExpressionsResponseTypeDef(BaseValidatorModel):
    LFTagExpressions: List[LFTagExpressionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ResourceOutputTypeDef(BaseValidatorModel):
    Catalog: Optional[CatalogResourceTypeDef] = None
    Database: Optional[DatabaseResourceTypeDef] = None
    Table: Optional[TableResourceOutputTypeDef] = None
    TableWithColumns: Optional[TableWithColumnsResourceOutputTypeDef] = None
    DataLocation: Optional[DataLocationResourceTypeDef] = None
    DataCellsFilter: Optional[DataCellsFilterResourceTypeDef] = None
    LFTag: Optional[LFTagKeyResourceOutputTypeDef] = None
    LFTagPolicy: Optional[LFTagPolicyResourceOutputTypeDef] = None
    LFTagExpression: Optional[LFTagExpressionResourceTypeDef] = None


class StartQueryPlanningRequestTypeDef(BaseValidatorModel):
    QueryPlanningContext: QueryPlanningContextTypeDef
    QueryString: str


class GetTemporaryGlueTableCredentialsRequestTypeDef(BaseValidatorModel):
    TableArn: str
    Permissions: Optional[Sequence[PermissionType]] = None
    DurationSeconds: Optional[int] = None
    AuditContext: Optional[AuditContextTypeDef] = None
    SupportedPermissionTypes: Optional[Sequence[PermissionTypeType]] = None
    S3Path: Optional[str] = None
    QuerySessionContext: Optional[QuerySessionContextTypeDef] = None


class LFTagUnionTypeDef(BaseValidatorModel):
    pass


class CreateLFTagExpressionRequestTypeDef(BaseValidatorModel):
    Name: str
    Expression: Sequence[LFTagUnionTypeDef]
    Description: Optional[str] = None
    CatalogId: Optional[str] = None


class LFTagPolicyResourceTypeDef(BaseValidatorModel):
    ResourceType: ResourceTypeType
    CatalogId: Optional[str] = None
    Expression: Optional[Sequence[LFTagUnionTypeDef]] = None
    ExpressionName: Optional[str] = None


class SearchDatabasesByLFTagsRequestPaginateTypeDef(BaseValidatorModel):
    Expression: Sequence[LFTagUnionTypeDef]
    CatalogId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchDatabasesByLFTagsRequestTypeDef(BaseValidatorModel):
    Expression: Sequence[LFTagUnionTypeDef]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CatalogId: Optional[str] = None


class SearchTablesByLFTagsRequestPaginateTypeDef(BaseValidatorModel):
    Expression: Sequence[LFTagUnionTypeDef]
    CatalogId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchTablesByLFTagsRequestTypeDef(BaseValidatorModel):
    Expression: Sequence[LFTagUnionTypeDef]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CatalogId: Optional[str] = None


class UpdateLFTagExpressionRequestTypeDef(BaseValidatorModel):
    Name: str
    Expression: Sequence[LFTagUnionTypeDef]
    Description: Optional[str] = None
    CatalogId: Optional[str] = None


class GetTableObjectsResponseTypeDef(BaseValidatorModel):
    Objects: List[PartitionObjectsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TableResourceUnionTypeDef(BaseValidatorModel):
    pass


class ListDataCellsFilterRequestPaginateTypeDef(BaseValidatorModel):
    Table: Optional[TableResourceUnionTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDataCellsFilterRequestTypeDef(BaseValidatorModel):
    Table: Optional[TableResourceUnionTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetDataLakeSettingsResponseTypeDef(BaseValidatorModel):
    DataLakeSettings: DataLakeSettingsOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SearchTablesByLFTagsResponseTypeDef(BaseValidatorModel):
    TableList: List[TaggedTableTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DataCellsFilterUnionTypeDef(BaseValidatorModel):
    pass


class CreateDataCellsFilterRequestTypeDef(BaseValidatorModel):
    TableData: DataCellsFilterUnionTypeDef


class UpdateDataCellsFilterRequestTypeDef(BaseValidatorModel):
    TableData: DataCellsFilterUnionTypeDef


class BatchPermissionsRequestEntryOutputTypeDef(BaseValidatorModel):
    Id: str
    Principal: Optional[DataLakePrincipalTypeDef] = None
    Resource: Optional[ResourceOutputTypeDef] = None
    Permissions: Optional[List[PermissionType]] = None
    PermissionsWithGrantOption: Optional[List[PermissionType]] = None


class LakeFormationOptInsInfoTypeDef(BaseValidatorModel):
    Resource: Optional[ResourceOutputTypeDef] = None
    Principal: Optional[DataLakePrincipalTypeDef] = None
    Condition: Optional[ConditionTypeDef] = None
    LastModified: Optional[datetime] = None
    LastUpdatedBy: Optional[str] = None


class PrincipalResourcePermissionsTypeDef(BaseValidatorModel):
    Principal: Optional[DataLakePrincipalTypeDef] = None
    Resource: Optional[ResourceOutputTypeDef] = None
    Condition: Optional[ConditionTypeDef] = None
    Permissions: Optional[List[PermissionType]] = None
    PermissionsWithGrantOption: Optional[List[PermissionType]] = None
    AdditionalDetails: Optional[DetailsMapTypeDef] = None
    LastUpdated: Optional[datetime] = None
    LastUpdatedBy: Optional[str] = None


class DataLakeSettingsUnionTypeDef(BaseValidatorModel):
    pass


class PutDataLakeSettingsRequestTypeDef(BaseValidatorModel):
    DataLakeSettings: DataLakeSettingsUnionTypeDef
    CatalogId: Optional[str] = None


class BatchPermissionsFailureEntryTypeDef(BaseValidatorModel):
    RequestEntry: Optional[BatchPermissionsRequestEntryOutputTypeDef] = None
    Error: Optional[ErrorDetailTypeDef] = None


class ListLakeFormationOptInsResponseTypeDef(BaseValidatorModel):
    LakeFormationOptInsInfoList: List[LakeFormationOptInsInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetEffectivePermissionsForPathResponseTypeDef(BaseValidatorModel):
    Permissions: List[PrincipalResourcePermissionsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListPermissionsResponseTypeDef(BaseValidatorModel):
    PrincipalResourcePermissions: List[PrincipalResourcePermissionsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TableWithColumnsResourceUnionTypeDef(BaseValidatorModel):
    pass


class LFTagPolicyResourceUnionTypeDef(BaseValidatorModel):
    pass


class LFTagKeyResourceUnionTypeDef(BaseValidatorModel):
    pass


class ResourceTypeDef(BaseValidatorModel):
    Catalog: Optional[CatalogResourceTypeDef] = None
    Database: Optional[DatabaseResourceTypeDef] = None
    Table: Optional[TableResourceUnionTypeDef] = None
    TableWithColumns: Optional[TableWithColumnsResourceUnionTypeDef] = None
    DataLocation: Optional[DataLocationResourceTypeDef] = None
    DataCellsFilter: Optional[DataCellsFilterResourceTypeDef] = None
    LFTag: Optional[LFTagKeyResourceUnionTypeDef] = None
    LFTagPolicy: Optional[LFTagPolicyResourceUnionTypeDef] = None
    LFTagExpression: Optional[LFTagExpressionResourceTypeDef] = None


class BatchGrantPermissionsResponseTypeDef(BaseValidatorModel):
    Failures: List[BatchPermissionsFailureEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchRevokePermissionsResponseTypeDef(BaseValidatorModel):
    Failures: List[BatchPermissionsFailureEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ResourceUnionTypeDef(BaseValidatorModel):
    pass


class LFTagPairUnionTypeDef(BaseValidatorModel):
    pass


class AddLFTagsToResourceRequestTypeDef(BaseValidatorModel):
    Resource: ResourceUnionTypeDef
    LFTags: Sequence[LFTagPairUnionTypeDef]
    CatalogId: Optional[str] = None


class BatchPermissionsRequestEntryTypeDef(BaseValidatorModel):
    Id: str
    Principal: Optional[DataLakePrincipalTypeDef] = None
    Resource: Optional[ResourceUnionTypeDef] = None
    Permissions: Optional[Sequence[PermissionType]] = None
    PermissionsWithGrantOption: Optional[Sequence[PermissionType]] = None


class CreateLakeFormationOptInRequestTypeDef(BaseValidatorModel):
    Principal: DataLakePrincipalTypeDef
    Resource: ResourceUnionTypeDef


class DeleteLakeFormationOptInRequestTypeDef(BaseValidatorModel):
    Principal: DataLakePrincipalTypeDef
    Resource: ResourceUnionTypeDef


class GetResourceLFTagsRequestTypeDef(BaseValidatorModel):
    Resource: ResourceUnionTypeDef
    CatalogId: Optional[str] = None
    ShowAssignedLFTags: Optional[bool] = None


class GrantPermissionsRequestTypeDef(BaseValidatorModel):
    Principal: DataLakePrincipalTypeDef
    Resource: ResourceUnionTypeDef
    Permissions: Sequence[PermissionType]
    CatalogId: Optional[str] = None
    PermissionsWithGrantOption: Optional[Sequence[PermissionType]] = None


class ListLakeFormationOptInsRequestTypeDef(BaseValidatorModel):
    Principal: Optional[DataLakePrincipalTypeDef] = None
    Resource: Optional[ResourceUnionTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListPermissionsRequestTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None
    Principal: Optional[DataLakePrincipalTypeDef] = None
    ResourceType: Optional[DataLakeResourceTypeType] = None
    Resource: Optional[ResourceUnionTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    IncludeRelated: Optional[str] = None


class RemoveLFTagsFromResourceRequestTypeDef(BaseValidatorModel):
    Resource: ResourceUnionTypeDef
    LFTags: Sequence[LFTagPairUnionTypeDef]
    CatalogId: Optional[str] = None


class RevokePermissionsRequestTypeDef(BaseValidatorModel):
    Principal: DataLakePrincipalTypeDef
    Resource: ResourceUnionTypeDef
    Permissions: Sequence[PermissionType]
    CatalogId: Optional[str] = None
    PermissionsWithGrantOption: Optional[Sequence[PermissionType]] = None


class BatchPermissionsRequestEntryUnionTypeDef(BaseValidatorModel):
    pass


class BatchGrantPermissionsRequestTypeDef(BaseValidatorModel):
    Entries: Sequence[BatchPermissionsRequestEntryUnionTypeDef]
    CatalogId: Optional[str] = None


class BatchRevokePermissionsRequestTypeDef(BaseValidatorModel):
    Entries: Sequence[BatchPermissionsRequestEntryUnionTypeDef]
    CatalogId: Optional[str] = None



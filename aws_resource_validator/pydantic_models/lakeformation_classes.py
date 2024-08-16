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

class AssumeDecoratedRoleWithSAMLRequestRequestTypeDef(BaseValidatorModel):
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

class CancelTransactionRequestRequestTypeDef(BaseValidatorModel):
    TransactionId: str

class LFTagPairOutputTypeDef(BaseValidatorModel):
    TagKey: str
    TagValues: List[str]
    CatalogId: Optional[str] = None

class ColumnWildcardExtraOutputTypeDef(BaseValidatorModel):
    ExcludedColumnNames: Optional[List[str]] = None

class ColumnWildcardOutputTypeDef(BaseValidatorModel):
    ExcludedColumnNames: Optional[List[str]] = None

class ColumnWildcardTypeDef(BaseValidatorModel):
    ExcludedColumnNames: Optional[Sequence[str]] = None

class CommitTransactionRequestRequestTypeDef(BaseValidatorModel):
    TransactionId: str

class CreateLFTagRequestRequestTypeDef(BaseValidatorModel):
    TagKey: str
    TagValues: Sequence[str]
    CatalogId: Optional[str] = None

class ExternalFilteringConfigurationTypeDef(BaseValidatorModel):
    Status: EnableStatusType
    AuthorizedTargets: Sequence[str]

class RowFilterExtraOutputTypeDef(BaseValidatorModel):
    FilterExpression: Optional[str] = None
    AllRowsWildcard: Optional[Dict[str, Any]] = None

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

class DeleteDataCellsFilterRequestRequestTypeDef(BaseValidatorModel):
    TableCatalogId: Optional[str] = None
    DatabaseName: Optional[str] = None
    TableName: Optional[str] = None
    Name: Optional[str] = None

class DeleteLFTagRequestRequestTypeDef(BaseValidatorModel):
    TagKey: str
    CatalogId: Optional[str] = None

class DeleteLakeFormationIdentityCenterConfigurationRequestRequestTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None

class DeleteObjectInputTypeDef(BaseValidatorModel):
    Uri: str
    ETag: Optional[str] = None
    PartitionValues: Optional[Sequence[str]] = None

class VirtualObjectTypeDef(BaseValidatorModel):
    Uri: str
    ETag: Optional[str] = None

class DeregisterResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class DescribeLakeFormationIdentityCenterConfigurationRequestRequestTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None

class ExternalFilteringConfigurationOutputTypeDef(BaseValidatorModel):
    Status: EnableStatusType
    AuthorizedTargets: List[str]

class DescribeResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class ResourceInfoTypeDef(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    RoleArn: Optional[str] = None
    LastModified: Optional[datetime] = None
    WithFederation: Optional[bool] = None
    HybridAccessEnabled: Optional[bool] = None

class DescribeTransactionRequestRequestTypeDef(BaseValidatorModel):
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

class ExtendTransactionRequestRequestTypeDef(BaseValidatorModel):
    TransactionId: Optional[str] = None

class FilterConditionTypeDef(BaseValidatorModel):
    Field: Optional[FieldNameStringType] = None
    ComparisonOperator: Optional[ComparisonOperatorType] = None
    StringValueList: Optional[Sequence[str]] = None

class GetDataCellsFilterRequestRequestTypeDef(BaseValidatorModel):
    TableCatalogId: str
    DatabaseName: str
    TableName: str
    Name: str

class GetDataLakeSettingsRequestRequestTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None

class GetEffectivePermissionsForPathRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    CatalogId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetLFTagRequestRequestTypeDef(BaseValidatorModel):
    TagKey: str
    CatalogId: Optional[str] = None

class GetQueryStateRequestRequestTypeDef(BaseValidatorModel):
    QueryId: str

class GetQueryStatisticsRequestRequestTypeDef(BaseValidatorModel):
    QueryId: str

class PlanningStatisticsTypeDef(BaseValidatorModel):
    EstimatedDataToScanBytes: Optional[int] = None
    PlanningTimeMillis: Optional[int] = None
    QueueTimeMillis: Optional[int] = None
    WorkUnitsGeneratedCount: Optional[int] = None

class PartitionValueListTypeDef(BaseValidatorModel):
    Values: Sequence[str]

class GetWorkUnitResultsRequestRequestTypeDef(BaseValidatorModel):
    QueryId: str
    WorkUnitId: int
    WorkUnitToken: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetWorkUnitsRequestRequestTypeDef(BaseValidatorModel):
    QueryId: str
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class WorkUnitRangeTypeDef(BaseValidatorModel):
    WorkUnitIdMax: int
    WorkUnitIdMin: int
    WorkUnitToken: str

class LFTagKeyResourceOutputTypeDef(BaseValidatorModel):
    TagKey: str
    TagValues: List[str]
    CatalogId: Optional[str] = None

class LFTagKeyResourceTypeDef(BaseValidatorModel):
    TagKey: str
    TagValues: Sequence[str]
    CatalogId: Optional[str] = None

class LFTagOutputTypeDef(BaseValidatorModel):
    TagKey: str
    TagValues: List[str]

class LFTagPairExtraOutputTypeDef(BaseValidatorModel):
    TagKey: str
    TagValues: List[str]
    CatalogId: Optional[str] = None

class LFTagPairTypeDef(BaseValidatorModel):
    TagKey: str
    TagValues: Sequence[str]
    CatalogId: Optional[str] = None

class LFTagTypeDef(BaseValidatorModel):
    TagKey: str
    TagValues: Sequence[str]

class TableResourceTypeDef(BaseValidatorModel):
    DatabaseName: str
    CatalogId: Optional[str] = None
    Name: Optional[str] = None
    TableWildcard: Optional[Mapping[str, Any]] = None

class ListLFTagsRequestRequestTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None
    ResourceShareType: Optional[ResourceShareTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTableStorageOptimizersRequestRequestTypeDef(BaseValidatorModel):
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

class ListTransactionsRequestRequestTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None
    StatusFilter: Optional[TransactionStatusFilterType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class TableObjectTypeDef(BaseValidatorModel):
    Uri: Optional[str] = None
    ETag: Optional[str] = None
    Size: Optional[int] = None

class RegisterResourceRequestRequestTypeDef(BaseValidatorModel):
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

class StartTransactionRequestRequestTypeDef(BaseValidatorModel):
    TransactionType: Optional[TransactionTypeType] = None

class TableResourceExtraOutputTypeDef(BaseValidatorModel):
    DatabaseName: str
    CatalogId: Optional[str] = None
    Name: Optional[str] = None
    TableWildcard: Optional[Dict[str, Any]] = None

class UpdateLFTagRequestRequestTypeDef(BaseValidatorModel):
    TagKey: str
    CatalogId: Optional[str] = None
    TagValuesToDelete: Optional[Sequence[str]] = None
    TagValuesToAdd: Optional[Sequence[str]] = None

class UpdateResourceRequestRequestTypeDef(BaseValidatorModel):
    RoleArn: str
    ResourceArn: str
    WithFederation: Optional[bool] = None
    HybridAccessEnabled: Optional[bool] = None

class UpdateTableStorageOptimizerRequestRequestTypeDef(BaseValidatorModel):
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

class TableWithColumnsResourceTypeDef(BaseValidatorModel):
    DatabaseName: str
    Name: str
    CatalogId: Optional[str] = None
    ColumnNames: Optional[Sequence[str]] = None
    ColumnWildcard: Optional[ColumnWildcardTypeDef] = None

class CreateLakeFormationIdentityCenterConfigurationRequestRequestTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None
    InstanceArn: Optional[str] = None
    ExternalFiltering: Optional[ExternalFilteringConfigurationTypeDef] = None
    ShareRecipients: Optional[Sequence[DataLakePrincipalTypeDef]] = None

class UpdateLakeFormationIdentityCenterConfigurationRequestRequestTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None
    ShareRecipients: Optional[Sequence[DataLakePrincipalTypeDef]] = None
    ApplicationStatus: Optional[ApplicationStatusType] = None
    ExternalFiltering: Optional[ExternalFilteringConfigurationTypeDef] = None

class DataCellsFilterExtraOutputTypeDef(BaseValidatorModel):
    TableCatalogId: str
    DatabaseName: str
    TableName: str
    Name: str
    RowFilter: Optional[RowFilterExtraOutputTypeDef] = None
    ColumnNames: Optional[List[str]] = None
    ColumnWildcard: Optional[ColumnWildcardExtraOutputTypeDef] = None
    VersionId: Optional[str] = None

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

class DeleteObjectsOnCancelRequestRequestTypeDef(BaseValidatorModel):
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

class ListResourcesRequestRequestTypeDef(BaseValidatorModel):
    FilterConditionList: Optional[Sequence[FilterConditionTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetQueryStatisticsResponseTypeDef(BaseValidatorModel):
    ExecutionStatistics: ExecutionStatisticsTypeDef
    PlanningStatistics: PlanningStatisticsTypeDef
    QuerySubmissionTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetTableObjectsRequestRequestTypeDef(BaseValidatorModel):
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

class GetTemporaryGluePartitionCredentialsRequestRequestTypeDef(BaseValidatorModel):
    TableArn: str
    Partition: PartitionValueListTypeDef
    Permissions: Optional[Sequence[PermissionType]] = None
    DurationSeconds: Optional[int] = None
    AuditContext: Optional[AuditContextTypeDef] = None
    SupportedPermissionTypes: Optional[Sequence[PermissionTypeType]] = None

class GetWorkUnitsRequestGetWorkUnitsPaginateTypeDef(BaseValidatorModel):
    QueryId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLFTagsRequestListLFTagsPaginateTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None
    ResourceShareType: Optional[ResourceShareTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetWorkUnitsResponseTypeDef(BaseValidatorModel):
    QueryId: str
    WorkUnitRanges: List[WorkUnitRangeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class LFTagPolicyResourceOutputTypeDef(BaseValidatorModel):
    ResourceType: ResourceTypeType
    Expression: List[LFTagOutputTypeDef]
    CatalogId: Optional[str] = None

class LFTagPolicyResourceTypeDef(BaseValidatorModel):
    ResourceType: ResourceTypeType
    Expression: Sequence[LFTagTypeDef]
    CatalogId: Optional[str] = None

class ListDataCellsFilterRequestListDataCellsFilterPaginateTypeDef(BaseValidatorModel):
    Table: Optional[TableResourceTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataCellsFilterRequestRequestTypeDef(BaseValidatorModel):
    Table: Optional[TableResourceTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

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

class GetDataCellsFilterResponseTypeDef(BaseValidatorModel):
    DataCellsFilter: DataCellsFilterOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDataCellsFilterResponseTypeDef(BaseValidatorModel):
    DataCellsFilters: List[DataCellsFilterOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateDataCellsFilterRequestRequestTypeDef(BaseValidatorModel):
    TableData: DataCellsFilterTypeDef

class UpdateDataCellsFilterRequestRequestTypeDef(BaseValidatorModel):
    TableData: DataCellsFilterTypeDef

class SearchDatabasesByLFTagsResponseTypeDef(BaseValidatorModel):
    DatabaseList: List[TaggedDatabaseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateTableObjectsRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    WriteOperations: Sequence[WriteOperationTypeDef]
    CatalogId: Optional[str] = None
    TransactionId: Optional[str] = None

class StartQueryPlanningRequestRequestTypeDef(BaseValidatorModel):
    QueryPlanningContext: QueryPlanningContextTypeDef
    QueryString: str

class GetTemporaryGlueTableCredentialsRequestRequestTypeDef(BaseValidatorModel):
    TableArn: str
    Permissions: Optional[Sequence[PermissionType]] = None
    DurationSeconds: Optional[int] = None
    AuditContext: Optional[AuditContextTypeDef] = None
    SupportedPermissionTypes: Optional[Sequence[PermissionTypeType]] = None
    S3Path: Optional[str] = None
    QuerySessionContext: Optional[QuerySessionContextTypeDef] = None

class ResourceOutputTypeDef(BaseValidatorModel):
    Catalog: Optional[Dict[str, Any]] = None
    Database: Optional[DatabaseResourceTypeDef] = None
    Table: Optional[TableResourceOutputTypeDef] = None
    TableWithColumns: Optional[TableWithColumnsResourceOutputTypeDef] = None
    DataLocation: Optional[DataLocationResourceTypeDef] = None
    DataCellsFilter: Optional[DataCellsFilterResourceTypeDef] = None
    LFTag: Optional[LFTagKeyResourceOutputTypeDef] = None
    LFTagPolicy: Optional[LFTagPolicyResourceOutputTypeDef] = None

class ResourceTypeDef(BaseValidatorModel):
    Catalog: Optional[Mapping[str, Any]] = None
    Database: Optional[DatabaseResourceTypeDef] = None
    Table: Optional[TableResourceTypeDef] = None
    TableWithColumns: Optional[TableWithColumnsResourceTypeDef] = None
    DataLocation: Optional[DataLocationResourceTypeDef] = None
    DataCellsFilter: Optional[DataCellsFilterResourceTypeDef] = None
    LFTag: Optional[LFTagKeyResourceTypeDef] = None
    LFTagPolicy: Optional[LFTagPolicyResourceTypeDef] = None

class SearchDatabasesByLFTagsRequestRequestTypeDef(BaseValidatorModel):
    Expression: Sequence[LFTagUnionTypeDef]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CatalogId: Optional[str] = None

class SearchDatabasesByLFTagsRequestSearchDatabasesByLFTagsPaginateTypeDef(BaseValidatorModel):
    Expression: Sequence[LFTagUnionTypeDef]
    CatalogId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchTablesByLFTagsRequestRequestTypeDef(BaseValidatorModel):
    Expression: Sequence[LFTagUnionTypeDef]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CatalogId: Optional[str] = None

class SearchTablesByLFTagsRequestSearchTablesByLFTagsPaginateTypeDef(BaseValidatorModel):
    Expression: Sequence[LFTagUnionTypeDef]
    CatalogId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetTableObjectsResponseTypeDef(BaseValidatorModel):
    Objects: List[PartitionObjectsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetDataLakeSettingsResponseTypeDef(BaseValidatorModel):
    DataLakeSettings: DataLakeSettingsOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutDataLakeSettingsRequestRequestTypeDef(BaseValidatorModel):
    DataLakeSettings: DataLakeSettingsTypeDef
    CatalogId: Optional[str] = None

class SearchTablesByLFTagsResponseTypeDef(BaseValidatorModel):
    TableList: List[TaggedTableTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BatchPermissionsRequestEntryOutputTypeDef(BaseValidatorModel):
    Id: str
    Principal: Optional[DataLakePrincipalTypeDef] = None
    Resource: Optional[ResourceOutputTypeDef] = None
    Permissions: Optional[List[PermissionType]] = None
    PermissionsWithGrantOption: Optional[List[PermissionType]] = None

class LakeFormationOptInsInfoTypeDef(BaseValidatorModel):
    Resource: Optional[ResourceOutputTypeDef] = None
    Principal: Optional[DataLakePrincipalTypeDef] = None
    LastModified: Optional[datetime] = None
    LastUpdatedBy: Optional[str] = None

class PrincipalResourcePermissionsTypeDef(BaseValidatorModel):
    Principal: Optional[DataLakePrincipalTypeDef] = None
    Resource: Optional[ResourceOutputTypeDef] = None
    Permissions: Optional[List[PermissionType]] = None
    PermissionsWithGrantOption: Optional[List[PermissionType]] = None
    AdditionalDetails: Optional[DetailsMapTypeDef] = None
    LastUpdated: Optional[datetime] = None
    LastUpdatedBy: Optional[str] = None

class AddLFTagsToResourceRequestRequestTypeDef(BaseValidatorModel):
    Resource: ResourceTypeDef
    LFTags: Sequence[LFTagPairUnionTypeDef]
    CatalogId: Optional[str] = None

class BatchPermissionsRequestEntryTypeDef(BaseValidatorModel):
    Id: str
    Principal: Optional[DataLakePrincipalTypeDef] = None
    Resource: Optional[ResourceTypeDef] = None
    Permissions: Optional[Sequence[PermissionType]] = None
    PermissionsWithGrantOption: Optional[Sequence[PermissionType]] = None

class CreateLakeFormationOptInRequestRequestTypeDef(BaseValidatorModel):
    Principal: DataLakePrincipalTypeDef
    Resource: ResourceTypeDef

class DeleteLakeFormationOptInRequestRequestTypeDef(BaseValidatorModel):
    Principal: DataLakePrincipalTypeDef
    Resource: ResourceTypeDef

class GetResourceLFTagsRequestRequestTypeDef(BaseValidatorModel):
    Resource: ResourceTypeDef
    CatalogId: Optional[str] = None
    ShowAssignedLFTags: Optional[bool] = None

class GrantPermissionsRequestRequestTypeDef(BaseValidatorModel):
    Principal: DataLakePrincipalTypeDef
    Resource: ResourceTypeDef
    Permissions: Sequence[PermissionType]
    CatalogId: Optional[str] = None
    PermissionsWithGrantOption: Optional[Sequence[PermissionType]] = None

class ListLakeFormationOptInsRequestRequestTypeDef(BaseValidatorModel):
    Principal: Optional[DataLakePrincipalTypeDef] = None
    Resource: Optional[ResourceTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListPermissionsRequestRequestTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None
    Principal: Optional[DataLakePrincipalTypeDef] = None
    ResourceType: Optional[DataLakeResourceTypeType] = None
    Resource: Optional[ResourceTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    IncludeRelated: Optional[str] = None

class RemoveLFTagsFromResourceRequestRequestTypeDef(BaseValidatorModel):
    Resource: ResourceTypeDef
    LFTags: Sequence[LFTagPairUnionTypeDef]
    CatalogId: Optional[str] = None

class RevokePermissionsRequestRequestTypeDef(BaseValidatorModel):
    Principal: DataLakePrincipalTypeDef
    Resource: ResourceTypeDef
    Permissions: Sequence[PermissionType]
    CatalogId: Optional[str] = None
    PermissionsWithGrantOption: Optional[Sequence[PermissionType]] = None

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

class BatchGrantPermissionsResponseTypeDef(BaseValidatorModel):
    Failures: List[BatchPermissionsFailureEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchRevokePermissionsResponseTypeDef(BaseValidatorModel):
    Failures: List[BatchPermissionsFailureEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGrantPermissionsRequestRequestTypeDef(BaseValidatorModel):
    Entries: Sequence[BatchPermissionsRequestEntryUnionTypeDef]
    CatalogId: Optional[str] = None

class BatchRevokePermissionsRequestRequestTypeDef(BaseValidatorModel):
    Entries: Sequence[BatchPermissionsRequestEntryUnionTypeDef]
    CatalogId: Optional[str] = None


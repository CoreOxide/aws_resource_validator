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
from aws_resource_validator.pydantic_models.lakeformation_constants import *

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AddObjectInputTypeDef(BaseModel):
    Uri: str
    ETag: str
    Size: int
    PartitionValues: Optional[Sequence[str]] = None

class AssumeDecoratedRoleWithSAMLRequestRequestTypeDef(BaseModel):
    SAMLAssertion: str
    RoleArn: str
    PrincipalArn: str
    DurationSeconds: Optional[int] = None

class AuditContextTypeDef(BaseModel):
    AdditionalAuditContext: Optional[str] = None

class ErrorDetailTypeDef(BaseModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class DataLakePrincipalTypeDef(BaseModel):
    DataLakePrincipalIdentifier: Optional[str] = None

class CancelTransactionRequestRequestTypeDef(BaseModel):
    TransactionId: str

class LFTagPairOutputTypeDef(BaseModel):
    TagKey: str
    TagValues: List[str]
    CatalogId: Optional[str] = None

class ColumnWildcardExtraOutputTypeDef(BaseModel):
    ExcludedColumnNames: Optional[List[str]] = None

class ColumnWildcardOutputTypeDef(BaseModel):
    ExcludedColumnNames: Optional[List[str]] = None

class ColumnWildcardTypeDef(BaseModel):
    ExcludedColumnNames: Optional[Sequence[str]] = None

class CommitTransactionRequestRequestTypeDef(BaseModel):
    TransactionId: str

class CreateLFTagRequestRequestTypeDef(BaseModel):
    TagKey: str
    TagValues: Sequence[str]
    CatalogId: Optional[str] = None

class ExternalFilteringConfigurationTypeDef(BaseModel):
    Status: EnableStatusType
    AuthorizedTargets: Sequence[str]

class RowFilterExtraOutputTypeDef(BaseModel):
    FilterExpression: Optional[str] = None
    AllRowsWildcard: Optional[Dict[str, Any]] = None

class RowFilterOutputTypeDef(BaseModel):
    FilterExpression: Optional[str] = None
    AllRowsWildcard: Optional[Dict[str, Any]] = None

class DataCellsFilterResourceTypeDef(BaseModel):
    TableCatalogId: Optional[str] = None
    DatabaseName: Optional[str] = None
    TableName: Optional[str] = None
    Name: Optional[str] = None

class RowFilterTypeDef(BaseModel):
    FilterExpression: Optional[str] = None
    AllRowsWildcard: Optional[Mapping[str, Any]] = None

class DataLocationResourceTypeDef(BaseModel):
    ResourceArn: str
    CatalogId: Optional[str] = None

class DatabaseResourceTypeDef(BaseModel):
    Name: str
    CatalogId: Optional[str] = None

class DeleteDataCellsFilterRequestRequestTypeDef(BaseModel):
    TableCatalogId: Optional[str] = None
    DatabaseName: Optional[str] = None
    TableName: Optional[str] = None
    Name: Optional[str] = None

class DeleteLFTagRequestRequestTypeDef(BaseModel):
    TagKey: str
    CatalogId: Optional[str] = None

class DeleteLakeFormationIdentityCenterConfigurationRequestRequestTypeDef(BaseModel):
    CatalogId: Optional[str] = None

class DeleteObjectInputTypeDef(BaseModel):
    Uri: str
    ETag: Optional[str] = None
    PartitionValues: Optional[Sequence[str]] = None

class VirtualObjectTypeDef(BaseModel):
    Uri: str
    ETag: Optional[str] = None

class DeregisterResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class DescribeLakeFormationIdentityCenterConfigurationRequestRequestTypeDef(BaseModel):
    CatalogId: Optional[str] = None

class ExternalFilteringConfigurationOutputTypeDef(BaseModel):
    Status: EnableStatusType
    AuthorizedTargets: List[str]

class DescribeResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class ResourceInfoTypeDef(BaseModel):
    ResourceArn: Optional[str] = None
    RoleArn: Optional[str] = None
    LastModified: Optional[datetime] = None
    WithFederation: Optional[bool] = None
    HybridAccessEnabled: Optional[bool] = None

class DescribeTransactionRequestRequestTypeDef(BaseModel):
    TransactionId: str

class TransactionDescriptionTypeDef(BaseModel):
    TransactionId: Optional[str] = None
    TransactionStatus: Optional[TransactionStatusType] = None
    TransactionStartTime: Optional[datetime] = None
    TransactionEndTime: Optional[datetime] = None

class DetailsMapTypeDef(BaseModel):
    ResourceShare: Optional[List[str]] = None

class ExecutionStatisticsTypeDef(BaseModel):
    AverageExecutionTimeMillis: Optional[int] = None
    DataScannedBytes: Optional[int] = None
    WorkUnitsExecutedCount: Optional[int] = None

class ExtendTransactionRequestRequestTypeDef(BaseModel):
    TransactionId: Optional[str] = None

class FilterConditionTypeDef(BaseModel):
    Field: Optional[FieldNameStringType] = None
    ComparisonOperator: Optional[ComparisonOperatorType] = None
    StringValueList: Optional[Sequence[str]] = None

class GetDataCellsFilterRequestRequestTypeDef(BaseModel):
    TableCatalogId: str
    DatabaseName: str
    TableName: str
    Name: str

class GetDataLakeSettingsRequestRequestTypeDef(BaseModel):
    CatalogId: Optional[str] = None

class GetEffectivePermissionsForPathRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    CatalogId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetLFTagRequestRequestTypeDef(BaseModel):
    TagKey: str
    CatalogId: Optional[str] = None

class GetQueryStateRequestRequestTypeDef(BaseModel):
    QueryId: str

class GetQueryStatisticsRequestRequestTypeDef(BaseModel):
    QueryId: str

class PlanningStatisticsTypeDef(BaseModel):
    EstimatedDataToScanBytes: Optional[int] = None
    PlanningTimeMillis: Optional[int] = None
    QueueTimeMillis: Optional[int] = None
    WorkUnitsGeneratedCount: Optional[int] = None

class PartitionValueListTypeDef(BaseModel):
    Values: Sequence[str]

class GetWorkUnitResultsRequestRequestTypeDef(BaseModel):
    QueryId: str
    WorkUnitId: int
    WorkUnitToken: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetWorkUnitsRequestRequestTypeDef(BaseModel):
    QueryId: str
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None

class WorkUnitRangeTypeDef(BaseModel):
    WorkUnitIdMax: int
    WorkUnitIdMin: int
    WorkUnitToken: str

class LFTagKeyResourceOutputTypeDef(BaseModel):
    TagKey: str
    TagValues: List[str]
    CatalogId: Optional[str] = None

class LFTagKeyResourceTypeDef(BaseModel):
    TagKey: str
    TagValues: Sequence[str]
    CatalogId: Optional[str] = None

class LFTagOutputTypeDef(BaseModel):
    TagKey: str
    TagValues: List[str]

class LFTagPairExtraOutputTypeDef(BaseModel):
    TagKey: str
    TagValues: List[str]
    CatalogId: Optional[str] = None

class LFTagPairTypeDef(BaseModel):
    TagKey: str
    TagValues: Sequence[str]
    CatalogId: Optional[str] = None

class LFTagTypeDef(BaseModel):
    TagKey: str
    TagValues: Sequence[str]

class TableResourceTypeDef(BaseModel):
    DatabaseName: str
    CatalogId: Optional[str] = None
    Name: Optional[str] = None
    TableWildcard: Optional[Mapping[str, Any]] = None

class ListLFTagsRequestRequestTypeDef(BaseModel):
    CatalogId: Optional[str] = None
    ResourceShareType: Optional[ResourceShareTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTableStorageOptimizersRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    StorageOptimizerType: Optional[OptimizerTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class StorageOptimizerTypeDef(BaseModel):
    StorageOptimizerType: Optional[OptimizerTypeType] = None
    Config: Optional[Dict[str, str]] = None
    ErrorMessage: Optional[str] = None
    Warnings: Optional[str] = None
    LastRunDetails: Optional[str] = None

class ListTransactionsRequestRequestTypeDef(BaseModel):
    CatalogId: Optional[str] = None
    StatusFilter: Optional[TransactionStatusFilterType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class TableObjectTypeDef(BaseModel):
    Uri: Optional[str] = None
    ETag: Optional[str] = None
    Size: Optional[int] = None

class RegisterResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    UseServiceLinkedRole: Optional[bool] = None
    RoleArn: Optional[str] = None
    WithFederation: Optional[bool] = None
    HybridAccessEnabled: Optional[bool] = None

class TableResourceOutputTypeDef(BaseModel):
    DatabaseName: str
    CatalogId: Optional[str] = None
    Name: Optional[str] = None
    TableWildcard: Optional[Dict[str, Any]] = None

class StartTransactionRequestRequestTypeDef(BaseModel):
    TransactionType: Optional[TransactionTypeType] = None

class TableResourceExtraOutputTypeDef(BaseModel):
    DatabaseName: str
    CatalogId: Optional[str] = None
    Name: Optional[str] = None
    TableWildcard: Optional[Dict[str, Any]] = None

class UpdateLFTagRequestRequestTypeDef(BaseModel):
    TagKey: str
    CatalogId: Optional[str] = None
    TagValuesToDelete: Optional[Sequence[str]] = None
    TagValuesToAdd: Optional[Sequence[str]] = None

class UpdateResourceRequestRequestTypeDef(BaseModel):
    RoleArn: str
    ResourceArn: str
    WithFederation: Optional[bool] = None
    HybridAccessEnabled: Optional[bool] = None

class UpdateTableStorageOptimizerRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    StorageOptimizerConfig: Mapping[OptimizerTypeType, Mapping[str, str]]
    CatalogId: Optional[str] = None

class AssumeDecoratedRoleWithSAMLResponseTypeDef(BaseModel):
    AccessKeyId: str
    SecretAccessKey: str
    SessionToken: str
    Expiration: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CommitTransactionResponseTypeDef(BaseModel):
    TransactionStatus: TransactionStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLakeFormationIdentityCenterConfigurationResponseTypeDef(BaseModel):
    ApplicationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDataLakePrincipalResponseTypeDef(BaseModel):
    Identity: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetLFTagResponseTypeDef(BaseModel):
    CatalogId: str
    TagKey: str
    TagValues: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetQueryStateResponseTypeDef(BaseModel):
    Error: str
    State: QueryStateStringType
    ResponseMetadata: ResponseMetadataTypeDef

class GetTemporaryGluePartitionCredentialsResponseTypeDef(BaseModel):
    AccessKeyId: str
    SecretAccessKey: str
    SessionToken: str
    Expiration: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetTemporaryGlueTableCredentialsResponseTypeDef(BaseModel):
    AccessKeyId: str
    SecretAccessKey: str
    SessionToken: str
    Expiration: datetime
    VendedS3Path: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetWorkUnitResultsResponseTypeDef(BaseModel):
    ResultStream: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class StartQueryPlanningResponseTypeDef(BaseModel):
    QueryId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartTransactionResponseTypeDef(BaseModel):
    TransactionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTableStorageOptimizerResponseTypeDef(BaseModel):
    Result: str
    ResponseMetadata: ResponseMetadataTypeDef

class PrincipalPermissionsOutputTypeDef(BaseModel):
    Principal: Optional[DataLakePrincipalTypeDef] = None
    Permissions: Optional[List[PermissionType]] = None

class PrincipalPermissionsTypeDef(BaseModel):
    Principal: Optional[DataLakePrincipalTypeDef] = None
    Permissions: Optional[Sequence[PermissionType]] = None

class ColumnLFTagTypeDef(BaseModel):
    Name: Optional[str] = None
    LFTags: Optional[List[LFTagPairOutputTypeDef]] = None

class LFTagErrorTypeDef(BaseModel):
    LFTag: Optional[LFTagPairOutputTypeDef] = None
    Error: Optional[ErrorDetailTypeDef] = None

class ListLFTagsResponseTypeDef(BaseModel):
    LFTags: List[LFTagPairOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TableWithColumnsResourceOutputTypeDef(BaseModel):
    DatabaseName: str
    Name: str
    CatalogId: Optional[str] = None
    ColumnNames: Optional[List[str]] = None
    ColumnWildcard: Optional[ColumnWildcardOutputTypeDef] = None

class TableWithColumnsResourceTypeDef(BaseModel):
    DatabaseName: str
    Name: str
    CatalogId: Optional[str] = None
    ColumnNames: Optional[Sequence[str]] = None
    ColumnWildcard: Optional[ColumnWildcardTypeDef] = None

class CreateLakeFormationIdentityCenterConfigurationRequestRequestTypeDef(BaseModel):
    CatalogId: Optional[str] = None
    InstanceArn: Optional[str] = None
    ExternalFiltering: Optional[ExternalFilteringConfigurationTypeDef] = None
    ShareRecipients: Optional[Sequence[DataLakePrincipalTypeDef]] = None

class UpdateLakeFormationIdentityCenterConfigurationRequestRequestTypeDef(BaseModel):
    CatalogId: Optional[str] = None
    ShareRecipients: Optional[Sequence[DataLakePrincipalTypeDef]] = None
    ApplicationStatus: Optional[ApplicationStatusType] = None
    ExternalFiltering: Optional[ExternalFilteringConfigurationTypeDef] = None

class DataCellsFilterExtraOutputTypeDef(BaseModel):
    TableCatalogId: str
    DatabaseName: str
    TableName: str
    Name: str
    RowFilter: Optional[RowFilterExtraOutputTypeDef] = None
    ColumnNames: Optional[List[str]] = None
    ColumnWildcard: Optional[ColumnWildcardExtraOutputTypeDef] = None
    VersionId: Optional[str] = None

class DataCellsFilterOutputTypeDef(BaseModel):
    TableCatalogId: str
    DatabaseName: str
    TableName: str
    Name: str
    RowFilter: Optional[RowFilterOutputTypeDef] = None
    ColumnNames: Optional[List[str]] = None
    ColumnWildcard: Optional[ColumnWildcardOutputTypeDef] = None
    VersionId: Optional[str] = None

class DataCellsFilterTypeDef(BaseModel):
    TableCatalogId: str
    DatabaseName: str
    TableName: str
    Name: str
    RowFilter: Optional[RowFilterTypeDef] = None
    ColumnNames: Optional[Sequence[str]] = None
    ColumnWildcard: Optional[ColumnWildcardTypeDef] = None
    VersionId: Optional[str] = None

class TaggedDatabaseTypeDef(BaseModel):
    Database: Optional[DatabaseResourceTypeDef] = None
    LFTags: Optional[List[LFTagPairOutputTypeDef]] = None

class WriteOperationTypeDef(BaseModel):
    AddObject: Optional[AddObjectInputTypeDef] = None
    DeleteObject: Optional[DeleteObjectInputTypeDef] = None

class DeleteObjectsOnCancelRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    TransactionId: str
    Objects: Sequence[VirtualObjectTypeDef]
    CatalogId: Optional[str] = None

class DescribeLakeFormationIdentityCenterConfigurationResponseTypeDef(BaseModel):
    CatalogId: str
    InstanceArn: str
    ApplicationArn: str
    ExternalFiltering: ExternalFilteringConfigurationOutputTypeDef
    ShareRecipients: List[DataLakePrincipalTypeDef]
    ResourceShare: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeResourceResponseTypeDef(BaseModel):
    ResourceInfo: ResourceInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourcesResponseTypeDef(BaseModel):
    ResourceInfoList: List[ResourceInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeTransactionResponseTypeDef(BaseModel):
    TransactionDescription: TransactionDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTransactionsResponseTypeDef(BaseModel):
    Transactions: List[TransactionDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListResourcesRequestRequestTypeDef(BaseModel):
    FilterConditionList: Optional[Sequence[FilterConditionTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetQueryStatisticsResponseTypeDef(BaseModel):
    ExecutionStatistics: ExecutionStatisticsTypeDef
    PlanningStatistics: PlanningStatisticsTypeDef
    QuerySubmissionTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetTableObjectsRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    TransactionId: Optional[str] = None
    QueryAsOfTime: Optional[TimestampTypeDef] = None
    PartitionPredicate: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class QueryPlanningContextTypeDef(BaseModel):
    DatabaseName: str
    CatalogId: Optional[str] = None
    QueryAsOfTime: Optional[TimestampTypeDef] = None
    QueryParameters: Optional[Mapping[str, str]] = None
    TransactionId: Optional[str] = None

class QuerySessionContextTypeDef(BaseModel):
    QueryId: Optional[str] = None
    QueryStartTime: Optional[TimestampTypeDef] = None
    ClusterId: Optional[str] = None
    QueryAuthorizationId: Optional[str] = None
    AdditionalContext: Optional[Mapping[str, str]] = None

class GetTemporaryGluePartitionCredentialsRequestRequestTypeDef(BaseModel):
    TableArn: str
    Partition: PartitionValueListTypeDef
    Permissions: Optional[Sequence[PermissionType]] = None
    DurationSeconds: Optional[int] = None
    AuditContext: Optional[AuditContextTypeDef] = None
    SupportedPermissionTypes: Optional[Sequence[PermissionTypeType]] = None

class GetWorkUnitsRequestGetWorkUnitsPaginateTypeDef(BaseModel):
    QueryId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLFTagsRequestListLFTagsPaginateTypeDef(BaseModel):
    CatalogId: Optional[str] = None
    ResourceShareType: Optional[ResourceShareTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetWorkUnitsResponseTypeDef(BaseModel):
    QueryId: str
    WorkUnitRanges: List[WorkUnitRangeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class LFTagPolicyResourceOutputTypeDef(BaseModel):
    ResourceType: ResourceTypeType
    Expression: List[LFTagOutputTypeDef]
    CatalogId: Optional[str] = None

class LFTagPolicyResourceTypeDef(BaseModel):
    ResourceType: ResourceTypeType
    Expression: Sequence[LFTagTypeDef]
    CatalogId: Optional[str] = None

class ListDataCellsFilterRequestListDataCellsFilterPaginateTypeDef(BaseModel):
    Table: Optional[TableResourceTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataCellsFilterRequestRequestTypeDef(BaseModel):
    Table: Optional[TableResourceTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTableStorageOptimizersResponseTypeDef(BaseModel):
    StorageOptimizerList: List[StorageOptimizerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PartitionObjectsTypeDef(BaseModel):
    PartitionValues: Optional[List[str]] = None
    Objects: Optional[List[TableObjectTypeDef]] = None

class DataLakeSettingsOutputTypeDef(BaseModel):
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

class DataLakeSettingsTypeDef(BaseModel):
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

class GetResourceLFTagsResponseTypeDef(BaseModel):
    LFTagOnDatabase: List[LFTagPairOutputTypeDef]
    LFTagsOnTable: List[LFTagPairOutputTypeDef]
    LFTagsOnColumns: List[ColumnLFTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TaggedTableTypeDef(BaseModel):
    Table: Optional[TableResourceOutputTypeDef] = None
    LFTagOnDatabase: Optional[List[LFTagPairOutputTypeDef]] = None
    LFTagsOnTable: Optional[List[LFTagPairOutputTypeDef]] = None
    LFTagsOnColumns: Optional[List[ColumnLFTagTypeDef]] = None

class AddLFTagsToResourceResponseTypeDef(BaseModel):
    Failures: List[LFTagErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveLFTagsFromResourceResponseTypeDef(BaseModel):
    Failures: List[LFTagErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDataCellsFilterResponseTypeDef(BaseModel):
    DataCellsFilter: DataCellsFilterOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDataCellsFilterResponseTypeDef(BaseModel):
    DataCellsFilters: List[DataCellsFilterOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateDataCellsFilterRequestRequestTypeDef(BaseModel):
    TableData: DataCellsFilterTypeDef

class UpdateDataCellsFilterRequestRequestTypeDef(BaseModel):
    TableData: DataCellsFilterTypeDef

class SearchDatabasesByLFTagsResponseTypeDef(BaseModel):
    DatabaseList: List[TaggedDatabaseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateTableObjectsRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    WriteOperations: Sequence[WriteOperationTypeDef]
    CatalogId: Optional[str] = None
    TransactionId: Optional[str] = None

class StartQueryPlanningRequestRequestTypeDef(BaseModel):
    QueryPlanningContext: QueryPlanningContextTypeDef
    QueryString: str

class GetTemporaryGlueTableCredentialsRequestRequestTypeDef(BaseModel):
    TableArn: str
    Permissions: Optional[Sequence[PermissionType]] = None
    DurationSeconds: Optional[int] = None
    AuditContext: Optional[AuditContextTypeDef] = None
    SupportedPermissionTypes: Optional[Sequence[PermissionTypeType]] = None
    S3Path: Optional[str] = None
    QuerySessionContext: Optional[QuerySessionContextTypeDef] = None

class ResourceOutputTypeDef(BaseModel):
    Catalog: Optional[Dict[str, Any]] = None
    Database: Optional[DatabaseResourceTypeDef] = None
    Table: Optional[TableResourceOutputTypeDef] = None
    TableWithColumns: Optional[TableWithColumnsResourceOutputTypeDef] = None
    DataLocation: Optional[DataLocationResourceTypeDef] = None
    DataCellsFilter: Optional[DataCellsFilterResourceTypeDef] = None
    LFTag: Optional[LFTagKeyResourceOutputTypeDef] = None
    LFTagPolicy: Optional[LFTagPolicyResourceOutputTypeDef] = None

class ResourceTypeDef(BaseModel):
    Catalog: Optional[Mapping[str, Any]] = None
    Database: Optional[DatabaseResourceTypeDef] = None
    Table: Optional[TableResourceTypeDef] = None
    TableWithColumns: Optional[TableWithColumnsResourceTypeDef] = None
    DataLocation: Optional[DataLocationResourceTypeDef] = None
    DataCellsFilter: Optional[DataCellsFilterResourceTypeDef] = None
    LFTag: Optional[LFTagKeyResourceTypeDef] = None
    LFTagPolicy: Optional[LFTagPolicyResourceTypeDef] = None

class SearchDatabasesByLFTagsRequestRequestTypeDef(BaseModel):
    Expression: Sequence[LFTagUnionTypeDef]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CatalogId: Optional[str] = None

class SearchDatabasesByLFTagsRequestSearchDatabasesByLFTagsPaginateTypeDef(BaseModel):
    Expression: Sequence[LFTagUnionTypeDef]
    CatalogId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchTablesByLFTagsRequestRequestTypeDef(BaseModel):
    Expression: Sequence[LFTagUnionTypeDef]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CatalogId: Optional[str] = None

class SearchTablesByLFTagsRequestSearchTablesByLFTagsPaginateTypeDef(BaseModel):
    Expression: Sequence[LFTagUnionTypeDef]
    CatalogId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetTableObjectsResponseTypeDef(BaseModel):
    Objects: List[PartitionObjectsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetDataLakeSettingsResponseTypeDef(BaseModel):
    DataLakeSettings: DataLakeSettingsOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutDataLakeSettingsRequestRequestTypeDef(BaseModel):
    DataLakeSettings: DataLakeSettingsTypeDef
    CatalogId: Optional[str] = None

class SearchTablesByLFTagsResponseTypeDef(BaseModel):
    TableList: List[TaggedTableTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BatchPermissionsRequestEntryOutputTypeDef(BaseModel):
    Id: str
    Principal: Optional[DataLakePrincipalTypeDef] = None
    Resource: Optional[ResourceOutputTypeDef] = None
    Permissions: Optional[List[PermissionType]] = None
    PermissionsWithGrantOption: Optional[List[PermissionType]] = None

class LakeFormationOptInsInfoTypeDef(BaseModel):
    Resource: Optional[ResourceOutputTypeDef] = None
    Principal: Optional[DataLakePrincipalTypeDef] = None
    LastModified: Optional[datetime] = None
    LastUpdatedBy: Optional[str] = None

class PrincipalResourcePermissionsTypeDef(BaseModel):
    Principal: Optional[DataLakePrincipalTypeDef] = None
    Resource: Optional[ResourceOutputTypeDef] = None
    Permissions: Optional[List[PermissionType]] = None
    PermissionsWithGrantOption: Optional[List[PermissionType]] = None
    AdditionalDetails: Optional[DetailsMapTypeDef] = None
    LastUpdated: Optional[datetime] = None
    LastUpdatedBy: Optional[str] = None

class AddLFTagsToResourceRequestRequestTypeDef(BaseModel):
    Resource: ResourceTypeDef
    LFTags: Sequence[LFTagPairUnionTypeDef]
    CatalogId: Optional[str] = None

class BatchPermissionsRequestEntryTypeDef(BaseModel):
    Id: str
    Principal: Optional[DataLakePrincipalTypeDef] = None
    Resource: Optional[ResourceTypeDef] = None
    Permissions: Optional[Sequence[PermissionType]] = None
    PermissionsWithGrantOption: Optional[Sequence[PermissionType]] = None

class CreateLakeFormationOptInRequestRequestTypeDef(BaseModel):
    Principal: DataLakePrincipalTypeDef
    Resource: ResourceTypeDef

class DeleteLakeFormationOptInRequestRequestTypeDef(BaseModel):
    Principal: DataLakePrincipalTypeDef
    Resource: ResourceTypeDef

class GetResourceLFTagsRequestRequestTypeDef(BaseModel):
    Resource: ResourceTypeDef
    CatalogId: Optional[str] = None
    ShowAssignedLFTags: Optional[bool] = None

class GrantPermissionsRequestRequestTypeDef(BaseModel):
    Principal: DataLakePrincipalTypeDef
    Resource: ResourceTypeDef
    Permissions: Sequence[PermissionType]
    CatalogId: Optional[str] = None
    PermissionsWithGrantOption: Optional[Sequence[PermissionType]] = None

class ListLakeFormationOptInsRequestRequestTypeDef(BaseModel):
    Principal: Optional[DataLakePrincipalTypeDef] = None
    Resource: Optional[ResourceTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListPermissionsRequestRequestTypeDef(BaseModel):
    CatalogId: Optional[str] = None
    Principal: Optional[DataLakePrincipalTypeDef] = None
    ResourceType: Optional[DataLakeResourceTypeType] = None
    Resource: Optional[ResourceTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    IncludeRelated: Optional[str] = None

class RemoveLFTagsFromResourceRequestRequestTypeDef(BaseModel):
    Resource: ResourceTypeDef
    LFTags: Sequence[LFTagPairUnionTypeDef]
    CatalogId: Optional[str] = None

class RevokePermissionsRequestRequestTypeDef(BaseModel):
    Principal: DataLakePrincipalTypeDef
    Resource: ResourceTypeDef
    Permissions: Sequence[PermissionType]
    CatalogId: Optional[str] = None
    PermissionsWithGrantOption: Optional[Sequence[PermissionType]] = None

class BatchPermissionsFailureEntryTypeDef(BaseModel):
    RequestEntry: Optional[BatchPermissionsRequestEntryOutputTypeDef] = None
    Error: Optional[ErrorDetailTypeDef] = None

class ListLakeFormationOptInsResponseTypeDef(BaseModel):
    LakeFormationOptInsInfoList: List[LakeFormationOptInsInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetEffectivePermissionsForPathResponseTypeDef(BaseModel):
    Permissions: List[PrincipalResourcePermissionsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListPermissionsResponseTypeDef(BaseModel):
    PrincipalResourcePermissions: List[PrincipalResourcePermissionsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BatchGrantPermissionsResponseTypeDef(BaseModel):
    Failures: List[BatchPermissionsFailureEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchRevokePermissionsResponseTypeDef(BaseModel):
    Failures: List[BatchPermissionsFailureEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGrantPermissionsRequestRequestTypeDef(BaseModel):
    Entries: Sequence[BatchPermissionsRequestEntryUnionTypeDef]
    CatalogId: Optional[str] = None

class BatchRevokePermissionsRequestRequestTypeDef(BaseModel):
    Entries: Sequence[BatchPermissionsRequestEntryUnionTypeDef]
    CatalogId: Optional[str] = None


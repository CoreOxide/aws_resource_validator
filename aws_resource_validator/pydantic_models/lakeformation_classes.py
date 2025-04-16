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

class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AddObjectInput(BaseValidatorModel):
    Uri: str
    ETag: str
    Size: int
    PartitionValues: Optional[Sequence[str]] = None


class AssumeDecoratedRoleWithSAMLRequest(BaseValidatorModel):
    SAMLAssertion: str
    RoleArn: str
    PrincipalArn: str
    DurationSeconds: Optional[int] = None


class AuditContext(BaseValidatorModel):
    AdditionalAuditContext: Optional[str] = None


class ErrorDetail(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class DataLakePrincipal(BaseValidatorModel):
    DataLakePrincipalIdentifier: Optional[str] = None


class CancelTransactionRequest(BaseValidatorModel):
    TransactionId: str


class CatalogResource(BaseValidatorModel):
    Id: Optional[str] = None


class LFTagPairOutput(BaseValidatorModel):
    TagKey: str
    TagValues: List[str]
    CatalogId: Optional[str] = None


class ColumnWildcardOutput(BaseValidatorModel):
    ExcludedColumnNames: Optional[List[str]] = None


class ColumnWildcard(BaseValidatorModel):
    ExcludedColumnNames: Optional[Sequence[str]] = None


class CommitTransactionRequest(BaseValidatorModel):
    TransactionId: str


class Condition(BaseValidatorModel):
    Expression: Optional[str] = None


class CreateLFTagRequest(BaseValidatorModel):
    TagKey: str
    TagValues: Sequence[str]
    CatalogId: Optional[str] = None


class RowFilterOutput(BaseValidatorModel):
    FilterExpression: Optional[str] = None
    AllRowsWildcard: Optional[Dict[str, Any]] = None


class DataCellsFilterResource(BaseValidatorModel):
    TableCatalogId: Optional[str] = None
    DatabaseName: Optional[str] = None
    TableName: Optional[str] = None
    Name: Optional[str] = None


class RowFilter(BaseValidatorModel):
    FilterExpression: Optional[str] = None
    AllRowsWildcard: Optional[Mapping[str, Any]] = None


class DataLocationResource(BaseValidatorModel):
    ResourceArn: str
    CatalogId: Optional[str] = None


class DatabaseResource(BaseValidatorModel):
    Name: str
    CatalogId: Optional[str] = None


class DeleteDataCellsFilterRequest(BaseValidatorModel):
    TableCatalogId: Optional[str] = None
    DatabaseName: Optional[str] = None
    TableName: Optional[str] = None
    Name: Optional[str] = None


class DeleteLFTagExpressionRequest(BaseValidatorModel):
    Name: str
    CatalogId: Optional[str] = None


class DeleteLFTagRequest(BaseValidatorModel):
    TagKey: str
    CatalogId: Optional[str] = None


class DeleteLakeFormationIdentityCenterConfigurationRequest(BaseValidatorModel):
    CatalogId: Optional[str] = None


class DeleteObjectInput(BaseValidatorModel):
    Uri: str
    ETag: Optional[str] = None
    PartitionValues: Optional[Sequence[str]] = None


class VirtualObject(BaseValidatorModel):
    Uri: str
    ETag: Optional[str] = None


class DeregisterResourceRequest(BaseValidatorModel):
    ResourceArn: str


class DescribeLakeFormationIdentityCenterConfigurationRequest(BaseValidatorModel):
    CatalogId: Optional[str] = None


class ExternalFilteringConfigurationOutput(BaseValidatorModel):
    Status: EnableStatusType
    AuthorizedTargets: List[str]


class DescribeResourceRequest(BaseValidatorModel):
    ResourceArn: str


class ResourceInfo(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    RoleArn: Optional[str] = None
    LastModified: Optional[datetime] = None
    WithFederation: Optional[bool] = None
    HybridAccessEnabled: Optional[bool] = None


class DescribeTransactionRequest(BaseValidatorModel):
    TransactionId: str


class TransactionDescription(BaseValidatorModel):
    TransactionId: Optional[str] = None
    TransactionStatus: Optional[TransactionStatusType] = None
    TransactionStartTime: Optional[datetime] = None
    TransactionEndTime: Optional[datetime] = None


class DetailsMap(BaseValidatorModel):
    ResourceShare: Optional[List[str]] = None


class ExecutionStatistics(BaseValidatorModel):
    AverageExecutionTimeMillis: Optional[int] = None
    DataScannedBytes: Optional[int] = None
    WorkUnitsExecutedCount: Optional[int] = None


class ExtendTransactionRequest(BaseValidatorModel):
    TransactionId: Optional[str] = None


class ExternalFilteringConfiguration(BaseValidatorModel):
    Status: EnableStatusType
    AuthorizedTargets: Sequence[str]


class FilterCondition(BaseValidatorModel):
    Field: Optional[FieldNameStringType] = None
    ComparisonOperator: Optional[ComparisonOperatorType] = None
    StringValueList: Optional[Sequence[str]] = None


class GetDataCellsFilterRequest(BaseValidatorModel):
    TableCatalogId: str
    DatabaseName: str
    TableName: str
    Name: str


class GetDataLakeSettingsRequest(BaseValidatorModel):
    CatalogId: Optional[str] = None


class GetEffectivePermissionsForPathRequest(BaseValidatorModel):
    ResourceArn: str
    CatalogId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetLFTagExpressionRequest(BaseValidatorModel):
    Name: str
    CatalogId: Optional[str] = None


class LFTagOutput(BaseValidatorModel):
    TagKey: str
    TagValues: List[str]


class GetLFTagRequest(BaseValidatorModel):
    TagKey: str
    CatalogId: Optional[str] = None


class GetQueryStateRequest(BaseValidatorModel):
    QueryId: str


class GetQueryStatisticsRequest(BaseValidatorModel):
    QueryId: str


class PlanningStatistics(BaseValidatorModel):
    EstimatedDataToScanBytes: Optional[int] = None
    PlanningTimeMillis: Optional[int] = None
    QueueTimeMillis: Optional[int] = None
    WorkUnitsGeneratedCount: Optional[int] = None


class PartitionValueList(BaseValidatorModel):
    Values: Sequence[str]


class GetWorkUnitResultsRequest(BaseValidatorModel):
    QueryId: str
    WorkUnitId: int
    WorkUnitToken: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetWorkUnitsRequest(BaseValidatorModel):
    QueryId: str
    NextToken: Optional[str] = None
    PageSize: Optional[int] = None


class WorkUnitRange(BaseValidatorModel):
    WorkUnitIdMax: int
    WorkUnitIdMin: int
    WorkUnitToken: str


class LFTagExpressionResource(BaseValidatorModel):
    Name: str
    CatalogId: Optional[str] = None


class LFTagKeyResourceOutput(BaseValidatorModel):
    TagKey: str
    TagValues: List[str]
    CatalogId: Optional[str] = None


class LFTagKeyResource(BaseValidatorModel):
    TagKey: str
    TagValues: Sequence[str]
    CatalogId: Optional[str] = None


class LFTagPair(BaseValidatorModel):
    TagKey: str
    TagValues: Sequence[str]
    CatalogId: Optional[str] = None


class LFTag(BaseValidatorModel):
    TagKey: str
    TagValues: Sequence[str]


class ListLFTagExpressionsRequest(BaseValidatorModel):
    CatalogId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListLFTagsRequest(BaseValidatorModel):
    CatalogId: Optional[str] = None
    ResourceShareType: Optional[ResourceShareTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTableStorageOptimizersRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    StorageOptimizerType: Optional[OptimizerTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class StorageOptimizer(BaseValidatorModel):
    StorageOptimizerType: Optional[OptimizerTypeType] = None
    Config: Optional[Dict[str, str]] = None
    ErrorMessage: Optional[str] = None
    Warnings: Optional[str] = None
    LastRunDetails: Optional[str] = None


class ListTransactionsRequest(BaseValidatorModel):
    CatalogId: Optional[str] = None
    StatusFilter: Optional[TransactionStatusFilterType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class TableObject(BaseValidatorModel):
    Uri: Optional[str] = None
    ETag: Optional[str] = None
    Size: Optional[int] = None


class RegisterResourceRequest(BaseValidatorModel):
    ResourceArn: str
    UseServiceLinkedRole: Optional[bool] = None
    RoleArn: Optional[str] = None
    WithFederation: Optional[bool] = None
    HybridAccessEnabled: Optional[bool] = None


class TableResourceOutput(BaseValidatorModel):
    DatabaseName: str
    CatalogId: Optional[str] = None
    Name: Optional[str] = None
    TableWildcard: Optional[Dict[str, Any]] = None


class StartTransactionRequest(BaseValidatorModel):
    TransactionType: Optional[TransactionTypeType] = None


class TableResource(BaseValidatorModel):
    DatabaseName: str
    CatalogId: Optional[str] = None
    Name: Optional[str] = None
    TableWildcard: Optional[Mapping[str, Any]] = None


class UpdateLFTagRequest(BaseValidatorModel):
    TagKey: str
    CatalogId: Optional[str] = None
    TagValuesToDelete: Optional[Sequence[str]] = None
    TagValuesToAdd: Optional[Sequence[str]] = None


class UpdateResourceRequest(BaseValidatorModel):
    RoleArn: str
    ResourceArn: str
    WithFederation: Optional[bool] = None
    HybridAccessEnabled: Optional[bool] = None


class UpdateTableStorageOptimizerRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    StorageOptimizerConfig: Mapping[OptimizerTypeType, Mapping[str, str]]
    CatalogId: Optional[str] = None


class AssumeDecoratedRoleWithSAMLResponse(BaseValidatorModel):
    AccessKeyId: str
    SecretAccessKey: str
    SessionToken: str
    Expiration: datetime
    ResponseMetadata: ResponseMetadata


class CommitTransactionResponse(BaseValidatorModel):
    TransactionStatus: TransactionStatusType
    ResponseMetadata: ResponseMetadata


class CreateLakeFormationIdentityCenterConfigurationResponse(BaseValidatorModel):
    ApplicationArn: str
    ResponseMetadata: ResponseMetadata


class GetDataLakePrincipalResponse(BaseValidatorModel):
    Identity: str
    ResponseMetadata: ResponseMetadata


class GetLFTagResponse(BaseValidatorModel):
    CatalogId: str
    TagKey: str
    TagValues: List[str]
    ResponseMetadata: ResponseMetadata


class GetQueryStateResponse(BaseValidatorModel):
    Error: str
    State: QueryStateStringType
    ResponseMetadata: ResponseMetadata


class GetTemporaryGluePartitionCredentialsResponse(BaseValidatorModel):
    AccessKeyId: str
    SecretAccessKey: str
    SessionToken: str
    Expiration: datetime
    ResponseMetadata: ResponseMetadata


class GetTemporaryGlueTableCredentialsResponse(BaseValidatorModel):
    AccessKeyId: str
    SecretAccessKey: str
    SessionToken: str
    Expiration: datetime
    VendedS3Path: List[str]
    ResponseMetadata: ResponseMetadata


class GetWorkUnitResultsResponse(BaseValidatorModel):
    ResultStream: StreamingBody
    ResponseMetadata: ResponseMetadata


class StartQueryPlanningResponse(BaseValidatorModel):
    QueryId: str
    ResponseMetadata: ResponseMetadata


class StartTransactionResponse(BaseValidatorModel):
    TransactionId: str
    ResponseMetadata: ResponseMetadata


class UpdateTableStorageOptimizerResponse(BaseValidatorModel):
    Result: str
    ResponseMetadata: ResponseMetadata


class PrincipalPermissionsOutput(BaseValidatorModel):
    Principal: Optional[DataLakePrincipal] = None
    Permissions: Optional[List[PermissionType]] = None


class PrincipalPermissions(BaseValidatorModel):
    Principal: Optional[DataLakePrincipal] = None
    Permissions: Optional[Sequence[PermissionType]] = None


class ColumnLFTag(BaseValidatorModel):
    Name: Optional[str] = None
    LFTags: Optional[List[LFTagPairOutput]] = None


class LFTagError(BaseValidatorModel):
    LFTag: Optional[LFTagPairOutput] = None
    Error: Optional[ErrorDetail] = None


class ListLFTagsResponse(BaseValidatorModel):
    LFTags: List[LFTagPairOutput]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TableWithColumnsResourceOutput(BaseValidatorModel):
    DatabaseName: str
    Name: str
    CatalogId: Optional[str] = None
    ColumnNames: Optional[List[str]] = None
    ColumnWildcard: Optional[ColumnWildcardOutput] = None


class DataCellsFilterOutput(BaseValidatorModel):
    TableCatalogId: str
    DatabaseName: str
    TableName: str
    Name: str
    RowFilter: Optional[RowFilterOutput] = None
    ColumnNames: Optional[List[str]] = None
    ColumnWildcard: Optional[ColumnWildcardOutput] = None
    VersionId: Optional[str] = None


class DataCellsFilter(BaseValidatorModel):
    TableCatalogId: str
    DatabaseName: str
    TableName: str
    Name: str
    RowFilter: Optional[RowFilter] = None
    ColumnNames: Optional[Sequence[str]] = None
    ColumnWildcard: Optional[ColumnWildcard] = None
    VersionId: Optional[str] = None


class TaggedDatabase(BaseValidatorModel):
    Database: Optional[DatabaseResource] = None
    LFTags: Optional[List[LFTagPairOutput]] = None


class WriteOperation(BaseValidatorModel):
    AddObject: Optional[AddObjectInput] = None
    DeleteObject: Optional[DeleteObjectInput] = None


class DeleteObjectsOnCancelRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    TransactionId: str
    Objects: Sequence[VirtualObject]
    CatalogId: Optional[str] = None


class DescribeLakeFormationIdentityCenterConfigurationResponse(BaseValidatorModel):
    CatalogId: str
    InstanceArn: str
    ApplicationArn: str
    ExternalFiltering: ExternalFilteringConfigurationOutput
    ShareRecipients: List[DataLakePrincipal]
    ResourceShare: str
    ResponseMetadata: ResponseMetadata


class DescribeResourceResponse(BaseValidatorModel):
    ResourceInfo: ResourceInfo
    ResponseMetadata: ResponseMetadata


class ListResourcesResponse(BaseValidatorModel):
    ResourceInfoList: List[ResourceInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeTransactionResponse(BaseValidatorModel):
    TransactionDescription: TransactionDescription
    ResponseMetadata: ResponseMetadata


class ListTransactionsResponse(BaseValidatorModel):
    Transactions: List[TransactionDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListResourcesRequest(BaseValidatorModel):
    FilterConditionList: Optional[Sequence[FilterCondition]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetLFTagExpressionResponse(BaseValidatorModel):
    Name: str
    Description: str
    CatalogId: str
    Expression: List[LFTagOutput]
    ResponseMetadata: ResponseMetadata


class LFTagExpression(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    CatalogId: Optional[str] = None
    Expression: Optional[List[LFTagOutput]] = None


class LFTagPolicyResourceOutput(BaseValidatorModel):
    ResourceType: ResourceTypeType
    CatalogId: Optional[str] = None
    Expression: Optional[List[LFTagOutput]] = None
    ExpressionName: Optional[str] = None


class GetQueryStatisticsResponse(BaseValidatorModel):
    ExecutionStatistics: ExecutionStatistics
    PlanningStatistics: PlanningStatistics
    QuerySubmissionTime: datetime
    ResponseMetadata: ResponseMetadata


class Timestamp(BaseValidatorModel):
    pass


class GetTableObjectsRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    TransactionId: Optional[str] = None
    QueryAsOfTime: Optional[Timestamp] = None
    PartitionPredicate: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class QueryPlanningContext(BaseValidatorModel):
    DatabaseName: str
    CatalogId: Optional[str] = None
    QueryAsOfTime: Optional[Timestamp] = None
    QueryParameters: Optional[Mapping[str, str]] = None
    TransactionId: Optional[str] = None


class QuerySessionContext(BaseValidatorModel):
    QueryId: Optional[str] = None
    QueryStartTime: Optional[Timestamp] = None
    ClusterId: Optional[str] = None
    QueryAuthorizationId: Optional[str] = None
    AdditionalContext: Optional[Mapping[str, str]] = None


class GetTemporaryGluePartitionCredentialsRequest(BaseValidatorModel):
    TableArn: str
    Partition: PartitionValueList
    Permissions: Optional[Sequence[PermissionType]] = None
    DurationSeconds: Optional[int] = None
    AuditContext: Optional[AuditContext] = None
    SupportedPermissionTypes: Optional[Sequence[PermissionTypeType]] = None


class GetWorkUnitsRequestPaginate(BaseValidatorModel):
    QueryId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLFTagExpressionsRequestPaginate(BaseValidatorModel):
    CatalogId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLFTagsRequestPaginate(BaseValidatorModel):
    CatalogId: Optional[str] = None
    ResourceShareType: Optional[ResourceShareTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetWorkUnitsResponse(BaseValidatorModel):
    QueryId: str
    WorkUnitRanges: List[WorkUnitRange]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTableStorageOptimizersResponse(BaseValidatorModel):
    StorageOptimizerList: List[StorageOptimizer]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PartitionObjects(BaseValidatorModel):
    PartitionValues: Optional[List[str]] = None
    Objects: Optional[List[TableObject]] = None


class DataLakeSettingsOutput(BaseValidatorModel):
    DataLakeAdmins: Optional[List[DataLakePrincipal]] = None
    ReadOnlyAdmins: Optional[List[DataLakePrincipal]] = None
    CreateDatabaseDefaultPermissions: Optional[List[PrincipalPermissionsOutput]] = None
    CreateTableDefaultPermissions: Optional[List[PrincipalPermissionsOutput]] = None
    Parameters: Optional[Dict[str, str]] = None
    TrustedResourceOwners: Optional[List[str]] = None
    AllowExternalDataFiltering: Optional[bool] = None
    AllowFullTableExternalDataAccess: Optional[bool] = None
    ExternalDataFilteringAllowList: Optional[List[DataLakePrincipal]] = None
    AuthorizedSessionTagValueList: Optional[List[str]] = None


class DataLakeSettings(BaseValidatorModel):
    DataLakeAdmins: Optional[Sequence[DataLakePrincipal]] = None
    ReadOnlyAdmins: Optional[Sequence[DataLakePrincipal]] = None
    CreateDatabaseDefaultPermissions: Optional[Sequence[PrincipalPermissions]] = None
    CreateTableDefaultPermissions: Optional[Sequence[PrincipalPermissions]] = None
    Parameters: Optional[Mapping[str, str]] = None
    TrustedResourceOwners: Optional[Sequence[str]] = None
    AllowExternalDataFiltering: Optional[bool] = None
    AllowFullTableExternalDataAccess: Optional[bool] = None
    ExternalDataFilteringAllowList: Optional[Sequence[DataLakePrincipal]] = None
    AuthorizedSessionTagValueList: Optional[Sequence[str]] = None


class GetResourceLFTagsResponse(BaseValidatorModel):
    LFTagOnDatabase: List[LFTagPairOutput]
    LFTagsOnTable: List[LFTagPairOutput]
    LFTagsOnColumns: List[ColumnLFTag]
    ResponseMetadata: ResponseMetadata


class TaggedTable(BaseValidatorModel):
    Table: Optional[TableResourceOutput] = None
    LFTagOnDatabase: Optional[List[LFTagPairOutput]] = None
    LFTagsOnTable: Optional[List[LFTagPairOutput]] = None
    LFTagsOnColumns: Optional[List[ColumnLFTag]] = None


class AddLFTagsToResourceResponse(BaseValidatorModel):
    Failures: List[LFTagError]
    ResponseMetadata: ResponseMetadata


class RemoveLFTagsFromResourceResponse(BaseValidatorModel):
    Failures: List[LFTagError]
    ResponseMetadata: ResponseMetadata


class ColumnWildcardUnion(BaseValidatorModel):
    pass


class TableWithColumnsResource(BaseValidatorModel):
    DatabaseName: str
    Name: str
    CatalogId: Optional[str] = None
    ColumnNames: Optional[Sequence[str]] = None
    ColumnWildcard: Optional[ColumnWildcardUnion] = None


class GetDataCellsFilterResponse(BaseValidatorModel):
    DataCellsFilter: DataCellsFilterOutput
    ResponseMetadata: ResponseMetadata


class ListDataCellsFilterResponse(BaseValidatorModel):
    DataCellsFilters: List[DataCellsFilterOutput]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SearchDatabasesByLFTagsResponse(BaseValidatorModel):
    DatabaseList: List[TaggedDatabase]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateTableObjectsRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    WriteOperations: Sequence[WriteOperation]
    CatalogId: Optional[str] = None
    TransactionId: Optional[str] = None


class ExternalFilteringConfigurationUnion(BaseValidatorModel):
    pass


class CreateLakeFormationIdentityCenterConfigurationRequest(BaseValidatorModel):
    CatalogId: Optional[str] = None
    InstanceArn: Optional[str] = None
    ExternalFiltering: Optional[ExternalFilteringConfigurationUnion] = None
    ShareRecipients: Optional[Sequence[DataLakePrincipal]] = None


class UpdateLakeFormationIdentityCenterConfigurationRequest(BaseValidatorModel):
    CatalogId: Optional[str] = None
    ShareRecipients: Optional[Sequence[DataLakePrincipal]] = None
    ApplicationStatus: Optional[ApplicationStatusType] = None
    ExternalFiltering: Optional[ExternalFilteringConfigurationUnion] = None


class ListLFTagExpressionsResponse(BaseValidatorModel):
    LFTagExpressions: List[LFTagExpression]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ResourceOutput(BaseValidatorModel):
    Catalog: Optional[CatalogResource] = None
    Database: Optional[DatabaseResource] = None
    Table: Optional[TableResourceOutput] = None
    TableWithColumns: Optional[TableWithColumnsResourceOutput] = None
    DataLocation: Optional[DataLocationResource] = None
    DataCellsFilter: Optional[DataCellsFilterResource] = None
    LFTag: Optional[LFTagKeyResourceOutput] = None
    LFTagPolicy: Optional[LFTagPolicyResourceOutput] = None
    LFTagExpression: Optional[LFTagExpressionResource] = None


class StartQueryPlanningRequest(BaseValidatorModel):
    QueryPlanningContext: QueryPlanningContext
    QueryString: str


class GetTemporaryGlueTableCredentialsRequest(BaseValidatorModel):
    TableArn: str
    Permissions: Optional[Sequence[PermissionType]] = None
    DurationSeconds: Optional[int] = None
    AuditContext: Optional[AuditContext] = None
    SupportedPermissionTypes: Optional[Sequence[PermissionTypeType]] = None
    S3Path: Optional[str] = None
    QuerySessionContext: Optional[QuerySessionContext] = None


class LFTagUnion(BaseValidatorModel):
    pass


class CreateLFTagExpressionRequest(BaseValidatorModel):
    Name: str
    Expression: Sequence[LFTagUnion]
    Description: Optional[str] = None
    CatalogId: Optional[str] = None


class LFTagPolicyResource(BaseValidatorModel):
    ResourceType: ResourceTypeType
    CatalogId: Optional[str] = None
    Expression: Optional[Sequence[LFTagUnion]] = None
    ExpressionName: Optional[str] = None


class SearchDatabasesByLFTagsRequestPaginate(BaseValidatorModel):
    Expression: Sequence[LFTagUnion]
    CatalogId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchDatabasesByLFTagsRequest(BaseValidatorModel):
    Expression: Sequence[LFTagUnion]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CatalogId: Optional[str] = None


class SearchTablesByLFTagsRequestPaginate(BaseValidatorModel):
    Expression: Sequence[LFTagUnion]
    CatalogId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchTablesByLFTagsRequest(BaseValidatorModel):
    Expression: Sequence[LFTagUnion]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CatalogId: Optional[str] = None


class UpdateLFTagExpressionRequest(BaseValidatorModel):
    Name: str
    Expression: Sequence[LFTagUnion]
    Description: Optional[str] = None
    CatalogId: Optional[str] = None


class GetTableObjectsResponse(BaseValidatorModel):
    Objects: List[PartitionObjects]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TableResourceUnion(BaseValidatorModel):
    pass


class ListDataCellsFilterRequestPaginate(BaseValidatorModel):
    Table: Optional[TableResourceUnion] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDataCellsFilterRequest(BaseValidatorModel):
    Table: Optional[TableResourceUnion] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetDataLakeSettingsResponse(BaseValidatorModel):
    DataLakeSettings: DataLakeSettingsOutput
    ResponseMetadata: ResponseMetadata


class SearchTablesByLFTagsResponse(BaseValidatorModel):
    TableList: List[TaggedTable]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DataCellsFilterUnion(BaseValidatorModel):
    pass


class CreateDataCellsFilterRequest(BaseValidatorModel):
    TableData: DataCellsFilterUnion


class UpdateDataCellsFilterRequest(BaseValidatorModel):
    TableData: DataCellsFilterUnion


class BatchPermissionsRequestEntryOutput(BaseValidatorModel):
    Id: str
    Principal: Optional[DataLakePrincipal] = None
    Resource: Optional[ResourceOutput] = None
    Permissions: Optional[List[PermissionType]] = None
    PermissionsWithGrantOption: Optional[List[PermissionType]] = None


class LakeFormationOptInsInfo(BaseValidatorModel):
    Resource: Optional[ResourceOutput] = None
    Principal: Optional[DataLakePrincipal] = None
    Condition: Optional[Condition] = None
    LastModified: Optional[datetime] = None
    LastUpdatedBy: Optional[str] = None


class PrincipalResourcePermissions(BaseValidatorModel):
    Principal: Optional[DataLakePrincipal] = None
    Resource: Optional[ResourceOutput] = None
    Condition: Optional[Condition] = None
    Permissions: Optional[List[PermissionType]] = None
    PermissionsWithGrantOption: Optional[List[PermissionType]] = None
    AdditionalDetails: Optional[DetailsMap] = None
    LastUpdated: Optional[datetime] = None
    LastUpdatedBy: Optional[str] = None


class DataLakeSettingsUnion(BaseValidatorModel):
    pass


class PutDataLakeSettingsRequest(BaseValidatorModel):
    DataLakeSettings: DataLakeSettingsUnion
    CatalogId: Optional[str] = None


class BatchPermissionsFailureEntry(BaseValidatorModel):
    RequestEntry: Optional[BatchPermissionsRequestEntryOutput] = None
    Error: Optional[ErrorDetail] = None


class ListLakeFormationOptInsResponse(BaseValidatorModel):
    LakeFormationOptInsInfoList: List[LakeFormationOptInsInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetEffectivePermissionsForPathResponse(BaseValidatorModel):
    Permissions: List[PrincipalResourcePermissions]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListPermissionsResponse(BaseValidatorModel):
    PrincipalResourcePermissions: List[PrincipalResourcePermissions]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TableWithColumnsResourceUnion(BaseValidatorModel):
    pass


class LFTagPolicyResourceUnion(BaseValidatorModel):
    pass


class LFTagKeyResourceUnion(BaseValidatorModel):
    pass


class Resource(BaseValidatorModel):
    Catalog: Optional[CatalogResource] = None
    Database: Optional[DatabaseResource] = None
    Table: Optional[TableResourceUnion] = None
    TableWithColumns: Optional[TableWithColumnsResourceUnion] = None
    DataLocation: Optional[DataLocationResource] = None
    DataCellsFilter: Optional[DataCellsFilterResource] = None
    LFTag: Optional[LFTagKeyResourceUnion] = None
    LFTagPolicy: Optional[LFTagPolicyResourceUnion] = None
    LFTagExpression: Optional[LFTagExpressionResource] = None


class BatchGrantPermissionsResponse(BaseValidatorModel):
    Failures: List[BatchPermissionsFailureEntry]
    ResponseMetadata: ResponseMetadata


class BatchRevokePermissionsResponse(BaseValidatorModel):
    Failures: List[BatchPermissionsFailureEntry]
    ResponseMetadata: ResponseMetadata


class ResourceUnion(BaseValidatorModel):
    pass


class LFTagPairUnion(BaseValidatorModel):
    pass


class AddLFTagsToResourceRequest(BaseValidatorModel):
    Resource: ResourceUnion
    LFTags: Sequence[LFTagPairUnion]
    CatalogId: Optional[str] = None


class BatchPermissionsRequestEntry(BaseValidatorModel):
    Id: str
    Principal: Optional[DataLakePrincipal] = None
    Resource: Optional[ResourceUnion] = None
    Permissions: Optional[Sequence[PermissionType]] = None
    PermissionsWithGrantOption: Optional[Sequence[PermissionType]] = None


class CreateLakeFormationOptInRequest(BaseValidatorModel):
    Principal: DataLakePrincipal
    Resource: ResourceUnion


class DeleteLakeFormationOptInRequest(BaseValidatorModel):
    Principal: DataLakePrincipal
    Resource: ResourceUnion


class GetResourceLFTagsRequest(BaseValidatorModel):
    Resource: ResourceUnion
    CatalogId: Optional[str] = None
    ShowAssignedLFTags: Optional[bool] = None


class GrantPermissionsRequest(BaseValidatorModel):
    Principal: DataLakePrincipal
    Resource: ResourceUnion
    Permissions: Sequence[PermissionType]
    CatalogId: Optional[str] = None
    PermissionsWithGrantOption: Optional[Sequence[PermissionType]] = None


class ListLakeFormationOptInsRequest(BaseValidatorModel):
    Principal: Optional[DataLakePrincipal] = None
    Resource: Optional[ResourceUnion] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListPermissionsRequest(BaseValidatorModel):
    CatalogId: Optional[str] = None
    Principal: Optional[DataLakePrincipal] = None
    ResourceType: Optional[DataLakeResourceTypeType] = None
    Resource: Optional[ResourceUnion] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    IncludeRelated: Optional[str] = None


class RemoveLFTagsFromResourceRequest(BaseValidatorModel):
    Resource: ResourceUnion
    LFTags: Sequence[LFTagPairUnion]
    CatalogId: Optional[str] = None


class RevokePermissionsRequest(BaseValidatorModel):
    Principal: DataLakePrincipal
    Resource: ResourceUnion
    Permissions: Sequence[PermissionType]
    CatalogId: Optional[str] = None
    PermissionsWithGrantOption: Optional[Sequence[PermissionType]] = None


class BatchPermissionsRequestEntryUnion(BaseValidatorModel):
    pass


class BatchGrantPermissionsRequest(BaseValidatorModel):
    Entries: Sequence[BatchPermissionsRequestEntryUnion]
    CatalogId: Optional[str] = None


class BatchRevokePermissionsRequest(BaseValidatorModel):
    Entries: Sequence[BatchPermissionsRequestEntryUnion]
    CatalogId: Optional[str] = None



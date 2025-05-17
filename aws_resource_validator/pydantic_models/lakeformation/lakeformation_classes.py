from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.lakeformation.lakeformation_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




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
    PartitionValues: Optional[List[str]] = None


# This class is the input for the 'assume_decorated_role_with_saml' function.
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
    ExcludedColumnNames: Optional[List[str]] = None


# This class is the input for the 'commit_transaction' function.
class CommitTransactionRequest(BaseValidatorModel):
    TransactionId: str


class Condition(BaseValidatorModel):
    Expression: Optional[str] = None


class CreateLFTagRequest(BaseValidatorModel):
    TagKey: str
    TagValues: List[str]
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
    AllRowsWildcard: Optional[Dict[str, Any]] = None


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
    PartitionValues: Optional[List[str]] = None


class VirtualObject(BaseValidatorModel):
    Uri: str
    ETag: Optional[str] = None


class DeregisterResourceRequest(BaseValidatorModel):
    ResourceArn: str


# This class is the input for the 'describe_lake_formation_identity_center_configuration' function.
class DescribeLakeFormationIdentityCenterConfigurationRequest(BaseValidatorModel):
    CatalogId: Optional[str] = None


class ExternalFilteringConfigurationOutput(BaseValidatorModel):
    Status: EnableStatusType
    AuthorizedTargets: List[str]


# This class is the input for the 'describe_resource' function.
class DescribeResourceRequest(BaseValidatorModel):
    ResourceArn: str


class ResourceInfo(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    RoleArn: Optional[str] = None
    LastModified: Optional[datetime] = None
    WithFederation: Optional[bool] = None
    HybridAccessEnabled: Optional[bool] = None


# This class is the input for the 'describe_transaction' function.
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
    AuthorizedTargets: List[str]


class FilterCondition(BaseValidatorModel):
    Field: Optional[FieldNameStringType] = None
    ComparisonOperator: Optional[ComparisonOperatorType] = None
    StringValueList: Optional[List[str]] = None


# This class is the input for the 'get_data_cells_filter' function.
class GetDataCellsFilterRequest(BaseValidatorModel):
    TableCatalogId: str
    DatabaseName: str
    TableName: str
    Name: str


# This class is the input for the 'get_data_lake_settings' function.
class GetDataLakeSettingsRequest(BaseValidatorModel):
    CatalogId: Optional[str] = None


# This class is the input for the 'get_effective_permissions_for_path' function.
class GetEffectivePermissionsForPathRequest(BaseValidatorModel):
    ResourceArn: str
    CatalogId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'get_lf_tag_expression' function.
class GetLFTagExpressionRequest(BaseValidatorModel):
    Name: str
    CatalogId: Optional[str] = None


class LFTagOutput(BaseValidatorModel):
    TagKey: str
    TagValues: List[str]


# This class is the input for the 'get_lf_tag' function.
class GetLFTagRequest(BaseValidatorModel):
    TagKey: str
    CatalogId: Optional[str] = None


# This class is the input for the 'get_query_state' function.
class GetQueryStateRequest(BaseValidatorModel):
    QueryId: str


# This class is the input for the 'get_query_statistics' function.
class GetQueryStatisticsRequest(BaseValidatorModel):
    QueryId: str


class PlanningStatistics(BaseValidatorModel):
    EstimatedDataToScanBytes: Optional[int] = None
    PlanningTimeMillis: Optional[int] = None
    QueueTimeMillis: Optional[int] = None
    WorkUnitsGeneratedCount: Optional[int] = None

Timestamp = Union[datetime, str]


class PartitionValueList(BaseValidatorModel):
    Values: List[str]


# This class is the input for the 'get_work_unit_results' function.
class GetWorkUnitResultsRequest(BaseValidatorModel):
    QueryId: str
    WorkUnitId: int
    WorkUnitToken: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'get_work_units' function.
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
    TagValues: List[str]
    CatalogId: Optional[str] = None


class LFTagPair(BaseValidatorModel):
    TagKey: str
    TagValues: List[str]
    CatalogId: Optional[str] = None


class LFTag(BaseValidatorModel):
    TagKey: str
    TagValues: List[str]


# This class is the input for the 'list_lf_tag_expressions' function.
class ListLFTagExpressionsRequest(BaseValidatorModel):
    CatalogId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_lf_tags' function.
class ListLFTagsRequest(BaseValidatorModel):
    CatalogId: Optional[str] = None
    ResourceShareType: Optional[ResourceShareTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_table_storage_optimizers' function.
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


# This class is the input for the 'list_transactions' function.
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


# This class is the input for the 'start_transaction' function.
class StartTransactionRequest(BaseValidatorModel):
    TransactionType: Optional[TransactionTypeType] = None


class TableResource(BaseValidatorModel):
    DatabaseName: str
    CatalogId: Optional[str] = None
    Name: Optional[str] = None
    TableWildcard: Optional[Dict[str, Any]] = None


class UpdateLFTagRequest(BaseValidatorModel):
    TagKey: str
    CatalogId: Optional[str] = None
    TagValuesToDelete: Optional[List[str]] = None
    TagValuesToAdd: Optional[List[str]] = None


class UpdateResourceRequest(BaseValidatorModel):
    RoleArn: str
    ResourceArn: str
    WithFederation: Optional[bool] = None
    HybridAccessEnabled: Optional[bool] = None


# This class is the input for the 'update_table_storage_optimizer' function.
class UpdateTableStorageOptimizerRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    StorageOptimizerConfig: Dict[OptimizerTypeType, Dict[str, str]]
    CatalogId: Optional[str] = None


# This class is the output for the 'assume_decorated_role_with_saml' function.
class AssumeDecoratedRoleWithSAMLResponse(BaseValidatorModel):
    AccessKeyId: str
    SecretAccessKey: str
    SessionToken: str
    Expiration: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'commit_transaction' function.
class CommitTransactionResponse(BaseValidatorModel):
    TransactionStatus: TransactionStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_lake_formation_identity_center_configuration' function.
class CreateLakeFormationIdentityCenterConfigurationResponse(BaseValidatorModel):
    ApplicationArn: str
    ResponseMetadata: ResponseMetadata


class GetDataLakePrincipalResponse(BaseValidatorModel):
    Identity: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_lf_tag' function.
class GetLFTagResponse(BaseValidatorModel):
    CatalogId: str
    TagKey: str
    TagValues: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_query_state' function.
class GetQueryStateResponse(BaseValidatorModel):
    Error: str
    State: QueryStateStringType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_temporary_glue_partition_credentials' function.
class GetTemporaryGluePartitionCredentialsResponse(BaseValidatorModel):
    AccessKeyId: str
    SecretAccessKey: str
    SessionToken: str
    Expiration: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_temporary_glue_table_credentials' function.
class GetTemporaryGlueTableCredentialsResponse(BaseValidatorModel):
    AccessKeyId: str
    SecretAccessKey: str
    SessionToken: str
    Expiration: datetime
    VendedS3Path: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_work_unit_results' function.
class GetWorkUnitResultsResponse(BaseValidatorModel):
    ResultStream: StreamingBody
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_query_planning' function.
class StartQueryPlanningResponse(BaseValidatorModel):
    QueryId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_transaction' function.
class StartTransactionResponse(BaseValidatorModel):
    TransactionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_table_storage_optimizer' function.
class UpdateTableStorageOptimizerResponse(BaseValidatorModel):
    Result: str
    ResponseMetadata: ResponseMetadata


class PrincipalPermissionsOutput(BaseValidatorModel):
    Principal: Optional[DataLakePrincipal] = None
    Permissions: Optional[List[PermissionType]] = None


class PrincipalPermissions(BaseValidatorModel):
    Principal: Optional[DataLakePrincipal] = None
    Permissions: Optional[List[PermissionType]] = None


class ColumnLFTag(BaseValidatorModel):
    Name: Optional[str] = None
    LFTags: Optional[List[LFTagPairOutput]] = None


class LFTagError(BaseValidatorModel):
    LFTag: Optional[LFTagPairOutput] = None
    Error: Optional[ErrorDetail] = None


# This class is the output for the 'list_lf_tags' function.
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

ColumnWildcardUnion = Union[ColumnWildcard, ColumnWildcardOutput]


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
    ColumnNames: Optional[List[str]] = None
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
    Objects: List[VirtualObject]
    CatalogId: Optional[str] = None


# This class is the output for the 'describe_lake_formation_identity_center_configuration' function.
class DescribeLakeFormationIdentityCenterConfigurationResponse(BaseValidatorModel):
    CatalogId: str
    InstanceArn: str
    ApplicationArn: str
    ExternalFiltering: ExternalFilteringConfigurationOutput
    ShareRecipients: List[DataLakePrincipal]
    ResourceShare: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_resource' function.
class DescribeResourceResponse(BaseValidatorModel):
    ResourceInfo: ResourceInfo
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_resources' function.
class ListResourcesResponse(BaseValidatorModel):
    ResourceInfoList: List[ResourceInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_transaction' function.
class DescribeTransactionResponse(BaseValidatorModel):
    TransactionDescription: TransactionDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_transactions' function.
class ListTransactionsResponse(BaseValidatorModel):
    Transactions: List[TransactionDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

ExternalFilteringConfigurationUnion = Union[ExternalFilteringConfiguration, ExternalFilteringConfigurationOutput]


# This class is the input for the 'list_resources' function.
class ListResourcesRequest(BaseValidatorModel):
    FilterConditionList: Optional[List[FilterCondition]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the output for the 'get_lf_tag_expression' function.
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


# This class is the output for the 'get_query_statistics' function.
class GetQueryStatisticsResponse(BaseValidatorModel):
    ExecutionStatistics: ExecutionStatistics
    PlanningStatistics: PlanningStatistics
    QuerySubmissionTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'get_table_objects' function.
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
    QueryParameters: Optional[Dict[str, str]] = None
    TransactionId: Optional[str] = None


class QuerySessionContext(BaseValidatorModel):
    QueryId: Optional[str] = None
    QueryStartTime: Optional[Timestamp] = None
    ClusterId: Optional[str] = None
    QueryAuthorizationId: Optional[str] = None
    AdditionalContext: Optional[Dict[str, str]] = None


# This class is the input for the 'get_temporary_glue_partition_credentials' function.
class GetTemporaryGluePartitionCredentialsRequest(BaseValidatorModel):
    TableArn: str
    Partition: PartitionValueList
    Permissions: Optional[List[PermissionType]] = None
    DurationSeconds: Optional[int] = None
    AuditContext: Optional[AuditContext] = None
    SupportedPermissionTypes: Optional[List[PermissionTypeType]] = None


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


# This class is the output for the 'get_work_units' function.
class GetWorkUnitsResponse(BaseValidatorModel):
    QueryId: str
    WorkUnitRanges: List[WorkUnitRange]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

LFTagKeyResourceUnion = Union[LFTagKeyResource, LFTagKeyResourceOutput]

LFTagPairUnion = Union[LFTagPair, LFTagPairOutput]

LFTagUnion = Union[LFTag, LFTagOutput]


# This class is the output for the 'list_table_storage_optimizers' function.
class ListTableStorageOptimizersResponse(BaseValidatorModel):
    StorageOptimizerList: List[StorageOptimizer]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PartitionObjects(BaseValidatorModel):
    PartitionValues: Optional[List[str]] = None
    Objects: Optional[List[TableObject]] = None

TableResourceUnion = Union[TableResource, TableResourceOutput]


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
    DataLakeAdmins: Optional[List[DataLakePrincipal]] = None
    ReadOnlyAdmins: Optional[List[DataLakePrincipal]] = None
    CreateDatabaseDefaultPermissions: Optional[List[PrincipalPermissions]] = None
    CreateTableDefaultPermissions: Optional[List[PrincipalPermissions]] = None
    Parameters: Optional[Dict[str, str]] = None
    TrustedResourceOwners: Optional[List[str]] = None
    AllowExternalDataFiltering: Optional[bool] = None
    AllowFullTableExternalDataAccess: Optional[bool] = None
    ExternalDataFilteringAllowList: Optional[List[DataLakePrincipal]] = None
    AuthorizedSessionTagValueList: Optional[List[str]] = None


# This class is the output for the 'get_resource_lf_tags' function.
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


# This class is the output for the 'add_lf_tags_to_resource' function.
class AddLFTagsToResourceResponse(BaseValidatorModel):
    Failures: List[LFTagError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'remove_lf_tags_from_resource' function.
class RemoveLFTagsFromResourceResponse(BaseValidatorModel):
    Failures: List[LFTagError]
    ResponseMetadata: ResponseMetadata


class TableWithColumnsResource(BaseValidatorModel):
    DatabaseName: str
    Name: str
    CatalogId: Optional[str] = None
    ColumnNames: Optional[List[str]] = None
    ColumnWildcard: Optional[ColumnWildcardUnion] = None


# This class is the output for the 'get_data_cells_filter' function.
class GetDataCellsFilterResponse(BaseValidatorModel):
    DataCellsFilter: DataCellsFilterOutput
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_data_cells_filter' function.
class ListDataCellsFilterResponse(BaseValidatorModel):
    DataCellsFilters: List[DataCellsFilterOutput]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

DataCellsFilterUnion = Union[DataCellsFilter, DataCellsFilterOutput]


# This class is the output for the 'search_databases_by_lf_tags' function.
class SearchDatabasesByLFTagsResponse(BaseValidatorModel):
    DatabaseList: List[TaggedDatabase]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateTableObjectsRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    WriteOperations: List[WriteOperation]
    CatalogId: Optional[str] = None
    TransactionId: Optional[str] = None


# This class is the input for the 'create_lake_formation_identity_center_configuration' function.
class CreateLakeFormationIdentityCenterConfigurationRequest(BaseValidatorModel):
    CatalogId: Optional[str] = None
    InstanceArn: Optional[str] = None
    ExternalFiltering: Optional[ExternalFilteringConfigurationUnion] = None
    ShareRecipients: Optional[List[DataLakePrincipal]] = None


class UpdateLakeFormationIdentityCenterConfigurationRequest(BaseValidatorModel):
    CatalogId: Optional[str] = None
    ShareRecipients: Optional[List[DataLakePrincipal]] = None
    ApplicationStatus: Optional[ApplicationStatusType] = None
    ExternalFiltering: Optional[ExternalFilteringConfigurationUnion] = None


# This class is the output for the 'list_lf_tag_expressions' function.
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


# This class is the input for the 'start_query_planning' function.
class StartQueryPlanningRequest(BaseValidatorModel):
    QueryPlanningContext: QueryPlanningContext
    QueryString: str


# This class is the input for the 'get_temporary_glue_table_credentials' function.
class GetTemporaryGlueTableCredentialsRequest(BaseValidatorModel):
    TableArn: str
    Permissions: Optional[List[PermissionType]] = None
    DurationSeconds: Optional[int] = None
    AuditContext: Optional[AuditContext] = None
    SupportedPermissionTypes: Optional[List[PermissionTypeType]] = None
    S3Path: Optional[str] = None
    QuerySessionContext: Optional[QuerySessionContext] = None


class CreateLFTagExpressionRequest(BaseValidatorModel):
    Name: str
    Expression: List[LFTagUnion]
    Description: Optional[str] = None
    CatalogId: Optional[str] = None


class LFTagPolicyResource(BaseValidatorModel):
    ResourceType: ResourceTypeType
    CatalogId: Optional[str] = None
    Expression: Optional[List[LFTagUnion]] = None
    ExpressionName: Optional[str] = None


class SearchDatabasesByLFTagsRequestPaginate(BaseValidatorModel):
    Expression: List[LFTagUnion]
    CatalogId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'search_databases_by_lf_tags' function.
class SearchDatabasesByLFTagsRequest(BaseValidatorModel):
    Expression: List[LFTagUnion]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CatalogId: Optional[str] = None


class SearchTablesByLFTagsRequestPaginate(BaseValidatorModel):
    Expression: List[LFTagUnion]
    CatalogId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'search_tables_by_lf_tags' function.
class SearchTablesByLFTagsRequest(BaseValidatorModel):
    Expression: List[LFTagUnion]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CatalogId: Optional[str] = None


class UpdateLFTagExpressionRequest(BaseValidatorModel):
    Name: str
    Expression: List[LFTagUnion]
    Description: Optional[str] = None
    CatalogId: Optional[str] = None


# This class is the output for the 'get_table_objects' function.
class GetTableObjectsResponse(BaseValidatorModel):
    Objects: List[PartitionObjects]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListDataCellsFilterRequestPaginate(BaseValidatorModel):
    Table: Optional[TableResourceUnion] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_data_cells_filter' function.
class ListDataCellsFilterRequest(BaseValidatorModel):
    Table: Optional[TableResourceUnion] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the output for the 'get_data_lake_settings' function.
class GetDataLakeSettingsResponse(BaseValidatorModel):
    DataLakeSettings: DataLakeSettingsOutput
    ResponseMetadata: ResponseMetadata

DataLakeSettingsUnion = Union[DataLakeSettings, DataLakeSettingsOutput]


# This class is the output for the 'search_tables_by_lf_tags' function.
class SearchTablesByLFTagsResponse(BaseValidatorModel):
    TableList: List[TaggedTable]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

TableWithColumnsResourceUnion = Union[TableWithColumnsResource, TableWithColumnsResourceOutput]


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

LFTagPolicyResourceUnion = Union[LFTagPolicyResource, LFTagPolicyResourceOutput]


class PutDataLakeSettingsRequest(BaseValidatorModel):
    DataLakeSettings: DataLakeSettingsUnion
    CatalogId: Optional[str] = None


class BatchPermissionsFailureEntry(BaseValidatorModel):
    RequestEntry: Optional[BatchPermissionsRequestEntryOutput] = None
    Error: Optional[ErrorDetail] = None


# This class is the output for the 'list_lake_formation_opt_ins' function.
class ListLakeFormationOptInsResponse(BaseValidatorModel):
    LakeFormationOptInsInfoList: List[LakeFormationOptInsInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_effective_permissions_for_path' function.
class GetEffectivePermissionsForPathResponse(BaseValidatorModel):
    Permissions: List[PrincipalResourcePermissions]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_permissions' function.
class ListPermissionsResponse(BaseValidatorModel):
    PrincipalResourcePermissions: List[PrincipalResourcePermissions]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


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


# This class is the output for the 'batch_grant_permissions' function.
class BatchGrantPermissionsResponse(BaseValidatorModel):
    Failures: List[BatchPermissionsFailureEntry]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_revoke_permissions' function.
class BatchRevokePermissionsResponse(BaseValidatorModel):
    Failures: List[BatchPermissionsFailureEntry]
    ResponseMetadata: ResponseMetadata

ResourceUnion = Union[Resource, ResourceOutput]


# This class is the input for the 'add_lf_tags_to_resource' function.
class AddLFTagsToResourceRequest(BaseValidatorModel):
    Resource: ResourceUnion
    LFTags: List[LFTagPairUnion]
    CatalogId: Optional[str] = None


class BatchPermissionsRequestEntry(BaseValidatorModel):
    Id: str
    Principal: Optional[DataLakePrincipal] = None
    Resource: Optional[ResourceUnion] = None
    Permissions: Optional[List[PermissionType]] = None
    PermissionsWithGrantOption: Optional[List[PermissionType]] = None


class CreateLakeFormationOptInRequest(BaseValidatorModel):
    Principal: DataLakePrincipal
    Resource: ResourceUnion


class DeleteLakeFormationOptInRequest(BaseValidatorModel):
    Principal: DataLakePrincipal
    Resource: ResourceUnion


# This class is the input for the 'get_resource_lf_tags' function.
class GetResourceLFTagsRequest(BaseValidatorModel):
    Resource: ResourceUnion
    CatalogId: Optional[str] = None
    ShowAssignedLFTags: Optional[bool] = None


class GrantPermissionsRequest(BaseValidatorModel):
    Principal: DataLakePrincipal
    Resource: ResourceUnion
    Permissions: List[PermissionType]
    CatalogId: Optional[str] = None
    PermissionsWithGrantOption: Optional[List[PermissionType]] = None


# This class is the input for the 'list_lake_formation_opt_ins' function.
class ListLakeFormationOptInsRequest(BaseValidatorModel):
    Principal: Optional[DataLakePrincipal] = None
    Resource: Optional[ResourceUnion] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_permissions' function.
class ListPermissionsRequest(BaseValidatorModel):
    CatalogId: Optional[str] = None
    Principal: Optional[DataLakePrincipal] = None
    ResourceType: Optional[DataLakeResourceTypeType] = None
    Resource: Optional[ResourceUnion] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    IncludeRelated: Optional[str] = None


# This class is the input for the 'remove_lf_tags_from_resource' function.
class RemoveLFTagsFromResourceRequest(BaseValidatorModel):
    Resource: ResourceUnion
    LFTags: List[LFTagPairUnion]
    CatalogId: Optional[str] = None


class RevokePermissionsRequest(BaseValidatorModel):
    Principal: DataLakePrincipal
    Resource: ResourceUnion
    Permissions: List[PermissionType]
    CatalogId: Optional[str] = None
    PermissionsWithGrantOption: Optional[List[PermissionType]] = None

BatchPermissionsRequestEntryUnion = Union[BatchPermissionsRequestEntry, BatchPermissionsRequestEntryOutput]


# This class is the input for the 'batch_grant_permissions' function.
class BatchGrantPermissionsRequest(BaseValidatorModel):
    Entries: List[BatchPermissionsRequestEntryUnion]
    CatalogId: Optional[str] = None


# This class is the input for the 'batch_revoke_permissions' function.
class BatchRevokePermissionsRequest(BaseValidatorModel):
    Entries: List[BatchPermissionsRequestEntryUnion]
    CatalogId: Optional[str] = None
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
from aws_resource_validator.pydantic_models.athena_constants import *

class AclConfiguration(BaseValidatorModel):
    S3AclOption: Literal["BUCKET_OWNER_FULL_CONTROL"]


class ApplicationDPUSizes(BaseValidatorModel):
    ApplicationRuntimeId: Optional[str] = None
    SupportedDPUSizes: Optional[List[int]] = None


class AthenaError(BaseValidatorModel):
    ErrorCategory: Optional[int] = None
    ErrorType: Optional[int] = None
    Retryable: Optional[bool] = None
    ErrorMessage: Optional[str] = None


class BatchGetNamedQueryInput(BaseValidatorModel):
    NamedQueryIds: Sequence[str]


class NamedQuery(BaseValidatorModel):
    Name: str
    Database: str
    QueryString: str
    Description: Optional[str] = None
    NamedQueryId: Optional[str] = None
    WorkGroup: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class UnprocessedNamedQueryId(BaseValidatorModel):
    NamedQueryId: Optional[str] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class BatchGetPreparedStatementInput(BaseValidatorModel):
    PreparedStatementNames: Sequence[str]
    WorkGroup: str


class PreparedStatement(BaseValidatorModel):
    StatementName: Optional[str] = None
    QueryStatement: Optional[str] = None
    WorkGroupName: Optional[str] = None
    Description: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None


class UnprocessedPreparedStatementName(BaseValidatorModel):
    StatementName: Optional[str] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class BatchGetQueryExecutionInput(BaseValidatorModel):
    QueryExecutionIds: Sequence[str]


class UnprocessedQueryExecutionId(BaseValidatorModel):
    QueryExecutionId: Optional[str] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class CalculationConfiguration(BaseValidatorModel):
    CodeBlock: Optional[str] = None


class CalculationResult(BaseValidatorModel):
    StdOutS3Uri: Optional[str] = None
    StdErrorS3Uri: Optional[str] = None
    ResultS3Uri: Optional[str] = None
    ResultType: Optional[str] = None


class CalculationStatistics(BaseValidatorModel):
    DpuExecutionInMillis: Optional[int] = None
    Progress: Optional[str] = None


class CalculationStatus(BaseValidatorModel):
    SubmissionDateTime: Optional[datetime] = None
    CompletionDateTime: Optional[datetime] = None
    State: Optional[CalculationExecutionStateType] = None
    StateChangeReason: Optional[str] = None


class CancelCapacityReservationInput(BaseValidatorModel):
    Name: str


class CapacityAllocation(BaseValidatorModel):
    Status: CapacityAllocationStatusType
    RequestTime: datetime
    StatusMessage: Optional[str] = None
    RequestCompletionTime: Optional[datetime] = None


class CapacityAssignmentOutput(BaseValidatorModel):
    WorkGroupNames: Optional[List[str]] = None


class CapacityAssignment(BaseValidatorModel):
    WorkGroupNames: Optional[Sequence[str]] = None


class Tag(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class CreateNamedQueryInput(BaseValidatorModel):
    Name: str
    Database: str
    QueryString: str
    Description: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    WorkGroup: Optional[str] = None


class CreateNotebookInput(BaseValidatorModel):
    WorkGroup: str
    Name: str
    ClientRequestToken: Optional[str] = None


class CreatePreparedStatementInput(BaseValidatorModel):
    StatementName: str
    WorkGroup: str
    QueryStatement: str
    Description: Optional[str] = None


class CreatePresignedNotebookUrlRequest(BaseValidatorModel):
    SessionId: str


class CustomerContentEncryptionConfiguration(BaseValidatorModel):
    KmsKey: str


class Database(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    Parameters: Optional[Dict[str, str]] = None


class Datum(BaseValidatorModel):
    VarCharValue: Optional[str] = None


class DeleteCapacityReservationInput(BaseValidatorModel):
    Name: str


class DeleteDataCatalogInput(BaseValidatorModel):
    Name: str
    DeleteCatalogOnly: Optional[bool] = None


class DeleteNamedQueryInput(BaseValidatorModel):
    NamedQueryId: str


class DeleteNotebookInput(BaseValidatorModel):
    NotebookId: str


class DeletePreparedStatementInput(BaseValidatorModel):
    StatementName: str
    WorkGroup: str


class DeleteWorkGroupInput(BaseValidatorModel):
    WorkGroup: str
    RecursiveDeleteOption: Optional[bool] = None


class EncryptionConfiguration(BaseValidatorModel):
    EncryptionOption: EncryptionOptionType
    KmsKey: Optional[str] = None


class EngineConfigurationOutput(BaseValidatorModel):
    MaxConcurrentDpus: int
    CoordinatorDpuSize: Optional[int] = None
    DefaultExecutorDpuSize: Optional[int] = None
    AdditionalConfigs: Optional[Dict[str, str]] = None
    SparkProperties: Optional[Dict[str, str]] = None


class EngineConfiguration(BaseValidatorModel):
    MaxConcurrentDpus: int
    CoordinatorDpuSize: Optional[int] = None
    DefaultExecutorDpuSize: Optional[int] = None
    AdditionalConfigs: Optional[Mapping[str, str]] = None
    SparkProperties: Optional[Mapping[str, str]] = None


class EngineVersion(BaseValidatorModel):
    SelectedEngineVersion: Optional[str] = None
    EffectiveEngineVersion: Optional[str] = None


class ExecutorsSummary(BaseValidatorModel):
    ExecutorId: str
    ExecutorType: Optional[ExecutorTypeType] = None
    StartDateTime: Optional[int] = None
    TerminationDateTime: Optional[int] = None
    ExecutorState: Optional[ExecutorStateType] = None
    ExecutorSize: Optional[int] = None


class ExportNotebookInput(BaseValidatorModel):
    NotebookId: str


class FilterDefinition(BaseValidatorModel):
    Name: Optional[str] = None


class GetCalculationExecutionCodeRequest(BaseValidatorModel):
    CalculationExecutionId: str


class GetCalculationExecutionRequest(BaseValidatorModel):
    CalculationExecutionId: str


class GetCalculationExecutionStatusRequest(BaseValidatorModel):
    CalculationExecutionId: str


class GetCapacityAssignmentConfigurationInput(BaseValidatorModel):
    CapacityReservationName: str


class GetCapacityReservationInput(BaseValidatorModel):
    Name: str


class GetDataCatalogInput(BaseValidatorModel):
    Name: str
    WorkGroup: Optional[str] = None


class GetDatabaseInput(BaseValidatorModel):
    CatalogName: str
    DatabaseName: str
    WorkGroup: Optional[str] = None


class GetNamedQueryInput(BaseValidatorModel):
    NamedQueryId: str


class GetNotebookMetadataInput(BaseValidatorModel):
    NotebookId: str


class GetPreparedStatementInput(BaseValidatorModel):
    StatementName: str
    WorkGroup: str


class GetQueryExecutionInput(BaseValidatorModel):
    QueryExecutionId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetQueryResultsInput(BaseValidatorModel):
    QueryExecutionId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetQueryRuntimeStatisticsInput(BaseValidatorModel):
    QueryExecutionId: str


class GetSessionRequest(BaseValidatorModel):
    SessionId: str


class SessionStatistics(BaseValidatorModel):
    DpuExecutionInMillis: Optional[int] = None


class SessionStatus(BaseValidatorModel):
    StartDateTime: Optional[datetime] = None
    LastModifiedDateTime: Optional[datetime] = None
    EndDateTime: Optional[datetime] = None
    IdleSinceDateTime: Optional[datetime] = None
    State: Optional[SessionStateType] = None
    StateChangeReason: Optional[str] = None


class GetSessionStatusRequest(BaseValidatorModel):
    SessionId: str


class GetTableMetadataInput(BaseValidatorModel):
    CatalogName: str
    DatabaseName: str
    TableName: str
    WorkGroup: Optional[str] = None


class GetWorkGroupInput(BaseValidatorModel):
    WorkGroup: str


class IdentityCenterConfiguration(BaseValidatorModel):
    EnableIdentityCenter: Optional[bool] = None
    IdentityCenterInstanceArn: Optional[str] = None


class ListApplicationDPUSizesInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListCalculationExecutionsRequest(BaseValidatorModel):
    SessionId: str
    StateFilter: Optional[CalculationExecutionStateType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListCapacityReservationsInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDataCatalogsInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WorkGroup: Optional[str] = None


class ListDatabasesInput(BaseValidatorModel):
    CatalogName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WorkGroup: Optional[str] = None


class ListEngineVersionsInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListExecutorsRequest(BaseValidatorModel):
    SessionId: str
    ExecutorStateFilter: Optional[ExecutorStateType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListNamedQueriesInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WorkGroup: Optional[str] = None


class ListNotebookSessionsRequest(BaseValidatorModel):
    NotebookId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class NotebookSessionSummary(BaseValidatorModel):
    SessionId: Optional[str] = None
    CreationTime: Optional[datetime] = None


class ListPreparedStatementsInput(BaseValidatorModel):
    WorkGroup: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class PreparedStatementSummary(BaseValidatorModel):
    StatementName: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None


class ListQueryExecutionsInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WorkGroup: Optional[str] = None


class ListSessionsRequest(BaseValidatorModel):
    WorkGroup: str
    StateFilter: Optional[SessionStateType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTableMetadataInput(BaseValidatorModel):
    CatalogName: str
    DatabaseName: str
    Expression: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WorkGroup: Optional[str] = None


class ListTagsForResourceInput(BaseValidatorModel):
    ResourceARN: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListWorkGroupsInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class QueryExecutionContext(BaseValidatorModel):
    Database: Optional[str] = None
    Catalog: Optional[str] = None


class ResultReuseInformation(BaseValidatorModel):
    ReusedPreviousResult: bool


class QueryResultsS3AccessGrantsConfiguration(BaseValidatorModel):
    EnableS3AccessGrants: bool
    AuthenticationType: Literal["DIRECTORY_IDENTITY"]
    CreateUserLevelPrefix: Optional[bool] = None


class QueryRuntimeStatisticsRows(BaseValidatorModel):
    InputRows: Optional[int] = None
    InputBytes: Optional[int] = None
    OutputBytes: Optional[int] = None
    OutputRows: Optional[int] = None


class QueryRuntimeStatisticsTimeline(BaseValidatorModel):
    QueryQueueTimeInMillis: Optional[int] = None
    ServicePreProcessingTimeInMillis: Optional[int] = None
    QueryPlanningTimeInMillis: Optional[int] = None
    EngineExecutionTimeInMillis: Optional[int] = None
    ServiceProcessingTimeInMillis: Optional[int] = None
    TotalExecutionTimeInMillis: Optional[int] = None


class QueryStagePlanNode(BaseValidatorModel):
    Name: Optional[str] = None
    Identifier: Optional[str] = None
    Children: Optional[List[Dict[str, Any]]] = None
    RemoteSources: Optional[List[str]] = None


class ResultReuseByAgeConfiguration(BaseValidatorModel):
    Enabled: bool
    MaxAgeInMinutes: Optional[int] = None


class StopCalculationExecutionRequest(BaseValidatorModel):
    CalculationExecutionId: str


class StopQueryExecutionInput(BaseValidatorModel):
    QueryExecutionId: str


class TerminateSessionRequest(BaseValidatorModel):
    SessionId: str


class UntagResourceInput(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class UpdateCapacityReservationInput(BaseValidatorModel):
    TargetDpus: int
    Name: str


class UpdateNamedQueryInput(BaseValidatorModel):
    NamedQueryId: str
    Name: str
    QueryString: str
    Description: Optional[str] = None


class UpdateNotebookMetadataInput(BaseValidatorModel):
    NotebookId: str
    Name: str
    ClientRequestToken: Optional[str] = None


class UpdatePreparedStatementInput(BaseValidatorModel):
    StatementName: str
    WorkGroup: str
    QueryStatement: str
    Description: Optional[str] = None


class QueryExecutionStatus(BaseValidatorModel):
    State: Optional[QueryExecutionStateType] = None
    StateChangeReason: Optional[str] = None
    SubmissionDateTime: Optional[datetime] = None
    CompletionDateTime: Optional[datetime] = None
    AthenaError: Optional[AthenaError] = None


class CreateNamedQueryOutput(BaseValidatorModel):
    NamedQueryId: str
    ResponseMetadata: ResponseMetadata


class CreateNotebookOutput(BaseValidatorModel):
    NotebookId: str
    ResponseMetadata: ResponseMetadata


class CreatePresignedNotebookUrlResponse(BaseValidatorModel):
    NotebookUrl: str
    AuthToken: str
    AuthTokenExpirationTime: int
    ResponseMetadata: ResponseMetadata


class GetCalculationExecutionCodeResponse(BaseValidatorModel):
    CodeBlock: str
    ResponseMetadata: ResponseMetadata


class GetNamedQueryOutput(BaseValidatorModel):
    NamedQuery: NamedQuery
    ResponseMetadata: ResponseMetadata


class ImportNotebookOutput(BaseValidatorModel):
    NotebookId: str
    ResponseMetadata: ResponseMetadata


class ListApplicationDPUSizesOutput(BaseValidatorModel):
    ApplicationDPUSizes: List[ApplicationDPUSizes]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListNamedQueriesOutput(BaseValidatorModel):
    NamedQueryIds: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListQueryExecutionsOutput(BaseValidatorModel):
    QueryExecutionIds: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class StartCalculationExecutionResponse(BaseValidatorModel):
    CalculationExecutionId: str
    State: CalculationExecutionStateType
    ResponseMetadata: ResponseMetadata


class StartQueryExecutionOutput(BaseValidatorModel):
    QueryExecutionId: str
    ResponseMetadata: ResponseMetadata


class StartSessionResponse(BaseValidatorModel):
    SessionId: str
    State: SessionStateType
    ResponseMetadata: ResponseMetadata


class StopCalculationExecutionResponse(BaseValidatorModel):
    State: CalculationExecutionStateType
    ResponseMetadata: ResponseMetadata


class TerminateSessionResponse(BaseValidatorModel):
    State: SessionStateType
    ResponseMetadata: ResponseMetadata


class BatchGetNamedQueryOutput(BaseValidatorModel):
    NamedQueries: List[NamedQuery]
    UnprocessedNamedQueryIds: List[UnprocessedNamedQueryId]
    ResponseMetadata: ResponseMetadata


class GetPreparedStatementOutput(BaseValidatorModel):
    PreparedStatement: PreparedStatement
    ResponseMetadata: ResponseMetadata


class BatchGetPreparedStatementOutput(BaseValidatorModel):
    PreparedStatements: List[PreparedStatement]
    UnprocessedPreparedStatementNames: List[UnprocessedPreparedStatementName]
    ResponseMetadata: ResponseMetadata


class StartCalculationExecutionRequest(BaseValidatorModel):
    SessionId: str
    Description: Optional[str] = None
    CalculationConfiguration: Optional[CalculationConfiguration] = None
    CodeBlock: Optional[str] = None
    ClientRequestToken: Optional[str] = None


class CalculationSummary(BaseValidatorModel):
    CalculationExecutionId: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[CalculationStatus] = None


class GetCalculationExecutionResponse(BaseValidatorModel):
    CalculationExecutionId: str
    SessionId: str
    Description: str
    WorkingDirectory: str
    Status: CalculationStatus
    Statistics: CalculationStatistics
    Result: CalculationResult
    ResponseMetadata: ResponseMetadata


class GetCalculationExecutionStatusResponse(BaseValidatorModel):
    Status: CalculationStatus
    Statistics: CalculationStatistics
    ResponseMetadata: ResponseMetadata


class CapacityReservation(BaseValidatorModel):
    Name: str
    Status: CapacityReservationStatusType
    TargetDpus: int
    AllocatedDpus: int
    CreationTime: datetime
    LastAllocation: Optional[CapacityAllocation] = None
    LastSuccessfulAllocationTime: Optional[datetime] = None


class CapacityAssignmentConfiguration(BaseValidatorModel):
    CapacityReservationName: Optional[str] = None
    CapacityAssignments: Optional[List[CapacityAssignmentOutput]] = None


class ColumnInfo(BaseValidatorModel):
    pass


class ResultSetMetadata(BaseValidatorModel):
    ColumnInfo: Optional[List[ColumnInfo]] = None


class Column(BaseValidatorModel):
    pass


class TableMetadata(BaseValidatorModel):
    Name: str
    CreateTime: Optional[datetime] = None
    LastAccessTime: Optional[datetime] = None
    TableType: Optional[str] = None
    Columns: Optional[List[Column]] = None
    PartitionKeys: Optional[List[Column]] = None
    Parameters: Optional[Dict[str, str]] = None


class CreateCapacityReservationInput(BaseValidatorModel):
    TargetDpus: int
    Name: str
    Tags: Optional[Sequence[Tag]] = None


class ListTagsForResourceOutput(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TagResourceInput(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[Tag]


class DataCatalog(BaseValidatorModel):
    pass


class CreateDataCatalogOutput(BaseValidatorModel):
    DataCatalog: DataCatalog
    ResponseMetadata: ResponseMetadata


class DeleteDataCatalogOutput(BaseValidatorModel):
    DataCatalog: DataCatalog
    ResponseMetadata: ResponseMetadata


class GetDataCatalogOutput(BaseValidatorModel):
    DataCatalog: DataCatalog
    ResponseMetadata: ResponseMetadata


class DataCatalogSummary(BaseValidatorModel):
    pass


class ListDataCatalogsOutput(BaseValidatorModel):
    DataCatalogsSummary: List[DataCatalogSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetDatabaseOutput(BaseValidatorModel):
    Database: Database
    ResponseMetadata: ResponseMetadata


class ListDatabasesOutput(BaseValidatorModel):
    DatabaseList: List[Database]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Row(BaseValidatorModel):
    Data: Optional[List[Datum]] = None


class ResultConfiguration(BaseValidatorModel):
    OutputLocation: Optional[str] = None
    EncryptionConfiguration: Optional[EncryptionConfiguration] = None
    ExpectedBucketOwner: Optional[str] = None
    AclConfiguration: Optional[AclConfiguration] = None


class ResultConfigurationUpdates(BaseValidatorModel):
    OutputLocation: Optional[str] = None
    RemoveOutputLocation: Optional[bool] = None
    EncryptionConfiguration: Optional[EncryptionConfiguration] = None
    RemoveEncryptionConfiguration: Optional[bool] = None
    ExpectedBucketOwner: Optional[str] = None
    RemoveExpectedBucketOwner: Optional[bool] = None
    AclConfiguration: Optional[AclConfiguration] = None
    RemoveAclConfiguration: Optional[bool] = None


class SessionConfiguration(BaseValidatorModel):
    ExecutionRole: Optional[str] = None
    WorkingDirectory: Optional[str] = None
    IdleTimeoutSeconds: Optional[int] = None
    EncryptionConfiguration: Optional[EncryptionConfiguration] = None


class ListEngineVersionsOutput(BaseValidatorModel):
    EngineVersions: List[EngineVersion]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class WorkGroupSummary(BaseValidatorModel):
    Name: Optional[str] = None
    State: Optional[WorkGroupStateType] = None
    Description: Optional[str] = None
    CreationTime: Optional[datetime] = None
    EngineVersion: Optional[EngineVersion] = None
    IdentityCenterApplicationArn: Optional[str] = None


class ListExecutorsResponse(BaseValidatorModel):
    SessionId: str
    ExecutorsSummary: List[ExecutorsSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class NotebookMetadata(BaseValidatorModel):
    pass


class ExportNotebookOutput(BaseValidatorModel):
    NotebookMetadata: NotebookMetadata
    Payload: str
    ResponseMetadata: ResponseMetadata


class GetNotebookMetadataOutput(BaseValidatorModel):
    NotebookMetadata: NotebookMetadata
    ResponseMetadata: ResponseMetadata


class ListNotebookMetadataOutput(BaseValidatorModel):
    NotebookMetadataList: List[NotebookMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListNotebookMetadataInput(BaseValidatorModel):
    WorkGroup: str
    Filters: Optional[FilterDefinition] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetQueryResultsInputPaginate(BaseValidatorModel):
    QueryExecutionId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDataCatalogsInputPaginate(BaseValidatorModel):
    WorkGroup: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDatabasesInputPaginate(BaseValidatorModel):
    CatalogName: str
    WorkGroup: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListNamedQueriesInputPaginate(BaseValidatorModel):
    WorkGroup: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListQueryExecutionsInputPaginate(BaseValidatorModel):
    WorkGroup: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTableMetadataInputPaginate(BaseValidatorModel):
    CatalogName: str
    DatabaseName: str
    Expression: Optional[str] = None
    WorkGroup: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTagsForResourceInputPaginate(BaseValidatorModel):
    ResourceARN: str
    PaginationConfig: Optional[PaginatorConfig] = None


class GetSessionStatusResponse(BaseValidatorModel):
    SessionId: str
    Status: SessionStatus
    ResponseMetadata: ResponseMetadata


class SessionSummary(BaseValidatorModel):
    SessionId: Optional[str] = None
    Description: Optional[str] = None
    EngineVersion: Optional[EngineVersion] = None
    NotebookVersion: Optional[str] = None
    Status: Optional[SessionStatus] = None


class ListNotebookSessionsResponse(BaseValidatorModel):
    NotebookSessionsList: List[NotebookSessionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListPreparedStatementsOutput(BaseValidatorModel):
    PreparedStatements: List[PreparedStatementSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class QueryExecutionStatistics(BaseValidatorModel):
    EngineExecutionTimeInMillis: Optional[int] = None
    DataScannedInBytes: Optional[int] = None
    DataManifestLocation: Optional[str] = None
    TotalExecutionTimeInMillis: Optional[int] = None
    QueryQueueTimeInMillis: Optional[int] = None
    ServicePreProcessingTimeInMillis: Optional[int] = None
    QueryPlanningTimeInMillis: Optional[int] = None
    ServiceProcessingTimeInMillis: Optional[int] = None
    ResultReuseInformation: Optional[ResultReuseInformation] = None


class QueryStage(BaseValidatorModel):
    StageId: Optional[int] = None
    State: Optional[str] = None
    OutputBytes: Optional[int] = None
    OutputRows: Optional[int] = None
    InputBytes: Optional[int] = None
    InputRows: Optional[int] = None
    ExecutionTime: Optional[int] = None
    QueryStagePlan: Optional[QueryStagePlanNode] = None
    SubStages: Optional[List[Dict[str, Any]]] = None


class ResultReuseConfiguration(BaseValidatorModel):
    ResultReuseByAgeConfiguration: Optional[ResultReuseByAgeConfiguration] = None


class ListCalculationExecutionsResponse(BaseValidatorModel):
    Calculations: List[CalculationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetCapacityReservationOutput(BaseValidatorModel):
    CapacityReservation: CapacityReservation
    ResponseMetadata: ResponseMetadata


class ListCapacityReservationsOutput(BaseValidatorModel):
    CapacityReservations: List[CapacityReservation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetCapacityAssignmentConfigurationOutput(BaseValidatorModel):
    CapacityAssignmentConfiguration: CapacityAssignmentConfiguration
    ResponseMetadata: ResponseMetadata


class CapacityAssignmentUnion(BaseValidatorModel):
    pass


class PutCapacityAssignmentConfigurationInput(BaseValidatorModel):
    CapacityReservationName: str
    CapacityAssignments: Sequence[CapacityAssignmentUnion]


class GetTableMetadataOutput(BaseValidatorModel):
    TableMetadata: TableMetadata
    ResponseMetadata: ResponseMetadata


class ListTableMetadataOutput(BaseValidatorModel):
    TableMetadataList: List[TableMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ResultSet(BaseValidatorModel):
    Rows: Optional[List[Row]] = None
    ResultSetMetadata: Optional[ResultSetMetadata] = None


class WorkGroupConfiguration(BaseValidatorModel):
    ResultConfiguration: Optional[ResultConfiguration] = None
    EnforceWorkGroupConfiguration: Optional[bool] = None
    PublishCloudWatchMetricsEnabled: Optional[bool] = None
    BytesScannedCutoffPerQuery: Optional[int] = None
    RequesterPaysEnabled: Optional[bool] = None
    EngineVersion: Optional[EngineVersion] = None
    AdditionalConfiguration: Optional[str] = None
    ExecutionRole: Optional[str] = None
    CustomerContentEncryptionConfiguration: Optional[ CustomerContentEncryptionConfiguration ] = None
    EnableMinimumEncryptionConfiguration: Optional[bool] = None
    IdentityCenterConfiguration: Optional[IdentityCenterConfiguration] = None
    QueryResultsS3AccessGrantsConfiguration: Optional[ QueryResultsS3AccessGrantsConfiguration ] = None


class WorkGroupConfigurationUpdates(BaseValidatorModel):
    EnforceWorkGroupConfiguration: Optional[bool] = None
    ResultConfigurationUpdates: Optional[ResultConfigurationUpdates] = None
    PublishCloudWatchMetricsEnabled: Optional[bool] = None
    BytesScannedCutoffPerQuery: Optional[int] = None
    RemoveBytesScannedCutoffPerQuery: Optional[bool] = None
    RequesterPaysEnabled: Optional[bool] = None
    EngineVersion: Optional[EngineVersion] = None
    RemoveCustomerContentEncryptionConfiguration: Optional[bool] = None
    AdditionalConfiguration: Optional[str] = None
    ExecutionRole: Optional[str] = None
    CustomerContentEncryptionConfiguration: Optional[ CustomerContentEncryptionConfiguration ] = None
    EnableMinimumEncryptionConfiguration: Optional[bool] = None
    QueryResultsS3AccessGrantsConfiguration: Optional[ QueryResultsS3AccessGrantsConfiguration ] = None


class GetSessionResponse(BaseValidatorModel):
    SessionId: str
    Description: str
    WorkGroup: str
    EngineVersion: str
    EngineConfiguration: EngineConfigurationOutput
    NotebookVersion: str
    SessionConfiguration: SessionConfiguration
    Status: SessionStatus
    Statistics: SessionStatistics
    ResponseMetadata: ResponseMetadata


class EngineConfigurationUnion(BaseValidatorModel):
    pass


class StartSessionRequest(BaseValidatorModel):
    WorkGroup: str
    EngineConfiguration: EngineConfigurationUnion
    Description: Optional[str] = None
    NotebookVersion: Optional[str] = None
    SessionIdleTimeoutInMinutes: Optional[int] = None
    ClientRequestToken: Optional[str] = None


class ListWorkGroupsOutput(BaseValidatorModel):
    WorkGroups: List[WorkGroupSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListSessionsResponse(BaseValidatorModel):
    Sessions: List[SessionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class QueryRuntimeStatistics(BaseValidatorModel):
    Timeline: Optional[QueryRuntimeStatisticsTimeline] = None
    Rows: Optional[QueryRuntimeStatisticsRows] = None
    OutputStage: Optional[QueryStage] = None


class QueryExecution(BaseValidatorModel):
    QueryExecutionId: Optional[str] = None
    Query: Optional[str] = None
    StatementType: Optional[StatementTypeType] = None
    ResultConfiguration: Optional[ResultConfiguration] = None
    ResultReuseConfiguration: Optional[ResultReuseConfiguration] = None
    QueryExecutionContext: Optional[QueryExecutionContext] = None
    Status: Optional[QueryExecutionStatus] = None
    Statistics: Optional[QueryExecutionStatistics] = None
    WorkGroup: Optional[str] = None
    EngineVersion: Optional[EngineVersion] = None
    ExecutionParameters: Optional[List[str]] = None
    SubstatementType: Optional[str] = None
    QueryResultsS3AccessGrantsConfiguration: Optional[ QueryResultsS3AccessGrantsConfiguration ] = None


class StartQueryExecutionInput(BaseValidatorModel):
    QueryString: str
    ClientRequestToken: Optional[str] = None
    QueryExecutionContext: Optional[QueryExecutionContext] = None
    ResultConfiguration: Optional[ResultConfiguration] = None
    WorkGroup: Optional[str] = None
    ExecutionParameters: Optional[Sequence[str]] = None
    ResultReuseConfiguration: Optional[ResultReuseConfiguration] = None


class GetQueryResultsOutput(BaseValidatorModel):
    UpdateCount: int
    ResultSet: ResultSet
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateWorkGroupInput(BaseValidatorModel):
    Name: str
    Configuration: Optional[WorkGroupConfiguration] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class WorkGroup(BaseValidatorModel):
    Name: str
    State: Optional[WorkGroupStateType] = None
    Configuration: Optional[WorkGroupConfiguration] = None
    Description: Optional[str] = None
    CreationTime: Optional[datetime] = None
    IdentityCenterApplicationArn: Optional[str] = None


class UpdateWorkGroupInput(BaseValidatorModel):
    WorkGroup: str
    Description: Optional[str] = None
    ConfigurationUpdates: Optional[WorkGroupConfigurationUpdates] = None
    State: Optional[WorkGroupStateType] = None


class GetQueryRuntimeStatisticsOutput(BaseValidatorModel):
    QueryRuntimeStatistics: QueryRuntimeStatistics
    ResponseMetadata: ResponseMetadata


class BatchGetQueryExecutionOutput(BaseValidatorModel):
    QueryExecutions: List[QueryExecution]
    UnprocessedQueryExecutionIds: List[UnprocessedQueryExecutionId]
    ResponseMetadata: ResponseMetadata


class GetQueryExecutionOutput(BaseValidatorModel):
    QueryExecution: QueryExecution
    ResponseMetadata: ResponseMetadata


class GetWorkGroupOutput(BaseValidatorModel):
    WorkGroup: WorkGroup
    ResponseMetadata: ResponseMetadata



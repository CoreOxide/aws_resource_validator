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
from aws_resource_validator.pydantic_models.athena_constants import *

class AclConfigurationTypeDef(BaseModel):
    S3AclOption: Literal["BUCKET_OWNER_FULL_CONTROL"]

class ApplicationDPUSizesTypeDef(BaseModel):
    ApplicationRuntimeId: Optional[str] = None
    SupportedDPUSizes: Optional[List[int]] = None

class AthenaErrorTypeDef(BaseModel):
    ErrorCategory: Optional[int] = None
    ErrorType: Optional[int] = None
    Retryable: Optional[bool] = None
    ErrorMessage: Optional[str] = None

class BatchGetNamedQueryInputRequestTypeDef(BaseModel):
    NamedQueryIds: Sequence[str]

class NamedQueryTypeDef(BaseModel):
    Name: str
    Database: str
    QueryString: str
    Description: Optional[str] = None
    NamedQueryId: Optional[str] = None
    WorkGroup: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class UnprocessedNamedQueryIdTypeDef(BaseModel):
    NamedQueryId: Optional[str] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class BatchGetPreparedStatementInputRequestTypeDef(BaseModel):
    PreparedStatementNames: Sequence[str]
    WorkGroup: str

class PreparedStatementTypeDef(BaseModel):
    StatementName: Optional[str] = None
    QueryStatement: Optional[str] = None
    WorkGroupName: Optional[str] = None
    Description: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None

class UnprocessedPreparedStatementNameTypeDef(BaseModel):
    StatementName: Optional[str] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class BatchGetQueryExecutionInputRequestTypeDef(BaseModel):
    QueryExecutionIds: Sequence[str]

class UnprocessedQueryExecutionIdTypeDef(BaseModel):
    QueryExecutionId: Optional[str] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class CalculationConfigurationTypeDef(BaseModel):
    CodeBlock: Optional[str] = None

class CalculationResultTypeDef(BaseModel):
    StdOutS3Uri: Optional[str] = None
    StdErrorS3Uri: Optional[str] = None
    ResultS3Uri: Optional[str] = None
    ResultType: Optional[str] = None

class CalculationStatisticsTypeDef(BaseModel):
    DpuExecutionInMillis: Optional[int] = None
    Progress: Optional[str] = None

class CalculationStatusTypeDef(BaseModel):
    SubmissionDateTime: Optional[datetime] = None
    CompletionDateTime: Optional[datetime] = None
    State: Optional[CalculationExecutionStateType] = None
    StateChangeReason: Optional[str] = None

class CancelCapacityReservationInputRequestTypeDef(BaseModel):
    Name: str

class CapacityAllocationTypeDef(BaseModel):
    Status: CapacityAllocationStatusType
    RequestTime: datetime
    StatusMessage: Optional[str] = None
    RequestCompletionTime: Optional[datetime] = None

class CapacityAssignmentOutputTypeDef(BaseModel):
    WorkGroupNames: Optional[List[str]] = None

class CapacityAssignmentTypeDef(BaseModel):
    WorkGroupNames: Optional[Sequence[str]] = None

class ColumnInfoTypeDef(BaseModel):
    Name: str
    Type: str
    CatalogName: Optional[str] = None
    SchemaName: Optional[str] = None
    TableName: Optional[str] = None
    Label: Optional[str] = None
    Precision: Optional[int] = None
    Scale: Optional[int] = None
    Nullable: Optional[ColumnNullableType] = None
    CaseSensitive: Optional[bool] = None

class ColumnTypeDef(BaseModel):
    Name: str
    Type: Optional[str] = None
    Comment: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class CreateNamedQueryInputRequestTypeDef(BaseModel):
    Name: str
    Database: str
    QueryString: str
    Description: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    WorkGroup: Optional[str] = None

class CreateNotebookInputRequestTypeDef(BaseModel):
    WorkGroup: str
    Name: str
    ClientRequestToken: Optional[str] = None

class CreatePreparedStatementInputRequestTypeDef(BaseModel):
    StatementName: str
    WorkGroup: str
    QueryStatement: str
    Description: Optional[str] = None

class CreatePresignedNotebookUrlRequestRequestTypeDef(BaseModel):
    SessionId: str

class CustomerContentEncryptionConfigurationTypeDef(BaseModel):
    KmsKey: str

class DataCatalogSummaryTypeDef(BaseModel):
    CatalogName: Optional[str] = None
    Type: Optional[DataCatalogTypeType] = None

class DataCatalogTypeDef(BaseModel):
    Name: str
    Type: DataCatalogTypeType
    Description: Optional[str] = None
    Parameters: Optional[Dict[str, str]] = None

class DatabaseTypeDef(BaseModel):
    Name: str
    Description: Optional[str] = None
    Parameters: Optional[Dict[str, str]] = None

class DatumTypeDef(BaseModel):
    VarCharValue: Optional[str] = None

class DeleteCapacityReservationInputRequestTypeDef(BaseModel):
    Name: str

class DeleteDataCatalogInputRequestTypeDef(BaseModel):
    Name: str

class DeleteNamedQueryInputRequestTypeDef(BaseModel):
    NamedQueryId: str

class DeleteNotebookInputRequestTypeDef(BaseModel):
    NotebookId: str

class DeletePreparedStatementInputRequestTypeDef(BaseModel):
    StatementName: str
    WorkGroup: str

class DeleteWorkGroupInputRequestTypeDef(BaseModel):
    WorkGroup: str
    RecursiveDeleteOption: Optional[bool] = None

class EncryptionConfigurationTypeDef(BaseModel):
    EncryptionOption: EncryptionOptionType
    KmsKey: Optional[str] = None

class EngineConfigurationOutputTypeDef(BaseModel):
    MaxConcurrentDpus: int
    CoordinatorDpuSize: Optional[int] = None
    DefaultExecutorDpuSize: Optional[int] = None
    AdditionalConfigs: Optional[Dict[str, str]] = None
    SparkProperties: Optional[Dict[str, str]] = None

class EngineConfigurationTypeDef(BaseModel):
    MaxConcurrentDpus: int
    CoordinatorDpuSize: Optional[int] = None
    DefaultExecutorDpuSize: Optional[int] = None
    AdditionalConfigs: Optional[Mapping[str, str]] = None
    SparkProperties: Optional[Mapping[str, str]] = None

class EngineVersionTypeDef(BaseModel):
    SelectedEngineVersion: Optional[str] = None
    EffectiveEngineVersion: Optional[str] = None

class ExecutorsSummaryTypeDef(BaseModel):
    ExecutorId: str
    ExecutorType: Optional[ExecutorTypeType] = None
    StartDateTime: Optional[int] = None
    TerminationDateTime: Optional[int] = None
    ExecutorState: Optional[ExecutorStateType] = None
    ExecutorSize: Optional[int] = None

class ExportNotebookInputRequestTypeDef(BaseModel):
    NotebookId: str

class NotebookMetadataTypeDef(BaseModel):
    NotebookId: Optional[str] = None
    Name: Optional[str] = None
    WorkGroup: Optional[str] = None
    CreationTime: Optional[datetime] = None
    Type: Optional[Literal["IPYNB"]] = None
    LastModifiedTime: Optional[datetime] = None

class FilterDefinitionTypeDef(BaseModel):
    Name: Optional[str] = None

class GetCalculationExecutionCodeRequestRequestTypeDef(BaseModel):
    CalculationExecutionId: str

class GetCalculationExecutionRequestRequestTypeDef(BaseModel):
    CalculationExecutionId: str

class GetCalculationExecutionStatusRequestRequestTypeDef(BaseModel):
    CalculationExecutionId: str

class GetCapacityAssignmentConfigurationInputRequestTypeDef(BaseModel):
    CapacityReservationName: str

class GetCapacityReservationInputRequestTypeDef(BaseModel):
    Name: str

class GetDataCatalogInputRequestTypeDef(BaseModel):
    Name: str
    WorkGroup: Optional[str] = None

class GetDatabaseInputRequestTypeDef(BaseModel):
    CatalogName: str
    DatabaseName: str
    WorkGroup: Optional[str] = None

class GetNamedQueryInputRequestTypeDef(BaseModel):
    NamedQueryId: str

class GetNotebookMetadataInputRequestTypeDef(BaseModel):
    NotebookId: str

class GetPreparedStatementInputRequestTypeDef(BaseModel):
    StatementName: str
    WorkGroup: str

class GetQueryExecutionInputRequestTypeDef(BaseModel):
    QueryExecutionId: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetQueryResultsInputRequestTypeDef(BaseModel):
    QueryExecutionId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetQueryRuntimeStatisticsInputRequestTypeDef(BaseModel):
    QueryExecutionId: str

class GetSessionRequestRequestTypeDef(BaseModel):
    SessionId: str

class SessionStatisticsTypeDef(BaseModel):
    DpuExecutionInMillis: Optional[int] = None

class SessionStatusTypeDef(BaseModel):
    StartDateTime: Optional[datetime] = None
    LastModifiedDateTime: Optional[datetime] = None
    EndDateTime: Optional[datetime] = None
    IdleSinceDateTime: Optional[datetime] = None
    State: Optional[SessionStateType] = None
    StateChangeReason: Optional[str] = None

class GetSessionStatusRequestRequestTypeDef(BaseModel):
    SessionId: str

class GetTableMetadataInputRequestTypeDef(BaseModel):
    CatalogName: str
    DatabaseName: str
    TableName: str
    WorkGroup: Optional[str] = None

class GetWorkGroupInputRequestTypeDef(BaseModel):
    WorkGroup: str

class IdentityCenterConfigurationTypeDef(BaseModel):
    EnableIdentityCenter: Optional[bool] = None
    IdentityCenterInstanceArn: Optional[str] = None

class ImportNotebookInputRequestTypeDef(BaseModel):
    WorkGroup: str
    Name: str
    Type: Literal["IPYNB"]
    Payload: Optional[str] = None
    NotebookS3LocationUri: Optional[str] = None
    ClientRequestToken: Optional[str] = None

class ListApplicationDPUSizesInputRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListCalculationExecutionsRequestRequestTypeDef(BaseModel):
    SessionId: str
    StateFilter: Optional[CalculationExecutionStateType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListCapacityReservationsInputRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDataCatalogsInputRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WorkGroup: Optional[str] = None

class ListDatabasesInputRequestTypeDef(BaseModel):
    CatalogName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WorkGroup: Optional[str] = None

class ListEngineVersionsInputRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListExecutorsRequestRequestTypeDef(BaseModel):
    SessionId: str
    ExecutorStateFilter: Optional[ExecutorStateType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListNamedQueriesInputRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WorkGroup: Optional[str] = None

class ListNotebookSessionsRequestRequestTypeDef(BaseModel):
    NotebookId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class NotebookSessionSummaryTypeDef(BaseModel):
    SessionId: Optional[str] = None
    CreationTime: Optional[datetime] = None

class ListPreparedStatementsInputRequestTypeDef(BaseModel):
    WorkGroup: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class PreparedStatementSummaryTypeDef(BaseModel):
    StatementName: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None

class ListQueryExecutionsInputRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WorkGroup: Optional[str] = None

class ListSessionsRequestRequestTypeDef(BaseModel):
    WorkGroup: str
    StateFilter: Optional[SessionStateType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTableMetadataInputRequestTypeDef(BaseModel):
    CatalogName: str
    DatabaseName: str
    Expression: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WorkGroup: Optional[str] = None

class ListTagsForResourceInputRequestTypeDef(BaseModel):
    ResourceARN: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListWorkGroupsInputRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class QueryExecutionContextTypeDef(BaseModel):
    Database: Optional[str] = None
    Catalog: Optional[str] = None

class ResultReuseInformationTypeDef(BaseModel):
    ReusedPreviousResult: bool

class QueryResultsS3AccessGrantsConfigurationTypeDef(BaseModel):
    EnableS3AccessGrants: bool
    AuthenticationType: Literal["DIRECTORY_IDENTITY"]
    CreateUserLevelPrefix: Optional[bool] = None

class QueryRuntimeStatisticsRowsTypeDef(BaseModel):
    InputRows: Optional[int] = None
    InputBytes: Optional[int] = None
    OutputBytes: Optional[int] = None
    OutputRows: Optional[int] = None

class QueryRuntimeStatisticsTimelineTypeDef(BaseModel):
    QueryQueueTimeInMillis: Optional[int] = None
    ServicePreProcessingTimeInMillis: Optional[int] = None
    QueryPlanningTimeInMillis: Optional[int] = None
    EngineExecutionTimeInMillis: Optional[int] = None
    ServiceProcessingTimeInMillis: Optional[int] = None
    TotalExecutionTimeInMillis: Optional[int] = None

class QueryStagePlanNodeTypeDef(BaseModel):
    Name: Optional[str] = None
    Identifier: Optional[str] = None
    Children: Optional[List[Dict[str, Any]]] = None
    RemoteSources: Optional[List[str]] = None

class QueryStageTypeDef(BaseModel):
    StageId: Optional[int] = None
    State: Optional[str] = None
    OutputBytes: Optional[int] = None
    OutputRows: Optional[int] = None
    InputBytes: Optional[int] = None
    InputRows: Optional[int] = None
    ExecutionTime: Optional[int] = None
    QueryStagePlan: Optional["QueryStagePlanNodeTypeDef"] = None
    SubStages: Optional[List[Dict[str, Any]]] = None

class ResultReuseByAgeConfigurationTypeDef(BaseModel):
    Enabled: bool
    MaxAgeInMinutes: Optional[int] = None

class StopCalculationExecutionRequestRequestTypeDef(BaseModel):
    CalculationExecutionId: str

class StopQueryExecutionInputRequestTypeDef(BaseModel):
    QueryExecutionId: str

class TerminateSessionRequestRequestTypeDef(BaseModel):
    SessionId: str

class UntagResourceInputRequestTypeDef(BaseModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateCapacityReservationInputRequestTypeDef(BaseModel):
    TargetDpus: int
    Name: str

class UpdateDataCatalogInputRequestTypeDef(BaseModel):
    Name: str
    Type: DataCatalogTypeType
    Description: Optional[str] = None
    Parameters: Optional[Mapping[str, str]] = None

class UpdateNamedQueryInputRequestTypeDef(BaseModel):
    NamedQueryId: str
    Name: str
    QueryString: str
    Description: Optional[str] = None

class UpdateNotebookInputRequestTypeDef(BaseModel):
    NotebookId: str
    Payload: str
    Type: Literal["IPYNB"]
    SessionId: Optional[str] = None
    ClientRequestToken: Optional[str] = None

class UpdateNotebookMetadataInputRequestTypeDef(BaseModel):
    NotebookId: str
    Name: str
    ClientRequestToken: Optional[str] = None

class UpdatePreparedStatementInputRequestTypeDef(BaseModel):
    StatementName: str
    WorkGroup: str
    QueryStatement: str
    Description: Optional[str] = None

class QueryExecutionStatusTypeDef(BaseModel):
    State: Optional[QueryExecutionStateType] = None
    StateChangeReason: Optional[str] = None
    SubmissionDateTime: Optional[datetime] = None
    CompletionDateTime: Optional[datetime] = None
    AthenaError: Optional[AthenaErrorTypeDef] = None

class CreateNamedQueryOutputTypeDef(BaseModel):
    NamedQueryId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNotebookOutputTypeDef(BaseModel):
    NotebookId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePresignedNotebookUrlResponseTypeDef(BaseModel):
    NotebookUrl: str
    AuthToken: str
    AuthTokenExpirationTime: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetCalculationExecutionCodeResponseTypeDef(BaseModel):
    CodeBlock: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetNamedQueryOutputTypeDef(BaseModel):
    NamedQuery: NamedQueryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ImportNotebookOutputTypeDef(BaseModel):
    NotebookId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationDPUSizesOutputTypeDef(BaseModel):
    ApplicationDPUSizes: List[ApplicationDPUSizesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListNamedQueriesOutputTypeDef(BaseModel):
    NamedQueryIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListQueryExecutionsOutputTypeDef(BaseModel):
    QueryExecutionIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class StartCalculationExecutionResponseTypeDef(BaseModel):
    CalculationExecutionId: str
    State: CalculationExecutionStateType
    ResponseMetadata: ResponseMetadataTypeDef

class StartQueryExecutionOutputTypeDef(BaseModel):
    QueryExecutionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartSessionResponseTypeDef(BaseModel):
    SessionId: str
    State: SessionStateType
    ResponseMetadata: ResponseMetadataTypeDef

class StopCalculationExecutionResponseTypeDef(BaseModel):
    State: CalculationExecutionStateType
    ResponseMetadata: ResponseMetadataTypeDef

class TerminateSessionResponseTypeDef(BaseModel):
    State: SessionStateType
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetNamedQueryOutputTypeDef(BaseModel):
    NamedQueries: List[NamedQueryTypeDef]
    UnprocessedNamedQueryIds: List[UnprocessedNamedQueryIdTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetPreparedStatementOutputTypeDef(BaseModel):
    PreparedStatement: PreparedStatementTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetPreparedStatementOutputTypeDef(BaseModel):
    PreparedStatements: List[PreparedStatementTypeDef]
    UnprocessedPreparedStatementNames: List[UnprocessedPreparedStatementNameTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartCalculationExecutionRequestRequestTypeDef(BaseModel):
    SessionId: str
    Description: Optional[str] = None
    CalculationConfiguration: Optional[CalculationConfigurationTypeDef] = None
    CodeBlock: Optional[str] = None
    ClientRequestToken: Optional[str] = None

class CalculationSummaryTypeDef(BaseModel):
    CalculationExecutionId: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[CalculationStatusTypeDef] = None

class GetCalculationExecutionResponseTypeDef(BaseModel):
    CalculationExecutionId: str
    SessionId: str
    Description: str
    WorkingDirectory: str
    Status: CalculationStatusTypeDef
    Statistics: CalculationStatisticsTypeDef
    Result: CalculationResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetCalculationExecutionStatusResponseTypeDef(BaseModel):
    Status: CalculationStatusTypeDef
    Statistics: CalculationStatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CapacityReservationTypeDef(BaseModel):
    Name: str
    Status: CapacityReservationStatusType
    TargetDpus: int
    AllocatedDpus: int
    CreationTime: datetime
    LastAllocation: Optional[CapacityAllocationTypeDef] = None
    LastSuccessfulAllocationTime: Optional[datetime] = None

class CapacityAssignmentConfigurationTypeDef(BaseModel):
    CapacityReservationName: Optional[str] = None
    CapacityAssignments: Optional[List[CapacityAssignmentOutputTypeDef]] = None

class ResultSetMetadataTypeDef(BaseModel):
    ColumnInfo: Optional[List[ColumnInfoTypeDef]] = None

class TableMetadataTypeDef(BaseModel):
    Name: str
    CreateTime: Optional[datetime] = None
    LastAccessTime: Optional[datetime] = None
    TableType: Optional[str] = None
    Columns: Optional[List[ColumnTypeDef]] = None
    PartitionKeys: Optional[List[ColumnTypeDef]] = None
    Parameters: Optional[Dict[str, str]] = None

class CreateCapacityReservationInputRequestTypeDef(BaseModel):
    TargetDpus: int
    Name: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateDataCatalogInputRequestTypeDef(BaseModel):
    Name: str
    Type: DataCatalogTypeType
    Description: Optional[str] = None
    Parameters: Optional[Mapping[str, str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceOutputTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TagResourceInputRequestTypeDef(BaseModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class ListDataCatalogsOutputTypeDef(BaseModel):
    DataCatalogsSummary: List[DataCatalogSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetDataCatalogOutputTypeDef(BaseModel):
    DataCatalog: DataCatalogTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDatabaseOutputTypeDef(BaseModel):
    Database: DatabaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDatabasesOutputTypeDef(BaseModel):
    DatabaseList: List[DatabaseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RowTypeDef(BaseModel):
    Data: Optional[List[DatumTypeDef]] = None

class ResultConfigurationTypeDef(BaseModel):
    OutputLocation: Optional[str] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None
    ExpectedBucketOwner: Optional[str] = None
    AclConfiguration: Optional[AclConfigurationTypeDef] = None

class ResultConfigurationUpdatesTypeDef(BaseModel):
    OutputLocation: Optional[str] = None
    RemoveOutputLocation: Optional[bool] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None
    RemoveEncryptionConfiguration: Optional[bool] = None
    ExpectedBucketOwner: Optional[str] = None
    RemoveExpectedBucketOwner: Optional[bool] = None
    AclConfiguration: Optional[AclConfigurationTypeDef] = None
    RemoveAclConfiguration: Optional[bool] = None

class SessionConfigurationTypeDef(BaseModel):
    ExecutionRole: Optional[str] = None
    WorkingDirectory: Optional[str] = None
    IdleTimeoutSeconds: Optional[int] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None

class StartSessionRequestRequestTypeDef(BaseModel):
    WorkGroup: str
    EngineConfiguration: EngineConfigurationTypeDef
    Description: Optional[str] = None
    NotebookVersion: Optional[str] = None
    SessionIdleTimeoutInMinutes: Optional[int] = None
    ClientRequestToken: Optional[str] = None

class ListEngineVersionsOutputTypeDef(BaseModel):
    EngineVersions: List[EngineVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class WorkGroupSummaryTypeDef(BaseModel):
    Name: Optional[str] = None
    State: Optional[WorkGroupStateType] = None
    Description: Optional[str] = None
    CreationTime: Optional[datetime] = None
    EngineVersion: Optional[EngineVersionTypeDef] = None
    IdentityCenterApplicationArn: Optional[str] = None

class ListExecutorsResponseTypeDef(BaseModel):
    SessionId: str
    ExecutorsSummary: List[ExecutorsSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ExportNotebookOutputTypeDef(BaseModel):
    NotebookMetadata: NotebookMetadataTypeDef
    Payload: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetNotebookMetadataOutputTypeDef(BaseModel):
    NotebookMetadata: NotebookMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListNotebookMetadataOutputTypeDef(BaseModel):
    NotebookMetadataList: List[NotebookMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListNotebookMetadataInputRequestTypeDef(BaseModel):
    WorkGroup: str
    Filters: Optional[FilterDefinitionTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetQueryResultsInputGetQueryResultsPaginateTypeDef(BaseModel):
    QueryExecutionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataCatalogsInputListDataCatalogsPaginateTypeDef(BaseModel):
    WorkGroup: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDatabasesInputListDatabasesPaginateTypeDef(BaseModel):
    CatalogName: str
    WorkGroup: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListNamedQueriesInputListNamedQueriesPaginateTypeDef(BaseModel):
    WorkGroup: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListQueryExecutionsInputListQueryExecutionsPaginateTypeDef(BaseModel):
    WorkGroup: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTableMetadataInputListTableMetadataPaginateTypeDef(BaseModel):
    CatalogName: str
    DatabaseName: str
    Expression: Optional[str] = None
    WorkGroup: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceInputListTagsForResourcePaginateTypeDef(BaseModel):
    ResourceARN: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetSessionStatusResponseTypeDef(BaseModel):
    SessionId: str
    Status: SessionStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SessionSummaryTypeDef(BaseModel):
    SessionId: Optional[str] = None
    Description: Optional[str] = None
    EngineVersion: Optional[EngineVersionTypeDef] = None
    NotebookVersion: Optional[str] = None
    Status: Optional[SessionStatusTypeDef] = None

class ListNotebookSessionsResponseTypeDef(BaseModel):
    NotebookSessionsList: List[NotebookSessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListPreparedStatementsOutputTypeDef(BaseModel):
    PreparedStatements: List[PreparedStatementSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class QueryExecutionStatisticsTypeDef(BaseModel):
    EngineExecutionTimeInMillis: Optional[int] = None
    DataScannedInBytes: Optional[int] = None
    DataManifestLocation: Optional[str] = None
    TotalExecutionTimeInMillis: Optional[int] = None
    QueryQueueTimeInMillis: Optional[int] = None
    ServicePreProcessingTimeInMillis: Optional[int] = None
    QueryPlanningTimeInMillis: Optional[int] = None
    ServiceProcessingTimeInMillis: Optional[int] = None
    ResultReuseInformation: Optional[ResultReuseInformationTypeDef] = None

class QueryRuntimeStatisticsTypeDef(BaseModel):
    Timeline: Optional[QueryRuntimeStatisticsTimelineTypeDef] = None
    Rows: Optional[QueryRuntimeStatisticsRowsTypeDef] = None
    OutputStage: Optional["QueryStageTypeDef"] = None

class ResultReuseConfigurationTypeDef(BaseModel):
    ResultReuseByAgeConfiguration: Optional[ResultReuseByAgeConfigurationTypeDef] = None

class ListCalculationExecutionsResponseTypeDef(BaseModel):
    Calculations: List[CalculationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetCapacityReservationOutputTypeDef(BaseModel):
    CapacityReservation: CapacityReservationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCapacityReservationsOutputTypeDef(BaseModel):
    CapacityReservations: List[CapacityReservationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetCapacityAssignmentConfigurationOutputTypeDef(BaseModel):
    CapacityAssignmentConfiguration: CapacityAssignmentConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutCapacityAssignmentConfigurationInputRequestTypeDef(BaseModel):
    CapacityReservationName: str
    CapacityAssignments: Sequence[CapacityAssignmentUnionTypeDef]

class GetTableMetadataOutputTypeDef(BaseModel):
    TableMetadata: TableMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTableMetadataOutputTypeDef(BaseModel):
    TableMetadataList: List[TableMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ResultSetTypeDef(BaseModel):
    Rows: Optional[List[RowTypeDef]] = None
    ResultSetMetadata: Optional[ResultSetMetadataTypeDef] = None

class WorkGroupConfigurationTypeDef(BaseModel):
    ResultConfiguration: Optional[ResultConfigurationTypeDef] = None
    EnforceWorkGroupConfiguration: Optional[bool] = None
    PublishCloudWatchMetricsEnabled: Optional[bool] = None
    BytesScannedCutoffPerQuery: Optional[int] = None
    RequesterPaysEnabled: Optional[bool] = None
    EngineVersion: Optional[EngineVersionTypeDef] = None
    AdditionalConfiguration: Optional[str] = None
    ExecutionRole: Optional[str] = None
    CustomerContentEncryptionConfiguration: Optional[       CustomerContentEncryptionConfigurationTypeDef     ] = None
    EnableMinimumEncryptionConfiguration: Optional[bool] = None
    IdentityCenterConfiguration: Optional[IdentityCenterConfigurationTypeDef] = None
    QueryResultsS3AccessGrantsConfiguration: Optional[       QueryResultsS3AccessGrantsConfigurationTypeDef     ] = None

class WorkGroupConfigurationUpdatesTypeDef(BaseModel):
    EnforceWorkGroupConfiguration: Optional[bool] = None
    ResultConfigurationUpdates: Optional[ResultConfigurationUpdatesTypeDef] = None
    PublishCloudWatchMetricsEnabled: Optional[bool] = None
    BytesScannedCutoffPerQuery: Optional[int] = None
    RemoveBytesScannedCutoffPerQuery: Optional[bool] = None
    RequesterPaysEnabled: Optional[bool] = None
    EngineVersion: Optional[EngineVersionTypeDef] = None
    RemoveCustomerContentEncryptionConfiguration: Optional[bool] = None
    AdditionalConfiguration: Optional[str] = None
    ExecutionRole: Optional[str] = None
    CustomerContentEncryptionConfiguration: Optional[       CustomerContentEncryptionConfigurationTypeDef     ] = None
    EnableMinimumEncryptionConfiguration: Optional[bool] = None
    QueryResultsS3AccessGrantsConfiguration: Optional[       QueryResultsS3AccessGrantsConfigurationTypeDef     ] = None

class GetSessionResponseTypeDef(BaseModel):
    SessionId: str
    Description: str
    WorkGroup: str
    EngineVersion: str
    EngineConfiguration: EngineConfigurationOutputTypeDef
    NotebookVersion: str
    SessionConfiguration: SessionConfigurationTypeDef
    Status: SessionStatusTypeDef
    Statistics: SessionStatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkGroupsOutputTypeDef(BaseModel):
    WorkGroups: List[WorkGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListSessionsResponseTypeDef(BaseModel):
    Sessions: List[SessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetQueryRuntimeStatisticsOutputTypeDef(BaseModel):
    QueryRuntimeStatistics: QueryRuntimeStatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class QueryExecutionTypeDef(BaseModel):
    QueryExecutionId: Optional[str] = None
    Query: Optional[str] = None
    StatementType: Optional[StatementTypeType] = None
    ResultConfiguration: Optional[ResultConfigurationTypeDef] = None
    ResultReuseConfiguration: Optional[ResultReuseConfigurationTypeDef] = None
    QueryExecutionContext: Optional[QueryExecutionContextTypeDef] = None
    Status: Optional[QueryExecutionStatusTypeDef] = None
    Statistics: Optional[QueryExecutionStatisticsTypeDef] = None
    WorkGroup: Optional[str] = None
    EngineVersion: Optional[EngineVersionTypeDef] = None
    ExecutionParameters: Optional[List[str]] = None
    SubstatementType: Optional[str] = None
    QueryResultsS3AccessGrantsConfiguration: Optional[       QueryResultsS3AccessGrantsConfigurationTypeDef     ] = None

class StartQueryExecutionInputRequestTypeDef(BaseModel):
    QueryString: str
    ClientRequestToken: Optional[str] = None
    QueryExecutionContext: Optional[QueryExecutionContextTypeDef] = None
    ResultConfiguration: Optional[ResultConfigurationTypeDef] = None
    WorkGroup: Optional[str] = None
    ExecutionParameters: Optional[Sequence[str]] = None
    ResultReuseConfiguration: Optional[ResultReuseConfigurationTypeDef] = None

class GetQueryResultsOutputTypeDef(BaseModel):
    UpdateCount: int
    ResultSet: ResultSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateWorkGroupInputRequestTypeDef(BaseModel):
    Name: str
    Configuration: Optional[WorkGroupConfigurationTypeDef] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class WorkGroupTypeDef(BaseModel):
    Name: str
    State: Optional[WorkGroupStateType] = None
    Configuration: Optional[WorkGroupConfigurationTypeDef] = None
    Description: Optional[str] = None
    CreationTime: Optional[datetime] = None
    IdentityCenterApplicationArn: Optional[str] = None

class UpdateWorkGroupInputRequestTypeDef(BaseModel):
    WorkGroup: str
    Description: Optional[str] = None
    ConfigurationUpdates: Optional[WorkGroupConfigurationUpdatesTypeDef] = None
    State: Optional[WorkGroupStateType] = None

class BatchGetQueryExecutionOutputTypeDef(BaseModel):
    QueryExecutions: List[QueryExecutionTypeDef]
    UnprocessedQueryExecutionIds: List[UnprocessedQueryExecutionIdTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetQueryExecutionOutputTypeDef(BaseModel):
    QueryExecution: QueryExecutionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetWorkGroupOutputTypeDef(BaseModel):
    WorkGroup: WorkGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


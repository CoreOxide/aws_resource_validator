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
from aws_resource_validator.pydantic_models.athena_constants import *

class AclConfigurationTypeDef(BaseValidatorModel):
    S3AclOption: Literal["BUCKET_OWNER_FULL_CONTROL"]

class ApplicationDPUSizesTypeDef(BaseValidatorModel):
    ApplicationRuntimeId: Optional[str] = None
    SupportedDPUSizes: Optional[List[int]] = None

class AthenaErrorTypeDef(BaseValidatorModel):
    ErrorCategory: Optional[int] = None
    ErrorType: Optional[int] = None
    Retryable: Optional[bool] = None
    ErrorMessage: Optional[str] = None

class BatchGetNamedQueryInputRequestTypeDef(BaseValidatorModel):
    NamedQueryIds: Sequence[str]

class NamedQueryTypeDef(BaseValidatorModel):
    Name: str
    Database: str
    QueryString: str
    Description: Optional[str] = None
    NamedQueryId: Optional[str] = None
    WorkGroup: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class UnprocessedNamedQueryIdTypeDef(BaseValidatorModel):
    NamedQueryId: Optional[str] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class BatchGetPreparedStatementInputRequestTypeDef(BaseValidatorModel):
    PreparedStatementNames: Sequence[str]
    WorkGroup: str

class PreparedStatementTypeDef(BaseValidatorModel):
    StatementName: Optional[str] = None
    QueryStatement: Optional[str] = None
    WorkGroupName: Optional[str] = None
    Description: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None

class UnprocessedPreparedStatementNameTypeDef(BaseValidatorModel):
    StatementName: Optional[str] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class BatchGetQueryExecutionInputRequestTypeDef(BaseValidatorModel):
    QueryExecutionIds: Sequence[str]

class UnprocessedQueryExecutionIdTypeDef(BaseValidatorModel):
    QueryExecutionId: Optional[str] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class CalculationConfigurationTypeDef(BaseValidatorModel):
    CodeBlock: Optional[str] = None

class CalculationResultTypeDef(BaseValidatorModel):
    StdOutS3Uri: Optional[str] = None
    StdErrorS3Uri: Optional[str] = None
    ResultS3Uri: Optional[str] = None
    ResultType: Optional[str] = None

class CalculationStatisticsTypeDef(BaseValidatorModel):
    DpuExecutionInMillis: Optional[int] = None
    Progress: Optional[str] = None

class CalculationStatusTypeDef(BaseValidatorModel):
    SubmissionDateTime: Optional[datetime] = None
    CompletionDateTime: Optional[datetime] = None
    State: Optional[CalculationExecutionStateType] = None
    StateChangeReason: Optional[str] = None

class CancelCapacityReservationInputRequestTypeDef(BaseValidatorModel):
    Name: str

class CapacityAllocationTypeDef(BaseValidatorModel):
    Status: CapacityAllocationStatusType
    RequestTime: datetime
    StatusMessage: Optional[str] = None
    RequestCompletionTime: Optional[datetime] = None

class CapacityAssignmentOutputTypeDef(BaseValidatorModel):
    WorkGroupNames: Optional[List[str]] = None

class CapacityAssignmentTypeDef(BaseValidatorModel):
    WorkGroupNames: Optional[Sequence[str]] = None

class ColumnInfoTypeDef(BaseValidatorModel):
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

class ColumnTypeDef(BaseValidatorModel):
    Name: str
    Type: Optional[str] = None
    Comment: Optional[str] = None

class TagTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class CreateNamedQueryInputRequestTypeDef(BaseValidatorModel):
    Name: str
    Database: str
    QueryString: str
    Description: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    WorkGroup: Optional[str] = None

class CreateNotebookInputRequestTypeDef(BaseValidatorModel):
    WorkGroup: str
    Name: str
    ClientRequestToken: Optional[str] = None

class CreatePreparedStatementInputRequestTypeDef(BaseValidatorModel):
    StatementName: str
    WorkGroup: str
    QueryStatement: str
    Description: Optional[str] = None

class CreatePresignedNotebookUrlRequestRequestTypeDef(BaseValidatorModel):
    SessionId: str

class CustomerContentEncryptionConfigurationTypeDef(BaseValidatorModel):
    KmsKey: str

class DataCatalogSummaryTypeDef(BaseValidatorModel):
    CatalogName: Optional[str] = None
    Type: Optional[DataCatalogTypeType] = None

class DataCatalogTypeDef(BaseValidatorModel):
    Name: str
    Type: DataCatalogTypeType
    Description: Optional[str] = None
    Parameters: Optional[Dict[str, str]] = None

class DatabaseTypeDef(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    Parameters: Optional[Dict[str, str]] = None

class DatumTypeDef(BaseValidatorModel):
    VarCharValue: Optional[str] = None

class DeleteCapacityReservationInputRequestTypeDef(BaseValidatorModel):
    Name: str

class DeleteDataCatalogInputRequestTypeDef(BaseValidatorModel):
    Name: str

class DeleteNamedQueryInputRequestTypeDef(BaseValidatorModel):
    NamedQueryId: str

class DeleteNotebookInputRequestTypeDef(BaseValidatorModel):
    NotebookId: str

class DeletePreparedStatementInputRequestTypeDef(BaseValidatorModel):
    StatementName: str
    WorkGroup: str

class DeleteWorkGroupInputRequestTypeDef(BaseValidatorModel):
    WorkGroup: str
    RecursiveDeleteOption: Optional[bool] = None

class EncryptionConfigurationTypeDef(BaseValidatorModel):
    EncryptionOption: EncryptionOptionType
    KmsKey: Optional[str] = None

class EngineConfigurationOutputTypeDef(BaseValidatorModel):
    MaxConcurrentDpus: int
    CoordinatorDpuSize: Optional[int] = None
    DefaultExecutorDpuSize: Optional[int] = None
    AdditionalConfigs: Optional[Dict[str, str]] = None
    SparkProperties: Optional[Dict[str, str]] = None

class EngineConfigurationTypeDef(BaseValidatorModel):
    MaxConcurrentDpus: int
    CoordinatorDpuSize: Optional[int] = None
    DefaultExecutorDpuSize: Optional[int] = None
    AdditionalConfigs: Optional[Mapping[str, str]] = None
    SparkProperties: Optional[Mapping[str, str]] = None

class EngineVersionTypeDef(BaseValidatorModel):
    SelectedEngineVersion: Optional[str] = None
    EffectiveEngineVersion: Optional[str] = None

class ExecutorsSummaryTypeDef(BaseValidatorModel):
    ExecutorId: str
    ExecutorType: Optional[ExecutorTypeType] = None
    StartDateTime: Optional[int] = None
    TerminationDateTime: Optional[int] = None
    ExecutorState: Optional[ExecutorStateType] = None
    ExecutorSize: Optional[int] = None

class ExportNotebookInputRequestTypeDef(BaseValidatorModel):
    NotebookId: str

class NotebookMetadataTypeDef(BaseValidatorModel):
    NotebookId: Optional[str] = None
    Name: Optional[str] = None
    WorkGroup: Optional[str] = None
    CreationTime: Optional[datetime] = None
    Type: Optional[Literal["IPYNB"]] = None
    LastModifiedTime: Optional[datetime] = None

class FilterDefinitionTypeDef(BaseValidatorModel):
    Name: Optional[str] = None

class GetCalculationExecutionCodeRequestRequestTypeDef(BaseValidatorModel):
    CalculationExecutionId: str

class GetCalculationExecutionRequestRequestTypeDef(BaseValidatorModel):
    CalculationExecutionId: str

class GetCalculationExecutionStatusRequestRequestTypeDef(BaseValidatorModel):
    CalculationExecutionId: str

class GetCapacityAssignmentConfigurationInputRequestTypeDef(BaseValidatorModel):
    CapacityReservationName: str

class GetCapacityReservationInputRequestTypeDef(BaseValidatorModel):
    Name: str

class GetDataCatalogInputRequestTypeDef(BaseValidatorModel):
    Name: str
    WorkGroup: Optional[str] = None

class GetDatabaseInputRequestTypeDef(BaseValidatorModel):
    CatalogName: str
    DatabaseName: str
    WorkGroup: Optional[str] = None

class GetNamedQueryInputRequestTypeDef(BaseValidatorModel):
    NamedQueryId: str

class GetNotebookMetadataInputRequestTypeDef(BaseValidatorModel):
    NotebookId: str

class GetPreparedStatementInputRequestTypeDef(BaseValidatorModel):
    StatementName: str
    WorkGroup: str

class GetQueryExecutionInputRequestTypeDef(BaseValidatorModel):
    QueryExecutionId: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetQueryResultsInputRequestTypeDef(BaseValidatorModel):
    QueryExecutionId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetQueryRuntimeStatisticsInputRequestTypeDef(BaseValidatorModel):
    QueryExecutionId: str

class GetSessionRequestRequestTypeDef(BaseValidatorModel):
    SessionId: str

class SessionStatisticsTypeDef(BaseValidatorModel):
    DpuExecutionInMillis: Optional[int] = None

class SessionStatusTypeDef(BaseValidatorModel):
    StartDateTime: Optional[datetime] = None
    LastModifiedDateTime: Optional[datetime] = None
    EndDateTime: Optional[datetime] = None
    IdleSinceDateTime: Optional[datetime] = None
    State: Optional[SessionStateType] = None
    StateChangeReason: Optional[str] = None

class GetSessionStatusRequestRequestTypeDef(BaseValidatorModel):
    SessionId: str

class GetTableMetadataInputRequestTypeDef(BaseValidatorModel):
    CatalogName: str
    DatabaseName: str
    TableName: str
    WorkGroup: Optional[str] = None

class GetWorkGroupInputRequestTypeDef(BaseValidatorModel):
    WorkGroup: str

class IdentityCenterConfigurationTypeDef(BaseValidatorModel):
    EnableIdentityCenter: Optional[bool] = None
    IdentityCenterInstanceArn: Optional[str] = None

class ImportNotebookInputRequestTypeDef(BaseValidatorModel):
    WorkGroup: str
    Name: str
    Type: Literal["IPYNB"]
    Payload: Optional[str] = None
    NotebookS3LocationUri: Optional[str] = None
    ClientRequestToken: Optional[str] = None

class ListApplicationDPUSizesInputRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListCalculationExecutionsRequestRequestTypeDef(BaseValidatorModel):
    SessionId: str
    StateFilter: Optional[CalculationExecutionStateType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListCapacityReservationsInputRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDataCatalogsInputRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WorkGroup: Optional[str] = None

class ListDatabasesInputRequestTypeDef(BaseValidatorModel):
    CatalogName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WorkGroup: Optional[str] = None

class ListEngineVersionsInputRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListExecutorsRequestRequestTypeDef(BaseValidatorModel):
    SessionId: str
    ExecutorStateFilter: Optional[ExecutorStateType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListNamedQueriesInputRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WorkGroup: Optional[str] = None

class ListNotebookSessionsRequestRequestTypeDef(BaseValidatorModel):
    NotebookId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class NotebookSessionSummaryTypeDef(BaseValidatorModel):
    SessionId: Optional[str] = None
    CreationTime: Optional[datetime] = None

class ListPreparedStatementsInputRequestTypeDef(BaseValidatorModel):
    WorkGroup: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class PreparedStatementSummaryTypeDef(BaseValidatorModel):
    StatementName: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None

class ListQueryExecutionsInputRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WorkGroup: Optional[str] = None

class ListSessionsRequestRequestTypeDef(BaseValidatorModel):
    WorkGroup: str
    StateFilter: Optional[SessionStateType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTableMetadataInputRequestTypeDef(BaseValidatorModel):
    CatalogName: str
    DatabaseName: str
    Expression: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WorkGroup: Optional[str] = None

class ListTagsForResourceInputRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListWorkGroupsInputRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class QueryExecutionContextTypeDef(BaseValidatorModel):
    Database: Optional[str] = None
    Catalog: Optional[str] = None

class ResultReuseInformationTypeDef(BaseValidatorModel):
    ReusedPreviousResult: bool

class QueryResultsS3AccessGrantsConfigurationTypeDef(BaseValidatorModel):
    EnableS3AccessGrants: bool
    AuthenticationType: Literal["DIRECTORY_IDENTITY"]
    CreateUserLevelPrefix: Optional[bool] = None

class QueryRuntimeStatisticsRowsTypeDef(BaseValidatorModel):
    InputRows: Optional[int] = None
    InputBytes: Optional[int] = None
    OutputBytes: Optional[int] = None
    OutputRows: Optional[int] = None

class QueryRuntimeStatisticsTimelineTypeDef(BaseValidatorModel):
    QueryQueueTimeInMillis: Optional[int] = None
    ServicePreProcessingTimeInMillis: Optional[int] = None
    QueryPlanningTimeInMillis: Optional[int] = None
    EngineExecutionTimeInMillis: Optional[int] = None
    ServiceProcessingTimeInMillis: Optional[int] = None
    TotalExecutionTimeInMillis: Optional[int] = None

class QueryStagePlanNodeTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Identifier: Optional[str] = None
    Children: Optional[List[Dict[str, Any]]] = None
    RemoteSources: Optional[List[str]] = None

class QueryStageTypeDef(BaseValidatorModel):
    StageId: Optional[int] = None
    State: Optional[str] = None
    OutputBytes: Optional[int] = None
    OutputRows: Optional[int] = None
    InputBytes: Optional[int] = None
    InputRows: Optional[int] = None
    ExecutionTime: Optional[int] = None
    QueryStagePlan: Optional["QueryStagePlanNodeTypeDef"] = None
    SubStages: Optional[List[Dict[str, Any]]] = None

class ResultReuseByAgeConfigurationTypeDef(BaseValidatorModel):
    Enabled: bool
    MaxAgeInMinutes: Optional[int] = None

class StopCalculationExecutionRequestRequestTypeDef(BaseValidatorModel):
    CalculationExecutionId: str

class StopQueryExecutionInputRequestTypeDef(BaseValidatorModel):
    QueryExecutionId: str

class TerminateSessionRequestRequestTypeDef(BaseValidatorModel):
    SessionId: str

class UntagResourceInputRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateCapacityReservationInputRequestTypeDef(BaseValidatorModel):
    TargetDpus: int
    Name: str

class UpdateDataCatalogInputRequestTypeDef(BaseValidatorModel):
    Name: str
    Type: DataCatalogTypeType
    Description: Optional[str] = None
    Parameters: Optional[Mapping[str, str]] = None

class UpdateNamedQueryInputRequestTypeDef(BaseValidatorModel):
    NamedQueryId: str
    Name: str
    QueryString: str
    Description: Optional[str] = None

class UpdateNotebookInputRequestTypeDef(BaseValidatorModel):
    NotebookId: str
    Payload: str
    Type: Literal["IPYNB"]
    SessionId: Optional[str] = None
    ClientRequestToken: Optional[str] = None

class UpdateNotebookMetadataInputRequestTypeDef(BaseValidatorModel):
    NotebookId: str
    Name: str
    ClientRequestToken: Optional[str] = None

class UpdatePreparedStatementInputRequestTypeDef(BaseValidatorModel):
    StatementName: str
    WorkGroup: str
    QueryStatement: str
    Description: Optional[str] = None

class QueryExecutionStatusTypeDef(BaseValidatorModel):
    State: Optional[QueryExecutionStateType] = None
    StateChangeReason: Optional[str] = None
    SubmissionDateTime: Optional[datetime] = None
    CompletionDateTime: Optional[datetime] = None
    AthenaError: Optional[AthenaErrorTypeDef] = None

class CreateNamedQueryOutputTypeDef(BaseValidatorModel):
    NamedQueryId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNotebookOutputTypeDef(BaseValidatorModel):
    NotebookId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePresignedNotebookUrlResponseTypeDef(BaseValidatorModel):
    NotebookUrl: str
    AuthToken: str
    AuthTokenExpirationTime: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetCalculationExecutionCodeResponseTypeDef(BaseValidatorModel):
    CodeBlock: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetNamedQueryOutputTypeDef(BaseValidatorModel):
    NamedQuery: NamedQueryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ImportNotebookOutputTypeDef(BaseValidatorModel):
    NotebookId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationDPUSizesOutputTypeDef(BaseValidatorModel):
    ApplicationDPUSizes: List[ApplicationDPUSizesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListNamedQueriesOutputTypeDef(BaseValidatorModel):
    NamedQueryIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListQueryExecutionsOutputTypeDef(BaseValidatorModel):
    QueryExecutionIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class StartCalculationExecutionResponseTypeDef(BaseValidatorModel):
    CalculationExecutionId: str
    State: CalculationExecutionStateType
    ResponseMetadata: ResponseMetadataTypeDef

class StartQueryExecutionOutputTypeDef(BaseValidatorModel):
    QueryExecutionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartSessionResponseTypeDef(BaseValidatorModel):
    SessionId: str
    State: SessionStateType
    ResponseMetadata: ResponseMetadataTypeDef

class StopCalculationExecutionResponseTypeDef(BaseValidatorModel):
    State: CalculationExecutionStateType
    ResponseMetadata: ResponseMetadataTypeDef

class TerminateSessionResponseTypeDef(BaseValidatorModel):
    State: SessionStateType
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetNamedQueryOutputTypeDef(BaseValidatorModel):
    NamedQueries: List[NamedQueryTypeDef]
    UnprocessedNamedQueryIds: List[UnprocessedNamedQueryIdTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetPreparedStatementOutputTypeDef(BaseValidatorModel):
    PreparedStatement: PreparedStatementTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetPreparedStatementOutputTypeDef(BaseValidatorModel):
    PreparedStatements: List[PreparedStatementTypeDef]
    UnprocessedPreparedStatementNames: List[UnprocessedPreparedStatementNameTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartCalculationExecutionRequestRequestTypeDef(BaseValidatorModel):
    SessionId: str
    Description: Optional[str] = None
    CalculationConfiguration: Optional[CalculationConfigurationTypeDef] = None
    CodeBlock: Optional[str] = None
    ClientRequestToken: Optional[str] = None

class CalculationSummaryTypeDef(BaseValidatorModel):
    CalculationExecutionId: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[CalculationStatusTypeDef] = None

class GetCalculationExecutionResponseTypeDef(BaseValidatorModel):
    CalculationExecutionId: str
    SessionId: str
    Description: str
    WorkingDirectory: str
    Status: CalculationStatusTypeDef
    Statistics: CalculationStatisticsTypeDef
    Result: CalculationResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetCalculationExecutionStatusResponseTypeDef(BaseValidatorModel):
    Status: CalculationStatusTypeDef
    Statistics: CalculationStatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CapacityReservationTypeDef(BaseValidatorModel):
    Name: str
    Status: CapacityReservationStatusType
    TargetDpus: int
    AllocatedDpus: int
    CreationTime: datetime
    LastAllocation: Optional[CapacityAllocationTypeDef] = None
    LastSuccessfulAllocationTime: Optional[datetime] = None

class CapacityAssignmentConfigurationTypeDef(BaseValidatorModel):
    CapacityReservationName: Optional[str] = None
    CapacityAssignments: Optional[List[CapacityAssignmentOutputTypeDef]] = None

class ResultSetMetadataTypeDef(BaseValidatorModel):
    ColumnInfo: Optional[List[ColumnInfoTypeDef]] = None

class TableMetadataTypeDef(BaseValidatorModel):
    Name: str
    CreateTime: Optional[datetime] = None
    LastAccessTime: Optional[datetime] = None
    TableType: Optional[str] = None
    Columns: Optional[List[ColumnTypeDef]] = None
    PartitionKeys: Optional[List[ColumnTypeDef]] = None
    Parameters: Optional[Dict[str, str]] = None

class CreateCapacityReservationInputRequestTypeDef(BaseValidatorModel):
    TargetDpus: int
    Name: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateDataCatalogInputRequestTypeDef(BaseValidatorModel):
    Name: str
    Type: DataCatalogTypeType
    Description: Optional[str] = None
    Parameters: Optional[Mapping[str, str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TagResourceInputRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class ListDataCatalogsOutputTypeDef(BaseValidatorModel):
    DataCatalogsSummary: List[DataCatalogSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetDataCatalogOutputTypeDef(BaseValidatorModel):
    DataCatalog: DataCatalogTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDatabaseOutputTypeDef(BaseValidatorModel):
    Database: DatabaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDatabasesOutputTypeDef(BaseValidatorModel):
    DatabaseList: List[DatabaseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RowTypeDef(BaseValidatorModel):
    Data: Optional[List[DatumTypeDef]] = None

class ResultConfigurationTypeDef(BaseValidatorModel):
    OutputLocation: Optional[str] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None
    ExpectedBucketOwner: Optional[str] = None
    AclConfiguration: Optional[AclConfigurationTypeDef] = None

class ResultConfigurationUpdatesTypeDef(BaseValidatorModel):
    OutputLocation: Optional[str] = None
    RemoveOutputLocation: Optional[bool] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None
    RemoveEncryptionConfiguration: Optional[bool] = None
    ExpectedBucketOwner: Optional[str] = None
    RemoveExpectedBucketOwner: Optional[bool] = None
    AclConfiguration: Optional[AclConfigurationTypeDef] = None
    RemoveAclConfiguration: Optional[bool] = None

class SessionConfigurationTypeDef(BaseValidatorModel):
    ExecutionRole: Optional[str] = None
    WorkingDirectory: Optional[str] = None
    IdleTimeoutSeconds: Optional[int] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None

class StartSessionRequestRequestTypeDef(BaseValidatorModel):
    WorkGroup: str
    EngineConfiguration: EngineConfigurationTypeDef
    Description: Optional[str] = None
    NotebookVersion: Optional[str] = None
    SessionIdleTimeoutInMinutes: Optional[int] = None
    ClientRequestToken: Optional[str] = None

class ListEngineVersionsOutputTypeDef(BaseValidatorModel):
    EngineVersions: List[EngineVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class WorkGroupSummaryTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    State: Optional[WorkGroupStateType] = None
    Description: Optional[str] = None
    CreationTime: Optional[datetime] = None
    EngineVersion: Optional[EngineVersionTypeDef] = None
    IdentityCenterApplicationArn: Optional[str] = None

class ListExecutorsResponseTypeDef(BaseValidatorModel):
    SessionId: str
    ExecutorsSummary: List[ExecutorsSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ExportNotebookOutputTypeDef(BaseValidatorModel):
    NotebookMetadata: NotebookMetadataTypeDef
    Payload: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetNotebookMetadataOutputTypeDef(BaseValidatorModel):
    NotebookMetadata: NotebookMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListNotebookMetadataOutputTypeDef(BaseValidatorModel):
    NotebookMetadataList: List[NotebookMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListNotebookMetadataInputRequestTypeDef(BaseValidatorModel):
    WorkGroup: str
    Filters: Optional[FilterDefinitionTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetQueryResultsInputGetQueryResultsPaginateTypeDef(BaseValidatorModel):
    QueryExecutionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataCatalogsInputListDataCatalogsPaginateTypeDef(BaseValidatorModel):
    WorkGroup: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDatabasesInputListDatabasesPaginateTypeDef(BaseValidatorModel):
    CatalogName: str
    WorkGroup: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListNamedQueriesInputListNamedQueriesPaginateTypeDef(BaseValidatorModel):
    WorkGroup: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListQueryExecutionsInputListQueryExecutionsPaginateTypeDef(BaseValidatorModel):
    WorkGroup: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTableMetadataInputListTableMetadataPaginateTypeDef(BaseValidatorModel):
    CatalogName: str
    DatabaseName: str
    Expression: Optional[str] = None
    WorkGroup: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceInputListTagsForResourcePaginateTypeDef(BaseValidatorModel):
    ResourceARN: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetSessionStatusResponseTypeDef(BaseValidatorModel):
    SessionId: str
    Status: SessionStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SessionSummaryTypeDef(BaseValidatorModel):
    SessionId: Optional[str] = None
    Description: Optional[str] = None
    EngineVersion: Optional[EngineVersionTypeDef] = None
    NotebookVersion: Optional[str] = None
    Status: Optional[SessionStatusTypeDef] = None

class ListNotebookSessionsResponseTypeDef(BaseValidatorModel):
    NotebookSessionsList: List[NotebookSessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListPreparedStatementsOutputTypeDef(BaseValidatorModel):
    PreparedStatements: List[PreparedStatementSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class QueryExecutionStatisticsTypeDef(BaseValidatorModel):
    EngineExecutionTimeInMillis: Optional[int] = None
    DataScannedInBytes: Optional[int] = None
    DataManifestLocation: Optional[str] = None
    TotalExecutionTimeInMillis: Optional[int] = None
    QueryQueueTimeInMillis: Optional[int] = None
    ServicePreProcessingTimeInMillis: Optional[int] = None
    QueryPlanningTimeInMillis: Optional[int] = None
    ServiceProcessingTimeInMillis: Optional[int] = None
    ResultReuseInformation: Optional[ResultReuseInformationTypeDef] = None

class QueryRuntimeStatisticsTypeDef(BaseValidatorModel):
    Timeline: Optional[QueryRuntimeStatisticsTimelineTypeDef] = None
    Rows: Optional[QueryRuntimeStatisticsRowsTypeDef] = None
    OutputStage: Optional["QueryStageTypeDef"] = None

class ResultReuseConfigurationTypeDef(BaseValidatorModel):
    ResultReuseByAgeConfiguration: Optional[ResultReuseByAgeConfigurationTypeDef] = None

class ListCalculationExecutionsResponseTypeDef(BaseValidatorModel):
    Calculations: List[CalculationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetCapacityReservationOutputTypeDef(BaseValidatorModel):
    CapacityReservation: CapacityReservationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCapacityReservationsOutputTypeDef(BaseValidatorModel):
    CapacityReservations: List[CapacityReservationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetCapacityAssignmentConfigurationOutputTypeDef(BaseValidatorModel):
    CapacityAssignmentConfiguration: CapacityAssignmentConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutCapacityAssignmentConfigurationInputRequestTypeDef(BaseValidatorModel):
    CapacityReservationName: str
    CapacityAssignments: Sequence[CapacityAssignmentUnionTypeDef]

class GetTableMetadataOutputTypeDef(BaseValidatorModel):
    TableMetadata: TableMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTableMetadataOutputTypeDef(BaseValidatorModel):
    TableMetadataList: List[TableMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ResultSetTypeDef(BaseValidatorModel):
    Rows: Optional[List[RowTypeDef]] = None
    ResultSetMetadata: Optional[ResultSetMetadataTypeDef] = None

class WorkGroupConfigurationTypeDef(BaseValidatorModel):
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

class WorkGroupConfigurationUpdatesTypeDef(BaseValidatorModel):
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

class GetSessionResponseTypeDef(BaseValidatorModel):
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

class ListWorkGroupsOutputTypeDef(BaseValidatorModel):
    WorkGroups: List[WorkGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListSessionsResponseTypeDef(BaseValidatorModel):
    Sessions: List[SessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetQueryRuntimeStatisticsOutputTypeDef(BaseValidatorModel):
    QueryRuntimeStatistics: QueryRuntimeStatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class QueryExecutionTypeDef(BaseValidatorModel):
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

class StartQueryExecutionInputRequestTypeDef(BaseValidatorModel):
    QueryString: str
    ClientRequestToken: Optional[str] = None
    QueryExecutionContext: Optional[QueryExecutionContextTypeDef] = None
    ResultConfiguration: Optional[ResultConfigurationTypeDef] = None
    WorkGroup: Optional[str] = None
    ExecutionParameters: Optional[Sequence[str]] = None
    ResultReuseConfiguration: Optional[ResultReuseConfigurationTypeDef] = None

class GetQueryResultsOutputTypeDef(BaseValidatorModel):
    UpdateCount: int
    ResultSet: ResultSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateWorkGroupInputRequestTypeDef(BaseValidatorModel):
    Name: str
    Configuration: Optional[WorkGroupConfigurationTypeDef] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class WorkGroupTypeDef(BaseValidatorModel):
    Name: str
    State: Optional[WorkGroupStateType] = None
    Configuration: Optional[WorkGroupConfigurationTypeDef] = None
    Description: Optional[str] = None
    CreationTime: Optional[datetime] = None
    IdentityCenterApplicationArn: Optional[str] = None

class UpdateWorkGroupInputRequestTypeDef(BaseValidatorModel):
    WorkGroup: str
    Description: Optional[str] = None
    ConfigurationUpdates: Optional[WorkGroupConfigurationUpdatesTypeDef] = None
    State: Optional[WorkGroupStateType] = None

class BatchGetQueryExecutionOutputTypeDef(BaseValidatorModel):
    QueryExecutions: List[QueryExecutionTypeDef]
    UnprocessedQueryExecutionIds: List[UnprocessedQueryExecutionIdTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetQueryExecutionOutputTypeDef(BaseValidatorModel):
    QueryExecution: QueryExecutionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetWorkGroupOutputTypeDef(BaseValidatorModel):
    WorkGroup: WorkGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


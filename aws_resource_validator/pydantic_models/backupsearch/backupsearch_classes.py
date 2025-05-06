from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.backupsearch.backupsearch_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class BackupCreationTimeFilterOutput(BaseValidatorModel):
    CreatedAfter: Optional[datetime] = None
    CreatedBefore: Optional[datetime] = None

Timestamp = Union[datetime, str]


class CurrentSearchProgress(BaseValidatorModel):
    RecoveryPointsScannedCount: Optional[int] = None
    ItemsScannedCount: Optional[int] = None
    ItemsMatchedCount: Optional[int] = None


class LongCondition(BaseValidatorModel):
    Value: int
    Operator: Optional[LongConditionOperatorType] = None


class StringCondition(BaseValidatorModel):
    Value: str
    Operator: Optional[StringConditionOperatorType] = None


class TimeConditionOutput(BaseValidatorModel):
    Value: datetime
    Operator: Optional[TimeConditionOperatorType] = None


class EBSResultItem(BaseValidatorModel):
    BackupResourceArn: Optional[str] = None
    SourceResourceArn: Optional[str] = None
    BackupVaultName: Optional[str] = None
    FileSystemIdentifier: Optional[str] = None
    FilePath: Optional[str] = None
    FileSize: Optional[int] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None


class ExportJobSummary(BaseValidatorModel):
    ExportJobIdentifier: str
    ExportJobArn: Optional[str] = None
    Status: Optional[ExportJobStatusType] = None
    CreationTime: Optional[datetime] = None
    CompletionTime: Optional[datetime] = None
    StatusMessage: Optional[str] = None
    SearchJobArn: Optional[str] = None


class S3ExportSpecification(BaseValidatorModel):
    DestinationBucket: str
    DestinationPrefix: Optional[str] = None


class GetSearchJobInput(BaseValidatorModel):
    SearchJobIdentifier: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class SearchScopeSummary(BaseValidatorModel):
    TotalRecoveryPointsToScanCount: Optional[int] = None
    TotalItemsToScanCount: Optional[int] = None


class GetSearchResultExportJobInput(BaseValidatorModel):
    ExportJobIdentifier: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListSearchJobBackupsInput(BaseValidatorModel):
    SearchJobIdentifier: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class SearchJobBackupsResult(BaseValidatorModel):
    Status: Optional[SearchJobStateType] = None
    StatusMessage: Optional[str] = None
    ResourceType: Optional[ResourceTypeType] = None
    BackupResourceArn: Optional[str] = None
    SourceResourceArn: Optional[str] = None
    IndexCreationTime: Optional[datetime] = None
    BackupCreationTime: Optional[datetime] = None


class ListSearchJobResultsInput(BaseValidatorModel):
    SearchJobIdentifier: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListSearchJobsInput(BaseValidatorModel):
    ByStatus: Optional[SearchJobStateType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListSearchResultExportJobsInput(BaseValidatorModel):
    Status: Optional[ExportJobStatusType] = None
    SearchJobIdentifier: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class S3ResultItem(BaseValidatorModel):
    BackupResourceArn: Optional[str] = None
    SourceResourceArn: Optional[str] = None
    BackupVaultName: Optional[str] = None
    ObjectKey: Optional[str] = None
    ObjectSize: Optional[int] = None
    CreationTime: Optional[datetime] = None
    ETag: Optional[str] = None
    VersionId: Optional[str] = None


class StopSearchJobInput(BaseValidatorModel):
    SearchJobIdentifier: str


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class SearchScopeOutput(BaseValidatorModel):
    BackupResourceTypes: List[ResourceTypeType]
    BackupResourceCreationTime: Optional[BackupCreationTimeFilterOutput] = None
    SourceResourceArns: Optional[List[str]] = None
    BackupResourceArns: Optional[List[str]] = None
    BackupResourceTags: Optional[Dict[str, str]] = None


class BackupCreationTimeFilter(BaseValidatorModel):
    CreatedAfter: Optional[Timestamp] = None
    CreatedBefore: Optional[Timestamp] = None


class TimeCondition(BaseValidatorModel):
    Value: Timestamp
    Operator: Optional[TimeConditionOperatorType] = None


class EBSItemFilterOutput(BaseValidatorModel):
    FilePaths: Optional[List[StringCondition]] = None
    Sizes: Optional[List[LongCondition]] = None
    CreationTimes: Optional[List[TimeConditionOutput]] = None
    LastModificationTimes: Optional[List[TimeConditionOutput]] = None


class S3ItemFilterOutput(BaseValidatorModel):
    ObjectKeys: Optional[List[StringCondition]] = None
    Sizes: Optional[List[LongCondition]] = None
    CreationTimes: Optional[List[TimeConditionOutput]] = None
    VersionIds: Optional[List[StringCondition]] = None
    ETags: Optional[List[StringCondition]] = None


class ExportSpecification(BaseValidatorModel):
    s3ExportSpecification: Optional[S3ExportSpecification] = None


class ListSearchResultExportJobsOutput(BaseValidatorModel):
    ExportJobs: List[ExportJobSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class StartSearchJobOutput(BaseValidatorModel):
    SearchJobArn: str
    CreationTime: datetime
    SearchJobIdentifier: str
    ResponseMetadata: ResponseMetadata


class StartSearchResultExportJobOutput(BaseValidatorModel):
    ExportJobArn: str
    ExportJobIdentifier: str
    ResponseMetadata: ResponseMetadata


class SearchJobSummary(BaseValidatorModel):
    SearchJobIdentifier: Optional[str] = None
    SearchJobArn: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[SearchJobStateType] = None
    CreationTime: Optional[datetime] = None
    CompletionTime: Optional[datetime] = None
    SearchScopeSummary: Optional[SearchScopeSummary] = None
    StatusMessage: Optional[str] = None


class ListSearchJobBackupsInputPaginate(BaseValidatorModel):
    SearchJobIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSearchJobResultsInputPaginate(BaseValidatorModel):
    SearchJobIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSearchJobsInputPaginate(BaseValidatorModel):
    ByStatus: Optional[SearchJobStateType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSearchResultExportJobsInputPaginate(BaseValidatorModel):
    Status: Optional[ExportJobStatusType] = None
    SearchJobIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSearchJobBackupsOutput(BaseValidatorModel):
    Results: List[SearchJobBackupsResult]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ResultItem(BaseValidatorModel):
    S3ResultItem: Optional[S3ResultItem] = None
    EBSResultItem: Optional[EBSResultItem] = None


class SearchScope(BaseValidatorModel):
    BackupResourceTypes: List[ResourceTypeType]
    BackupResourceCreationTime: Optional[BackupCreationTimeFilter] = None
    SourceResourceArns: Optional[List[str]] = None
    BackupResourceArns: Optional[List[str]] = None
    BackupResourceTags: Optional[Dict[str, str]] = None


class EBSItemFilter(BaseValidatorModel):
    FilePaths: Optional[List[StringCondition]] = None
    Sizes: Optional[List[LongCondition]] = None
    CreationTimes: Optional[List[TimeCondition]] = None
    LastModificationTimes: Optional[List[TimeCondition]] = None


class S3ItemFilter(BaseValidatorModel):
    ObjectKeys: Optional[List[StringCondition]] = None
    Sizes: Optional[List[LongCondition]] = None
    CreationTimes: Optional[List[TimeCondition]] = None
    VersionIds: Optional[List[StringCondition]] = None
    ETags: Optional[List[StringCondition]] = None


class ItemFiltersOutput(BaseValidatorModel):
    S3ItemFilters: Optional[List[S3ItemFilterOutput]] = None
    EBSItemFilters: Optional[List[EBSItemFilterOutput]] = None


class GetSearchResultExportJobOutput(BaseValidatorModel):
    ExportJobIdentifier: str
    ExportJobArn: str
    Status: ExportJobStatusType
    CreationTime: datetime
    CompletionTime: datetime
    StatusMessage: str
    ExportSpecification: ExportSpecification
    SearchJobArn: str
    ResponseMetadata: ResponseMetadata


class StartSearchResultExportJobInput(BaseValidatorModel):
    SearchJobIdentifier: str
    ExportSpecification: ExportSpecification
    ClientToken: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    RoleArn: Optional[str] = None


class ListSearchJobsOutput(BaseValidatorModel):
    SearchJobs: List[SearchJobSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListSearchJobResultsOutput(BaseValidatorModel):
    Results: List[ResultItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

SearchScopeUnion = Union[SearchScope, SearchScopeOutput]


class ItemFilters(BaseValidatorModel):
    S3ItemFilters: Optional[List[S3ItemFilter]] = None
    EBSItemFilters: Optional[List[EBSItemFilter]] = None


class GetSearchJobOutput(BaseValidatorModel):
    Name: str
    SearchScopeSummary: SearchScopeSummary
    CurrentSearchProgress: CurrentSearchProgress
    StatusMessage: str
    EncryptionKeyArn: str
    CompletionTime: datetime
    Status: SearchJobStateType
    SearchScope: SearchScopeOutput
    ItemFilters: ItemFiltersOutput
    CreationTime: datetime
    SearchJobIdentifier: str
    SearchJobArn: str
    ResponseMetadata: ResponseMetadata

ItemFiltersUnion = Union[ItemFilters, ItemFiltersOutput]


class StartSearchJobInput(BaseValidatorModel):
    SearchScope: SearchScopeUnion
    Tags: Optional[Dict[str, str]] = None
    Name: Optional[str] = None
    EncryptionKeyArn: Optional[str] = None
    ClientToken: Optional[str] = None
    ItemFilters: Optional[ItemFiltersUnion] = None
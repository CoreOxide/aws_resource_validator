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
from aws_resource_validator.pydantic_models.backupsearch_constants import *

class BackupCreationTimeFilterOutputTypeDef(BaseValidatorModel):
    CreatedAfter: Optional[datetime] = None
    CreatedBefore: Optional[datetime] = None


class CurrentSearchProgressTypeDef(BaseValidatorModel):
    RecoveryPointsScannedCount: Optional[int] = None
    ItemsScannedCount: Optional[int] = None
    ItemsMatchedCount: Optional[int] = None


class LongConditionTypeDef(BaseValidatorModel):
    Value: int
    Operator: Optional[LongConditionOperatorType] = None


class StringConditionTypeDef(BaseValidatorModel):
    Value: str
    Operator: Optional[StringConditionOperatorType] = None


class TimeConditionOutputTypeDef(BaseValidatorModel):
    Value: datetime
    Operator: Optional[TimeConditionOperatorType] = None


class EBSResultItemTypeDef(BaseValidatorModel):
    BackupResourceArn: Optional[str] = None
    SourceResourceArn: Optional[str] = None
    BackupVaultName: Optional[str] = None
    FileSystemIdentifier: Optional[str] = None
    FilePath: Optional[str] = None
    FileSize: Optional[int] = None
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None


class ExportJobSummaryTypeDef(BaseValidatorModel):
    ExportJobIdentifier: str
    ExportJobArn: Optional[str] = None
    Status: Optional[ExportJobStatusType] = None
    CreationTime: Optional[datetime] = None
    CompletionTime: Optional[datetime] = None
    StatusMessage: Optional[str] = None
    SearchJobArn: Optional[str] = None


class S3ExportSpecificationTypeDef(BaseValidatorModel):
    DestinationBucket: str
    DestinationPrefix: Optional[str] = None


class GetSearchJobInputTypeDef(BaseValidatorModel):
    SearchJobIdentifier: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class SearchScopeSummaryTypeDef(BaseValidatorModel):
    TotalRecoveryPointsToScanCount: Optional[int] = None
    TotalItemsToScanCount: Optional[int] = None


class GetSearchResultExportJobInputTypeDef(BaseValidatorModel):
    ExportJobIdentifier: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListSearchJobBackupsInputTypeDef(BaseValidatorModel):
    SearchJobIdentifier: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class SearchJobBackupsResultTypeDef(BaseValidatorModel):
    Status: Optional[SearchJobStateType] = None
    StatusMessage: Optional[str] = None
    ResourceType: Optional[ResourceTypeType] = None
    BackupResourceArn: Optional[str] = None
    SourceResourceArn: Optional[str] = None
    IndexCreationTime: Optional[datetime] = None
    BackupCreationTime: Optional[datetime] = None


class ListSearchJobResultsInputTypeDef(BaseValidatorModel):
    SearchJobIdentifier: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListSearchJobsInputTypeDef(BaseValidatorModel):
    ByStatus: Optional[SearchJobStateType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListSearchResultExportJobsInputTypeDef(BaseValidatorModel):
    Status: Optional[ExportJobStatusType] = None
    SearchJobIdentifier: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class S3ResultItemTypeDef(BaseValidatorModel):
    BackupResourceArn: Optional[str] = None
    SourceResourceArn: Optional[str] = None
    BackupVaultName: Optional[str] = None
    ObjectKey: Optional[str] = None
    ObjectSize: Optional[int] = None
    CreationTime: Optional[datetime] = None
    ETag: Optional[str] = None
    VersionId: Optional[str] = None


class StopSearchJobInputTypeDef(BaseValidatorModel):
    SearchJobIdentifier: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class SearchScopeOutputTypeDef(BaseValidatorModel):
    BackupResourceTypes: List[ResourceTypeType]
    BackupResourceCreationTime: Optional[BackupCreationTimeFilterOutputTypeDef] = None
    SourceResourceArns: Optional[List[str]] = None
    BackupResourceArns: Optional[List[str]] = None
    BackupResourceTags: Optional[Dict[str, str]] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class BackupCreationTimeFilterTypeDef(BaseValidatorModel):
    CreatedAfter: Optional[TimestampTypeDef] = None
    CreatedBefore: Optional[TimestampTypeDef] = None


class TimeConditionTypeDef(BaseValidatorModel):
    Value: TimestampTypeDef
    Operator: Optional[TimeConditionOperatorType] = None


class EBSItemFilterOutputTypeDef(BaseValidatorModel):
    FilePaths: Optional[List[StringConditionTypeDef]] = None
    Sizes: Optional[List[LongConditionTypeDef]] = None
    CreationTimes: Optional[List[TimeConditionOutputTypeDef]] = None
    LastModificationTimes: Optional[List[TimeConditionOutputTypeDef]] = None


class S3ItemFilterOutputTypeDef(BaseValidatorModel):
    ObjectKeys: Optional[List[StringConditionTypeDef]] = None
    Sizes: Optional[List[LongConditionTypeDef]] = None
    CreationTimes: Optional[List[TimeConditionOutputTypeDef]] = None
    VersionIds: Optional[List[StringConditionTypeDef]] = None
    ETags: Optional[List[StringConditionTypeDef]] = None


class ExportSpecificationTypeDef(BaseValidatorModel):
    s3ExportSpecification: Optional[S3ExportSpecificationTypeDef] = None


class ListSearchResultExportJobsOutputTypeDef(BaseValidatorModel):
    ExportJobs: List[ExportJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class StartSearchJobOutputTypeDef(BaseValidatorModel):
    SearchJobArn: str
    CreationTime: datetime
    SearchJobIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartSearchResultExportJobOutputTypeDef(BaseValidatorModel):
    ExportJobArn: str
    ExportJobIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef


class SearchJobSummaryTypeDef(BaseValidatorModel):
    SearchJobIdentifier: Optional[str] = None
    SearchJobArn: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[SearchJobStateType] = None
    CreationTime: Optional[datetime] = None
    CompletionTime: Optional[datetime] = None
    SearchScopeSummary: Optional[SearchScopeSummaryTypeDef] = None
    StatusMessage: Optional[str] = None


class ListSearchJobBackupsInputPaginateTypeDef(BaseValidatorModel):
    SearchJobIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSearchJobResultsInputPaginateTypeDef(BaseValidatorModel):
    SearchJobIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSearchJobsInputPaginateTypeDef(BaseValidatorModel):
    ByStatus: Optional[SearchJobStateType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSearchResultExportJobsInputPaginateTypeDef(BaseValidatorModel):
    Status: Optional[ExportJobStatusType] = None
    SearchJobIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSearchJobBackupsOutputTypeDef(BaseValidatorModel):
    Results: List[SearchJobBackupsResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ResultItemTypeDef(BaseValidatorModel):
    S3ResultItem: Optional[S3ResultItemTypeDef] = None
    EBSResultItem: Optional[EBSResultItemTypeDef] = None


class SearchScopeTypeDef(BaseValidatorModel):
    BackupResourceTypes: Sequence[ResourceTypeType]
    BackupResourceCreationTime: Optional[BackupCreationTimeFilterTypeDef] = None
    SourceResourceArns: Optional[Sequence[str]] = None
    BackupResourceArns: Optional[Sequence[str]] = None
    BackupResourceTags: Optional[Mapping[str, str]] = None


class EBSItemFilterTypeDef(BaseValidatorModel):
    FilePaths: Optional[Sequence[StringConditionTypeDef]] = None
    Sizes: Optional[Sequence[LongConditionTypeDef]] = None
    CreationTimes: Optional[Sequence[TimeConditionTypeDef]] = None
    LastModificationTimes: Optional[Sequence[TimeConditionTypeDef]] = None


class S3ItemFilterTypeDef(BaseValidatorModel):
    ObjectKeys: Optional[Sequence[StringConditionTypeDef]] = None
    Sizes: Optional[Sequence[LongConditionTypeDef]] = None
    CreationTimes: Optional[Sequence[TimeConditionTypeDef]] = None
    VersionIds: Optional[Sequence[StringConditionTypeDef]] = None
    ETags: Optional[Sequence[StringConditionTypeDef]] = None


class ItemFiltersOutputTypeDef(BaseValidatorModel):
    S3ItemFilters: Optional[List[S3ItemFilterOutputTypeDef]] = None
    EBSItemFilters: Optional[List[EBSItemFilterOutputTypeDef]] = None


class GetSearchResultExportJobOutputTypeDef(BaseValidatorModel):
    ExportJobIdentifier: str
    ExportJobArn: str
    Status: ExportJobStatusType
    CreationTime: datetime
    CompletionTime: datetime
    StatusMessage: str
    ExportSpecification: ExportSpecificationTypeDef
    SearchJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartSearchResultExportJobInputTypeDef(BaseValidatorModel):
    SearchJobIdentifier: str
    ExportSpecification: ExportSpecificationTypeDef
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    RoleArn: Optional[str] = None


class ListSearchJobsOutputTypeDef(BaseValidatorModel):
    SearchJobs: List[SearchJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListSearchJobResultsOutputTypeDef(BaseValidatorModel):
    Results: List[ResultItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ItemFiltersTypeDef(BaseValidatorModel):
    S3ItemFilters: Optional[Sequence[S3ItemFilterTypeDef]] = None
    EBSItemFilters: Optional[Sequence[EBSItemFilterTypeDef]] = None


class GetSearchJobOutputTypeDef(BaseValidatorModel):
    Name: str
    SearchScopeSummary: SearchScopeSummaryTypeDef
    CurrentSearchProgress: CurrentSearchProgressTypeDef
    StatusMessage: str
    EncryptionKeyArn: str
    CompletionTime: datetime
    Status: SearchJobStateType
    SearchScope: SearchScopeOutputTypeDef
    ItemFilters: ItemFiltersOutputTypeDef
    CreationTime: datetime
    SearchJobIdentifier: str
    SearchJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class ItemFiltersUnionTypeDef(BaseValidatorModel):
    pass


class SearchScopeUnionTypeDef(BaseValidatorModel):
    pass


class StartSearchJobInputTypeDef(BaseValidatorModel):
    SearchScope: SearchScopeUnionTypeDef
    Tags: Optional[Mapping[str, str]] = None
    Name: Optional[str] = None
    EncryptionKeyArn: Optional[str] = None
    ClientToken: Optional[str] = None
    ItemFilters: Optional[ItemFiltersUnionTypeDef] = None



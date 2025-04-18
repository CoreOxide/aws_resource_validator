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
from aws_resource_validator.pydantic_models.s3tables_constants import *

class CreateNamespaceRequest(BaseValidatorModel):
    tableBucketARN: str
    namespace: Sequence[str]


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateTableBucketRequest(BaseValidatorModel):
    name: str


class DeleteNamespaceRequest(BaseValidatorModel):
    tableBucketARN: str
    namespace: str


class DeleteTableBucketPolicyRequest(BaseValidatorModel):
    tableBucketARN: str


class DeleteTableBucketRequest(BaseValidatorModel):
    tableBucketARN: str


class DeleteTablePolicyRequest(BaseValidatorModel):
    tableBucketARN: str
    namespace: str
    name: str


class DeleteTableRequest(BaseValidatorModel):
    tableBucketARN: str
    namespace: str
    name: str
    versionToken: Optional[str] = None


class GetNamespaceRequest(BaseValidatorModel):
    tableBucketARN: str
    namespace: str


class GetTableBucketMaintenanceConfigurationRequest(BaseValidatorModel):
    tableBucketARN: str


class GetTableBucketPolicyRequest(BaseValidatorModel):
    tableBucketARN: str


class GetTableBucketRequest(BaseValidatorModel):
    tableBucketARN: str


class GetTableMaintenanceConfigurationRequest(BaseValidatorModel):
    tableBucketARN: str
    namespace: str
    name: str


class GetTableMaintenanceJobStatusRequest(BaseValidatorModel):
    tableBucketARN: str
    namespace: str
    name: str


class TableMaintenanceJobStatusValue(BaseValidatorModel):
    status: JobStatusType
    lastRunTimestamp: Optional[datetime] = None
    failureMessage: Optional[str] = None


class GetTableMetadataLocationRequest(BaseValidatorModel):
    tableBucketARN: str
    namespace: str
    name: str


class GetTablePolicyRequest(BaseValidatorModel):
    tableBucketARN: str
    namespace: str
    name: str


class GetTableRequest(BaseValidatorModel):
    tableBucketARN: str
    namespace: str
    name: str


class IcebergCompactionSettings(BaseValidatorModel):
    targetFileSizeMB: Optional[int] = None


class IcebergSnapshotManagementSettings(BaseValidatorModel):
    minSnapshotsToKeep: Optional[int] = None
    maxSnapshotAgeHours: Optional[int] = None


class IcebergUnreferencedFileRemovalSettings(BaseValidatorModel):
    unreferencedDays: Optional[int] = None
    nonCurrentDays: Optional[int] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListNamespacesRequest(BaseValidatorModel):
    tableBucketARN: str
    prefix: Optional[str] = None
    continuationToken: Optional[str] = None
    maxNamespaces: Optional[int] = None


class NamespaceSummary(BaseValidatorModel):
    namespace: List[str]
    createdAt: datetime
    createdBy: str
    ownerAccountId: str


class ListTableBucketsRequest(BaseValidatorModel):
    prefix: Optional[str] = None
    continuationToken: Optional[str] = None
    maxBuckets: Optional[int] = None


class TableBucketSummary(BaseValidatorModel):
    arn: str
    name: str
    ownerAccountId: str
    createdAt: datetime


class ListTablesRequest(BaseValidatorModel):
    tableBucketARN: str
    namespace: Optional[str] = None
    prefix: Optional[str] = None
    continuationToken: Optional[str] = None
    maxTables: Optional[int] = None


class PutTableBucketPolicyRequest(BaseValidatorModel):
    tableBucketARN: str
    resourcePolicy: str


class PutTablePolicyRequest(BaseValidatorModel):
    tableBucketARN: str
    namespace: str
    name: str
    resourcePolicy: str


class RenameTableRequest(BaseValidatorModel):
    tableBucketARN: str
    namespace: str
    name: str
    newNamespaceName: Optional[str] = None
    newName: Optional[str] = None
    versionToken: Optional[str] = None


class UpdateTableMetadataLocationRequest(BaseValidatorModel):
    tableBucketARN: str
    namespace: str
    name: str
    versionToken: str
    metadataLocation: str


class CreateNamespaceResponse(BaseValidatorModel):
    tableBucketARN: str
    namespace: List[str]
    ResponseMetadata: ResponseMetadata


class CreateTableBucketResponse(BaseValidatorModel):
    arn: str
    ResponseMetadata: ResponseMetadata


class CreateTableResponse(BaseValidatorModel):
    tableARN: str
    versionToken: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetNamespaceResponse(BaseValidatorModel):
    namespace: List[str]
    createdAt: datetime
    createdBy: str
    ownerAccountId: str
    ResponseMetadata: ResponseMetadata


class GetTableBucketPolicyResponse(BaseValidatorModel):
    resourcePolicy: str
    ResponseMetadata: ResponseMetadata


class GetTableBucketResponse(BaseValidatorModel):
    arn: str
    name: str
    ownerAccountId: str
    createdAt: datetime
    ResponseMetadata: ResponseMetadata


class GetTableMetadataLocationResponse(BaseValidatorModel):
    versionToken: str
    metadataLocation: str
    warehouseLocation: str
    ResponseMetadata: ResponseMetadata


class GetTablePolicyResponse(BaseValidatorModel):
    resourcePolicy: str
    ResponseMetadata: ResponseMetadata


class UpdateTableMetadataLocationResponse(BaseValidatorModel):
    name: str
    tableARN: str
    namespace: List[str]
    versionToken: str
    metadataLocation: str
    ResponseMetadata: ResponseMetadata


class GetTableMaintenanceJobStatusResponse(BaseValidatorModel):
    tableARN: str
    status: Dict[TableMaintenanceJobTypeType, TableMaintenanceJobStatusValue]
    ResponseMetadata: ResponseMetadata


class SchemaField(BaseValidatorModel):
    pass


class IcebergSchema(BaseValidatorModel):
    fields: Sequence[SchemaField]


class TableMaintenanceSettings(BaseValidatorModel):
    icebergCompaction: Optional[IcebergCompactionSettings] = None
    icebergSnapshotManagement: Optional[IcebergSnapshotManagementSettings] = None


class TableBucketMaintenanceSettings(BaseValidatorModel):
    icebergUnreferencedFileRemoval: Optional[IcebergUnreferencedFileRemovalSettings] = None


class ListNamespacesRequestPaginate(BaseValidatorModel):
    tableBucketARN: str
    prefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTableBucketsRequestPaginate(BaseValidatorModel):
    prefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTablesRequestPaginate(BaseValidatorModel):
    tableBucketARN: str
    namespace: Optional[str] = None
    prefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListNamespacesResponse(BaseValidatorModel):
    namespaces: List[NamespaceSummary]
    continuationToken: str
    ResponseMetadata: ResponseMetadata


class ListTableBucketsResponse(BaseValidatorModel):
    tableBuckets: List[TableBucketSummary]
    continuationToken: str
    ResponseMetadata: ResponseMetadata


class TableSummary(BaseValidatorModel):
    pass


class ListTablesResponse(BaseValidatorModel):
    tables: List[TableSummary]
    continuationToken: str
    ResponseMetadata: ResponseMetadata


class IcebergMetadata(BaseValidatorModel):
    schema: IcebergSchema


class TableMaintenanceConfigurationValue(BaseValidatorModel):
    status: Optional[MaintenanceStatusType] = None
    settings: Optional[TableMaintenanceSettings] = None


class TableBucketMaintenanceConfigurationValue(BaseValidatorModel):
    status: Optional[MaintenanceStatusType] = None
    settings: Optional[TableBucketMaintenanceSettings] = None


class TableMetadata(BaseValidatorModel):
    iceberg: Optional[IcebergMetadata] = None


class GetTableMaintenanceConfigurationResponse(BaseValidatorModel):
    tableARN: str
    configuration: Dict[TableMaintenanceTypeType, TableMaintenanceConfigurationValue]
    ResponseMetadata: ResponseMetadata


class GetTableBucketMaintenanceConfigurationResponse(BaseValidatorModel):
    tableBucketARN: str
    configuration: Dict[ Literal["icebergUnreferencedFileRemoval"], TableBucketMaintenanceConfigurationValue ]
    ResponseMetadata: ResponseMetadata



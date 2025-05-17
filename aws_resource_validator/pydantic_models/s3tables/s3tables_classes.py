from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.s3tables.s3tables_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




# This class is the input for the 'create_namespace' function.
class CreateNamespaceRequest(BaseValidatorModel):
    tableBucketARN: str
    namespace: List[str]


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'create_table_bucket' function.
class CreateTableBucketRequest(BaseValidatorModel):
    name: str


# This class is the input for the 'delete_namespace' function.
class DeleteNamespaceRequest(BaseValidatorModel):
    tableBucketARN: str
    namespace: str


# This class is the input for the 'delete_table_bucket_policy' function.
class DeleteTableBucketPolicyRequest(BaseValidatorModel):
    tableBucketARN: str


# This class is the input for the 'delete_table_bucket' function.
class DeleteTableBucketRequest(BaseValidatorModel):
    tableBucketARN: str


# This class is the input for the 'delete_table_policy' function.
class DeleteTablePolicyRequest(BaseValidatorModel):
    tableBucketARN: str
    namespace: str
    name: str


# This class is the input for the 'delete_table' function.
class DeleteTableRequest(BaseValidatorModel):
    tableBucketARN: str
    namespace: str
    name: str
    versionToken: Optional[str] = None


# This class is the input for the 'get_namespace' function.
class GetNamespaceRequest(BaseValidatorModel):
    tableBucketARN: str
    namespace: str


# This class is the input for the 'get_table_bucket_maintenance_configuration' function.
class GetTableBucketMaintenanceConfigurationRequest(BaseValidatorModel):
    tableBucketARN: str


# This class is the input for the 'get_table_bucket_policy' function.
class GetTableBucketPolicyRequest(BaseValidatorModel):
    tableBucketARN: str


# This class is the input for the 'get_table_bucket' function.
class GetTableBucketRequest(BaseValidatorModel):
    tableBucketARN: str


# This class is the input for the 'get_table_maintenance_configuration' function.
class GetTableMaintenanceConfigurationRequest(BaseValidatorModel):
    tableBucketARN: str
    namespace: str
    name: str


# This class is the input for the 'get_table_maintenance_job_status' function.
class GetTableMaintenanceJobStatusRequest(BaseValidatorModel):
    tableBucketARN: str
    namespace: str
    name: str


class TableMaintenanceJobStatusValue(BaseValidatorModel):
    status: JobStatusType
    lastRunTimestamp: Optional[datetime] = None
    failureMessage: Optional[str] = None


# This class is the input for the 'get_table_metadata_location' function.
class GetTableMetadataLocationRequest(BaseValidatorModel):
    tableBucketARN: str
    namespace: str
    name: str


# This class is the input for the 'get_table_policy' function.
class GetTablePolicyRequest(BaseValidatorModel):
    tableBucketARN: str
    namespace: str
    name: str


# This class is the input for the 'get_table' function.
class GetTableRequest(BaseValidatorModel):
    tableBucketARN: str
    namespace: str
    name: str


class IcebergCompactionSettings(BaseValidatorModel):
    targetFileSizeMB: Optional[int] = None


class SchemaField(BaseValidatorModel):
    name: str
    type: str
    required: Optional[bool] = None


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


# This class is the input for the 'list_namespaces' function.
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


# This class is the input for the 'list_table_buckets' function.
class ListTableBucketsRequest(BaseValidatorModel):
    prefix: Optional[str] = None
    continuationToken: Optional[str] = None
    maxBuckets: Optional[int] = None


class TableBucketSummary(BaseValidatorModel):
    arn: str
    name: str
    ownerAccountId: str
    createdAt: datetime


# This class is the input for the 'list_tables' function.
class ListTablesRequest(BaseValidatorModel):
    tableBucketARN: str
    namespace: Optional[str] = None
    prefix: Optional[str] = None
    continuationToken: Optional[str] = None
    maxTables: Optional[int] = None


class TableSummary(BaseValidatorModel):
    namespace: List[str]
    name: str
    type: TableTypeType
    tableARN: str
    createdAt: datetime
    modifiedAt: datetime


# This class is the input for the 'put_table_bucket_policy' function.
class PutTableBucketPolicyRequest(BaseValidatorModel):
    tableBucketARN: str
    resourcePolicy: str


# This class is the input for the 'put_table_policy' function.
class PutTablePolicyRequest(BaseValidatorModel):
    tableBucketARN: str
    namespace: str
    name: str
    resourcePolicy: str


# This class is the input for the 'rename_table' function.
class RenameTableRequest(BaseValidatorModel):
    tableBucketARN: str
    namespace: str
    name: str
    newNamespaceName: Optional[str] = None
    newName: Optional[str] = None
    versionToken: Optional[str] = None


# This class is the input for the 'update_table_metadata_location' function.
class UpdateTableMetadataLocationRequest(BaseValidatorModel):
    tableBucketARN: str
    namespace: str
    name: str
    versionToken: str
    metadataLocation: str


# This class is the output for the 'create_namespace' function.
class CreateNamespaceResponse(BaseValidatorModel):
    tableBucketARN: str
    namespace: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_table_bucket' function.
class CreateTableBucketResponse(BaseValidatorModel):
    arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_table' function.
class CreateTableResponse(BaseValidatorModel):
    tableARN: str
    versionToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'rename_table' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_namespace' function.
class GetNamespaceResponse(BaseValidatorModel):
    namespace: List[str]
    createdAt: datetime
    createdBy: str
    ownerAccountId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_table_bucket_policy' function.
class GetTableBucketPolicyResponse(BaseValidatorModel):
    resourcePolicy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_table_bucket' function.
class GetTableBucketResponse(BaseValidatorModel):
    arn: str
    name: str
    ownerAccountId: str
    createdAt: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_table_metadata_location' function.
class GetTableMetadataLocationResponse(BaseValidatorModel):
    versionToken: str
    metadataLocation: str
    warehouseLocation: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_table_policy' function.
class GetTablePolicyResponse(BaseValidatorModel):
    resourcePolicy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_table' function.
class GetTableResponse(BaseValidatorModel):
    name: str
    type: TableTypeType
    tableARN: str
    namespace: List[str]
    versionToken: str
    metadataLocation: str
    warehouseLocation: str
    createdAt: datetime
    createdBy: str
    managedByService: str
    modifiedAt: datetime
    modifiedBy: str
    ownerAccountId: str
    format: Literal['ICEBERG']
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_table_metadata_location' function.
class UpdateTableMetadataLocationResponse(BaseValidatorModel):
    name: str
    tableARN: str
    namespace: List[str]
    versionToken: str
    metadataLocation: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_table_maintenance_job_status' function.
class GetTableMaintenanceJobStatusResponse(BaseValidatorModel):
    tableARN: str
    status: Dict[TableMaintenanceJobTypeType, TableMaintenanceJobStatusValue]
    ResponseMetadata: ResponseMetadata


class IcebergSchema(BaseValidatorModel):
    fields: List[SchemaField]


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


# This class is the output for the 'list_namespaces' function.
class ListNamespacesResponse(BaseValidatorModel):
    namespaces: List[NamespaceSummary]
    continuationToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_table_buckets' function.
class ListTableBucketsResponse(BaseValidatorModel):
    tableBuckets: List[TableBucketSummary]
    continuationToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tables' function.
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


# This class is the output for the 'get_table_maintenance_configuration' function.
class GetTableMaintenanceConfigurationResponse(BaseValidatorModel):
    tableARN: str
    configuration: Dict[TableMaintenanceTypeType, TableMaintenanceConfigurationValue]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'put_table_maintenance_configuration' function.
class PutTableMaintenanceConfigurationRequest(BaseValidatorModel):
    tableBucketARN: str
    namespace: str
    name: str
    type: TableMaintenanceTypeType
    value: TableMaintenanceConfigurationValue


# This class is the output for the 'get_table_bucket_maintenance_configuration' function.
class GetTableBucketMaintenanceConfigurationResponse(BaseValidatorModel):
    tableBucketARN: str
    configuration: Dict[Literal['icebergUnreferencedFileRemoval'], TableBucketMaintenanceConfigurationValue]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'put_table_bucket_maintenance_configuration' function.
class PutTableBucketMaintenanceConfigurationRequest(BaseValidatorModel):
    tableBucketARN: str
    type: Literal['icebergUnreferencedFileRemoval']
    value: TableBucketMaintenanceConfigurationValue


# This class is the input for the 'create_table' function.
class CreateTableRequest(BaseValidatorModel):
    tableBucketARN: str
    namespace: str
    name: str
    format: Literal['ICEBERG']
    metadata: Optional[TableMetadata] = None
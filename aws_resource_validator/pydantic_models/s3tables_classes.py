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

class CreateNamespaceRequestTypeDef(BaseValidatorModel):
    tableBucketARN: str
    namespace: Sequence[str]


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateTableBucketRequestTypeDef(BaseValidatorModel):
    name: str


class DeleteNamespaceRequestTypeDef(BaseValidatorModel):
    tableBucketARN: str
    namespace: str


class DeleteTableBucketPolicyRequestTypeDef(BaseValidatorModel):
    tableBucketARN: str


class DeleteTableBucketRequestTypeDef(BaseValidatorModel):
    tableBucketARN: str


class DeleteTablePolicyRequestTypeDef(BaseValidatorModel):
    tableBucketARN: str
    namespace: str
    name: str


class DeleteTableRequestTypeDef(BaseValidatorModel):
    tableBucketARN: str
    namespace: str
    name: str
    versionToken: Optional[str] = None


class GetNamespaceRequestTypeDef(BaseValidatorModel):
    tableBucketARN: str
    namespace: str


class GetTableBucketMaintenanceConfigurationRequestTypeDef(BaseValidatorModel):
    tableBucketARN: str


class GetTableBucketPolicyRequestTypeDef(BaseValidatorModel):
    tableBucketARN: str


class GetTableBucketRequestTypeDef(BaseValidatorModel):
    tableBucketARN: str


class GetTableMaintenanceConfigurationRequestTypeDef(BaseValidatorModel):
    tableBucketARN: str
    namespace: str
    name: str


class GetTableMaintenanceJobStatusRequestTypeDef(BaseValidatorModel):
    tableBucketARN: str
    namespace: str
    name: str


class TableMaintenanceJobStatusValueTypeDef(BaseValidatorModel):
    status: JobStatusType
    lastRunTimestamp: Optional[datetime] = None
    failureMessage: Optional[str] = None


class GetTableMetadataLocationRequestTypeDef(BaseValidatorModel):
    tableBucketARN: str
    namespace: str
    name: str


class GetTablePolicyRequestTypeDef(BaseValidatorModel):
    tableBucketARN: str
    namespace: str
    name: str


class GetTableRequestTypeDef(BaseValidatorModel):
    tableBucketARN: str
    namespace: str
    name: str


class IcebergCompactionSettingsTypeDef(BaseValidatorModel):
    targetFileSizeMB: Optional[int] = None


class IcebergSnapshotManagementSettingsTypeDef(BaseValidatorModel):
    minSnapshotsToKeep: Optional[int] = None
    maxSnapshotAgeHours: Optional[int] = None


class IcebergUnreferencedFileRemovalSettingsTypeDef(BaseValidatorModel):
    unreferencedDays: Optional[int] = None
    nonCurrentDays: Optional[int] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListNamespacesRequestTypeDef(BaseValidatorModel):
    tableBucketARN: str
    prefix: Optional[str] = None
    continuationToken: Optional[str] = None
    maxNamespaces: Optional[int] = None


class NamespaceSummaryTypeDef(BaseValidatorModel):
    namespace: List[str]
    createdAt: datetime
    createdBy: str
    ownerAccountId: str


class ListTableBucketsRequestTypeDef(BaseValidatorModel):
    prefix: Optional[str] = None
    continuationToken: Optional[str] = None
    maxBuckets: Optional[int] = None


class TableBucketSummaryTypeDef(BaseValidatorModel):
    arn: str
    name: str
    ownerAccountId: str
    createdAt: datetime


class ListTablesRequestTypeDef(BaseValidatorModel):
    tableBucketARN: str
    namespace: Optional[str] = None
    prefix: Optional[str] = None
    continuationToken: Optional[str] = None
    maxTables: Optional[int] = None


class PutTableBucketPolicyRequestTypeDef(BaseValidatorModel):
    tableBucketARN: str
    resourcePolicy: str


class PutTablePolicyRequestTypeDef(BaseValidatorModel):
    tableBucketARN: str
    namespace: str
    name: str
    resourcePolicy: str


class RenameTableRequestTypeDef(BaseValidatorModel):
    tableBucketARN: str
    namespace: str
    name: str
    newNamespaceName: Optional[str] = None
    newName: Optional[str] = None
    versionToken: Optional[str] = None


class UpdateTableMetadataLocationRequestTypeDef(BaseValidatorModel):
    tableBucketARN: str
    namespace: str
    name: str
    versionToken: str
    metadataLocation: str


class CreateNamespaceResponseTypeDef(BaseValidatorModel):
    tableBucketARN: str
    namespace: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateTableBucketResponseTypeDef(BaseValidatorModel):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateTableResponseTypeDef(BaseValidatorModel):
    tableARN: str
    versionToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetNamespaceResponseTypeDef(BaseValidatorModel):
    namespace: List[str]
    createdAt: datetime
    createdBy: str
    ownerAccountId: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetTableBucketPolicyResponseTypeDef(BaseValidatorModel):
    resourcePolicy: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetTableBucketResponseTypeDef(BaseValidatorModel):
    arn: str
    name: str
    ownerAccountId: str
    createdAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class GetTableMetadataLocationResponseTypeDef(BaseValidatorModel):
    versionToken: str
    metadataLocation: str
    warehouseLocation: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetTablePolicyResponseTypeDef(BaseValidatorModel):
    resourcePolicy: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateTableMetadataLocationResponseTypeDef(BaseValidatorModel):
    name: str
    tableARN: str
    namespace: List[str]
    versionToken: str
    metadataLocation: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetTableMaintenanceJobStatusResponseTypeDef(BaseValidatorModel):
    tableARN: str
    status: Dict[TableMaintenanceJobTypeType, TableMaintenanceJobStatusValueTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class SchemaFieldTypeDef(BaseValidatorModel):
    pass


class IcebergSchemaTypeDef(BaseValidatorModel):
    fields: Sequence[SchemaFieldTypeDef]


class TableMaintenanceSettingsTypeDef(BaseValidatorModel):
    icebergCompaction: Optional[IcebergCompactionSettingsTypeDef] = None
    icebergSnapshotManagement: Optional[IcebergSnapshotManagementSettingsTypeDef] = None


class TableBucketMaintenanceSettingsTypeDef(BaseValidatorModel):
    icebergUnreferencedFileRemoval: Optional[IcebergUnreferencedFileRemovalSettingsTypeDef] = None


class ListNamespacesRequestPaginateTypeDef(BaseValidatorModel):
    tableBucketARN: str
    prefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTableBucketsRequestPaginateTypeDef(BaseValidatorModel):
    prefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTablesRequestPaginateTypeDef(BaseValidatorModel):
    tableBucketARN: str
    namespace: Optional[str] = None
    prefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListNamespacesResponseTypeDef(BaseValidatorModel):
    namespaces: List[NamespaceSummaryTypeDef]
    continuationToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTableBucketsResponseTypeDef(BaseValidatorModel):
    tableBuckets: List[TableBucketSummaryTypeDef]
    continuationToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class TableSummaryTypeDef(BaseValidatorModel):
    pass


class ListTablesResponseTypeDef(BaseValidatorModel):
    tables: List[TableSummaryTypeDef]
    continuationToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class IcebergMetadataTypeDef(BaseValidatorModel):
    schema: IcebergSchemaTypeDef


class TableMaintenanceConfigurationValueTypeDef(BaseValidatorModel):
    status: Optional[MaintenanceStatusType] = None
    settings: Optional[TableMaintenanceSettingsTypeDef] = None


class TableBucketMaintenanceConfigurationValueTypeDef(BaseValidatorModel):
    status: Optional[MaintenanceStatusType] = None
    settings: Optional[TableBucketMaintenanceSettingsTypeDef] = None


class TableMetadataTypeDef(BaseValidatorModel):
    iceberg: Optional[IcebergMetadataTypeDef] = None


class GetTableMaintenanceConfigurationResponseTypeDef(BaseValidatorModel):
    tableARN: str
    configuration: Dict[TableMaintenanceTypeType, TableMaintenanceConfigurationValueTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetTableBucketMaintenanceConfigurationResponseTypeDef(BaseValidatorModel):
    tableBucketARN: str
    configuration: Dict[ Literal["icebergUnreferencedFileRemoval"], TableBucketMaintenanceConfigurationValueTypeDef ]
    ResponseMetadata: ResponseMetadataTypeDef



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
from aws_resource_validator.pydantic_models.keyspaces_constants import *

class TargetTrackingScalingPolicyConfigurationTypeDef(BaseModel):
    targetValue: float
    disableScaleIn: Optional[bool] = None
    scaleInCooldown: Optional[int] = None
    scaleOutCooldown: Optional[int] = None

class CapacitySpecificationSummaryTypeDef(BaseModel):
    throughputMode: ThroughputModeType
    readCapacityUnits: Optional[int] = None
    writeCapacityUnits: Optional[int] = None
    lastUpdateToPayPerRequestTimestamp: Optional[datetime] = None

class CapacitySpecificationTypeDef(BaseModel):
    throughputMode: ThroughputModeType
    readCapacityUnits: Optional[int] = None
    writeCapacityUnits: Optional[int] = None

class ClientSideTimestampsTypeDef(BaseModel):
    status: Literal["ENABLED"]

class ClusteringKeyTypeDef(BaseModel):
    name: str
    orderBy: SortOrderType

class ColumnDefinitionTypeDef(BaseModel):
    name: str
    type: str

class CommentTypeDef(BaseModel):
    message: str

class ReplicationSpecificationTypeDef(BaseModel):
    replicationStrategy: rsType
    regionList: Optional[Sequence[str]] = None

class TagTypeDef(BaseModel):
    key: str
    value: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class EncryptionSpecificationTypeDef(BaseModel):
    type: EncryptionTypeType
    kmsKeyIdentifier: Optional[str] = None

class PointInTimeRecoveryTypeDef(BaseModel):
    status: PointInTimeRecoveryStatusType

class TimeToLiveTypeDef(BaseModel):
    status: Literal["ENABLED"]

class DeleteKeyspaceRequestRequestTypeDef(BaseModel):
    keyspaceName: str

class DeleteTableRequestRequestTypeDef(BaseModel):
    keyspaceName: str
    tableName: str

class GetKeyspaceRequestRequestTypeDef(BaseModel):
    keyspaceName: str

class GetTableAutoScalingSettingsRequestRequestTypeDef(BaseModel):
    keyspaceName: str
    tableName: str

class GetTableRequestRequestTypeDef(BaseModel):
    keyspaceName: str
    tableName: str

class PointInTimeRecoverySummaryTypeDef(BaseModel):
    status: PointInTimeRecoveryStatusType
    earliestRestorableTimestamp: Optional[datetime] = None

class KeyspaceSummaryTypeDef(BaseModel):
    keyspaceName: str
    resourceArn: str
    replicationStrategy: rsType
    replicationRegions: Optional[List[str]] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListKeyspacesRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListTablesRequestRequestTypeDef(BaseModel):
    keyspaceName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class TableSummaryTypeDef(BaseModel):
    keyspaceName: str
    tableName: str
    resourceArn: str

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class PartitionKeyTypeDef(BaseModel):
    name: str

class StaticColumnTypeDef(BaseModel):
    name: str

class AutoScalingPolicyTypeDef(BaseModel):
    targetTrackingScalingPolicyConfiguration: Optional[       TargetTrackingScalingPolicyConfigurationTypeDef     ] = None

class ReplicaSpecificationSummaryTypeDef(BaseModel):
    region: Optional[str] = None
    status: Optional[TableStatusType] = None
    capacitySpecification: Optional[CapacitySpecificationSummaryTypeDef] = None

class CreateKeyspaceRequestRequestTypeDef(BaseModel):
    keyspaceName: str
    tags: Optional[Sequence[TagTypeDef]] = None
    replicationSpecification: Optional[ReplicationSpecificationTypeDef] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class CreateKeyspaceResponseTypeDef(BaseModel):
    resourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTableResponseTypeDef(BaseModel):
    resourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetKeyspaceResponseTypeDef(BaseModel):
    keyspaceName: str
    resourceArn: str
    replicationStrategy: rsType
    replicationRegions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    nextToken: str
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreTableResponseTypeDef(BaseModel):
    restoredTableARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTableResponseTypeDef(BaseModel):
    resourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListKeyspacesResponseTypeDef(BaseModel):
    nextToken: str
    keyspaces: List[KeyspaceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListKeyspacesRequestListKeyspacesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTablesRequestListTablesPaginateTypeDef(BaseModel):
    keyspaceName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceRequestListTagsForResourcePaginateTypeDef(BaseModel):
    resourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTablesResponseTypeDef(BaseModel):
    nextToken: str
    tables: List[TableSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SchemaDefinitionTypeDef(BaseModel):
    allColumns: Sequence[ColumnDefinitionTypeDef]
    partitionKeys: Sequence[PartitionKeyTypeDef]
    clusteringKeys: Optional[Sequence[ClusteringKeyTypeDef]] = None
    staticColumns: Optional[Sequence[StaticColumnTypeDef]] = None

class AutoScalingSettingsTypeDef(BaseModel):
    autoScalingDisabled: Optional[bool] = None
    minimumUnits: Optional[int] = None
    maximumUnits: Optional[int] = None
    scalingPolicy: Optional[AutoScalingPolicyTypeDef] = None

class GetTableResponseTypeDef(BaseModel):
    keyspaceName: str
    tableName: str
    resourceArn: str
    creationTimestamp: datetime
    status: TableStatusType
    schemaDefinition: SchemaDefinitionTypeDef
    capacitySpecification: CapacitySpecificationSummaryTypeDef
    encryptionSpecification: EncryptionSpecificationTypeDef
    pointInTimeRecovery: PointInTimeRecoverySummaryTypeDef
    ttl: TimeToLiveTypeDef
    defaultTimeToLive: int
    comment: CommentTypeDef
    clientSideTimestamps: ClientSideTimestampsTypeDef
    replicaSpecifications: List[ReplicaSpecificationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AutoScalingSpecificationTypeDef(BaseModel):
    writeCapacityAutoScaling: Optional[AutoScalingSettingsTypeDef] = None
    readCapacityAutoScaling: Optional[AutoScalingSettingsTypeDef] = None

class ReplicaSpecificationTypeDef(BaseModel):
    region: str
    readCapacityUnits: Optional[int] = None
    readCapacityAutoScaling: Optional[AutoScalingSettingsTypeDef] = None

class ReplicaAutoScalingSpecificationTypeDef(BaseModel):
    region: Optional[str] = None
    autoScalingSpecification: Optional[AutoScalingSpecificationTypeDef] = None

class CreateTableRequestRequestTypeDef(BaseModel):
    keyspaceName: str
    tableName: str
    schemaDefinition: SchemaDefinitionTypeDef
    comment: Optional[CommentTypeDef] = None
    capacitySpecification: Optional[CapacitySpecificationTypeDef] = None
    encryptionSpecification: Optional[EncryptionSpecificationTypeDef] = None
    pointInTimeRecovery: Optional[PointInTimeRecoveryTypeDef] = None
    ttl: Optional[TimeToLiveTypeDef] = None
    defaultTimeToLive: Optional[int] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    clientSideTimestamps: Optional[ClientSideTimestampsTypeDef] = None
    autoScalingSpecification: Optional[AutoScalingSpecificationTypeDef] = None
    replicaSpecifications: Optional[Sequence[ReplicaSpecificationTypeDef]] = None

class RestoreTableRequestRequestTypeDef(BaseModel):
    sourceKeyspaceName: str
    sourceTableName: str
    targetKeyspaceName: str
    targetTableName: str
    restoreTimestamp: Optional[TimestampTypeDef] = None
    capacitySpecificationOverride: Optional[CapacitySpecificationTypeDef] = None
    encryptionSpecificationOverride: Optional[EncryptionSpecificationTypeDef] = None
    pointInTimeRecoveryOverride: Optional[PointInTimeRecoveryTypeDef] = None
    tagsOverride: Optional[Sequence[TagTypeDef]] = None
    autoScalingSpecification: Optional[AutoScalingSpecificationTypeDef] = None
    replicaSpecifications: Optional[Sequence[ReplicaSpecificationTypeDef]] = None

class UpdateTableRequestRequestTypeDef(BaseModel):
    keyspaceName: str
    tableName: str
    addColumns: Optional[Sequence[ColumnDefinitionTypeDef]] = None
    capacitySpecification: Optional[CapacitySpecificationTypeDef] = None
    encryptionSpecification: Optional[EncryptionSpecificationTypeDef] = None
    pointInTimeRecovery: Optional[PointInTimeRecoveryTypeDef] = None
    ttl: Optional[TimeToLiveTypeDef] = None
    defaultTimeToLive: Optional[int] = None
    clientSideTimestamps: Optional[ClientSideTimestampsTypeDef] = None
    autoScalingSpecification: Optional[AutoScalingSpecificationTypeDef] = None
    replicaSpecifications: Optional[Sequence[ReplicaSpecificationTypeDef]] = None

class GetTableAutoScalingSettingsResponseTypeDef(BaseModel):
    keyspaceName: str
    tableName: str
    resourceArn: str
    autoScalingSpecification: AutoScalingSpecificationTypeDef
    replicaSpecifications: List[ReplicaAutoScalingSpecificationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


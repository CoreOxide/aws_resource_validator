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
from aws_resource_validator.pydantic_models.keyspaces_constants import *

class TargetTrackingScalingPolicyConfigurationTypeDef(BaseValidatorModel):
    targetValue: float
    disableScaleIn: Optional[bool] = None
    scaleInCooldown: Optional[int] = None
    scaleOutCooldown: Optional[int] = None


class CapacitySpecificationSummaryTypeDef(BaseValidatorModel):
    throughputMode: ThroughputModeType
    readCapacityUnits: Optional[int] = None
    writeCapacityUnits: Optional[int] = None
    lastUpdateToPayPerRequestTimestamp: Optional[datetime] = None


class CapacitySpecificationTypeDef(BaseValidatorModel):
    throughputMode: ThroughputModeType
    readCapacityUnits: Optional[int] = None
    writeCapacityUnits: Optional[int] = None


class ClientSideTimestampsTypeDef(BaseValidatorModel):
    status: Literal["ENABLED"]


class ClusteringKeyTypeDef(BaseValidatorModel):
    name: str
    orderBy: SortOrderType


class CommentTypeDef(BaseValidatorModel):
    message: str


class ReplicationSpecificationTypeDef(BaseValidatorModel):
    replicationStrategy: RsType
    regionList: Optional[Sequence[str]] = None


class TagTypeDef(BaseValidatorModel):
    key: str
    value: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class PointInTimeRecoveryTypeDef(BaseValidatorModel):
    status: PointInTimeRecoveryStatusType


class TimeToLiveTypeDef(BaseValidatorModel):
    status: Literal["ENABLED"]


class DeleteKeyspaceRequestTypeDef(BaseValidatorModel):
    keyspaceName: str


class DeleteTableRequestTypeDef(BaseValidatorModel):
    keyspaceName: str
    tableName: str


class DeleteTypeRequestTypeDef(BaseValidatorModel):
    keyspaceName: str
    typeName: str


class GetKeyspaceRequestTypeDef(BaseValidatorModel):
    keyspaceName: str


class ReplicationGroupStatusTypeDef(BaseValidatorModel):
    region: str
    keyspaceStatus: KeyspaceStatusType
    tablesReplicationProgress: Optional[str] = None


class GetTableAutoScalingSettingsRequestTypeDef(BaseValidatorModel):
    keyspaceName: str
    tableName: str


class GetTableRequestTypeDef(BaseValidatorModel):
    keyspaceName: str
    tableName: str


class PointInTimeRecoverySummaryTypeDef(BaseValidatorModel):
    status: PointInTimeRecoveryStatusType
    earliestRestorableTimestamp: Optional[datetime] = None


class GetTypeRequestTypeDef(BaseValidatorModel):
    keyspaceName: str
    typeName: str


class KeyspaceSummaryTypeDef(BaseValidatorModel):
    keyspaceName: str
    resourceArn: str
    replicationStrategy: RsType
    replicationRegions: Optional[List[str]] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListKeyspacesRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTablesRequestTypeDef(BaseValidatorModel):
    keyspaceName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class TableSummaryTypeDef(BaseValidatorModel):
    keyspaceName: str
    tableName: str
    resourceArn: str


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTypesRequestTypeDef(BaseValidatorModel):
    keyspaceName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class PartitionKeyTypeDef(BaseValidatorModel):
    name: str


class StaticColumnTypeDef(BaseValidatorModel):
    name: str


class AutoScalingPolicyTypeDef(BaseValidatorModel):
    targetTrackingScalingPolicyConfiguration: Optional[ TargetTrackingScalingPolicyConfigurationTypeDef ] = None


class ReplicaSpecificationSummaryTypeDef(BaseValidatorModel):
    region: Optional[str] = None
    status: Optional[TableStatusType] = None
    capacitySpecification: Optional[CapacitySpecificationSummaryTypeDef] = None


class UpdateKeyspaceRequestTypeDef(BaseValidatorModel):
    keyspaceName: str
    replicationSpecification: ReplicationSpecificationTypeDef
    clientSideTimestamps: Optional[ClientSideTimestampsTypeDef] = None


class CreateKeyspaceRequestTypeDef(BaseValidatorModel):
    keyspaceName: str
    tags: Optional[Sequence[TagTypeDef]] = None
    replicationSpecification: Optional[ReplicationSpecificationTypeDef] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]


class CreateKeyspaceResponseTypeDef(BaseValidatorModel):
    resourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateTableResponseTypeDef(BaseValidatorModel):
    resourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateTypeResponseTypeDef(BaseValidatorModel):
    keyspaceArn: str
    typeName: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteTypeResponseTypeDef(BaseValidatorModel):
    keyspaceArn: str
    typeName: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class RestoreTableResponseTypeDef(BaseValidatorModel):
    restoredTableARN: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateKeyspaceResponseTypeDef(BaseValidatorModel):
    resourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateTableResponseTypeDef(BaseValidatorModel):
    resourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class FieldDefinitionTypeDef(BaseValidatorModel):
    pass


class CreateTypeRequestTypeDef(BaseValidatorModel):
    keyspaceName: str
    typeName: str
    fieldDefinitions: Sequence[FieldDefinitionTypeDef]


class GetTypeResponseTypeDef(BaseValidatorModel):
    keyspaceName: str
    typeName: str
    fieldDefinitions: List[FieldDefinitionTypeDef]
    lastModifiedTimestamp: datetime
    status: TypeStatusType
    directReferringTables: List[str]
    directParentTypes: List[str]
    maxNestingDepth: int
    keyspaceArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetKeyspaceResponseTypeDef(BaseValidatorModel):
    keyspaceName: str
    resourceArn: str
    replicationStrategy: RsType
    replicationRegions: List[str]
    replicationGroupStatuses: List[ReplicationGroupStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListKeyspacesResponseTypeDef(BaseValidatorModel):
    keyspaces: List[KeyspaceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListKeyspacesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTablesRequestPaginateTypeDef(BaseValidatorModel):
    keyspaceName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTagsForResourceRequestPaginateTypeDef(BaseValidatorModel):
    resourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTypesRequestPaginateTypeDef(BaseValidatorModel):
    keyspaceName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTablesResponseTypeDef(BaseValidatorModel):
    tables: List[TableSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ColumnDefinitionTypeDef(BaseValidatorModel):
    pass


class SchemaDefinitionOutputTypeDef(BaseValidatorModel):
    allColumns: List[ColumnDefinitionTypeDef]
    partitionKeys: List[PartitionKeyTypeDef]
    clusteringKeys: Optional[List[ClusteringKeyTypeDef]] = None
    staticColumns: Optional[List[StaticColumnTypeDef]] = None


class SchemaDefinitionTypeDef(BaseValidatorModel):
    allColumns: Sequence[ColumnDefinitionTypeDef]
    partitionKeys: Sequence[PartitionKeyTypeDef]
    clusteringKeys: Optional[Sequence[ClusteringKeyTypeDef]] = None
    staticColumns: Optional[Sequence[StaticColumnTypeDef]] = None


class AutoScalingSettingsTypeDef(BaseValidatorModel):
    autoScalingDisabled: Optional[bool] = None
    minimumUnits: Optional[int] = None
    maximumUnits: Optional[int] = None
    scalingPolicy: Optional[AutoScalingPolicyTypeDef] = None


class EncryptionSpecificationTypeDef(BaseValidatorModel):
    pass


class GetTableResponseTypeDef(BaseValidatorModel):
    keyspaceName: str
    tableName: str
    resourceArn: str
    creationTimestamp: datetime
    status: TableStatusType
    schemaDefinition: SchemaDefinitionOutputTypeDef
    capacitySpecification: CapacitySpecificationSummaryTypeDef
    encryptionSpecification: EncryptionSpecificationTypeDef
    pointInTimeRecovery: PointInTimeRecoverySummaryTypeDef
    ttl: TimeToLiveTypeDef
    defaultTimeToLive: int
    comment: CommentTypeDef
    clientSideTimestamps: ClientSideTimestampsTypeDef
    replicaSpecifications: List[ReplicaSpecificationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class AutoScalingSpecificationTypeDef(BaseValidatorModel):
    writeCapacityAutoScaling: Optional[AutoScalingSettingsTypeDef] = None
    readCapacityAutoScaling: Optional[AutoScalingSettingsTypeDef] = None


class ReplicaSpecificationTypeDef(BaseValidatorModel):
    region: str
    readCapacityUnits: Optional[int] = None
    readCapacityAutoScaling: Optional[AutoScalingSettingsTypeDef] = None


class ReplicaAutoScalingSpecificationTypeDef(BaseValidatorModel):
    region: Optional[str] = None
    autoScalingSpecification: Optional[AutoScalingSpecificationTypeDef] = None


class SchemaDefinitionUnionTypeDef(BaseValidatorModel):
    pass


class CreateTableRequestTypeDef(BaseValidatorModel):
    keyspaceName: str
    tableName: str
    schemaDefinition: SchemaDefinitionUnionTypeDef
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


class TimestampTypeDef(BaseValidatorModel):
    pass


class RestoreTableRequestTypeDef(BaseValidatorModel):
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


class UpdateTableRequestTypeDef(BaseValidatorModel):
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


class GetTableAutoScalingSettingsResponseTypeDef(BaseValidatorModel):
    keyspaceName: str
    tableName: str
    resourceArn: str
    autoScalingSpecification: AutoScalingSpecificationTypeDef
    replicaSpecifications: List[ReplicaAutoScalingSpecificationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef



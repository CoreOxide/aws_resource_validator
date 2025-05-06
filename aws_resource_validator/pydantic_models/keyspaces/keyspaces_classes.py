from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.keyspaces.keyspaces_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class TargetTrackingScalingPolicyConfiguration(BaseValidatorModel):
    targetValue: float
    disableScaleIn: Optional[bool] = None
    scaleInCooldown: Optional[int] = None
    scaleOutCooldown: Optional[int] = None


class CapacitySpecificationSummary(BaseValidatorModel):
    throughputMode: ThroughputModeType
    readCapacityUnits: Optional[int] = None
    writeCapacityUnits: Optional[int] = None
    lastUpdateToPayPerRequestTimestamp: Optional[datetime] = None


class CapacitySpecification(BaseValidatorModel):
    throughputMode: ThroughputModeType
    readCapacityUnits: Optional[int] = None
    writeCapacityUnits: Optional[int] = None


class ClientSideTimestamps(BaseValidatorModel):
    status: Literal['ENABLED']


class ClusteringKey(BaseValidatorModel):
    name: str
    orderBy: SortOrderType


class ColumnDefinition(BaseValidatorModel):
    name: str
    type: str


class Comment(BaseValidatorModel):
    message: str


class ReplicationSpecification(BaseValidatorModel):
    replicationStrategy: RsType
    regionList: Optional[List[str]] = None


class Tag(BaseValidatorModel):
    key: str
    value: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class EncryptionSpecification(BaseValidatorModel):
    type: EncryptionTypeType
    kmsKeyIdentifier: Optional[str] = None


class PointInTimeRecovery(BaseValidatorModel):
    status: PointInTimeRecoveryStatusType


class TimeToLive(BaseValidatorModel):
    status: Literal['ENABLED']


class FieldDefinition(BaseValidatorModel):
    name: str
    type: str


class DeleteKeyspaceRequest(BaseValidatorModel):
    keyspaceName: str


class DeleteTableRequest(BaseValidatorModel):
    keyspaceName: str
    tableName: str


class DeleteTypeRequest(BaseValidatorModel):
    keyspaceName: str
    typeName: str


class GetKeyspaceRequest(BaseValidatorModel):
    keyspaceName: str


class ReplicationGroupStatus(BaseValidatorModel):
    region: str
    keyspaceStatus: KeyspaceStatusType
    tablesReplicationProgress: Optional[str] = None


class GetTableAutoScalingSettingsRequest(BaseValidatorModel):
    keyspaceName: str
    tableName: str


class GetTableRequest(BaseValidatorModel):
    keyspaceName: str
    tableName: str


class PointInTimeRecoverySummary(BaseValidatorModel):
    status: PointInTimeRecoveryStatusType
    earliestRestorableTimestamp: Optional[datetime] = None


class GetTypeRequest(BaseValidatorModel):
    keyspaceName: str
    typeName: str


class KeyspaceSummary(BaseValidatorModel):
    keyspaceName: str
    resourceArn: str
    replicationStrategy: RsType
    replicationRegions: Optional[List[str]] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListKeyspacesRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTablesRequest(BaseValidatorModel):
    keyspaceName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class TableSummary(BaseValidatorModel):
    keyspaceName: str
    tableName: str
    resourceArn: str


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTypesRequest(BaseValidatorModel):
    keyspaceName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class PartitionKey(BaseValidatorModel):
    name: str

Timestamp = Union[datetime, str]


class StaticColumn(BaseValidatorModel):
    name: str


class AutoScalingPolicy(BaseValidatorModel):
    targetTrackingScalingPolicyConfiguration: Optional[TargetTrackingScalingPolicyConfiguration] = None


class ReplicaSpecificationSummary(BaseValidatorModel):
    region: Optional[str] = None
    status: Optional[TableStatusType] = None
    capacitySpecification: Optional[CapacitySpecificationSummary] = None


class UpdateKeyspaceRequest(BaseValidatorModel):
    keyspaceName: str
    replicationSpecification: ReplicationSpecification
    clientSideTimestamps: Optional[ClientSideTimestamps] = None


class CreateKeyspaceRequest(BaseValidatorModel):
    keyspaceName: str
    tags: Optional[List[Tag]] = None
    replicationSpecification: Optional[ReplicationSpecification] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: List[Tag]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: List[Tag]


class CreateKeyspaceResponse(BaseValidatorModel):
    resourceArn: str
    ResponseMetadata: ResponseMetadata


class CreateTableResponse(BaseValidatorModel):
    resourceArn: str
    ResponseMetadata: ResponseMetadata


class CreateTypeResponse(BaseValidatorModel):
    keyspaceArn: str
    typeName: str
    ResponseMetadata: ResponseMetadata


class DeleteTypeResponse(BaseValidatorModel):
    keyspaceArn: str
    typeName: str
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTypesResponse(BaseValidatorModel):
    types: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class RestoreTableResponse(BaseValidatorModel):
    restoredTableARN: str
    ResponseMetadata: ResponseMetadata


class UpdateKeyspaceResponse(BaseValidatorModel):
    resourceArn: str
    ResponseMetadata: ResponseMetadata


class UpdateTableResponse(BaseValidatorModel):
    resourceArn: str
    ResponseMetadata: ResponseMetadata


class CreateTypeRequest(BaseValidatorModel):
    keyspaceName: str
    typeName: str
    fieldDefinitions: List[FieldDefinition]


class GetTypeResponse(BaseValidatorModel):
    keyspaceName: str
    typeName: str
    fieldDefinitions: List[FieldDefinition]
    lastModifiedTimestamp: datetime
    status: TypeStatusType
    directReferringTables: List[str]
    directParentTypes: List[str]
    maxNestingDepth: int
    keyspaceArn: str
    ResponseMetadata: ResponseMetadata


class GetKeyspaceResponse(BaseValidatorModel):
    keyspaceName: str
    resourceArn: str
    replicationStrategy: RsType
    replicationRegions: List[str]
    replicationGroupStatuses: List[ReplicationGroupStatus]
    ResponseMetadata: ResponseMetadata


class ListKeyspacesResponse(BaseValidatorModel):
    keyspaces: List[KeyspaceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListKeyspacesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTablesRequestPaginate(BaseValidatorModel):
    keyspaceName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTagsForResourceRequestPaginate(BaseValidatorModel):
    resourceArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTypesRequestPaginate(BaseValidatorModel):
    keyspaceName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTablesResponse(BaseValidatorModel):
    tables: List[TableSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SchemaDefinitionOutput(BaseValidatorModel):
    allColumns: List[ColumnDefinition]
    partitionKeys: List[PartitionKey]
    clusteringKeys: Optional[List[ClusteringKey]] = None
    staticColumns: Optional[List[StaticColumn]] = None


class SchemaDefinition(BaseValidatorModel):
    allColumns: List[ColumnDefinition]
    partitionKeys: List[PartitionKey]
    clusteringKeys: Optional[List[ClusteringKey]] = None
    staticColumns: Optional[List[StaticColumn]] = None


class AutoScalingSettings(BaseValidatorModel):
    autoScalingDisabled: Optional[bool] = None
    minimumUnits: Optional[int] = None
    maximumUnits: Optional[int] = None
    scalingPolicy: Optional[AutoScalingPolicy] = None


class GetTableResponse(BaseValidatorModel):
    keyspaceName: str
    tableName: str
    resourceArn: str
    creationTimestamp: datetime
    status: TableStatusType
    schemaDefinition: SchemaDefinitionOutput
    capacitySpecification: CapacitySpecificationSummary
    encryptionSpecification: EncryptionSpecification
    pointInTimeRecovery: PointInTimeRecoverySummary
    ttl: TimeToLive
    defaultTimeToLive: int
    comment: Comment
    clientSideTimestamps: ClientSideTimestamps
    replicaSpecifications: List[ReplicaSpecificationSummary]
    ResponseMetadata: ResponseMetadata

SchemaDefinitionUnion = Union[SchemaDefinition, SchemaDefinitionOutput]


class AutoScalingSpecification(BaseValidatorModel):
    writeCapacityAutoScaling: Optional[AutoScalingSettings] = None
    readCapacityAutoScaling: Optional[AutoScalingSettings] = None


class ReplicaSpecification(BaseValidatorModel):
    region: str
    readCapacityUnits: Optional[int] = None
    readCapacityAutoScaling: Optional[AutoScalingSettings] = None


class ReplicaAutoScalingSpecification(BaseValidatorModel):
    region: Optional[str] = None
    autoScalingSpecification: Optional[AutoScalingSpecification] = None


class CreateTableRequest(BaseValidatorModel):
    keyspaceName: str
    tableName: str
    schemaDefinition: SchemaDefinitionUnion
    comment: Optional[Comment] = None
    capacitySpecification: Optional[CapacitySpecification] = None
    encryptionSpecification: Optional[EncryptionSpecification] = None
    pointInTimeRecovery: Optional[PointInTimeRecovery] = None
    ttl: Optional[TimeToLive] = None
    defaultTimeToLive: Optional[int] = None
    tags: Optional[List[Tag]] = None
    clientSideTimestamps: Optional[ClientSideTimestamps] = None
    autoScalingSpecification: Optional[AutoScalingSpecification] = None
    replicaSpecifications: Optional[List[ReplicaSpecification]] = None


class RestoreTableRequest(BaseValidatorModel):
    sourceKeyspaceName: str
    sourceTableName: str
    targetKeyspaceName: str
    targetTableName: str
    restoreTimestamp: Optional[Timestamp] = None
    capacitySpecificationOverride: Optional[CapacitySpecification] = None
    encryptionSpecificationOverride: Optional[EncryptionSpecification] = None
    pointInTimeRecoveryOverride: Optional[PointInTimeRecovery] = None
    tagsOverride: Optional[List[Tag]] = None
    autoScalingSpecification: Optional[AutoScalingSpecification] = None
    replicaSpecifications: Optional[List[ReplicaSpecification]] = None


class UpdateTableRequest(BaseValidatorModel):
    keyspaceName: str
    tableName: str
    addColumns: Optional[List[ColumnDefinition]] = None
    capacitySpecification: Optional[CapacitySpecification] = None
    encryptionSpecification: Optional[EncryptionSpecification] = None
    pointInTimeRecovery: Optional[PointInTimeRecovery] = None
    ttl: Optional[TimeToLive] = None
    defaultTimeToLive: Optional[int] = None
    clientSideTimestamps: Optional[ClientSideTimestamps] = None
    autoScalingSpecification: Optional[AutoScalingSpecification] = None
    replicaSpecifications: Optional[List[ReplicaSpecification]] = None


class GetTableAutoScalingSettingsResponse(BaseValidatorModel):
    keyspaceName: str
    tableName: str
    resourceArn: str
    autoScalingSpecification: AutoScalingSpecification
    replicaSpecifications: List[ReplicaAutoScalingSpecification]
    ResponseMetadata: ResponseMetadata
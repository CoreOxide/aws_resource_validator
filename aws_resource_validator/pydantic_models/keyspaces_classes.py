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

class ColumnDefinitionTypeDef(BaseValidatorModel):
    name: str
    type: str

class CommentTypeDef(BaseValidatorModel):
    message: str

class ReplicationSpecificationTypeDef(BaseValidatorModel):
    replicationStrategy: rsType
    regionList: Optional[Sequence[str]] = None

class TagTypeDef(BaseValidatorModel):
    key: str
    value: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class EncryptionSpecificationTypeDef(BaseValidatorModel):
    type: EncryptionTypeType
    kmsKeyIdentifier: Optional[str] = None

class PointInTimeRecoveryTypeDef(BaseValidatorModel):
    status: PointInTimeRecoveryStatusType

class TimeToLiveTypeDef(BaseValidatorModel):
    status: Literal["ENABLED"]

class DeleteKeyspaceRequestRequestTypeDef(BaseValidatorModel):
    keyspaceName: str

class DeleteTableRequestRequestTypeDef(BaseValidatorModel):
    keyspaceName: str
    tableName: str

class GetKeyspaceRequestRequestTypeDef(BaseValidatorModel):
    keyspaceName: str

class GetTableAutoScalingSettingsRequestRequestTypeDef(BaseValidatorModel):
    keyspaceName: str
    tableName: str

class GetTableRequestRequestTypeDef(BaseValidatorModel):
    keyspaceName: str
    tableName: str

class PointInTimeRecoverySummaryTypeDef(BaseValidatorModel):
    status: PointInTimeRecoveryStatusType
    earliestRestorableTimestamp: Optional[datetime] = None

class KeyspaceSummaryTypeDef(BaseValidatorModel):
    keyspaceName: str
    resourceArn: str
    replicationStrategy: rsType
    replicationRegions: Optional[List[str]] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListKeyspacesRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListTablesRequestRequestTypeDef(BaseValidatorModel):
    keyspaceName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class TableSummaryTypeDef(BaseValidatorModel):
    keyspaceName: str
    tableName: str
    resourceArn: str

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class PartitionKeyTypeDef(BaseValidatorModel):
    name: str

class StaticColumnTypeDef(BaseValidatorModel):
    name: str

class AutoScalingPolicyTypeDef(BaseValidatorModel):
    targetTrackingScalingPolicyConfiguration: Optional[       TargetTrackingScalingPolicyConfigurationTypeDef     ] = None

class ReplicaSpecificationSummaryTypeDef(BaseValidatorModel):
    region: Optional[str] = None
    status: Optional[TableStatusType] = None
    capacitySpecification: Optional[CapacitySpecificationSummaryTypeDef] = None

class CreateKeyspaceRequestRequestTypeDef(BaseValidatorModel):
    keyspaceName: str
    tags: Optional[Sequence[TagTypeDef]] = None
    replicationSpecification: Optional[ReplicationSpecificationTypeDef] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class CreateKeyspaceResponseTypeDef(BaseValidatorModel):
    resourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTableResponseTypeDef(BaseValidatorModel):
    resourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetKeyspaceResponseTypeDef(BaseValidatorModel):
    keyspaceName: str
    resourceArn: str
    replicationStrategy: rsType
    replicationRegions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    nextToken: str
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreTableResponseTypeDef(BaseValidatorModel):
    restoredTableARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTableResponseTypeDef(BaseValidatorModel):
    resourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListKeyspacesResponseTypeDef(BaseValidatorModel):
    nextToken: str
    keyspaces: List[KeyspaceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListKeyspacesRequestListKeyspacesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTablesRequestListTablesPaginateTypeDef(BaseValidatorModel):
    keyspaceName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceRequestListTagsForResourcePaginateTypeDef(BaseValidatorModel):
    resourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTablesResponseTypeDef(BaseValidatorModel):
    nextToken: str
    tables: List[TableSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

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

class GetTableResponseTypeDef(BaseValidatorModel):
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

class CreateTableRequestRequestTypeDef(BaseValidatorModel):
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

class RestoreTableRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateTableRequestRequestTypeDef(BaseValidatorModel):
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


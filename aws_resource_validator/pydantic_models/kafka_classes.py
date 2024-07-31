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
from aws_resource_validator.pydantic_models.kafka_constants import *

class AmazonMskClusterTypeDef(BaseModel):
    MskClusterArn: str

class BatchAssociateScramSecretRequestRequestTypeDef(BaseModel):
    ClusterArn: str
    SecretArnList: Sequence[str]

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class UnprocessedScramSecretTypeDef(BaseModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None
    SecretArn: Optional[str] = None

class BatchDisassociateScramSecretRequestRequestTypeDef(BaseModel):
    ClusterArn: str
    SecretArnList: Sequence[str]

class BrokerCountUpdateInfoTypeDef(BaseModel):
    CreatedBrokerIds: Optional[List[float]] = None
    DeletedBrokerIds: Optional[List[float]] = None

class ProvisionedThroughputTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    VolumeThroughput: Optional[int] = None

class CloudWatchLogsTypeDef(BaseModel):
    Enabled: bool
    LogGroup: Optional[str] = None

class FirehoseTypeDef(BaseModel):
    Enabled: bool
    DeliveryStream: Optional[str] = None

class S3TypeDef(BaseModel):
    Enabled: bool
    Bucket: Optional[str] = None
    Prefix: Optional[str] = None

class BrokerSoftwareInfoTypeDef(BaseModel):
    ConfigurationArn: Optional[str] = None
    ConfigurationRevision: Optional[int] = None
    KafkaVersion: Optional[str] = None

class TlsExtraOutputTypeDef(BaseModel):
    CertificateAuthorityArnList: Optional[List[str]] = None
    Enabled: Optional[bool] = None

class UnauthenticatedTypeDef(BaseModel):
    Enabled: Optional[bool] = None

class TlsOutputTypeDef(BaseModel):
    CertificateAuthorityArnList: Optional[List[str]] = None
    Enabled: Optional[bool] = None

class TlsTypeDef(BaseModel):
    CertificateAuthorityArnList: Optional[Sequence[str]] = None
    Enabled: Optional[bool] = None

class ClientVpcConnectionTypeDef(BaseModel):
    VpcConnectionArn: str
    Authentication: Optional[str] = None
    CreationTime: Optional[datetime] = None
    State: Optional[VpcConnectionStateType] = None
    Owner: Optional[str] = None

class StateInfoTypeDef(BaseModel):
    Code: Optional[str] = None
    Message: Optional[str] = None

class ErrorInfoTypeDef(BaseModel):
    ErrorCode: Optional[str] = None
    ErrorString: Optional[str] = None

class ClusterOperationStepInfoTypeDef(BaseModel):
    StepStatus: Optional[str] = None

class ClusterOperationV2SummaryTypeDef(BaseModel):
    ClusterArn: Optional[str] = None
    ClusterType: Optional[ClusterTypeType] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    OperationArn: Optional[str] = None
    OperationState: Optional[str] = None
    OperationType: Optional[str] = None

class CompatibleKafkaVersionTypeDef(BaseModel):
    SourceVersion: Optional[str] = None
    TargetVersions: Optional[List[str]] = None

class ConfigurationInfoTypeDef(BaseModel):
    Arn: str
    Revision: int

class ConfigurationRevisionTypeDef(BaseModel):
    CreationTime: datetime
    Revision: int
    Description: Optional[str] = None

class PublicAccessTypeDef(BaseModel):
    Type: Optional[str] = None

class ConsumerGroupReplicationOutputTypeDef(BaseModel):
    ConsumerGroupsToReplicate: List[str]
    ConsumerGroupsToExclude: Optional[List[str]] = None
    DetectAndCopyNewConsumerGroups: Optional[bool] = None
    SynchroniseConsumerGroupOffsets: Optional[bool] = None

class ConsumerGroupReplicationTypeDef(BaseModel):
    ConsumerGroupsToReplicate: Sequence[str]
    ConsumerGroupsToExclude: Optional[Sequence[str]] = None
    DetectAndCopyNewConsumerGroups: Optional[bool] = None
    SynchroniseConsumerGroupOffsets: Optional[bool] = None

class ConsumerGroupReplicationUpdateTypeDef(BaseModel):
    ConsumerGroupsToExclude: Sequence[str]
    ConsumerGroupsToReplicate: Sequence[str]
    DetectAndCopyNewConsumerGroups: bool
    SynchroniseConsumerGroupOffsets: bool

class ControllerNodeInfoTypeDef(BaseModel):
    Endpoints: Optional[List[str]] = None

class CreateVpcConnectionRequestRequestTypeDef(BaseModel):
    TargetClusterArn: str
    Authentication: str
    VpcId: str
    ClientSubnets: Sequence[str]
    SecurityGroups: Sequence[str]
    Tags: Optional[Mapping[str, str]] = None

class DeleteClusterPolicyRequestRequestTypeDef(BaseModel):
    ClusterArn: str

class DeleteClusterRequestRequestTypeDef(BaseModel):
    ClusterArn: str
    CurrentVersion: Optional[str] = None

class DeleteConfigurationRequestRequestTypeDef(BaseModel):
    Arn: str

class DeleteReplicatorRequestRequestTypeDef(BaseModel):
    ReplicatorArn: str
    CurrentVersion: Optional[str] = None

class DeleteVpcConnectionRequestRequestTypeDef(BaseModel):
    Arn: str

class DescribeClusterOperationRequestRequestTypeDef(BaseModel):
    ClusterOperationArn: str

class DescribeClusterOperationV2RequestRequestTypeDef(BaseModel):
    ClusterOperationArn: str

class DescribeClusterRequestRequestTypeDef(BaseModel):
    ClusterArn: str

class DescribeClusterV2RequestRequestTypeDef(BaseModel):
    ClusterArn: str

class DescribeConfigurationRequestRequestTypeDef(BaseModel):
    Arn: str

class DescribeConfigurationRevisionRequestRequestTypeDef(BaseModel):
    Arn: str
    Revision: int

class DescribeReplicatorRequestRequestTypeDef(BaseModel):
    ReplicatorArn: str

class ReplicationStateInfoTypeDef(BaseModel):
    Code: Optional[str] = None
    Message: Optional[str] = None

class DescribeVpcConnectionRequestRequestTypeDef(BaseModel):
    Arn: str

class EncryptionAtRestTypeDef(BaseModel):
    DataVolumeKMSKeyId: str

class EncryptionInTransitTypeDef(BaseModel):
    ClientBroker: Optional[ClientBrokerType] = None
    InCluster: Optional[bool] = None

class GetBootstrapBrokersRequestRequestTypeDef(BaseModel):
    ClusterArn: str

class GetClusterPolicyRequestRequestTypeDef(BaseModel):
    ClusterArn: str

class GetCompatibleKafkaVersionsRequestRequestTypeDef(BaseModel):
    ClusterArn: Optional[str] = None

class IamTypeDef(BaseModel):
    Enabled: Optional[bool] = None

class JmxExporterInfoTypeDef(BaseModel):
    EnabledInBroker: bool

class JmxExporterTypeDef(BaseModel):
    EnabledInBroker: bool

class KafkaClusterClientVpcConfigOutputTypeDef(BaseModel):
    SubnetIds: List[str]
    SecurityGroupIds: Optional[List[str]] = None

class KafkaClusterClientVpcConfigTypeDef(BaseModel):
    SubnetIds: Sequence[str]
    SecurityGroupIds: Optional[Sequence[str]] = None

class KafkaVersionTypeDef(BaseModel):
    Version: Optional[str] = None
    Status: Optional[KafkaVersionStatusType] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListClientVpcConnectionsRequestRequestTypeDef(BaseModel):
    ClusterArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListClusterOperationsRequestRequestTypeDef(BaseModel):
    ClusterArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListClusterOperationsV2RequestRequestTypeDef(BaseModel):
    ClusterArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListClustersRequestRequestTypeDef(BaseModel):
    ClusterNameFilter: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListClustersV2RequestRequestTypeDef(BaseModel):
    ClusterNameFilter: Optional[str] = None
    ClusterTypeFilter: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListConfigurationRevisionsRequestRequestTypeDef(BaseModel):
    Arn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListConfigurationsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListKafkaVersionsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListNodesRequestRequestTypeDef(BaseModel):
    ClusterArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListReplicatorsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ReplicatorNameFilter: Optional[str] = None

class ListScramSecretsRequestRequestTypeDef(BaseModel):
    ClusterArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class ListVpcConnectionsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class VpcConnectionTypeDef(BaseModel):
    VpcConnectionArn: str
    TargetClusterArn: str
    CreationTime: Optional[datetime] = None
    Authentication: Optional[str] = None
    VpcId: Optional[str] = None
    State: Optional[VpcConnectionStateType] = None

class NodeExporterInfoTypeDef(BaseModel):
    EnabledInBroker: bool

class NodeExporterTypeDef(BaseModel):
    EnabledInBroker: bool

class ZookeeperNodeInfoTypeDef(BaseModel):
    AttachedENIId: Optional[str] = None
    ClientVpcIpAddress: Optional[str] = None
    Endpoints: Optional[List[str]] = None
    ZookeeperId: Optional[float] = None
    ZookeeperVersion: Optional[str] = None

class PutClusterPolicyRequestRequestTypeDef(BaseModel):
    ClusterArn: str
    Policy: str
    CurrentVersion: Optional[str] = None

class RebootBrokerRequestRequestTypeDef(BaseModel):
    BrokerIds: Sequence[str]
    ClusterArn: str

class RejectClientVpcConnectionRequestRequestTypeDef(BaseModel):
    ClusterArn: str
    VpcConnectionArn: str

class ReplicationInfoSummaryTypeDef(BaseModel):
    SourceKafkaClusterAlias: Optional[str] = None
    TargetKafkaClusterAlias: Optional[str] = None

class ReplicationStartingPositionTypeDef(BaseModel):
    Type: Optional[ReplicationStartingPositionTypeType] = None

class ScramTypeDef(BaseModel):
    Enabled: Optional[bool] = None

class VpcConfigTypeDef(BaseModel):
    SubnetIds: Sequence[str]
    SecurityGroupIds: Optional[Sequence[str]] = None

class VpcConfigOutputTypeDef(BaseModel):
    SubnetIds: List[str]
    SecurityGroupIds: Optional[List[str]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class TopicReplicationUpdateTypeDef(BaseModel):
    CopyAccessControlListsForTopics: bool
    CopyTopicConfigurations: bool
    DetectAndCopyNewTopics: bool
    TopicsToExclude: Sequence[str]
    TopicsToReplicate: Sequence[str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateBrokerCountRequestRequestTypeDef(BaseModel):
    ClusterArn: str
    CurrentVersion: str
    TargetNumberOfBrokerNodes: int

class UpdateBrokerTypeRequestRequestTypeDef(BaseModel):
    ClusterArn: str
    CurrentVersion: str
    TargetInstanceType: str

class UserIdentityTypeDef(BaseModel):
    Type: Optional[UserIdentityTypeType] = None
    PrincipalId: Optional[str] = None

class VpcConnectivityTlsTypeDef(BaseModel):
    Enabled: Optional[bool] = None

class VpcConnectivityIamTypeDef(BaseModel):
    Enabled: Optional[bool] = None

class VpcConnectivityScramTypeDef(BaseModel):
    Enabled: Optional[bool] = None

class KafkaClusterSummaryTypeDef(BaseModel):
    AmazonMskCluster: Optional[AmazonMskClusterTypeDef] = None
    KafkaClusterAlias: Optional[str] = None

class CreateClusterResponseTypeDef(BaseModel):
    ClusterArn: str
    ClusterName: str
    State: ClusterStateType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateClusterV2ResponseTypeDef(BaseModel):
    ClusterArn: str
    ClusterName: str
    State: ClusterStateType
    ClusterType: ClusterTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateReplicatorResponseTypeDef(BaseModel):
    ReplicatorArn: str
    ReplicatorName: str
    ReplicatorState: ReplicatorStateType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVpcConnectionResponseTypeDef(BaseModel):
    VpcConnectionArn: str
    State: VpcConnectionStateType
    Authentication: str
    VpcId: str
    ClientSubnets: List[str]
    SecurityGroups: List[str]
    CreationTime: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteClusterResponseTypeDef(BaseModel):
    ClusterArn: str
    State: ClusterStateType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteConfigurationResponseTypeDef(BaseModel):
    Arn: str
    State: ConfigurationStateType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteReplicatorResponseTypeDef(BaseModel):
    ReplicatorArn: str
    ReplicatorState: ReplicatorStateType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVpcConnectionResponseTypeDef(BaseModel):
    VpcConnectionArn: str
    State: VpcConnectionStateType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeConfigurationRevisionResponseTypeDef(BaseModel):
    Arn: str
    CreationTime: datetime
    Description: str
    Revision: int
    ServerProperties: bytes
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVpcConnectionResponseTypeDef(BaseModel):
    VpcConnectionArn: str
    TargetClusterArn: str
    State: VpcConnectionStateType
    Authentication: str
    VpcId: str
    Subnets: List[str]
    SecurityGroups: List[str]
    CreationTime: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetBootstrapBrokersResponseTypeDef(BaseModel):
    BootstrapBrokerString: str
    BootstrapBrokerStringTls: str
    BootstrapBrokerStringSaslScram: str
    BootstrapBrokerStringSaslIam: str
    BootstrapBrokerStringPublicTls: str
    BootstrapBrokerStringPublicSaslScram: str
    BootstrapBrokerStringPublicSaslIam: str
    BootstrapBrokerStringVpcConnectivityTls: str
    BootstrapBrokerStringVpcConnectivitySaslScram: str
    BootstrapBrokerStringVpcConnectivitySaslIam: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetClusterPolicyResponseTypeDef(BaseModel):
    CurrentVersion: str
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListScramSecretsResponseTypeDef(BaseModel):
    SecretArnList: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutClusterPolicyResponseTypeDef(BaseModel):
    CurrentVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class RebootBrokerResponseTypeDef(BaseModel):
    ClusterArn: str
    ClusterOperationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBrokerCountResponseTypeDef(BaseModel):
    ClusterArn: str
    ClusterOperationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBrokerStorageResponseTypeDef(BaseModel):
    ClusterArn: str
    ClusterOperationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBrokerTypeResponseTypeDef(BaseModel):
    ClusterArn: str
    ClusterOperationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateClusterConfigurationResponseTypeDef(BaseModel):
    ClusterArn: str
    ClusterOperationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateClusterKafkaVersionResponseTypeDef(BaseModel):
    ClusterArn: str
    ClusterOperationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConnectivityResponseTypeDef(BaseModel):
    ClusterArn: str
    ClusterOperationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMonitoringResponseTypeDef(BaseModel):
    ClusterArn: str
    ClusterOperationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateReplicationInfoResponseTypeDef(BaseModel):
    ReplicatorArn: str
    ReplicatorState: ReplicatorStateType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSecurityResponseTypeDef(BaseModel):
    ClusterArn: str
    ClusterOperationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateStorageResponseTypeDef(BaseModel):
    ClusterArn: str
    ClusterOperationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchAssociateScramSecretResponseTypeDef(BaseModel):
    ClusterArn: str
    UnprocessedScramSecrets: List[UnprocessedScramSecretTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDisassociateScramSecretResponseTypeDef(BaseModel):
    ClusterArn: str
    UnprocessedScramSecrets: List[UnprocessedScramSecretTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConfigurationRequestRequestTypeDef(BaseModel):
    Name: str
    ServerProperties: BlobTypeDef
    Description: Optional[str] = None
    KafkaVersions: Optional[Sequence[str]] = None

class UpdateConfigurationRequestRequestTypeDef(BaseModel):
    Arn: str
    ServerProperties: BlobTypeDef
    Description: Optional[str] = None

class BrokerEBSVolumeInfoTypeDef(BaseModel):
    KafkaBrokerNodeId: str
    ProvisionedThroughput: Optional[ProvisionedThroughputTypeDef] = None
    VolumeSizeGB: Optional[int] = None

class EBSStorageInfoTypeDef(BaseModel):
    ProvisionedThroughput: Optional[ProvisionedThroughputTypeDef] = None
    VolumeSize: Optional[int] = None

class UpdateStorageRequestRequestTypeDef(BaseModel):
    ClusterArn: str
    CurrentVersion: str
    ProvisionedThroughput: Optional[ProvisionedThroughputTypeDef] = None
    StorageMode: Optional[StorageModeType] = None
    VolumeSizeGB: Optional[int] = None

class BrokerLogsTypeDef(BaseModel):
    CloudWatchLogs: Optional[CloudWatchLogsTypeDef] = None
    Firehose: Optional[FirehoseTypeDef] = None
    S3: Optional[S3TypeDef] = None

class BrokerNodeInfoTypeDef(BaseModel):
    AttachedENIId: Optional[str] = None
    BrokerId: Optional[float] = None
    ClientSubnet: Optional[str] = None
    ClientVpcIpAddress: Optional[str] = None
    CurrentBrokerSoftwareInfo: Optional[BrokerSoftwareInfoTypeDef] = None
    Endpoints: Optional[List[str]] = None

class ListClientVpcConnectionsResponseTypeDef(BaseModel):
    ClientVpcConnections: List[ClientVpcConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ClusterOperationStepTypeDef(BaseModel):
    StepInfo: Optional[ClusterOperationStepInfoTypeDef] = None
    StepName: Optional[str] = None

class ListClusterOperationsV2ResponseTypeDef(BaseModel):
    ClusterOperationInfoList: List[ClusterOperationV2SummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetCompatibleKafkaVersionsResponseTypeDef(BaseModel):
    CompatibleKafkaVersions: List[CompatibleKafkaVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateClusterConfigurationRequestRequestTypeDef(BaseModel):
    ClusterArn: str
    ConfigurationInfo: ConfigurationInfoTypeDef
    CurrentVersion: str

class UpdateClusterKafkaVersionRequestRequestTypeDef(BaseModel):
    ClusterArn: str
    CurrentVersion: str
    TargetKafkaVersion: str
    ConfigurationInfo: Optional[ConfigurationInfoTypeDef] = None

class ConfigurationTypeDef(BaseModel):
    Arn: str
    CreationTime: datetime
    Description: str
    KafkaVersions: List[str]
    LatestRevision: ConfigurationRevisionTypeDef
    Name: str
    State: ConfigurationStateType

class CreateConfigurationResponseTypeDef(BaseModel):
    Arn: str
    CreationTime: datetime
    LatestRevision: ConfigurationRevisionTypeDef
    Name: str
    State: ConfigurationStateType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeConfigurationResponseTypeDef(BaseModel):
    Arn: str
    CreationTime: datetime
    Description: str
    KafkaVersions: List[str]
    LatestRevision: ConfigurationRevisionTypeDef
    Name: str
    State: ConfigurationStateType
    ResponseMetadata: ResponseMetadataTypeDef

class ListConfigurationRevisionsResponseTypeDef(BaseModel):
    Revisions: List[ConfigurationRevisionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateConfigurationResponseTypeDef(BaseModel):
    Arn: str
    LatestRevision: ConfigurationRevisionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EncryptionInfoTypeDef(BaseModel):
    EncryptionAtRest: Optional[EncryptionAtRestTypeDef] = None
    EncryptionInTransit: Optional[EncryptionInTransitTypeDef] = None

class ServerlessSaslTypeDef(BaseModel):
    Iam: Optional[IamTypeDef] = None

class KafkaClusterDescriptionTypeDef(BaseModel):
    AmazonMskCluster: Optional[AmazonMskClusterTypeDef] = None
    KafkaClusterAlias: Optional[str] = None
    VpcConfig: Optional[KafkaClusterClientVpcConfigOutputTypeDef] = None

class KafkaClusterTypeDef(BaseModel):
    AmazonMskCluster: AmazonMskClusterTypeDef
    VpcConfig: KafkaClusterClientVpcConfigTypeDef

class ListKafkaVersionsResponseTypeDef(BaseModel):
    KafkaVersions: List[KafkaVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListClientVpcConnectionsRequestListClientVpcConnectionsPaginateTypeDef(BaseModel):
    ClusterArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListClusterOperationsRequestListClusterOperationsPaginateTypeDef(BaseModel):
    ClusterArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListClusterOperationsV2RequestListClusterOperationsV2PaginateTypeDef(BaseModel):
    ClusterArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListClustersRequestListClustersPaginateTypeDef(BaseModel):
    ClusterNameFilter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListClustersV2RequestListClustersV2PaginateTypeDef(BaseModel):
    ClusterNameFilter: Optional[str] = None
    ClusterTypeFilter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConfigurationRevisionsRequestListConfigurationRevisionsPaginateTypeDef(BaseModel):
    Arn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConfigurationsRequestListConfigurationsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListKafkaVersionsRequestListKafkaVersionsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListNodesRequestListNodesPaginateTypeDef(BaseModel):
    ClusterArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReplicatorsRequestListReplicatorsPaginateTypeDef(BaseModel):
    ReplicatorNameFilter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListScramSecretsRequestListScramSecretsPaginateTypeDef(BaseModel):
    ClusterArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVpcConnectionsRequestListVpcConnectionsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVpcConnectionsResponseTypeDef(BaseModel):
    VpcConnections: List[VpcConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PrometheusInfoTypeDef(BaseModel):
    JmxExporter: Optional[JmxExporterInfoTypeDef] = None
    NodeExporter: Optional[NodeExporterInfoTypeDef] = None

class PrometheusTypeDef(BaseModel):
    JmxExporter: Optional[JmxExporterTypeDef] = None
    NodeExporter: Optional[NodeExporterTypeDef] = None

class TopicReplicationOutputTypeDef(BaseModel):
    TopicsToReplicate: List[str]
    CopyAccessControlListsForTopics: Optional[bool] = None
    CopyTopicConfigurations: Optional[bool] = None
    DetectAndCopyNewTopics: Optional[bool] = None
    StartingPosition: Optional[ReplicationStartingPositionTypeDef] = None
    TopicsToExclude: Optional[List[str]] = None

class TopicReplicationTypeDef(BaseModel):
    TopicsToReplicate: Sequence[str]
    CopyAccessControlListsForTopics: Optional[bool] = None
    CopyTopicConfigurations: Optional[bool] = None
    DetectAndCopyNewTopics: Optional[bool] = None
    StartingPosition: Optional[ReplicationStartingPositionTypeDef] = None
    TopicsToExclude: Optional[Sequence[str]] = None

class SaslTypeDef(BaseModel):
    Scram: Optional[ScramTypeDef] = None
    Iam: Optional[IamTypeDef] = None

class UpdateReplicationInfoRequestRequestTypeDef(BaseModel):
    CurrentVersion: str
    ReplicatorArn: str
    SourceKafkaClusterArn: str
    TargetKafkaClusterArn: str
    ConsumerGroupReplication: Optional[ConsumerGroupReplicationUpdateTypeDef] = None
    TopicReplication: Optional[TopicReplicationUpdateTypeDef] = None

class VpcConnectionInfoServerlessTypeDef(BaseModel):
    CreationTime: Optional[datetime] = None
    Owner: Optional[str] = None
    UserIdentity: Optional[UserIdentityTypeDef] = None
    VpcConnectionArn: Optional[str] = None

class VpcConnectionInfoTypeDef(BaseModel):
    VpcConnectionArn: Optional[str] = None
    Owner: Optional[str] = None
    UserIdentity: Optional[UserIdentityTypeDef] = None
    CreationTime: Optional[datetime] = None

class VpcConnectivitySaslTypeDef(BaseModel):
    Scram: Optional[VpcConnectivityScramTypeDef] = None
    Iam: Optional[VpcConnectivityIamTypeDef] = None

class ReplicatorSummaryTypeDef(BaseModel):
    CreationTime: Optional[datetime] = None
    CurrentVersion: Optional[str] = None
    IsReplicatorReference: Optional[bool] = None
    KafkaClustersSummary: Optional[List[KafkaClusterSummaryTypeDef]] = None
    ReplicationInfoSummaryList: Optional[List[ReplicationInfoSummaryTypeDef]] = None
    ReplicatorArn: Optional[str] = None
    ReplicatorName: Optional[str] = None
    ReplicatorResourceArn: Optional[str] = None
    ReplicatorState: Optional[ReplicatorStateType] = None

class UpdateBrokerStorageRequestRequestTypeDef(BaseModel):
    ClusterArn: str
    CurrentVersion: str
    TargetBrokerEBSVolumeInfo: Sequence[BrokerEBSVolumeInfoTypeDef]

class StorageInfoTypeDef(BaseModel):
    EbsStorageInfo: Optional[EBSStorageInfoTypeDef] = None

class LoggingInfoTypeDef(BaseModel):
    BrokerLogs: BrokerLogsTypeDef

class NodeInfoTypeDef(BaseModel):
    AddedToClusterTime: Optional[str] = None
    BrokerNodeInfo: Optional[BrokerNodeInfoTypeDef] = None
    ControllerNodeInfo: Optional[ControllerNodeInfoTypeDef] = None
    InstanceType: Optional[str] = None
    NodeARN: Optional[str] = None
    NodeType: Optional[Literal["BROKER"]] = None
    ZookeeperNodeInfo: Optional[ZookeeperNodeInfoTypeDef] = None

class ListConfigurationsResponseTypeDef(BaseModel):
    Configurations: List[ConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ServerlessClientAuthenticationTypeDef(BaseModel):
    Sasl: Optional[ServerlessSaslTypeDef] = None

class OpenMonitoringInfoTypeDef(BaseModel):
    Prometheus: PrometheusInfoTypeDef

class OpenMonitoringTypeDef(BaseModel):
    Prometheus: PrometheusTypeDef

class ReplicationInfoDescriptionTypeDef(BaseModel):
    ConsumerGroupReplication: Optional[ConsumerGroupReplicationOutputTypeDef] = None
    SourceKafkaClusterAlias: Optional[str] = None
    TargetCompressionType: Optional[TargetCompressionTypeType] = None
    TargetKafkaClusterAlias: Optional[str] = None
    TopicReplication: Optional[TopicReplicationOutputTypeDef] = None

class ReplicationInfoTypeDef(BaseModel):
    ConsumerGroupReplication: ConsumerGroupReplicationTypeDef
    SourceKafkaClusterArn: str
    TargetCompressionType: TargetCompressionTypeType
    TargetKafkaClusterArn: str
    TopicReplication: TopicReplicationTypeDef

class ClientAuthenticationExtraOutputTypeDef(BaseModel):
    Sasl: Optional[SaslTypeDef] = None
    Tls: Optional[TlsExtraOutputTypeDef] = None
    Unauthenticated: Optional[UnauthenticatedTypeDef] = None

class ClientAuthenticationOutputTypeDef(BaseModel):
    Sasl: Optional[SaslTypeDef] = None
    Tls: Optional[TlsOutputTypeDef] = None
    Unauthenticated: Optional[UnauthenticatedTypeDef] = None

class ClientAuthenticationTypeDef(BaseModel):
    Sasl: Optional[SaslTypeDef] = None
    Tls: Optional[TlsTypeDef] = None
    Unauthenticated: Optional[UnauthenticatedTypeDef] = None

class ClusterOperationV2ServerlessTypeDef(BaseModel):
    VpcConnectionInfo: Optional[VpcConnectionInfoServerlessTypeDef] = None

class VpcConnectivityClientAuthenticationTypeDef(BaseModel):
    Sasl: Optional[VpcConnectivitySaslTypeDef] = None
    Tls: Optional[VpcConnectivityTlsTypeDef] = None

class ListReplicatorsResponseTypeDef(BaseModel):
    Replicators: List[ReplicatorSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListNodesResponseTypeDef(BaseModel):
    NodeInfoList: List[NodeInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ServerlessRequestTypeDef(BaseModel):
    VpcConfigs: Sequence[VpcConfigTypeDef]
    ClientAuthentication: Optional[ServerlessClientAuthenticationTypeDef] = None

class ServerlessTypeDef(BaseModel):
    VpcConfigs: List[VpcConfigOutputTypeDef]
    ClientAuthentication: Optional[ServerlessClientAuthenticationTypeDef] = None

class UpdateMonitoringRequestRequestTypeDef(BaseModel):
    ClusterArn: str
    CurrentVersion: str
    EnhancedMonitoring: Optional[EnhancedMonitoringType] = None
    OpenMonitoring: Optional[OpenMonitoringInfoTypeDef] = None
    LoggingInfo: Optional[LoggingInfoTypeDef] = None

class DescribeReplicatorResponseTypeDef(BaseModel):
    CreationTime: datetime
    CurrentVersion: str
    IsReplicatorReference: bool
    KafkaClusters: List[KafkaClusterDescriptionTypeDef]
    ReplicationInfoList: List[ReplicationInfoDescriptionTypeDef]
    ReplicatorArn: str
    ReplicatorDescription: str
    ReplicatorName: str
    ReplicatorResourceArn: str
    ReplicatorState: ReplicatorStateType
    ServiceExecutionRoleArn: str
    StateInfo: ReplicationStateInfoTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateReplicatorRequestRequestTypeDef(BaseModel):
    KafkaClusters: Sequence[KafkaClusterTypeDef]
    ReplicationInfoList: Sequence[ReplicationInfoTypeDef]
    ReplicatorName: str
    ServiceExecutionRoleArn: str
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class UpdateSecurityRequestRequestTypeDef(BaseModel):
    ClusterArn: str
    CurrentVersion: str
    ClientAuthentication: Optional[ClientAuthenticationTypeDef] = None
    EncryptionInfo: Optional[EncryptionInfoTypeDef] = None

class VpcConnectivityTypeDef(BaseModel):
    ClientAuthentication: Optional[VpcConnectivityClientAuthenticationTypeDef] = None

class ConnectivityInfoTypeDef(BaseModel):
    PublicAccess: Optional[PublicAccessTypeDef] = None
    VpcConnectivity: Optional[VpcConnectivityTypeDef] = None

class BrokerNodeGroupInfoExtraOutputTypeDef(BaseModel):
    ClientSubnets: List[str]
    InstanceType: str
    BrokerAZDistribution: Optional[Literal["DEFAULT"]] = None
    SecurityGroups: Optional[List[str]] = None
    StorageInfo: Optional[StorageInfoTypeDef] = None
    ConnectivityInfo: Optional[ConnectivityInfoTypeDef] = None
    ZoneIds: Optional[List[str]] = None

class BrokerNodeGroupInfoOutputTypeDef(BaseModel):
    ClientSubnets: List[str]
    InstanceType: str
    BrokerAZDistribution: Optional[Literal["DEFAULT"]] = None
    SecurityGroups: Optional[List[str]] = None
    StorageInfo: Optional[StorageInfoTypeDef] = None
    ConnectivityInfo: Optional[ConnectivityInfoTypeDef] = None
    ZoneIds: Optional[List[str]] = None

class BrokerNodeGroupInfoTypeDef(BaseModel):
    ClientSubnets: Sequence[str]
    InstanceType: str
    BrokerAZDistribution: Optional[Literal["DEFAULT"]] = None
    SecurityGroups: Optional[Sequence[str]] = None
    StorageInfo: Optional[StorageInfoTypeDef] = None
    ConnectivityInfo: Optional[ConnectivityInfoTypeDef] = None
    ZoneIds: Optional[Sequence[str]] = None

class MutableClusterInfoTypeDef(BaseModel):
    BrokerEBSVolumeInfo: Optional[List[BrokerEBSVolumeInfoTypeDef]] = None
    ConfigurationInfo: Optional[ConfigurationInfoTypeDef] = None
    NumberOfBrokerNodes: Optional[int] = None
    EnhancedMonitoring: Optional[EnhancedMonitoringType] = None
    OpenMonitoring: Optional[OpenMonitoringTypeDef] = None
    KafkaVersion: Optional[str] = None
    LoggingInfo: Optional[LoggingInfoTypeDef] = None
    InstanceType: Optional[str] = None
    ClientAuthentication: Optional[ClientAuthenticationOutputTypeDef] = None
    EncryptionInfo: Optional[EncryptionInfoTypeDef] = None
    ConnectivityInfo: Optional[ConnectivityInfoTypeDef] = None
    StorageMode: Optional[StorageModeType] = None
    BrokerCountUpdateInfo: Optional[BrokerCountUpdateInfoTypeDef] = None

class UpdateConnectivityRequestRequestTypeDef(BaseModel):
    ClusterArn: str
    ConnectivityInfo: ConnectivityInfoTypeDef
    CurrentVersion: str

class ClusterInfoTypeDef(BaseModel):
    ActiveOperationArn: Optional[str] = None
    BrokerNodeGroupInfo: Optional[BrokerNodeGroupInfoOutputTypeDef] = None
    ClientAuthentication: Optional[ClientAuthenticationOutputTypeDef] = None
    ClusterArn: Optional[str] = None
    ClusterName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    CurrentBrokerSoftwareInfo: Optional[BrokerSoftwareInfoTypeDef] = None
    CurrentVersion: Optional[str] = None
    EncryptionInfo: Optional[EncryptionInfoTypeDef] = None
    EnhancedMonitoring: Optional[EnhancedMonitoringType] = None
    OpenMonitoring: Optional[OpenMonitoringTypeDef] = None
    LoggingInfo: Optional[LoggingInfoTypeDef] = None
    NumberOfBrokerNodes: Optional[int] = None
    State: Optional[ClusterStateType] = None
    StateInfo: Optional[StateInfoTypeDef] = None
    Tags: Optional[Dict[str, str]] = None
    ZookeeperConnectString: Optional[str] = None
    ZookeeperConnectStringTls: Optional[str] = None
    StorageMode: Optional[StorageModeType] = None
    CustomerActionStatus: Optional[CustomerActionStatusType] = None

class ProvisionedTypeDef(BaseModel):
    BrokerNodeGroupInfo: BrokerNodeGroupInfoOutputTypeDef
    NumberOfBrokerNodes: int
    CurrentBrokerSoftwareInfo: Optional[BrokerSoftwareInfoTypeDef] = None
    ClientAuthentication: Optional[ClientAuthenticationOutputTypeDef] = None
    EncryptionInfo: Optional[EncryptionInfoTypeDef] = None
    EnhancedMonitoring: Optional[EnhancedMonitoringType] = None
    OpenMonitoring: Optional[OpenMonitoringInfoTypeDef] = None
    LoggingInfo: Optional[LoggingInfoTypeDef] = None
    ZookeeperConnectString: Optional[str] = None
    ZookeeperConnectStringTls: Optional[str] = None
    StorageMode: Optional[StorageModeType] = None
    CustomerActionStatus: Optional[CustomerActionStatusType] = None

class CreateClusterRequestRequestTypeDef(BaseModel):
    BrokerNodeGroupInfo: BrokerNodeGroupInfoTypeDef
    ClusterName: str
    KafkaVersion: str
    NumberOfBrokerNodes: int
    ClientAuthentication: Optional[ClientAuthenticationTypeDef] = None
    ConfigurationInfo: Optional[ConfigurationInfoTypeDef] = None
    EncryptionInfo: Optional[EncryptionInfoTypeDef] = None
    EnhancedMonitoring: Optional[EnhancedMonitoringType] = None
    OpenMonitoring: Optional[OpenMonitoringInfoTypeDef] = None
    LoggingInfo: Optional[LoggingInfoTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None
    StorageMode: Optional[StorageModeType] = None

class ProvisionedRequestTypeDef(BaseModel):
    BrokerNodeGroupInfo: BrokerNodeGroupInfoTypeDef
    KafkaVersion: str
    NumberOfBrokerNodes: int
    ClientAuthentication: Optional[ClientAuthenticationTypeDef] = None
    ConfigurationInfo: Optional[ConfigurationInfoTypeDef] = None
    EncryptionInfo: Optional[EncryptionInfoTypeDef] = None
    EnhancedMonitoring: Optional[EnhancedMonitoringType] = None
    OpenMonitoring: Optional[OpenMonitoringInfoTypeDef] = None
    LoggingInfo: Optional[LoggingInfoTypeDef] = None
    StorageMode: Optional[StorageModeType] = None

class ClusterOperationInfoTypeDef(BaseModel):
    ClientRequestId: Optional[str] = None
    ClusterArn: Optional[str] = None
    CreationTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    ErrorInfo: Optional[ErrorInfoTypeDef] = None
    OperationArn: Optional[str] = None
    OperationState: Optional[str] = None
    OperationSteps: Optional[List[ClusterOperationStepTypeDef]] = None
    OperationType: Optional[str] = None
    SourceClusterInfo: Optional[MutableClusterInfoTypeDef] = None
    TargetClusterInfo: Optional[MutableClusterInfoTypeDef] = None
    VpcConnectionInfo: Optional[VpcConnectionInfoTypeDef] = None

class ClusterOperationV2ProvisionedTypeDef(BaseModel):
    OperationSteps: Optional[List[ClusterOperationStepTypeDef]] = None
    SourceClusterInfo: Optional[MutableClusterInfoTypeDef] = None
    TargetClusterInfo: Optional[MutableClusterInfoTypeDef] = None
    VpcConnectionInfo: Optional[VpcConnectionInfoTypeDef] = None

class DescribeClusterResponseTypeDef(BaseModel):
    ClusterInfo: ClusterInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListClustersResponseTypeDef(BaseModel):
    ClusterInfoList: List[ClusterInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ClusterTypeDef(BaseModel):
    ActiveOperationArn: Optional[str] = None
    ClusterType: Optional[ClusterTypeType] = None
    ClusterArn: Optional[str] = None
    ClusterName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    CurrentVersion: Optional[str] = None
    State: Optional[ClusterStateType] = None
    StateInfo: Optional[StateInfoTypeDef] = None
    Tags: Optional[Dict[str, str]] = None
    Provisioned: Optional[ProvisionedTypeDef] = None
    Serverless: Optional[ServerlessTypeDef] = None

class CreateClusterV2RequestRequestTypeDef(BaseModel):
    ClusterName: str
    Tags: Optional[Mapping[str, str]] = None
    Provisioned: Optional[ProvisionedRequestTypeDef] = None
    Serverless: Optional[ServerlessRequestTypeDef] = None

class DescribeClusterOperationResponseTypeDef(BaseModel):
    ClusterOperationInfo: ClusterOperationInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListClusterOperationsResponseTypeDef(BaseModel):
    ClusterOperationInfoList: List[ClusterOperationInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ClusterOperationV2TypeDef(BaseModel):
    ClusterArn: Optional[str] = None
    ClusterType: Optional[ClusterTypeType] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    ErrorInfo: Optional[ErrorInfoTypeDef] = None
    OperationArn: Optional[str] = None
    OperationState: Optional[str] = None
    OperationType: Optional[str] = None
    Provisioned: Optional[ClusterOperationV2ProvisionedTypeDef] = None
    Serverless: Optional[ClusterOperationV2ServerlessTypeDef] = None

class DescribeClusterV2ResponseTypeDef(BaseModel):
    ClusterInfo: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListClustersV2ResponseTypeDef(BaseModel):
    ClusterInfoList: List[ClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeClusterOperationV2ResponseTypeDef(BaseModel):
    ClusterOperationInfo: ClusterOperationV2TypeDef
    ResponseMetadata: ResponseMetadataTypeDef


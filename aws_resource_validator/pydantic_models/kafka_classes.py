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
from aws_resource_validator.pydantic_models.kafka_constants import *

class AmazonMskClusterTypeDef(BaseValidatorModel):
    MskClusterArn: str

class BatchAssociateScramSecretRequestRequestTypeDef(BaseValidatorModel):
    ClusterArn: str
    SecretArnList: Sequence[str]

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class UnprocessedScramSecretTypeDef(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None
    SecretArn: Optional[str] = None

class BatchDisassociateScramSecretRequestRequestTypeDef(BaseValidatorModel):
    ClusterArn: str
    SecretArnList: Sequence[str]

class BrokerCountUpdateInfoTypeDef(BaseValidatorModel):
    CreatedBrokerIds: Optional[List[float]] = None
    DeletedBrokerIds: Optional[List[float]] = None

class ProvisionedThroughputTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    VolumeThroughput: Optional[int] = None

class CloudWatchLogsTypeDef(BaseValidatorModel):
    Enabled: bool
    LogGroup: Optional[str] = None

class FirehoseTypeDef(BaseValidatorModel):
    Enabled: bool
    DeliveryStream: Optional[str] = None

class S3TypeDef(BaseValidatorModel):
    Enabled: bool
    Bucket: Optional[str] = None
    Prefix: Optional[str] = None

class BrokerSoftwareInfoTypeDef(BaseValidatorModel):
    ConfigurationArn: Optional[str] = None
    ConfigurationRevision: Optional[int] = None
    KafkaVersion: Optional[str] = None

class TlsExtraOutputTypeDef(BaseValidatorModel):
    CertificateAuthorityArnList: Optional[List[str]] = None
    Enabled: Optional[bool] = None

class UnauthenticatedTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None

class TlsOutputTypeDef(BaseValidatorModel):
    CertificateAuthorityArnList: Optional[List[str]] = None
    Enabled: Optional[bool] = None

class TlsTypeDef(BaseValidatorModel):
    CertificateAuthorityArnList: Optional[Sequence[str]] = None
    Enabled: Optional[bool] = None

class ClientVpcConnectionTypeDef(BaseValidatorModel):
    VpcConnectionArn: str
    Authentication: Optional[str] = None
    CreationTime: Optional[datetime] = None
    State: Optional[VpcConnectionStateType] = None
    Owner: Optional[str] = None

class StateInfoTypeDef(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None

class ErrorInfoTypeDef(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorString: Optional[str] = None

class ClusterOperationStepInfoTypeDef(BaseValidatorModel):
    StepStatus: Optional[str] = None

class ClusterOperationV2SummaryTypeDef(BaseValidatorModel):
    ClusterArn: Optional[str] = None
    ClusterType: Optional[ClusterTypeType] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    OperationArn: Optional[str] = None
    OperationState: Optional[str] = None
    OperationType: Optional[str] = None

class CompatibleKafkaVersionTypeDef(BaseValidatorModel):
    SourceVersion: Optional[str] = None
    TargetVersions: Optional[List[str]] = None

class ConfigurationInfoTypeDef(BaseValidatorModel):
    Arn: str
    Revision: int

class ConfigurationRevisionTypeDef(BaseValidatorModel):
    CreationTime: datetime
    Revision: int
    Description: Optional[str] = None

class PublicAccessTypeDef(BaseValidatorModel):
    Type: Optional[str] = None

class ConsumerGroupReplicationOutputTypeDef(BaseValidatorModel):
    ConsumerGroupsToReplicate: List[str]
    ConsumerGroupsToExclude: Optional[List[str]] = None
    DetectAndCopyNewConsumerGroups: Optional[bool] = None
    SynchroniseConsumerGroupOffsets: Optional[bool] = None

class ConsumerGroupReplicationTypeDef(BaseValidatorModel):
    ConsumerGroupsToReplicate: Sequence[str]
    ConsumerGroupsToExclude: Optional[Sequence[str]] = None
    DetectAndCopyNewConsumerGroups: Optional[bool] = None
    SynchroniseConsumerGroupOffsets: Optional[bool] = None

class ConsumerGroupReplicationUpdateTypeDef(BaseValidatorModel):
    ConsumerGroupsToExclude: Sequence[str]
    ConsumerGroupsToReplicate: Sequence[str]
    DetectAndCopyNewConsumerGroups: bool
    SynchroniseConsumerGroupOffsets: bool

class ControllerNodeInfoTypeDef(BaseValidatorModel):
    Endpoints: Optional[List[str]] = None

class CreateVpcConnectionRequestRequestTypeDef(BaseValidatorModel):
    TargetClusterArn: str
    Authentication: str
    VpcId: str
    ClientSubnets: Sequence[str]
    SecurityGroups: Sequence[str]
    Tags: Optional[Mapping[str, str]] = None

class DeleteClusterPolicyRequestRequestTypeDef(BaseValidatorModel):
    ClusterArn: str

class DeleteClusterRequestRequestTypeDef(BaseValidatorModel):
    ClusterArn: str
    CurrentVersion: Optional[str] = None

class DeleteConfigurationRequestRequestTypeDef(BaseValidatorModel):
    Arn: str

class DeleteReplicatorRequestRequestTypeDef(BaseValidatorModel):
    ReplicatorArn: str
    CurrentVersion: Optional[str] = None

class DeleteVpcConnectionRequestRequestTypeDef(BaseValidatorModel):
    Arn: str

class DescribeClusterOperationRequestRequestTypeDef(BaseValidatorModel):
    ClusterOperationArn: str

class DescribeClusterOperationV2RequestRequestTypeDef(BaseValidatorModel):
    ClusterOperationArn: str

class DescribeClusterRequestRequestTypeDef(BaseValidatorModel):
    ClusterArn: str

class DescribeClusterV2RequestRequestTypeDef(BaseValidatorModel):
    ClusterArn: str

class DescribeConfigurationRequestRequestTypeDef(BaseValidatorModel):
    Arn: str

class DescribeConfigurationRevisionRequestRequestTypeDef(BaseValidatorModel):
    Arn: str
    Revision: int

class DescribeReplicatorRequestRequestTypeDef(BaseValidatorModel):
    ReplicatorArn: str

class ReplicationStateInfoTypeDef(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None

class DescribeVpcConnectionRequestRequestTypeDef(BaseValidatorModel):
    Arn: str

class EncryptionAtRestTypeDef(BaseValidatorModel):
    DataVolumeKMSKeyId: str

class EncryptionInTransitTypeDef(BaseValidatorModel):
    ClientBroker: Optional[ClientBrokerType] = None
    InCluster: Optional[bool] = None

class GetBootstrapBrokersRequestRequestTypeDef(BaseValidatorModel):
    ClusterArn: str

class GetClusterPolicyRequestRequestTypeDef(BaseValidatorModel):
    ClusterArn: str

class GetCompatibleKafkaVersionsRequestRequestTypeDef(BaseValidatorModel):
    ClusterArn: Optional[str] = None

class IamTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None

class JmxExporterInfoTypeDef(BaseValidatorModel):
    EnabledInBroker: bool

class JmxExporterTypeDef(BaseValidatorModel):
    EnabledInBroker: bool

class KafkaClusterClientVpcConfigOutputTypeDef(BaseValidatorModel):
    SubnetIds: List[str]
    SecurityGroupIds: Optional[List[str]] = None

class KafkaClusterClientVpcConfigTypeDef(BaseValidatorModel):
    SubnetIds: Sequence[str]
    SecurityGroupIds: Optional[Sequence[str]] = None

class KafkaVersionTypeDef(BaseValidatorModel):
    Version: Optional[str] = None
    Status: Optional[KafkaVersionStatusType] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListClientVpcConnectionsRequestRequestTypeDef(BaseValidatorModel):
    ClusterArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListClusterOperationsRequestRequestTypeDef(BaseValidatorModel):
    ClusterArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListClusterOperationsV2RequestRequestTypeDef(BaseValidatorModel):
    ClusterArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListClustersRequestRequestTypeDef(BaseValidatorModel):
    ClusterNameFilter: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListClustersV2RequestRequestTypeDef(BaseValidatorModel):
    ClusterNameFilter: Optional[str] = None
    ClusterTypeFilter: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListConfigurationRevisionsRequestRequestTypeDef(BaseValidatorModel):
    Arn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListKafkaVersionsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListNodesRequestRequestTypeDef(BaseValidatorModel):
    ClusterArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListReplicatorsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ReplicatorNameFilter: Optional[str] = None

class ListScramSecretsRequestRequestTypeDef(BaseValidatorModel):
    ClusterArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class ListVpcConnectionsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class VpcConnectionTypeDef(BaseValidatorModel):
    VpcConnectionArn: str
    TargetClusterArn: str
    CreationTime: Optional[datetime] = None
    Authentication: Optional[str] = None
    VpcId: Optional[str] = None
    State: Optional[VpcConnectionStateType] = None

class NodeExporterInfoTypeDef(BaseValidatorModel):
    EnabledInBroker: bool

class NodeExporterTypeDef(BaseValidatorModel):
    EnabledInBroker: bool

class ZookeeperNodeInfoTypeDef(BaseValidatorModel):
    AttachedENIId: Optional[str] = None
    ClientVpcIpAddress: Optional[str] = None
    Endpoints: Optional[List[str]] = None
    ZookeeperId: Optional[float] = None
    ZookeeperVersion: Optional[str] = None

class PutClusterPolicyRequestRequestTypeDef(BaseValidatorModel):
    ClusterArn: str
    Policy: str
    CurrentVersion: Optional[str] = None

class RebootBrokerRequestRequestTypeDef(BaseValidatorModel):
    BrokerIds: Sequence[str]
    ClusterArn: str

class RejectClientVpcConnectionRequestRequestTypeDef(BaseValidatorModel):
    ClusterArn: str
    VpcConnectionArn: str

class ReplicationInfoSummaryTypeDef(BaseValidatorModel):
    SourceKafkaClusterAlias: Optional[str] = None
    TargetKafkaClusterAlias: Optional[str] = None

class ReplicationStartingPositionTypeDef(BaseValidatorModel):
    Type: Optional[ReplicationStartingPositionTypeType] = None

class ScramTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None

class VpcConfigTypeDef(BaseValidatorModel):
    SubnetIds: Sequence[str]
    SecurityGroupIds: Optional[Sequence[str]] = None

class VpcConfigOutputTypeDef(BaseValidatorModel):
    SubnetIds: List[str]
    SecurityGroupIds: Optional[List[str]] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class TopicReplicationUpdateTypeDef(BaseValidatorModel):
    CopyAccessControlListsForTopics: bool
    CopyTopicConfigurations: bool
    DetectAndCopyNewTopics: bool
    TopicsToExclude: Sequence[str]
    TopicsToReplicate: Sequence[str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateBrokerCountRequestRequestTypeDef(BaseValidatorModel):
    ClusterArn: str
    CurrentVersion: str
    TargetNumberOfBrokerNodes: int

class UpdateBrokerTypeRequestRequestTypeDef(BaseValidatorModel):
    ClusterArn: str
    CurrentVersion: str
    TargetInstanceType: str

class UserIdentityTypeDef(BaseValidatorModel):
    Type: Optional[UserIdentityTypeType] = None
    PrincipalId: Optional[str] = None

class VpcConnectivityTlsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None

class VpcConnectivityIamTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None

class VpcConnectivityScramTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None

class KafkaClusterSummaryTypeDef(BaseValidatorModel):
    AmazonMskCluster: Optional[AmazonMskClusterTypeDef] = None
    KafkaClusterAlias: Optional[str] = None

class CreateClusterResponseTypeDef(BaseValidatorModel):
    ClusterArn: str
    ClusterName: str
    State: ClusterStateType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateClusterV2ResponseTypeDef(BaseValidatorModel):
    ClusterArn: str
    ClusterName: str
    State: ClusterStateType
    ClusterType: ClusterTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateReplicatorResponseTypeDef(BaseValidatorModel):
    ReplicatorArn: str
    ReplicatorName: str
    ReplicatorState: ReplicatorStateType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVpcConnectionResponseTypeDef(BaseValidatorModel):
    VpcConnectionArn: str
    State: VpcConnectionStateType
    Authentication: str
    VpcId: str
    ClientSubnets: List[str]
    SecurityGroups: List[str]
    CreationTime: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteClusterResponseTypeDef(BaseValidatorModel):
    ClusterArn: str
    State: ClusterStateType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteConfigurationResponseTypeDef(BaseValidatorModel):
    Arn: str
    State: ConfigurationStateType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteReplicatorResponseTypeDef(BaseValidatorModel):
    ReplicatorArn: str
    ReplicatorState: ReplicatorStateType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVpcConnectionResponseTypeDef(BaseValidatorModel):
    VpcConnectionArn: str
    State: VpcConnectionStateType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeConfigurationRevisionResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTime: datetime
    Description: str
    Revision: int
    ServerProperties: bytes
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVpcConnectionResponseTypeDef(BaseValidatorModel):
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

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetBootstrapBrokersResponseTypeDef(BaseValidatorModel):
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

class GetClusterPolicyResponseTypeDef(BaseValidatorModel):
    CurrentVersion: str
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListScramSecretsResponseTypeDef(BaseValidatorModel):
    SecretArnList: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutClusterPolicyResponseTypeDef(BaseValidatorModel):
    CurrentVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class RebootBrokerResponseTypeDef(BaseValidatorModel):
    ClusterArn: str
    ClusterOperationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBrokerCountResponseTypeDef(BaseValidatorModel):
    ClusterArn: str
    ClusterOperationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBrokerStorageResponseTypeDef(BaseValidatorModel):
    ClusterArn: str
    ClusterOperationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBrokerTypeResponseTypeDef(BaseValidatorModel):
    ClusterArn: str
    ClusterOperationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateClusterConfigurationResponseTypeDef(BaseValidatorModel):
    ClusterArn: str
    ClusterOperationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateClusterKafkaVersionResponseTypeDef(BaseValidatorModel):
    ClusterArn: str
    ClusterOperationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConnectivityResponseTypeDef(BaseValidatorModel):
    ClusterArn: str
    ClusterOperationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMonitoringResponseTypeDef(BaseValidatorModel):
    ClusterArn: str
    ClusterOperationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateReplicationInfoResponseTypeDef(BaseValidatorModel):
    ReplicatorArn: str
    ReplicatorState: ReplicatorStateType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSecurityResponseTypeDef(BaseValidatorModel):
    ClusterArn: str
    ClusterOperationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateStorageResponseTypeDef(BaseValidatorModel):
    ClusterArn: str
    ClusterOperationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchAssociateScramSecretResponseTypeDef(BaseValidatorModel):
    ClusterArn: str
    UnprocessedScramSecrets: List[UnprocessedScramSecretTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDisassociateScramSecretResponseTypeDef(BaseValidatorModel):
    ClusterArn: str
    UnprocessedScramSecrets: List[UnprocessedScramSecretTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConfigurationRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    ServerProperties: BlobTypeDef
    Description: Optional[str] = None
    KafkaVersions: Optional[Sequence[str]] = None

class UpdateConfigurationRequestRequestTypeDef(BaseValidatorModel):
    Arn: str
    ServerProperties: BlobTypeDef
    Description: Optional[str] = None

class BrokerEBSVolumeInfoTypeDef(BaseValidatorModel):
    KafkaBrokerNodeId: str
    ProvisionedThroughput: Optional[ProvisionedThroughputTypeDef] = None
    VolumeSizeGB: Optional[int] = None

class EBSStorageInfoTypeDef(BaseValidatorModel):
    ProvisionedThroughput: Optional[ProvisionedThroughputTypeDef] = None
    VolumeSize: Optional[int] = None

class UpdateStorageRequestRequestTypeDef(BaseValidatorModel):
    ClusterArn: str
    CurrentVersion: str
    ProvisionedThroughput: Optional[ProvisionedThroughputTypeDef] = None
    StorageMode: Optional[StorageModeType] = None
    VolumeSizeGB: Optional[int] = None

class BrokerLogsTypeDef(BaseValidatorModel):
    CloudWatchLogs: Optional[CloudWatchLogsTypeDef] = None
    Firehose: Optional[FirehoseTypeDef] = None
    S3: Optional[S3TypeDef] = None

class BrokerNodeInfoTypeDef(BaseValidatorModel):
    AttachedENIId: Optional[str] = None
    BrokerId: Optional[float] = None
    ClientSubnet: Optional[str] = None
    ClientVpcIpAddress: Optional[str] = None
    CurrentBrokerSoftwareInfo: Optional[BrokerSoftwareInfoTypeDef] = None
    Endpoints: Optional[List[str]] = None

class ListClientVpcConnectionsResponseTypeDef(BaseValidatorModel):
    ClientVpcConnections: List[ClientVpcConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ClusterOperationStepTypeDef(BaseValidatorModel):
    StepInfo: Optional[ClusterOperationStepInfoTypeDef] = None
    StepName: Optional[str] = None

class ListClusterOperationsV2ResponseTypeDef(BaseValidatorModel):
    ClusterOperationInfoList: List[ClusterOperationV2SummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetCompatibleKafkaVersionsResponseTypeDef(BaseValidatorModel):
    CompatibleKafkaVersions: List[CompatibleKafkaVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateClusterConfigurationRequestRequestTypeDef(BaseValidatorModel):
    ClusterArn: str
    ConfigurationInfo: ConfigurationInfoTypeDef
    CurrentVersion: str

class UpdateClusterKafkaVersionRequestRequestTypeDef(BaseValidatorModel):
    ClusterArn: str
    CurrentVersion: str
    TargetKafkaVersion: str
    ConfigurationInfo: Optional[ConfigurationInfoTypeDef] = None

class ConfigurationTypeDef(BaseValidatorModel):
    Arn: str
    CreationTime: datetime
    Description: str
    KafkaVersions: List[str]
    LatestRevision: ConfigurationRevisionTypeDef
    Name: str
    State: ConfigurationStateType

class CreateConfigurationResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTime: datetime
    LatestRevision: ConfigurationRevisionTypeDef
    Name: str
    State: ConfigurationStateType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeConfigurationResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTime: datetime
    Description: str
    KafkaVersions: List[str]
    LatestRevision: ConfigurationRevisionTypeDef
    Name: str
    State: ConfigurationStateType
    ResponseMetadata: ResponseMetadataTypeDef

class ListConfigurationRevisionsResponseTypeDef(BaseValidatorModel):
    Revisions: List[ConfigurationRevisionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateConfigurationResponseTypeDef(BaseValidatorModel):
    Arn: str
    LatestRevision: ConfigurationRevisionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EncryptionInfoTypeDef(BaseValidatorModel):
    EncryptionAtRest: Optional[EncryptionAtRestTypeDef] = None
    EncryptionInTransit: Optional[EncryptionInTransitTypeDef] = None

class ServerlessSaslTypeDef(BaseValidatorModel):
    Iam: Optional[IamTypeDef] = None

class KafkaClusterDescriptionTypeDef(BaseValidatorModel):
    AmazonMskCluster: Optional[AmazonMskClusterTypeDef] = None
    KafkaClusterAlias: Optional[str] = None
    VpcConfig: Optional[KafkaClusterClientVpcConfigOutputTypeDef] = None

class KafkaClusterTypeDef(BaseValidatorModel):
    AmazonMskCluster: AmazonMskClusterTypeDef
    VpcConfig: KafkaClusterClientVpcConfigTypeDef

class ListKafkaVersionsResponseTypeDef(BaseValidatorModel):
    KafkaVersions: List[KafkaVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListClientVpcConnectionsRequestListClientVpcConnectionsPaginateTypeDef(BaseValidatorModel):
    ClusterArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListClusterOperationsRequestListClusterOperationsPaginateTypeDef(BaseValidatorModel):
    ClusterArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListClusterOperationsV2RequestListClusterOperationsV2PaginateTypeDef(BaseValidatorModel):
    ClusterArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListClustersRequestListClustersPaginateTypeDef(BaseValidatorModel):
    ClusterNameFilter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListClustersV2RequestListClustersV2PaginateTypeDef(BaseValidatorModel):
    ClusterNameFilter: Optional[str] = None
    ClusterTypeFilter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConfigurationRevisionsRequestListConfigurationRevisionsPaginateTypeDef(BaseValidatorModel):
    Arn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConfigurationsRequestListConfigurationsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListKafkaVersionsRequestListKafkaVersionsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListNodesRequestListNodesPaginateTypeDef(BaseValidatorModel):
    ClusterArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReplicatorsRequestListReplicatorsPaginateTypeDef(BaseValidatorModel):
    ReplicatorNameFilter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListScramSecretsRequestListScramSecretsPaginateTypeDef(BaseValidatorModel):
    ClusterArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVpcConnectionsRequestListVpcConnectionsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVpcConnectionsResponseTypeDef(BaseValidatorModel):
    VpcConnections: List[VpcConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PrometheusInfoTypeDef(BaseValidatorModel):
    JmxExporter: Optional[JmxExporterInfoTypeDef] = None
    NodeExporter: Optional[NodeExporterInfoTypeDef] = None

class PrometheusTypeDef(BaseValidatorModel):
    JmxExporter: Optional[JmxExporterTypeDef] = None
    NodeExporter: Optional[NodeExporterTypeDef] = None

class TopicReplicationOutputTypeDef(BaseValidatorModel):
    TopicsToReplicate: List[str]
    CopyAccessControlListsForTopics: Optional[bool] = None
    CopyTopicConfigurations: Optional[bool] = None
    DetectAndCopyNewTopics: Optional[bool] = None
    StartingPosition: Optional[ReplicationStartingPositionTypeDef] = None
    TopicsToExclude: Optional[List[str]] = None

class TopicReplicationTypeDef(BaseValidatorModel):
    TopicsToReplicate: Sequence[str]
    CopyAccessControlListsForTopics: Optional[bool] = None
    CopyTopicConfigurations: Optional[bool] = None
    DetectAndCopyNewTopics: Optional[bool] = None
    StartingPosition: Optional[ReplicationStartingPositionTypeDef] = None
    TopicsToExclude: Optional[Sequence[str]] = None

class SaslTypeDef(BaseValidatorModel):
    Scram: Optional[ScramTypeDef] = None
    Iam: Optional[IamTypeDef] = None

class UpdateReplicationInfoRequestRequestTypeDef(BaseValidatorModel):
    CurrentVersion: str
    ReplicatorArn: str
    SourceKafkaClusterArn: str
    TargetKafkaClusterArn: str
    ConsumerGroupReplication: Optional[ConsumerGroupReplicationUpdateTypeDef] = None
    TopicReplication: Optional[TopicReplicationUpdateTypeDef] = None

class VpcConnectionInfoServerlessTypeDef(BaseValidatorModel):
    CreationTime: Optional[datetime] = None
    Owner: Optional[str] = None
    UserIdentity: Optional[UserIdentityTypeDef] = None
    VpcConnectionArn: Optional[str] = None

class VpcConnectionInfoTypeDef(BaseValidatorModel):
    VpcConnectionArn: Optional[str] = None
    Owner: Optional[str] = None
    UserIdentity: Optional[UserIdentityTypeDef] = None
    CreationTime: Optional[datetime] = None

class VpcConnectivitySaslTypeDef(BaseValidatorModel):
    Scram: Optional[VpcConnectivityScramTypeDef] = None
    Iam: Optional[VpcConnectivityIamTypeDef] = None

class ReplicatorSummaryTypeDef(BaseValidatorModel):
    CreationTime: Optional[datetime] = None
    CurrentVersion: Optional[str] = None
    IsReplicatorReference: Optional[bool] = None
    KafkaClustersSummary: Optional[List[KafkaClusterSummaryTypeDef]] = None
    ReplicationInfoSummaryList: Optional[List[ReplicationInfoSummaryTypeDef]] = None
    ReplicatorArn: Optional[str] = None
    ReplicatorName: Optional[str] = None
    ReplicatorResourceArn: Optional[str] = None
    ReplicatorState: Optional[ReplicatorStateType] = None

class UpdateBrokerStorageRequestRequestTypeDef(BaseValidatorModel):
    ClusterArn: str
    CurrentVersion: str
    TargetBrokerEBSVolumeInfo: Sequence[BrokerEBSVolumeInfoTypeDef]

class StorageInfoTypeDef(BaseValidatorModel):
    EbsStorageInfo: Optional[EBSStorageInfoTypeDef] = None

class LoggingInfoTypeDef(BaseValidatorModel):
    BrokerLogs: BrokerLogsTypeDef

class NodeInfoTypeDef(BaseValidatorModel):
    AddedToClusterTime: Optional[str] = None
    BrokerNodeInfo: Optional[BrokerNodeInfoTypeDef] = None
    ControllerNodeInfo: Optional[ControllerNodeInfoTypeDef] = None
    InstanceType: Optional[str] = None
    NodeARN: Optional[str] = None
    NodeType: Optional[Literal["BROKER"]] = None
    ZookeeperNodeInfo: Optional[ZookeeperNodeInfoTypeDef] = None

class ListConfigurationsResponseTypeDef(BaseValidatorModel):
    Configurations: List[ConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ServerlessClientAuthenticationTypeDef(BaseValidatorModel):
    Sasl: Optional[ServerlessSaslTypeDef] = None

class OpenMonitoringInfoTypeDef(BaseValidatorModel):
    Prometheus: PrometheusInfoTypeDef

class OpenMonitoringTypeDef(BaseValidatorModel):
    Prometheus: PrometheusTypeDef

class ReplicationInfoDescriptionTypeDef(BaseValidatorModel):
    ConsumerGroupReplication: Optional[ConsumerGroupReplicationOutputTypeDef] = None
    SourceKafkaClusterAlias: Optional[str] = None
    TargetCompressionType: Optional[TargetCompressionTypeType] = None
    TargetKafkaClusterAlias: Optional[str] = None
    TopicReplication: Optional[TopicReplicationOutputTypeDef] = None

class ReplicationInfoTypeDef(BaseValidatorModel):
    ConsumerGroupReplication: ConsumerGroupReplicationTypeDef
    SourceKafkaClusterArn: str
    TargetCompressionType: TargetCompressionTypeType
    TargetKafkaClusterArn: str
    TopicReplication: TopicReplicationTypeDef

class ClientAuthenticationExtraOutputTypeDef(BaseValidatorModel):
    Sasl: Optional[SaslTypeDef] = None
    Tls: Optional[TlsExtraOutputTypeDef] = None
    Unauthenticated: Optional[UnauthenticatedTypeDef] = None

class ClientAuthenticationOutputTypeDef(BaseValidatorModel):
    Sasl: Optional[SaslTypeDef] = None
    Tls: Optional[TlsOutputTypeDef] = None
    Unauthenticated: Optional[UnauthenticatedTypeDef] = None

class ClientAuthenticationTypeDef(BaseValidatorModel):
    Sasl: Optional[SaslTypeDef] = None
    Tls: Optional[TlsTypeDef] = None
    Unauthenticated: Optional[UnauthenticatedTypeDef] = None

class ClusterOperationV2ServerlessTypeDef(BaseValidatorModel):
    VpcConnectionInfo: Optional[VpcConnectionInfoServerlessTypeDef] = None

class VpcConnectivityClientAuthenticationTypeDef(BaseValidatorModel):
    Sasl: Optional[VpcConnectivitySaslTypeDef] = None
    Tls: Optional[VpcConnectivityTlsTypeDef] = None

class ListReplicatorsResponseTypeDef(BaseValidatorModel):
    Replicators: List[ReplicatorSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListNodesResponseTypeDef(BaseValidatorModel):
    NodeInfoList: List[NodeInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ServerlessRequestTypeDef(BaseValidatorModel):
    VpcConfigs: Sequence[VpcConfigTypeDef]
    ClientAuthentication: Optional[ServerlessClientAuthenticationTypeDef] = None

class ServerlessTypeDef(BaseValidatorModel):
    VpcConfigs: List[VpcConfigOutputTypeDef]
    ClientAuthentication: Optional[ServerlessClientAuthenticationTypeDef] = None

class UpdateMonitoringRequestRequestTypeDef(BaseValidatorModel):
    ClusterArn: str
    CurrentVersion: str
    EnhancedMonitoring: Optional[EnhancedMonitoringType] = None
    OpenMonitoring: Optional[OpenMonitoringInfoTypeDef] = None
    LoggingInfo: Optional[LoggingInfoTypeDef] = None

class DescribeReplicatorResponseTypeDef(BaseValidatorModel):
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

class CreateReplicatorRequestRequestTypeDef(BaseValidatorModel):
    KafkaClusters: Sequence[KafkaClusterTypeDef]
    ReplicationInfoList: Sequence[ReplicationInfoTypeDef]
    ReplicatorName: str
    ServiceExecutionRoleArn: str
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class UpdateSecurityRequestRequestTypeDef(BaseValidatorModel):
    ClusterArn: str
    CurrentVersion: str
    ClientAuthentication: Optional[ClientAuthenticationTypeDef] = None
    EncryptionInfo: Optional[EncryptionInfoTypeDef] = None

class VpcConnectivityTypeDef(BaseValidatorModel):
    ClientAuthentication: Optional[VpcConnectivityClientAuthenticationTypeDef] = None

class ConnectivityInfoTypeDef(BaseValidatorModel):
    PublicAccess: Optional[PublicAccessTypeDef] = None
    VpcConnectivity: Optional[VpcConnectivityTypeDef] = None

class BrokerNodeGroupInfoExtraOutputTypeDef(BaseValidatorModel):
    ClientSubnets: List[str]
    InstanceType: str
    BrokerAZDistribution: Optional[Literal["DEFAULT"]] = None
    SecurityGroups: Optional[List[str]] = None
    StorageInfo: Optional[StorageInfoTypeDef] = None
    ConnectivityInfo: Optional[ConnectivityInfoTypeDef] = None
    ZoneIds: Optional[List[str]] = None

class BrokerNodeGroupInfoOutputTypeDef(BaseValidatorModel):
    ClientSubnets: List[str]
    InstanceType: str
    BrokerAZDistribution: Optional[Literal["DEFAULT"]] = None
    SecurityGroups: Optional[List[str]] = None
    StorageInfo: Optional[StorageInfoTypeDef] = None
    ConnectivityInfo: Optional[ConnectivityInfoTypeDef] = None
    ZoneIds: Optional[List[str]] = None

class BrokerNodeGroupInfoTypeDef(BaseValidatorModel):
    ClientSubnets: Sequence[str]
    InstanceType: str
    BrokerAZDistribution: Optional[Literal["DEFAULT"]] = None
    SecurityGroups: Optional[Sequence[str]] = None
    StorageInfo: Optional[StorageInfoTypeDef] = None
    ConnectivityInfo: Optional[ConnectivityInfoTypeDef] = None
    ZoneIds: Optional[Sequence[str]] = None

class MutableClusterInfoTypeDef(BaseValidatorModel):
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

class UpdateConnectivityRequestRequestTypeDef(BaseValidatorModel):
    ClusterArn: str
    ConnectivityInfo: ConnectivityInfoTypeDef
    CurrentVersion: str

class ClusterInfoTypeDef(BaseValidatorModel):
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

class ProvisionedTypeDef(BaseValidatorModel):
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

class CreateClusterRequestRequestTypeDef(BaseValidatorModel):
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

class ProvisionedRequestTypeDef(BaseValidatorModel):
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

class ClusterOperationInfoTypeDef(BaseValidatorModel):
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

class ClusterOperationV2ProvisionedTypeDef(BaseValidatorModel):
    OperationSteps: Optional[List[ClusterOperationStepTypeDef]] = None
    SourceClusterInfo: Optional[MutableClusterInfoTypeDef] = None
    TargetClusterInfo: Optional[MutableClusterInfoTypeDef] = None
    VpcConnectionInfo: Optional[VpcConnectionInfoTypeDef] = None

class DescribeClusterResponseTypeDef(BaseValidatorModel):
    ClusterInfo: ClusterInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListClustersResponseTypeDef(BaseValidatorModel):
    ClusterInfoList: List[ClusterInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ClusterTypeDef(BaseValidatorModel):
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

class CreateClusterV2RequestRequestTypeDef(BaseValidatorModel):
    ClusterName: str
    Tags: Optional[Mapping[str, str]] = None
    Provisioned: Optional[ProvisionedRequestTypeDef] = None
    Serverless: Optional[ServerlessRequestTypeDef] = None

class DescribeClusterOperationResponseTypeDef(BaseValidatorModel):
    ClusterOperationInfo: ClusterOperationInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListClusterOperationsResponseTypeDef(BaseValidatorModel):
    ClusterOperationInfoList: List[ClusterOperationInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ClusterOperationV2TypeDef(BaseValidatorModel):
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

class DescribeClusterV2ResponseTypeDef(BaseValidatorModel):
    ClusterInfo: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListClustersV2ResponseTypeDef(BaseValidatorModel):
    ClusterInfoList: List[ClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeClusterOperationV2ResponseTypeDef(BaseValidatorModel):
    ClusterOperationInfo: ClusterOperationV2TypeDef
    ResponseMetadata: ResponseMetadataTypeDef


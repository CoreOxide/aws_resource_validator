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
from aws_resource_validator.pydantic_models.kafka_constants import *

class AmazonMskCluster(BaseValidatorModel):
    MskClusterArn: str


class BatchAssociateScramSecretRequest(BaseValidatorModel):
    ClusterArn: str
    SecretArnList: Sequence[str]


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class UnprocessedScramSecret(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None
    SecretArn: Optional[str] = None


class BatchDisassociateScramSecretRequest(BaseValidatorModel):
    ClusterArn: str
    SecretArnList: Sequence[str]


class BrokerCountUpdateInfo(BaseValidatorModel):
    CreatedBrokerIds: Optional[List[float]] = None
    DeletedBrokerIds: Optional[List[float]] = None


class ProvisionedThroughput(BaseValidatorModel):
    Enabled: Optional[bool] = None
    VolumeThroughput: Optional[int] = None


class CloudWatchLogs(BaseValidatorModel):
    Enabled: bool
    LogGroup: Optional[str] = None


class Firehose(BaseValidatorModel):
    Enabled: bool
    DeliveryStream: Optional[str] = None


class S3(BaseValidatorModel):
    Enabled: bool
    Bucket: Optional[str] = None
    Prefix: Optional[str] = None


class BrokerSoftwareInfo(BaseValidatorModel):
    ConfigurationArn: Optional[str] = None
    ConfigurationRevision: Optional[int] = None
    KafkaVersion: Optional[str] = None


class TlsOutput(BaseValidatorModel):
    CertificateAuthorityArnList: Optional[List[str]] = None
    Enabled: Optional[bool] = None


class Unauthenticated(BaseValidatorModel):
    Enabled: Optional[bool] = None


class ClientVpcConnection(BaseValidatorModel):
    VpcConnectionArn: str
    Authentication: Optional[str] = None
    CreationTime: Optional[datetime] = None
    State: Optional[VpcConnectionStateType] = None
    Owner: Optional[str] = None


class StateInfo(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None


class ErrorInfo(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorString: Optional[str] = None


class ClusterOperationStepInfo(BaseValidatorModel):
    StepStatus: Optional[str] = None


class ClusterOperationV2Summary(BaseValidatorModel):
    ClusterArn: Optional[str] = None
    ClusterType: Optional[ClusterTypeType] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    OperationArn: Optional[str] = None
    OperationState: Optional[str] = None
    OperationType: Optional[str] = None


class CompatibleKafkaVersion(BaseValidatorModel):
    SourceVersion: Optional[str] = None
    TargetVersions: Optional[List[str]] = None


class ConfigurationInfo(BaseValidatorModel):
    Arn: str
    Revision: int


class ConfigurationRevision(BaseValidatorModel):
    CreationTime: datetime
    Revision: int
    Description: Optional[str] = None


class ConsumerGroupReplicationOutput(BaseValidatorModel):
    ConsumerGroupsToReplicate: List[str]
    ConsumerGroupsToExclude: Optional[List[str]] = None
    DetectAndCopyNewConsumerGroups: Optional[bool] = None
    SynchroniseConsumerGroupOffsets: Optional[bool] = None


class ConsumerGroupReplication(BaseValidatorModel):
    ConsumerGroupsToReplicate: Sequence[str]
    ConsumerGroupsToExclude: Optional[Sequence[str]] = None
    DetectAndCopyNewConsumerGroups: Optional[bool] = None
    SynchroniseConsumerGroupOffsets: Optional[bool] = None


class ConsumerGroupReplicationUpdate(BaseValidatorModel):
    ConsumerGroupsToExclude: Sequence[str]
    ConsumerGroupsToReplicate: Sequence[str]
    DetectAndCopyNewConsumerGroups: bool
    SynchroniseConsumerGroupOffsets: bool


class ControllerNodeInfo(BaseValidatorModel):
    Endpoints: Optional[List[str]] = None


class CreateVpcConnectionRequest(BaseValidatorModel):
    TargetClusterArn: str
    Authentication: str
    VpcId: str
    ClientSubnets: Sequence[str]
    SecurityGroups: Sequence[str]
    Tags: Optional[Mapping[str, str]] = None


class DeleteClusterPolicyRequest(BaseValidatorModel):
    ClusterArn: str


class DeleteClusterRequest(BaseValidatorModel):
    ClusterArn: str
    CurrentVersion: Optional[str] = None


class DeleteConfigurationRequest(BaseValidatorModel):
    Arn: str


class DeleteReplicatorRequest(BaseValidatorModel):
    ReplicatorArn: str
    CurrentVersion: Optional[str] = None


class DeleteVpcConnectionRequest(BaseValidatorModel):
    Arn: str


class DescribeClusterOperationRequest(BaseValidatorModel):
    ClusterOperationArn: str


class DescribeClusterOperationV2Request(BaseValidatorModel):
    ClusterOperationArn: str


class DescribeClusterRequest(BaseValidatorModel):
    ClusterArn: str


class DescribeClusterV2Request(BaseValidatorModel):
    ClusterArn: str


class DescribeConfigurationRequest(BaseValidatorModel):
    Arn: str


class DescribeConfigurationRevisionRequest(BaseValidatorModel):
    Arn: str
    Revision: int


class DescribeReplicatorRequest(BaseValidatorModel):
    ReplicatorArn: str


class ReplicationStateInfo(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None


class DescribeVpcConnectionRequest(BaseValidatorModel):
    Arn: str


class EncryptionAtRest(BaseValidatorModel):
    DataVolumeKMSKeyId: str


class EncryptionInTransit(BaseValidatorModel):
    ClientBroker: Optional[ClientBrokerType] = None
    InCluster: Optional[bool] = None


class GetBootstrapBrokersRequest(BaseValidatorModel):
    ClusterArn: str


class GetClusterPolicyRequest(BaseValidatorModel):
    ClusterArn: str


class GetCompatibleKafkaVersionsRequest(BaseValidatorModel):
    ClusterArn: Optional[str] = None


class Iam(BaseValidatorModel):
    Enabled: Optional[bool] = None


class JmxExporterInfo(BaseValidatorModel):
    EnabledInBroker: bool


class JmxExporter(BaseValidatorModel):
    EnabledInBroker: bool


class KafkaClusterClientVpcConfigOutput(BaseValidatorModel):
    SubnetIds: List[str]
    SecurityGroupIds: Optional[List[str]] = None


class KafkaClusterClientVpcConfig(BaseValidatorModel):
    SubnetIds: Sequence[str]
    SecurityGroupIds: Optional[Sequence[str]] = None


class KafkaVersion(BaseValidatorModel):
    Version: Optional[str] = None
    Status: Optional[KafkaVersionStatusType] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListClientVpcConnectionsRequest(BaseValidatorModel):
    ClusterArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListClusterOperationsRequest(BaseValidatorModel):
    ClusterArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListClusterOperationsV2Request(BaseValidatorModel):
    ClusterArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListClustersRequest(BaseValidatorModel):
    ClusterNameFilter: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListClustersV2Request(BaseValidatorModel):
    ClusterNameFilter: Optional[str] = None
    ClusterTypeFilter: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListConfigurationRevisionsRequest(BaseValidatorModel):
    Arn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListConfigurationsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListKafkaVersionsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListNodesRequest(BaseValidatorModel):
    ClusterArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListReplicatorsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ReplicatorNameFilter: Optional[str] = None


class ListScramSecretsRequest(BaseValidatorModel):
    ClusterArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class ListVpcConnectionsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class VpcConnection(BaseValidatorModel):
    VpcConnectionArn: str
    TargetClusterArn: str
    CreationTime: Optional[datetime] = None
    Authentication: Optional[str] = None
    VpcId: Optional[str] = None
    State: Optional[VpcConnectionStateType] = None


class NodeExporterInfo(BaseValidatorModel):
    EnabledInBroker: bool


class NodeExporter(BaseValidatorModel):
    EnabledInBroker: bool


class ZookeeperNodeInfo(BaseValidatorModel):
    AttachedENIId: Optional[str] = None
    ClientVpcIpAddress: Optional[str] = None
    Endpoints: Optional[List[str]] = None
    ZookeeperId: Optional[float] = None
    ZookeeperVersion: Optional[str] = None


class PutClusterPolicyRequest(BaseValidatorModel):
    ClusterArn: str
    Policy: str
    CurrentVersion: Optional[str] = None


class RebootBrokerRequest(BaseValidatorModel):
    BrokerIds: Sequence[str]
    ClusterArn: str


class RejectClientVpcConnectionRequest(BaseValidatorModel):
    ClusterArn: str
    VpcConnectionArn: str


class ReplicationInfoSummary(BaseValidatorModel):
    SourceKafkaClusterAlias: Optional[str] = None
    TargetKafkaClusterAlias: Optional[str] = None


class Scram(BaseValidatorModel):
    Enabled: Optional[bool] = None


class VpcConfigOutput(BaseValidatorModel):
    SubnetIds: List[str]
    SecurityGroupIds: Optional[List[str]] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class Tls(BaseValidatorModel):
    CertificateAuthorityArnList: Optional[Sequence[str]] = None
    Enabled: Optional[bool] = None


class TopicReplicationUpdate(BaseValidatorModel):
    CopyAccessControlListsForTopics: bool
    CopyTopicConfigurations: bool
    DetectAndCopyNewTopics: bool
    TopicsToExclude: Sequence[str]
    TopicsToReplicate: Sequence[str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateBrokerCountRequest(BaseValidatorModel):
    ClusterArn: str
    CurrentVersion: str
    TargetNumberOfBrokerNodes: int


class UpdateBrokerTypeRequest(BaseValidatorModel):
    ClusterArn: str
    CurrentVersion: str
    TargetInstanceType: str


class VpcConfig(BaseValidatorModel):
    SubnetIds: Sequence[str]
    SecurityGroupIds: Optional[Sequence[str]] = None


class VpcConnectivityTls(BaseValidatorModel):
    Enabled: Optional[bool] = None


class VpcConnectivityIam(BaseValidatorModel):
    Enabled: Optional[bool] = None


class VpcConnectivityScram(BaseValidatorModel):
    Enabled: Optional[bool] = None


class KafkaClusterSummary(BaseValidatorModel):
    AmazonMskCluster: Optional[AmazonMskCluster] = None
    KafkaClusterAlias: Optional[str] = None


class CreateClusterResponse(BaseValidatorModel):
    ClusterArn: str
    ClusterName: str
    State: ClusterStateType
    ResponseMetadata: ResponseMetadata


class CreateClusterV2Response(BaseValidatorModel):
    ClusterArn: str
    ClusterName: str
    State: ClusterStateType
    ClusterType: ClusterTypeType
    ResponseMetadata: ResponseMetadata


class CreateReplicatorResponse(BaseValidatorModel):
    ReplicatorArn: str
    ReplicatorName: str
    ReplicatorState: ReplicatorStateType
    ResponseMetadata: ResponseMetadata


class CreateVpcConnectionResponse(BaseValidatorModel):
    VpcConnectionArn: str
    State: VpcConnectionStateType
    Authentication: str
    VpcId: str
    ClientSubnets: List[str]
    SecurityGroups: List[str]
    CreationTime: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class DeleteClusterResponse(BaseValidatorModel):
    ClusterArn: str
    State: ClusterStateType
    ResponseMetadata: ResponseMetadata


class DeleteConfigurationResponse(BaseValidatorModel):
    Arn: str
    State: ConfigurationStateType
    ResponseMetadata: ResponseMetadata


class DeleteReplicatorResponse(BaseValidatorModel):
    ReplicatorArn: str
    ReplicatorState: ReplicatorStateType
    ResponseMetadata: ResponseMetadata


class DeleteVpcConnectionResponse(BaseValidatorModel):
    VpcConnectionArn: str
    State: VpcConnectionStateType
    ResponseMetadata: ResponseMetadata


class DescribeConfigurationRevisionResponse(BaseValidatorModel):
    Arn: str
    CreationTime: datetime
    Description: str
    Revision: int
    ServerProperties: bytes
    ResponseMetadata: ResponseMetadata


class DescribeVpcConnectionResponse(BaseValidatorModel):
    VpcConnectionArn: str
    TargetClusterArn: str
    State: VpcConnectionStateType
    Authentication: str
    VpcId: str
    Subnets: List[str]
    SecurityGroups: List[str]
    CreationTime: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetBootstrapBrokersResponse(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadata


class GetClusterPolicyResponse(BaseValidatorModel):
    CurrentVersion: str
    Policy: str
    ResponseMetadata: ResponseMetadata


class ListScramSecretsResponse(BaseValidatorModel):
    SecretArnList: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class PutClusterPolicyResponse(BaseValidatorModel):
    CurrentVersion: str
    ResponseMetadata: ResponseMetadata


class RebootBrokerResponse(BaseValidatorModel):
    ClusterArn: str
    ClusterOperationArn: str
    ResponseMetadata: ResponseMetadata


class UpdateBrokerCountResponse(BaseValidatorModel):
    ClusterArn: str
    ClusterOperationArn: str
    ResponseMetadata: ResponseMetadata


class UpdateBrokerStorageResponse(BaseValidatorModel):
    ClusterArn: str
    ClusterOperationArn: str
    ResponseMetadata: ResponseMetadata


class UpdateBrokerTypeResponse(BaseValidatorModel):
    ClusterArn: str
    ClusterOperationArn: str
    ResponseMetadata: ResponseMetadata


class UpdateClusterConfigurationResponse(BaseValidatorModel):
    ClusterArn: str
    ClusterOperationArn: str
    ResponseMetadata: ResponseMetadata


class UpdateClusterKafkaVersionResponse(BaseValidatorModel):
    ClusterArn: str
    ClusterOperationArn: str
    ResponseMetadata: ResponseMetadata


class UpdateConnectivityResponse(BaseValidatorModel):
    ClusterArn: str
    ClusterOperationArn: str
    ResponseMetadata: ResponseMetadata


class UpdateMonitoringResponse(BaseValidatorModel):
    ClusterArn: str
    ClusterOperationArn: str
    ResponseMetadata: ResponseMetadata


class UpdateReplicationInfoResponse(BaseValidatorModel):
    ReplicatorArn: str
    ReplicatorState: ReplicatorStateType
    ResponseMetadata: ResponseMetadata


class UpdateSecurityResponse(BaseValidatorModel):
    ClusterArn: str
    ClusterOperationArn: str
    ResponseMetadata: ResponseMetadata


class UpdateStorageResponse(BaseValidatorModel):
    ClusterArn: str
    ClusterOperationArn: str
    ResponseMetadata: ResponseMetadata


class BatchAssociateScramSecretResponse(BaseValidatorModel):
    ClusterArn: str
    UnprocessedScramSecrets: List[UnprocessedScramSecret]
    ResponseMetadata: ResponseMetadata


class BatchDisassociateScramSecretResponse(BaseValidatorModel):
    ClusterArn: str
    UnprocessedScramSecrets: List[UnprocessedScramSecret]
    ResponseMetadata: ResponseMetadata


class Blob(BaseValidatorModel):
    pass


class CreateConfigurationRequest(BaseValidatorModel):
    Name: str
    ServerProperties: Blob
    Description: Optional[str] = None
    KafkaVersions: Optional[Sequence[str]] = None


class UpdateConfigurationRequest(BaseValidatorModel):
    Arn: str
    ServerProperties: Blob
    Description: Optional[str] = None


class BrokerEBSVolumeInfo(BaseValidatorModel):
    KafkaBrokerNodeId: str
    ProvisionedThroughput: Optional[ProvisionedThroughput] = None
    VolumeSizeGB: Optional[int] = None


class EBSStorageInfo(BaseValidatorModel):
    ProvisionedThroughput: Optional[ProvisionedThroughput] = None
    VolumeSize: Optional[int] = None


class UpdateStorageRequest(BaseValidatorModel):
    ClusterArn: str
    CurrentVersion: str
    ProvisionedThroughput: Optional[ProvisionedThroughput] = None
    StorageMode: Optional[StorageModeType] = None
    VolumeSizeGB: Optional[int] = None


class BrokerLogs(BaseValidatorModel):
    CloudWatchLogs: Optional[CloudWatchLogs] = None
    Firehose: Optional[Firehose] = None
    S3: Optional[S3] = None


class BrokerNodeInfo(BaseValidatorModel):
    AttachedENIId: Optional[str] = None
    BrokerId: Optional[float] = None
    ClientSubnet: Optional[str] = None
    ClientVpcIpAddress: Optional[str] = None
    CurrentBrokerSoftwareInfo: Optional[BrokerSoftwareInfo] = None
    Endpoints: Optional[List[str]] = None


class ListClientVpcConnectionsResponse(BaseValidatorModel):
    ClientVpcConnections: List[ClientVpcConnection]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ClusterOperationStep(BaseValidatorModel):
    StepInfo: Optional[ClusterOperationStepInfo] = None
    StepName: Optional[str] = None


class ListClusterOperationsV2Response(BaseValidatorModel):
    ClusterOperationInfoList: List[ClusterOperationV2Summary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetCompatibleKafkaVersionsResponse(BaseValidatorModel):
    CompatibleKafkaVersions: List[CompatibleKafkaVersion]
    ResponseMetadata: ResponseMetadata


class UpdateClusterConfigurationRequest(BaseValidatorModel):
    ClusterArn: str
    ConfigurationInfo: ConfigurationInfo
    CurrentVersion: str


class UpdateClusterKafkaVersionRequest(BaseValidatorModel):
    ClusterArn: str
    CurrentVersion: str
    TargetKafkaVersion: str
    ConfigurationInfo: Optional[ConfigurationInfo] = None


class Configuration(BaseValidatorModel):
    Arn: str
    CreationTime: datetime
    Description: str
    KafkaVersions: List[str]
    LatestRevision: ConfigurationRevision
    Name: str
    State: ConfigurationStateType


class CreateConfigurationResponse(BaseValidatorModel):
    Arn: str
    CreationTime: datetime
    LatestRevision: ConfigurationRevision
    Name: str
    State: ConfigurationStateType
    ResponseMetadata: ResponseMetadata


class DescribeConfigurationResponse(BaseValidatorModel):
    Arn: str
    CreationTime: datetime
    Description: str
    KafkaVersions: List[str]
    LatestRevision: ConfigurationRevision
    Name: str
    State: ConfigurationStateType
    ResponseMetadata: ResponseMetadata


class ListConfigurationRevisionsResponse(BaseValidatorModel):
    Revisions: List[ConfigurationRevision]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateConfigurationResponse(BaseValidatorModel):
    Arn: str
    LatestRevision: ConfigurationRevision
    ResponseMetadata: ResponseMetadata


class EncryptionInfo(BaseValidatorModel):
    EncryptionAtRest: Optional[EncryptionAtRest] = None
    EncryptionInTransit: Optional[EncryptionInTransit] = None


class ServerlessSasl(BaseValidatorModel):
    Iam: Optional[Iam] = None


class KafkaClusterDescription(BaseValidatorModel):
    AmazonMskCluster: Optional[AmazonMskCluster] = None
    KafkaClusterAlias: Optional[str] = None
    VpcConfig: Optional[KafkaClusterClientVpcConfigOutput] = None


class ListKafkaVersionsResponse(BaseValidatorModel):
    KafkaVersions: List[KafkaVersion]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListClientVpcConnectionsRequestPaginate(BaseValidatorModel):
    ClusterArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListClusterOperationsRequestPaginate(BaseValidatorModel):
    ClusterArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListClusterOperationsV2RequestPaginate(BaseValidatorModel):
    ClusterArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListClustersRequestPaginate(BaseValidatorModel):
    ClusterNameFilter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListClustersV2RequestPaginate(BaseValidatorModel):
    ClusterNameFilter: Optional[str] = None
    ClusterTypeFilter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListConfigurationRevisionsRequestPaginate(BaseValidatorModel):
    Arn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListConfigurationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListKafkaVersionsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListNodesRequestPaginate(BaseValidatorModel):
    ClusterArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListReplicatorsRequestPaginate(BaseValidatorModel):
    ReplicatorNameFilter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListScramSecretsRequestPaginate(BaseValidatorModel):
    ClusterArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListVpcConnectionsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListVpcConnectionsResponse(BaseValidatorModel):
    VpcConnections: List[VpcConnection]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PrometheusInfo(BaseValidatorModel):
    JmxExporter: Optional[JmxExporterInfo] = None
    NodeExporter: Optional[NodeExporterInfo] = None


class Prometheus(BaseValidatorModel):
    JmxExporter: Optional[JmxExporter] = None
    NodeExporter: Optional[NodeExporter] = None


class ReplicationStartingPosition(BaseValidatorModel):
    pass


class ReplicationTopicNameConfiguration(BaseValidatorModel):
    pass


class TopicReplicationOutput(BaseValidatorModel):
    TopicsToReplicate: List[str]
    CopyAccessControlListsForTopics: Optional[bool] = None
    CopyTopicConfigurations: Optional[bool] = None
    DetectAndCopyNewTopics: Optional[bool] = None
    StartingPosition: Optional[ReplicationStartingPosition] = None
    TopicNameConfiguration: Optional[ReplicationTopicNameConfiguration] = None
    TopicsToExclude: Optional[List[str]] = None


class TopicReplication(BaseValidatorModel):
    TopicsToReplicate: Sequence[str]
    CopyAccessControlListsForTopics: Optional[bool] = None
    CopyTopicConfigurations: Optional[bool] = None
    DetectAndCopyNewTopics: Optional[bool] = None
    StartingPosition: Optional[ReplicationStartingPosition] = None
    TopicNameConfiguration: Optional[ReplicationTopicNameConfiguration] = None
    TopicsToExclude: Optional[Sequence[str]] = None


class Sasl(BaseValidatorModel):
    Scram: Optional[Scram] = None
    Iam: Optional[Iam] = None


class UpdateReplicationInfoRequest(BaseValidatorModel):
    CurrentVersion: str
    ReplicatorArn: str
    SourceKafkaClusterArn: str
    TargetKafkaClusterArn: str
    ConsumerGroupReplication: Optional[ConsumerGroupReplicationUpdate] = None
    TopicReplication: Optional[TopicReplicationUpdate] = None


class UserIdentity(BaseValidatorModel):
    pass


class VpcConnectionInfoServerless(BaseValidatorModel):
    CreationTime: Optional[datetime] = None
    Owner: Optional[str] = None
    UserIdentity: Optional[UserIdentity] = None
    VpcConnectionArn: Optional[str] = None


class VpcConnectionInfo(BaseValidatorModel):
    VpcConnectionArn: Optional[str] = None
    Owner: Optional[str] = None
    UserIdentity: Optional[UserIdentity] = None
    CreationTime: Optional[datetime] = None


class VpcConnectivitySasl(BaseValidatorModel):
    Scram: Optional[VpcConnectivityScram] = None
    Iam: Optional[VpcConnectivityIam] = None


class ReplicatorSummary(BaseValidatorModel):
    CreationTime: Optional[datetime] = None
    CurrentVersion: Optional[str] = None
    IsReplicatorReference: Optional[bool] = None
    KafkaClustersSummary: Optional[List[KafkaClusterSummary]] = None
    ReplicationInfoSummaryList: Optional[List[ReplicationInfoSummary]] = None
    ReplicatorArn: Optional[str] = None
    ReplicatorName: Optional[str] = None
    ReplicatorResourceArn: Optional[str] = None
    ReplicatorState: Optional[ReplicatorStateType] = None


class UpdateBrokerStorageRequest(BaseValidatorModel):
    ClusterArn: str
    CurrentVersion: str
    TargetBrokerEBSVolumeInfo: Sequence[BrokerEBSVolumeInfo]


class StorageInfo(BaseValidatorModel):
    EbsStorageInfo: Optional[EBSStorageInfo] = None


class LoggingInfo(BaseValidatorModel):
    BrokerLogs: BrokerLogs


class NodeInfo(BaseValidatorModel):
    AddedToClusterTime: Optional[str] = None
    BrokerNodeInfo: Optional[BrokerNodeInfo] = None
    ControllerNodeInfo: Optional[ControllerNodeInfo] = None
    InstanceType: Optional[str] = None
    NodeARN: Optional[str] = None
    NodeType: Optional[Literal["BROKER"]] = None
    ZookeeperNodeInfo: Optional[ZookeeperNodeInfo] = None


class ListConfigurationsResponse(BaseValidatorModel):
    Configurations: List[Configuration]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ServerlessClientAuthentication(BaseValidatorModel):
    Sasl: Optional[ServerlessSasl] = None


class KafkaClusterClientVpcConfigUnion(BaseValidatorModel):
    pass


class KafkaCluster(BaseValidatorModel):
    AmazonMskCluster: AmazonMskCluster
    VpcConfig: KafkaClusterClientVpcConfigUnion


class OpenMonitoringInfo(BaseValidatorModel):
    Prometheus: PrometheusInfo


class OpenMonitoring(BaseValidatorModel):
    Prometheus: Prometheus


class ReplicationInfoDescription(BaseValidatorModel):
    ConsumerGroupReplication: Optional[ConsumerGroupReplicationOutput] = None
    SourceKafkaClusterAlias: Optional[str] = None
    TargetCompressionType: Optional[TargetCompressionTypeType] = None
    TargetKafkaClusterAlias: Optional[str] = None
    TopicReplication: Optional[TopicReplicationOutput] = None


class ClientAuthenticationOutput(BaseValidatorModel):
    Sasl: Optional[Sasl] = None
    Tls: Optional[TlsOutput] = None
    Unauthenticated: Optional[Unauthenticated] = None


class TlsUnion(BaseValidatorModel):
    pass


class ClientAuthentication(BaseValidatorModel):
    Sasl: Optional[Sasl] = None
    Tls: Optional[TlsUnion] = None
    Unauthenticated: Optional[Unauthenticated] = None


class ClusterOperationV2Serverless(BaseValidatorModel):
    VpcConnectionInfo: Optional[VpcConnectionInfoServerless] = None


class VpcConnectivityClientAuthentication(BaseValidatorModel):
    Sasl: Optional[VpcConnectivitySasl] = None
    Tls: Optional[VpcConnectivityTls] = None


class ListReplicatorsResponse(BaseValidatorModel):
    Replicators: List[ReplicatorSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListNodesResponse(BaseValidatorModel):
    NodeInfoList: List[NodeInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class VpcConfigUnion(BaseValidatorModel):
    pass


class ServerlessRequest(BaseValidatorModel):
    VpcConfigs: Sequence[VpcConfigUnion]
    ClientAuthentication: Optional[ServerlessClientAuthentication] = None


class Serverless(BaseValidatorModel):
    VpcConfigs: List[VpcConfigOutput]
    ClientAuthentication: Optional[ServerlessClientAuthentication] = None


class UpdateMonitoringRequest(BaseValidatorModel):
    ClusterArn: str
    CurrentVersion: str
    EnhancedMonitoring: Optional[EnhancedMonitoringType] = None
    OpenMonitoring: Optional[OpenMonitoringInfo] = None
    LoggingInfo: Optional[LoggingInfo] = None


class DescribeReplicatorResponse(BaseValidatorModel):
    CreationTime: datetime
    CurrentVersion: str
    IsReplicatorReference: bool
    KafkaClusters: List[KafkaClusterDescription]
    ReplicationInfoList: List[ReplicationInfoDescription]
    ReplicatorArn: str
    ReplicatorDescription: str
    ReplicatorName: str
    ReplicatorResourceArn: str
    ReplicatorState: ReplicatorStateType
    ServiceExecutionRoleArn: str
    StateInfo: ReplicationStateInfo
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class TopicReplicationUnion(BaseValidatorModel):
    pass


class ConsumerGroupReplicationUnion(BaseValidatorModel):
    pass


class ReplicationInfo(BaseValidatorModel):
    ConsumerGroupReplication: ConsumerGroupReplicationUnion
    SourceKafkaClusterArn: str
    TargetCompressionType: TargetCompressionTypeType
    TargetKafkaClusterArn: str
    TopicReplication: TopicReplicationUnion


class VpcConnectivity(BaseValidatorModel):
    ClientAuthentication: Optional[VpcConnectivityClientAuthentication] = None


class CreateReplicatorRequest(BaseValidatorModel):
    KafkaClusters: Sequence[KafkaCluster]
    ReplicationInfoList: Sequence[ReplicationInfo]
    ReplicatorName: str
    ServiceExecutionRoleArn: str
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class ClientAuthenticationUnion(BaseValidatorModel):
    pass


class UpdateSecurityRequest(BaseValidatorModel):
    ClusterArn: str
    CurrentVersion: str
    ClientAuthentication: Optional[ClientAuthenticationUnion] = None
    EncryptionInfo: Optional[EncryptionInfo] = None


class PublicAccess(BaseValidatorModel):
    pass


class ConnectivityInfo(BaseValidatorModel):
    PublicAccess: Optional[PublicAccess] = None
    VpcConnectivity: Optional[VpcConnectivity] = None


class BrokerNodeGroupInfoOutput(BaseValidatorModel):
    ClientSubnets: List[str]
    InstanceType: str
    BrokerAZDistribution: Optional[Literal["DEFAULT"]] = None
    SecurityGroups: Optional[List[str]] = None
    StorageInfo: Optional[StorageInfo] = None
    ConnectivityInfo: Optional[ConnectivityInfo] = None
    ZoneIds: Optional[List[str]] = None


class BrokerNodeGroupInfo(BaseValidatorModel):
    ClientSubnets: Sequence[str]
    InstanceType: str
    BrokerAZDistribution: Optional[Literal["DEFAULT"]] = None
    SecurityGroups: Optional[Sequence[str]] = None
    StorageInfo: Optional[StorageInfo] = None
    ConnectivityInfo: Optional[ConnectivityInfo] = None
    ZoneIds: Optional[Sequence[str]] = None


class MutableClusterInfo(BaseValidatorModel):
    BrokerEBSVolumeInfo: Optional[List[BrokerEBSVolumeInfo]] = None
    ConfigurationInfo: Optional[ConfigurationInfo] = None
    NumberOfBrokerNodes: Optional[int] = None
    EnhancedMonitoring: Optional[EnhancedMonitoringType] = None
    OpenMonitoring: Optional[OpenMonitoring] = None
    KafkaVersion: Optional[str] = None
    LoggingInfo: Optional[LoggingInfo] = None
    InstanceType: Optional[str] = None
    ClientAuthentication: Optional[ClientAuthenticationOutput] = None
    EncryptionInfo: Optional[EncryptionInfo] = None
    ConnectivityInfo: Optional[ConnectivityInfo] = None
    StorageMode: Optional[StorageModeType] = None
    BrokerCountUpdateInfo: Optional[BrokerCountUpdateInfo] = None


class UpdateConnectivityRequest(BaseValidatorModel):
    ClusterArn: str
    ConnectivityInfo: ConnectivityInfo
    CurrentVersion: str


class ClusterInfo(BaseValidatorModel):
    ActiveOperationArn: Optional[str] = None
    BrokerNodeGroupInfo: Optional[BrokerNodeGroupInfoOutput] = None
    ClientAuthentication: Optional[ClientAuthenticationOutput] = None
    ClusterArn: Optional[str] = None
    ClusterName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    CurrentBrokerSoftwareInfo: Optional[BrokerSoftwareInfo] = None
    CurrentVersion: Optional[str] = None
    EncryptionInfo: Optional[EncryptionInfo] = None
    EnhancedMonitoring: Optional[EnhancedMonitoringType] = None
    OpenMonitoring: Optional[OpenMonitoring] = None
    LoggingInfo: Optional[LoggingInfo] = None
    NumberOfBrokerNodes: Optional[int] = None
    State: Optional[ClusterStateType] = None
    StateInfo: Optional[StateInfo] = None
    Tags: Optional[Dict[str, str]] = None
    ZookeeperConnectString: Optional[str] = None
    ZookeeperConnectStringTls: Optional[str] = None
    StorageMode: Optional[StorageModeType] = None
    CustomerActionStatus: Optional[CustomerActionStatusType] = None


class Provisioned(BaseValidatorModel):
    BrokerNodeGroupInfo: BrokerNodeGroupInfoOutput
    NumberOfBrokerNodes: int
    CurrentBrokerSoftwareInfo: Optional[BrokerSoftwareInfo] = None
    ClientAuthentication: Optional[ClientAuthenticationOutput] = None
    EncryptionInfo: Optional[EncryptionInfo] = None
    EnhancedMonitoring: Optional[EnhancedMonitoringType] = None
    OpenMonitoring: Optional[OpenMonitoringInfo] = None
    LoggingInfo: Optional[LoggingInfo] = None
    ZookeeperConnectString: Optional[str] = None
    ZookeeperConnectStringTls: Optional[str] = None
    StorageMode: Optional[StorageModeType] = None
    CustomerActionStatus: Optional[CustomerActionStatusType] = None


class ClusterOperationInfo(BaseValidatorModel):
    ClientRequestId: Optional[str] = None
    ClusterArn: Optional[str] = None
    CreationTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    ErrorInfo: Optional[ErrorInfo] = None
    OperationArn: Optional[str] = None
    OperationState: Optional[str] = None
    OperationSteps: Optional[List[ClusterOperationStep]] = None
    OperationType: Optional[str] = None
    SourceClusterInfo: Optional[MutableClusterInfo] = None
    TargetClusterInfo: Optional[MutableClusterInfo] = None
    VpcConnectionInfo: Optional[VpcConnectionInfo] = None


class ClusterOperationV2Provisioned(BaseValidatorModel):
    OperationSteps: Optional[List[ClusterOperationStep]] = None
    SourceClusterInfo: Optional[MutableClusterInfo] = None
    TargetClusterInfo: Optional[MutableClusterInfo] = None
    VpcConnectionInfo: Optional[VpcConnectionInfo] = None


class DescribeClusterResponse(BaseValidatorModel):
    ClusterInfo: ClusterInfo
    ResponseMetadata: ResponseMetadata


class ListClustersResponse(BaseValidatorModel):
    ClusterInfoList: List[ClusterInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Cluster(BaseValidatorModel):
    ActiveOperationArn: Optional[str] = None
    ClusterType: Optional[ClusterTypeType] = None
    ClusterArn: Optional[str] = None
    ClusterName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    CurrentVersion: Optional[str] = None
    State: Optional[ClusterStateType] = None
    StateInfo: Optional[StateInfo] = None
    Tags: Optional[Dict[str, str]] = None
    Provisioned: Optional[Provisioned] = None
    Serverless: Optional[Serverless] = None


class BrokerNodeGroupInfoUnion(BaseValidatorModel):
    pass


class CreateClusterRequest(BaseValidatorModel):
    BrokerNodeGroupInfo: BrokerNodeGroupInfoUnion
    ClusterName: str
    KafkaVersion: str
    NumberOfBrokerNodes: int
    ClientAuthentication: Optional[ClientAuthenticationUnion] = None
    ConfigurationInfo: Optional[ConfigurationInfo] = None
    EncryptionInfo: Optional[EncryptionInfo] = None
    EnhancedMonitoring: Optional[EnhancedMonitoringType] = None
    OpenMonitoring: Optional[OpenMonitoringInfo] = None
    LoggingInfo: Optional[LoggingInfo] = None
    Tags: Optional[Mapping[str, str]] = None
    StorageMode: Optional[StorageModeType] = None


class ProvisionedRequest(BaseValidatorModel):
    BrokerNodeGroupInfo: BrokerNodeGroupInfoUnion
    KafkaVersion: str
    NumberOfBrokerNodes: int
    ClientAuthentication: Optional[ClientAuthenticationUnion] = None
    ConfigurationInfo: Optional[ConfigurationInfo] = None
    EncryptionInfo: Optional[EncryptionInfo] = None
    EnhancedMonitoring: Optional[EnhancedMonitoringType] = None
    OpenMonitoring: Optional[OpenMonitoringInfo] = None
    LoggingInfo: Optional[LoggingInfo] = None
    StorageMode: Optional[StorageModeType] = None


class DescribeClusterOperationResponse(BaseValidatorModel):
    ClusterOperationInfo: ClusterOperationInfo
    ResponseMetadata: ResponseMetadata


class ListClusterOperationsResponse(BaseValidatorModel):
    ClusterOperationInfoList: List[ClusterOperationInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ClusterOperationV2(BaseValidatorModel):
    ClusterArn: Optional[str] = None
    ClusterType: Optional[ClusterTypeType] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    ErrorInfo: Optional[ErrorInfo] = None
    OperationArn: Optional[str] = None
    OperationState: Optional[str] = None
    OperationType: Optional[str] = None
    Provisioned: Optional[ClusterOperationV2Provisioned] = None
    Serverless: Optional[ClusterOperationV2Serverless] = None


class DescribeClusterV2Response(BaseValidatorModel):
    ClusterInfo: Cluster
    ResponseMetadata: ResponseMetadata


class ListClustersV2Response(BaseValidatorModel):
    ClusterInfoList: List[Cluster]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateClusterV2Request(BaseValidatorModel):
    ClusterName: str
    Tags: Optional[Mapping[str, str]] = None
    Provisioned: Optional[ProvisionedRequest] = None
    Serverless: Optional[ServerlessRequest] = None


class DescribeClusterOperationV2Response(BaseValidatorModel):
    ClusterOperationInfo: ClusterOperationV2
    ResponseMetadata: ResponseMetadata



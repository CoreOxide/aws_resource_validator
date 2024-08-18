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
from aws_resource_validator.pydantic_models.managedblockchain_constants import *

class AccessorSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Type: Optional[Literal["BILLING_TOKEN"]] = None
    Status: Optional[AccessorStatusType] = None
    CreationDate: Optional[datetime] = None
    Arn: Optional[str] = None
    NetworkType: Optional[AccessorNetworkTypeType] = None

class AccessorTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Type: Optional[Literal["BILLING_TOKEN"]] = None
    BillingToken: Optional[str] = None
    Status: Optional[AccessorStatusType] = None
    CreationDate: Optional[datetime] = None
    Arn: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    NetworkType: Optional[AccessorNetworkTypeType] = None

class ApprovalThresholdPolicyTypeDef(BaseValidatorModel):
    ThresholdPercentage: Optional[int] = None
    ProposalDurationInHours: Optional[int] = None
    ThresholdComparator: Optional[ThresholdComparatorType] = None

class CreateAccessorInputRequestTypeDef(BaseValidatorModel):
    ClientRequestToken: str
    AccessorType: Literal["BILLING_TOKEN"]
    Tags: Optional[Mapping[str, str]] = None
    NetworkType: Optional[AccessorNetworkTypeType] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DeleteAccessorInputRequestTypeDef(BaseValidatorModel):
    AccessorId: str

class DeleteMemberInputRequestTypeDef(BaseValidatorModel):
    NetworkId: str
    MemberId: str

class DeleteNodeInputRequestTypeDef(BaseValidatorModel):
    NetworkId: str
    NodeId: str
    MemberId: Optional[str] = None

class GetAccessorInputRequestTypeDef(BaseValidatorModel):
    AccessorId: str

class GetMemberInputRequestTypeDef(BaseValidatorModel):
    NetworkId: str
    MemberId: str

class GetNetworkInputRequestTypeDef(BaseValidatorModel):
    NetworkId: str

class GetNodeInputRequestTypeDef(BaseValidatorModel):
    NetworkId: str
    NodeId: str
    MemberId: Optional[str] = None

class GetProposalInputRequestTypeDef(BaseValidatorModel):
    NetworkId: str
    ProposalId: str

class NetworkSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Framework: Optional[FrameworkType] = None
    FrameworkVersion: Optional[str] = None
    Status: Optional[NetworkStatusType] = None
    CreationDate: Optional[datetime] = None
    Arn: Optional[str] = None

class InviteActionTypeDef(BaseValidatorModel):
    Principal: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAccessorsInputRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    NetworkType: Optional[AccessorNetworkTypeType] = None

class ListInvitationsInputRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListMembersInputRequestTypeDef(BaseValidatorModel):
    NetworkId: str
    Name: Optional[str] = None
    Status: Optional[MemberStatusType] = None
    IsOwned: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class MemberSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[MemberStatusType] = None
    CreationDate: Optional[datetime] = None
    IsOwned: Optional[bool] = None
    Arn: Optional[str] = None

class ListNetworksInputRequestTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Framework: Optional[FrameworkType] = None
    Status: Optional[NetworkStatusType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListNodesInputRequestTypeDef(BaseValidatorModel):
    NetworkId: str
    MemberId: Optional[str] = None
    Status: Optional[NodeStatusType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class NodeSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Status: Optional[NodeStatusType] = None
    CreationDate: Optional[datetime] = None
    AvailabilityZone: Optional[str] = None
    InstanceType: Optional[str] = None
    Arn: Optional[str] = None

class ListProposalVotesInputRequestTypeDef(BaseValidatorModel):
    NetworkId: str
    ProposalId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class VoteSummaryTypeDef(BaseValidatorModel):
    Vote: Optional[VoteValueType] = None
    MemberName: Optional[str] = None
    MemberId: Optional[str] = None

class ListProposalsInputRequestTypeDef(BaseValidatorModel):
    NetworkId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ProposalSummaryTypeDef(BaseValidatorModel):
    ProposalId: Optional[str] = None
    Description: Optional[str] = None
    ProposedByMemberId: Optional[str] = None
    ProposedByMemberName: Optional[str] = None
    Status: Optional[ProposalStatusType] = None
    CreationDate: Optional[datetime] = None
    ExpirationDate: Optional[datetime] = None
    Arn: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class LogConfigurationTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None

class MemberFabricAttributesTypeDef(BaseValidatorModel):
    AdminUsername: Optional[str] = None
    CaEndpoint: Optional[str] = None

class MemberFabricConfigurationTypeDef(BaseValidatorModel):
    AdminUsername: str
    AdminPassword: str

class NetworkEthereumAttributesTypeDef(BaseValidatorModel):
    ChainId: Optional[str] = None

class NetworkFabricAttributesTypeDef(BaseValidatorModel):
    OrderingServiceEndpoint: Optional[str] = None
    Edition: Optional[EditionType] = None

class NetworkFabricConfigurationTypeDef(BaseValidatorModel):
    Edition: EditionType

class NodeEthereumAttributesTypeDef(BaseValidatorModel):
    HttpEndpoint: Optional[str] = None
    WebSocketEndpoint: Optional[str] = None

class NodeFabricAttributesTypeDef(BaseValidatorModel):
    PeerEndpoint: Optional[str] = None
    PeerEventEndpoint: Optional[str] = None

class RemoveActionTypeDef(BaseValidatorModel):
    MemberId: str

class RejectInvitationInputRequestTypeDef(BaseValidatorModel):
    InvitationId: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class VoteOnProposalInputRequestTypeDef(BaseValidatorModel):
    NetworkId: str
    ProposalId: str
    VoterMemberId: str
    Vote: VoteValueType

class VotingPolicyTypeDef(BaseValidatorModel):
    ApprovalThresholdPolicy: Optional[ApprovalThresholdPolicyTypeDef] = None

class CreateAccessorOutputTypeDef(BaseValidatorModel):
    AccessorId: str
    BillingToken: str
    NetworkType: AccessorNetworkTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMemberOutputTypeDef(BaseValidatorModel):
    MemberId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNetworkOutputTypeDef(BaseValidatorModel):
    NetworkId: str
    MemberId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNodeOutputTypeDef(BaseValidatorModel):
    NodeId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProposalOutputTypeDef(BaseValidatorModel):
    ProposalId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccessorOutputTypeDef(BaseValidatorModel):
    Accessor: AccessorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccessorsOutputTypeDef(BaseValidatorModel):
    Accessors: List[AccessorSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class InvitationTypeDef(BaseValidatorModel):
    InvitationId: Optional[str] = None
    CreationDate: Optional[datetime] = None
    ExpirationDate: Optional[datetime] = None
    Status: Optional[InvitationStatusType] = None
    NetworkSummary: Optional[NetworkSummaryTypeDef] = None
    Arn: Optional[str] = None

class ListNetworksOutputTypeDef(BaseValidatorModel):
    Networks: List[NetworkSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListAccessorsInputListAccessorsPaginateTypeDef(BaseValidatorModel):
    NetworkType: Optional[AccessorNetworkTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMembersOutputTypeDef(BaseValidatorModel):
    Members: List[MemberSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListNodesOutputTypeDef(BaseValidatorModel):
    Nodes: List[NodeSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListProposalVotesOutputTypeDef(BaseValidatorModel):
    ProposalVotes: List[VoteSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListProposalsOutputTypeDef(BaseValidatorModel):
    Proposals: List[ProposalSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class LogConfigurationsTypeDef(BaseValidatorModel):
    Cloudwatch: Optional[LogConfigurationTypeDef] = None

class MemberFrameworkAttributesTypeDef(BaseValidatorModel):
    Fabric: Optional[MemberFabricAttributesTypeDef] = None

class MemberFrameworkConfigurationTypeDef(BaseValidatorModel):
    Fabric: Optional[MemberFabricConfigurationTypeDef] = None

class NetworkFrameworkAttributesTypeDef(BaseValidatorModel):
    Fabric: Optional[NetworkFabricAttributesTypeDef] = None
    Ethereum: Optional[NetworkEthereumAttributesTypeDef] = None

class NetworkFrameworkConfigurationTypeDef(BaseValidatorModel):
    Fabric: Optional[NetworkFabricConfigurationTypeDef] = None

class NodeFrameworkAttributesTypeDef(BaseValidatorModel):
    Fabric: Optional[NodeFabricAttributesTypeDef] = None
    Ethereum: Optional[NodeEthereumAttributesTypeDef] = None

class ProposalActionsOutputTypeDef(BaseValidatorModel):
    Invitations: Optional[List[InviteActionTypeDef]] = None
    Removals: Optional[List[RemoveActionTypeDef]] = None

class ProposalActionsTypeDef(BaseValidatorModel):
    Invitations: Optional[Sequence[InviteActionTypeDef]] = None
    Removals: Optional[Sequence[RemoveActionTypeDef]] = None

class ListInvitationsOutputTypeDef(BaseValidatorModel):
    Invitations: List[InvitationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class MemberFabricLogPublishingConfigurationTypeDef(BaseValidatorModel):
    CaLogs: Optional[LogConfigurationsTypeDef] = None

class NodeFabricLogPublishingConfigurationTypeDef(BaseValidatorModel):
    ChaincodeLogs: Optional[LogConfigurationsTypeDef] = None
    PeerLogs: Optional[LogConfigurationsTypeDef] = None

class NetworkTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Framework: Optional[FrameworkType] = None
    FrameworkVersion: Optional[str] = None
    FrameworkAttributes: Optional[NetworkFrameworkAttributesTypeDef] = None
    VpcEndpointServiceName: Optional[str] = None
    VotingPolicy: Optional[VotingPolicyTypeDef] = None
    Status: Optional[NetworkStatusType] = None
    CreationDate: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None
    Arn: Optional[str] = None

class ProposalTypeDef(BaseValidatorModel):
    ProposalId: Optional[str] = None
    NetworkId: Optional[str] = None
    Description: Optional[str] = None
    Actions: Optional[ProposalActionsOutputTypeDef] = None
    ProposedByMemberId: Optional[str] = None
    ProposedByMemberName: Optional[str] = None
    Status: Optional[ProposalStatusType] = None
    CreationDate: Optional[datetime] = None
    ExpirationDate: Optional[datetime] = None
    YesVoteCount: Optional[int] = None
    NoVoteCount: Optional[int] = None
    OutstandingVoteCount: Optional[int] = None
    Tags: Optional[Dict[str, str]] = None
    Arn: Optional[str] = None

class CreateProposalInputRequestTypeDef(BaseValidatorModel):
    ClientRequestToken: str
    NetworkId: str
    MemberId: str
    Actions: ProposalActionsTypeDef
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class MemberLogPublishingConfigurationTypeDef(BaseValidatorModel):
    Fabric: Optional[MemberFabricLogPublishingConfigurationTypeDef] = None

class NodeLogPublishingConfigurationTypeDef(BaseValidatorModel):
    Fabric: Optional[NodeFabricLogPublishingConfigurationTypeDef] = None

class GetNetworkOutputTypeDef(BaseValidatorModel):
    Network: NetworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetProposalOutputTypeDef(BaseValidatorModel):
    Proposal: ProposalTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class MemberConfigurationTypeDef(BaseValidatorModel):
    Name: str
    FrameworkConfiguration: MemberFrameworkConfigurationTypeDef
    Description: Optional[str] = None
    LogPublishingConfiguration: Optional[MemberLogPublishingConfigurationTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None
    KmsKeyArn: Optional[str] = None

class MemberTypeDef(BaseValidatorModel):
    NetworkId: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    FrameworkAttributes: Optional[MemberFrameworkAttributesTypeDef] = None
    LogPublishingConfiguration: Optional[MemberLogPublishingConfigurationTypeDef] = None
    Status: Optional[MemberStatusType] = None
    CreationDate: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None
    Arn: Optional[str] = None
    KmsKeyArn: Optional[str] = None

class UpdateMemberInputRequestTypeDef(BaseValidatorModel):
    NetworkId: str
    MemberId: str
    LogPublishingConfiguration: Optional[MemberLogPublishingConfigurationTypeDef] = None

class NodeConfigurationTypeDef(BaseValidatorModel):
    InstanceType: str
    AvailabilityZone: Optional[str] = None
    LogPublishingConfiguration: Optional[NodeLogPublishingConfigurationTypeDef] = None
    StateDB: Optional[StateDBTypeType] = None

class NodeTypeDef(BaseValidatorModel):
    NetworkId: Optional[str] = None
    MemberId: Optional[str] = None
    Id: Optional[str] = None
    InstanceType: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    FrameworkAttributes: Optional[NodeFrameworkAttributesTypeDef] = None
    LogPublishingConfiguration: Optional[NodeLogPublishingConfigurationTypeDef] = None
    StateDB: Optional[StateDBTypeType] = None
    Status: Optional[NodeStatusType] = None
    CreationDate: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None
    Arn: Optional[str] = None
    KmsKeyArn: Optional[str] = None

class UpdateNodeInputRequestTypeDef(BaseValidatorModel):
    NetworkId: str
    NodeId: str
    MemberId: Optional[str] = None
    LogPublishingConfiguration: Optional[NodeLogPublishingConfigurationTypeDef] = None

class CreateMemberInputRequestTypeDef(BaseValidatorModel):
    ClientRequestToken: str
    InvitationId: str
    NetworkId: str
    MemberConfiguration: MemberConfigurationTypeDef

class CreateNetworkInputRequestTypeDef(BaseValidatorModel):
    ClientRequestToken: str
    Name: str
    Framework: FrameworkType
    FrameworkVersion: str
    VotingPolicy: VotingPolicyTypeDef
    MemberConfiguration: MemberConfigurationTypeDef
    Description: Optional[str] = None
    FrameworkConfiguration: Optional[NetworkFrameworkConfigurationTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None

class GetMemberOutputTypeDef(BaseValidatorModel):
    Member: MemberTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNodeInputRequestTypeDef(BaseValidatorModel):
    ClientRequestToken: str
    NetworkId: str
    NodeConfiguration: NodeConfigurationTypeDef
    MemberId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class GetNodeOutputTypeDef(BaseValidatorModel):
    Node: NodeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


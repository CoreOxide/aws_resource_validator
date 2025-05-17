from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AccessorSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Type: Optional[Literal['BILLING_TOKEN']] = None
    Status: Optional[AccessorStatusType] = None
    CreationDate: Optional[datetime] = None
    Arn: Optional[str] = None
    NetworkType: Optional[AccessorNetworkTypeType] = None


class Accessor(BaseValidatorModel):
    Id: Optional[str] = None
    Type: Optional[Literal['BILLING_TOKEN']] = None
    BillingToken: Optional[str] = None
    Status: Optional[AccessorStatusType] = None
    CreationDate: Optional[datetime] = None
    Arn: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    NetworkType: Optional[AccessorNetworkTypeType] = None


class ApprovalThresholdPolicy(BaseValidatorModel):
    ThresholdPercentage: Optional[int] = None
    ProposalDurationInHours: Optional[int] = None
    ThresholdComparator: Optional[ThresholdComparatorType] = None


# This class is the input for the 'create_accessor' function.
class CreateAccessorInput(BaseValidatorModel):
    ClientRequestToken: str
    AccessorType: Literal['BILLING_TOKEN']
    Tags: Optional[Dict[str, str]] = None
    NetworkType: Optional[AccessorNetworkTypeType] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteAccessorInput(BaseValidatorModel):
    AccessorId: str


class DeleteMemberInput(BaseValidatorModel):
    NetworkId: str
    MemberId: str


class DeleteNodeInput(BaseValidatorModel):
    NetworkId: str
    NodeId: str
    MemberId: Optional[str] = None


# This class is the input for the 'get_accessor' function.
class GetAccessorInput(BaseValidatorModel):
    AccessorId: str


# This class is the input for the 'get_member' function.
class GetMemberInput(BaseValidatorModel):
    NetworkId: str
    MemberId: str


# This class is the input for the 'get_network' function.
class GetNetworkInput(BaseValidatorModel):
    NetworkId: str


# This class is the input for the 'get_node' function.
class GetNodeInput(BaseValidatorModel):
    NetworkId: str
    NodeId: str
    MemberId: Optional[str] = None


# This class is the input for the 'get_proposal' function.
class GetProposalInput(BaseValidatorModel):
    NetworkId: str
    ProposalId: str


class NetworkSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Framework: Optional[FrameworkType] = None
    FrameworkVersion: Optional[str] = None
    Status: Optional[NetworkStatusType] = None
    CreationDate: Optional[datetime] = None
    Arn: Optional[str] = None


class InviteAction(BaseValidatorModel):
    Principal: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_accessors' function.
class ListAccessorsInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    NetworkType: Optional[AccessorNetworkTypeType] = None


# This class is the input for the 'list_invitations' function.
class ListInvitationsInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_members' function.
class ListMembersInput(BaseValidatorModel):
    NetworkId: str
    Name: Optional[str] = None
    Status: Optional[MemberStatusType] = None
    IsOwned: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class MemberSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[MemberStatusType] = None
    CreationDate: Optional[datetime] = None
    IsOwned: Optional[bool] = None
    Arn: Optional[str] = None


# This class is the input for the 'list_networks' function.
class ListNetworksInput(BaseValidatorModel):
    Name: Optional[str] = None
    Framework: Optional[FrameworkType] = None
    Status: Optional[NetworkStatusType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_nodes' function.
class ListNodesInput(BaseValidatorModel):
    NetworkId: str
    MemberId: Optional[str] = None
    Status: Optional[NodeStatusType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class NodeSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Status: Optional[NodeStatusType] = None
    CreationDate: Optional[datetime] = None
    AvailabilityZone: Optional[str] = None
    InstanceType: Optional[str] = None
    Arn: Optional[str] = None


# This class is the input for the 'list_proposal_votes' function.
class ListProposalVotesInput(BaseValidatorModel):
    NetworkId: str
    ProposalId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class VoteSummary(BaseValidatorModel):
    Vote: Optional[VoteValueType] = None
    MemberName: Optional[str] = None
    MemberId: Optional[str] = None


# This class is the input for the 'list_proposals' function.
class ListProposalsInput(BaseValidatorModel):
    NetworkId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ProposalSummary(BaseValidatorModel):
    ProposalId: Optional[str] = None
    Description: Optional[str] = None
    ProposedByMemberId: Optional[str] = None
    ProposedByMemberName: Optional[str] = None
    Status: Optional[ProposalStatusType] = None
    CreationDate: Optional[datetime] = None
    ExpirationDate: Optional[datetime] = None
    Arn: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class LogConfiguration(BaseValidatorModel):
    Enabled: Optional[bool] = None


class MemberFabricAttributes(BaseValidatorModel):
    AdminUsername: Optional[str] = None
    CaEndpoint: Optional[str] = None


class MemberFabricConfiguration(BaseValidatorModel):
    AdminUsername: str
    AdminPassword: str


class NetworkEthereumAttributes(BaseValidatorModel):
    ChainId: Optional[str] = None


class NetworkFabricAttributes(BaseValidatorModel):
    OrderingServiceEndpoint: Optional[str] = None
    Edition: Optional[EditionType] = None


class NetworkFabricConfiguration(BaseValidatorModel):
    Edition: EditionType


class NodeEthereumAttributes(BaseValidatorModel):
    HttpEndpoint: Optional[str] = None
    WebSocketEndpoint: Optional[str] = None


class NodeFabricAttributes(BaseValidatorModel):
    PeerEndpoint: Optional[str] = None
    PeerEventEndpoint: Optional[str] = None


class RemoveAction(BaseValidatorModel):
    MemberId: str


class RejectInvitationInput(BaseValidatorModel):
    InvitationId: str


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class VoteOnProposalInput(BaseValidatorModel):
    NetworkId: str
    ProposalId: str
    VoterMemberId: str
    Vote: VoteValueType


class VotingPolicy(BaseValidatorModel):
    ApprovalThresholdPolicy: Optional[ApprovalThresholdPolicy] = None


# This class is the output for the 'create_accessor' function.
class CreateAccessorOutput(BaseValidatorModel):
    AccessorId: str
    BillingToken: str
    NetworkType: AccessorNetworkTypeType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_member' function.
class CreateMemberOutput(BaseValidatorModel):
    MemberId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_network' function.
class CreateNetworkOutput(BaseValidatorModel):
    NetworkId: str
    MemberId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_node' function.
class CreateNodeOutput(BaseValidatorModel):
    NodeId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_proposal' function.
class CreateProposalOutput(BaseValidatorModel):
    ProposalId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_accessor' function.
class GetAccessorOutput(BaseValidatorModel):
    Accessor: Accessor
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_accessors' function.
class ListAccessorsOutput(BaseValidatorModel):
    Accessors: List[AccessorSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class Invitation(BaseValidatorModel):
    InvitationId: Optional[str] = None
    CreationDate: Optional[datetime] = None
    ExpirationDate: Optional[datetime] = None
    Status: Optional[InvitationStatusType] = None
    NetworkSummary: Optional[NetworkSummary] = None
    Arn: Optional[str] = None


# This class is the output for the 'list_networks' function.
class ListNetworksOutput(BaseValidatorModel):
    Networks: List[NetworkSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListAccessorsInputPaginate(BaseValidatorModel):
    NetworkType: Optional[AccessorNetworkTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_members' function.
class ListMembersOutput(BaseValidatorModel):
    Members: List[MemberSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_nodes' function.
class ListNodesOutput(BaseValidatorModel):
    Nodes: List[NodeSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_proposal_votes' function.
class ListProposalVotesOutput(BaseValidatorModel):
    ProposalVotes: List[VoteSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_proposals' function.
class ListProposalsOutput(BaseValidatorModel):
    Proposals: List[ProposalSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class LogConfigurations(BaseValidatorModel):
    Cloudwatch: Optional[LogConfiguration] = None


class MemberFrameworkAttributes(BaseValidatorModel):
    Fabric: Optional[MemberFabricAttributes] = None


class MemberFrameworkConfiguration(BaseValidatorModel):
    Fabric: Optional[MemberFabricConfiguration] = None


class NetworkFrameworkAttributes(BaseValidatorModel):
    Fabric: Optional[NetworkFabricAttributes] = None
    Ethereum: Optional[NetworkEthereumAttributes] = None


class NetworkFrameworkConfiguration(BaseValidatorModel):
    Fabric: Optional[NetworkFabricConfiguration] = None


class NodeFrameworkAttributes(BaseValidatorModel):
    Fabric: Optional[NodeFabricAttributes] = None
    Ethereum: Optional[NodeEthereumAttributes] = None


class ProposalActionsOutput(BaseValidatorModel):
    Invitations: Optional[List[InviteAction]] = None
    Removals: Optional[List[RemoveAction]] = None


class ProposalActions(BaseValidatorModel):
    Invitations: Optional[List[InviteAction]] = None
    Removals: Optional[List[RemoveAction]] = None


# This class is the output for the 'list_invitations' function.
class ListInvitationsOutput(BaseValidatorModel):
    Invitations: List[Invitation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class MemberFabricLogPublishingConfiguration(BaseValidatorModel):
    CaLogs: Optional[LogConfigurations] = None


class NodeFabricLogPublishingConfiguration(BaseValidatorModel):
    ChaincodeLogs: Optional[LogConfigurations] = None
    PeerLogs: Optional[LogConfigurations] = None


class Network(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Framework: Optional[FrameworkType] = None
    FrameworkVersion: Optional[str] = None
    FrameworkAttributes: Optional[NetworkFrameworkAttributes] = None
    VpcEndpointServiceName: Optional[str] = None
    VotingPolicy: Optional[VotingPolicy] = None
    Status: Optional[NetworkStatusType] = None
    CreationDate: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None
    Arn: Optional[str] = None


class Proposal(BaseValidatorModel):
    ProposalId: Optional[str] = None
    NetworkId: Optional[str] = None
    Description: Optional[str] = None
    Actions: Optional[ProposalActionsOutput] = None
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

ProposalActionsUnion = Union[ProposalActions, ProposalActionsOutput]


class MemberLogPublishingConfiguration(BaseValidatorModel):
    Fabric: Optional[MemberFabricLogPublishingConfiguration] = None


class NodeLogPublishingConfiguration(BaseValidatorModel):
    Fabric: Optional[NodeFabricLogPublishingConfiguration] = None


# This class is the output for the 'get_network' function.
class GetNetworkOutput(BaseValidatorModel):
    Network: Network
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_proposal' function.
class GetProposalOutput(BaseValidatorModel):
    Proposal: Proposal
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_proposal' function.
class CreateProposalInput(BaseValidatorModel):
    ClientRequestToken: str
    NetworkId: str
    MemberId: str
    Actions: ProposalActionsUnion
    Description: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class MemberConfiguration(BaseValidatorModel):
    Name: str
    FrameworkConfiguration: MemberFrameworkConfiguration
    Description: Optional[str] = None
    LogPublishingConfiguration: Optional[MemberLogPublishingConfiguration] = None
    Tags: Optional[Dict[str, str]] = None
    KmsKeyArn: Optional[str] = None


class Member(BaseValidatorModel):
    NetworkId: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    FrameworkAttributes: Optional[MemberFrameworkAttributes] = None
    LogPublishingConfiguration: Optional[MemberLogPublishingConfiguration] = None
    Status: Optional[MemberStatusType] = None
    CreationDate: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None
    Arn: Optional[str] = None
    KmsKeyArn: Optional[str] = None


class UpdateMemberInput(BaseValidatorModel):
    NetworkId: str
    MemberId: str
    LogPublishingConfiguration: Optional[MemberLogPublishingConfiguration] = None


class NodeConfiguration(BaseValidatorModel):
    InstanceType: str
    AvailabilityZone: Optional[str] = None
    LogPublishingConfiguration: Optional[NodeLogPublishingConfiguration] = None
    StateDB: Optional[StateDBTypeType] = None


class Node(BaseValidatorModel):
    NetworkId: Optional[str] = None
    MemberId: Optional[str] = None
    Id: Optional[str] = None
    InstanceType: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    FrameworkAttributes: Optional[NodeFrameworkAttributes] = None
    LogPublishingConfiguration: Optional[NodeLogPublishingConfiguration] = None
    StateDB: Optional[StateDBTypeType] = None
    Status: Optional[NodeStatusType] = None
    CreationDate: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None
    Arn: Optional[str] = None
    KmsKeyArn: Optional[str] = None


class UpdateNodeInput(BaseValidatorModel):
    NetworkId: str
    NodeId: str
    MemberId: Optional[str] = None
    LogPublishingConfiguration: Optional[NodeLogPublishingConfiguration] = None


# This class is the input for the 'create_member' function.
class CreateMemberInput(BaseValidatorModel):
    ClientRequestToken: str
    InvitationId: str
    NetworkId: str
    MemberConfiguration: MemberConfiguration


# This class is the input for the 'create_network' function.
class CreateNetworkInput(BaseValidatorModel):
    ClientRequestToken: str
    Name: str
    Framework: FrameworkType
    FrameworkVersion: str
    VotingPolicy: VotingPolicy
    MemberConfiguration: MemberConfiguration
    Description: Optional[str] = None
    FrameworkConfiguration: Optional[NetworkFrameworkConfiguration] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the output for the 'get_member' function.
class GetMemberOutput(BaseValidatorModel):
    Member: Member
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_node' function.
class CreateNodeInput(BaseValidatorModel):
    ClientRequestToken: str
    NetworkId: str
    NodeConfiguration: NodeConfiguration
    MemberId: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the output for the 'get_node' function.
class GetNodeOutput(BaseValidatorModel):
    Node: Node
    ResponseMetadata: ResponseMetadata
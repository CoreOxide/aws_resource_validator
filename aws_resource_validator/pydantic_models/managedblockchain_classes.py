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
from aws_resource_validator.pydantic_models.managedblockchain_constants import *

class ApprovalThresholdPolicy(BaseValidatorModel):
    ThresholdPercentage: Optional[int] = None
    ProposalDurationInHours: Optional[int] = None
    ThresholdComparator: Optional[ThresholdComparatorType] = None


class CreateAccessorInput(BaseValidatorModel):
    ClientRequestToken: str
    AccessorType: Literal["BILLING_TOKEN"]
    Tags: Optional[Mapping[str, str]] = None
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


class GetAccessorInput(BaseValidatorModel):
    AccessorId: str


class GetMemberInput(BaseValidatorModel):
    NetworkId: str
    MemberId: str


class GetNetworkInput(BaseValidatorModel):
    NetworkId: str


class GetNodeInput(BaseValidatorModel):
    NetworkId: str
    NodeId: str
    MemberId: Optional[str] = None


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


class ListAccessorsInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    NetworkType: Optional[AccessorNetworkTypeType] = None


class ListInvitationsInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


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


class ListNetworksInput(BaseValidatorModel):
    Name: Optional[str] = None
    Framework: Optional[FrameworkType] = None
    Status: Optional[NetworkStatusType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


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


class ListProposalVotesInput(BaseValidatorModel):
    NetworkId: str
    ProposalId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class VoteSummary(BaseValidatorModel):
    Vote: Optional[VoteValueType] = None
    MemberName: Optional[str] = None
    MemberId: Optional[str] = None


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
    Tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class VoteOnProposalInput(BaseValidatorModel):
    NetworkId: str
    ProposalId: str
    VoterMemberId: str
    Vote: VoteValueType


class VotingPolicy(BaseValidatorModel):
    ApprovalThresholdPolicy: Optional[ApprovalThresholdPolicy] = None


class CreateAccessorOutput(BaseValidatorModel):
    AccessorId: str
    BillingToken: str
    NetworkType: AccessorNetworkTypeType
    ResponseMetadata: ResponseMetadata


class CreateMemberOutput(BaseValidatorModel):
    MemberId: str
    ResponseMetadata: ResponseMetadata


class CreateNetworkOutput(BaseValidatorModel):
    NetworkId: str
    MemberId: str
    ResponseMetadata: ResponseMetadata


class CreateNodeOutput(BaseValidatorModel):
    NodeId: str
    ResponseMetadata: ResponseMetadata


class CreateProposalOutput(BaseValidatorModel):
    ProposalId: str
    ResponseMetadata: ResponseMetadata


class Accessor(BaseValidatorModel):
    pass


class GetAccessorOutput(BaseValidatorModel):
    Accessor: Accessor
    ResponseMetadata: ResponseMetadata


class AccessorSummary(BaseValidatorModel):
    pass


class ListAccessorsOutput(BaseValidatorModel):
    Accessors: List[AccessorSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


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


class ListNetworksOutput(BaseValidatorModel):
    Networks: List[NetworkSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListAccessorsInputPaginate(BaseValidatorModel):
    NetworkType: Optional[AccessorNetworkTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMembersOutput(BaseValidatorModel):
    Members: List[MemberSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListNodesOutput(BaseValidatorModel):
    Nodes: List[NodeSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListProposalVotesOutput(BaseValidatorModel):
    ProposalVotes: List[VoteSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


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
    Invitations: Optional[Sequence[InviteAction]] = None
    Removals: Optional[Sequence[RemoveAction]] = None


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


class MemberLogPublishingConfiguration(BaseValidatorModel):
    Fabric: Optional[MemberFabricLogPublishingConfiguration] = None


class NodeLogPublishingConfiguration(BaseValidatorModel):
    Fabric: Optional[NodeFabricLogPublishingConfiguration] = None


class GetNetworkOutput(BaseValidatorModel):
    Network: Network
    ResponseMetadata: ResponseMetadata


class GetProposalOutput(BaseValidatorModel):
    Proposal: Proposal
    ResponseMetadata: ResponseMetadata


class ProposalActionsUnion(BaseValidatorModel):
    pass


class CreateProposalInput(BaseValidatorModel):
    ClientRequestToken: str
    NetworkId: str
    MemberId: str
    Actions: ProposalActionsUnion
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class MemberConfiguration(BaseValidatorModel):
    Name: str
    FrameworkConfiguration: MemberFrameworkConfiguration
    Description: Optional[str] = None
    LogPublishingConfiguration: Optional[MemberLogPublishingConfiguration] = None
    Tags: Optional[Mapping[str, str]] = None
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


class CreateMemberInput(BaseValidatorModel):
    ClientRequestToken: str
    InvitationId: str
    NetworkId: str
    MemberConfiguration: MemberConfiguration


class CreateNetworkInput(BaseValidatorModel):
    ClientRequestToken: str
    Name: str
    Framework: FrameworkType
    FrameworkVersion: str
    VotingPolicy: VotingPolicy
    MemberConfiguration: MemberConfiguration
    Description: Optional[str] = None
    FrameworkConfiguration: Optional[NetworkFrameworkConfiguration] = None
    Tags: Optional[Mapping[str, str]] = None


class GetMemberOutput(BaseValidatorModel):
    Member: Member
    ResponseMetadata: ResponseMetadata


class CreateNodeInput(BaseValidatorModel):
    ClientRequestToken: str
    NetworkId: str
    NodeConfiguration: NodeConfiguration
    MemberId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class GetNodeOutput(BaseValidatorModel):
    Node: Node
    ResponseMetadata: ResponseMetadata



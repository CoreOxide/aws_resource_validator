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
from aws_resource_validator.pydantic_models.managedblockchain_constants import *

class AccessorSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Type: Optional[Literal["BILLING_TOKEN"]] = None
    Status: Optional[AccessorStatusType] = None
    CreationDate: Optional[datetime] = None
    Arn: Optional[str] = None
    NetworkType: Optional[AccessorNetworkTypeType] = None

class AccessorTypeDef(BaseModel):
    Id: Optional[str] = None
    Type: Optional[Literal["BILLING_TOKEN"]] = None
    BillingToken: Optional[str] = None
    Status: Optional[AccessorStatusType] = None
    CreationDate: Optional[datetime] = None
    Arn: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    NetworkType: Optional[AccessorNetworkTypeType] = None

class ApprovalThresholdPolicyTypeDef(BaseModel):
    ThresholdPercentage: Optional[int] = None
    ProposalDurationInHours: Optional[int] = None
    ThresholdComparator: Optional[ThresholdComparatorType] = None

class CreateAccessorInputRequestTypeDef(BaseModel):
    ClientRequestToken: str
    AccessorType: Literal["BILLING_TOKEN"]
    Tags: Optional[Mapping[str, str]] = None
    NetworkType: Optional[AccessorNetworkTypeType] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DeleteAccessorInputRequestTypeDef(BaseModel):
    AccessorId: str

class DeleteMemberInputRequestTypeDef(BaseModel):
    NetworkId: str
    MemberId: str

class DeleteNodeInputRequestTypeDef(BaseModel):
    NetworkId: str
    NodeId: str
    MemberId: Optional[str] = None

class GetAccessorInputRequestTypeDef(BaseModel):
    AccessorId: str

class GetMemberInputRequestTypeDef(BaseModel):
    NetworkId: str
    MemberId: str

class GetNetworkInputRequestTypeDef(BaseModel):
    NetworkId: str

class GetNodeInputRequestTypeDef(BaseModel):
    NetworkId: str
    NodeId: str
    MemberId: Optional[str] = None

class GetProposalInputRequestTypeDef(BaseModel):
    NetworkId: str
    ProposalId: str

class NetworkSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Framework: Optional[FrameworkType] = None
    FrameworkVersion: Optional[str] = None
    Status: Optional[NetworkStatusType] = None
    CreationDate: Optional[datetime] = None
    Arn: Optional[str] = None

class InviteActionTypeDef(BaseModel):
    Principal: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAccessorsInputRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    NetworkType: Optional[AccessorNetworkTypeType] = None

class ListInvitationsInputRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListMembersInputRequestTypeDef(BaseModel):
    NetworkId: str
    Name: Optional[str] = None
    Status: Optional[MemberStatusType] = None
    IsOwned: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class MemberSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[MemberStatusType] = None
    CreationDate: Optional[datetime] = None
    IsOwned: Optional[bool] = None
    Arn: Optional[str] = None

class ListNetworksInputRequestTypeDef(BaseModel):
    Name: Optional[str] = None
    Framework: Optional[FrameworkType] = None
    Status: Optional[NetworkStatusType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListNodesInputRequestTypeDef(BaseModel):
    NetworkId: str
    MemberId: Optional[str] = None
    Status: Optional[NodeStatusType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class NodeSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Status: Optional[NodeStatusType] = None
    CreationDate: Optional[datetime] = None
    AvailabilityZone: Optional[str] = None
    InstanceType: Optional[str] = None
    Arn: Optional[str] = None

class ListProposalVotesInputRequestTypeDef(BaseModel):
    NetworkId: str
    ProposalId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class VoteSummaryTypeDef(BaseModel):
    Vote: Optional[VoteValueType] = None
    MemberName: Optional[str] = None
    MemberId: Optional[str] = None

class ListProposalsInputRequestTypeDef(BaseModel):
    NetworkId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ProposalSummaryTypeDef(BaseModel):
    ProposalId: Optional[str] = None
    Description: Optional[str] = None
    ProposedByMemberId: Optional[str] = None
    ProposedByMemberName: Optional[str] = None
    Status: Optional[ProposalStatusType] = None
    CreationDate: Optional[datetime] = None
    ExpirationDate: Optional[datetime] = None
    Arn: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class LogConfigurationTypeDef(BaseModel):
    Enabled: Optional[bool] = None

class MemberFabricAttributesTypeDef(BaseModel):
    AdminUsername: Optional[str] = None
    CaEndpoint: Optional[str] = None

class MemberFabricConfigurationTypeDef(BaseModel):
    AdminUsername: str
    AdminPassword: str

class NetworkEthereumAttributesTypeDef(BaseModel):
    ChainId: Optional[str] = None

class NetworkFabricAttributesTypeDef(BaseModel):
    OrderingServiceEndpoint: Optional[str] = None
    Edition: Optional[EditionType] = None

class NetworkFabricConfigurationTypeDef(BaseModel):
    Edition: EditionType

class NodeEthereumAttributesTypeDef(BaseModel):
    HttpEndpoint: Optional[str] = None
    WebSocketEndpoint: Optional[str] = None

class NodeFabricAttributesTypeDef(BaseModel):
    PeerEndpoint: Optional[str] = None
    PeerEventEndpoint: Optional[str] = None

class RemoveActionTypeDef(BaseModel):
    MemberId: str

class RejectInvitationInputRequestTypeDef(BaseModel):
    InvitationId: str

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class VoteOnProposalInputRequestTypeDef(BaseModel):
    NetworkId: str
    ProposalId: str
    VoterMemberId: str
    Vote: VoteValueType

class VotingPolicyTypeDef(BaseModel):
    ApprovalThresholdPolicy: Optional[ApprovalThresholdPolicyTypeDef] = None

class CreateAccessorOutputTypeDef(BaseModel):
    AccessorId: str
    BillingToken: str
    NetworkType: AccessorNetworkTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMemberOutputTypeDef(BaseModel):
    MemberId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNetworkOutputTypeDef(BaseModel):
    NetworkId: str
    MemberId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNodeOutputTypeDef(BaseModel):
    NodeId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProposalOutputTypeDef(BaseModel):
    ProposalId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccessorOutputTypeDef(BaseModel):
    Accessor: AccessorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccessorsOutputTypeDef(BaseModel):
    Accessors: List[AccessorSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class InvitationTypeDef(BaseModel):
    InvitationId: Optional[str] = None
    CreationDate: Optional[datetime] = None
    ExpirationDate: Optional[datetime] = None
    Status: Optional[InvitationStatusType] = None
    NetworkSummary: Optional[NetworkSummaryTypeDef] = None
    Arn: Optional[str] = None

class ListNetworksOutputTypeDef(BaseModel):
    Networks: List[NetworkSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListAccessorsInputListAccessorsPaginateTypeDef(BaseModel):
    NetworkType: Optional[AccessorNetworkTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMembersOutputTypeDef(BaseModel):
    Members: List[MemberSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListNodesOutputTypeDef(BaseModel):
    Nodes: List[NodeSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListProposalVotesOutputTypeDef(BaseModel):
    ProposalVotes: List[VoteSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListProposalsOutputTypeDef(BaseModel):
    Proposals: List[ProposalSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class LogConfigurationsTypeDef(BaseModel):
    Cloudwatch: Optional[LogConfigurationTypeDef] = None

class MemberFrameworkAttributesTypeDef(BaseModel):
    Fabric: Optional[MemberFabricAttributesTypeDef] = None

class MemberFrameworkConfigurationTypeDef(BaseModel):
    Fabric: Optional[MemberFabricConfigurationTypeDef] = None

class NetworkFrameworkAttributesTypeDef(BaseModel):
    Fabric: Optional[NetworkFabricAttributesTypeDef] = None
    Ethereum: Optional[NetworkEthereumAttributesTypeDef] = None

class NetworkFrameworkConfigurationTypeDef(BaseModel):
    Fabric: Optional[NetworkFabricConfigurationTypeDef] = None

class NodeFrameworkAttributesTypeDef(BaseModel):
    Fabric: Optional[NodeFabricAttributesTypeDef] = None
    Ethereum: Optional[NodeEthereumAttributesTypeDef] = None

class ProposalActionsOutputTypeDef(BaseModel):
    Invitations: Optional[List[InviteActionTypeDef]] = None
    Removals: Optional[List[RemoveActionTypeDef]] = None

class ProposalActionsTypeDef(BaseModel):
    Invitations: Optional[Sequence[InviteActionTypeDef]] = None
    Removals: Optional[Sequence[RemoveActionTypeDef]] = None

class ListInvitationsOutputTypeDef(BaseModel):
    Invitations: List[InvitationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class MemberFabricLogPublishingConfigurationTypeDef(BaseModel):
    CaLogs: Optional[LogConfigurationsTypeDef] = None

class NodeFabricLogPublishingConfigurationTypeDef(BaseModel):
    ChaincodeLogs: Optional[LogConfigurationsTypeDef] = None
    PeerLogs: Optional[LogConfigurationsTypeDef] = None

class NetworkTypeDef(BaseModel):
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

class ProposalTypeDef(BaseModel):
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

class CreateProposalInputRequestTypeDef(BaseModel):
    ClientRequestToken: str
    NetworkId: str
    MemberId: str
    Actions: ProposalActionsTypeDef
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class MemberLogPublishingConfigurationTypeDef(BaseModel):
    Fabric: Optional[MemberFabricLogPublishingConfigurationTypeDef] = None

class NodeLogPublishingConfigurationTypeDef(BaseModel):
    Fabric: Optional[NodeFabricLogPublishingConfigurationTypeDef] = None

class GetNetworkOutputTypeDef(BaseModel):
    Network: NetworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetProposalOutputTypeDef(BaseModel):
    Proposal: ProposalTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class MemberConfigurationTypeDef(BaseModel):
    Name: str
    FrameworkConfiguration: MemberFrameworkConfigurationTypeDef
    Description: Optional[str] = None
    LogPublishingConfiguration: Optional[MemberLogPublishingConfigurationTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None
    KmsKeyArn: Optional[str] = None

class MemberTypeDef(BaseModel):
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

class UpdateMemberInputRequestTypeDef(BaseModel):
    NetworkId: str
    MemberId: str
    LogPublishingConfiguration: Optional[MemberLogPublishingConfigurationTypeDef] = None

class NodeConfigurationTypeDef(BaseModel):
    InstanceType: str
    AvailabilityZone: Optional[str] = None
    LogPublishingConfiguration: Optional[NodeLogPublishingConfigurationTypeDef] = None
    StateDB: Optional[StateDBTypeType] = None

class NodeTypeDef(BaseModel):
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

class UpdateNodeInputRequestTypeDef(BaseModel):
    NetworkId: str
    NodeId: str
    MemberId: Optional[str] = None
    LogPublishingConfiguration: Optional[NodeLogPublishingConfigurationTypeDef] = None

class CreateMemberInputRequestTypeDef(BaseModel):
    ClientRequestToken: str
    InvitationId: str
    NetworkId: str
    MemberConfiguration: MemberConfigurationTypeDef

class CreateNetworkInputRequestTypeDef(BaseModel):
    ClientRequestToken: str
    Name: str
    Framework: FrameworkType
    FrameworkVersion: str
    VotingPolicy: VotingPolicyTypeDef
    MemberConfiguration: MemberConfigurationTypeDef
    Description: Optional[str] = None
    FrameworkConfiguration: Optional[NetworkFrameworkConfigurationTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None

class GetMemberOutputTypeDef(BaseModel):
    Member: MemberTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNodeInputRequestTypeDef(BaseModel):
    ClientRequestToken: str
    NetworkId: str
    NodeConfiguration: NodeConfigurationTypeDef
    MemberId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class GetNodeOutputTypeDef(BaseModel):
    Node: NodeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


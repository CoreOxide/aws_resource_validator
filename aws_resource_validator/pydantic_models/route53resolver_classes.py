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
from aws_resource_validator.pydantic_models.route53resolver_constants import *

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class FirewallRuleGroupAssociationTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    FirewallRuleGroupId: Optional[str] = None
    VpcId: Optional[str] = None
    Name: Optional[str] = None
    Priority: Optional[int] = None
    MutationProtection: Optional[MutationProtectionStatusType] = None
    ManagedOwnerName: Optional[str] = None
    Status: Optional[FirewallRuleGroupAssociationStatusType] = None
    StatusMessage: Optional[str] = None
    CreatorRequestId: Optional[str] = None
    CreationTime: Optional[str] = None
    ModificationTime: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class IpAddressUpdateTypeDef(BaseModel):
    IpId: Optional[str] = None
    SubnetId: Optional[str] = None
    Ip: Optional[str] = None
    Ipv6: Optional[str] = None

class ResolverEndpointTypeDef(BaseModel):
    Id: Optional[str] = None
    CreatorRequestId: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    SecurityGroupIds: Optional[List[str]] = None
    Direction: Optional[ResolverEndpointDirectionType] = None
    IpAddressCount: Optional[int] = None
    HostVPCId: Optional[str] = None
    Status: Optional[ResolverEndpointStatusType] = None
    StatusMessage: Optional[str] = None
    CreationTime: Optional[str] = None
    ModificationTime: Optional[str] = None
    OutpostArn: Optional[str] = None
    PreferredInstanceType: Optional[str] = None
    ResolverEndpointType: Optional[ResolverEndpointTypeType] = None
    Protocols: Optional[List[ProtocolType]] = None

class AssociateResolverQueryLogConfigRequestRequestTypeDef(BaseModel):
    ResolverQueryLogConfigId: str
    ResourceId: str

class ResolverQueryLogConfigAssociationTypeDef(BaseModel):
    Id: Optional[str] = None
    ResolverQueryLogConfigId: Optional[str] = None
    ResourceId: Optional[str] = None
    Status: Optional[ResolverQueryLogConfigAssociationStatusType] = None
    Error: Optional[ResolverQueryLogConfigAssociationErrorType] = None
    ErrorMessage: Optional[str] = None
    CreationTime: Optional[str] = None

class AssociateResolverRuleRequestRequestTypeDef(BaseModel):
    ResolverRuleId: str
    VPCId: str
    Name: Optional[str] = None

class ResolverRuleAssociationTypeDef(BaseModel):
    Id: Optional[str] = None
    ResolverRuleId: Optional[str] = None
    Name: Optional[str] = None
    VPCId: Optional[str] = None
    Status: Optional[ResolverRuleAssociationStatusType] = None
    StatusMessage: Optional[str] = None

class FirewallDomainListTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    DomainCount: Optional[int] = None
    Status: Optional[FirewallDomainListStatusType] = None
    StatusMessage: Optional[str] = None
    ManagedOwnerName: Optional[str] = None
    CreatorRequestId: Optional[str] = None
    CreationTime: Optional[str] = None
    ModificationTime: Optional[str] = None

class FirewallRuleGroupTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    RuleCount: Optional[int] = None
    Status: Optional[FirewallRuleGroupStatusType] = None
    StatusMessage: Optional[str] = None
    OwnerId: Optional[str] = None
    CreatorRequestId: Optional[str] = None
    ShareStatus: Optional[ShareStatusType] = None
    CreationTime: Optional[str] = None
    ModificationTime: Optional[str] = None

class CreateFirewallRuleRequestRequestTypeDef(BaseModel):
    CreatorRequestId: str
    FirewallRuleGroupId: str
    FirewallDomainListId: str
    Priority: int
    Action: ActionType
    Name: str
    BlockResponse: Optional[BlockResponseType] = None
    BlockOverrideDomain: Optional[str] = None
    BlockOverrideDnsType: Optional[Literal["CNAME"]] = None
    BlockOverrideTtl: Optional[int] = None
    FirewallDomainRedirectionAction: Optional[FirewallDomainRedirectionActionType] = None
    Qtype: Optional[str] = None

class FirewallRuleTypeDef(BaseModel):
    FirewallRuleGroupId: Optional[str] = None
    FirewallDomainListId: Optional[str] = None
    Name: Optional[str] = None
    Priority: Optional[int] = None
    Action: Optional[ActionType] = None
    BlockResponse: Optional[BlockResponseType] = None
    BlockOverrideDomain: Optional[str] = None
    BlockOverrideDnsType: Optional[Literal["CNAME"]] = None
    BlockOverrideTtl: Optional[int] = None
    CreatorRequestId: Optional[str] = None
    CreationTime: Optional[str] = None
    ModificationTime: Optional[str] = None
    FirewallDomainRedirectionAction: Optional[FirewallDomainRedirectionActionType] = None
    Qtype: Optional[str] = None

class OutpostResolverTypeDef(BaseModel):
    Arn: Optional[str] = None
    CreationTime: Optional[str] = None
    ModificationTime: Optional[str] = None
    CreatorRequestId: Optional[str] = None
    Id: Optional[str] = None
    InstanceCount: Optional[int] = None
    PreferredInstanceType: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[OutpostResolverStatusType] = None
    StatusMessage: Optional[str] = None
    OutpostArn: Optional[str] = None

class IpAddressRequestTypeDef(BaseModel):
    SubnetId: str
    Ip: Optional[str] = None
    Ipv6: Optional[str] = None

class ResolverQueryLogConfigTypeDef(BaseModel):
    Id: Optional[str] = None
    OwnerId: Optional[str] = None
    Status: Optional[ResolverQueryLogConfigStatusType] = None
    ShareStatus: Optional[ShareStatusType] = None
    AssociationCount: Optional[int] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    DestinationArn: Optional[str] = None
    CreatorRequestId: Optional[str] = None
    CreationTime: Optional[str] = None

class TargetAddressTypeDef(BaseModel):
    Ip: Optional[str] = None
    Port: Optional[int] = None
    Ipv6: Optional[str] = None
    Protocol: Optional[ProtocolType] = None

class DeleteFirewallDomainListRequestRequestTypeDef(BaseModel):
    FirewallDomainListId: str

class DeleteFirewallRuleGroupRequestRequestTypeDef(BaseModel):
    FirewallRuleGroupId: str

class DeleteFirewallRuleRequestRequestTypeDef(BaseModel):
    FirewallRuleGroupId: str
    FirewallDomainListId: str
    Qtype: Optional[str] = None

class DeleteOutpostResolverRequestRequestTypeDef(BaseModel):
    Id: str

class DeleteResolverEndpointRequestRequestTypeDef(BaseModel):
    ResolverEndpointId: str

class DeleteResolverQueryLogConfigRequestRequestTypeDef(BaseModel):
    ResolverQueryLogConfigId: str

class DeleteResolverRuleRequestRequestTypeDef(BaseModel):
    ResolverRuleId: str

class DisassociateFirewallRuleGroupRequestRequestTypeDef(BaseModel):
    FirewallRuleGroupAssociationId: str

class DisassociateResolverQueryLogConfigRequestRequestTypeDef(BaseModel):
    ResolverQueryLogConfigId: str
    ResourceId: str

class DisassociateResolverRuleRequestRequestTypeDef(BaseModel):
    VPCId: str
    ResolverRuleId: str

class FilterTypeDef(BaseModel):
    Name: Optional[str] = None
    Values: Optional[Sequence[str]] = None

class FirewallConfigTypeDef(BaseModel):
    Id: Optional[str] = None
    ResourceId: Optional[str] = None
    OwnerId: Optional[str] = None
    FirewallFailOpen: Optional[FirewallFailOpenStatusType] = None

class FirewallDomainListMetadataTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    CreatorRequestId: Optional[str] = None
    ManagedOwnerName: Optional[str] = None

class FirewallRuleGroupMetadataTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    OwnerId: Optional[str] = None
    CreatorRequestId: Optional[str] = None
    ShareStatus: Optional[ShareStatusType] = None

class GetFirewallConfigRequestRequestTypeDef(BaseModel):
    ResourceId: str

class GetFirewallDomainListRequestRequestTypeDef(BaseModel):
    FirewallDomainListId: str

class GetFirewallRuleGroupAssociationRequestRequestTypeDef(BaseModel):
    FirewallRuleGroupAssociationId: str

class GetFirewallRuleGroupPolicyRequestRequestTypeDef(BaseModel):
    Arn: str

class GetFirewallRuleGroupRequestRequestTypeDef(BaseModel):
    FirewallRuleGroupId: str

class GetOutpostResolverRequestRequestTypeDef(BaseModel):
    Id: str

class GetResolverConfigRequestRequestTypeDef(BaseModel):
    ResourceId: str

class ResolverConfigTypeDef(BaseModel):
    Id: Optional[str] = None
    ResourceId: Optional[str] = None
    OwnerId: Optional[str] = None
    AutodefinedReverse: Optional[ResolverAutodefinedReverseStatusType] = None

class GetResolverDnssecConfigRequestRequestTypeDef(BaseModel):
    ResourceId: str

class ResolverDnssecConfigTypeDef(BaseModel):
    Id: Optional[str] = None
    OwnerId: Optional[str] = None
    ResourceId: Optional[str] = None
    ValidationStatus: Optional[ResolverDNSSECValidationStatusType] = None

class GetResolverEndpointRequestRequestTypeDef(BaseModel):
    ResolverEndpointId: str

class GetResolverQueryLogConfigAssociationRequestRequestTypeDef(BaseModel):
    ResolverQueryLogConfigAssociationId: str

class GetResolverQueryLogConfigPolicyRequestRequestTypeDef(BaseModel):
    Arn: str

class GetResolverQueryLogConfigRequestRequestTypeDef(BaseModel):
    ResolverQueryLogConfigId: str

class GetResolverRuleAssociationRequestRequestTypeDef(BaseModel):
    ResolverRuleAssociationId: str

class GetResolverRulePolicyRequestRequestTypeDef(BaseModel):
    Arn: str

class GetResolverRuleRequestRequestTypeDef(BaseModel):
    ResolverRuleId: str

class ImportFirewallDomainsRequestRequestTypeDef(BaseModel):
    FirewallDomainListId: str
    Operation: Literal["REPLACE"]
    DomainFileUrl: str

class IpAddressResponseTypeDef(BaseModel):
    IpId: Optional[str] = None
    SubnetId: Optional[str] = None
    Ip: Optional[str] = None
    Ipv6: Optional[str] = None
    Status: Optional[IpAddressStatusType] = None
    StatusMessage: Optional[str] = None
    CreationTime: Optional[str] = None
    ModificationTime: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListFirewallConfigsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListFirewallDomainListsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListFirewallDomainsRequestRequestTypeDef(BaseModel):
    FirewallDomainListId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListFirewallRuleGroupAssociationsRequestRequestTypeDef(BaseModel):
    FirewallRuleGroupId: Optional[str] = None
    VpcId: Optional[str] = None
    Priority: Optional[int] = None
    Status: Optional[FirewallRuleGroupAssociationStatusType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListFirewallRuleGroupsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListFirewallRulesRequestRequestTypeDef(BaseModel):
    FirewallRuleGroupId: str
    Priority: Optional[int] = None
    Action: Optional[ActionType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListOutpostResolversRequestRequestTypeDef(BaseModel):
    OutpostArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListResolverConfigsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListResolverEndpointIpAddressesRequestRequestTypeDef(BaseModel):
    ResolverEndpointId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class PutFirewallRuleGroupPolicyRequestRequestTypeDef(BaseModel):
    Arn: str
    FirewallRuleGroupPolicy: str

class PutResolverQueryLogConfigPolicyRequestRequestTypeDef(BaseModel):
    Arn: str
    ResolverQueryLogConfigPolicy: str

class PutResolverRulePolicyRequestRequestTypeDef(BaseModel):
    Arn: str
    ResolverRulePolicy: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateFirewallConfigRequestRequestTypeDef(BaseModel):
    ResourceId: str
    FirewallFailOpen: FirewallFailOpenStatusType

class UpdateFirewallDomainsRequestRequestTypeDef(BaseModel):
    FirewallDomainListId: str
    Operation: FirewallDomainUpdateOperationType
    Domains: Sequence[str]

class UpdateFirewallRuleGroupAssociationRequestRequestTypeDef(BaseModel):
    FirewallRuleGroupAssociationId: str
    Priority: Optional[int] = None
    MutationProtection: Optional[MutationProtectionStatusType] = None
    Name: Optional[str] = None

class UpdateFirewallRuleRequestRequestTypeDef(BaseModel):
    FirewallRuleGroupId: str
    FirewallDomainListId: str
    Priority: Optional[int] = None
    Action: Optional[ActionType] = None
    BlockResponse: Optional[BlockResponseType] = None
    BlockOverrideDomain: Optional[str] = None
    BlockOverrideDnsType: Optional[Literal["CNAME"]] = None
    BlockOverrideTtl: Optional[int] = None
    Name: Optional[str] = None
    FirewallDomainRedirectionAction: Optional[FirewallDomainRedirectionActionType] = None
    Qtype: Optional[str] = None

class UpdateIpAddressTypeDef(BaseModel):
    IpId: str
    Ipv6: str

class UpdateOutpostResolverRequestRequestTypeDef(BaseModel):
    Id: str
    Name: Optional[str] = None
    InstanceCount: Optional[int] = None
    PreferredInstanceType: Optional[str] = None

class UpdateResolverConfigRequestRequestTypeDef(BaseModel):
    ResourceId: str
    AutodefinedReverseFlag: AutodefinedReverseFlagType

class UpdateResolverDnssecConfigRequestRequestTypeDef(BaseModel):
    ResourceId: str
    Validation: ValidationType

class AssociateFirewallRuleGroupRequestRequestTypeDef(BaseModel):
    CreatorRequestId: str
    FirewallRuleGroupId: str
    VpcId: str
    Priority: int
    Name: str
    MutationProtection: Optional[MutationProtectionStatusType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateFirewallDomainListRequestRequestTypeDef(BaseModel):
    CreatorRequestId: str
    Name: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateFirewallRuleGroupRequestRequestTypeDef(BaseModel):
    CreatorRequestId: str
    Name: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateOutpostResolverRequestRequestTypeDef(BaseModel):
    CreatorRequestId: str
    Name: str
    PreferredInstanceType: str
    OutpostArn: str
    InstanceCount: Optional[int] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateResolverQueryLogConfigRequestRequestTypeDef(BaseModel):
    Name: str
    DestinationArn: str
    CreatorRequestId: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class AssociateFirewallRuleGroupResponseTypeDef(BaseModel):
    FirewallRuleGroupAssociation: FirewallRuleGroupAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateFirewallRuleGroupResponseTypeDef(BaseModel):
    FirewallRuleGroupAssociation: FirewallRuleGroupAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetFirewallRuleGroupAssociationResponseTypeDef(BaseModel):
    FirewallRuleGroupAssociation: FirewallRuleGroupAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetFirewallRuleGroupPolicyResponseTypeDef(BaseModel):
    FirewallRuleGroupPolicy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetResolverQueryLogConfigPolicyResponseTypeDef(BaseModel):
    ResolverQueryLogConfigPolicy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetResolverRulePolicyResponseTypeDef(BaseModel):
    ResolverRulePolicy: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportFirewallDomainsResponseTypeDef(BaseModel):
    Id: str
    Name: str
    Status: FirewallDomainListStatusType
    StatusMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListFirewallDomainsResponseTypeDef(BaseModel):
    Domains: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListFirewallRuleGroupAssociationsResponseTypeDef(BaseModel):
    FirewallRuleGroupAssociations: List[FirewallRuleGroupAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutFirewallRuleGroupPolicyResponseTypeDef(BaseModel):
    ReturnValue: bool
    ResponseMetadata: ResponseMetadataTypeDef

class PutResolverQueryLogConfigPolicyResponseTypeDef(BaseModel):
    ReturnValue: bool
    ResponseMetadata: ResponseMetadataTypeDef

class PutResolverRulePolicyResponseTypeDef(BaseModel):
    ReturnValue: bool
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFirewallDomainsResponseTypeDef(BaseModel):
    Id: str
    Name: str
    Status: FirewallDomainListStatusType
    StatusMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFirewallRuleGroupAssociationResponseTypeDef(BaseModel):
    FirewallRuleGroupAssociation: FirewallRuleGroupAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateResolverEndpointIpAddressRequestRequestTypeDef(BaseModel):
    ResolverEndpointId: str
    IpAddress: IpAddressUpdateTypeDef

class DisassociateResolverEndpointIpAddressRequestRequestTypeDef(BaseModel):
    ResolverEndpointId: str
    IpAddress: IpAddressUpdateTypeDef

class AssociateResolverEndpointIpAddressResponseTypeDef(BaseModel):
    ResolverEndpoint: ResolverEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateResolverEndpointResponseTypeDef(BaseModel):
    ResolverEndpoint: ResolverEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteResolverEndpointResponseTypeDef(BaseModel):
    ResolverEndpoint: ResolverEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateResolverEndpointIpAddressResponseTypeDef(BaseModel):
    ResolverEndpoint: ResolverEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetResolverEndpointResponseTypeDef(BaseModel):
    ResolverEndpoint: ResolverEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListResolverEndpointsResponseTypeDef(BaseModel):
    MaxResults: int
    ResolverEndpoints: List[ResolverEndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateResolverEndpointResponseTypeDef(BaseModel):
    ResolverEndpoint: ResolverEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateResolverQueryLogConfigResponseTypeDef(BaseModel):
    ResolverQueryLogConfigAssociation: ResolverQueryLogConfigAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateResolverQueryLogConfigResponseTypeDef(BaseModel):
    ResolverQueryLogConfigAssociation: ResolverQueryLogConfigAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetResolverQueryLogConfigAssociationResponseTypeDef(BaseModel):
    ResolverQueryLogConfigAssociation: ResolverQueryLogConfigAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListResolverQueryLogConfigAssociationsResponseTypeDef(BaseModel):
    TotalCount: int
    TotalFilteredCount: int
    ResolverQueryLogConfigAssociations: List[ResolverQueryLogConfigAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AssociateResolverRuleResponseTypeDef(BaseModel):
    ResolverRuleAssociation: ResolverRuleAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateResolverRuleResponseTypeDef(BaseModel):
    ResolverRuleAssociation: ResolverRuleAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetResolverRuleAssociationResponseTypeDef(BaseModel):
    ResolverRuleAssociation: ResolverRuleAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListResolverRuleAssociationsResponseTypeDef(BaseModel):
    MaxResults: int
    ResolverRuleAssociations: List[ResolverRuleAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateFirewallDomainListResponseTypeDef(BaseModel):
    FirewallDomainList: FirewallDomainListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFirewallDomainListResponseTypeDef(BaseModel):
    FirewallDomainList: FirewallDomainListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetFirewallDomainListResponseTypeDef(BaseModel):
    FirewallDomainList: FirewallDomainListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFirewallRuleGroupResponseTypeDef(BaseModel):
    FirewallRuleGroup: FirewallRuleGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFirewallRuleGroupResponseTypeDef(BaseModel):
    FirewallRuleGroup: FirewallRuleGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetFirewallRuleGroupResponseTypeDef(BaseModel):
    FirewallRuleGroup: FirewallRuleGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFirewallRuleResponseTypeDef(BaseModel):
    FirewallRule: FirewallRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFirewallRuleResponseTypeDef(BaseModel):
    FirewallRule: FirewallRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListFirewallRulesResponseTypeDef(BaseModel):
    FirewallRules: List[FirewallRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateFirewallRuleResponseTypeDef(BaseModel):
    FirewallRule: FirewallRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateOutpostResolverResponseTypeDef(BaseModel):
    OutpostResolver: OutpostResolverTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteOutpostResolverResponseTypeDef(BaseModel):
    OutpostResolver: OutpostResolverTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetOutpostResolverResponseTypeDef(BaseModel):
    OutpostResolver: OutpostResolverTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListOutpostResolversResponseTypeDef(BaseModel):
    OutpostResolvers: List[OutpostResolverTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateOutpostResolverResponseTypeDef(BaseModel):
    OutpostResolver: OutpostResolverTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateResolverEndpointRequestRequestTypeDef(BaseModel):
    CreatorRequestId: str
    SecurityGroupIds: Sequence[str]
    Direction: ResolverEndpointDirectionType
    IpAddresses: Sequence[IpAddressRequestTypeDef]
    Name: Optional[str] = None
    OutpostArn: Optional[str] = None
    PreferredInstanceType: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ResolverEndpointType: Optional[ResolverEndpointTypeType] = None
    Protocols: Optional[Sequence[ProtocolType]] = None

class CreateResolverQueryLogConfigResponseTypeDef(BaseModel):
    ResolverQueryLogConfig: ResolverQueryLogConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteResolverQueryLogConfigResponseTypeDef(BaseModel):
    ResolverQueryLogConfig: ResolverQueryLogConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetResolverQueryLogConfigResponseTypeDef(BaseModel):
    ResolverQueryLogConfig: ResolverQueryLogConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListResolverQueryLogConfigsResponseTypeDef(BaseModel):
    TotalCount: int
    TotalFilteredCount: int
    ResolverQueryLogConfigs: List[ResolverQueryLogConfigTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateResolverRuleRequestRequestTypeDef(BaseModel):
    CreatorRequestId: str
    RuleType: RuleTypeOptionType
    Name: Optional[str] = None
    DomainName: Optional[str] = None
    TargetIps: Optional[Sequence[TargetAddressTypeDef]] = None
    ResolverEndpointId: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ResolverRuleConfigTypeDef(BaseModel):
    Name: Optional[str] = None
    TargetIps: Optional[Sequence[TargetAddressTypeDef]] = None
    ResolverEndpointId: Optional[str] = None

class ResolverRuleTypeDef(BaseModel):
    Id: Optional[str] = None
    CreatorRequestId: Optional[str] = None
    Arn: Optional[str] = None
    DomainName: Optional[str] = None
    Status: Optional[ResolverRuleStatusType] = None
    StatusMessage: Optional[str] = None
    RuleType: Optional[RuleTypeOptionType] = None
    Name: Optional[str] = None
    TargetIps: Optional[List[TargetAddressTypeDef]] = None
    ResolverEndpointId: Optional[str] = None
    OwnerId: Optional[str] = None
    ShareStatus: Optional[ShareStatusType] = None
    CreationTime: Optional[str] = None
    ModificationTime: Optional[str] = None

class ListResolverDnssecConfigsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class ListResolverEndpointsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class ListResolverQueryLogConfigAssociationsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    SortBy: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None

class ListResolverQueryLogConfigsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    SortBy: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None

class ListResolverRuleAssociationsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class ListResolverRulesRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class GetFirewallConfigResponseTypeDef(BaseModel):
    FirewallConfig: FirewallConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListFirewallConfigsResponseTypeDef(BaseModel):
    FirewallConfigs: List[FirewallConfigTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateFirewallConfigResponseTypeDef(BaseModel):
    FirewallConfig: FirewallConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListFirewallDomainListsResponseTypeDef(BaseModel):
    FirewallDomainLists: List[FirewallDomainListMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListFirewallRuleGroupsResponseTypeDef(BaseModel):
    FirewallRuleGroups: List[FirewallRuleGroupMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetResolverConfigResponseTypeDef(BaseModel):
    ResolverConfig: ResolverConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListResolverConfigsResponseTypeDef(BaseModel):
    ResolverConfigs: List[ResolverConfigTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateResolverConfigResponseTypeDef(BaseModel):
    ResolverConfig: ResolverConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetResolverDnssecConfigResponseTypeDef(BaseModel):
    ResolverDNSSECConfig: ResolverDnssecConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListResolverDnssecConfigsResponseTypeDef(BaseModel):
    ResolverDnssecConfigs: List[ResolverDnssecConfigTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateResolverDnssecConfigResponseTypeDef(BaseModel):
    ResolverDNSSECConfig: ResolverDnssecConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListResolverEndpointIpAddressesResponseTypeDef(BaseModel):
    MaxResults: int
    IpAddresses: List[IpAddressResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListFirewallConfigsRequestListFirewallConfigsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFirewallDomainListsRequestListFirewallDomainListsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFirewallDomainsRequestListFirewallDomainsPaginateTypeDef(BaseModel):
    FirewallDomainListId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFirewallRuleGroupsRequestListFirewallRuleGroupsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFirewallRulesRequestListFirewallRulesPaginateTypeDef(BaseModel):
    FirewallRuleGroupId: str
    Priority: Optional[int] = None
    Action: Optional[ActionType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOutpostResolversRequestListOutpostResolversPaginateTypeDef(BaseModel):
    OutpostArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResolverConfigsRequestListResolverConfigsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResolverDnssecConfigsRequestListResolverDnssecConfigsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResolverEndpointIpAddressesRequestListResolverEndpointIpAddressesPaginateTypeDef(BaseModel):
    ResolverEndpointId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResolverEndpointsRequestListResolverEndpointsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResolverQueryLogConfigAssociationsRequestListResolverQueryLogConfigAssociationsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    SortBy: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResolverQueryLogConfigsRequestListResolverQueryLogConfigsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    SortBy: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResolverRuleAssociationsRequestListResolverRuleAssociationsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResolverRulesRequestListResolverRulesPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceRequestListTagsForResourcePaginateTypeDef(BaseModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class UpdateResolverEndpointRequestRequestTypeDef(BaseModel):
    ResolverEndpointId: str
    Name: Optional[str] = None
    ResolverEndpointType: Optional[ResolverEndpointTypeType] = None
    UpdateIpAddresses: Optional[Sequence[UpdateIpAddressTypeDef]] = None
    Protocols: Optional[Sequence[ProtocolType]] = None

class UpdateResolverRuleRequestRequestTypeDef(BaseModel):
    ResolverRuleId: str
    Config: ResolverRuleConfigTypeDef

class CreateResolverRuleResponseTypeDef(BaseModel):
    ResolverRule: ResolverRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteResolverRuleResponseTypeDef(BaseModel):
    ResolverRule: ResolverRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetResolverRuleResponseTypeDef(BaseModel):
    ResolverRule: ResolverRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListResolverRulesResponseTypeDef(BaseModel):
    MaxResults: int
    ResolverRules: List[ResolverRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateResolverRuleResponseTypeDef(BaseModel):
    ResolverRule: ResolverRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


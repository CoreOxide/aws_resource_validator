from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.route53resolver.route53resolver_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class Tag(BaseValidatorModel):
    Key: str
    Value: str


class FirewallRuleGroupAssociation(BaseValidatorModel):
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


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class IpAddressUpdate(BaseValidatorModel):
    IpId: Optional[str] = None
    SubnetId: Optional[str] = None
    Ip: Optional[str] = None
    Ipv6: Optional[str] = None


class ResolverEndpoint(BaseValidatorModel):
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


# This class is the input for the 'associate_resolver_query_log_config' function.
class AssociateResolverQueryLogConfigRequest(BaseValidatorModel):
    ResolverQueryLogConfigId: str
    ResourceId: str


class ResolverQueryLogConfigAssociation(BaseValidatorModel):
    Id: Optional[str] = None
    ResolverQueryLogConfigId: Optional[str] = None
    ResourceId: Optional[str] = None
    Status: Optional[ResolverQueryLogConfigAssociationStatusType] = None
    Error: Optional[ResolverQueryLogConfigAssociationErrorType] = None
    ErrorMessage: Optional[str] = None
    CreationTime: Optional[str] = None


# This class is the input for the 'associate_resolver_rule' function.
class AssociateResolverRuleRequest(BaseValidatorModel):
    ResolverRuleId: str
    VPCId: str
    Name: Optional[str] = None


class ResolverRuleAssociation(BaseValidatorModel):
    Id: Optional[str] = None
    ResolverRuleId: Optional[str] = None
    Name: Optional[str] = None
    VPCId: Optional[str] = None
    Status: Optional[ResolverRuleAssociationStatusType] = None
    StatusMessage: Optional[str] = None


class FirewallDomainList(BaseValidatorModel):
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


class FirewallRuleGroup(BaseValidatorModel):
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


# This class is the input for the 'create_firewall_rule' function.
class CreateFirewallRuleRequest(BaseValidatorModel):
    CreatorRequestId: str
    FirewallRuleGroupId: str
    Priority: int
    Action: ActionType
    Name: str
    FirewallDomainListId: Optional[str] = None
    BlockResponse: Optional[BlockResponseType] = None
    BlockOverrideDomain: Optional[str] = None
    BlockOverrideDnsType: Optional[Literal['CNAME']] = None
    BlockOverrideTtl: Optional[int] = None
    FirewallDomainRedirectionAction: Optional[FirewallDomainRedirectionActionType] = None
    Qtype: Optional[str] = None
    DnsThreatProtection: Optional[DnsThreatProtectionType] = None
    ConfidenceThreshold: Optional[ConfidenceThresholdType] = None


class FirewallRule(BaseValidatorModel):
    FirewallRuleGroupId: Optional[str] = None
    FirewallDomainListId: Optional[str] = None
    FirewallThreatProtectionId: Optional[str] = None
    Name: Optional[str] = None
    Priority: Optional[int] = None
    Action: Optional[ActionType] = None
    BlockResponse: Optional[BlockResponseType] = None
    BlockOverrideDomain: Optional[str] = None
    BlockOverrideDnsType: Optional[Literal['CNAME']] = None
    BlockOverrideTtl: Optional[int] = None
    CreatorRequestId: Optional[str] = None
    CreationTime: Optional[str] = None
    ModificationTime: Optional[str] = None
    FirewallDomainRedirectionAction: Optional[FirewallDomainRedirectionActionType] = None
    Qtype: Optional[str] = None
    DnsThreatProtection: Optional[DnsThreatProtectionType] = None
    ConfidenceThreshold: Optional[ConfidenceThresholdType] = None


class OutpostResolver(BaseValidatorModel):
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


class IpAddressRequest(BaseValidatorModel):
    SubnetId: str
    Ip: Optional[str] = None
    Ipv6: Optional[str] = None


class ResolverQueryLogConfig(BaseValidatorModel):
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


class TargetAddress(BaseValidatorModel):
    Ip: Optional[str] = None
    Port: Optional[int] = None
    Ipv6: Optional[str] = None
    Protocol: Optional[ProtocolType] = None
    ServerNameIndication: Optional[str] = None


# This class is the input for the 'delete_firewall_domain_list' function.
class DeleteFirewallDomainListRequest(BaseValidatorModel):
    FirewallDomainListId: str


# This class is the input for the 'delete_firewall_rule_group' function.
class DeleteFirewallRuleGroupRequest(BaseValidatorModel):
    FirewallRuleGroupId: str


# This class is the input for the 'delete_firewall_rule' function.
class DeleteFirewallRuleRequest(BaseValidatorModel):
    FirewallRuleGroupId: str
    FirewallDomainListId: Optional[str] = None
    FirewallThreatProtectionId: Optional[str] = None
    Qtype: Optional[str] = None


# This class is the input for the 'delete_outpost_resolver' function.
class DeleteOutpostResolverRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'delete_resolver_endpoint' function.
class DeleteResolverEndpointRequest(BaseValidatorModel):
    ResolverEndpointId: str


# This class is the input for the 'delete_resolver_query_log_config' function.
class DeleteResolverQueryLogConfigRequest(BaseValidatorModel):
    ResolverQueryLogConfigId: str


# This class is the input for the 'delete_resolver_rule' function.
class DeleteResolverRuleRequest(BaseValidatorModel):
    ResolverRuleId: str


# This class is the input for the 'disassociate_firewall_rule_group' function.
class DisassociateFirewallRuleGroupRequest(BaseValidatorModel):
    FirewallRuleGroupAssociationId: str


# This class is the input for the 'disassociate_resolver_query_log_config' function.
class DisassociateResolverQueryLogConfigRequest(BaseValidatorModel):
    ResolverQueryLogConfigId: str
    ResourceId: str


# This class is the input for the 'disassociate_resolver_rule' function.
class DisassociateResolverRuleRequest(BaseValidatorModel):
    VPCId: str
    ResolverRuleId: str


class Filter(BaseValidatorModel):
    Name: Optional[str] = None
    Values: Optional[List[str]] = None


class FirewallConfig(BaseValidatorModel):
    Id: Optional[str] = None
    ResourceId: Optional[str] = None
    OwnerId: Optional[str] = None
    FirewallFailOpen: Optional[FirewallFailOpenStatusType] = None


class FirewallDomainListMetadata(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    CreatorRequestId: Optional[str] = None
    ManagedOwnerName: Optional[str] = None


class FirewallRuleGroupMetadata(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    OwnerId: Optional[str] = None
    CreatorRequestId: Optional[str] = None
    ShareStatus: Optional[ShareStatusType] = None


# This class is the input for the 'get_firewall_config' function.
class GetFirewallConfigRequest(BaseValidatorModel):
    ResourceId: str


# This class is the input for the 'get_firewall_domain_list' function.
class GetFirewallDomainListRequest(BaseValidatorModel):
    FirewallDomainListId: str


# This class is the input for the 'get_firewall_rule_group_association' function.
class GetFirewallRuleGroupAssociationRequest(BaseValidatorModel):
    FirewallRuleGroupAssociationId: str


# This class is the input for the 'get_firewall_rule_group_policy' function.
class GetFirewallRuleGroupPolicyRequest(BaseValidatorModel):
    Arn: str


# This class is the input for the 'get_firewall_rule_group' function.
class GetFirewallRuleGroupRequest(BaseValidatorModel):
    FirewallRuleGroupId: str


# This class is the input for the 'get_outpost_resolver' function.
class GetOutpostResolverRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'get_resolver_config' function.
class GetResolverConfigRequest(BaseValidatorModel):
    ResourceId: str


class ResolverConfig(BaseValidatorModel):
    Id: Optional[str] = None
    ResourceId: Optional[str] = None
    OwnerId: Optional[str] = None
    AutodefinedReverse: Optional[ResolverAutodefinedReverseStatusType] = None


# This class is the input for the 'get_resolver_dnssec_config' function.
class GetResolverDnssecConfigRequest(BaseValidatorModel):
    ResourceId: str


class ResolverDnssecConfig(BaseValidatorModel):
    Id: Optional[str] = None
    OwnerId: Optional[str] = None
    ResourceId: Optional[str] = None
    ValidationStatus: Optional[ResolverDNSSECValidationStatusType] = None


# This class is the input for the 'get_resolver_endpoint' function.
class GetResolverEndpointRequest(BaseValidatorModel):
    ResolverEndpointId: str


# This class is the input for the 'get_resolver_query_log_config_association' function.
class GetResolverQueryLogConfigAssociationRequest(BaseValidatorModel):
    ResolverQueryLogConfigAssociationId: str


# This class is the input for the 'get_resolver_query_log_config_policy' function.
class GetResolverQueryLogConfigPolicyRequest(BaseValidatorModel):
    Arn: str


# This class is the input for the 'get_resolver_query_log_config' function.
class GetResolverQueryLogConfigRequest(BaseValidatorModel):
    ResolverQueryLogConfigId: str


# This class is the input for the 'get_resolver_rule_association' function.
class GetResolverRuleAssociationRequest(BaseValidatorModel):
    ResolverRuleAssociationId: str


# This class is the input for the 'get_resolver_rule_policy' function.
class GetResolverRulePolicyRequest(BaseValidatorModel):
    Arn: str


# This class is the input for the 'get_resolver_rule' function.
class GetResolverRuleRequest(BaseValidatorModel):
    ResolverRuleId: str


# This class is the input for the 'import_firewall_domains' function.
class ImportFirewallDomainsRequest(BaseValidatorModel):
    FirewallDomainListId: str
    Operation: Literal['REPLACE']
    DomainFileUrl: str


class IpAddressResponse(BaseValidatorModel):
    IpId: Optional[str] = None
    SubnetId: Optional[str] = None
    Ip: Optional[str] = None
    Ipv6: Optional[str] = None
    Status: Optional[IpAddressStatusType] = None
    StatusMessage: Optional[str] = None
    CreationTime: Optional[str] = None
    ModificationTime: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_firewall_configs' function.
class ListFirewallConfigsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_firewall_domain_lists' function.
class ListFirewallDomainListsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_firewall_domains' function.
class ListFirewallDomainsRequest(BaseValidatorModel):
    FirewallDomainListId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_firewall_rule_group_associations' function.
class ListFirewallRuleGroupAssociationsRequest(BaseValidatorModel):
    FirewallRuleGroupId: Optional[str] = None
    VpcId: Optional[str] = None
    Priority: Optional[int] = None
    Status: Optional[FirewallRuleGroupAssociationStatusType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_firewall_rule_groups' function.
class ListFirewallRuleGroupsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_firewall_rules' function.
class ListFirewallRulesRequest(BaseValidatorModel):
    FirewallRuleGroupId: str
    Priority: Optional[int] = None
    Action: Optional[ActionType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_outpost_resolvers' function.
class ListOutpostResolversRequest(BaseValidatorModel):
    OutpostArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_resolver_configs' function.
class ListResolverConfigsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_resolver_endpoint_ip_addresses' function.
class ListResolverEndpointIpAddressesRequest(BaseValidatorModel):
    ResolverEndpointId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'put_firewall_rule_group_policy' function.
class PutFirewallRuleGroupPolicyRequest(BaseValidatorModel):
    Arn: str
    FirewallRuleGroupPolicy: str


# This class is the input for the 'put_resolver_query_log_config_policy' function.
class PutResolverQueryLogConfigPolicyRequest(BaseValidatorModel):
    Arn: str
    ResolverQueryLogConfigPolicy: str


# This class is the input for the 'put_resolver_rule_policy' function.
class PutResolverRulePolicyRequest(BaseValidatorModel):
    Arn: str
    ResolverRulePolicy: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


# This class is the input for the 'update_firewall_config' function.
class UpdateFirewallConfigRequest(BaseValidatorModel):
    ResourceId: str
    FirewallFailOpen: FirewallFailOpenStatusType


# This class is the input for the 'update_firewall_domains' function.
class UpdateFirewallDomainsRequest(BaseValidatorModel):
    FirewallDomainListId: str
    Operation: FirewallDomainUpdateOperationType
    Domains: List[str]


# This class is the input for the 'update_firewall_rule_group_association' function.
class UpdateFirewallRuleGroupAssociationRequest(BaseValidatorModel):
    FirewallRuleGroupAssociationId: str
    Priority: Optional[int] = None
    MutationProtection: Optional[MutationProtectionStatusType] = None
    Name: Optional[str] = None


# This class is the input for the 'update_firewall_rule' function.
class UpdateFirewallRuleRequest(BaseValidatorModel):
    FirewallRuleGroupId: str
    FirewallDomainListId: Optional[str] = None
    FirewallThreatProtectionId: Optional[str] = None
    Priority: Optional[int] = None
    Action: Optional[ActionType] = None
    BlockResponse: Optional[BlockResponseType] = None
    BlockOverrideDomain: Optional[str] = None
    BlockOverrideDnsType: Optional[Literal['CNAME']] = None
    BlockOverrideTtl: Optional[int] = None
    Name: Optional[str] = None
    FirewallDomainRedirectionAction: Optional[FirewallDomainRedirectionActionType] = None
    Qtype: Optional[str] = None
    DnsThreatProtection: Optional[DnsThreatProtectionType] = None
    ConfidenceThreshold: Optional[ConfidenceThresholdType] = None


class UpdateIpAddress(BaseValidatorModel):
    IpId: str
    Ipv6: str


# This class is the input for the 'update_outpost_resolver' function.
class UpdateOutpostResolverRequest(BaseValidatorModel):
    Id: str
    Name: Optional[str] = None
    InstanceCount: Optional[int] = None
    PreferredInstanceType: Optional[str] = None


# This class is the input for the 'update_resolver_config' function.
class UpdateResolverConfigRequest(BaseValidatorModel):
    ResourceId: str
    AutodefinedReverseFlag: AutodefinedReverseFlagType


# This class is the input for the 'update_resolver_dnssec_config' function.
class UpdateResolverDnssecConfigRequest(BaseValidatorModel):
    ResourceId: str
    Validation: ValidationType


# This class is the input for the 'associate_firewall_rule_group' function.
class AssociateFirewallRuleGroupRequest(BaseValidatorModel):
    CreatorRequestId: str
    FirewallRuleGroupId: str
    VpcId: str
    Priority: int
    Name: str
    MutationProtection: Optional[MutationProtectionStatusType] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_firewall_domain_list' function.
class CreateFirewallDomainListRequest(BaseValidatorModel):
    CreatorRequestId: str
    Name: str
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_firewall_rule_group' function.
class CreateFirewallRuleGroupRequest(BaseValidatorModel):
    CreatorRequestId: str
    Name: str
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_outpost_resolver' function.
class CreateOutpostResolverRequest(BaseValidatorModel):
    CreatorRequestId: str
    Name: str
    PreferredInstanceType: str
    OutpostArn: str
    InstanceCount: Optional[int] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_resolver_query_log_config' function.
class CreateResolverQueryLogConfigRequest(BaseValidatorModel):
    Name: str
    DestinationArn: str
    CreatorRequestId: str
    Tags: Optional[List[Tag]] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]


# This class is the output for the 'associate_firewall_rule_group' function.
class AssociateFirewallRuleGroupResponse(BaseValidatorModel):
    FirewallRuleGroupAssociation: FirewallRuleGroupAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_firewall_rule_group' function.
class DisassociateFirewallRuleGroupResponse(BaseValidatorModel):
    FirewallRuleGroupAssociation: FirewallRuleGroupAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_firewall_rule_group_association' function.
class GetFirewallRuleGroupAssociationResponse(BaseValidatorModel):
    FirewallRuleGroupAssociation: FirewallRuleGroupAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_firewall_rule_group_policy' function.
class GetFirewallRuleGroupPolicyResponse(BaseValidatorModel):
    FirewallRuleGroupPolicy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_resolver_query_log_config_policy' function.
class GetResolverQueryLogConfigPolicyResponse(BaseValidatorModel):
    ResolverQueryLogConfigPolicy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_resolver_rule_policy' function.
class GetResolverRulePolicyResponse(BaseValidatorModel):
    ResolverRulePolicy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'import_firewall_domains' function.
class ImportFirewallDomainsResponse(BaseValidatorModel):
    Id: str
    Name: str
    Status: FirewallDomainListStatusType
    StatusMessage: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_firewall_domains' function.
class ListFirewallDomainsResponse(BaseValidatorModel):
    Domains: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_firewall_rule_group_associations' function.
class ListFirewallRuleGroupAssociationsResponse(BaseValidatorModel):
    FirewallRuleGroupAssociations: List[FirewallRuleGroupAssociation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'put_firewall_rule_group_policy' function.
class PutFirewallRuleGroupPolicyResponse(BaseValidatorModel):
    ReturnValue: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_resolver_query_log_config_policy' function.
class PutResolverQueryLogConfigPolicyResponse(BaseValidatorModel):
    ReturnValue: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_resolver_rule_policy' function.
class PutResolverRulePolicyResponse(BaseValidatorModel):
    ReturnValue: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_firewall_domains' function.
class UpdateFirewallDomainsResponse(BaseValidatorModel):
    Id: str
    Name: str
    Status: FirewallDomainListStatusType
    StatusMessage: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_firewall_rule_group_association' function.
class UpdateFirewallRuleGroupAssociationResponse(BaseValidatorModel):
    FirewallRuleGroupAssociation: FirewallRuleGroupAssociation
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'associate_resolver_endpoint_ip_address' function.
class AssociateResolverEndpointIpAddressRequest(BaseValidatorModel):
    ResolverEndpointId: str
    IpAddress: IpAddressUpdate


# This class is the input for the 'disassociate_resolver_endpoint_ip_address' function.
class DisassociateResolverEndpointIpAddressRequest(BaseValidatorModel):
    ResolverEndpointId: str
    IpAddress: IpAddressUpdate


# This class is the output for the 'associate_resolver_endpoint_ip_address' function.
class AssociateResolverEndpointIpAddressResponse(BaseValidatorModel):
    ResolverEndpoint: ResolverEndpoint
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_resolver_endpoint' function.
class CreateResolverEndpointResponse(BaseValidatorModel):
    ResolverEndpoint: ResolverEndpoint
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_resolver_endpoint' function.
class DeleteResolverEndpointResponse(BaseValidatorModel):
    ResolverEndpoint: ResolverEndpoint
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_resolver_endpoint_ip_address' function.
class DisassociateResolverEndpointIpAddressResponse(BaseValidatorModel):
    ResolverEndpoint: ResolverEndpoint
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_resolver_endpoint' function.
class GetResolverEndpointResponse(BaseValidatorModel):
    ResolverEndpoint: ResolverEndpoint
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_resolver_endpoints' function.
class ListResolverEndpointsResponse(BaseValidatorModel):
    MaxResults: int
    ResolverEndpoints: List[ResolverEndpoint]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_resolver_endpoint' function.
class UpdateResolverEndpointResponse(BaseValidatorModel):
    ResolverEndpoint: ResolverEndpoint
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'associate_resolver_query_log_config' function.
class AssociateResolverQueryLogConfigResponse(BaseValidatorModel):
    ResolverQueryLogConfigAssociation: ResolverQueryLogConfigAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_resolver_query_log_config' function.
class DisassociateResolverQueryLogConfigResponse(BaseValidatorModel):
    ResolverQueryLogConfigAssociation: ResolverQueryLogConfigAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_resolver_query_log_config_association' function.
class GetResolverQueryLogConfigAssociationResponse(BaseValidatorModel):
    ResolverQueryLogConfigAssociation: ResolverQueryLogConfigAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_resolver_query_log_config_associations' function.
class ListResolverQueryLogConfigAssociationsResponse(BaseValidatorModel):
    TotalCount: int
    TotalFilteredCount: int
    ResolverQueryLogConfigAssociations: List[ResolverQueryLogConfigAssociation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'associate_resolver_rule' function.
class AssociateResolverRuleResponse(BaseValidatorModel):
    ResolverRuleAssociation: ResolverRuleAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_resolver_rule' function.
class DisassociateResolverRuleResponse(BaseValidatorModel):
    ResolverRuleAssociation: ResolverRuleAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_resolver_rule_association' function.
class GetResolverRuleAssociationResponse(BaseValidatorModel):
    ResolverRuleAssociation: ResolverRuleAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_resolver_rule_associations' function.
class ListResolverRuleAssociationsResponse(BaseValidatorModel):
    MaxResults: int
    ResolverRuleAssociations: List[ResolverRuleAssociation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_firewall_domain_list' function.
class CreateFirewallDomainListResponse(BaseValidatorModel):
    FirewallDomainList: FirewallDomainList
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_firewall_domain_list' function.
class DeleteFirewallDomainListResponse(BaseValidatorModel):
    FirewallDomainList: FirewallDomainList
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_firewall_domain_list' function.
class GetFirewallDomainListResponse(BaseValidatorModel):
    FirewallDomainList: FirewallDomainList
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_firewall_rule_group' function.
class CreateFirewallRuleGroupResponse(BaseValidatorModel):
    FirewallRuleGroup: FirewallRuleGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_firewall_rule_group' function.
class DeleteFirewallRuleGroupResponse(BaseValidatorModel):
    FirewallRuleGroup: FirewallRuleGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_firewall_rule_group' function.
class GetFirewallRuleGroupResponse(BaseValidatorModel):
    FirewallRuleGroup: FirewallRuleGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_firewall_rule' function.
class CreateFirewallRuleResponse(BaseValidatorModel):
    FirewallRule: FirewallRule
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_firewall_rule' function.
class DeleteFirewallRuleResponse(BaseValidatorModel):
    FirewallRule: FirewallRule
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_firewall_rules' function.
class ListFirewallRulesResponse(BaseValidatorModel):
    FirewallRules: List[FirewallRule]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_firewall_rule' function.
class UpdateFirewallRuleResponse(BaseValidatorModel):
    FirewallRule: FirewallRule
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_outpost_resolver' function.
class CreateOutpostResolverResponse(BaseValidatorModel):
    OutpostResolver: OutpostResolver
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_outpost_resolver' function.
class DeleteOutpostResolverResponse(BaseValidatorModel):
    OutpostResolver: OutpostResolver
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_outpost_resolver' function.
class GetOutpostResolverResponse(BaseValidatorModel):
    OutpostResolver: OutpostResolver
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_outpost_resolvers' function.
class ListOutpostResolversResponse(BaseValidatorModel):
    OutpostResolvers: List[OutpostResolver]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_outpost_resolver' function.
class UpdateOutpostResolverResponse(BaseValidatorModel):
    OutpostResolver: OutpostResolver
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_resolver_endpoint' function.
class CreateResolverEndpointRequest(BaseValidatorModel):
    CreatorRequestId: str
    SecurityGroupIds: List[str]
    Direction: ResolverEndpointDirectionType
    IpAddresses: List[IpAddressRequest]
    Name: Optional[str] = None
    OutpostArn: Optional[str] = None
    PreferredInstanceType: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    ResolverEndpointType: Optional[ResolverEndpointTypeType] = None
    Protocols: Optional[List[ProtocolType]] = None


# This class is the output for the 'create_resolver_query_log_config' function.
class CreateResolverQueryLogConfigResponse(BaseValidatorModel):
    ResolverQueryLogConfig: ResolverQueryLogConfig
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_resolver_query_log_config' function.
class DeleteResolverQueryLogConfigResponse(BaseValidatorModel):
    ResolverQueryLogConfig: ResolverQueryLogConfig
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_resolver_query_log_config' function.
class GetResolverQueryLogConfigResponse(BaseValidatorModel):
    ResolverQueryLogConfig: ResolverQueryLogConfig
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_resolver_query_log_configs' function.
class ListResolverQueryLogConfigsResponse(BaseValidatorModel):
    TotalCount: int
    TotalFilteredCount: int
    ResolverQueryLogConfigs: List[ResolverQueryLogConfig]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'create_resolver_rule' function.
class CreateResolverRuleRequest(BaseValidatorModel):
    CreatorRequestId: str
    RuleType: RuleTypeOptionType
    Name: Optional[str] = None
    DomainName: Optional[str] = None
    TargetIps: Optional[List[TargetAddress]] = None
    ResolverEndpointId: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class ResolverRuleConfig(BaseValidatorModel):
    Name: Optional[str] = None
    TargetIps: Optional[List[TargetAddress]] = None
    ResolverEndpointId: Optional[str] = None


class ResolverRule(BaseValidatorModel):
    Id: Optional[str] = None
    CreatorRequestId: Optional[str] = None
    Arn: Optional[str] = None
    DomainName: Optional[str] = None
    Status: Optional[ResolverRuleStatusType] = None
    StatusMessage: Optional[str] = None
    RuleType: Optional[RuleTypeOptionType] = None
    Name: Optional[str] = None
    TargetIps: Optional[List[TargetAddress]] = None
    ResolverEndpointId: Optional[str] = None
    OwnerId: Optional[str] = None
    ShareStatus: Optional[ShareStatusType] = None
    CreationTime: Optional[str] = None
    ModificationTime: Optional[str] = None


# This class is the input for the 'list_resolver_dnssec_configs' function.
class ListResolverDnssecConfigsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[List[Filter]] = None


# This class is the input for the 'list_resolver_endpoints' function.
class ListResolverEndpointsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[List[Filter]] = None


# This class is the input for the 'list_resolver_query_log_config_associations' function.
class ListResolverQueryLogConfigAssociationsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    SortBy: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None


# This class is the input for the 'list_resolver_query_log_configs' function.
class ListResolverQueryLogConfigsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    SortBy: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None


# This class is the input for the 'list_resolver_rule_associations' function.
class ListResolverRuleAssociationsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[List[Filter]] = None


# This class is the input for the 'list_resolver_rules' function.
class ListResolverRulesRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[List[Filter]] = None


# This class is the output for the 'get_firewall_config' function.
class GetFirewallConfigResponse(BaseValidatorModel):
    FirewallConfig: FirewallConfig
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_firewall_configs' function.
class ListFirewallConfigsResponse(BaseValidatorModel):
    FirewallConfigs: List[FirewallConfig]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_firewall_config' function.
class UpdateFirewallConfigResponse(BaseValidatorModel):
    FirewallConfig: FirewallConfig
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_firewall_domain_lists' function.
class ListFirewallDomainListsResponse(BaseValidatorModel):
    FirewallDomainLists: List[FirewallDomainListMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_firewall_rule_groups' function.
class ListFirewallRuleGroupsResponse(BaseValidatorModel):
    FirewallRuleGroups: List[FirewallRuleGroupMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_resolver_config' function.
class GetResolverConfigResponse(BaseValidatorModel):
    ResolverConfig: ResolverConfig
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_resolver_configs' function.
class ListResolverConfigsResponse(BaseValidatorModel):
    ResolverConfigs: List[ResolverConfig]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_resolver_config' function.
class UpdateResolverConfigResponse(BaseValidatorModel):
    ResolverConfig: ResolverConfig
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_resolver_dnssec_config' function.
class GetResolverDnssecConfigResponse(BaseValidatorModel):
    ResolverDNSSECConfig: ResolverDnssecConfig
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_resolver_dnssec_configs' function.
class ListResolverDnssecConfigsResponse(BaseValidatorModel):
    ResolverDnssecConfigs: List[ResolverDnssecConfig]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_resolver_dnssec_config' function.
class UpdateResolverDnssecConfigResponse(BaseValidatorModel):
    ResolverDNSSECConfig: ResolverDnssecConfig
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_resolver_endpoint_ip_addresses' function.
class ListResolverEndpointIpAddressesResponse(BaseValidatorModel):
    MaxResults: int
    IpAddresses: List[IpAddressResponse]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListFirewallConfigsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFirewallDomainListsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFirewallDomainsRequestPaginate(BaseValidatorModel):
    FirewallDomainListId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFirewallRuleGroupAssociationsRequestPaginate(BaseValidatorModel):
    FirewallRuleGroupId: Optional[str] = None
    VpcId: Optional[str] = None
    Priority: Optional[int] = None
    Status: Optional[FirewallRuleGroupAssociationStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFirewallRuleGroupsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFirewallRulesRequestPaginate(BaseValidatorModel):
    FirewallRuleGroupId: str
    Priority: Optional[int] = None
    Action: Optional[ActionType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOutpostResolversRequestPaginate(BaseValidatorModel):
    OutpostArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResolverConfigsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResolverDnssecConfigsRequestPaginate(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResolverEndpointIpAddressesRequestPaginate(BaseValidatorModel):
    ResolverEndpointId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResolverEndpointsRequestPaginate(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResolverQueryLogConfigAssociationsRequestPaginate(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    SortBy: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResolverQueryLogConfigsRequestPaginate(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    SortBy: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResolverRuleAssociationsRequestPaginate(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResolverRulesRequestPaginate(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTagsForResourceRequestPaginate(BaseValidatorModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'update_resolver_endpoint' function.
class UpdateResolverEndpointRequest(BaseValidatorModel):
    ResolverEndpointId: str
    Name: Optional[str] = None
    ResolverEndpointType: Optional[ResolverEndpointTypeType] = None
    UpdateIpAddresses: Optional[List[UpdateIpAddress]] = None
    Protocols: Optional[List[ProtocolType]] = None


# This class is the input for the 'update_resolver_rule' function.
class UpdateResolverRuleRequest(BaseValidatorModel):
    ResolverRuleId: str
    Config: ResolverRuleConfig


# This class is the output for the 'create_resolver_rule' function.
class CreateResolverRuleResponse(BaseValidatorModel):
    ResolverRule: ResolverRule
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_resolver_rule' function.
class DeleteResolverRuleResponse(BaseValidatorModel):
    ResolverRule: ResolverRule
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_resolver_rule' function.
class GetResolverRuleResponse(BaseValidatorModel):
    ResolverRule: ResolverRule
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_resolver_rules' function.
class ListResolverRulesResponse(BaseValidatorModel):
    MaxResults: int
    ResolverRules: List[ResolverRule]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_resolver_rule' function.
class UpdateResolverRuleResponse(BaseValidatorModel):
    ResolverRule: ResolverRule
    ResponseMetadata: ResponseMetadata
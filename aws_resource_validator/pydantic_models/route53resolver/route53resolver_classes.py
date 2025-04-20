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


class DeleteFirewallDomainListRequest(BaseValidatorModel):
    FirewallDomainListId: str


class DeleteFirewallRuleGroupRequest(BaseValidatorModel):
    FirewallRuleGroupId: str


class DeleteFirewallRuleRequest(BaseValidatorModel):
    FirewallRuleGroupId: str
    FirewallDomainListId: Optional[str] = None
    FirewallThreatProtectionId: Optional[str] = None
    Qtype: Optional[str] = None


class DeleteOutpostResolverRequest(BaseValidatorModel):
    Id: str


class DeleteResolverEndpointRequest(BaseValidatorModel):
    ResolverEndpointId: str


class DeleteResolverQueryLogConfigRequest(BaseValidatorModel):
    ResolverQueryLogConfigId: str


class DeleteResolverRuleRequest(BaseValidatorModel):
    ResolverRuleId: str


class DisassociateFirewallRuleGroupRequest(BaseValidatorModel):
    FirewallRuleGroupAssociationId: str


class DisassociateResolverQueryLogConfigRequest(BaseValidatorModel):
    ResolverQueryLogConfigId: str
    ResourceId: str


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


class GetFirewallConfigRequest(BaseValidatorModel):
    ResourceId: str


class GetFirewallDomainListRequest(BaseValidatorModel):
    FirewallDomainListId: str


class GetFirewallRuleGroupAssociationRequest(BaseValidatorModel):
    FirewallRuleGroupAssociationId: str


class GetFirewallRuleGroupPolicyRequest(BaseValidatorModel):
    Arn: str


class GetFirewallRuleGroupRequest(BaseValidatorModel):
    FirewallRuleGroupId: str


class GetOutpostResolverRequest(BaseValidatorModel):
    Id: str


class GetResolverConfigRequest(BaseValidatorModel):
    ResourceId: str


class ResolverConfig(BaseValidatorModel):
    Id: Optional[str] = None
    ResourceId: Optional[str] = None
    OwnerId: Optional[str] = None
    AutodefinedReverse: Optional[ResolverAutodefinedReverseStatusType] = None


class GetResolverDnssecConfigRequest(BaseValidatorModel):
    ResourceId: str


class ResolverDnssecConfig(BaseValidatorModel):
    Id: Optional[str] = None
    OwnerId: Optional[str] = None
    ResourceId: Optional[str] = None
    ValidationStatus: Optional[ResolverDNSSECValidationStatusType] = None


class GetResolverEndpointRequest(BaseValidatorModel):
    ResolverEndpointId: str


class GetResolverQueryLogConfigAssociationRequest(BaseValidatorModel):
    ResolverQueryLogConfigAssociationId: str


class GetResolverQueryLogConfigPolicyRequest(BaseValidatorModel):
    Arn: str


class GetResolverQueryLogConfigRequest(BaseValidatorModel):
    ResolverQueryLogConfigId: str


class GetResolverRuleAssociationRequest(BaseValidatorModel):
    ResolverRuleAssociationId: str


class GetResolverRulePolicyRequest(BaseValidatorModel):
    Arn: str


class GetResolverRuleRequest(BaseValidatorModel):
    ResolverRuleId: str


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


class ListFirewallConfigsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListFirewallDomainListsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListFirewallDomainsRequest(BaseValidatorModel):
    FirewallDomainListId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListFirewallRuleGroupAssociationsRequest(BaseValidatorModel):
    FirewallRuleGroupId: Optional[str] = None
    VpcId: Optional[str] = None
    Priority: Optional[int] = None
    Status: Optional[FirewallRuleGroupAssociationStatusType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListFirewallRuleGroupsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListFirewallRulesRequest(BaseValidatorModel):
    FirewallRuleGroupId: str
    Priority: Optional[int] = None
    Action: Optional[ActionType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListOutpostResolversRequest(BaseValidatorModel):
    OutpostArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListResolverConfigsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListResolverEndpointIpAddressesRequest(BaseValidatorModel):
    ResolverEndpointId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class PutFirewallRuleGroupPolicyRequest(BaseValidatorModel):
    Arn: str
    FirewallRuleGroupPolicy: str


class PutResolverQueryLogConfigPolicyRequest(BaseValidatorModel):
    Arn: str
    ResolverQueryLogConfigPolicy: str


class PutResolverRulePolicyRequest(BaseValidatorModel):
    Arn: str
    ResolverRulePolicy: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class UpdateFirewallConfigRequest(BaseValidatorModel):
    ResourceId: str
    FirewallFailOpen: FirewallFailOpenStatusType


class UpdateFirewallDomainsRequest(BaseValidatorModel):
    FirewallDomainListId: str
    Operation: FirewallDomainUpdateOperationType
    Domains: List[str]


class UpdateFirewallRuleGroupAssociationRequest(BaseValidatorModel):
    FirewallRuleGroupAssociationId: str
    Priority: Optional[int] = None
    MutationProtection: Optional[MutationProtectionStatusType] = None
    Name: Optional[str] = None


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


class UpdateOutpostResolverRequest(BaseValidatorModel):
    Id: str
    Name: Optional[str] = None
    InstanceCount: Optional[int] = None
    PreferredInstanceType: Optional[str] = None


class UpdateResolverConfigRequest(BaseValidatorModel):
    ResourceId: str
    AutodefinedReverseFlag: AutodefinedReverseFlagType


class UpdateResolverDnssecConfigRequest(BaseValidatorModel):
    ResourceId: str
    Validation: ValidationType


class AssociateFirewallRuleGroupRequest(BaseValidatorModel):
    CreatorRequestId: str
    FirewallRuleGroupId: str
    VpcId: str
    Priority: int
    Name: str
    MutationProtection: Optional[MutationProtectionStatusType] = None
    Tags: Optional[List[Tag]] = None


class CreateFirewallDomainListRequest(BaseValidatorModel):
    CreatorRequestId: str
    Name: str
    Tags: Optional[List[Tag]] = None


class CreateFirewallRuleGroupRequest(BaseValidatorModel):
    CreatorRequestId: str
    Name: str
    Tags: Optional[List[Tag]] = None


class CreateOutpostResolverRequest(BaseValidatorModel):
    CreatorRequestId: str
    Name: str
    PreferredInstanceType: str
    OutpostArn: str
    InstanceCount: Optional[int] = None
    Tags: Optional[List[Tag]] = None


class CreateResolverQueryLogConfigRequest(BaseValidatorModel):
    Name: str
    DestinationArn: str
    CreatorRequestId: str
    Tags: Optional[List[Tag]] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]


class AssociateFirewallRuleGroupResponse(BaseValidatorModel):
    FirewallRuleGroupAssociation: FirewallRuleGroupAssociation
    ResponseMetadata: ResponseMetadata


class DisassociateFirewallRuleGroupResponse(BaseValidatorModel):
    FirewallRuleGroupAssociation: FirewallRuleGroupAssociation
    ResponseMetadata: ResponseMetadata


class GetFirewallRuleGroupAssociationResponse(BaseValidatorModel):
    FirewallRuleGroupAssociation: FirewallRuleGroupAssociation
    ResponseMetadata: ResponseMetadata


class GetFirewallRuleGroupPolicyResponse(BaseValidatorModel):
    FirewallRuleGroupPolicy: str
    ResponseMetadata: ResponseMetadata


class GetResolverQueryLogConfigPolicyResponse(BaseValidatorModel):
    ResolverQueryLogConfigPolicy: str
    ResponseMetadata: ResponseMetadata


class GetResolverRulePolicyResponse(BaseValidatorModel):
    ResolverRulePolicy: str
    ResponseMetadata: ResponseMetadata


class ImportFirewallDomainsResponse(BaseValidatorModel):
    Id: str
    Name: str
    Status: FirewallDomainListStatusType
    StatusMessage: str
    ResponseMetadata: ResponseMetadata


class ListFirewallDomainsResponse(BaseValidatorModel):
    Domains: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListFirewallRuleGroupAssociationsResponse(BaseValidatorModel):
    FirewallRuleGroupAssociations: List[FirewallRuleGroupAssociation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PutFirewallRuleGroupPolicyResponse(BaseValidatorModel):
    ReturnValue: bool
    ResponseMetadata: ResponseMetadata


class PutResolverQueryLogConfigPolicyResponse(BaseValidatorModel):
    ReturnValue: bool
    ResponseMetadata: ResponseMetadata


class PutResolverRulePolicyResponse(BaseValidatorModel):
    ReturnValue: bool
    ResponseMetadata: ResponseMetadata


class UpdateFirewallDomainsResponse(BaseValidatorModel):
    Id: str
    Name: str
    Status: FirewallDomainListStatusType
    StatusMessage: str
    ResponseMetadata: ResponseMetadata


class UpdateFirewallRuleGroupAssociationResponse(BaseValidatorModel):
    FirewallRuleGroupAssociation: FirewallRuleGroupAssociation
    ResponseMetadata: ResponseMetadata


class AssociateResolverEndpointIpAddressRequest(BaseValidatorModel):
    ResolverEndpointId: str
    IpAddress: IpAddressUpdate


class DisassociateResolverEndpointIpAddressRequest(BaseValidatorModel):
    ResolverEndpointId: str
    IpAddress: IpAddressUpdate


class AssociateResolverEndpointIpAddressResponse(BaseValidatorModel):
    ResolverEndpoint: ResolverEndpoint
    ResponseMetadata: ResponseMetadata


class CreateResolverEndpointResponse(BaseValidatorModel):
    ResolverEndpoint: ResolverEndpoint
    ResponseMetadata: ResponseMetadata


class DeleteResolverEndpointResponse(BaseValidatorModel):
    ResolverEndpoint: ResolverEndpoint
    ResponseMetadata: ResponseMetadata


class DisassociateResolverEndpointIpAddressResponse(BaseValidatorModel):
    ResolverEndpoint: ResolverEndpoint
    ResponseMetadata: ResponseMetadata


class GetResolverEndpointResponse(BaseValidatorModel):
    ResolverEndpoint: ResolverEndpoint
    ResponseMetadata: ResponseMetadata


class ListResolverEndpointsResponse(BaseValidatorModel):
    MaxResults: int
    ResolverEndpoints: List[ResolverEndpoint]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateResolverEndpointResponse(BaseValidatorModel):
    ResolverEndpoint: ResolverEndpoint
    ResponseMetadata: ResponseMetadata


class AssociateResolverQueryLogConfigResponse(BaseValidatorModel):
    ResolverQueryLogConfigAssociation: ResolverQueryLogConfigAssociation
    ResponseMetadata: ResponseMetadata


class DisassociateResolverQueryLogConfigResponse(BaseValidatorModel):
    ResolverQueryLogConfigAssociation: ResolverQueryLogConfigAssociation
    ResponseMetadata: ResponseMetadata


class GetResolverQueryLogConfigAssociationResponse(BaseValidatorModel):
    ResolverQueryLogConfigAssociation: ResolverQueryLogConfigAssociation
    ResponseMetadata: ResponseMetadata


class ListResolverQueryLogConfigAssociationsResponse(BaseValidatorModel):
    TotalCount: int
    TotalFilteredCount: int
    ResolverQueryLogConfigAssociations: List[ResolverQueryLogConfigAssociation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AssociateResolverRuleResponse(BaseValidatorModel):
    ResolverRuleAssociation: ResolverRuleAssociation
    ResponseMetadata: ResponseMetadata


class DisassociateResolverRuleResponse(BaseValidatorModel):
    ResolverRuleAssociation: ResolverRuleAssociation
    ResponseMetadata: ResponseMetadata


class GetResolverRuleAssociationResponse(BaseValidatorModel):
    ResolverRuleAssociation: ResolverRuleAssociation
    ResponseMetadata: ResponseMetadata


class ListResolverRuleAssociationsResponse(BaseValidatorModel):
    MaxResults: int
    ResolverRuleAssociations: List[ResolverRuleAssociation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateFirewallDomainListResponse(BaseValidatorModel):
    FirewallDomainList: FirewallDomainList
    ResponseMetadata: ResponseMetadata


class DeleteFirewallDomainListResponse(BaseValidatorModel):
    FirewallDomainList: FirewallDomainList
    ResponseMetadata: ResponseMetadata


class GetFirewallDomainListResponse(BaseValidatorModel):
    FirewallDomainList: FirewallDomainList
    ResponseMetadata: ResponseMetadata


class CreateFirewallRuleGroupResponse(BaseValidatorModel):
    FirewallRuleGroup: FirewallRuleGroup
    ResponseMetadata: ResponseMetadata


class DeleteFirewallRuleGroupResponse(BaseValidatorModel):
    FirewallRuleGroup: FirewallRuleGroup
    ResponseMetadata: ResponseMetadata


class GetFirewallRuleGroupResponse(BaseValidatorModel):
    FirewallRuleGroup: FirewallRuleGroup
    ResponseMetadata: ResponseMetadata


class CreateFirewallRuleResponse(BaseValidatorModel):
    FirewallRule: FirewallRule
    ResponseMetadata: ResponseMetadata


class DeleteFirewallRuleResponse(BaseValidatorModel):
    FirewallRule: FirewallRule
    ResponseMetadata: ResponseMetadata


class ListFirewallRulesResponse(BaseValidatorModel):
    FirewallRules: List[FirewallRule]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateFirewallRuleResponse(BaseValidatorModel):
    FirewallRule: FirewallRule
    ResponseMetadata: ResponseMetadata


class CreateOutpostResolverResponse(BaseValidatorModel):
    OutpostResolver: OutpostResolver
    ResponseMetadata: ResponseMetadata


class DeleteOutpostResolverResponse(BaseValidatorModel):
    OutpostResolver: OutpostResolver
    ResponseMetadata: ResponseMetadata


class GetOutpostResolverResponse(BaseValidatorModel):
    OutpostResolver: OutpostResolver
    ResponseMetadata: ResponseMetadata


class ListOutpostResolversResponse(BaseValidatorModel):
    OutpostResolvers: List[OutpostResolver]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateOutpostResolverResponse(BaseValidatorModel):
    OutpostResolver: OutpostResolver
    ResponseMetadata: ResponseMetadata


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


class CreateResolverQueryLogConfigResponse(BaseValidatorModel):
    ResolverQueryLogConfig: ResolverQueryLogConfig
    ResponseMetadata: ResponseMetadata


class DeleteResolverQueryLogConfigResponse(BaseValidatorModel):
    ResolverQueryLogConfig: ResolverQueryLogConfig
    ResponseMetadata: ResponseMetadata


class GetResolverQueryLogConfigResponse(BaseValidatorModel):
    ResolverQueryLogConfig: ResolverQueryLogConfig
    ResponseMetadata: ResponseMetadata


class ListResolverQueryLogConfigsResponse(BaseValidatorModel):
    TotalCount: int
    TotalFilteredCount: int
    ResolverQueryLogConfigs: List[ResolverQueryLogConfig]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


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


class ListResolverDnssecConfigsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[List[Filter]] = None


class ListResolverEndpointsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[List[Filter]] = None


class ListResolverQueryLogConfigAssociationsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    SortBy: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None


class ListResolverQueryLogConfigsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    SortBy: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None


class ListResolverRuleAssociationsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[List[Filter]] = None


class ListResolverRulesRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[List[Filter]] = None


class GetFirewallConfigResponse(BaseValidatorModel):
    FirewallConfig: FirewallConfig
    ResponseMetadata: ResponseMetadata


class ListFirewallConfigsResponse(BaseValidatorModel):
    FirewallConfigs: List[FirewallConfig]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateFirewallConfigResponse(BaseValidatorModel):
    FirewallConfig: FirewallConfig
    ResponseMetadata: ResponseMetadata


class ListFirewallDomainListsResponse(BaseValidatorModel):
    FirewallDomainLists: List[FirewallDomainListMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListFirewallRuleGroupsResponse(BaseValidatorModel):
    FirewallRuleGroups: List[FirewallRuleGroupMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetResolverConfigResponse(BaseValidatorModel):
    ResolverConfig: ResolverConfig
    ResponseMetadata: ResponseMetadata


class ListResolverConfigsResponse(BaseValidatorModel):
    ResolverConfigs: List[ResolverConfig]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateResolverConfigResponse(BaseValidatorModel):
    ResolverConfig: ResolverConfig
    ResponseMetadata: ResponseMetadata


class GetResolverDnssecConfigResponse(BaseValidatorModel):
    ResolverDNSSECConfig: ResolverDnssecConfig
    ResponseMetadata: ResponseMetadata


class ListResolverDnssecConfigsResponse(BaseValidatorModel):
    ResolverDnssecConfigs: List[ResolverDnssecConfig]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateResolverDnssecConfigResponse(BaseValidatorModel):
    ResolverDNSSECConfig: ResolverDnssecConfig
    ResponseMetadata: ResponseMetadata


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


class UpdateResolverEndpointRequest(BaseValidatorModel):
    ResolverEndpointId: str
    Name: Optional[str] = None
    ResolverEndpointType: Optional[ResolverEndpointTypeType] = None
    UpdateIpAddresses: Optional[List[UpdateIpAddress]] = None
    Protocols: Optional[List[ProtocolType]] = None


class UpdateResolverRuleRequest(BaseValidatorModel):
    ResolverRuleId: str
    Config: ResolverRuleConfig


class CreateResolverRuleResponse(BaseValidatorModel):
    ResolverRule: ResolverRule
    ResponseMetadata: ResponseMetadata


class DeleteResolverRuleResponse(BaseValidatorModel):
    ResolverRule: ResolverRule
    ResponseMetadata: ResponseMetadata


class GetResolverRuleResponse(BaseValidatorModel):
    ResolverRule: ResolverRule
    ResponseMetadata: ResponseMetadata


class ListResolverRulesResponse(BaseValidatorModel):
    MaxResults: int
    ResolverRules: List[ResolverRule]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateResolverRuleResponse(BaseValidatorModel):
    ResolverRule: ResolverRule
    ResponseMetadata: ResponseMetadata
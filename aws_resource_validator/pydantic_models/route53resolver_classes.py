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
from aws_resource_validator.pydantic_models.route53resolver_constants import *

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class FirewallRuleGroupAssociationTypeDef(BaseValidatorModel):
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


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class IpAddressUpdateTypeDef(BaseValidatorModel):
    IpId: Optional[str] = None
    SubnetId: Optional[str] = None
    Ip: Optional[str] = None
    Ipv6: Optional[str] = None


class ResolverEndpointTypeDef(BaseValidatorModel):
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


class AssociateResolverQueryLogConfigRequestTypeDef(BaseValidatorModel):
    ResolverQueryLogConfigId: str
    ResourceId: str


class ResolverQueryLogConfigAssociationTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    ResolverQueryLogConfigId: Optional[str] = None
    ResourceId: Optional[str] = None
    Status: Optional[ResolverQueryLogConfigAssociationStatusType] = None
    Error: Optional[ResolverQueryLogConfigAssociationErrorType] = None
    ErrorMessage: Optional[str] = None
    CreationTime: Optional[str] = None


class AssociateResolverRuleRequestTypeDef(BaseValidatorModel):
    ResolverRuleId: str
    VPCId: str
    Name: Optional[str] = None


class ResolverRuleAssociationTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    ResolverRuleId: Optional[str] = None
    Name: Optional[str] = None
    VPCId: Optional[str] = None
    Status: Optional[ResolverRuleAssociationStatusType] = None
    StatusMessage: Optional[str] = None


class FirewallDomainListTypeDef(BaseValidatorModel):
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


class FirewallRuleGroupTypeDef(BaseValidatorModel):
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


class CreateFirewallRuleRequestTypeDef(BaseValidatorModel):
    CreatorRequestId: str
    FirewallRuleGroupId: str
    Priority: int
    Action: ActionType
    Name: str
    FirewallDomainListId: Optional[str] = None
    BlockResponse: Optional[BlockResponseType] = None
    BlockOverrideDomain: Optional[str] = None
    BlockOverrideDnsType: Optional[Literal["CNAME"]] = None
    BlockOverrideTtl: Optional[int] = None
    FirewallDomainRedirectionAction: Optional[FirewallDomainRedirectionActionType] = None
    Qtype: Optional[str] = None
    DnsThreatProtection: Optional[DnsThreatProtectionType] = None
    ConfidenceThreshold: Optional[ConfidenceThresholdType] = None


class FirewallRuleTypeDef(BaseValidatorModel):
    FirewallRuleGroupId: Optional[str] = None
    FirewallDomainListId: Optional[str] = None
    FirewallThreatProtectionId: Optional[str] = None
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
    DnsThreatProtection: Optional[DnsThreatProtectionType] = None
    ConfidenceThreshold: Optional[ConfidenceThresholdType] = None


class OutpostResolverTypeDef(BaseValidatorModel):
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


class IpAddressRequestTypeDef(BaseValidatorModel):
    SubnetId: str
    Ip: Optional[str] = None
    Ipv6: Optional[str] = None


class ResolverQueryLogConfigTypeDef(BaseValidatorModel):
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


class DeleteFirewallDomainListRequestTypeDef(BaseValidatorModel):
    FirewallDomainListId: str


class DeleteFirewallRuleGroupRequestTypeDef(BaseValidatorModel):
    FirewallRuleGroupId: str


class DeleteFirewallRuleRequestTypeDef(BaseValidatorModel):
    FirewallRuleGroupId: str
    FirewallDomainListId: Optional[str] = None
    FirewallThreatProtectionId: Optional[str] = None
    Qtype: Optional[str] = None


class DeleteOutpostResolverRequestTypeDef(BaseValidatorModel):
    Id: str


class DeleteResolverEndpointRequestTypeDef(BaseValidatorModel):
    ResolverEndpointId: str


class DeleteResolverQueryLogConfigRequestTypeDef(BaseValidatorModel):
    ResolverQueryLogConfigId: str


class DeleteResolverRuleRequestTypeDef(BaseValidatorModel):
    ResolverRuleId: str


class DisassociateFirewallRuleGroupRequestTypeDef(BaseValidatorModel):
    FirewallRuleGroupAssociationId: str


class DisassociateResolverQueryLogConfigRequestTypeDef(BaseValidatorModel):
    ResolverQueryLogConfigId: str
    ResourceId: str


class DisassociateResolverRuleRequestTypeDef(BaseValidatorModel):
    VPCId: str
    ResolverRuleId: str


class FilterTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Values: Optional[Sequence[str]] = None


class FirewallConfigTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    ResourceId: Optional[str] = None
    OwnerId: Optional[str] = None
    FirewallFailOpen: Optional[FirewallFailOpenStatusType] = None


class FirewallDomainListMetadataTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    CreatorRequestId: Optional[str] = None
    ManagedOwnerName: Optional[str] = None


class FirewallRuleGroupMetadataTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    OwnerId: Optional[str] = None
    CreatorRequestId: Optional[str] = None
    ShareStatus: Optional[ShareStatusType] = None


class GetFirewallConfigRequestTypeDef(BaseValidatorModel):
    ResourceId: str


class GetFirewallDomainListRequestTypeDef(BaseValidatorModel):
    FirewallDomainListId: str


class GetFirewallRuleGroupAssociationRequestTypeDef(BaseValidatorModel):
    FirewallRuleGroupAssociationId: str


class GetFirewallRuleGroupPolicyRequestTypeDef(BaseValidatorModel):
    Arn: str


class GetFirewallRuleGroupRequestTypeDef(BaseValidatorModel):
    FirewallRuleGroupId: str


class GetOutpostResolverRequestTypeDef(BaseValidatorModel):
    Id: str


class GetResolverConfigRequestTypeDef(BaseValidatorModel):
    ResourceId: str


class ResolverConfigTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    ResourceId: Optional[str] = None
    OwnerId: Optional[str] = None
    AutodefinedReverse: Optional[ResolverAutodefinedReverseStatusType] = None


class GetResolverDnssecConfigRequestTypeDef(BaseValidatorModel):
    ResourceId: str


class ResolverDnssecConfigTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    OwnerId: Optional[str] = None
    ResourceId: Optional[str] = None
    ValidationStatus: Optional[ResolverDNSSECValidationStatusType] = None


class GetResolverEndpointRequestTypeDef(BaseValidatorModel):
    ResolverEndpointId: str


class GetResolverQueryLogConfigAssociationRequestTypeDef(BaseValidatorModel):
    ResolverQueryLogConfigAssociationId: str


class GetResolverQueryLogConfigPolicyRequestTypeDef(BaseValidatorModel):
    Arn: str


class GetResolverQueryLogConfigRequestTypeDef(BaseValidatorModel):
    ResolverQueryLogConfigId: str


class GetResolverRuleAssociationRequestTypeDef(BaseValidatorModel):
    ResolverRuleAssociationId: str


class GetResolverRulePolicyRequestTypeDef(BaseValidatorModel):
    Arn: str


class GetResolverRuleRequestTypeDef(BaseValidatorModel):
    ResolverRuleId: str


class ImportFirewallDomainsRequestTypeDef(BaseValidatorModel):
    FirewallDomainListId: str
    Operation: Literal["REPLACE"]
    DomainFileUrl: str


class IpAddressResponseTypeDef(BaseValidatorModel):
    IpId: Optional[str] = None
    SubnetId: Optional[str] = None
    Ip: Optional[str] = None
    Ipv6: Optional[str] = None
    Status: Optional[IpAddressStatusType] = None
    StatusMessage: Optional[str] = None
    CreationTime: Optional[str] = None
    ModificationTime: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListFirewallConfigsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListFirewallDomainListsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListFirewallDomainsRequestTypeDef(BaseValidatorModel):
    FirewallDomainListId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListFirewallRuleGroupAssociationsRequestTypeDef(BaseValidatorModel):
    FirewallRuleGroupId: Optional[str] = None
    VpcId: Optional[str] = None
    Priority: Optional[int] = None
    Status: Optional[FirewallRuleGroupAssociationStatusType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListFirewallRuleGroupsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListFirewallRulesRequestTypeDef(BaseValidatorModel):
    FirewallRuleGroupId: str
    Priority: Optional[int] = None
    Action: Optional[ActionType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListOutpostResolversRequestTypeDef(BaseValidatorModel):
    OutpostArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListResolverConfigsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListResolverEndpointIpAddressesRequestTypeDef(BaseValidatorModel):
    ResolverEndpointId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class PutFirewallRuleGroupPolicyRequestTypeDef(BaseValidatorModel):
    Arn: str
    FirewallRuleGroupPolicy: str


class PutResolverQueryLogConfigPolicyRequestTypeDef(BaseValidatorModel):
    Arn: str
    ResolverQueryLogConfigPolicy: str


class PutResolverRulePolicyRequestTypeDef(BaseValidatorModel):
    Arn: str
    ResolverRulePolicy: str


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateFirewallConfigRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    FirewallFailOpen: FirewallFailOpenStatusType


class UpdateFirewallDomainsRequestTypeDef(BaseValidatorModel):
    FirewallDomainListId: str
    Operation: FirewallDomainUpdateOperationType
    Domains: Sequence[str]


class UpdateFirewallRuleGroupAssociationRequestTypeDef(BaseValidatorModel):
    FirewallRuleGroupAssociationId: str
    Priority: Optional[int] = None
    MutationProtection: Optional[MutationProtectionStatusType] = None
    Name: Optional[str] = None


class UpdateFirewallRuleRequestTypeDef(BaseValidatorModel):
    FirewallRuleGroupId: str
    FirewallDomainListId: Optional[str] = None
    FirewallThreatProtectionId: Optional[str] = None
    Priority: Optional[int] = None
    Action: Optional[ActionType] = None
    BlockResponse: Optional[BlockResponseType] = None
    BlockOverrideDomain: Optional[str] = None
    BlockOverrideDnsType: Optional[Literal["CNAME"]] = None
    BlockOverrideTtl: Optional[int] = None
    Name: Optional[str] = None
    FirewallDomainRedirectionAction: Optional[FirewallDomainRedirectionActionType] = None
    Qtype: Optional[str] = None
    DnsThreatProtection: Optional[DnsThreatProtectionType] = None
    ConfidenceThreshold: Optional[ConfidenceThresholdType] = None


class UpdateIpAddressTypeDef(BaseValidatorModel):
    IpId: str
    Ipv6: str


class UpdateOutpostResolverRequestTypeDef(BaseValidatorModel):
    Id: str
    Name: Optional[str] = None
    InstanceCount: Optional[int] = None
    PreferredInstanceType: Optional[str] = None


class UpdateResolverConfigRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    AutodefinedReverseFlag: AutodefinedReverseFlagType


class UpdateResolverDnssecConfigRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    Validation: ValidationType


class AssociateFirewallRuleGroupRequestTypeDef(BaseValidatorModel):
    CreatorRequestId: str
    FirewallRuleGroupId: str
    VpcId: str
    Priority: int
    Name: str
    MutationProtection: Optional[MutationProtectionStatusType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateFirewallDomainListRequestTypeDef(BaseValidatorModel):
    CreatorRequestId: str
    Name: str
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateFirewallRuleGroupRequestTypeDef(BaseValidatorModel):
    CreatorRequestId: str
    Name: str
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateOutpostResolverRequestTypeDef(BaseValidatorModel):
    CreatorRequestId: str
    Name: str
    PreferredInstanceType: str
    OutpostArn: str
    InstanceCount: Optional[int] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateResolverQueryLogConfigRequestTypeDef(BaseValidatorModel):
    Name: str
    DestinationArn: str
    CreatorRequestId: str
    Tags: Optional[Sequence[TagTypeDef]] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]


class AssociateFirewallRuleGroupResponseTypeDef(BaseValidatorModel):
    FirewallRuleGroupAssociation: FirewallRuleGroupAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DisassociateFirewallRuleGroupResponseTypeDef(BaseValidatorModel):
    FirewallRuleGroupAssociation: FirewallRuleGroupAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetFirewallRuleGroupAssociationResponseTypeDef(BaseValidatorModel):
    FirewallRuleGroupAssociation: FirewallRuleGroupAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetFirewallRuleGroupPolicyResponseTypeDef(BaseValidatorModel):
    FirewallRuleGroupPolicy: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetResolverQueryLogConfigPolicyResponseTypeDef(BaseValidatorModel):
    ResolverQueryLogConfigPolicy: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetResolverRulePolicyResponseTypeDef(BaseValidatorModel):
    ResolverRulePolicy: str
    ResponseMetadata: ResponseMetadataTypeDef


class ImportFirewallDomainsResponseTypeDef(BaseValidatorModel):
    Id: str
    Name: str
    Status: FirewallDomainListStatusType
    StatusMessage: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListFirewallDomainsResponseTypeDef(BaseValidatorModel):
    Domains: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListFirewallRuleGroupAssociationsResponseTypeDef(BaseValidatorModel):
    FirewallRuleGroupAssociations: List[FirewallRuleGroupAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class PutFirewallRuleGroupPolicyResponseTypeDef(BaseValidatorModel):
    ReturnValue: bool
    ResponseMetadata: ResponseMetadataTypeDef


class PutResolverQueryLogConfigPolicyResponseTypeDef(BaseValidatorModel):
    ReturnValue: bool
    ResponseMetadata: ResponseMetadataTypeDef


class PutResolverRulePolicyResponseTypeDef(BaseValidatorModel):
    ReturnValue: bool
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateFirewallDomainsResponseTypeDef(BaseValidatorModel):
    Id: str
    Name: str
    Status: FirewallDomainListStatusType
    StatusMessage: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateFirewallRuleGroupAssociationResponseTypeDef(BaseValidatorModel):
    FirewallRuleGroupAssociation: FirewallRuleGroupAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AssociateResolverEndpointIpAddressRequestTypeDef(BaseValidatorModel):
    ResolverEndpointId: str
    IpAddress: IpAddressUpdateTypeDef


class DisassociateResolverEndpointIpAddressRequestTypeDef(BaseValidatorModel):
    ResolverEndpointId: str
    IpAddress: IpAddressUpdateTypeDef


class AssociateResolverEndpointIpAddressResponseTypeDef(BaseValidatorModel):
    ResolverEndpoint: ResolverEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateResolverEndpointResponseTypeDef(BaseValidatorModel):
    ResolverEndpoint: ResolverEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteResolverEndpointResponseTypeDef(BaseValidatorModel):
    ResolverEndpoint: ResolverEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DisassociateResolverEndpointIpAddressResponseTypeDef(BaseValidatorModel):
    ResolverEndpoint: ResolverEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetResolverEndpointResponseTypeDef(BaseValidatorModel):
    ResolverEndpoint: ResolverEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListResolverEndpointsResponseTypeDef(BaseValidatorModel):
    MaxResults: int
    ResolverEndpoints: List[ResolverEndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateResolverEndpointResponseTypeDef(BaseValidatorModel):
    ResolverEndpoint: ResolverEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AssociateResolverQueryLogConfigResponseTypeDef(BaseValidatorModel):
    ResolverQueryLogConfigAssociation: ResolverQueryLogConfigAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DisassociateResolverQueryLogConfigResponseTypeDef(BaseValidatorModel):
    ResolverQueryLogConfigAssociation: ResolverQueryLogConfigAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetResolverQueryLogConfigAssociationResponseTypeDef(BaseValidatorModel):
    ResolverQueryLogConfigAssociation: ResolverQueryLogConfigAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListResolverQueryLogConfigAssociationsResponseTypeDef(BaseValidatorModel):
    TotalCount: int
    TotalFilteredCount: int
    ResolverQueryLogConfigAssociations: List[ResolverQueryLogConfigAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class AssociateResolverRuleResponseTypeDef(BaseValidatorModel):
    ResolverRuleAssociation: ResolverRuleAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DisassociateResolverRuleResponseTypeDef(BaseValidatorModel):
    ResolverRuleAssociation: ResolverRuleAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetResolverRuleAssociationResponseTypeDef(BaseValidatorModel):
    ResolverRuleAssociation: ResolverRuleAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListResolverRuleAssociationsResponseTypeDef(BaseValidatorModel):
    MaxResults: int
    ResolverRuleAssociations: List[ResolverRuleAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateFirewallDomainListResponseTypeDef(BaseValidatorModel):
    FirewallDomainList: FirewallDomainListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteFirewallDomainListResponseTypeDef(BaseValidatorModel):
    FirewallDomainList: FirewallDomainListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetFirewallDomainListResponseTypeDef(BaseValidatorModel):
    FirewallDomainList: FirewallDomainListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateFirewallRuleGroupResponseTypeDef(BaseValidatorModel):
    FirewallRuleGroup: FirewallRuleGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteFirewallRuleGroupResponseTypeDef(BaseValidatorModel):
    FirewallRuleGroup: FirewallRuleGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetFirewallRuleGroupResponseTypeDef(BaseValidatorModel):
    FirewallRuleGroup: FirewallRuleGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateFirewallRuleResponseTypeDef(BaseValidatorModel):
    FirewallRule: FirewallRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteFirewallRuleResponseTypeDef(BaseValidatorModel):
    FirewallRule: FirewallRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListFirewallRulesResponseTypeDef(BaseValidatorModel):
    FirewallRules: List[FirewallRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateFirewallRuleResponseTypeDef(BaseValidatorModel):
    FirewallRule: FirewallRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateOutpostResolverResponseTypeDef(BaseValidatorModel):
    OutpostResolver: OutpostResolverTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteOutpostResolverResponseTypeDef(BaseValidatorModel):
    OutpostResolver: OutpostResolverTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetOutpostResolverResponseTypeDef(BaseValidatorModel):
    OutpostResolver: OutpostResolverTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListOutpostResolversResponseTypeDef(BaseValidatorModel):
    OutpostResolvers: List[OutpostResolverTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateOutpostResolverResponseTypeDef(BaseValidatorModel):
    OutpostResolver: OutpostResolverTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateResolverEndpointRequestTypeDef(BaseValidatorModel):
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


class CreateResolverQueryLogConfigResponseTypeDef(BaseValidatorModel):
    ResolverQueryLogConfig: ResolverQueryLogConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteResolverQueryLogConfigResponseTypeDef(BaseValidatorModel):
    ResolverQueryLogConfig: ResolverQueryLogConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetResolverQueryLogConfigResponseTypeDef(BaseValidatorModel):
    ResolverQueryLogConfig: ResolverQueryLogConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListResolverQueryLogConfigsResponseTypeDef(BaseValidatorModel):
    TotalCount: int
    TotalFilteredCount: int
    ResolverQueryLogConfigs: List[ResolverQueryLogConfigTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TargetAddressTypeDef(BaseValidatorModel):
    pass


class CreateResolverRuleRequestTypeDef(BaseValidatorModel):
    CreatorRequestId: str
    RuleType: RuleTypeOptionType
    Name: Optional[str] = None
    DomainName: Optional[str] = None
    TargetIps: Optional[Sequence[TargetAddressTypeDef]] = None
    ResolverEndpointId: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class ResolverRuleConfigTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    TargetIps: Optional[Sequence[TargetAddressTypeDef]] = None
    ResolverEndpointId: Optional[str] = None


class ResolverRuleTypeDef(BaseValidatorModel):
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


class ListResolverDnssecConfigsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None


class ListResolverEndpointsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None


class ListResolverQueryLogConfigAssociationsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    SortBy: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None


class ListResolverQueryLogConfigsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    SortBy: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None


class ListResolverRuleAssociationsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None


class ListResolverRulesRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None


class GetFirewallConfigResponseTypeDef(BaseValidatorModel):
    FirewallConfig: FirewallConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListFirewallConfigsResponseTypeDef(BaseValidatorModel):
    FirewallConfigs: List[FirewallConfigTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateFirewallConfigResponseTypeDef(BaseValidatorModel):
    FirewallConfig: FirewallConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListFirewallDomainListsResponseTypeDef(BaseValidatorModel):
    FirewallDomainLists: List[FirewallDomainListMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListFirewallRuleGroupsResponseTypeDef(BaseValidatorModel):
    FirewallRuleGroups: List[FirewallRuleGroupMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetResolverConfigResponseTypeDef(BaseValidatorModel):
    ResolverConfig: ResolverConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListResolverConfigsResponseTypeDef(BaseValidatorModel):
    ResolverConfigs: List[ResolverConfigTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateResolverConfigResponseTypeDef(BaseValidatorModel):
    ResolverConfig: ResolverConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetResolverDnssecConfigResponseTypeDef(BaseValidatorModel):
    ResolverDNSSECConfig: ResolverDnssecConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListResolverDnssecConfigsResponseTypeDef(BaseValidatorModel):
    ResolverDnssecConfigs: List[ResolverDnssecConfigTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateResolverDnssecConfigResponseTypeDef(BaseValidatorModel):
    ResolverDNSSECConfig: ResolverDnssecConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListResolverEndpointIpAddressesResponseTypeDef(BaseValidatorModel):
    MaxResults: int
    IpAddresses: List[IpAddressResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListFirewallConfigsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFirewallDomainListsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFirewallDomainsRequestPaginateTypeDef(BaseValidatorModel):
    FirewallDomainListId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFirewallRuleGroupAssociationsRequestPaginateTypeDef(BaseValidatorModel):
    FirewallRuleGroupId: Optional[str] = None
    VpcId: Optional[str] = None
    Priority: Optional[int] = None
    Status: Optional[FirewallRuleGroupAssociationStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFirewallRuleGroupsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFirewallRulesRequestPaginateTypeDef(BaseValidatorModel):
    FirewallRuleGroupId: str
    Priority: Optional[int] = None
    Action: Optional[ActionType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListOutpostResolversRequestPaginateTypeDef(BaseValidatorModel):
    OutpostArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResolverConfigsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResolverDnssecConfigsRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResolverEndpointIpAddressesRequestPaginateTypeDef(BaseValidatorModel):
    ResolverEndpointId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResolverEndpointsRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResolverQueryLogConfigAssociationsRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    SortBy: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResolverQueryLogConfigsRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    SortBy: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResolverRuleAssociationsRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResolverRulesRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTagsForResourceRequestPaginateTypeDef(BaseValidatorModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class UpdateResolverEndpointRequestTypeDef(BaseValidatorModel):
    ResolverEndpointId: str
    Name: Optional[str] = None
    ResolverEndpointType: Optional[ResolverEndpointTypeType] = None
    UpdateIpAddresses: Optional[Sequence[UpdateIpAddressTypeDef]] = None
    Protocols: Optional[Sequence[ProtocolType]] = None


class UpdateResolverRuleRequestTypeDef(BaseValidatorModel):
    ResolverRuleId: str
    Config: ResolverRuleConfigTypeDef


class CreateResolverRuleResponseTypeDef(BaseValidatorModel):
    ResolverRule: ResolverRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteResolverRuleResponseTypeDef(BaseValidatorModel):
    ResolverRule: ResolverRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetResolverRuleResponseTypeDef(BaseValidatorModel):
    ResolverRule: ResolverRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListResolverRulesResponseTypeDef(BaseValidatorModel):
    MaxResults: int
    ResolverRules: List[ResolverRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateResolverRuleResponseTypeDef(BaseValidatorModel):
    ResolverRule: ResolverRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef



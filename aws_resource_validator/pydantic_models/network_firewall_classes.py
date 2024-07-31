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
from aws_resource_validator.pydantic_models.network_firewall_constants import *

class AddressTypeDef(BaseModel):
    AddressDefinition: str

class AnalysisResultTypeDef(BaseModel):
    IdentifiedRuleIds: Optional[List[str]] = None
    IdentifiedType: Optional[IdentifiedTypeType] = None
    AnalysisDetail: Optional[str] = None

class AssociateFirewallPolicyRequestRequestTypeDef(BaseModel):
    FirewallPolicyArn: str
    UpdateToken: Optional[str] = None
    FirewallArn: Optional[str] = None
    FirewallName: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class SubnetMappingTypeDef(BaseModel):
    SubnetId: str
    IPAddressType: Optional[IPAddressTypeType] = None

class AttachmentTypeDef(BaseModel):
    SubnetId: Optional[str] = None
    EndpointId: Optional[str] = None
    Status: Optional[AttachmentStatusType] = None
    StatusMessage: Optional[str] = None

class IPSetMetadataTypeDef(BaseModel):
    ResolvedCIDRCount: Optional[int] = None

class CheckCertificateRevocationStatusActionsTypeDef(BaseModel):
    RevokedStatusAction: Optional[RevocationCheckActionType] = None
    UnknownStatusAction: Optional[RevocationCheckActionType] = None

class EncryptionConfigurationTypeDef(BaseModel):
    Type: EncryptionTypeType
    KeyId: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class SourceMetadataTypeDef(BaseModel):
    SourceArn: Optional[str] = None
    SourceUpdateToken: Optional[str] = None

class DeleteFirewallPolicyRequestRequestTypeDef(BaseModel):
    FirewallPolicyName: Optional[str] = None
    FirewallPolicyArn: Optional[str] = None

class DeleteFirewallRequestRequestTypeDef(BaseModel):
    FirewallName: Optional[str] = None
    FirewallArn: Optional[str] = None

class DeleteResourcePolicyRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class DeleteRuleGroupRequestRequestTypeDef(BaseModel):
    RuleGroupName: Optional[str] = None
    RuleGroupArn: Optional[str] = None
    Type: Optional[RuleGroupTypeType] = None

class DeleteTLSInspectionConfigurationRequestRequestTypeDef(BaseModel):
    TLSInspectionConfigurationArn: Optional[str] = None
    TLSInspectionConfigurationName: Optional[str] = None

class DescribeFirewallPolicyRequestRequestTypeDef(BaseModel):
    FirewallPolicyName: Optional[str] = None
    FirewallPolicyArn: Optional[str] = None

class DescribeFirewallRequestRequestTypeDef(BaseModel):
    FirewallName: Optional[str] = None
    FirewallArn: Optional[str] = None

class DescribeLoggingConfigurationRequestRequestTypeDef(BaseModel):
    FirewallArn: Optional[str] = None
    FirewallName: Optional[str] = None

class DescribeResourcePolicyRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class DescribeRuleGroupMetadataRequestRequestTypeDef(BaseModel):
    RuleGroupName: Optional[str] = None
    RuleGroupArn: Optional[str] = None
    Type: Optional[RuleGroupTypeType] = None

class StatefulRuleOptionsTypeDef(BaseModel):
    RuleOrder: Optional[RuleOrderType] = None

class DescribeRuleGroupRequestRequestTypeDef(BaseModel):
    RuleGroupName: Optional[str] = None
    RuleGroupArn: Optional[str] = None
    Type: Optional[RuleGroupTypeType] = None
    AnalyzeRuleGroup: Optional[bool] = None

class DescribeTLSInspectionConfigurationRequestRequestTypeDef(BaseModel):
    TLSInspectionConfigurationArn: Optional[str] = None
    TLSInspectionConfigurationName: Optional[str] = None

class DimensionTypeDef(BaseModel):
    Value: str

class DisassociateSubnetsRequestRequestTypeDef(BaseModel):
    SubnetIds: Sequence[str]
    UpdateToken: Optional[str] = None
    FirewallArn: Optional[str] = None
    FirewallName: Optional[str] = None

class FirewallMetadataTypeDef(BaseModel):
    FirewallName: Optional[str] = None
    FirewallArn: Optional[str] = None

class FirewallPolicyMetadataTypeDef(BaseModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None

class StatefulEngineOptionsTypeDef(BaseModel):
    RuleOrder: Optional[RuleOrderType] = None
    StreamExceptionPolicy: Optional[StreamExceptionPolicyType] = None

class StatelessRuleGroupReferenceTypeDef(BaseModel):
    ResourceArn: str
    Priority: int

class HeaderTypeDef(BaseModel):
    Protocol: StatefulRuleProtocolType
    Source: str
    SourcePort: str
    Direction: StatefulRuleDirectionType
    Destination: str
    DestinationPort: str

class IPSetReferenceTypeDef(BaseModel):
    ReferenceArn: Optional[str] = None

class IPSetTypeDef(BaseModel):
    Definition: Sequence[str]

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListFirewallPoliciesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListFirewallsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    VpcIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None

class ListRuleGroupsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Scope: Optional[ResourceManagedStatusType] = None
    ManagedType: Optional[ResourceManagedTypeType] = None
    Type: Optional[RuleGroupTypeType] = None

class RuleGroupMetadataTypeDef(BaseModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None

class ListTLSInspectionConfigurationsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class TLSInspectionConfigurationMetadataTypeDef(BaseModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class LogDestinationConfigTypeDef(BaseModel):
    LogType: LogTypeType
    LogDestinationType: LogDestinationTypeType
    LogDestination: Dict[str, str]

class PortRangeTypeDef(BaseModel):
    FromPort: int
    ToPort: int

class TCPFlagFieldTypeDef(BaseModel):
    Flags: Sequence[TCPFlagType]
    Masks: Optional[Sequence[TCPFlagType]] = None

class PerObjectStatusTypeDef(BaseModel):
    SyncStatus: Optional[PerObjectSyncStatusType] = None
    UpdateToken: Optional[str] = None

class PortSetTypeDef(BaseModel):
    Definition: Optional[Sequence[str]] = None

class PutResourcePolicyRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Policy: str

class RuleOptionTypeDef(BaseModel):
    Keyword: str
    Settings: Optional[Sequence[str]] = None

class RulesSourceListTypeDef(BaseModel):
    Targets: Sequence[str]
    TargetTypes: Sequence[TargetTypeType]
    GeneratedRulesType: GeneratedRulesTypeType

class ServerCertificateTypeDef(BaseModel):
    ResourceArn: Optional[str] = None

class StatefulRuleGroupOverrideTypeDef(BaseModel):
    Action: Optional[Literal["DROP_TO_ALERT"]] = None

class TlsCertificateDataTypeDef(BaseModel):
    CertificateArn: Optional[str] = None
    CertificateSerial: Optional[str] = None
    Status: Optional[str] = None
    StatusMessage: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateFirewallDeleteProtectionRequestRequestTypeDef(BaseModel):
    DeleteProtection: bool
    UpdateToken: Optional[str] = None
    FirewallArn: Optional[str] = None
    FirewallName: Optional[str] = None

class UpdateFirewallDescriptionRequestRequestTypeDef(BaseModel):
    UpdateToken: Optional[str] = None
    FirewallArn: Optional[str] = None
    FirewallName: Optional[str] = None
    Description: Optional[str] = None

class UpdateFirewallPolicyChangeProtectionRequestRequestTypeDef(BaseModel):
    FirewallPolicyChangeProtection: bool
    UpdateToken: Optional[str] = None
    FirewallArn: Optional[str] = None
    FirewallName: Optional[str] = None

class UpdateSubnetChangeProtectionRequestRequestTypeDef(BaseModel):
    SubnetChangeProtection: bool
    UpdateToken: Optional[str] = None
    FirewallArn: Optional[str] = None
    FirewallName: Optional[str] = None

class AssociateFirewallPolicyResponseTypeDef(BaseModel):
    FirewallArn: str
    FirewallName: str
    FirewallPolicyArn: str
    UpdateToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeResourcePolicyResponseTypeDef(BaseModel):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFirewallDeleteProtectionResponseTypeDef(BaseModel):
    FirewallArn: str
    FirewallName: str
    DeleteProtection: bool
    UpdateToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFirewallDescriptionResponseTypeDef(BaseModel):
    FirewallArn: str
    FirewallName: str
    Description: str
    UpdateToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFirewallPolicyChangeProtectionResponseTypeDef(BaseModel):
    UpdateToken: str
    FirewallArn: str
    FirewallName: str
    FirewallPolicyChangeProtection: bool
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSubnetChangeProtectionResponseTypeDef(BaseModel):
    UpdateToken: str
    FirewallArn: str
    FirewallName: str
    SubnetChangeProtection: bool
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateSubnetsRequestRequestTypeDef(BaseModel):
    SubnetMappings: Sequence[SubnetMappingTypeDef]
    UpdateToken: Optional[str] = None
    FirewallArn: Optional[str] = None
    FirewallName: Optional[str] = None

class AssociateSubnetsResponseTypeDef(BaseModel):
    FirewallArn: str
    FirewallName: str
    SubnetMappings: List[SubnetMappingTypeDef]
    UpdateToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateSubnetsResponseTypeDef(BaseModel):
    FirewallArn: str
    FirewallName: str
    SubnetMappings: List[SubnetMappingTypeDef]
    UpdateToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CIDRSummaryTypeDef(BaseModel):
    AvailableCIDRCount: Optional[int] = None
    UtilizedCIDRCount: Optional[int] = None
    IPSetReferences: Optional[Dict[str, IPSetMetadataTypeDef]] = None

class UpdateFirewallEncryptionConfigurationRequestRequestTypeDef(BaseModel):
    UpdateToken: Optional[str] = None
    FirewallArn: Optional[str] = None
    FirewallName: Optional[str] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None

class UpdateFirewallEncryptionConfigurationResponseTypeDef(BaseModel):
    FirewallArn: str
    FirewallName: str
    UpdateToken: str
    EncryptionConfiguration: EncryptionConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFirewallRequestRequestTypeDef(BaseModel):
    FirewallName: str
    FirewallPolicyArn: str
    VpcId: str
    SubnetMappings: Sequence[SubnetMappingTypeDef]
    DeleteProtection: Optional[bool] = None
    SubnetChangeProtection: Optional[bool] = None
    FirewallPolicyChangeProtection: Optional[bool] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None

class FirewallPolicyResponseTypeDef(BaseModel):
    FirewallPolicyName: str
    FirewallPolicyArn: str
    FirewallPolicyId: str
    Description: Optional[str] = None
    FirewallPolicyStatus: Optional[ResourceStatusType] = None
    Tags: Optional[List[TagTypeDef]] = None
    ConsumedStatelessRuleCapacity: Optional[int] = None
    ConsumedStatefulRuleCapacity: Optional[int] = None
    NumberOfAssociations: Optional[int] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None
    LastModifiedTime: Optional[datetime] = None

class FirewallTypeDef(BaseModel):
    FirewallPolicyArn: str
    VpcId: str
    SubnetMappings: List[SubnetMappingTypeDef]
    FirewallId: str
    FirewallName: Optional[str] = None
    FirewallArn: Optional[str] = None
    DeleteProtection: Optional[bool] = None
    SubnetChangeProtection: Optional[bool] = None
    FirewallPolicyChangeProtection: Optional[bool] = None
    Description: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    NextToken: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class RuleGroupResponseTypeDef(BaseModel):
    RuleGroupArn: str
    RuleGroupName: str
    RuleGroupId: str
    Description: Optional[str] = None
    Type: Optional[RuleGroupTypeType] = None
    Capacity: Optional[int] = None
    RuleGroupStatus: Optional[ResourceStatusType] = None
    Tags: Optional[List[TagTypeDef]] = None
    ConsumedCapacity: Optional[int] = None
    NumberOfAssociations: Optional[int] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None
    SourceMetadata: Optional[SourceMetadataTypeDef] = None
    SnsTopic: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    AnalysisResults: Optional[List[AnalysisResultTypeDef]] = None

class DescribeRuleGroupMetadataResponseTypeDef(BaseModel):
    RuleGroupArn: str
    RuleGroupName: str
    Description: str
    Type: RuleGroupTypeType
    Capacity: int
    StatefulRuleOptions: StatefulRuleOptionsTypeDef
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class PublishMetricActionTypeDef(BaseModel):
    Dimensions: Sequence[DimensionTypeDef]

class ListFirewallsResponseTypeDef(BaseModel):
    NextToken: str
    Firewalls: List[FirewallMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListFirewallPoliciesResponseTypeDef(BaseModel):
    NextToken: str
    FirewallPolicies: List[FirewallPolicyMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ReferenceSetsTypeDef(BaseModel):
    IPSetReferences: Optional[Mapping[str, IPSetReferenceTypeDef]] = None

class PolicyVariablesTypeDef(BaseModel):
    RuleVariables: Optional[Mapping[str, IPSetTypeDef]] = None

class ListFirewallPoliciesRequestListFirewallPoliciesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFirewallsRequestListFirewallsPaginateTypeDef(BaseModel):
    VpcIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRuleGroupsRequestListRuleGroupsPaginateTypeDef(BaseModel):
    Scope: Optional[ResourceManagedStatusType] = None
    ManagedType: Optional[ResourceManagedTypeType] = None
    Type: Optional[RuleGroupTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTLSInspectionConfigurationsRequestListTLSInspectionConfigurationsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceRequestListTagsForResourcePaginateTypeDef(BaseModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRuleGroupsResponseTypeDef(BaseModel):
    NextToken: str
    RuleGroups: List[RuleGroupMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTLSInspectionConfigurationsResponseTypeDef(BaseModel):
    NextToken: str
    TLSInspectionConfigurations: List[TLSInspectionConfigurationMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class LoggingConfigurationTypeDef(BaseModel):
    LogDestinationConfigs: List[LogDestinationConfigTypeDef]

class ServerCertificateScopeTypeDef(BaseModel):
    Sources: Optional[Sequence[AddressTypeDef]] = None
    Destinations: Optional[Sequence[AddressTypeDef]] = None
    SourcePorts: Optional[Sequence[PortRangeTypeDef]] = None
    DestinationPorts: Optional[Sequence[PortRangeTypeDef]] = None
    Protocols: Optional[Sequence[int]] = None

class MatchAttributesTypeDef(BaseModel):
    Sources: Optional[Sequence[AddressTypeDef]] = None
    Destinations: Optional[Sequence[AddressTypeDef]] = None
    SourcePorts: Optional[Sequence[PortRangeTypeDef]] = None
    DestinationPorts: Optional[Sequence[PortRangeTypeDef]] = None
    Protocols: Optional[Sequence[int]] = None
    TCPFlags: Optional[Sequence[TCPFlagFieldTypeDef]] = None

class SyncStateTypeDef(BaseModel):
    Attachment: Optional[AttachmentTypeDef] = None
    Config: Optional[Dict[str, PerObjectStatusTypeDef]] = None

class RuleVariablesTypeDef(BaseModel):
    IPSets: Optional[Mapping[str, IPSetTypeDef]] = None
    PortSets: Optional[Mapping[str, PortSetTypeDef]] = None

class StatefulRuleTypeDef(BaseModel):
    Action: StatefulActionType
    Header: HeaderTypeDef
    RuleOptions: Sequence[RuleOptionTypeDef]

class StatefulRuleGroupReferenceTypeDef(BaseModel):
    ResourceArn: str
    Priority: Optional[int] = None
    Override: Optional[StatefulRuleGroupOverrideTypeDef] = None

class TLSInspectionConfigurationResponseTypeDef(BaseModel):
    TLSInspectionConfigurationArn: str
    TLSInspectionConfigurationName: str
    TLSInspectionConfigurationId: str
    TLSInspectionConfigurationStatus: Optional[ResourceStatusType] = None
    Description: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    LastModifiedTime: Optional[datetime] = None
    NumberOfAssociations: Optional[int] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None
    Certificates: Optional[List[TlsCertificateDataTypeDef]] = None
    CertificateAuthority: Optional[TlsCertificateDataTypeDef] = None

class CapacityUsageSummaryTypeDef(BaseModel):
    CIDRs: Optional[CIDRSummaryTypeDef] = None

class CreateFirewallPolicyResponseTypeDef(BaseModel):
    UpdateToken: str
    FirewallPolicyResponse: FirewallPolicyResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFirewallPolicyResponseTypeDef(BaseModel):
    FirewallPolicyResponse: FirewallPolicyResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFirewallPolicyResponseTypeDef(BaseModel):
    UpdateToken: str
    FirewallPolicyResponse: FirewallPolicyResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRuleGroupResponseTypeDef(BaseModel):
    UpdateToken: str
    RuleGroupResponse: RuleGroupResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRuleGroupResponseTypeDef(BaseModel):
    RuleGroupResponse: RuleGroupResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRuleGroupResponseTypeDef(BaseModel):
    UpdateToken: str
    RuleGroupResponse: RuleGroupResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ActionDefinitionTypeDef(BaseModel):
    PublishMetricAction: Optional[PublishMetricActionTypeDef] = None

class DescribeLoggingConfigurationResponseTypeDef(BaseModel):
    FirewallArn: str
    LoggingConfiguration: LoggingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLoggingConfigurationRequestRequestTypeDef(BaseModel):
    FirewallArn: Optional[str] = None
    FirewallName: Optional[str] = None
    LoggingConfiguration: Optional[LoggingConfigurationTypeDef] = None

class UpdateLoggingConfigurationResponseTypeDef(BaseModel):
    FirewallArn: str
    FirewallName: str
    LoggingConfiguration: LoggingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ServerCertificateConfigurationTypeDef(BaseModel):
    ServerCertificates: Optional[Sequence[ServerCertificateTypeDef]] = None
    Scopes: Optional[Sequence[ServerCertificateScopeTypeDef]] = None
    CertificateAuthorityArn: Optional[str] = None
    CheckCertificateRevocationStatus: Optional[       CheckCertificateRevocationStatusActionsTypeDef     ] = None

class RuleDefinitionTypeDef(BaseModel):
    MatchAttributes: MatchAttributesTypeDef
    Actions: Sequence[str]

class CreateTLSInspectionConfigurationResponseTypeDef(BaseModel):
    UpdateToken: str
    TLSInspectionConfigurationResponse: TLSInspectionConfigurationResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTLSInspectionConfigurationResponseTypeDef(BaseModel):
    TLSInspectionConfigurationResponse: TLSInspectionConfigurationResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTLSInspectionConfigurationResponseTypeDef(BaseModel):
    UpdateToken: str
    TLSInspectionConfigurationResponse: TLSInspectionConfigurationResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class FirewallStatusTypeDef(BaseModel):
    Status: FirewallStatusValueType
    ConfigurationSyncStateSummary: ConfigurationSyncStateType
    SyncStates: Optional[Dict[str, SyncStateTypeDef]] = None
    CapacityUsageSummary: Optional[CapacityUsageSummaryTypeDef] = None

class CustomActionTypeDef(BaseModel):
    ActionName: str
    ActionDefinition: ActionDefinitionTypeDef

class TLSInspectionConfigurationTypeDef(BaseModel):
    ServerCertificateConfigurations: Optional[       Sequence[ServerCertificateConfigurationTypeDef]     ] = None

class StatelessRuleTypeDef(BaseModel):
    RuleDefinition: RuleDefinitionTypeDef
    Priority: int

class CreateFirewallResponseTypeDef(BaseModel):
    Firewall: FirewallTypeDef
    FirewallStatus: FirewallStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFirewallResponseTypeDef(BaseModel):
    Firewall: FirewallTypeDef
    FirewallStatus: FirewallStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFirewallResponseTypeDef(BaseModel):
    UpdateToken: str
    Firewall: FirewallTypeDef
    FirewallStatus: FirewallStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class FirewallPolicyTypeDef(BaseModel):
    StatelessDefaultActions: Sequence[str]
    StatelessFragmentDefaultActions: Sequence[str]
    StatelessRuleGroupReferences: Optional[Sequence[StatelessRuleGroupReferenceTypeDef]] = None
    StatelessCustomActions: Optional[Sequence[CustomActionTypeDef]] = None
    StatefulRuleGroupReferences: Optional[Sequence[StatefulRuleGroupReferenceTypeDef]] = None
    StatefulDefaultActions: Optional[Sequence[str]] = None
    StatefulEngineOptions: Optional[StatefulEngineOptionsTypeDef] = None
    TLSInspectionConfigurationArn: Optional[str] = None
    PolicyVariables: Optional[PolicyVariablesTypeDef] = None

class CreateTLSInspectionConfigurationRequestRequestTypeDef(BaseModel):
    TLSInspectionConfigurationName: str
    TLSInspectionConfiguration: TLSInspectionConfigurationTypeDef
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None

class DescribeTLSInspectionConfigurationResponseTypeDef(BaseModel):
    UpdateToken: str
    TLSInspectionConfiguration: TLSInspectionConfigurationTypeDef
    TLSInspectionConfigurationResponse: TLSInspectionConfigurationResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTLSInspectionConfigurationRequestRequestTypeDef(BaseModel):
    TLSInspectionConfiguration: TLSInspectionConfigurationTypeDef
    UpdateToken: str
    TLSInspectionConfigurationArn: Optional[str] = None
    TLSInspectionConfigurationName: Optional[str] = None
    Description: Optional[str] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None

class StatelessRulesAndCustomActionsTypeDef(BaseModel):
    StatelessRules: Sequence[StatelessRuleTypeDef]
    CustomActions: Optional[Sequence[CustomActionTypeDef]] = None

class CreateFirewallPolicyRequestRequestTypeDef(BaseModel):
    FirewallPolicyName: str
    FirewallPolicy: FirewallPolicyTypeDef
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    DryRun: Optional[bool] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None

class DescribeFirewallPolicyResponseTypeDef(BaseModel):
    UpdateToken: str
    FirewallPolicyResponse: FirewallPolicyResponseTypeDef
    FirewallPolicy: FirewallPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFirewallPolicyRequestRequestTypeDef(BaseModel):
    UpdateToken: str
    FirewallPolicy: FirewallPolicyTypeDef
    FirewallPolicyArn: Optional[str] = None
    FirewallPolicyName: Optional[str] = None
    Description: Optional[str] = None
    DryRun: Optional[bool] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None

class RulesSourceTypeDef(BaseModel):
    RulesString: Optional[str] = None
    RulesSourceList: Optional[RulesSourceListTypeDef] = None
    StatefulRules: Optional[Sequence[StatefulRuleTypeDef]] = None
    StatelessRulesAndCustomActions: Optional[StatelessRulesAndCustomActionsTypeDef] = None

class RuleGroupTypeDef(BaseModel):
    RulesSource: RulesSourceTypeDef
    RuleVariables: Optional[RuleVariablesTypeDef] = None
    ReferenceSets: Optional[ReferenceSetsTypeDef] = None
    StatefulRuleOptions: Optional[StatefulRuleOptionsTypeDef] = None

class CreateRuleGroupRequestRequestTypeDef(BaseModel):
    RuleGroupName: str
    Type: RuleGroupTypeType
    Capacity: int
    RuleGroup: Optional[RuleGroupTypeDef] = None
    Rules: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    DryRun: Optional[bool] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None
    SourceMetadata: Optional[SourceMetadataTypeDef] = None
    AnalyzeRuleGroup: Optional[bool] = None

class DescribeRuleGroupResponseTypeDef(BaseModel):
    UpdateToken: str
    RuleGroup: RuleGroupTypeDef
    RuleGroupResponse: RuleGroupResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRuleGroupRequestRequestTypeDef(BaseModel):
    UpdateToken: str
    RuleGroupArn: Optional[str] = None
    RuleGroupName: Optional[str] = None
    RuleGroup: Optional[RuleGroupTypeDef] = None
    Rules: Optional[str] = None
    Type: Optional[RuleGroupTypeType] = None
    Description: Optional[str] = None
    DryRun: Optional[bool] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None
    SourceMetadata: Optional[SourceMetadataTypeDef] = None
    AnalyzeRuleGroup: Optional[bool] = None


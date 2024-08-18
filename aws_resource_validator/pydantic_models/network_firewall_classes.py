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
from aws_resource_validator.pydantic_models.network_firewall_constants import *

class AddressTypeDef(BaseValidatorModel):
    AddressDefinition: str

class AnalysisResultTypeDef(BaseValidatorModel):
    IdentifiedRuleIds: Optional[List[str]] = None
    IdentifiedType: Optional[IdentifiedTypeType] = None
    AnalysisDetail: Optional[str] = None

class AssociateFirewallPolicyRequestRequestTypeDef(BaseValidatorModel):
    FirewallPolicyArn: str
    UpdateToken: Optional[str] = None
    FirewallArn: Optional[str] = None
    FirewallName: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class SubnetMappingTypeDef(BaseValidatorModel):
    SubnetId: str
    IPAddressType: Optional[IPAddressTypeType] = None

class AttachmentTypeDef(BaseValidatorModel):
    SubnetId: Optional[str] = None
    EndpointId: Optional[str] = None
    Status: Optional[AttachmentStatusType] = None
    StatusMessage: Optional[str] = None

class IPSetMetadataTypeDef(BaseValidatorModel):
    ResolvedCIDRCount: Optional[int] = None

class CheckCertificateRevocationStatusActionsTypeDef(BaseValidatorModel):
    RevokedStatusAction: Optional[RevocationCheckActionType] = None
    UnknownStatusAction: Optional[RevocationCheckActionType] = None

class EncryptionConfigurationTypeDef(BaseValidatorModel):
    Type: EncryptionTypeType
    KeyId: Optional[str] = None

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class SourceMetadataTypeDef(BaseValidatorModel):
    SourceArn: Optional[str] = None
    SourceUpdateToken: Optional[str] = None

class DeleteFirewallPolicyRequestRequestTypeDef(BaseValidatorModel):
    FirewallPolicyName: Optional[str] = None
    FirewallPolicyArn: Optional[str] = None

class DeleteFirewallRequestRequestTypeDef(BaseValidatorModel):
    FirewallName: Optional[str] = None
    FirewallArn: Optional[str] = None

class DeleteResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class DeleteRuleGroupRequestRequestTypeDef(BaseValidatorModel):
    RuleGroupName: Optional[str] = None
    RuleGroupArn: Optional[str] = None
    Type: Optional[RuleGroupTypeType] = None

class DeleteTLSInspectionConfigurationRequestRequestTypeDef(BaseValidatorModel):
    TLSInspectionConfigurationArn: Optional[str] = None
    TLSInspectionConfigurationName: Optional[str] = None

class DescribeFirewallPolicyRequestRequestTypeDef(BaseValidatorModel):
    FirewallPolicyName: Optional[str] = None
    FirewallPolicyArn: Optional[str] = None

class DescribeFirewallRequestRequestTypeDef(BaseValidatorModel):
    FirewallName: Optional[str] = None
    FirewallArn: Optional[str] = None

class DescribeLoggingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    FirewallArn: Optional[str] = None
    FirewallName: Optional[str] = None

class DescribeResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class DescribeRuleGroupMetadataRequestRequestTypeDef(BaseValidatorModel):
    RuleGroupName: Optional[str] = None
    RuleGroupArn: Optional[str] = None
    Type: Optional[RuleGroupTypeType] = None

class StatefulRuleOptionsTypeDef(BaseValidatorModel):
    RuleOrder: Optional[RuleOrderType] = None

class DescribeRuleGroupRequestRequestTypeDef(BaseValidatorModel):
    RuleGroupName: Optional[str] = None
    RuleGroupArn: Optional[str] = None
    Type: Optional[RuleGroupTypeType] = None
    AnalyzeRuleGroup: Optional[bool] = None

class DescribeTLSInspectionConfigurationRequestRequestTypeDef(BaseValidatorModel):
    TLSInspectionConfigurationArn: Optional[str] = None
    TLSInspectionConfigurationName: Optional[str] = None

class DimensionTypeDef(BaseValidatorModel):
    Value: str

class DisassociateSubnetsRequestRequestTypeDef(BaseValidatorModel):
    SubnetIds: Sequence[str]
    UpdateToken: Optional[str] = None
    FirewallArn: Optional[str] = None
    FirewallName: Optional[str] = None

class FirewallMetadataTypeDef(BaseValidatorModel):
    FirewallName: Optional[str] = None
    FirewallArn: Optional[str] = None

class FirewallPolicyMetadataTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None

class StatefulEngineOptionsTypeDef(BaseValidatorModel):
    RuleOrder: Optional[RuleOrderType] = None
    StreamExceptionPolicy: Optional[StreamExceptionPolicyType] = None

class StatelessRuleGroupReferenceTypeDef(BaseValidatorModel):
    ResourceArn: str
    Priority: int

class HeaderTypeDef(BaseValidatorModel):
    Protocol: StatefulRuleProtocolType
    Source: str
    SourcePort: str
    Direction: StatefulRuleDirectionType
    Destination: str
    DestinationPort: str

class IPSetReferenceTypeDef(BaseValidatorModel):
    ReferenceArn: Optional[str] = None

class IPSetTypeDef(BaseValidatorModel):
    Definition: Sequence[str]

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListFirewallPoliciesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListFirewallsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    VpcIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None

class ListRuleGroupsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Scope: Optional[ResourceManagedStatusType] = None
    ManagedType: Optional[ResourceManagedTypeType] = None
    Type: Optional[RuleGroupTypeType] = None

class RuleGroupMetadataTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None

class ListTLSInspectionConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class TLSInspectionConfigurationMetadataTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class LogDestinationConfigTypeDef(BaseValidatorModel):
    LogType: LogTypeType
    LogDestinationType: LogDestinationTypeType
    LogDestination: Dict[str, str]

class PortRangeTypeDef(BaseValidatorModel):
    FromPort: int
    ToPort: int

class TCPFlagFieldTypeDef(BaseValidatorModel):
    Flags: Sequence[TCPFlagType]
    Masks: Optional[Sequence[TCPFlagType]] = None

class PerObjectStatusTypeDef(BaseValidatorModel):
    SyncStatus: Optional[PerObjectSyncStatusType] = None
    UpdateToken: Optional[str] = None

class PortSetTypeDef(BaseValidatorModel):
    Definition: Optional[Sequence[str]] = None

class PutResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Policy: str

class RuleOptionTypeDef(BaseValidatorModel):
    Keyword: str
    Settings: Optional[Sequence[str]] = None

class RulesSourceListTypeDef(BaseValidatorModel):
    Targets: Sequence[str]
    TargetTypes: Sequence[TargetTypeType]
    GeneratedRulesType: GeneratedRulesTypeType

class ServerCertificateTypeDef(BaseValidatorModel):
    ResourceArn: Optional[str] = None

class StatefulRuleGroupOverrideTypeDef(BaseValidatorModel):
    Action: Optional[Literal["DROP_TO_ALERT"]] = None

class TlsCertificateDataTypeDef(BaseValidatorModel):
    CertificateArn: Optional[str] = None
    CertificateSerial: Optional[str] = None
    Status: Optional[str] = None
    StatusMessage: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateFirewallDeleteProtectionRequestRequestTypeDef(BaseValidatorModel):
    DeleteProtection: bool
    UpdateToken: Optional[str] = None
    FirewallArn: Optional[str] = None
    FirewallName: Optional[str] = None

class UpdateFirewallDescriptionRequestRequestTypeDef(BaseValidatorModel):
    UpdateToken: Optional[str] = None
    FirewallArn: Optional[str] = None
    FirewallName: Optional[str] = None
    Description: Optional[str] = None

class UpdateFirewallPolicyChangeProtectionRequestRequestTypeDef(BaseValidatorModel):
    FirewallPolicyChangeProtection: bool
    UpdateToken: Optional[str] = None
    FirewallArn: Optional[str] = None
    FirewallName: Optional[str] = None

class UpdateSubnetChangeProtectionRequestRequestTypeDef(BaseValidatorModel):
    SubnetChangeProtection: bool
    UpdateToken: Optional[str] = None
    FirewallArn: Optional[str] = None
    FirewallName: Optional[str] = None

class AssociateFirewallPolicyResponseTypeDef(BaseValidatorModel):
    FirewallArn: str
    FirewallName: str
    FirewallPolicyArn: str
    UpdateToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeResourcePolicyResponseTypeDef(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFirewallDeleteProtectionResponseTypeDef(BaseValidatorModel):
    FirewallArn: str
    FirewallName: str
    DeleteProtection: bool
    UpdateToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFirewallDescriptionResponseTypeDef(BaseValidatorModel):
    FirewallArn: str
    FirewallName: str
    Description: str
    UpdateToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFirewallPolicyChangeProtectionResponseTypeDef(BaseValidatorModel):
    UpdateToken: str
    FirewallArn: str
    FirewallName: str
    FirewallPolicyChangeProtection: bool
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSubnetChangeProtectionResponseTypeDef(BaseValidatorModel):
    UpdateToken: str
    FirewallArn: str
    FirewallName: str
    SubnetChangeProtection: bool
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateSubnetsRequestRequestTypeDef(BaseValidatorModel):
    SubnetMappings: Sequence[SubnetMappingTypeDef]
    UpdateToken: Optional[str] = None
    FirewallArn: Optional[str] = None
    FirewallName: Optional[str] = None

class AssociateSubnetsResponseTypeDef(BaseValidatorModel):
    FirewallArn: str
    FirewallName: str
    SubnetMappings: List[SubnetMappingTypeDef]
    UpdateToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateSubnetsResponseTypeDef(BaseValidatorModel):
    FirewallArn: str
    FirewallName: str
    SubnetMappings: List[SubnetMappingTypeDef]
    UpdateToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CIDRSummaryTypeDef(BaseValidatorModel):
    AvailableCIDRCount: Optional[int] = None
    UtilizedCIDRCount: Optional[int] = None
    IPSetReferences: Optional[Dict[str, IPSetMetadataTypeDef]] = None

class UpdateFirewallEncryptionConfigurationRequestRequestTypeDef(BaseValidatorModel):
    UpdateToken: Optional[str] = None
    FirewallArn: Optional[str] = None
    FirewallName: Optional[str] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None

class UpdateFirewallEncryptionConfigurationResponseTypeDef(BaseValidatorModel):
    FirewallArn: str
    FirewallName: str
    UpdateToken: str
    EncryptionConfiguration: EncryptionConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFirewallRequestRequestTypeDef(BaseValidatorModel):
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

class FirewallPolicyResponseTypeDef(BaseValidatorModel):
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

class FirewallTypeDef(BaseValidatorModel):
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

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    NextToken: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class RuleGroupResponseTypeDef(BaseValidatorModel):
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

class DescribeRuleGroupMetadataResponseTypeDef(BaseValidatorModel):
    RuleGroupArn: str
    RuleGroupName: str
    Description: str
    Type: RuleGroupTypeType
    Capacity: int
    StatefulRuleOptions: StatefulRuleOptionsTypeDef
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class PublishMetricActionTypeDef(BaseValidatorModel):
    Dimensions: Sequence[DimensionTypeDef]

class ListFirewallsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    Firewalls: List[FirewallMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListFirewallPoliciesResponseTypeDef(BaseValidatorModel):
    NextToken: str
    FirewallPolicies: List[FirewallPolicyMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ReferenceSetsTypeDef(BaseValidatorModel):
    IPSetReferences: Optional[Mapping[str, IPSetReferenceTypeDef]] = None

class PolicyVariablesTypeDef(BaseValidatorModel):
    RuleVariables: Optional[Mapping[str, IPSetTypeDef]] = None

class ListFirewallPoliciesRequestListFirewallPoliciesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFirewallsRequestListFirewallsPaginateTypeDef(BaseValidatorModel):
    VpcIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRuleGroupsRequestListRuleGroupsPaginateTypeDef(BaseValidatorModel):
    Scope: Optional[ResourceManagedStatusType] = None
    ManagedType: Optional[ResourceManagedTypeType] = None
    Type: Optional[RuleGroupTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTLSInspectionConfigurationsRequestListTLSInspectionConfigurationsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceRequestListTagsForResourcePaginateTypeDef(BaseValidatorModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRuleGroupsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    RuleGroups: List[RuleGroupMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTLSInspectionConfigurationsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    TLSInspectionConfigurations: List[TLSInspectionConfigurationMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class LoggingConfigurationTypeDef(BaseValidatorModel):
    LogDestinationConfigs: List[LogDestinationConfigTypeDef]

class ServerCertificateScopeTypeDef(BaseValidatorModel):
    Sources: Optional[Sequence[AddressTypeDef]] = None
    Destinations: Optional[Sequence[AddressTypeDef]] = None
    SourcePorts: Optional[Sequence[PortRangeTypeDef]] = None
    DestinationPorts: Optional[Sequence[PortRangeTypeDef]] = None
    Protocols: Optional[Sequence[int]] = None

class MatchAttributesTypeDef(BaseValidatorModel):
    Sources: Optional[Sequence[AddressTypeDef]] = None
    Destinations: Optional[Sequence[AddressTypeDef]] = None
    SourcePorts: Optional[Sequence[PortRangeTypeDef]] = None
    DestinationPorts: Optional[Sequence[PortRangeTypeDef]] = None
    Protocols: Optional[Sequence[int]] = None
    TCPFlags: Optional[Sequence[TCPFlagFieldTypeDef]] = None

class SyncStateTypeDef(BaseValidatorModel):
    Attachment: Optional[AttachmentTypeDef] = None
    Config: Optional[Dict[str, PerObjectStatusTypeDef]] = None

class RuleVariablesTypeDef(BaseValidatorModel):
    IPSets: Optional[Mapping[str, IPSetTypeDef]] = None
    PortSets: Optional[Mapping[str, PortSetTypeDef]] = None

class StatefulRuleTypeDef(BaseValidatorModel):
    Action: StatefulActionType
    Header: HeaderTypeDef
    RuleOptions: Sequence[RuleOptionTypeDef]

class StatefulRuleGroupReferenceTypeDef(BaseValidatorModel):
    ResourceArn: str
    Priority: Optional[int] = None
    Override: Optional[StatefulRuleGroupOverrideTypeDef] = None

class TLSInspectionConfigurationResponseTypeDef(BaseValidatorModel):
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

class CapacityUsageSummaryTypeDef(BaseValidatorModel):
    CIDRs: Optional[CIDRSummaryTypeDef] = None

class CreateFirewallPolicyResponseTypeDef(BaseValidatorModel):
    UpdateToken: str
    FirewallPolicyResponse: FirewallPolicyResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFirewallPolicyResponseTypeDef(BaseValidatorModel):
    FirewallPolicyResponse: FirewallPolicyResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFirewallPolicyResponseTypeDef(BaseValidatorModel):
    UpdateToken: str
    FirewallPolicyResponse: FirewallPolicyResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRuleGroupResponseTypeDef(BaseValidatorModel):
    UpdateToken: str
    RuleGroupResponse: RuleGroupResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRuleGroupResponseTypeDef(BaseValidatorModel):
    RuleGroupResponse: RuleGroupResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRuleGroupResponseTypeDef(BaseValidatorModel):
    UpdateToken: str
    RuleGroupResponse: RuleGroupResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ActionDefinitionTypeDef(BaseValidatorModel):
    PublishMetricAction: Optional[PublishMetricActionTypeDef] = None

class DescribeLoggingConfigurationResponseTypeDef(BaseValidatorModel):
    FirewallArn: str
    LoggingConfiguration: LoggingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLoggingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    FirewallArn: Optional[str] = None
    FirewallName: Optional[str] = None
    LoggingConfiguration: Optional[LoggingConfigurationTypeDef] = None

class UpdateLoggingConfigurationResponseTypeDef(BaseValidatorModel):
    FirewallArn: str
    FirewallName: str
    LoggingConfiguration: LoggingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ServerCertificateConfigurationTypeDef(BaseValidatorModel):
    ServerCertificates: Optional[Sequence[ServerCertificateTypeDef]] = None
    Scopes: Optional[Sequence[ServerCertificateScopeTypeDef]] = None
    CertificateAuthorityArn: Optional[str] = None
    CheckCertificateRevocationStatus: Optional[       CheckCertificateRevocationStatusActionsTypeDef     ] = None

class RuleDefinitionTypeDef(BaseValidatorModel):
    MatchAttributes: MatchAttributesTypeDef
    Actions: Sequence[str]

class CreateTLSInspectionConfigurationResponseTypeDef(BaseValidatorModel):
    UpdateToken: str
    TLSInspectionConfigurationResponse: TLSInspectionConfigurationResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTLSInspectionConfigurationResponseTypeDef(BaseValidatorModel):
    TLSInspectionConfigurationResponse: TLSInspectionConfigurationResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTLSInspectionConfigurationResponseTypeDef(BaseValidatorModel):
    UpdateToken: str
    TLSInspectionConfigurationResponse: TLSInspectionConfigurationResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class FirewallStatusTypeDef(BaseValidatorModel):
    Status: FirewallStatusValueType
    ConfigurationSyncStateSummary: ConfigurationSyncStateType
    SyncStates: Optional[Dict[str, SyncStateTypeDef]] = None
    CapacityUsageSummary: Optional[CapacityUsageSummaryTypeDef] = None

class CustomActionTypeDef(BaseValidatorModel):
    ActionName: str
    ActionDefinition: ActionDefinitionTypeDef

class TLSInspectionConfigurationTypeDef(BaseValidatorModel):
    ServerCertificateConfigurations: Optional[       Sequence[ServerCertificateConfigurationTypeDef]     ] = None

class StatelessRuleTypeDef(BaseValidatorModel):
    RuleDefinition: RuleDefinitionTypeDef
    Priority: int

class CreateFirewallResponseTypeDef(BaseValidatorModel):
    Firewall: FirewallTypeDef
    FirewallStatus: FirewallStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFirewallResponseTypeDef(BaseValidatorModel):
    Firewall: FirewallTypeDef
    FirewallStatus: FirewallStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFirewallResponseTypeDef(BaseValidatorModel):
    UpdateToken: str
    Firewall: FirewallTypeDef
    FirewallStatus: FirewallStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class FirewallPolicyTypeDef(BaseValidatorModel):
    StatelessDefaultActions: Sequence[str]
    StatelessFragmentDefaultActions: Sequence[str]
    StatelessRuleGroupReferences: Optional[Sequence[StatelessRuleGroupReferenceTypeDef]] = None
    StatelessCustomActions: Optional[Sequence[CustomActionTypeDef]] = None
    StatefulRuleGroupReferences: Optional[Sequence[StatefulRuleGroupReferenceTypeDef]] = None
    StatefulDefaultActions: Optional[Sequence[str]] = None
    StatefulEngineOptions: Optional[StatefulEngineOptionsTypeDef] = None
    TLSInspectionConfigurationArn: Optional[str] = None
    PolicyVariables: Optional[PolicyVariablesTypeDef] = None

class CreateTLSInspectionConfigurationRequestRequestTypeDef(BaseValidatorModel):
    TLSInspectionConfigurationName: str
    TLSInspectionConfiguration: TLSInspectionConfigurationTypeDef
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None

class DescribeTLSInspectionConfigurationResponseTypeDef(BaseValidatorModel):
    UpdateToken: str
    TLSInspectionConfiguration: TLSInspectionConfigurationTypeDef
    TLSInspectionConfigurationResponse: TLSInspectionConfigurationResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTLSInspectionConfigurationRequestRequestTypeDef(BaseValidatorModel):
    TLSInspectionConfiguration: TLSInspectionConfigurationTypeDef
    UpdateToken: str
    TLSInspectionConfigurationArn: Optional[str] = None
    TLSInspectionConfigurationName: Optional[str] = None
    Description: Optional[str] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None

class StatelessRulesAndCustomActionsTypeDef(BaseValidatorModel):
    StatelessRules: Sequence[StatelessRuleTypeDef]
    CustomActions: Optional[Sequence[CustomActionTypeDef]] = None

class CreateFirewallPolicyRequestRequestTypeDef(BaseValidatorModel):
    FirewallPolicyName: str
    FirewallPolicy: FirewallPolicyTypeDef
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    DryRun: Optional[bool] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None

class DescribeFirewallPolicyResponseTypeDef(BaseValidatorModel):
    UpdateToken: str
    FirewallPolicyResponse: FirewallPolicyResponseTypeDef
    FirewallPolicy: FirewallPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFirewallPolicyRequestRequestTypeDef(BaseValidatorModel):
    UpdateToken: str
    FirewallPolicy: FirewallPolicyTypeDef
    FirewallPolicyArn: Optional[str] = None
    FirewallPolicyName: Optional[str] = None
    Description: Optional[str] = None
    DryRun: Optional[bool] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None

class RulesSourceTypeDef(BaseValidatorModel):
    RulesString: Optional[str] = None
    RulesSourceList: Optional[RulesSourceListTypeDef] = None
    StatefulRules: Optional[Sequence[StatefulRuleTypeDef]] = None
    StatelessRulesAndCustomActions: Optional[StatelessRulesAndCustomActionsTypeDef] = None

class RuleGroupTypeDef(BaseValidatorModel):
    RulesSource: RulesSourceTypeDef
    RuleVariables: Optional[RuleVariablesTypeDef] = None
    ReferenceSets: Optional[ReferenceSetsTypeDef] = None
    StatefulRuleOptions: Optional[StatefulRuleOptionsTypeDef] = None

class CreateRuleGroupRequestRequestTypeDef(BaseValidatorModel):
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

class DescribeRuleGroupResponseTypeDef(BaseValidatorModel):
    UpdateToken: str
    RuleGroup: RuleGroupTypeDef
    RuleGroupResponse: RuleGroupResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRuleGroupRequestRequestTypeDef(BaseValidatorModel):
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


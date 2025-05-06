from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.network_firewall.network_firewall_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class Address(BaseValidatorModel):
    AddressDefinition: str


class AnalysisReport(BaseValidatorModel):
    AnalysisReportId: Optional[str] = None
    AnalysisType: Optional[EnabledAnalysisTypeType] = None
    ReportTime: Optional[datetime] = None
    Status: Optional[str] = None


class AnalysisResult(BaseValidatorModel):
    IdentifiedRuleIds: Optional[List[str]] = None
    IdentifiedType: Optional[IdentifiedTypeType] = None
    AnalysisDetail: Optional[str] = None


class Hits(BaseValidatorModel):
    Count: Optional[int] = None


class UniqueSources(BaseValidatorModel):
    Count: Optional[int] = None


class AssociateFirewallPolicyRequest(BaseValidatorModel):
    FirewallPolicyArn: str
    UpdateToken: Optional[str] = None
    FirewallArn: Optional[str] = None
    FirewallName: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class SubnetMapping(BaseValidatorModel):
    SubnetId: str
    IPAddressType: Optional[IPAddressTypeType] = None


class Attachment(BaseValidatorModel):
    SubnetId: Optional[str] = None
    EndpointId: Optional[str] = None
    Status: Optional[AttachmentStatusType] = None
    StatusMessage: Optional[str] = None


class IPSetMetadata(BaseValidatorModel):
    ResolvedCIDRCount: Optional[int] = None


class CheckCertificateRevocationStatusActions(BaseValidatorModel):
    RevokedStatusAction: Optional[RevocationCheckActionType] = None
    UnknownStatusAction: Optional[RevocationCheckActionType] = None


class EncryptionConfiguration(BaseValidatorModel):
    Type: EncryptionTypeType
    KeyId: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class SourceMetadata(BaseValidatorModel):
    SourceArn: Optional[str] = None
    SourceUpdateToken: Optional[str] = None


class DeleteFirewallPolicyRequest(BaseValidatorModel):
    FirewallPolicyName: Optional[str] = None
    FirewallPolicyArn: Optional[str] = None


class DeleteFirewallRequest(BaseValidatorModel):
    FirewallName: Optional[str] = None
    FirewallArn: Optional[str] = None


class DeleteResourcePolicyRequest(BaseValidatorModel):
    ResourceArn: str


class DeleteRuleGroupRequest(BaseValidatorModel):
    RuleGroupName: Optional[str] = None
    RuleGroupArn: Optional[str] = None
    Type: Optional[RuleGroupTypeType] = None


class DeleteTLSInspectionConfigurationRequest(BaseValidatorModel):
    TLSInspectionConfigurationArn: Optional[str] = None
    TLSInspectionConfigurationName: Optional[str] = None


class DescribeFirewallPolicyRequest(BaseValidatorModel):
    FirewallPolicyName: Optional[str] = None
    FirewallPolicyArn: Optional[str] = None


class DescribeFirewallRequest(BaseValidatorModel):
    FirewallName: Optional[str] = None
    FirewallArn: Optional[str] = None


class DescribeLoggingConfigurationRequest(BaseValidatorModel):
    FirewallArn: Optional[str] = None
    FirewallName: Optional[str] = None


class DescribeResourcePolicyRequest(BaseValidatorModel):
    ResourceArn: str


class DescribeRuleGroupMetadataRequest(BaseValidatorModel):
    RuleGroupName: Optional[str] = None
    RuleGroupArn: Optional[str] = None
    Type: Optional[RuleGroupTypeType] = None


class StatefulRuleOptions(BaseValidatorModel):
    RuleOrder: Optional[RuleOrderType] = None


class DescribeRuleGroupRequest(BaseValidatorModel):
    RuleGroupName: Optional[str] = None
    RuleGroupArn: Optional[str] = None
    Type: Optional[RuleGroupTypeType] = None
    AnalyzeRuleGroup: Optional[bool] = None


class DescribeTLSInspectionConfigurationRequest(BaseValidatorModel):
    TLSInspectionConfigurationArn: Optional[str] = None
    TLSInspectionConfigurationName: Optional[str] = None


class Dimension(BaseValidatorModel):
    Value: str


class DisassociateSubnetsRequest(BaseValidatorModel):
    SubnetIds: List[str]
    UpdateToken: Optional[str] = None
    FirewallArn: Optional[str] = None
    FirewallName: Optional[str] = None


class FirewallMetadata(BaseValidatorModel):
    FirewallName: Optional[str] = None
    FirewallArn: Optional[str] = None


class FirewallPolicyMetadata(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None


class StatelessRuleGroupReference(BaseValidatorModel):
    ResourceArn: str
    Priority: int


class FlowTimeouts(BaseValidatorModel):
    TcpIdleTimeoutSeconds: Optional[int] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetAnalysisReportResultsRequest(BaseValidatorModel):
    AnalysisReportId: str
    FirewallName: Optional[str] = None
    FirewallArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class Header(BaseValidatorModel):
    Protocol: StatefulRuleProtocolType
    Source: str
    SourcePort: str
    Direction: StatefulRuleDirectionType
    Destination: str
    DestinationPort: str


class IPSetOutput(BaseValidatorModel):
    Definition: List[str]


class IPSetReference(BaseValidatorModel):
    ReferenceArn: Optional[str] = None


class IPSet(BaseValidatorModel):
    Definition: List[str]


class ListAnalysisReportsRequest(BaseValidatorModel):
    FirewallName: Optional[str] = None
    FirewallArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListFirewallPoliciesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListFirewallsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    VpcIds: Optional[List[str]] = None
    MaxResults: Optional[int] = None


class ListRuleGroupsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Scope: Optional[ResourceManagedStatusType] = None
    ManagedType: Optional[ResourceManagedTypeType] = None
    Type: Optional[RuleGroupTypeType] = None


class RuleGroupMetadata(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None


class ListTLSInspectionConfigurationsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class TLSInspectionConfigurationMetadata(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class LogDestinationConfigOutput(BaseValidatorModel):
    LogType: LogTypeType
    LogDestinationType: LogDestinationTypeType
    LogDestination: Dict[str, str]


class LogDestinationConfig(BaseValidatorModel):
    LogType: LogTypeType
    LogDestinationType: LogDestinationTypeType
    LogDestination: Dict[str, str]


class PortRange(BaseValidatorModel):
    FromPort: int
    ToPort: int


class TCPFlagFieldOutput(BaseValidatorModel):
    Flags: List[TCPFlagType]
    Masks: Optional[List[TCPFlagType]] = None


class TCPFlagField(BaseValidatorModel):
    Flags: List[TCPFlagType]
    Masks: Optional[List[TCPFlagType]] = None


class PerObjectStatus(BaseValidatorModel):
    SyncStatus: Optional[PerObjectSyncStatusType] = None
    UpdateToken: Optional[str] = None


class PortSetOutput(BaseValidatorModel):
    Definition: Optional[List[str]] = None


class PortSet(BaseValidatorModel):
    Definition: Optional[List[str]] = None


class PutResourcePolicyRequest(BaseValidatorModel):
    ResourceArn: str
    Policy: str


class RuleOptionOutput(BaseValidatorModel):
    Keyword: str
    Settings: Optional[List[str]] = None


class RuleOption(BaseValidatorModel):
    Keyword: str
    Settings: Optional[List[str]] = None


class RulesSourceListOutput(BaseValidatorModel):
    Targets: List[str]
    TargetTypes: List[TargetTypeType]
    GeneratedRulesType: GeneratedRulesTypeType


class RulesSourceList(BaseValidatorModel):
    Targets: List[str]
    TargetTypes: List[TargetTypeType]
    GeneratedRulesType: GeneratedRulesTypeType


class ServerCertificate(BaseValidatorModel):
    ResourceArn: Optional[str] = None


class StartAnalysisReportRequest(BaseValidatorModel):
    AnalysisType: EnabledAnalysisTypeType
    FirewallName: Optional[str] = None
    FirewallArn: Optional[str] = None


class StatefulRuleGroupOverride(BaseValidatorModel):
    Action: Optional[Literal['DROP_TO_ALERT']] = None


class TlsCertificateData(BaseValidatorModel):
    CertificateArn: Optional[str] = None
    CertificateSerial: Optional[str] = None
    Status: Optional[str] = None
    StatusMessage: Optional[str] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class UpdateFirewallAnalysisSettingsRequest(BaseValidatorModel):
    EnabledAnalysisTypes: Optional[List[EnabledAnalysisTypeType]] = None
    FirewallArn: Optional[str] = None
    FirewallName: Optional[str] = None
    UpdateToken: Optional[str] = None


class UpdateFirewallDeleteProtectionRequest(BaseValidatorModel):
    DeleteProtection: bool
    UpdateToken: Optional[str] = None
    FirewallArn: Optional[str] = None
    FirewallName: Optional[str] = None


class UpdateFirewallDescriptionRequest(BaseValidatorModel):
    UpdateToken: Optional[str] = None
    FirewallArn: Optional[str] = None
    FirewallName: Optional[str] = None
    Description: Optional[str] = None


class UpdateFirewallPolicyChangeProtectionRequest(BaseValidatorModel):
    FirewallPolicyChangeProtection: bool
    UpdateToken: Optional[str] = None
    FirewallArn: Optional[str] = None
    FirewallName: Optional[str] = None


class UpdateSubnetChangeProtectionRequest(BaseValidatorModel):
    SubnetChangeProtection: bool
    UpdateToken: Optional[str] = None
    FirewallArn: Optional[str] = None
    FirewallName: Optional[str] = None


class AnalysisTypeReportResult(BaseValidatorModel):
    Protocol: Optional[str] = None
    FirstAccessed: Optional[datetime] = None
    LastAccessed: Optional[datetime] = None
    Domain: Optional[str] = None
    Hits: Optional[Hits] = None
    UniqueSources: Optional[UniqueSources] = None


class AssociateFirewallPolicyResponse(BaseValidatorModel):
    FirewallArn: str
    FirewallName: str
    FirewallPolicyArn: str
    UpdateToken: str
    ResponseMetadata: ResponseMetadata


class DescribeResourcePolicyResponse(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadata


class ListAnalysisReportsResponse(BaseValidatorModel):
    AnalysisReports: List[AnalysisReport]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class StartAnalysisReportResponse(BaseValidatorModel):
    AnalysisReportId: str
    ResponseMetadata: ResponseMetadata


class UpdateFirewallAnalysisSettingsResponse(BaseValidatorModel):
    EnabledAnalysisTypes: List[EnabledAnalysisTypeType]
    FirewallArn: str
    FirewallName: str
    UpdateToken: str
    ResponseMetadata: ResponseMetadata


class UpdateFirewallDeleteProtectionResponse(BaseValidatorModel):
    FirewallArn: str
    FirewallName: str
    DeleteProtection: bool
    UpdateToken: str
    ResponseMetadata: ResponseMetadata


class UpdateFirewallDescriptionResponse(BaseValidatorModel):
    FirewallArn: str
    FirewallName: str
    Description: str
    UpdateToken: str
    ResponseMetadata: ResponseMetadata


class UpdateFirewallPolicyChangeProtectionResponse(BaseValidatorModel):
    UpdateToken: str
    FirewallArn: str
    FirewallName: str
    FirewallPolicyChangeProtection: bool
    ResponseMetadata: ResponseMetadata


class UpdateSubnetChangeProtectionResponse(BaseValidatorModel):
    UpdateToken: str
    FirewallArn: str
    FirewallName: str
    SubnetChangeProtection: bool
    ResponseMetadata: ResponseMetadata


class AssociateSubnetsRequest(BaseValidatorModel):
    SubnetMappings: List[SubnetMapping]
    UpdateToken: Optional[str] = None
    FirewallArn: Optional[str] = None
    FirewallName: Optional[str] = None


class AssociateSubnetsResponse(BaseValidatorModel):
    FirewallArn: str
    FirewallName: str
    SubnetMappings: List[SubnetMapping]
    UpdateToken: str
    ResponseMetadata: ResponseMetadata


class DisassociateSubnetsResponse(BaseValidatorModel):
    FirewallArn: str
    FirewallName: str
    SubnetMappings: List[SubnetMapping]
    UpdateToken: str
    ResponseMetadata: ResponseMetadata


class CIDRSummary(BaseValidatorModel):
    AvailableCIDRCount: Optional[int] = None
    UtilizedCIDRCount: Optional[int] = None
    IPSetReferences: Optional[Dict[str, IPSetMetadata]] = None


class UpdateFirewallEncryptionConfigurationRequest(BaseValidatorModel):
    UpdateToken: Optional[str] = None
    FirewallArn: Optional[str] = None
    FirewallName: Optional[str] = None
    EncryptionConfiguration: Optional[EncryptionConfiguration] = None


class UpdateFirewallEncryptionConfigurationResponse(BaseValidatorModel):
    FirewallArn: str
    FirewallName: str
    UpdateToken: str
    EncryptionConfiguration: EncryptionConfiguration
    ResponseMetadata: ResponseMetadata


class CreateFirewallRequest(BaseValidatorModel):
    FirewallName: str
    FirewallPolicyArn: str
    VpcId: Optional[str] = None
    SubnetMappings: Optional[List[SubnetMapping]] = None
    DeleteProtection: Optional[bool] = None
    SubnetChangeProtection: Optional[bool] = None
    FirewallPolicyChangeProtection: Optional[bool] = None
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    EncryptionConfiguration: Optional[EncryptionConfiguration] = None
    EnabledAnalysisTypes: Optional[List[EnabledAnalysisTypeType]] = None


class FirewallPolicyResponse(BaseValidatorModel):
    FirewallPolicyName: str
    FirewallPolicyArn: str
    FirewallPolicyId: str
    Description: Optional[str] = None
    FirewallPolicyStatus: Optional[ResourceStatusType] = None
    Tags: Optional[List[Tag]] = None
    ConsumedStatelessRuleCapacity: Optional[int] = None
    ConsumedStatefulRuleCapacity: Optional[int] = None
    NumberOfAssociations: Optional[int] = None
    EncryptionConfiguration: Optional[EncryptionConfiguration] = None
    LastModifiedTime: Optional[datetime] = None


class Firewall(BaseValidatorModel):
    FirewallPolicyArn: str
    VpcId: str
    SubnetMappings: List[SubnetMapping]
    FirewallId: str
    FirewallName: Optional[str] = None
    FirewallArn: Optional[str] = None
    DeleteProtection: Optional[bool] = None
    SubnetChangeProtection: Optional[bool] = None
    FirewallPolicyChangeProtection: Optional[bool] = None
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    EncryptionConfiguration: Optional[EncryptionConfiguration] = None
    EnabledAnalysisTypes: Optional[List[EnabledAnalysisTypeType]] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]


class RuleGroupResponse(BaseValidatorModel):
    RuleGroupArn: str
    RuleGroupName: str
    RuleGroupId: str
    Description: Optional[str] = None
    Type: Optional[RuleGroupTypeType] = None
    Capacity: Optional[int] = None
    RuleGroupStatus: Optional[ResourceStatusType] = None
    Tags: Optional[List[Tag]] = None
    ConsumedCapacity: Optional[int] = None
    NumberOfAssociations: Optional[int] = None
    EncryptionConfiguration: Optional[EncryptionConfiguration] = None
    SourceMetadata: Optional[SourceMetadata] = None
    SnsTopic: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    AnalysisResults: Optional[List[AnalysisResult]] = None


class DescribeRuleGroupMetadataResponse(BaseValidatorModel):
    RuleGroupArn: str
    RuleGroupName: str
    Description: str
    Type: RuleGroupTypeType
    Capacity: int
    StatefulRuleOptions: StatefulRuleOptions
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadata


class PublishMetricActionOutput(BaseValidatorModel):
    Dimensions: List[Dimension]


class PublishMetricAction(BaseValidatorModel):
    Dimensions: List[Dimension]


class ListFirewallsResponse(BaseValidatorModel):
    Firewalls: List[FirewallMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListFirewallPoliciesResponse(BaseValidatorModel):
    FirewallPolicies: List[FirewallPolicyMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class StatefulEngineOptions(BaseValidatorModel):
    RuleOrder: Optional[RuleOrderType] = None
    StreamExceptionPolicy: Optional[StreamExceptionPolicyType] = None
    FlowTimeouts: Optional[FlowTimeouts] = None


class GetAnalysisReportResultsRequestPaginate(BaseValidatorModel):
    AnalysisReportId: str
    FirewallName: Optional[str] = None
    FirewallArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAnalysisReportsRequestPaginate(BaseValidatorModel):
    FirewallName: Optional[str] = None
    FirewallArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFirewallPoliciesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFirewallsRequestPaginate(BaseValidatorModel):
    VpcIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRuleGroupsRequestPaginate(BaseValidatorModel):
    Scope: Optional[ResourceManagedStatusType] = None
    ManagedType: Optional[ResourceManagedTypeType] = None
    Type: Optional[RuleGroupTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTLSInspectionConfigurationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTagsForResourceRequestPaginate(BaseValidatorModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class PolicyVariablesOutput(BaseValidatorModel):
    RuleVariables: Optional[Dict[str, IPSetOutput]] = None


class ReferenceSetsOutput(BaseValidatorModel):
    IPSetReferences: Optional[Dict[str, IPSetReference]] = None


class ReferenceSets(BaseValidatorModel):
    IPSetReferences: Optional[Dict[str, IPSetReference]] = None


class PolicyVariables(BaseValidatorModel):
    RuleVariables: Optional[Dict[str, IPSet]] = None


class ListRuleGroupsResponse(BaseValidatorModel):
    RuleGroups: List[RuleGroupMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTLSInspectionConfigurationsResponse(BaseValidatorModel):
    TLSInspectionConfigurations: List[TLSInspectionConfigurationMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class LoggingConfigurationOutput(BaseValidatorModel):
    LogDestinationConfigs: List[LogDestinationConfigOutput]


class LoggingConfiguration(BaseValidatorModel):
    LogDestinationConfigs: List[LogDestinationConfig]


class ServerCertificateScopeOutput(BaseValidatorModel):
    Sources: Optional[List[Address]] = None
    Destinations: Optional[List[Address]] = None
    SourcePorts: Optional[List[PortRange]] = None
    DestinationPorts: Optional[List[PortRange]] = None
    Protocols: Optional[List[int]] = None


class ServerCertificateScope(BaseValidatorModel):
    Sources: Optional[List[Address]] = None
    Destinations: Optional[List[Address]] = None
    SourcePorts: Optional[List[PortRange]] = None
    DestinationPorts: Optional[List[PortRange]] = None
    Protocols: Optional[List[int]] = None


class MatchAttributesOutput(BaseValidatorModel):
    Sources: Optional[List[Address]] = None
    Destinations: Optional[List[Address]] = None
    SourcePorts: Optional[List[PortRange]] = None
    DestinationPorts: Optional[List[PortRange]] = None
    Protocols: Optional[List[int]] = None
    TCPFlags: Optional[List[TCPFlagFieldOutput]] = None


class MatchAttributes(BaseValidatorModel):
    Sources: Optional[List[Address]] = None
    Destinations: Optional[List[Address]] = None
    SourcePorts: Optional[List[PortRange]] = None
    DestinationPorts: Optional[List[PortRange]] = None
    Protocols: Optional[List[int]] = None
    TCPFlags: Optional[List[TCPFlagField]] = None


class SyncState(BaseValidatorModel):
    Attachment: Optional[Attachment] = None
    Config: Optional[Dict[str, PerObjectStatus]] = None


class RuleVariablesOutput(BaseValidatorModel):
    IPSets: Optional[Dict[str, IPSetOutput]] = None
    PortSets: Optional[Dict[str, PortSetOutput]] = None


class RuleVariables(BaseValidatorModel):
    IPSets: Optional[Dict[str, IPSet]] = None
    PortSets: Optional[Dict[str, PortSet]] = None


class StatefulRuleOutput(BaseValidatorModel):
    Action: StatefulActionType
    Header: Header
    RuleOptions: List[RuleOptionOutput]


class StatefulRule(BaseValidatorModel):
    Action: StatefulActionType
    Header: Header
    RuleOptions: List[RuleOption]


class StatefulRuleGroupReference(BaseValidatorModel):
    ResourceArn: str
    Priority: Optional[int] = None
    Override: Optional[StatefulRuleGroupOverride] = None


class TLSInspectionConfigurationResponse(BaseValidatorModel):
    TLSInspectionConfigurationArn: str
    TLSInspectionConfigurationName: str
    TLSInspectionConfigurationId: str
    TLSInspectionConfigurationStatus: Optional[ResourceStatusType] = None
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    LastModifiedTime: Optional[datetime] = None
    NumberOfAssociations: Optional[int] = None
    EncryptionConfiguration: Optional[EncryptionConfiguration] = None
    Certificates: Optional[List[TlsCertificateData]] = None
    CertificateAuthority: Optional[TlsCertificateData] = None


class GetAnalysisReportResultsResponse(BaseValidatorModel):
    Status: str
    StartTime: datetime
    EndTime: datetime
    ReportTime: datetime
    AnalysisType: EnabledAnalysisTypeType
    AnalysisReportResults: List[AnalysisTypeReportResult]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CapacityUsageSummary(BaseValidatorModel):
    CIDRs: Optional[CIDRSummary] = None


class CreateFirewallPolicyResponse(BaseValidatorModel):
    UpdateToken: str
    FirewallPolicyResponse: FirewallPolicyResponse
    ResponseMetadata: ResponseMetadata


class DeleteFirewallPolicyResponse(BaseValidatorModel):
    FirewallPolicyResponse: FirewallPolicyResponse
    ResponseMetadata: ResponseMetadata


class UpdateFirewallPolicyResponse(BaseValidatorModel):
    UpdateToken: str
    FirewallPolicyResponse: FirewallPolicyResponse
    ResponseMetadata: ResponseMetadata


class CreateRuleGroupResponse(BaseValidatorModel):
    UpdateToken: str
    RuleGroupResponse: RuleGroupResponse
    ResponseMetadata: ResponseMetadata


class DeleteRuleGroupResponse(BaseValidatorModel):
    RuleGroupResponse: RuleGroupResponse
    ResponseMetadata: ResponseMetadata


class UpdateRuleGroupResponse(BaseValidatorModel):
    UpdateToken: str
    RuleGroupResponse: RuleGroupResponse
    ResponseMetadata: ResponseMetadata


class ActionDefinitionOutput(BaseValidatorModel):
    PublishMetricAction: Optional[PublishMetricActionOutput] = None


class ActionDefinition(BaseValidatorModel):
    PublishMetricAction: Optional[PublishMetricAction] = None


class DescribeLoggingConfigurationResponse(BaseValidatorModel):
    FirewallArn: str
    LoggingConfiguration: LoggingConfigurationOutput
    ResponseMetadata: ResponseMetadata


class UpdateLoggingConfigurationResponse(BaseValidatorModel):
    FirewallArn: str
    FirewallName: str
    LoggingConfiguration: LoggingConfigurationOutput
    ResponseMetadata: ResponseMetadata

LoggingConfigurationUnion = Union[LoggingConfiguration, LoggingConfigurationOutput]


class ServerCertificateConfigurationOutput(BaseValidatorModel):
    ServerCertificates: Optional[List[ServerCertificate]] = None
    Scopes: Optional[List[ServerCertificateScopeOutput]] = None
    CertificateAuthorityArn: Optional[str] = None
    CheckCertificateRevocationStatus: Optional[CheckCertificateRevocationStatusActions] = None


class ServerCertificateConfiguration(BaseValidatorModel):
    ServerCertificates: Optional[List[ServerCertificate]] = None
    Scopes: Optional[List[ServerCertificateScope]] = None
    CertificateAuthorityArn: Optional[str] = None
    CheckCertificateRevocationStatus: Optional[CheckCertificateRevocationStatusActions] = None


class RuleDefinitionOutput(BaseValidatorModel):
    MatchAttributes: MatchAttributesOutput
    Actions: List[str]


class RuleDefinition(BaseValidatorModel):
    MatchAttributes: MatchAttributes
    Actions: List[str]


class CreateTLSInspectionConfigurationResponse(BaseValidatorModel):
    UpdateToken: str
    TLSInspectionConfigurationResponse: TLSInspectionConfigurationResponse
    ResponseMetadata: ResponseMetadata


class DeleteTLSInspectionConfigurationResponse(BaseValidatorModel):
    TLSInspectionConfigurationResponse: TLSInspectionConfigurationResponse
    ResponseMetadata: ResponseMetadata


class UpdateTLSInspectionConfigurationResponse(BaseValidatorModel):
    UpdateToken: str
    TLSInspectionConfigurationResponse: TLSInspectionConfigurationResponse
    ResponseMetadata: ResponseMetadata


class FirewallStatus(BaseValidatorModel):
    Status: FirewallStatusValueType
    ConfigurationSyncStateSummary: ConfigurationSyncStateType
    SyncStates: Optional[Dict[str, SyncState]] = None
    CapacityUsageSummary: Optional[CapacityUsageSummary] = None


class CustomActionOutput(BaseValidatorModel):
    ActionName: str
    ActionDefinition: ActionDefinitionOutput


class CustomAction(BaseValidatorModel):
    ActionName: str
    ActionDefinition: ActionDefinition


class UpdateLoggingConfigurationRequest(BaseValidatorModel):
    FirewallArn: Optional[str] = None
    FirewallName: Optional[str] = None
    LoggingConfiguration: Optional[LoggingConfigurationUnion] = None


class TLSInspectionConfigurationOutput(BaseValidatorModel):
    ServerCertificateConfigurations: Optional[List[ServerCertificateConfigurationOutput]] = None


class TLSInspectionConfiguration(BaseValidatorModel):
    ServerCertificateConfigurations: Optional[List[ServerCertificateConfiguration]] = None


class StatelessRuleOutput(BaseValidatorModel):
    RuleDefinition: RuleDefinitionOutput
    Priority: int


class StatelessRule(BaseValidatorModel):
    RuleDefinition: RuleDefinition
    Priority: int


class CreateFirewallResponse(BaseValidatorModel):
    Firewall: Firewall
    FirewallStatus: FirewallStatus
    ResponseMetadata: ResponseMetadata


class DeleteFirewallResponse(BaseValidatorModel):
    Firewall: Firewall
    FirewallStatus: FirewallStatus
    ResponseMetadata: ResponseMetadata


class DescribeFirewallResponse(BaseValidatorModel):
    UpdateToken: str
    Firewall: Firewall
    FirewallStatus: FirewallStatus
    ResponseMetadata: ResponseMetadata


class FirewallPolicyOutput(BaseValidatorModel):
    StatelessDefaultActions: List[str]
    StatelessFragmentDefaultActions: List[str]
    StatelessRuleGroupReferences: Optional[List[StatelessRuleGroupReference]] = None
    StatelessCustomActions: Optional[List[CustomActionOutput]] = None
    StatefulRuleGroupReferences: Optional[List[StatefulRuleGroupReference]] = None
    StatefulDefaultActions: Optional[List[str]] = None
    StatefulEngineOptions: Optional[StatefulEngineOptions] = None
    TLSInspectionConfigurationArn: Optional[str] = None
    PolicyVariables: Optional[PolicyVariablesOutput] = None


class FirewallPolicy(BaseValidatorModel):
    StatelessDefaultActions: List[str]
    StatelessFragmentDefaultActions: List[str]
    StatelessRuleGroupReferences: Optional[List[StatelessRuleGroupReference]] = None
    StatelessCustomActions: Optional[List[CustomAction]] = None
    StatefulRuleGroupReferences: Optional[List[StatefulRuleGroupReference]] = None
    StatefulDefaultActions: Optional[List[str]] = None
    StatefulEngineOptions: Optional[StatefulEngineOptions] = None
    TLSInspectionConfigurationArn: Optional[str] = None
    PolicyVariables: Optional[PolicyVariables] = None


class DescribeTLSInspectionConfigurationResponse(BaseValidatorModel):
    UpdateToken: str
    TLSInspectionConfiguration: TLSInspectionConfigurationOutput
    TLSInspectionConfigurationResponse: TLSInspectionConfigurationResponse
    ResponseMetadata: ResponseMetadata

TLSInspectionConfigurationUnion = Union[TLSInspectionConfiguration, TLSInspectionConfigurationOutput]


class StatelessRulesAndCustomActionsOutput(BaseValidatorModel):
    StatelessRules: List[StatelessRuleOutput]
    CustomActions: Optional[List[CustomActionOutput]] = None


class StatelessRulesAndCustomActions(BaseValidatorModel):
    StatelessRules: List[StatelessRule]
    CustomActions: Optional[List[CustomAction]] = None


class DescribeFirewallPolicyResponse(BaseValidatorModel):
    UpdateToken: str
    FirewallPolicyResponse: FirewallPolicyResponse
    FirewallPolicy: FirewallPolicyOutput
    ResponseMetadata: ResponseMetadata

FirewallPolicyUnion = Union[FirewallPolicy, FirewallPolicyOutput]


class CreateTLSInspectionConfigurationRequest(BaseValidatorModel):
    TLSInspectionConfigurationName: str
    TLSInspectionConfiguration: TLSInspectionConfigurationUnion
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    EncryptionConfiguration: Optional[EncryptionConfiguration] = None


class UpdateTLSInspectionConfigurationRequest(BaseValidatorModel):
    TLSInspectionConfiguration: TLSInspectionConfigurationUnion
    UpdateToken: str
    TLSInspectionConfigurationArn: Optional[str] = None
    TLSInspectionConfigurationName: Optional[str] = None
    Description: Optional[str] = None
    EncryptionConfiguration: Optional[EncryptionConfiguration] = None


class RulesSourceOutput(BaseValidatorModel):
    RulesString: Optional[str] = None
    RulesSourceList: Optional[RulesSourceListOutput] = None
    StatefulRules: Optional[List[StatefulRuleOutput]] = None
    StatelessRulesAndCustomActions: Optional[StatelessRulesAndCustomActionsOutput] = None


class RulesSource(BaseValidatorModel):
    RulesString: Optional[str] = None
    RulesSourceList: Optional[RulesSourceList] = None
    StatefulRules: Optional[List[StatefulRule]] = None
    StatelessRulesAndCustomActions: Optional[StatelessRulesAndCustomActions] = None


class CreateFirewallPolicyRequest(BaseValidatorModel):
    FirewallPolicyName: str
    FirewallPolicy: FirewallPolicyUnion
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    DryRun: Optional[bool] = None
    EncryptionConfiguration: Optional[EncryptionConfiguration] = None


class UpdateFirewallPolicyRequest(BaseValidatorModel):
    UpdateToken: str
    FirewallPolicy: FirewallPolicyUnion
    FirewallPolicyArn: Optional[str] = None
    FirewallPolicyName: Optional[str] = None
    Description: Optional[str] = None
    DryRun: Optional[bool] = None
    EncryptionConfiguration: Optional[EncryptionConfiguration] = None


class RuleGroupOutput(BaseValidatorModel):
    RulesSource: RulesSourceOutput
    RuleVariables: Optional[RuleVariablesOutput] = None
    ReferenceSets: Optional[ReferenceSetsOutput] = None
    StatefulRuleOptions: Optional[StatefulRuleOptions] = None


class RuleGroup(BaseValidatorModel):
    RulesSource: RulesSource
    RuleVariables: Optional[RuleVariables] = None
    ReferenceSets: Optional[ReferenceSets] = None
    StatefulRuleOptions: Optional[StatefulRuleOptions] = None


class DescribeRuleGroupResponse(BaseValidatorModel):
    UpdateToken: str
    RuleGroup: RuleGroupOutput
    RuleGroupResponse: RuleGroupResponse
    ResponseMetadata: ResponseMetadata

RuleGroupUnion = Union[RuleGroup, RuleGroupOutput]


class CreateRuleGroupRequest(BaseValidatorModel):
    RuleGroupName: str
    Type: RuleGroupTypeType
    Capacity: int
    RuleGroup: Optional[RuleGroupUnion] = None
    Rules: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    DryRun: Optional[bool] = None
    EncryptionConfiguration: Optional[EncryptionConfiguration] = None
    SourceMetadata: Optional[SourceMetadata] = None
    AnalyzeRuleGroup: Optional[bool] = None


class UpdateRuleGroupRequest(BaseValidatorModel):
    UpdateToken: str
    RuleGroupArn: Optional[str] = None
    RuleGroupName: Optional[str] = None
    RuleGroup: Optional[RuleGroupUnion] = None
    Rules: Optional[str] = None
    Type: Optional[RuleGroupTypeType] = None
    Description: Optional[str] = None
    DryRun: Optional[bool] = None
    EncryptionConfiguration: Optional[EncryptionConfiguration] = None
    SourceMetadata: Optional[SourceMetadata] = None
    AnalyzeRuleGroup: Optional[bool] = None
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
from aws_resource_validator.pydantic_models.network_firewall_constants import *

class AddressTypeDef(BaseValidatorModel):
    AddressDefinition: str


class AnalysisReportTypeDef(BaseValidatorModel):
    AnalysisReportId: Optional[str] = None
    AnalysisType: Optional[EnabledAnalysisTypeType] = None
    ReportTime: Optional[datetime] = None
    Status: Optional[str] = None


class AnalysisResultTypeDef(BaseValidatorModel):
    IdentifiedRuleIds: Optional[List[str]] = None
    IdentifiedType: Optional[IdentifiedTypeType] = None
    AnalysisDetail: Optional[str] = None


class HitsTypeDef(BaseValidatorModel):
    Count: Optional[int] = None


class UniqueSourcesTypeDef(BaseValidatorModel):
    Count: Optional[int] = None


class AssociateFirewallPolicyRequestTypeDef(BaseValidatorModel):
    FirewallPolicyArn: str
    UpdateToken: Optional[str] = None
    FirewallArn: Optional[str] = None
    FirewallName: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


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


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class SourceMetadataTypeDef(BaseValidatorModel):
    SourceArn: Optional[str] = None
    SourceUpdateToken: Optional[str] = None


class DeleteFirewallPolicyRequestTypeDef(BaseValidatorModel):
    FirewallPolicyName: Optional[str] = None
    FirewallPolicyArn: Optional[str] = None


class DeleteFirewallRequestTypeDef(BaseValidatorModel):
    FirewallName: Optional[str] = None
    FirewallArn: Optional[str] = None


class DeleteResourcePolicyRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class DeleteTLSInspectionConfigurationRequestTypeDef(BaseValidatorModel):
    TLSInspectionConfigurationArn: Optional[str] = None
    TLSInspectionConfigurationName: Optional[str] = None


class DescribeFirewallPolicyRequestTypeDef(BaseValidatorModel):
    FirewallPolicyName: Optional[str] = None
    FirewallPolicyArn: Optional[str] = None


class DescribeFirewallRequestTypeDef(BaseValidatorModel):
    FirewallName: Optional[str] = None
    FirewallArn: Optional[str] = None


class DescribeLoggingConfigurationRequestTypeDef(BaseValidatorModel):
    FirewallArn: Optional[str] = None
    FirewallName: Optional[str] = None


class DescribeResourcePolicyRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class StatefulRuleOptionsTypeDef(BaseValidatorModel):
    RuleOrder: Optional[RuleOrderType] = None


class DescribeTLSInspectionConfigurationRequestTypeDef(BaseValidatorModel):
    TLSInspectionConfigurationArn: Optional[str] = None
    TLSInspectionConfigurationName: Optional[str] = None


class DimensionTypeDef(BaseValidatorModel):
    Value: str


class DisassociateSubnetsRequestTypeDef(BaseValidatorModel):
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


class StatelessRuleGroupReferenceTypeDef(BaseValidatorModel):
    ResourceArn: str
    Priority: int


class FlowTimeoutsTypeDef(BaseValidatorModel):
    TcpIdleTimeoutSeconds: Optional[int] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetAnalysisReportResultsRequestTypeDef(BaseValidatorModel):
    AnalysisReportId: str
    FirewallName: Optional[str] = None
    FirewallArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class IPSetOutputTypeDef(BaseValidatorModel):
    Definition: List[str]


class IPSetReferenceTypeDef(BaseValidatorModel):
    ReferenceArn: Optional[str] = None


class IPSetTypeDef(BaseValidatorModel):
    Definition: Sequence[str]


class ListAnalysisReportsRequestTypeDef(BaseValidatorModel):
    FirewallName: Optional[str] = None
    FirewallArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListFirewallPoliciesRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListFirewallsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    VpcIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None


class RuleGroupMetadataTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None


class ListTLSInspectionConfigurationsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class TLSInspectionConfigurationMetadataTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class LogDestinationConfigOutputTypeDef(BaseValidatorModel):
    LogType: LogTypeType
    LogDestinationType: LogDestinationTypeType
    LogDestination: Dict[str, str]


class LogDestinationConfigTypeDef(BaseValidatorModel):
    LogType: LogTypeType
    LogDestinationType: LogDestinationTypeType
    LogDestination: Mapping[str, str]


class PortRangeTypeDef(BaseValidatorModel):
    FromPort: int
    ToPort: int


class TCPFlagFieldOutputTypeDef(BaseValidatorModel):
    Flags: List[TCPFlagType]
    Masks: Optional[List[TCPFlagType]] = None


class TCPFlagFieldTypeDef(BaseValidatorModel):
    Flags: Sequence[TCPFlagType]
    Masks: Optional[Sequence[TCPFlagType]] = None


class PerObjectStatusTypeDef(BaseValidatorModel):
    SyncStatus: Optional[PerObjectSyncStatusType] = None
    UpdateToken: Optional[str] = None


class PortSetOutputTypeDef(BaseValidatorModel):
    Definition: Optional[List[str]] = None


class PortSetTypeDef(BaseValidatorModel):
    Definition: Optional[Sequence[str]] = None


class PutResourcePolicyRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Policy: str


class RuleOptionOutputTypeDef(BaseValidatorModel):
    Keyword: str
    Settings: Optional[List[str]] = None


class RuleOptionTypeDef(BaseValidatorModel):
    Keyword: str
    Settings: Optional[Sequence[str]] = None


class RulesSourceListOutputTypeDef(BaseValidatorModel):
    Targets: List[str]
    TargetTypes: List[TargetTypeType]
    GeneratedRulesType: GeneratedRulesTypeType


class RulesSourceListTypeDef(BaseValidatorModel):
    Targets: Sequence[str]
    TargetTypes: Sequence[TargetTypeType]
    GeneratedRulesType: GeneratedRulesTypeType


class ServerCertificateTypeDef(BaseValidatorModel):
    ResourceArn: Optional[str] = None


class StartAnalysisReportRequestTypeDef(BaseValidatorModel):
    AnalysisType: EnabledAnalysisTypeType
    FirewallName: Optional[str] = None
    FirewallArn: Optional[str] = None


class StatefulRuleGroupOverrideTypeDef(BaseValidatorModel):
    Action: Optional[Literal["DROP_TO_ALERT"]] = None


class TlsCertificateDataTypeDef(BaseValidatorModel):
    CertificateArn: Optional[str] = None
    CertificateSerial: Optional[str] = None
    Status: Optional[str] = None
    StatusMessage: Optional[str] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateFirewallAnalysisSettingsRequestTypeDef(BaseValidatorModel):
    EnabledAnalysisTypes: Optional[Sequence[EnabledAnalysisTypeType]] = None
    FirewallArn: Optional[str] = None
    FirewallName: Optional[str] = None
    UpdateToken: Optional[str] = None


class UpdateFirewallDeleteProtectionRequestTypeDef(BaseValidatorModel):
    DeleteProtection: bool
    UpdateToken: Optional[str] = None
    FirewallArn: Optional[str] = None
    FirewallName: Optional[str] = None


class UpdateFirewallDescriptionRequestTypeDef(BaseValidatorModel):
    UpdateToken: Optional[str] = None
    FirewallArn: Optional[str] = None
    FirewallName: Optional[str] = None
    Description: Optional[str] = None


class UpdateFirewallPolicyChangeProtectionRequestTypeDef(BaseValidatorModel):
    FirewallPolicyChangeProtection: bool
    UpdateToken: Optional[str] = None
    FirewallArn: Optional[str] = None
    FirewallName: Optional[str] = None


class UpdateSubnetChangeProtectionRequestTypeDef(BaseValidatorModel):
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


class ListAnalysisReportsResponseTypeDef(BaseValidatorModel):
    AnalysisReports: List[AnalysisReportTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class StartAnalysisReportResponseTypeDef(BaseValidatorModel):
    AnalysisReportId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateFirewallAnalysisSettingsResponseTypeDef(BaseValidatorModel):
    EnabledAnalysisTypes: List[EnabledAnalysisTypeType]
    FirewallArn: str
    FirewallName: str
    UpdateToken: str
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


class AssociateSubnetsRequestTypeDef(BaseValidatorModel):
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


class EncryptionConfigurationTypeDef(BaseValidatorModel):
    pass


class UpdateFirewallEncryptionConfigurationRequestTypeDef(BaseValidatorModel):
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


class CreateFirewallRequestTypeDef(BaseValidatorModel):
    FirewallName: str
    FirewallPolicyArn: str
    VpcId: Optional[str] = None
    SubnetMappings: Optional[Sequence[SubnetMappingTypeDef]] = None
    DeleteProtection: Optional[bool] = None
    SubnetChangeProtection: Optional[bool] = None
    FirewallPolicyChangeProtection: Optional[bool] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None
    EnabledAnalysisTypes: Optional[Sequence[EnabledAnalysisTypeType]] = None


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
    EnabledAnalysisTypes: Optional[List[EnabledAnalysisTypeType]] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]


class PublishMetricActionOutputTypeDef(BaseValidatorModel):
    Dimensions: List[DimensionTypeDef]


class PublishMetricActionTypeDef(BaseValidatorModel):
    Dimensions: Sequence[DimensionTypeDef]


class ListFirewallsResponseTypeDef(BaseValidatorModel):
    Firewalls: List[FirewallMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListFirewallPoliciesResponseTypeDef(BaseValidatorModel):
    FirewallPolicies: List[FirewallPolicyMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class StatefulEngineOptionsTypeDef(BaseValidatorModel):
    RuleOrder: Optional[RuleOrderType] = None
    StreamExceptionPolicy: Optional[StreamExceptionPolicyType] = None
    FlowTimeouts: Optional[FlowTimeoutsTypeDef] = None


class GetAnalysisReportResultsRequestPaginateTypeDef(BaseValidatorModel):
    AnalysisReportId: str
    FirewallName: Optional[str] = None
    FirewallArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAnalysisReportsRequestPaginateTypeDef(BaseValidatorModel):
    FirewallName: Optional[str] = None
    FirewallArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFirewallPoliciesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFirewallsRequestPaginateTypeDef(BaseValidatorModel):
    VpcIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTLSInspectionConfigurationsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTagsForResourceRequestPaginateTypeDef(BaseValidatorModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class PolicyVariablesOutputTypeDef(BaseValidatorModel):
    RuleVariables: Optional[Dict[str, IPSetOutputTypeDef]] = None


class ReferenceSetsOutputTypeDef(BaseValidatorModel):
    IPSetReferences: Optional[Dict[str, IPSetReferenceTypeDef]] = None


class ReferenceSetsTypeDef(BaseValidatorModel):
    IPSetReferences: Optional[Mapping[str, IPSetReferenceTypeDef]] = None


class PolicyVariablesTypeDef(BaseValidatorModel):
    RuleVariables: Optional[Mapping[str, IPSetTypeDef]] = None


class ListRuleGroupsResponseTypeDef(BaseValidatorModel):
    RuleGroups: List[RuleGroupMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTLSInspectionConfigurationsResponseTypeDef(BaseValidatorModel):
    TLSInspectionConfigurations: List[TLSInspectionConfigurationMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class LoggingConfigurationOutputTypeDef(BaseValidatorModel):
    LogDestinationConfigs: List[LogDestinationConfigOutputTypeDef]


class LoggingConfigurationTypeDef(BaseValidatorModel):
    LogDestinationConfigs: Sequence[LogDestinationConfigTypeDef]


class ServerCertificateScopeOutputTypeDef(BaseValidatorModel):
    Sources: Optional[List[AddressTypeDef]] = None
    Destinations: Optional[List[AddressTypeDef]] = None
    SourcePorts: Optional[List[PortRangeTypeDef]] = None
    DestinationPorts: Optional[List[PortRangeTypeDef]] = None
    Protocols: Optional[List[int]] = None


class ServerCertificateScopeTypeDef(BaseValidatorModel):
    Sources: Optional[Sequence[AddressTypeDef]] = None
    Destinations: Optional[Sequence[AddressTypeDef]] = None
    SourcePorts: Optional[Sequence[PortRangeTypeDef]] = None
    DestinationPorts: Optional[Sequence[PortRangeTypeDef]] = None
    Protocols: Optional[Sequence[int]] = None


class MatchAttributesOutputTypeDef(BaseValidatorModel):
    Sources: Optional[List[AddressTypeDef]] = None
    Destinations: Optional[List[AddressTypeDef]] = None
    SourcePorts: Optional[List[PortRangeTypeDef]] = None
    DestinationPorts: Optional[List[PortRangeTypeDef]] = None
    Protocols: Optional[List[int]] = None
    TCPFlags: Optional[List[TCPFlagFieldOutputTypeDef]] = None


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


class RuleVariablesOutputTypeDef(BaseValidatorModel):
    IPSets: Optional[Dict[str, IPSetOutputTypeDef]] = None
    PortSets: Optional[Dict[str, PortSetOutputTypeDef]] = None


class RuleVariablesTypeDef(BaseValidatorModel):
    IPSets: Optional[Mapping[str, IPSetTypeDef]] = None
    PortSets: Optional[Mapping[str, PortSetTypeDef]] = None


class HeaderTypeDef(BaseValidatorModel):
    pass


class StatefulRuleOutputTypeDef(BaseValidatorModel):
    Action: StatefulActionType
    Header: HeaderTypeDef
    RuleOptions: List[RuleOptionOutputTypeDef]


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


class AnalysisTypeReportResultTypeDef(BaseValidatorModel):
    pass


class GetAnalysisReportResultsResponseTypeDef(BaseValidatorModel):
    Status: str
    StartTime: datetime
    EndTime: datetime
    ReportTime: datetime
    AnalysisType: EnabledAnalysisTypeType
    AnalysisReportResults: List[AnalysisTypeReportResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


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


class RuleGroupResponseTypeDef(BaseValidatorModel):
    pass


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


class ActionDefinitionOutputTypeDef(BaseValidatorModel):
    PublishMetricAction: Optional[PublishMetricActionOutputTypeDef] = None


class ActionDefinitionTypeDef(BaseValidatorModel):
    PublishMetricAction: Optional[PublishMetricActionTypeDef] = None


class DescribeLoggingConfigurationResponseTypeDef(BaseValidatorModel):
    FirewallArn: str
    LoggingConfiguration: LoggingConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateLoggingConfigurationResponseTypeDef(BaseValidatorModel):
    FirewallArn: str
    FirewallName: str
    LoggingConfiguration: LoggingConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ServerCertificateConfigurationOutputTypeDef(BaseValidatorModel):
    ServerCertificates: Optional[List[ServerCertificateTypeDef]] = None
    Scopes: Optional[List[ServerCertificateScopeOutputTypeDef]] = None
    CertificateAuthorityArn: Optional[str] = None
    CheckCertificateRevocationStatus: Optional[CheckCertificateRevocationStatusActionsTypeDef] = None


class ServerCertificateConfigurationTypeDef(BaseValidatorModel):
    ServerCertificates: Optional[Sequence[ServerCertificateTypeDef]] = None
    Scopes: Optional[Sequence[ServerCertificateScopeTypeDef]] = None
    CertificateAuthorityArn: Optional[str] = None
    CheckCertificateRevocationStatus: Optional[CheckCertificateRevocationStatusActionsTypeDef] = None


class RuleDefinitionOutputTypeDef(BaseValidatorModel):
    MatchAttributes: MatchAttributesOutputTypeDef
    Actions: List[str]


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


class CustomActionOutputTypeDef(BaseValidatorModel):
    ActionName: str
    ActionDefinition: ActionDefinitionOutputTypeDef


class CustomActionTypeDef(BaseValidatorModel):
    ActionName: str
    ActionDefinition: ActionDefinitionTypeDef


class LoggingConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class UpdateLoggingConfigurationRequestTypeDef(BaseValidatorModel):
    FirewallArn: Optional[str] = None
    FirewallName: Optional[str] = None
    LoggingConfiguration: Optional[LoggingConfigurationUnionTypeDef] = None


class TLSInspectionConfigurationOutputTypeDef(BaseValidatorModel):
    ServerCertificateConfigurations: Optional[List[ServerCertificateConfigurationOutputTypeDef]] = None


class TLSInspectionConfigurationTypeDef(BaseValidatorModel):
    ServerCertificateConfigurations: Optional[Sequence[ServerCertificateConfigurationTypeDef]] = None


class StatelessRuleOutputTypeDef(BaseValidatorModel):
    RuleDefinition: RuleDefinitionOutputTypeDef
    Priority: int


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


class FirewallPolicyOutputTypeDef(BaseValidatorModel):
    StatelessDefaultActions: List[str]
    StatelessFragmentDefaultActions: List[str]
    StatelessRuleGroupReferences: Optional[List[StatelessRuleGroupReferenceTypeDef]] = None
    StatelessCustomActions: Optional[List[CustomActionOutputTypeDef]] = None
    StatefulRuleGroupReferences: Optional[List[StatefulRuleGroupReferenceTypeDef]] = None
    StatefulDefaultActions: Optional[List[str]] = None
    StatefulEngineOptions: Optional[StatefulEngineOptionsTypeDef] = None
    TLSInspectionConfigurationArn: Optional[str] = None
    PolicyVariables: Optional[PolicyVariablesOutputTypeDef] = None


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


class DescribeTLSInspectionConfigurationResponseTypeDef(BaseValidatorModel):
    UpdateToken: str
    TLSInspectionConfiguration: TLSInspectionConfigurationOutputTypeDef
    TLSInspectionConfigurationResponse: TLSInspectionConfigurationResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StatelessRulesAndCustomActionsOutputTypeDef(BaseValidatorModel):
    StatelessRules: List[StatelessRuleOutputTypeDef]
    CustomActions: Optional[List[CustomActionOutputTypeDef]] = None


class StatelessRulesAndCustomActionsTypeDef(BaseValidatorModel):
    StatelessRules: Sequence[StatelessRuleTypeDef]
    CustomActions: Optional[Sequence[CustomActionTypeDef]] = None


class DescribeFirewallPolicyResponseTypeDef(BaseValidatorModel):
    UpdateToken: str
    FirewallPolicyResponse: FirewallPolicyResponseTypeDef
    FirewallPolicy: FirewallPolicyOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class TLSInspectionConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateTLSInspectionConfigurationRequestTypeDef(BaseValidatorModel):
    TLSInspectionConfigurationName: str
    TLSInspectionConfiguration: TLSInspectionConfigurationUnionTypeDef
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None


class UpdateTLSInspectionConfigurationRequestTypeDef(BaseValidatorModel):
    TLSInspectionConfiguration: TLSInspectionConfigurationUnionTypeDef
    UpdateToken: str
    TLSInspectionConfigurationArn: Optional[str] = None
    TLSInspectionConfigurationName: Optional[str] = None
    Description: Optional[str] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None


class RulesSourceOutputTypeDef(BaseValidatorModel):
    RulesString: Optional[str] = None
    RulesSourceList: Optional[RulesSourceListOutputTypeDef] = None
    StatefulRules: Optional[List[StatefulRuleOutputTypeDef]] = None
    StatelessRulesAndCustomActions: Optional[StatelessRulesAndCustomActionsOutputTypeDef] = None


class RulesSourceTypeDef(BaseValidatorModel):
    RulesString: Optional[str] = None
    RulesSourceList: Optional[RulesSourceListTypeDef] = None
    StatefulRules: Optional[Sequence[StatefulRuleTypeDef]] = None
    StatelessRulesAndCustomActions: Optional[StatelessRulesAndCustomActionsTypeDef] = None


class FirewallPolicyUnionTypeDef(BaseValidatorModel):
    pass


class CreateFirewallPolicyRequestTypeDef(BaseValidatorModel):
    FirewallPolicyName: str
    FirewallPolicy: FirewallPolicyUnionTypeDef
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    DryRun: Optional[bool] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None


class UpdateFirewallPolicyRequestTypeDef(BaseValidatorModel):
    UpdateToken: str
    FirewallPolicy: FirewallPolicyUnionTypeDef
    FirewallPolicyArn: Optional[str] = None
    FirewallPolicyName: Optional[str] = None
    Description: Optional[str] = None
    DryRun: Optional[bool] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None


class RuleGroupOutputTypeDef(BaseValidatorModel):
    RulesSource: RulesSourceOutputTypeDef
    RuleVariables: Optional[RuleVariablesOutputTypeDef] = None
    ReferenceSets: Optional[ReferenceSetsOutputTypeDef] = None
    StatefulRuleOptions: Optional[StatefulRuleOptionsTypeDef] = None


class RuleGroupTypeDef(BaseValidatorModel):
    RulesSource: RulesSourceTypeDef
    RuleVariables: Optional[RuleVariablesTypeDef] = None
    ReferenceSets: Optional[ReferenceSetsTypeDef] = None
    StatefulRuleOptions: Optional[StatefulRuleOptionsTypeDef] = None


class DescribeRuleGroupResponseTypeDef(BaseValidatorModel):
    UpdateToken: str
    RuleGroup: RuleGroupOutputTypeDef
    RuleGroupResponse: RuleGroupResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef



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
from aws_resource_validator.pydantic_models.apprunner_constants import *

class AssociateCustomDomainRequestRequestTypeDef(BaseValidatorModel):
    ServiceArn: str
    DomainName: str
    EnableWWWSubdomain: Optional[bool] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class VpcDNSTargetTypeDef(BaseValidatorModel):
    VpcIngressConnectionArn: Optional[str] = None
    VpcId: Optional[str] = None
    DomainName: Optional[str] = None

class AuthenticationConfigurationTypeDef(BaseValidatorModel):
    ConnectionArn: Optional[str] = None
    AccessRoleArn: Optional[str] = None

class AutoScalingConfigurationSummaryTypeDef(BaseValidatorModel):
    AutoScalingConfigurationArn: Optional[str] = None
    AutoScalingConfigurationName: Optional[str] = None
    AutoScalingConfigurationRevision: Optional[int] = None
    Status: Optional[AutoScalingConfigurationStatusType] = None
    CreatedAt: Optional[datetime] = None
    HasAssociatedService: Optional[bool] = None
    IsDefault: Optional[bool] = None

class AutoScalingConfigurationTypeDef(BaseValidatorModel):
    AutoScalingConfigurationArn: Optional[str] = None
    AutoScalingConfigurationName: Optional[str] = None
    AutoScalingConfigurationRevision: Optional[int] = None
    Latest: Optional[bool] = None
    Status: Optional[AutoScalingConfigurationStatusType] = None
    MaxConcurrency: Optional[int] = None
    MinSize: Optional[int] = None
    MaxSize: Optional[int] = None
    CreatedAt: Optional[datetime] = None
    DeletedAt: Optional[datetime] = None
    HasAssociatedService: Optional[bool] = None
    IsDefault: Optional[bool] = None

class CertificateValidationRecordTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Type: Optional[str] = None
    Value: Optional[str] = None
    Status: Optional[CertificateValidationRecordStatusType] = None

class CodeConfigurationValuesTypeDef(BaseValidatorModel):
    Runtime: RuntimeType
    BuildCommand: Optional[str] = None
    StartCommand: Optional[str] = None
    Port: Optional[str] = None
    RuntimeEnvironmentVariables: Optional[Mapping[str, str]] = None
    RuntimeEnvironmentSecrets: Optional[Mapping[str, str]] = None

class SourceCodeVersionTypeDef(BaseValidatorModel):
    Type: Literal["BRANCH"]
    Value: str

class ConnectionSummaryTypeDef(BaseValidatorModel):
    ConnectionName: Optional[str] = None
    ConnectionArn: Optional[str] = None
    ProviderType: Optional[ProviderTypeType] = None
    Status: Optional[ConnectionStatusType] = None
    CreatedAt: Optional[datetime] = None

class ConnectionTypeDef(BaseValidatorModel):
    ConnectionName: Optional[str] = None
    ConnectionArn: Optional[str] = None
    ProviderType: Optional[ProviderTypeType] = None
    Status: Optional[ConnectionStatusType] = None
    CreatedAt: Optional[datetime] = None

class TagTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class TraceConfigurationTypeDef(BaseValidatorModel):
    Vendor: Literal["AWSXRAY"]

class EncryptionConfigurationTypeDef(BaseValidatorModel):
    KmsKey: str

class HealthCheckConfigurationTypeDef(BaseValidatorModel):
    Protocol: Optional[HealthCheckProtocolType] = None
    Path: Optional[str] = None
    Interval: Optional[int] = None
    Timeout: Optional[int] = None
    HealthyThreshold: Optional[int] = None
    UnhealthyThreshold: Optional[int] = None

class InstanceConfigurationTypeDef(BaseValidatorModel):
    Cpu: Optional[str] = None
    Memory: Optional[str] = None
    InstanceRoleArn: Optional[str] = None

class ServiceObservabilityConfigurationTypeDef(BaseValidatorModel):
    ObservabilityEnabled: bool
    ObservabilityConfigurationArn: Optional[str] = None

class VpcConnectorTypeDef(BaseValidatorModel):
    VpcConnectorName: Optional[str] = None
    VpcConnectorArn: Optional[str] = None
    VpcConnectorRevision: Optional[int] = None
    Subnets: Optional[List[str]] = None
    SecurityGroups: Optional[List[str]] = None
    Status: Optional[VpcConnectorStatusType] = None
    CreatedAt: Optional[datetime] = None
    DeletedAt: Optional[datetime] = None

class IngressVpcConfigurationTypeDef(BaseValidatorModel):
    VpcId: Optional[str] = None
    VpcEndpointId: Optional[str] = None

class DeleteAutoScalingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    AutoScalingConfigurationArn: str
    DeleteAllRevisions: Optional[bool] = None

class DeleteConnectionRequestRequestTypeDef(BaseValidatorModel):
    ConnectionArn: str

class DeleteObservabilityConfigurationRequestRequestTypeDef(BaseValidatorModel):
    ObservabilityConfigurationArn: str

class DeleteServiceRequestRequestTypeDef(BaseValidatorModel):
    ServiceArn: str

class DeleteVpcConnectorRequestRequestTypeDef(BaseValidatorModel):
    VpcConnectorArn: str

class DeleteVpcIngressConnectionRequestRequestTypeDef(BaseValidatorModel):
    VpcIngressConnectionArn: str

class DescribeAutoScalingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    AutoScalingConfigurationArn: str

class DescribeCustomDomainsRequestRequestTypeDef(BaseValidatorModel):
    ServiceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeObservabilityConfigurationRequestRequestTypeDef(BaseValidatorModel):
    ObservabilityConfigurationArn: str

class DescribeServiceRequestRequestTypeDef(BaseValidatorModel):
    ServiceArn: str

class DescribeVpcConnectorRequestRequestTypeDef(BaseValidatorModel):
    VpcConnectorArn: str

class DescribeVpcIngressConnectionRequestRequestTypeDef(BaseValidatorModel):
    VpcIngressConnectionArn: str

class DisassociateCustomDomainRequestRequestTypeDef(BaseValidatorModel):
    ServiceArn: str
    DomainName: str

class EgressConfigurationTypeDef(BaseValidatorModel):
    EgressType: Optional[EgressTypeType] = None
    VpcConnectorArn: Optional[str] = None

class ImageConfigurationTypeDef(BaseValidatorModel):
    RuntimeEnvironmentVariables: Optional[Mapping[str, str]] = None
    StartCommand: Optional[str] = None
    Port: Optional[str] = None
    RuntimeEnvironmentSecrets: Optional[Mapping[str, str]] = None

class IngressConfigurationTypeDef(BaseValidatorModel):
    IsPubliclyAccessible: Optional[bool] = None

class ListAutoScalingConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    AutoScalingConfigurationName: Optional[str] = None
    LatestOnly: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListConnectionsRequestRequestTypeDef(BaseValidatorModel):
    ConnectionName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListObservabilityConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    ObservabilityConfigurationName: Optional[str] = None
    LatestOnly: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ObservabilityConfigurationSummaryTypeDef(BaseValidatorModel):
    ObservabilityConfigurationArn: Optional[str] = None
    ObservabilityConfigurationName: Optional[str] = None
    ObservabilityConfigurationRevision: Optional[int] = None

class ListOperationsRequestRequestTypeDef(BaseValidatorModel):
    ServiceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class OperationSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Type: Optional[OperationTypeType] = None
    Status: Optional[OperationStatusType] = None
    TargetArn: Optional[str] = None
    StartedAt: Optional[datetime] = None
    EndedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None

class ListServicesForAutoScalingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    AutoScalingConfigurationArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListServicesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ServiceSummaryTypeDef(BaseValidatorModel):
    ServiceName: Optional[str] = None
    ServiceId: Optional[str] = None
    ServiceArn: Optional[str] = None
    ServiceUrl: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None
    Status: Optional[ServiceStatusType] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class ListVpcConnectorsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListVpcIngressConnectionsFilterTypeDef(BaseValidatorModel):
    ServiceArn: Optional[str] = None
    VpcEndpointId: Optional[str] = None

class VpcIngressConnectionSummaryTypeDef(BaseValidatorModel):
    VpcIngressConnectionArn: Optional[str] = None
    ServiceArn: Optional[str] = None

class PauseServiceRequestRequestTypeDef(BaseValidatorModel):
    ServiceArn: str

class ResumeServiceRequestRequestTypeDef(BaseValidatorModel):
    ServiceArn: str

class StartDeploymentRequestRequestTypeDef(BaseValidatorModel):
    ServiceArn: str

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateDefaultAutoScalingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    AutoScalingConfigurationArn: str

class ListServicesForAutoScalingConfigurationResponseTypeDef(BaseValidatorModel):
    ServiceArnList: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartDeploymentResponseTypeDef(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAutoScalingConfigurationsResponseTypeDef(BaseValidatorModel):
    AutoScalingConfigurationSummaryList: List[AutoScalingConfigurationSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAutoScalingConfigurationResponseTypeDef(BaseValidatorModel):
    AutoScalingConfiguration: AutoScalingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAutoScalingConfigurationResponseTypeDef(BaseValidatorModel):
    AutoScalingConfiguration: AutoScalingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAutoScalingConfigurationResponseTypeDef(BaseValidatorModel):
    AutoScalingConfiguration: AutoScalingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDefaultAutoScalingConfigurationResponseTypeDef(BaseValidatorModel):
    AutoScalingConfiguration: AutoScalingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CustomDomainTypeDef(BaseValidatorModel):
    DomainName: str
    EnableWWWSubdomain: bool
    Status: CustomDomainAssociationStatusType
    CertificateValidationRecords: Optional[List[CertificateValidationRecordTypeDef]] = None

class CodeConfigurationTypeDef(BaseValidatorModel):
    ConfigurationSource: ConfigurationSourceType
    CodeConfigurationValues: Optional[CodeConfigurationValuesTypeDef] = None

class ListConnectionsResponseTypeDef(BaseValidatorModel):
    ConnectionSummaryList: List[ConnectionSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConnectionResponseTypeDef(BaseValidatorModel):
    Connection: ConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteConnectionResponseTypeDef(BaseValidatorModel):
    Connection: ConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAutoScalingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    AutoScalingConfigurationName: str
    MaxConcurrency: Optional[int] = None
    MinSize: Optional[int] = None
    MaxSize: Optional[int] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateConnectionRequestRequestTypeDef(BaseValidatorModel):
    ConnectionName: str
    ProviderType: ProviderTypeType
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateVpcConnectorRequestRequestTypeDef(BaseValidatorModel):
    VpcConnectorName: str
    Subnets: Sequence[str]
    SecurityGroups: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CreateObservabilityConfigurationRequestRequestTypeDef(BaseValidatorModel):
    ObservabilityConfigurationName: str
    TraceConfiguration: Optional[TraceConfigurationTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ObservabilityConfigurationTypeDef(BaseValidatorModel):
    ObservabilityConfigurationArn: Optional[str] = None
    ObservabilityConfigurationName: Optional[str] = None
    TraceConfiguration: Optional[TraceConfigurationTypeDef] = None
    ObservabilityConfigurationRevision: Optional[int] = None
    Latest: Optional[bool] = None
    Status: Optional[ObservabilityConfigurationStatusType] = None
    CreatedAt: Optional[datetime] = None
    DeletedAt: Optional[datetime] = None

class CreateVpcConnectorResponseTypeDef(BaseValidatorModel):
    VpcConnector: VpcConnectorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVpcConnectorResponseTypeDef(BaseValidatorModel):
    VpcConnector: VpcConnectorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVpcConnectorResponseTypeDef(BaseValidatorModel):
    VpcConnector: VpcConnectorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListVpcConnectorsResponseTypeDef(BaseValidatorModel):
    VpcConnectors: List[VpcConnectorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVpcIngressConnectionRequestRequestTypeDef(BaseValidatorModel):
    ServiceArn: str
    VpcIngressConnectionName: str
    IngressVpcConfiguration: IngressVpcConfigurationTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateVpcIngressConnectionRequestRequestTypeDef(BaseValidatorModel):
    VpcIngressConnectionArn: str
    IngressVpcConfiguration: IngressVpcConfigurationTypeDef

class VpcIngressConnectionTypeDef(BaseValidatorModel):
    VpcIngressConnectionArn: Optional[str] = None
    VpcIngressConnectionName: Optional[str] = None
    ServiceArn: Optional[str] = None
    Status: Optional[VpcIngressConnectionStatusType] = None
    AccountId: Optional[str] = None
    DomainName: Optional[str] = None
    IngressVpcConfiguration: Optional[IngressVpcConfigurationTypeDef] = None
    CreatedAt: Optional[datetime] = None
    DeletedAt: Optional[datetime] = None

class ImageRepositoryTypeDef(BaseValidatorModel):
    ImageIdentifier: str
    ImageRepositoryType: ImageRepositoryTypeType
    ImageConfiguration: Optional[ImageConfigurationTypeDef] = None

class NetworkConfigurationTypeDef(BaseValidatorModel):
    EgressConfiguration: Optional[EgressConfigurationTypeDef] = None
    IngressConfiguration: Optional[IngressConfigurationTypeDef] = None
    IpAddressType: Optional[IpAddressTypeType] = None

class ListObservabilityConfigurationsResponseTypeDef(BaseValidatorModel):
    ObservabilityConfigurationSummaryList: List[ObservabilityConfigurationSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListOperationsResponseTypeDef(BaseValidatorModel):
    OperationSummaryList: List[OperationSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListServicesResponseTypeDef(BaseValidatorModel):
    ServiceSummaryList: List[ServiceSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListVpcIngressConnectionsRequestRequestTypeDef(BaseValidatorModel):
    Filter: Optional[ListVpcIngressConnectionsFilterTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListVpcIngressConnectionsResponseTypeDef(BaseValidatorModel):
    VpcIngressConnectionSummaryList: List[VpcIngressConnectionSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateCustomDomainResponseTypeDef(BaseValidatorModel):
    DNSTarget: str
    ServiceArn: str
    CustomDomain: CustomDomainTypeDef
    VpcDNSTargets: List[VpcDNSTargetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCustomDomainsResponseTypeDef(BaseValidatorModel):
    DNSTarget: str
    ServiceArn: str
    CustomDomains: List[CustomDomainTypeDef]
    VpcDNSTargets: List[VpcDNSTargetTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateCustomDomainResponseTypeDef(BaseValidatorModel):
    DNSTarget: str
    ServiceArn: str
    CustomDomain: CustomDomainTypeDef
    VpcDNSTargets: List[VpcDNSTargetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CodeRepositoryTypeDef(BaseValidatorModel):
    RepositoryUrl: str
    SourceCodeVersion: SourceCodeVersionTypeDef
    CodeConfiguration: Optional[CodeConfigurationTypeDef] = None
    SourceDirectory: Optional[str] = None

class CreateObservabilityConfigurationResponseTypeDef(BaseValidatorModel):
    ObservabilityConfiguration: ObservabilityConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteObservabilityConfigurationResponseTypeDef(BaseValidatorModel):
    ObservabilityConfiguration: ObservabilityConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeObservabilityConfigurationResponseTypeDef(BaseValidatorModel):
    ObservabilityConfiguration: ObservabilityConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVpcIngressConnectionResponseTypeDef(BaseValidatorModel):
    VpcIngressConnection: VpcIngressConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVpcIngressConnectionResponseTypeDef(BaseValidatorModel):
    VpcIngressConnection: VpcIngressConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVpcIngressConnectionResponseTypeDef(BaseValidatorModel):
    VpcIngressConnection: VpcIngressConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVpcIngressConnectionResponseTypeDef(BaseValidatorModel):
    VpcIngressConnection: VpcIngressConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SourceConfigurationTypeDef(BaseValidatorModel):
    CodeRepository: Optional[CodeRepositoryTypeDef] = None
    ImageRepository: Optional[ImageRepositoryTypeDef] = None
    AutoDeploymentsEnabled: Optional[bool] = None
    AuthenticationConfiguration: Optional[AuthenticationConfigurationTypeDef] = None

class CreateServiceRequestRequestTypeDef(BaseValidatorModel):
    ServiceName: str
    SourceConfiguration: SourceConfigurationTypeDef
    InstanceConfiguration: Optional[InstanceConfigurationTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None
    HealthCheckConfiguration: Optional[HealthCheckConfigurationTypeDef] = None
    AutoScalingConfigurationArn: Optional[str] = None
    NetworkConfiguration: Optional[NetworkConfigurationTypeDef] = None
    ObservabilityConfiguration: Optional[ServiceObservabilityConfigurationTypeDef] = None

class ServiceTypeDef(BaseValidatorModel):
    ServiceName: str
    ServiceId: str
    ServiceArn: str
    CreatedAt: datetime
    UpdatedAt: datetime
    Status: ServiceStatusType
    SourceConfiguration: SourceConfigurationTypeDef
    InstanceConfiguration: InstanceConfigurationTypeDef
    AutoScalingConfigurationSummary: AutoScalingConfigurationSummaryTypeDef
    NetworkConfiguration: NetworkConfigurationTypeDef
    ServiceUrl: Optional[str] = None
    DeletedAt: Optional[datetime] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None
    HealthCheckConfiguration: Optional[HealthCheckConfigurationTypeDef] = None
    ObservabilityConfiguration: Optional[ServiceObservabilityConfigurationTypeDef] = None

class UpdateServiceRequestRequestTypeDef(BaseValidatorModel):
    ServiceArn: str
    SourceConfiguration: Optional[SourceConfigurationTypeDef] = None
    InstanceConfiguration: Optional[InstanceConfigurationTypeDef] = None
    AutoScalingConfigurationArn: Optional[str] = None
    HealthCheckConfiguration: Optional[HealthCheckConfigurationTypeDef] = None
    NetworkConfiguration: Optional[NetworkConfigurationTypeDef] = None
    ObservabilityConfiguration: Optional[ServiceObservabilityConfigurationTypeDef] = None

class CreateServiceResponseTypeDef(BaseValidatorModel):
    Service: ServiceTypeDef
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteServiceResponseTypeDef(BaseValidatorModel):
    Service: ServiceTypeDef
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeServiceResponseTypeDef(BaseValidatorModel):
    Service: ServiceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PauseServiceResponseTypeDef(BaseValidatorModel):
    Service: ServiceTypeDef
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResumeServiceResponseTypeDef(BaseValidatorModel):
    Service: ServiceTypeDef
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceResponseTypeDef(BaseValidatorModel):
    Service: ServiceTypeDef
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef


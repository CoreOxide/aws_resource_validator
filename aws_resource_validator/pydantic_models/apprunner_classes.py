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
from aws_resource_validator.pydantic_models.apprunner_constants import *

class AssociateCustomDomainRequestRequestTypeDef(BaseModel):
    ServiceArn: str
    DomainName: str
    EnableWWWSubdomain: Optional[bool] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class VpcDNSTargetTypeDef(BaseModel):
    VpcIngressConnectionArn: Optional[str] = None
    VpcId: Optional[str] = None
    DomainName: Optional[str] = None

class AuthenticationConfigurationTypeDef(BaseModel):
    ConnectionArn: Optional[str] = None
    AccessRoleArn: Optional[str] = None

class AutoScalingConfigurationSummaryTypeDef(BaseModel):
    AutoScalingConfigurationArn: Optional[str] = None
    AutoScalingConfigurationName: Optional[str] = None
    AutoScalingConfigurationRevision: Optional[int] = None
    Status: Optional[AutoScalingConfigurationStatusType] = None
    CreatedAt: Optional[datetime] = None
    HasAssociatedService: Optional[bool] = None
    IsDefault: Optional[bool] = None

class AutoScalingConfigurationTypeDef(BaseModel):
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

class CertificateValidationRecordTypeDef(BaseModel):
    Name: Optional[str] = None
    Type: Optional[str] = None
    Value: Optional[str] = None
    Status: Optional[CertificateValidationRecordStatusType] = None

class CodeConfigurationValuesTypeDef(BaseModel):
    Runtime: RuntimeType
    BuildCommand: Optional[str] = None
    StartCommand: Optional[str] = None
    Port: Optional[str] = None
    RuntimeEnvironmentVariables: Optional[Mapping[str, str]] = None
    RuntimeEnvironmentSecrets: Optional[Mapping[str, str]] = None

class SourceCodeVersionTypeDef(BaseModel):
    Type: Literal["BRANCH"]
    Value: str

class ConnectionSummaryTypeDef(BaseModel):
    ConnectionName: Optional[str] = None
    ConnectionArn: Optional[str] = None
    ProviderType: Optional[ProviderTypeType] = None
    Status: Optional[ConnectionStatusType] = None
    CreatedAt: Optional[datetime] = None

class ConnectionTypeDef(BaseModel):
    ConnectionName: Optional[str] = None
    ConnectionArn: Optional[str] = None
    ProviderType: Optional[ProviderTypeType] = None
    Status: Optional[ConnectionStatusType] = None
    CreatedAt: Optional[datetime] = None

class TagTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class TraceConfigurationTypeDef(BaseModel):
    Vendor: Literal["AWSXRAY"]

class EncryptionConfigurationTypeDef(BaseModel):
    KmsKey: str

class HealthCheckConfigurationTypeDef(BaseModel):
    Protocol: Optional[HealthCheckProtocolType] = None
    Path: Optional[str] = None
    Interval: Optional[int] = None
    Timeout: Optional[int] = None
    HealthyThreshold: Optional[int] = None
    UnhealthyThreshold: Optional[int] = None

class InstanceConfigurationTypeDef(BaseModel):
    Cpu: Optional[str] = None
    Memory: Optional[str] = None
    InstanceRoleArn: Optional[str] = None

class ServiceObservabilityConfigurationTypeDef(BaseModel):
    ObservabilityEnabled: bool
    ObservabilityConfigurationArn: Optional[str] = None

class VpcConnectorTypeDef(BaseModel):
    VpcConnectorName: Optional[str] = None
    VpcConnectorArn: Optional[str] = None
    VpcConnectorRevision: Optional[int] = None
    Subnets: Optional[List[str]] = None
    SecurityGroups: Optional[List[str]] = None
    Status: Optional[VpcConnectorStatusType] = None
    CreatedAt: Optional[datetime] = None
    DeletedAt: Optional[datetime] = None

class IngressVpcConfigurationTypeDef(BaseModel):
    VpcId: Optional[str] = None
    VpcEndpointId: Optional[str] = None

class DeleteAutoScalingConfigurationRequestRequestTypeDef(BaseModel):
    AutoScalingConfigurationArn: str
    DeleteAllRevisions: Optional[bool] = None

class DeleteConnectionRequestRequestTypeDef(BaseModel):
    ConnectionArn: str

class DeleteObservabilityConfigurationRequestRequestTypeDef(BaseModel):
    ObservabilityConfigurationArn: str

class DeleteServiceRequestRequestTypeDef(BaseModel):
    ServiceArn: str

class DeleteVpcConnectorRequestRequestTypeDef(BaseModel):
    VpcConnectorArn: str

class DeleteVpcIngressConnectionRequestRequestTypeDef(BaseModel):
    VpcIngressConnectionArn: str

class DescribeAutoScalingConfigurationRequestRequestTypeDef(BaseModel):
    AutoScalingConfigurationArn: str

class DescribeCustomDomainsRequestRequestTypeDef(BaseModel):
    ServiceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeObservabilityConfigurationRequestRequestTypeDef(BaseModel):
    ObservabilityConfigurationArn: str

class DescribeServiceRequestRequestTypeDef(BaseModel):
    ServiceArn: str

class DescribeVpcConnectorRequestRequestTypeDef(BaseModel):
    VpcConnectorArn: str

class DescribeVpcIngressConnectionRequestRequestTypeDef(BaseModel):
    VpcIngressConnectionArn: str

class DisassociateCustomDomainRequestRequestTypeDef(BaseModel):
    ServiceArn: str
    DomainName: str

class EgressConfigurationTypeDef(BaseModel):
    EgressType: Optional[EgressTypeType] = None
    VpcConnectorArn: Optional[str] = None

class ImageConfigurationTypeDef(BaseModel):
    RuntimeEnvironmentVariables: Optional[Mapping[str, str]] = None
    StartCommand: Optional[str] = None
    Port: Optional[str] = None
    RuntimeEnvironmentSecrets: Optional[Mapping[str, str]] = None

class IngressConfigurationTypeDef(BaseModel):
    IsPubliclyAccessible: Optional[bool] = None

class ListAutoScalingConfigurationsRequestRequestTypeDef(BaseModel):
    AutoScalingConfigurationName: Optional[str] = None
    LatestOnly: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListConnectionsRequestRequestTypeDef(BaseModel):
    ConnectionName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListObservabilityConfigurationsRequestRequestTypeDef(BaseModel):
    ObservabilityConfigurationName: Optional[str] = None
    LatestOnly: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ObservabilityConfigurationSummaryTypeDef(BaseModel):
    ObservabilityConfigurationArn: Optional[str] = None
    ObservabilityConfigurationName: Optional[str] = None
    ObservabilityConfigurationRevision: Optional[int] = None

class ListOperationsRequestRequestTypeDef(BaseModel):
    ServiceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class OperationSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Type: Optional[OperationTypeType] = None
    Status: Optional[OperationStatusType] = None
    TargetArn: Optional[str] = None
    StartedAt: Optional[datetime] = None
    EndedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None

class ListServicesForAutoScalingConfigurationRequestRequestTypeDef(BaseModel):
    AutoScalingConfigurationArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListServicesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ServiceSummaryTypeDef(BaseModel):
    ServiceName: Optional[str] = None
    ServiceId: Optional[str] = None
    ServiceArn: Optional[str] = None
    ServiceUrl: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None
    Status: Optional[ServiceStatusType] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class ListVpcConnectorsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListVpcIngressConnectionsFilterTypeDef(BaseModel):
    ServiceArn: Optional[str] = None
    VpcEndpointId: Optional[str] = None

class VpcIngressConnectionSummaryTypeDef(BaseModel):
    VpcIngressConnectionArn: Optional[str] = None
    ServiceArn: Optional[str] = None

class PauseServiceRequestRequestTypeDef(BaseModel):
    ServiceArn: str

class ResumeServiceRequestRequestTypeDef(BaseModel):
    ServiceArn: str

class StartDeploymentRequestRequestTypeDef(BaseModel):
    ServiceArn: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateDefaultAutoScalingConfigurationRequestRequestTypeDef(BaseModel):
    AutoScalingConfigurationArn: str

class ListServicesForAutoScalingConfigurationResponseTypeDef(BaseModel):
    ServiceArnList: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartDeploymentResponseTypeDef(BaseModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAutoScalingConfigurationsResponseTypeDef(BaseModel):
    AutoScalingConfigurationSummaryList: List[AutoScalingConfigurationSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAutoScalingConfigurationResponseTypeDef(BaseModel):
    AutoScalingConfiguration: AutoScalingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAutoScalingConfigurationResponseTypeDef(BaseModel):
    AutoScalingConfiguration: AutoScalingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAutoScalingConfigurationResponseTypeDef(BaseModel):
    AutoScalingConfiguration: AutoScalingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDefaultAutoScalingConfigurationResponseTypeDef(BaseModel):
    AutoScalingConfiguration: AutoScalingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CustomDomainTypeDef(BaseModel):
    DomainName: str
    EnableWWWSubdomain: bool
    Status: CustomDomainAssociationStatusType
    CertificateValidationRecords: Optional[List[CertificateValidationRecordTypeDef]] = None

class CodeConfigurationTypeDef(BaseModel):
    ConfigurationSource: ConfigurationSourceType
    CodeConfigurationValues: Optional[CodeConfigurationValuesTypeDef] = None

class ListConnectionsResponseTypeDef(BaseModel):
    ConnectionSummaryList: List[ConnectionSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConnectionResponseTypeDef(BaseModel):
    Connection: ConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteConnectionResponseTypeDef(BaseModel):
    Connection: ConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAutoScalingConfigurationRequestRequestTypeDef(BaseModel):
    AutoScalingConfigurationName: str
    MaxConcurrency: Optional[int] = None
    MinSize: Optional[int] = None
    MaxSize: Optional[int] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateConnectionRequestRequestTypeDef(BaseModel):
    ConnectionName: str
    ProviderType: ProviderTypeType
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateVpcConnectorRequestRequestTypeDef(BaseModel):
    VpcConnectorName: str
    Subnets: Sequence[str]
    SecurityGroups: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CreateObservabilityConfigurationRequestRequestTypeDef(BaseModel):
    ObservabilityConfigurationName: str
    TraceConfiguration: Optional[TraceConfigurationTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ObservabilityConfigurationTypeDef(BaseModel):
    ObservabilityConfigurationArn: Optional[str] = None
    ObservabilityConfigurationName: Optional[str] = None
    TraceConfiguration: Optional[TraceConfigurationTypeDef] = None
    ObservabilityConfigurationRevision: Optional[int] = None
    Latest: Optional[bool] = None
    Status: Optional[ObservabilityConfigurationStatusType] = None
    CreatedAt: Optional[datetime] = None
    DeletedAt: Optional[datetime] = None

class CreateVpcConnectorResponseTypeDef(BaseModel):
    VpcConnector: VpcConnectorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVpcConnectorResponseTypeDef(BaseModel):
    VpcConnector: VpcConnectorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVpcConnectorResponseTypeDef(BaseModel):
    VpcConnector: VpcConnectorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListVpcConnectorsResponseTypeDef(BaseModel):
    VpcConnectors: List[VpcConnectorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVpcIngressConnectionRequestRequestTypeDef(BaseModel):
    ServiceArn: str
    VpcIngressConnectionName: str
    IngressVpcConfiguration: IngressVpcConfigurationTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateVpcIngressConnectionRequestRequestTypeDef(BaseModel):
    VpcIngressConnectionArn: str
    IngressVpcConfiguration: IngressVpcConfigurationTypeDef

class VpcIngressConnectionTypeDef(BaseModel):
    VpcIngressConnectionArn: Optional[str] = None
    VpcIngressConnectionName: Optional[str] = None
    ServiceArn: Optional[str] = None
    Status: Optional[VpcIngressConnectionStatusType] = None
    AccountId: Optional[str] = None
    DomainName: Optional[str] = None
    IngressVpcConfiguration: Optional[IngressVpcConfigurationTypeDef] = None
    CreatedAt: Optional[datetime] = None
    DeletedAt: Optional[datetime] = None

class ImageRepositoryTypeDef(BaseModel):
    ImageIdentifier: str
    ImageRepositoryType: ImageRepositoryTypeType
    ImageConfiguration: Optional[ImageConfigurationTypeDef] = None

class NetworkConfigurationTypeDef(BaseModel):
    EgressConfiguration: Optional[EgressConfigurationTypeDef] = None
    IngressConfiguration: Optional[IngressConfigurationTypeDef] = None
    IpAddressType: Optional[IpAddressTypeType] = None

class ListObservabilityConfigurationsResponseTypeDef(BaseModel):
    ObservabilityConfigurationSummaryList: List[ObservabilityConfigurationSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListOperationsResponseTypeDef(BaseModel):
    OperationSummaryList: List[OperationSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListServicesResponseTypeDef(BaseModel):
    ServiceSummaryList: List[ServiceSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListVpcIngressConnectionsRequestRequestTypeDef(BaseModel):
    Filter: Optional[ListVpcIngressConnectionsFilterTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListVpcIngressConnectionsResponseTypeDef(BaseModel):
    VpcIngressConnectionSummaryList: List[VpcIngressConnectionSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateCustomDomainResponseTypeDef(BaseModel):
    DNSTarget: str
    ServiceArn: str
    CustomDomain: CustomDomainTypeDef
    VpcDNSTargets: List[VpcDNSTargetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCustomDomainsResponseTypeDef(BaseModel):
    DNSTarget: str
    ServiceArn: str
    CustomDomains: List[CustomDomainTypeDef]
    VpcDNSTargets: List[VpcDNSTargetTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateCustomDomainResponseTypeDef(BaseModel):
    DNSTarget: str
    ServiceArn: str
    CustomDomain: CustomDomainTypeDef
    VpcDNSTargets: List[VpcDNSTargetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CodeRepositoryTypeDef(BaseModel):
    RepositoryUrl: str
    SourceCodeVersion: SourceCodeVersionTypeDef
    CodeConfiguration: Optional[CodeConfigurationTypeDef] = None
    SourceDirectory: Optional[str] = None

class CreateObservabilityConfigurationResponseTypeDef(BaseModel):
    ObservabilityConfiguration: ObservabilityConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteObservabilityConfigurationResponseTypeDef(BaseModel):
    ObservabilityConfiguration: ObservabilityConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeObservabilityConfigurationResponseTypeDef(BaseModel):
    ObservabilityConfiguration: ObservabilityConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVpcIngressConnectionResponseTypeDef(BaseModel):
    VpcIngressConnection: VpcIngressConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVpcIngressConnectionResponseTypeDef(BaseModel):
    VpcIngressConnection: VpcIngressConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVpcIngressConnectionResponseTypeDef(BaseModel):
    VpcIngressConnection: VpcIngressConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVpcIngressConnectionResponseTypeDef(BaseModel):
    VpcIngressConnection: VpcIngressConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SourceConfigurationTypeDef(BaseModel):
    CodeRepository: Optional[CodeRepositoryTypeDef] = None
    ImageRepository: Optional[ImageRepositoryTypeDef] = None
    AutoDeploymentsEnabled: Optional[bool] = None
    AuthenticationConfiguration: Optional[AuthenticationConfigurationTypeDef] = None

class CreateServiceRequestRequestTypeDef(BaseModel):
    ServiceName: str
    SourceConfiguration: SourceConfigurationTypeDef
    InstanceConfiguration: Optional[InstanceConfigurationTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None
    HealthCheckConfiguration: Optional[HealthCheckConfigurationTypeDef] = None
    AutoScalingConfigurationArn: Optional[str] = None
    NetworkConfiguration: Optional[NetworkConfigurationTypeDef] = None
    ObservabilityConfiguration: Optional[ServiceObservabilityConfigurationTypeDef] = None

class ServiceTypeDef(BaseModel):
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

class UpdateServiceRequestRequestTypeDef(BaseModel):
    ServiceArn: str
    SourceConfiguration: Optional[SourceConfigurationTypeDef] = None
    InstanceConfiguration: Optional[InstanceConfigurationTypeDef] = None
    AutoScalingConfigurationArn: Optional[str] = None
    HealthCheckConfiguration: Optional[HealthCheckConfigurationTypeDef] = None
    NetworkConfiguration: Optional[NetworkConfigurationTypeDef] = None
    ObservabilityConfiguration: Optional[ServiceObservabilityConfigurationTypeDef] = None

class CreateServiceResponseTypeDef(BaseModel):
    Service: ServiceTypeDef
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteServiceResponseTypeDef(BaseModel):
    Service: ServiceTypeDef
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeServiceResponseTypeDef(BaseModel):
    Service: ServiceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PauseServiceResponseTypeDef(BaseModel):
    Service: ServiceTypeDef
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResumeServiceResponseTypeDef(BaseModel):
    Service: ServiceTypeDef
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceResponseTypeDef(BaseModel):
    Service: ServiceTypeDef
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef


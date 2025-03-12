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
from aws_resource_validator.pydantic_models.apprunner_constants import *

class AssociateCustomDomainRequestTypeDef(BaseValidatorModel):
    ServiceArn: str
    DomainName: str
    EnableWWWSubdomain: Optional[bool] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


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


class CodeConfigurationValuesOutputTypeDef(BaseValidatorModel):
    Runtime: RuntimeType
    BuildCommand: Optional[str] = None
    StartCommand: Optional[str] = None
    Port: Optional[str] = None
    RuntimeEnvironmentVariables: Optional[Dict[str, str]] = None
    RuntimeEnvironmentSecrets: Optional[Dict[str, str]] = None


class CodeConfigurationValuesTypeDef(BaseValidatorModel):
    Runtime: RuntimeType
    BuildCommand: Optional[str] = None
    StartCommand: Optional[str] = None
    Port: Optional[str] = None
    RuntimeEnvironmentVariables: Optional[Mapping[str, str]] = None
    RuntimeEnvironmentSecrets: Optional[Mapping[str, str]] = None


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


class DeleteAutoScalingConfigurationRequestTypeDef(BaseValidatorModel):
    AutoScalingConfigurationArn: str
    DeleteAllRevisions: Optional[bool] = None


class DeleteConnectionRequestTypeDef(BaseValidatorModel):
    ConnectionArn: str


class DeleteObservabilityConfigurationRequestTypeDef(BaseValidatorModel):
    ObservabilityConfigurationArn: str


class DeleteServiceRequestTypeDef(BaseValidatorModel):
    ServiceArn: str


class DeleteVpcConnectorRequestTypeDef(BaseValidatorModel):
    VpcConnectorArn: str


class DeleteVpcIngressConnectionRequestTypeDef(BaseValidatorModel):
    VpcIngressConnectionArn: str


class DescribeAutoScalingConfigurationRequestTypeDef(BaseValidatorModel):
    AutoScalingConfigurationArn: str


class DescribeCustomDomainsRequestTypeDef(BaseValidatorModel):
    ServiceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeObservabilityConfigurationRequestTypeDef(BaseValidatorModel):
    ObservabilityConfigurationArn: str


class DescribeServiceRequestTypeDef(BaseValidatorModel):
    ServiceArn: str


class DescribeVpcConnectorRequestTypeDef(BaseValidatorModel):
    VpcConnectorArn: str


class DescribeVpcIngressConnectionRequestTypeDef(BaseValidatorModel):
    VpcIngressConnectionArn: str


class DisassociateCustomDomainRequestTypeDef(BaseValidatorModel):
    ServiceArn: str
    DomainName: str


class EgressConfigurationTypeDef(BaseValidatorModel):
    EgressType: Optional[EgressTypeType] = None
    VpcConnectorArn: Optional[str] = None


class ImageConfigurationOutputTypeDef(BaseValidatorModel):
    RuntimeEnvironmentVariables: Optional[Dict[str, str]] = None
    StartCommand: Optional[str] = None
    Port: Optional[str] = None
    RuntimeEnvironmentSecrets: Optional[Dict[str, str]] = None


class ImageConfigurationTypeDef(BaseValidatorModel):
    RuntimeEnvironmentVariables: Optional[Mapping[str, str]] = None
    StartCommand: Optional[str] = None
    Port: Optional[str] = None
    RuntimeEnvironmentSecrets: Optional[Mapping[str, str]] = None


class IngressConfigurationTypeDef(BaseValidatorModel):
    IsPubliclyAccessible: Optional[bool] = None


class ListAutoScalingConfigurationsRequestTypeDef(BaseValidatorModel):
    AutoScalingConfigurationName: Optional[str] = None
    LatestOnly: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListConnectionsRequestTypeDef(BaseValidatorModel):
    ConnectionName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListObservabilityConfigurationsRequestTypeDef(BaseValidatorModel):
    ObservabilityConfigurationName: Optional[str] = None
    LatestOnly: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ObservabilityConfigurationSummaryTypeDef(BaseValidatorModel):
    ObservabilityConfigurationArn: Optional[str] = None
    ObservabilityConfigurationName: Optional[str] = None
    ObservabilityConfigurationRevision: Optional[int] = None


class ListOperationsRequestTypeDef(BaseValidatorModel):
    ServiceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListServicesForAutoScalingConfigurationRequestTypeDef(BaseValidatorModel):
    AutoScalingConfigurationArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListServicesRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class ListVpcConnectorsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListVpcIngressConnectionsFilterTypeDef(BaseValidatorModel):
    ServiceArn: Optional[str] = None
    VpcEndpointId: Optional[str] = None


class VpcIngressConnectionSummaryTypeDef(BaseValidatorModel):
    VpcIngressConnectionArn: Optional[str] = None
    ServiceArn: Optional[str] = None


class PauseServiceRequestTypeDef(BaseValidatorModel):
    ServiceArn: str


class ResumeServiceRequestTypeDef(BaseValidatorModel):
    ServiceArn: str


class StartDeploymentRequestTypeDef(BaseValidatorModel):
    ServiceArn: str


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateDefaultAutoScalingConfigurationRequestTypeDef(BaseValidatorModel):
    AutoScalingConfigurationArn: str


class ListServicesForAutoScalingConfigurationResponseTypeDef(BaseValidatorModel):
    ServiceArnList: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class StartDeploymentResponseTypeDef(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListAutoScalingConfigurationsResponseTypeDef(BaseValidatorModel):
    AutoScalingConfigurationSummaryList: List[AutoScalingConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


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


class CertificateValidationRecordTypeDef(BaseValidatorModel):
    pass


class CustomDomainTypeDef(BaseValidatorModel):
    DomainName: str
    EnableWWWSubdomain: bool
    Status: CustomDomainAssociationStatusType
    CertificateValidationRecords: Optional[List[CertificateValidationRecordTypeDef]] = None


class CodeConfigurationOutputTypeDef(BaseValidatorModel):
    ConfigurationSource: ConfigurationSourceType
    CodeConfigurationValues: Optional[CodeConfigurationValuesOutputTypeDef] = None


class CodeConfigurationTypeDef(BaseValidatorModel):
    ConfigurationSource: ConfigurationSourceType
    CodeConfigurationValues: Optional[CodeConfigurationValuesTypeDef] = None


class ListConnectionsResponseTypeDef(BaseValidatorModel):
    ConnectionSummaryList: List[ConnectionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateConnectionResponseTypeDef(BaseValidatorModel):
    Connection: ConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteConnectionResponseTypeDef(BaseValidatorModel):
    Connection: ConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateAutoScalingConfigurationRequestTypeDef(BaseValidatorModel):
    AutoScalingConfigurationName: str
    MaxConcurrency: Optional[int] = None
    MinSize: Optional[int] = None
    MaxSize: Optional[int] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateConnectionRequestTypeDef(BaseValidatorModel):
    ConnectionName: str
    ProviderType: ProviderTypeType
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateVpcConnectorRequestTypeDef(BaseValidatorModel):
    VpcConnectorName: str
    Subnets: Sequence[str]
    SecurityGroups: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]


class CreateObservabilityConfigurationRequestTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateVpcIngressConnectionRequestTypeDef(BaseValidatorModel):
    ServiceArn: str
    VpcIngressConnectionName: str
    IngressVpcConfiguration: IngressVpcConfigurationTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None


class UpdateVpcIngressConnectionRequestTypeDef(BaseValidatorModel):
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


class ImageRepositoryOutputTypeDef(BaseValidatorModel):
    ImageIdentifier: str
    ImageRepositoryType: ImageRepositoryTypeType
    ImageConfiguration: Optional[ImageConfigurationOutputTypeDef] = None


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
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class OperationSummaryTypeDef(BaseValidatorModel):
    pass


class ListOperationsResponseTypeDef(BaseValidatorModel):
    OperationSummaryList: List[OperationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ServiceSummaryTypeDef(BaseValidatorModel):
    pass


class ListServicesResponseTypeDef(BaseValidatorModel):
    ServiceSummaryList: List[ServiceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListVpcIngressConnectionsRequestTypeDef(BaseValidatorModel):
    Filter: Optional[ListVpcIngressConnectionsFilterTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListVpcIngressConnectionsResponseTypeDef(BaseValidatorModel):
    VpcIngressConnectionSummaryList: List[VpcIngressConnectionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


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
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DisassociateCustomDomainResponseTypeDef(BaseValidatorModel):
    DNSTarget: str
    ServiceArn: str
    CustomDomain: CustomDomainTypeDef
    VpcDNSTargets: List[VpcDNSTargetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class SourceCodeVersionTypeDef(BaseValidatorModel):
    pass


class CodeRepositoryOutputTypeDef(BaseValidatorModel):
    RepositoryUrl: str
    SourceCodeVersion: SourceCodeVersionTypeDef
    CodeConfiguration: Optional[CodeConfigurationOutputTypeDef] = None
    SourceDirectory: Optional[str] = None


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


class SourceConfigurationOutputTypeDef(BaseValidatorModel):
    CodeRepository: Optional[CodeRepositoryOutputTypeDef] = None
    ImageRepository: Optional[ImageRepositoryOutputTypeDef] = None
    AutoDeploymentsEnabled: Optional[bool] = None
    AuthenticationConfiguration: Optional[AuthenticationConfigurationTypeDef] = None


class SourceConfigurationTypeDef(BaseValidatorModel):
    CodeRepository: Optional[CodeRepositoryTypeDef] = None
    ImageRepository: Optional[ImageRepositoryTypeDef] = None
    AutoDeploymentsEnabled: Optional[bool] = None
    AuthenticationConfiguration: Optional[AuthenticationConfigurationTypeDef] = None


class ServiceTypeDef(BaseValidatorModel):
    pass


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


class HealthCheckConfigurationTypeDef(BaseValidatorModel):
    pass


class SourceConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class UpdateServiceRequestTypeDef(BaseValidatorModel):
    ServiceArn: str
    SourceConfiguration: Optional[SourceConfigurationUnionTypeDef] = None
    InstanceConfiguration: Optional[InstanceConfigurationTypeDef] = None
    AutoScalingConfigurationArn: Optional[str] = None
    HealthCheckConfiguration: Optional[HealthCheckConfigurationTypeDef] = None
    NetworkConfiguration: Optional[NetworkConfigurationTypeDef] = None
    ObservabilityConfiguration: Optional[ServiceObservabilityConfigurationTypeDef] = None



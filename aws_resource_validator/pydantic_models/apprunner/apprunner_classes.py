from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.apprunner.apprunner_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AssociateCustomDomainRequest(BaseValidatorModel):
    ServiceArn: str
    DomainName: str
    EnableWWWSubdomain: Optional[bool] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class VpcDNSTarget(BaseValidatorModel):
    VpcIngressConnectionArn: Optional[str] = None
    VpcId: Optional[str] = None
    DomainName: Optional[str] = None


class AuthenticationConfiguration(BaseValidatorModel):
    ConnectionArn: Optional[str] = None
    AccessRoleArn: Optional[str] = None


class AutoScalingConfigurationSummary(BaseValidatorModel):
    AutoScalingConfigurationArn: Optional[str] = None
    AutoScalingConfigurationName: Optional[str] = None
    AutoScalingConfigurationRevision: Optional[int] = None
    Status: Optional[AutoScalingConfigurationStatusType] = None
    CreatedAt: Optional[datetime] = None
    HasAssociatedService: Optional[bool] = None
    IsDefault: Optional[bool] = None


class AutoScalingConfiguration(BaseValidatorModel):
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


class CertificateValidationRecord(BaseValidatorModel):
    Name: Optional[str] = None
    Type: Optional[str] = None
    Value: Optional[str] = None
    Status: Optional[CertificateValidationRecordStatusType] = None


class CodeConfigurationValuesOutput(BaseValidatorModel):
    Runtime: RuntimeType
    BuildCommand: Optional[str] = None
    StartCommand: Optional[str] = None
    Port: Optional[str] = None
    RuntimeEnvironmentVariables: Optional[Dict[str, str]] = None
    RuntimeEnvironmentSecrets: Optional[Dict[str, str]] = None


class CodeConfigurationValues(BaseValidatorModel):
    Runtime: RuntimeType
    BuildCommand: Optional[str] = None
    StartCommand: Optional[str] = None
    Port: Optional[str] = None
    RuntimeEnvironmentVariables: Optional[Dict[str, str]] = None
    RuntimeEnvironmentSecrets: Optional[Dict[str, str]] = None


class SourceCodeVersion(BaseValidatorModel):
    Type: Literal['BRANCH']
    Value: str


class ConnectionSummary(BaseValidatorModel):
    ConnectionName: Optional[str] = None
    ConnectionArn: Optional[str] = None
    ProviderType: Optional[ProviderTypeType] = None
    Status: Optional[ConnectionStatusType] = None
    CreatedAt: Optional[datetime] = None


class Connection(BaseValidatorModel):
    ConnectionName: Optional[str] = None
    ConnectionArn: Optional[str] = None
    ProviderType: Optional[ProviderTypeType] = None
    Status: Optional[ConnectionStatusType] = None
    CreatedAt: Optional[datetime] = None


class Tag(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class TraceConfiguration(BaseValidatorModel):
    Vendor: Literal['AWSXRAY']


class EncryptionConfiguration(BaseValidatorModel):
    KmsKey: str


class HealthCheckConfiguration(BaseValidatorModel):
    Protocol: Optional[HealthCheckProtocolType] = None
    Path: Optional[str] = None
    Interval: Optional[int] = None
    Timeout: Optional[int] = None
    HealthyThreshold: Optional[int] = None
    UnhealthyThreshold: Optional[int] = None


class InstanceConfiguration(BaseValidatorModel):
    Cpu: Optional[str] = None
    Memory: Optional[str] = None
    InstanceRoleArn: Optional[str] = None


class ServiceObservabilityConfiguration(BaseValidatorModel):
    ObservabilityEnabled: bool
    ObservabilityConfigurationArn: Optional[str] = None


class VpcConnector(BaseValidatorModel):
    VpcConnectorName: Optional[str] = None
    VpcConnectorArn: Optional[str] = None
    VpcConnectorRevision: Optional[int] = None
    Subnets: Optional[List[str]] = None
    SecurityGroups: Optional[List[str]] = None
    Status: Optional[VpcConnectorStatusType] = None
    CreatedAt: Optional[datetime] = None
    DeletedAt: Optional[datetime] = None


class IngressVpcConfiguration(BaseValidatorModel):
    VpcId: Optional[str] = None
    VpcEndpointId: Optional[str] = None


class DeleteAutoScalingConfigurationRequest(BaseValidatorModel):
    AutoScalingConfigurationArn: str
    DeleteAllRevisions: Optional[bool] = None


class DeleteConnectionRequest(BaseValidatorModel):
    ConnectionArn: str


class DeleteObservabilityConfigurationRequest(BaseValidatorModel):
    ObservabilityConfigurationArn: str


class DeleteServiceRequest(BaseValidatorModel):
    ServiceArn: str


class DeleteVpcConnectorRequest(BaseValidatorModel):
    VpcConnectorArn: str


class DeleteVpcIngressConnectionRequest(BaseValidatorModel):
    VpcIngressConnectionArn: str


class DescribeAutoScalingConfigurationRequest(BaseValidatorModel):
    AutoScalingConfigurationArn: str


class DescribeCustomDomainsRequest(BaseValidatorModel):
    ServiceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeObservabilityConfigurationRequest(BaseValidatorModel):
    ObservabilityConfigurationArn: str


class DescribeServiceRequest(BaseValidatorModel):
    ServiceArn: str


class DescribeVpcConnectorRequest(BaseValidatorModel):
    VpcConnectorArn: str


class DescribeVpcIngressConnectionRequest(BaseValidatorModel):
    VpcIngressConnectionArn: str


class DisassociateCustomDomainRequest(BaseValidatorModel):
    ServiceArn: str
    DomainName: str


class EgressConfiguration(BaseValidatorModel):
    EgressType: Optional[EgressTypeType] = None
    VpcConnectorArn: Optional[str] = None


class ImageConfigurationOutput(BaseValidatorModel):
    RuntimeEnvironmentVariables: Optional[Dict[str, str]] = None
    StartCommand: Optional[str] = None
    Port: Optional[str] = None
    RuntimeEnvironmentSecrets: Optional[Dict[str, str]] = None


class ImageConfiguration(BaseValidatorModel):
    RuntimeEnvironmentVariables: Optional[Dict[str, str]] = None
    StartCommand: Optional[str] = None
    Port: Optional[str] = None
    RuntimeEnvironmentSecrets: Optional[Dict[str, str]] = None


class IngressConfiguration(BaseValidatorModel):
    IsPubliclyAccessible: Optional[bool] = None


class ListAutoScalingConfigurationsRequest(BaseValidatorModel):
    AutoScalingConfigurationName: Optional[str] = None
    LatestOnly: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListConnectionsRequest(BaseValidatorModel):
    ConnectionName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListObservabilityConfigurationsRequest(BaseValidatorModel):
    ObservabilityConfigurationName: Optional[str] = None
    LatestOnly: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ObservabilityConfigurationSummary(BaseValidatorModel):
    ObservabilityConfigurationArn: Optional[str] = None
    ObservabilityConfigurationName: Optional[str] = None
    ObservabilityConfigurationRevision: Optional[int] = None


class ListOperationsRequest(BaseValidatorModel):
    ServiceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class OperationSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Type: Optional[OperationTypeType] = None
    Status: Optional[OperationStatusType] = None
    TargetArn: Optional[str] = None
    StartedAt: Optional[datetime] = None
    EndedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None


class ListServicesForAutoScalingConfigurationRequest(BaseValidatorModel):
    AutoScalingConfigurationArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListServicesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ServiceSummary(BaseValidatorModel):
    ServiceName: Optional[str] = None
    ServiceId: Optional[str] = None
    ServiceArn: Optional[str] = None
    ServiceUrl: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None
    Status: Optional[ServiceStatusType] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class ListVpcConnectorsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListVpcIngressConnectionsFilter(BaseValidatorModel):
    ServiceArn: Optional[str] = None
    VpcEndpointId: Optional[str] = None


class VpcIngressConnectionSummary(BaseValidatorModel):
    VpcIngressConnectionArn: Optional[str] = None
    ServiceArn: Optional[str] = None


class PauseServiceRequest(BaseValidatorModel):
    ServiceArn: str


class ResumeServiceRequest(BaseValidatorModel):
    ServiceArn: str


class StartDeploymentRequest(BaseValidatorModel):
    ServiceArn: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class UpdateDefaultAutoScalingConfigurationRequest(BaseValidatorModel):
    AutoScalingConfigurationArn: str


class ListServicesForAutoScalingConfigurationResponse(BaseValidatorModel):
    ServiceArnList: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class StartDeploymentResponse(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


class ListAutoScalingConfigurationsResponse(BaseValidatorModel):
    AutoScalingConfigurationSummaryList: List[AutoScalingConfigurationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateAutoScalingConfigurationResponse(BaseValidatorModel):
    AutoScalingConfiguration: AutoScalingConfiguration
    ResponseMetadata: ResponseMetadata


class DeleteAutoScalingConfigurationResponse(BaseValidatorModel):
    AutoScalingConfiguration: AutoScalingConfiguration
    ResponseMetadata: ResponseMetadata


class DescribeAutoScalingConfigurationResponse(BaseValidatorModel):
    AutoScalingConfiguration: AutoScalingConfiguration
    ResponseMetadata: ResponseMetadata


class UpdateDefaultAutoScalingConfigurationResponse(BaseValidatorModel):
    AutoScalingConfiguration: AutoScalingConfiguration
    ResponseMetadata: ResponseMetadata


class CustomDomain(BaseValidatorModel):
    DomainName: str
    EnableWWWSubdomain: bool
    Status: CustomDomainAssociationStatusType
    CertificateValidationRecords: Optional[List[CertificateValidationRecord]] = None


class CodeConfigurationOutput(BaseValidatorModel):
    ConfigurationSource: ConfigurationSourceType
    CodeConfigurationValues: Optional[CodeConfigurationValuesOutput] = None


class CodeConfiguration(BaseValidatorModel):
    ConfigurationSource: ConfigurationSourceType
    CodeConfigurationValues: Optional[CodeConfigurationValues] = None


class ListConnectionsResponse(BaseValidatorModel):
    ConnectionSummaryList: List[ConnectionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateConnectionResponse(BaseValidatorModel):
    Connection: Connection
    ResponseMetadata: ResponseMetadata


class DeleteConnectionResponse(BaseValidatorModel):
    Connection: Connection
    ResponseMetadata: ResponseMetadata


class CreateAutoScalingConfigurationRequest(BaseValidatorModel):
    AutoScalingConfigurationName: str
    MaxConcurrency: Optional[int] = None
    MinSize: Optional[int] = None
    MaxSize: Optional[int] = None
    Tags: Optional[List[Tag]] = None


class CreateConnectionRequest(BaseValidatorModel):
    ConnectionName: str
    ProviderType: ProviderTypeType
    Tags: Optional[List[Tag]] = None


class CreateVpcConnectorRequest(BaseValidatorModel):
    VpcConnectorName: str
    Subnets: List[str]
    SecurityGroups: Optional[List[str]] = None
    Tags: Optional[List[Tag]] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]


class CreateObservabilityConfigurationRequest(BaseValidatorModel):
    ObservabilityConfigurationName: str
    TraceConfiguration: Optional[TraceConfiguration] = None
    Tags: Optional[List[Tag]] = None


class ObservabilityConfiguration(BaseValidatorModel):
    ObservabilityConfigurationArn: Optional[str] = None
    ObservabilityConfigurationName: Optional[str] = None
    TraceConfiguration: Optional[TraceConfiguration] = None
    ObservabilityConfigurationRevision: Optional[int] = None
    Latest: Optional[bool] = None
    Status: Optional[ObservabilityConfigurationStatusType] = None
    CreatedAt: Optional[datetime] = None
    DeletedAt: Optional[datetime] = None


class CreateVpcConnectorResponse(BaseValidatorModel):
    VpcConnector: VpcConnector
    ResponseMetadata: ResponseMetadata


class DeleteVpcConnectorResponse(BaseValidatorModel):
    VpcConnector: VpcConnector
    ResponseMetadata: ResponseMetadata


class DescribeVpcConnectorResponse(BaseValidatorModel):
    VpcConnector: VpcConnector
    ResponseMetadata: ResponseMetadata


class ListVpcConnectorsResponse(BaseValidatorModel):
    VpcConnectors: List[VpcConnector]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateVpcIngressConnectionRequest(BaseValidatorModel):
    ServiceArn: str
    VpcIngressConnectionName: str
    IngressVpcConfiguration: IngressVpcConfiguration
    Tags: Optional[List[Tag]] = None


class UpdateVpcIngressConnectionRequest(BaseValidatorModel):
    VpcIngressConnectionArn: str
    IngressVpcConfiguration: IngressVpcConfiguration


class VpcIngressConnection(BaseValidatorModel):
    VpcIngressConnectionArn: Optional[str] = None
    VpcIngressConnectionName: Optional[str] = None
    ServiceArn: Optional[str] = None
    Status: Optional[VpcIngressConnectionStatusType] = None
    AccountId: Optional[str] = None
    DomainName: Optional[str] = None
    IngressVpcConfiguration: Optional[IngressVpcConfiguration] = None
    CreatedAt: Optional[datetime] = None
    DeletedAt: Optional[datetime] = None


class ImageRepositoryOutput(BaseValidatorModel):
    ImageIdentifier: str
    ImageRepositoryType: ImageRepositoryTypeType
    ImageConfiguration: Optional[ImageConfigurationOutput] = None


class ImageRepository(BaseValidatorModel):
    ImageIdentifier: str
    ImageRepositoryType: ImageRepositoryTypeType
    ImageConfiguration: Optional[ImageConfiguration] = None


class NetworkConfiguration(BaseValidatorModel):
    EgressConfiguration: Optional[EgressConfiguration] = None
    IngressConfiguration: Optional[IngressConfiguration] = None
    IpAddressType: Optional[IpAddressTypeType] = None


class ListObservabilityConfigurationsResponse(BaseValidatorModel):
    ObservabilityConfigurationSummaryList: List[ObservabilityConfigurationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListOperationsResponse(BaseValidatorModel):
    OperationSummaryList: List[OperationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListServicesResponse(BaseValidatorModel):
    ServiceSummaryList: List[ServiceSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListVpcIngressConnectionsRequest(BaseValidatorModel):
    Filter: Optional[ListVpcIngressConnectionsFilter] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListVpcIngressConnectionsResponse(BaseValidatorModel):
    VpcIngressConnectionSummaryList: List[VpcIngressConnectionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AssociateCustomDomainResponse(BaseValidatorModel):
    DNSTarget: str
    ServiceArn: str
    CustomDomain: CustomDomain
    VpcDNSTargets: List[VpcDNSTarget]
    ResponseMetadata: ResponseMetadata


class DescribeCustomDomainsResponse(BaseValidatorModel):
    DNSTarget: str
    ServiceArn: str
    CustomDomains: List[CustomDomain]
    VpcDNSTargets: List[VpcDNSTarget]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DisassociateCustomDomainResponse(BaseValidatorModel):
    DNSTarget: str
    ServiceArn: str
    CustomDomain: CustomDomain
    VpcDNSTargets: List[VpcDNSTarget]
    ResponseMetadata: ResponseMetadata


class CodeRepositoryOutput(BaseValidatorModel):
    RepositoryUrl: str
    SourceCodeVersion: SourceCodeVersion
    CodeConfiguration: Optional[CodeConfigurationOutput] = None
    SourceDirectory: Optional[str] = None


class CodeRepository(BaseValidatorModel):
    RepositoryUrl: str
    SourceCodeVersion: SourceCodeVersion
    CodeConfiguration: Optional[CodeConfiguration] = None
    SourceDirectory: Optional[str] = None


class CreateObservabilityConfigurationResponse(BaseValidatorModel):
    ObservabilityConfiguration: ObservabilityConfiguration
    ResponseMetadata: ResponseMetadata


class DeleteObservabilityConfigurationResponse(BaseValidatorModel):
    ObservabilityConfiguration: ObservabilityConfiguration
    ResponseMetadata: ResponseMetadata


class DescribeObservabilityConfigurationResponse(BaseValidatorModel):
    ObservabilityConfiguration: ObservabilityConfiguration
    ResponseMetadata: ResponseMetadata


class CreateVpcIngressConnectionResponse(BaseValidatorModel):
    VpcIngressConnection: VpcIngressConnection
    ResponseMetadata: ResponseMetadata


class DeleteVpcIngressConnectionResponse(BaseValidatorModel):
    VpcIngressConnection: VpcIngressConnection
    ResponseMetadata: ResponseMetadata


class DescribeVpcIngressConnectionResponse(BaseValidatorModel):
    VpcIngressConnection: VpcIngressConnection
    ResponseMetadata: ResponseMetadata


class UpdateVpcIngressConnectionResponse(BaseValidatorModel):
    VpcIngressConnection: VpcIngressConnection
    ResponseMetadata: ResponseMetadata


class SourceConfigurationOutput(BaseValidatorModel):
    CodeRepository: Optional[CodeRepositoryOutput] = None
    ImageRepository: Optional[ImageRepositoryOutput] = None
    AutoDeploymentsEnabled: Optional[bool] = None
    AuthenticationConfiguration: Optional[AuthenticationConfiguration] = None


class SourceConfiguration(BaseValidatorModel):
    CodeRepository: Optional[CodeRepository] = None
    ImageRepository: Optional[ImageRepository] = None
    AutoDeploymentsEnabled: Optional[bool] = None
    AuthenticationConfiguration: Optional[AuthenticationConfiguration] = None


class Service(BaseValidatorModel):
    ServiceName: str
    ServiceId: str
    ServiceArn: str
    CreatedAt: datetime
    UpdatedAt: datetime
    Status: ServiceStatusType
    SourceConfiguration: SourceConfigurationOutput
    InstanceConfiguration: InstanceConfiguration
    AutoScalingConfigurationSummary: AutoScalingConfigurationSummary
    NetworkConfiguration: NetworkConfiguration
    ServiceUrl: Optional[str] = None
    DeletedAt: Optional[datetime] = None
    EncryptionConfiguration: Optional[EncryptionConfiguration] = None
    HealthCheckConfiguration: Optional[HealthCheckConfiguration] = None
    ObservabilityConfiguration: Optional[ServiceObservabilityConfiguration] = None

SourceConfigurationUnion = Union[SourceConfiguration, SourceConfigurationOutput]


class CreateServiceResponse(BaseValidatorModel):
    Service: Service
    OperationId: str
    ResponseMetadata: ResponseMetadata


class DeleteServiceResponse(BaseValidatorModel):
    Service: Service
    OperationId: str
    ResponseMetadata: ResponseMetadata


class DescribeServiceResponse(BaseValidatorModel):
    Service: Service
    ResponseMetadata: ResponseMetadata


class PauseServiceResponse(BaseValidatorModel):
    Service: Service
    OperationId: str
    ResponseMetadata: ResponseMetadata


class ResumeServiceResponse(BaseValidatorModel):
    Service: Service
    OperationId: str
    ResponseMetadata: ResponseMetadata


class UpdateServiceResponse(BaseValidatorModel):
    Service: Service
    OperationId: str
    ResponseMetadata: ResponseMetadata


class CreateServiceRequest(BaseValidatorModel):
    ServiceName: str
    SourceConfiguration: SourceConfigurationUnion
    InstanceConfiguration: Optional[InstanceConfiguration] = None
    Tags: Optional[List[Tag]] = None
    EncryptionConfiguration: Optional[EncryptionConfiguration] = None
    HealthCheckConfiguration: Optional[HealthCheckConfiguration] = None
    AutoScalingConfigurationArn: Optional[str] = None
    NetworkConfiguration: Optional[NetworkConfiguration] = None
    ObservabilityConfiguration: Optional[ServiceObservabilityConfiguration] = None


class UpdateServiceRequest(BaseValidatorModel):
    ServiceArn: str
    SourceConfiguration: Optional[SourceConfigurationUnion] = None
    InstanceConfiguration: Optional[InstanceConfiguration] = None
    AutoScalingConfigurationArn: Optional[str] = None
    HealthCheckConfiguration: Optional[HealthCheckConfiguration] = None
    NetworkConfiguration: Optional[NetworkConfiguration] = None
    ObservabilityConfiguration: Optional[ServiceObservabilityConfiguration] = None
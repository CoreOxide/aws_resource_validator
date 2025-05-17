from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.apprunner.apprunner_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




# This class is the input for the 'associate_custom_domain' function.
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


# This class is the input for the 'delete_auto_scaling_configuration' function.
class DeleteAutoScalingConfigurationRequest(BaseValidatorModel):
    AutoScalingConfigurationArn: str
    DeleteAllRevisions: Optional[bool] = None


# This class is the input for the 'delete_connection' function.
class DeleteConnectionRequest(BaseValidatorModel):
    ConnectionArn: str


# This class is the input for the 'delete_observability_configuration' function.
class DeleteObservabilityConfigurationRequest(BaseValidatorModel):
    ObservabilityConfigurationArn: str


# This class is the input for the 'delete_service' function.
class DeleteServiceRequest(BaseValidatorModel):
    ServiceArn: str


# This class is the input for the 'delete_vpc_connector' function.
class DeleteVpcConnectorRequest(BaseValidatorModel):
    VpcConnectorArn: str


# This class is the input for the 'delete_vpc_ingress_connection' function.
class DeleteVpcIngressConnectionRequest(BaseValidatorModel):
    VpcIngressConnectionArn: str


# This class is the input for the 'describe_auto_scaling_configuration' function.
class DescribeAutoScalingConfigurationRequest(BaseValidatorModel):
    AutoScalingConfigurationArn: str


# This class is the input for the 'describe_custom_domains' function.
class DescribeCustomDomainsRequest(BaseValidatorModel):
    ServiceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'describe_observability_configuration' function.
class DescribeObservabilityConfigurationRequest(BaseValidatorModel):
    ObservabilityConfigurationArn: str


# This class is the input for the 'describe_service' function.
class DescribeServiceRequest(BaseValidatorModel):
    ServiceArn: str


# This class is the input for the 'describe_vpc_connector' function.
class DescribeVpcConnectorRequest(BaseValidatorModel):
    VpcConnectorArn: str


# This class is the input for the 'describe_vpc_ingress_connection' function.
class DescribeVpcIngressConnectionRequest(BaseValidatorModel):
    VpcIngressConnectionArn: str


# This class is the input for the 'disassociate_custom_domain' function.
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


# This class is the input for the 'list_auto_scaling_configurations' function.
class ListAutoScalingConfigurationsRequest(BaseValidatorModel):
    AutoScalingConfigurationName: Optional[str] = None
    LatestOnly: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_connections' function.
class ListConnectionsRequest(BaseValidatorModel):
    ConnectionName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_observability_configurations' function.
class ListObservabilityConfigurationsRequest(BaseValidatorModel):
    ObservabilityConfigurationName: Optional[str] = None
    LatestOnly: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ObservabilityConfigurationSummary(BaseValidatorModel):
    ObservabilityConfigurationArn: Optional[str] = None
    ObservabilityConfigurationName: Optional[str] = None
    ObservabilityConfigurationRevision: Optional[int] = None


# This class is the input for the 'list_operations' function.
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


# This class is the input for the 'list_services_for_auto_scaling_configuration' function.
class ListServicesForAutoScalingConfigurationRequest(BaseValidatorModel):
    AutoScalingConfigurationArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_services' function.
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


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


# This class is the input for the 'list_vpc_connectors' function.
class ListVpcConnectorsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListVpcIngressConnectionsFilter(BaseValidatorModel):
    ServiceArn: Optional[str] = None
    VpcEndpointId: Optional[str] = None


class VpcIngressConnectionSummary(BaseValidatorModel):
    VpcIngressConnectionArn: Optional[str] = None
    ServiceArn: Optional[str] = None


# This class is the input for the 'pause_service' function.
class PauseServiceRequest(BaseValidatorModel):
    ServiceArn: str


# This class is the input for the 'resume_service' function.
class ResumeServiceRequest(BaseValidatorModel):
    ServiceArn: str


# This class is the input for the 'start_deployment' function.
class StartDeploymentRequest(BaseValidatorModel):
    ServiceArn: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


# This class is the input for the 'update_default_auto_scaling_configuration' function.
class UpdateDefaultAutoScalingConfigurationRequest(BaseValidatorModel):
    AutoScalingConfigurationArn: str


# This class is the output for the 'list_services_for_auto_scaling_configuration' function.
class ListServicesForAutoScalingConfigurationResponse(BaseValidatorModel):
    ServiceArnList: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'start_deployment' function.
class StartDeploymentResponse(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_auto_scaling_configurations' function.
class ListAutoScalingConfigurationsResponse(BaseValidatorModel):
    AutoScalingConfigurationSummaryList: List[AutoScalingConfigurationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_auto_scaling_configuration' function.
class CreateAutoScalingConfigurationResponse(BaseValidatorModel):
    AutoScalingConfiguration: AutoScalingConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_auto_scaling_configuration' function.
class DeleteAutoScalingConfigurationResponse(BaseValidatorModel):
    AutoScalingConfiguration: AutoScalingConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_auto_scaling_configuration' function.
class DescribeAutoScalingConfigurationResponse(BaseValidatorModel):
    AutoScalingConfiguration: AutoScalingConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_default_auto_scaling_configuration' function.
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


# This class is the output for the 'list_connections' function.
class ListConnectionsResponse(BaseValidatorModel):
    ConnectionSummaryList: List[ConnectionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_connection' function.
class CreateConnectionResponse(BaseValidatorModel):
    Connection: Connection
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_connection' function.
class DeleteConnectionResponse(BaseValidatorModel):
    Connection: Connection
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_auto_scaling_configuration' function.
class CreateAutoScalingConfigurationRequest(BaseValidatorModel):
    AutoScalingConfigurationName: str
    MaxConcurrency: Optional[int] = None
    MinSize: Optional[int] = None
    MaxSize: Optional[int] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_connection' function.
class CreateConnectionRequest(BaseValidatorModel):
    ConnectionName: str
    ProviderType: ProviderTypeType
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_vpc_connector' function.
class CreateVpcConnectorRequest(BaseValidatorModel):
    VpcConnectorName: str
    Subnets: List[str]
    SecurityGroups: Optional[List[str]] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]


# This class is the input for the 'create_observability_configuration' function.
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


# This class is the output for the 'create_vpc_connector' function.
class CreateVpcConnectorResponse(BaseValidatorModel):
    VpcConnector: VpcConnector
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_vpc_connector' function.
class DeleteVpcConnectorResponse(BaseValidatorModel):
    VpcConnector: VpcConnector
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_vpc_connector' function.
class DescribeVpcConnectorResponse(BaseValidatorModel):
    VpcConnector: VpcConnector
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_vpc_connectors' function.
class ListVpcConnectorsResponse(BaseValidatorModel):
    VpcConnectors: List[VpcConnector]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'create_vpc_ingress_connection' function.
class CreateVpcIngressConnectionRequest(BaseValidatorModel):
    ServiceArn: str
    VpcIngressConnectionName: str
    IngressVpcConfiguration: IngressVpcConfiguration
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'update_vpc_ingress_connection' function.
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


# This class is the output for the 'list_observability_configurations' function.
class ListObservabilityConfigurationsResponse(BaseValidatorModel):
    ObservabilityConfigurationSummaryList: List[ObservabilityConfigurationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_operations' function.
class ListOperationsResponse(BaseValidatorModel):
    OperationSummaryList: List[OperationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_services' function.
class ListServicesResponse(BaseValidatorModel):
    ServiceSummaryList: List[ServiceSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'list_vpc_ingress_connections' function.
class ListVpcIngressConnectionsRequest(BaseValidatorModel):
    Filter: Optional[ListVpcIngressConnectionsFilter] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the output for the 'list_vpc_ingress_connections' function.
class ListVpcIngressConnectionsResponse(BaseValidatorModel):
    VpcIngressConnectionSummaryList: List[VpcIngressConnectionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'associate_custom_domain' function.
class AssociateCustomDomainResponse(BaseValidatorModel):
    DNSTarget: str
    ServiceArn: str
    CustomDomain: CustomDomain
    VpcDNSTargets: List[VpcDNSTarget]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_custom_domains' function.
class DescribeCustomDomainsResponse(BaseValidatorModel):
    DNSTarget: str
    ServiceArn: str
    CustomDomains: List[CustomDomain]
    VpcDNSTargets: List[VpcDNSTarget]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'disassociate_custom_domain' function.
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


# This class is the output for the 'create_observability_configuration' function.
class CreateObservabilityConfigurationResponse(BaseValidatorModel):
    ObservabilityConfiguration: ObservabilityConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_observability_configuration' function.
class DeleteObservabilityConfigurationResponse(BaseValidatorModel):
    ObservabilityConfiguration: ObservabilityConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_observability_configuration' function.
class DescribeObservabilityConfigurationResponse(BaseValidatorModel):
    ObservabilityConfiguration: ObservabilityConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_vpc_ingress_connection' function.
class CreateVpcIngressConnectionResponse(BaseValidatorModel):
    VpcIngressConnection: VpcIngressConnection
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_vpc_ingress_connection' function.
class DeleteVpcIngressConnectionResponse(BaseValidatorModel):
    VpcIngressConnection: VpcIngressConnection
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_vpc_ingress_connection' function.
class DescribeVpcIngressConnectionResponse(BaseValidatorModel):
    VpcIngressConnection: VpcIngressConnection
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_vpc_ingress_connection' function.
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


# This class is the output for the 'create_service' function.
class CreateServiceResponse(BaseValidatorModel):
    Service: Service
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_service' function.
class DeleteServiceResponse(BaseValidatorModel):
    Service: Service
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_service' function.
class DescribeServiceResponse(BaseValidatorModel):
    Service: Service
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'pause_service' function.
class PauseServiceResponse(BaseValidatorModel):
    Service: Service
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'resume_service' function.
class ResumeServiceResponse(BaseValidatorModel):
    Service: Service
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_service' function.
class UpdateServiceResponse(BaseValidatorModel):
    Service: Service
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_service' function.
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


# This class is the input for the 'update_service' function.
class UpdateServiceRequest(BaseValidatorModel):
    ServiceArn: str
    SourceConfiguration: Optional[SourceConfigurationUnion] = None
    InstanceConfiguration: Optional[InstanceConfiguration] = None
    AutoScalingConfigurationArn: Optional[str] = None
    HealthCheckConfiguration: Optional[HealthCheckConfiguration] = None
    NetworkConfiguration: Optional[NetworkConfiguration] = None
    ObservabilityConfiguration: Optional[ServiceObservabilityConfiguration] = None
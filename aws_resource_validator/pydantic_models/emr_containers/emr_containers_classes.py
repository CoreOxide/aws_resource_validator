from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.emr_containers.emr_containers_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




# This class is the input for the 'cancel_job_run' function.
class CancelJobRunRequest(BaseValidatorModel):
    id: str
    virtualClusterId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class Certificate(BaseValidatorModel):
    certificateArn: Optional[str] = None
    certificateData: Optional[str] = None


class CloudWatchMonitoringConfiguration(BaseValidatorModel):
    logGroupName: str
    logStreamNamePrefix: Optional[str] = None


class ConfigurationOutput(BaseValidatorModel):
    classification: str
    properties: Optional[Dict[str, str]] = None
    configurations: Optional[List[Dict[str, Any]]] = None


class ConfigurationPaginator(BaseValidatorModel):
    classification: str
    properties: Optional[Dict[str, str]] = None
    configurations: Optional[List[Dict[str, Any]]] = None


class Configuration(BaseValidatorModel):
    classification: str
    properties: Optional[Dict[str, str]] = None
    configurations: Optional[List[Dict[str, Any]]] = None


class EksInfo(BaseValidatorModel):
    namespace: Optional[str] = None


class ContainerLogRotationConfiguration(BaseValidatorModel):
    rotationSize: str
    maxFilesToKeep: int


class Credentials(BaseValidatorModel):
    token: Optional[str] = None


# This class is the input for the 'delete_job_template' function.
class DeleteJobTemplateRequest(BaseValidatorModel):
    id: str


# This class is the input for the 'delete_managed_endpoint' function.
class DeleteManagedEndpointRequest(BaseValidatorModel):
    id: str
    virtualClusterId: str


# This class is the input for the 'delete_virtual_cluster' function.
class DeleteVirtualClusterRequest(BaseValidatorModel):
    id: str


# This class is the input for the 'describe_job_run' function.
class DescribeJobRunRequest(BaseValidatorModel):
    id: str
    virtualClusterId: str


# This class is the input for the 'describe_job_template' function.
class DescribeJobTemplateRequest(BaseValidatorModel):
    id: str


# This class is the input for the 'describe_managed_endpoint' function.
class DescribeManagedEndpointRequest(BaseValidatorModel):
    id: str
    virtualClusterId: str


# This class is the input for the 'describe_security_configuration' function.
class DescribeSecurityConfigurationRequest(BaseValidatorModel):
    id: str


# This class is the input for the 'describe_virtual_cluster' function.
class DescribeVirtualClusterRequest(BaseValidatorModel):
    id: str


# This class is the input for the 'get_managed_endpoint_session_credentials' function.
class GetManagedEndpointSessionCredentialsRequest(BaseValidatorModel):
    endpointIdentifier: str
    virtualClusterIdentifier: str
    executionRoleArn: str
    credentialType: str
    durationInSeconds: Optional[int] = None
    logContext: Optional[str] = None
    clientToken: Optional[str] = None


class TLSCertificateConfiguration(BaseValidatorModel):
    certificateProviderType: Optional[Literal['PEM']] = None
    publicCertificateSecretArn: Optional[str] = None
    privateCertificateSecretArn: Optional[str] = None


class SparkSqlJobDriver(BaseValidatorModel):
    entryPoint: Optional[str] = None
    sparkSqlParameters: Optional[str] = None


class SparkSubmitJobDriverOutput(BaseValidatorModel):
    entryPoint: str
    entryPointArguments: Optional[List[str]] = None
    sparkSubmitParameters: Optional[str] = None


class SparkSubmitJobDriver(BaseValidatorModel):
    entryPoint: str
    entryPointArguments: Optional[List[str]] = None
    sparkSubmitParameters: Optional[str] = None


class RetryPolicyConfiguration(BaseValidatorModel):
    maxAttempts: int


class RetryPolicyExecution(BaseValidatorModel):
    currentAttemptCount: int


class TemplateParameterConfiguration(BaseValidatorModel):
    type: Optional[TemplateParameterDataTypeType] = None
    defaultValue: Optional[str] = None


class SecureNamespaceInfo(BaseValidatorModel):
    clusterId: Optional[str] = None
    namespace: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

Timestamp = Union[datetime, str]


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class ManagedLogs(BaseValidatorModel):
    allowAWSToRetainLogs: Optional[AllowAWSToRetainLogsType] = None
    encryptionKeyArn: Optional[str] = None


class S3MonitoringConfiguration(BaseValidatorModel):
    logUri: str


class ParametricCloudWatchMonitoringConfiguration(BaseValidatorModel):
    logGroupName: Optional[str] = None
    logStreamNamePrefix: Optional[str] = None


class ParametricS3MonitoringConfiguration(BaseValidatorModel):
    logUri: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the output for the 'cancel_job_run' function.
class CancelJobRunResponse(BaseValidatorModel):
    id: str
    virtualClusterId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_job_template' function.
class CreateJobTemplateResponse(BaseValidatorModel):
    id: str
    name: str
    arn: str
    createdAt: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_managed_endpoint' function.
class CreateManagedEndpointResponse(BaseValidatorModel):
    id: str
    name: str
    arn: str
    virtualClusterId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_security_configuration' function.
class CreateSecurityConfigurationResponse(BaseValidatorModel):
    id: str
    name: str
    arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_virtual_cluster' function.
class CreateVirtualClusterResponse(BaseValidatorModel):
    id: str
    name: str
    arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_job_template' function.
class DeleteJobTemplateResponse(BaseValidatorModel):
    id: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_managed_endpoint' function.
class DeleteManagedEndpointResponse(BaseValidatorModel):
    id: str
    virtualClusterId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_virtual_cluster' function.
class DeleteVirtualClusterResponse(BaseValidatorModel):
    id: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_job_run' function.
class StartJobRunResponse(BaseValidatorModel):
    id: str
    name: str
    arn: str
    virtualClusterId: str
    ResponseMetadata: ResponseMetadata


class ContainerInfo(BaseValidatorModel):
    eksInfo: Optional[EksInfo] = None


# This class is the output for the 'get_managed_endpoint_session_credentials' function.
class GetManagedEndpointSessionCredentialsResponse(BaseValidatorModel):
    id: str
    credentials: Credentials
    expiresAt: datetime
    ResponseMetadata: ResponseMetadata


class InTransitEncryptionConfiguration(BaseValidatorModel):
    tlsCertificateConfiguration: Optional[TLSCertificateConfiguration] = None


class JobDriverOutput(BaseValidatorModel):
    sparkSubmitJobDriver: Optional[SparkSubmitJobDriverOutput] = None
    sparkSqlJobDriver: Optional[SparkSqlJobDriver] = None


class JobDriver(BaseValidatorModel):
    sparkSubmitJobDriver: Optional[SparkSubmitJobDriver] = None
    sparkSqlJobDriver: Optional[SparkSqlJobDriver] = None


class LakeFormationConfiguration(BaseValidatorModel):
    authorizedSessionTagValue: Optional[str] = None
    secureNamespaceInfo: Optional[SecureNamespaceInfo] = None
    queryEngineRoleArn: Optional[str] = None


class ListJobRunsRequestPaginate(BaseValidatorModel):
    virtualClusterId: str
    createdBefore: Optional[Timestamp] = None
    createdAfter: Optional[Timestamp] = None
    name: Optional[str] = None
    states: Optional[List[JobRunStateType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_job_runs' function.
class ListJobRunsRequest(BaseValidatorModel):
    virtualClusterId: str
    createdBefore: Optional[Timestamp] = None
    createdAfter: Optional[Timestamp] = None
    name: Optional[str] = None
    states: Optional[List[JobRunStateType]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListJobTemplatesRequestPaginate(BaseValidatorModel):
    createdAfter: Optional[Timestamp] = None
    createdBefore: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_job_templates' function.
class ListJobTemplatesRequest(BaseValidatorModel):
    createdAfter: Optional[Timestamp] = None
    createdBefore: Optional[Timestamp] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListManagedEndpointsRequestPaginate(BaseValidatorModel):
    virtualClusterId: str
    createdBefore: Optional[Timestamp] = None
    createdAfter: Optional[Timestamp] = None
    types: Optional[List[str]] = None
    states: Optional[List[EndpointStateType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_managed_endpoints' function.
class ListManagedEndpointsRequest(BaseValidatorModel):
    virtualClusterId: str
    createdBefore: Optional[Timestamp] = None
    createdAfter: Optional[Timestamp] = None
    types: Optional[List[str]] = None
    states: Optional[List[EndpointStateType]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListSecurityConfigurationsRequestPaginate(BaseValidatorModel):
    createdAfter: Optional[Timestamp] = None
    createdBefore: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_security_configurations' function.
class ListSecurityConfigurationsRequest(BaseValidatorModel):
    createdAfter: Optional[Timestamp] = None
    createdBefore: Optional[Timestamp] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListVirtualClustersRequestPaginate(BaseValidatorModel):
    containerProviderId: Optional[str] = None
    containerProviderType: Optional[Literal['EKS']] = None
    createdAfter: Optional[Timestamp] = None
    createdBefore: Optional[Timestamp] = None
    states: Optional[List[VirtualClusterStateType]] = None
    eksAccessEntryIntegrated: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_virtual_clusters' function.
class ListVirtualClustersRequest(BaseValidatorModel):
    containerProviderId: Optional[str] = None
    containerProviderType: Optional[Literal['EKS']] = None
    createdAfter: Optional[Timestamp] = None
    createdBefore: Optional[Timestamp] = None
    states: Optional[List[VirtualClusterStateType]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    eksAccessEntryIntegrated: Optional[bool] = None


class MonitoringConfiguration(BaseValidatorModel):
    managedLogs: Optional[ManagedLogs] = None
    persistentAppUI: Optional[PersistentAppUIType] = None
    cloudWatchMonitoringConfiguration: Optional[CloudWatchMonitoringConfiguration] = None
    s3MonitoringConfiguration: Optional[S3MonitoringConfiguration] = None
    containerLogRotationConfiguration: Optional[ContainerLogRotationConfiguration] = None


class ParametricMonitoringConfiguration(BaseValidatorModel):
    persistentAppUI: Optional[str] = None
    cloudWatchMonitoringConfiguration: Optional[ParametricCloudWatchMonitoringConfiguration] = None
    s3MonitoringConfiguration: Optional[ParametricS3MonitoringConfiguration] = None


class ContainerProvider(BaseValidatorModel):
    type: Literal['EKS']
    id: str
    info: Optional[ContainerInfo] = None


class EncryptionConfiguration(BaseValidatorModel):
    inTransitEncryptionConfiguration: Optional[InTransitEncryptionConfiguration] = None

JobDriverUnion = Union[JobDriver, JobDriverOutput]


class ConfigurationOverridesOutput(BaseValidatorModel):
    applicationConfiguration: Optional[List[ConfigurationOutput]] = None
    monitoringConfiguration: Optional[MonitoringConfiguration] = None


class ConfigurationOverridesPaginator(BaseValidatorModel):
    applicationConfiguration: Optional[List[ConfigurationPaginator]] = None
    monitoringConfiguration: Optional[MonitoringConfiguration] = None


class ConfigurationOverrides(BaseValidatorModel):
    applicationConfiguration: Optional[List[Configuration]] = None
    monitoringConfiguration: Optional[MonitoringConfiguration] = None


class ParametricConfigurationOverridesOutput(BaseValidatorModel):
    applicationConfiguration: Optional[List[ConfigurationOutput]] = None
    monitoringConfiguration: Optional[ParametricMonitoringConfiguration] = None


class ParametricConfigurationOverridesPaginator(BaseValidatorModel):
    applicationConfiguration: Optional[List[ConfigurationPaginator]] = None
    monitoringConfiguration: Optional[ParametricMonitoringConfiguration] = None


class ParametricConfigurationOverrides(BaseValidatorModel):
    applicationConfiguration: Optional[List[Configuration]] = None
    monitoringConfiguration: Optional[ParametricMonitoringConfiguration] = None


# This class is the input for the 'create_virtual_cluster' function.
class CreateVirtualClusterRequest(BaseValidatorModel):
    name: str
    containerProvider: ContainerProvider
    clientToken: str
    tags: Optional[Dict[str, str]] = None
    securityConfigurationId: Optional[str] = None


class VirtualCluster(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    arn: Optional[str] = None
    state: Optional[VirtualClusterStateType] = None
    containerProvider: Optional[ContainerProvider] = None
    createdAt: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None
    securityConfigurationId: Optional[str] = None


class AuthorizationConfiguration(BaseValidatorModel):
    lakeFormationConfiguration: Optional[LakeFormationConfiguration] = None
    encryptionConfiguration: Optional[EncryptionConfiguration] = None


class Endpoint(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    arn: Optional[str] = None
    virtualClusterId: Optional[str] = None
    type: Optional[str] = None
    state: Optional[EndpointStateType] = None
    releaseLabel: Optional[str] = None
    executionRoleArn: Optional[str] = None
    certificateArn: Optional[str] = None
    certificateAuthority: Optional[Certificate] = None
    configurationOverrides: Optional[ConfigurationOverridesOutput] = None
    serverUrl: Optional[str] = None
    createdAt: Optional[datetime] = None
    securityGroup: Optional[str] = None
    subnetIds: Optional[List[str]] = None
    stateDetails: Optional[str] = None
    failureReason: Optional[FailureReasonType] = None
    tags: Optional[Dict[str, str]] = None


class JobRun(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    virtualClusterId: Optional[str] = None
    arn: Optional[str] = None
    state: Optional[JobRunStateType] = None
    clientToken: Optional[str] = None
    executionRoleArn: Optional[str] = None
    releaseLabel: Optional[str] = None
    configurationOverrides: Optional[ConfigurationOverridesOutput] = None
    jobDriver: Optional[JobDriverOutput] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    finishedAt: Optional[datetime] = None
    stateDetails: Optional[str] = None
    failureReason: Optional[FailureReasonType] = None
    tags: Optional[Dict[str, str]] = None
    retryPolicyConfiguration: Optional[RetryPolicyConfiguration] = None
    retryPolicyExecution: Optional[RetryPolicyExecution] = None


class EndpointPaginator(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    arn: Optional[str] = None
    virtualClusterId: Optional[str] = None
    type: Optional[str] = None
    state: Optional[EndpointStateType] = None
    releaseLabel: Optional[str] = None
    executionRoleArn: Optional[str] = None
    certificateArn: Optional[str] = None
    certificateAuthority: Optional[Certificate] = None
    configurationOverrides: Optional[ConfigurationOverridesPaginator] = None
    serverUrl: Optional[str] = None
    createdAt: Optional[datetime] = None
    securityGroup: Optional[str] = None
    subnetIds: Optional[List[str]] = None
    stateDetails: Optional[str] = None
    failureReason: Optional[FailureReasonType] = None
    tags: Optional[Dict[str, str]] = None


class JobRunPaginator(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    virtualClusterId: Optional[str] = None
    arn: Optional[str] = None
    state: Optional[JobRunStateType] = None
    clientToken: Optional[str] = None
    executionRoleArn: Optional[str] = None
    releaseLabel: Optional[str] = None
    configurationOverrides: Optional[ConfigurationOverridesPaginator] = None
    jobDriver: Optional[JobDriverOutput] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    finishedAt: Optional[datetime] = None
    stateDetails: Optional[str] = None
    failureReason: Optional[FailureReasonType] = None
    tags: Optional[Dict[str, str]] = None
    retryPolicyConfiguration: Optional[RetryPolicyConfiguration] = None
    retryPolicyExecution: Optional[RetryPolicyExecution] = None

ConfigurationOverridesUnion = Union[ConfigurationOverrides, ConfigurationOverridesOutput]


class JobTemplateDataOutput(BaseValidatorModel):
    executionRoleArn: str
    releaseLabel: str
    jobDriver: JobDriverOutput
    configurationOverrides: Optional[ParametricConfigurationOverridesOutput] = None
    parameterConfiguration: Optional[Dict[str, TemplateParameterConfiguration]] = None
    jobTags: Optional[Dict[str, str]] = None


class JobTemplateDataPaginator(BaseValidatorModel):
    executionRoleArn: str
    releaseLabel: str
    jobDriver: JobDriverOutput
    configurationOverrides: Optional[ParametricConfigurationOverridesPaginator] = None
    parameterConfiguration: Optional[Dict[str, TemplateParameterConfiguration]] = None
    jobTags: Optional[Dict[str, str]] = None


class JobTemplateData(BaseValidatorModel):
    executionRoleArn: str
    releaseLabel: str
    jobDriver: JobDriver
    configurationOverrides: Optional[ParametricConfigurationOverrides] = None
    parameterConfiguration: Optional[Dict[str, TemplateParameterConfiguration]] = None
    jobTags: Optional[Dict[str, str]] = None


# This class is the output for the 'describe_virtual_cluster' function.
class DescribeVirtualClusterResponse(BaseValidatorModel):
    virtualCluster: VirtualCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_virtual_clusters' function.
class ListVirtualClustersResponse(BaseValidatorModel):
    virtualClusters: List[VirtualCluster]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SecurityConfigurationData(BaseValidatorModel):
    authorizationConfiguration: Optional[AuthorizationConfiguration] = None


# This class is the output for the 'describe_managed_endpoint' function.
class DescribeManagedEndpointResponse(BaseValidatorModel):
    endpoint: Endpoint
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_managed_endpoints' function.
class ListManagedEndpointsResponse(BaseValidatorModel):
    endpoints: List[Endpoint]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'describe_job_run' function.
class DescribeJobRunResponse(BaseValidatorModel):
    jobRun: JobRun
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_job_runs' function.
class ListJobRunsResponse(BaseValidatorModel):
    jobRuns: List[JobRun]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListManagedEndpointsResponsePaginator(BaseValidatorModel):
    endpoints: List[EndpointPaginator]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListJobRunsResponsePaginator(BaseValidatorModel):
    jobRuns: List[JobRunPaginator]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'create_managed_endpoint' function.
class CreateManagedEndpointRequest(BaseValidatorModel):
    name: str
    virtualClusterId: str
    type: str
    releaseLabel: str
    executionRoleArn: str
    clientToken: str
    certificateArn: Optional[str] = None
    configurationOverrides: Optional[ConfigurationOverridesUnion] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'start_job_run' function.
class StartJobRunRequest(BaseValidatorModel):
    virtualClusterId: str
    clientToken: str
    name: Optional[str] = None
    executionRoleArn: Optional[str] = None
    releaseLabel: Optional[str] = None
    jobDriver: Optional[JobDriverUnion] = None
    configurationOverrides: Optional[ConfigurationOverridesUnion] = None
    tags: Optional[Dict[str, str]] = None
    jobTemplateId: Optional[str] = None
    jobTemplateParameters: Optional[Dict[str, str]] = None
    retryPolicyConfiguration: Optional[RetryPolicyConfiguration] = None


class JobTemplate(BaseValidatorModel):
    jobTemplateData: JobTemplateDataOutput
    name: Optional[str] = None
    id: Optional[str] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    kmsKeyArn: Optional[str] = None
    decryptionError: Optional[str] = None


class JobTemplatePaginator(BaseValidatorModel):
    jobTemplateData: JobTemplateDataPaginator
    name: Optional[str] = None
    id: Optional[str] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    kmsKeyArn: Optional[str] = None
    decryptionError: Optional[str] = None

JobTemplateDataUnion = Union[JobTemplateData, JobTemplateDataOutput]


# This class is the input for the 'create_security_configuration' function.
class CreateSecurityConfigurationRequest(BaseValidatorModel):
    clientToken: str
    name: str
    securityConfigurationData: SecurityConfigurationData
    tags: Optional[Dict[str, str]] = None


class SecurityConfiguration(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    securityConfigurationData: Optional[SecurityConfigurationData] = None
    tags: Optional[Dict[str, str]] = None


# This class is the output for the 'describe_job_template' function.
class DescribeJobTemplateResponse(BaseValidatorModel):
    jobTemplate: JobTemplate
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_job_templates' function.
class ListJobTemplatesResponse(BaseValidatorModel):
    templates: List[JobTemplate]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListJobTemplatesResponsePaginator(BaseValidatorModel):
    templates: List[JobTemplatePaginator]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'create_job_template' function.
class CreateJobTemplateRequest(BaseValidatorModel):
    name: str
    clientToken: str
    jobTemplateData: JobTemplateDataUnion
    tags: Optional[Dict[str, str]] = None
    kmsKeyArn: Optional[str] = None


# This class is the output for the 'describe_security_configuration' function.
class DescribeSecurityConfigurationResponse(BaseValidatorModel):
    securityConfiguration: SecurityConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_security_configurations' function.
class ListSecurityConfigurationsResponse(BaseValidatorModel):
    securityConfigurations: List[SecurityConfiguration]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None
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
from aws_resource_validator.pydantic_models.emr_containers_constants import *

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
    properties: Optional[Mapping[str, str]] = None
    configurations: Optional[Sequence[Mapping[str, Any]]] = None


class EksInfo(BaseValidatorModel):
    namespace: Optional[str] = None


class ContainerLogRotationConfiguration(BaseValidatorModel):
    rotationSize: str
    maxFilesToKeep: int


class Credentials(BaseValidatorModel):
    token: Optional[str] = None


class GetManagedEndpointSessionCredentialsRequest(BaseValidatorModel):
    endpointIdentifier: str
    virtualClusterIdentifier: str
    executionRoleArn: str
    credentialType: str
    durationInSeconds: Optional[int] = None
    logContext: Optional[str] = None
    clientToken: Optional[str] = None


class TLSCertificateConfiguration(BaseValidatorModel):
    certificateProviderType: Optional[Literal["PEM"]] = None
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
    entryPointArguments: Optional[Sequence[str]] = None
    sparkSubmitParameters: Optional[str] = None


class RetryPolicyConfiguration(BaseValidatorModel):
    maxAttempts: int


class RetryPolicyExecution(BaseValidatorModel):
    currentAttemptCount: int


class SecureNamespaceInfo(BaseValidatorModel):
    clusterId: Optional[str] = None
    namespace: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


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
    tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ContainerInfo(BaseValidatorModel):
    eksInfo: Optional[EksInfo] = None


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


class Timestamp(BaseValidatorModel):
    pass


class ListJobRunsRequestPaginate(BaseValidatorModel):
    virtualClusterId: str
    createdBefore: Optional[Timestamp] = None
    createdAfter: Optional[Timestamp] = None
    name: Optional[str] = None
    states: Optional[Sequence[JobRunStateType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListJobRunsRequest(BaseValidatorModel):
    virtualClusterId: str
    createdBefore: Optional[Timestamp] = None
    createdAfter: Optional[Timestamp] = None
    name: Optional[str] = None
    states: Optional[Sequence[JobRunStateType]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListJobTemplatesRequestPaginate(BaseValidatorModel):
    createdAfter: Optional[Timestamp] = None
    createdBefore: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListJobTemplatesRequest(BaseValidatorModel):
    createdAfter: Optional[Timestamp] = None
    createdBefore: Optional[Timestamp] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListSecurityConfigurationsRequestPaginate(BaseValidatorModel):
    createdAfter: Optional[Timestamp] = None
    createdBefore: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSecurityConfigurationsRequest(BaseValidatorModel):
    createdAfter: Optional[Timestamp] = None
    createdBefore: Optional[Timestamp] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListVirtualClustersRequestPaginate(BaseValidatorModel):
    containerProviderId: Optional[str] = None
    containerProviderType: Optional[Literal["EKS"]] = None
    createdAfter: Optional[Timestamp] = None
    createdBefore: Optional[Timestamp] = None
    states: Optional[Sequence[VirtualClusterStateType]] = None
    eksAccessEntryIntegrated: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListVirtualClustersRequest(BaseValidatorModel):
    containerProviderId: Optional[str] = None
    containerProviderType: Optional[Literal["EKS"]] = None
    createdAfter: Optional[Timestamp] = None
    createdBefore: Optional[Timestamp] = None
    states: Optional[Sequence[VirtualClusterStateType]] = None
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
    cloudWatchMonitoringConfiguration: Optional[ ParametricCloudWatchMonitoringConfiguration ] = None
    s3MonitoringConfiguration: Optional[ParametricS3MonitoringConfiguration] = None


class EncryptionConfiguration(BaseValidatorModel):
    inTransitEncryptionConfiguration: Optional[InTransitEncryptionConfiguration] = None


class ConfigurationOverridesOutput(BaseValidatorModel):
    applicationConfiguration: Optional[List[ConfigurationOutput]] = None
    monitoringConfiguration: Optional[MonitoringConfiguration] = None


class ConfigurationOverridesPaginator(BaseValidatorModel):
    applicationConfiguration: Optional[List[ConfigurationPaginator]] = None
    monitoringConfiguration: Optional[MonitoringConfiguration] = None


class ConfigurationOverrides(BaseValidatorModel):
    applicationConfiguration: Optional[Sequence[Configuration]] = None
    monitoringConfiguration: Optional[MonitoringConfiguration] = None


class ParametricConfigurationOverridesOutput(BaseValidatorModel):
    applicationConfiguration: Optional[List[ConfigurationOutput]] = None
    monitoringConfiguration: Optional[ParametricMonitoringConfiguration] = None


class ParametricConfigurationOverridesPaginator(BaseValidatorModel):
    applicationConfiguration: Optional[List[ConfigurationPaginator]] = None
    monitoringConfiguration: Optional[ParametricMonitoringConfiguration] = None


class ParametricConfigurationOverrides(BaseValidatorModel):
    applicationConfiguration: Optional[Sequence[Configuration]] = None
    monitoringConfiguration: Optional[ParametricMonitoringConfiguration] = None


class ContainerProvider(BaseValidatorModel):
    pass


class CreateVirtualClusterRequest(BaseValidatorModel):
    name: str
    containerProvider: ContainerProvider
    clientToken: str
    tags: Optional[Mapping[str, str]] = None
    securityConfigurationId: Optional[str] = None


class AuthorizationConfiguration(BaseValidatorModel):
    lakeFormationConfiguration: Optional[LakeFormationConfiguration] = None
    encryptionConfiguration: Optional[EncryptionConfiguration] = None


class TemplateParameterConfiguration(BaseValidatorModel):
    pass


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
    parameterConfiguration: Optional[Mapping[str, TemplateParameterConfiguration]] = None
    jobTags: Optional[Mapping[str, str]] = None


class VirtualCluster(BaseValidatorModel):
    pass


class DescribeVirtualClusterResponse(BaseValidatorModel):
    virtualCluster: VirtualCluster
    ResponseMetadata: ResponseMetadata


class ListVirtualClustersResponse(BaseValidatorModel):
    virtualClusters: List[VirtualCluster]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SecurityConfigurationData(BaseValidatorModel):
    authorizationConfiguration: Optional[AuthorizationConfiguration] = None


class Endpoint(BaseValidatorModel):
    pass


class DescribeManagedEndpointResponse(BaseValidatorModel):
    endpoint: Endpoint
    ResponseMetadata: ResponseMetadata


class ListManagedEndpointsResponse(BaseValidatorModel):
    endpoints: List[Endpoint]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class JobRun(BaseValidatorModel):
    pass


class DescribeJobRunResponse(BaseValidatorModel):
    jobRun: JobRun
    ResponseMetadata: ResponseMetadata


class ListJobRunsResponse(BaseValidatorModel):
    jobRuns: List[JobRun]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class EndpointPaginator(BaseValidatorModel):
    pass


class ListManagedEndpointsResponsePaginator(BaseValidatorModel):
    endpoints: List[EndpointPaginator]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class JobRunPaginator(BaseValidatorModel):
    pass


class ListJobRunsResponsePaginator(BaseValidatorModel):
    jobRuns: List[JobRunPaginator]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class JobDriverUnion(BaseValidatorModel):
    pass


class ConfigurationOverridesUnion(BaseValidatorModel):
    pass


class StartJobRunRequest(BaseValidatorModel):
    virtualClusterId: str
    clientToken: str
    name: Optional[str] = None
    executionRoleArn: Optional[str] = None
    releaseLabel: Optional[str] = None
    jobDriver: Optional[JobDriverUnion] = None
    configurationOverrides: Optional[ConfigurationOverridesUnion] = None
    tags: Optional[Mapping[str, str]] = None
    jobTemplateId: Optional[str] = None
    jobTemplateParameters: Optional[Mapping[str, str]] = None
    retryPolicyConfiguration: Optional[RetryPolicyConfiguration] = None


class CreateSecurityConfigurationRequest(BaseValidatorModel):
    clientToken: str
    name: str
    securityConfigurationData: SecurityConfigurationData
    tags: Optional[Mapping[str, str]] = None


class JobTemplate(BaseValidatorModel):
    pass


class DescribeJobTemplateResponse(BaseValidatorModel):
    jobTemplate: JobTemplate
    ResponseMetadata: ResponseMetadata


class ListJobTemplatesResponse(BaseValidatorModel):
    templates: List[JobTemplate]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class JobTemplatePaginator(BaseValidatorModel):
    pass


class ListJobTemplatesResponsePaginator(BaseValidatorModel):
    templates: List[JobTemplatePaginator]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class JobTemplateDataUnion(BaseValidatorModel):
    pass


class CreateJobTemplateRequest(BaseValidatorModel):
    name: str
    clientToken: str
    jobTemplateData: JobTemplateDataUnion
    tags: Optional[Mapping[str, str]] = None
    kmsKeyArn: Optional[str] = None


class SecurityConfiguration(BaseValidatorModel):
    pass


class DescribeSecurityConfigurationResponse(BaseValidatorModel):
    securityConfiguration: SecurityConfiguration
    ResponseMetadata: ResponseMetadata


class ListSecurityConfigurationsResponse(BaseValidatorModel):
    securityConfigurations: List[SecurityConfiguration]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None



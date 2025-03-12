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

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CertificateTypeDef(BaseValidatorModel):
    certificateArn: Optional[str] = None
    certificateData: Optional[str] = None


class CloudWatchMonitoringConfigurationTypeDef(BaseValidatorModel):
    logGroupName: str
    logStreamNamePrefix: Optional[str] = None


class ConfigurationOutputTypeDef(BaseValidatorModel):
    classification: str
    properties: Optional[Dict[str, str]] = None
    configurations: Optional[List[Dict[str, Any]]] = None


class ConfigurationPaginatorTypeDef(BaseValidatorModel):
    classification: str
    properties: Optional[Dict[str, str]] = None
    configurations: Optional[List[Dict[str, Any]]] = None


class ConfigurationTypeDef(BaseValidatorModel):
    classification: str
    properties: Optional[Mapping[str, str]] = None
    configurations: Optional[Sequence[Mapping[str, Any]]] = None


class EksInfoTypeDef(BaseValidatorModel):
    namespace: Optional[str] = None


class ContainerLogRotationConfigurationTypeDef(BaseValidatorModel):
    rotationSize: str
    maxFilesToKeep: int


class CredentialsTypeDef(BaseValidatorModel):
    token: Optional[str] = None


class GetManagedEndpointSessionCredentialsRequestTypeDef(BaseValidatorModel):
    endpointIdentifier: str
    virtualClusterIdentifier: str
    executionRoleArn: str
    credentialType: str
    durationInSeconds: Optional[int] = None
    logContext: Optional[str] = None
    clientToken: Optional[str] = None


class TLSCertificateConfigurationTypeDef(BaseValidatorModel):
    certificateProviderType: Optional[Literal["PEM"]] = None
    publicCertificateSecretArn: Optional[str] = None
    privateCertificateSecretArn: Optional[str] = None


class SparkSqlJobDriverTypeDef(BaseValidatorModel):
    entryPoint: Optional[str] = None
    sparkSqlParameters: Optional[str] = None


class SparkSubmitJobDriverOutputTypeDef(BaseValidatorModel):
    entryPoint: str
    entryPointArguments: Optional[List[str]] = None
    sparkSubmitParameters: Optional[str] = None


class SparkSubmitJobDriverTypeDef(BaseValidatorModel):
    entryPoint: str
    entryPointArguments: Optional[Sequence[str]] = None
    sparkSubmitParameters: Optional[str] = None


class RetryPolicyConfigurationTypeDef(BaseValidatorModel):
    maxAttempts: int


class RetryPolicyExecutionTypeDef(BaseValidatorModel):
    currentAttemptCount: int


class SecureNamespaceInfoTypeDef(BaseValidatorModel):
    clusterId: Optional[str] = None
    namespace: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class ManagedLogsTypeDef(BaseValidatorModel):
    allowAWSToRetainLogs: Optional[AllowAWSToRetainLogsType] = None
    encryptionKeyArn: Optional[str] = None


class S3MonitoringConfigurationTypeDef(BaseValidatorModel):
    logUri: str


class ParametricCloudWatchMonitoringConfigurationTypeDef(BaseValidatorModel):
    logGroupName: Optional[str] = None
    logStreamNamePrefix: Optional[str] = None


class ParametricS3MonitoringConfigurationTypeDef(BaseValidatorModel):
    logUri: Optional[str] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class ContainerInfoTypeDef(BaseValidatorModel):
    eksInfo: Optional[EksInfoTypeDef] = None


class InTransitEncryptionConfigurationTypeDef(BaseValidatorModel):
    tlsCertificateConfiguration: Optional[TLSCertificateConfigurationTypeDef] = None


class JobDriverOutputTypeDef(BaseValidatorModel):
    sparkSubmitJobDriver: Optional[SparkSubmitJobDriverOutputTypeDef] = None
    sparkSqlJobDriver: Optional[SparkSqlJobDriverTypeDef] = None


class JobDriverTypeDef(BaseValidatorModel):
    sparkSubmitJobDriver: Optional[SparkSubmitJobDriverTypeDef] = None
    sparkSqlJobDriver: Optional[SparkSqlJobDriverTypeDef] = None


class LakeFormationConfigurationTypeDef(BaseValidatorModel):
    authorizedSessionTagValue: Optional[str] = None
    secureNamespaceInfo: Optional[SecureNamespaceInfoTypeDef] = None
    queryEngineRoleArn: Optional[str] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class ListJobRunsRequestPaginateTypeDef(BaseValidatorModel):
    virtualClusterId: str
    createdBefore: Optional[TimestampTypeDef] = None
    createdAfter: Optional[TimestampTypeDef] = None
    name: Optional[str] = None
    states: Optional[Sequence[JobRunStateType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListJobRunsRequestTypeDef(BaseValidatorModel):
    virtualClusterId: str
    createdBefore: Optional[TimestampTypeDef] = None
    createdAfter: Optional[TimestampTypeDef] = None
    name: Optional[str] = None
    states: Optional[Sequence[JobRunStateType]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListJobTemplatesRequestPaginateTypeDef(BaseValidatorModel):
    createdAfter: Optional[TimestampTypeDef] = None
    createdBefore: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListJobTemplatesRequestTypeDef(BaseValidatorModel):
    createdAfter: Optional[TimestampTypeDef] = None
    createdBefore: Optional[TimestampTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListSecurityConfigurationsRequestPaginateTypeDef(BaseValidatorModel):
    createdAfter: Optional[TimestampTypeDef] = None
    createdBefore: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSecurityConfigurationsRequestTypeDef(BaseValidatorModel):
    createdAfter: Optional[TimestampTypeDef] = None
    createdBefore: Optional[TimestampTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListVirtualClustersRequestPaginateTypeDef(BaseValidatorModel):
    containerProviderId: Optional[str] = None
    containerProviderType: Optional[Literal["EKS"]] = None
    createdAfter: Optional[TimestampTypeDef] = None
    createdBefore: Optional[TimestampTypeDef] = None
    states: Optional[Sequence[VirtualClusterStateType]] = None
    eksAccessEntryIntegrated: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListVirtualClustersRequestTypeDef(BaseValidatorModel):
    containerProviderId: Optional[str] = None
    containerProviderType: Optional[Literal["EKS"]] = None
    createdAfter: Optional[TimestampTypeDef] = None
    createdBefore: Optional[TimestampTypeDef] = None
    states: Optional[Sequence[VirtualClusterStateType]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    eksAccessEntryIntegrated: Optional[bool] = None


class MonitoringConfigurationTypeDef(BaseValidatorModel):
    managedLogs: Optional[ManagedLogsTypeDef] = None
    persistentAppUI: Optional[PersistentAppUIType] = None
    cloudWatchMonitoringConfiguration: Optional[CloudWatchMonitoringConfigurationTypeDef] = None
    s3MonitoringConfiguration: Optional[S3MonitoringConfigurationTypeDef] = None
    containerLogRotationConfiguration: Optional[ContainerLogRotationConfigurationTypeDef] = None


class ParametricMonitoringConfigurationTypeDef(BaseValidatorModel):
    persistentAppUI: Optional[str] = None
    cloudWatchMonitoringConfiguration: Optional[ ParametricCloudWatchMonitoringConfigurationTypeDef ] = None
    s3MonitoringConfiguration: Optional[ParametricS3MonitoringConfigurationTypeDef] = None


class EncryptionConfigurationTypeDef(BaseValidatorModel):
    inTransitEncryptionConfiguration: Optional[InTransitEncryptionConfigurationTypeDef] = None


class ConfigurationOverridesOutputTypeDef(BaseValidatorModel):
    applicationConfiguration: Optional[List[ConfigurationOutputTypeDef]] = None
    monitoringConfiguration: Optional[MonitoringConfigurationTypeDef] = None


class ConfigurationOverridesPaginatorTypeDef(BaseValidatorModel):
    applicationConfiguration: Optional[List[ConfigurationPaginatorTypeDef]] = None
    monitoringConfiguration: Optional[MonitoringConfigurationTypeDef] = None


class ConfigurationOverridesTypeDef(BaseValidatorModel):
    applicationConfiguration: Optional[Sequence[ConfigurationTypeDef]] = None
    monitoringConfiguration: Optional[MonitoringConfigurationTypeDef] = None


class ParametricConfigurationOverridesOutputTypeDef(BaseValidatorModel):
    applicationConfiguration: Optional[List[ConfigurationOutputTypeDef]] = None
    monitoringConfiguration: Optional[ParametricMonitoringConfigurationTypeDef] = None


class ParametricConfigurationOverridesPaginatorTypeDef(BaseValidatorModel):
    applicationConfiguration: Optional[List[ConfigurationPaginatorTypeDef]] = None
    monitoringConfiguration: Optional[ParametricMonitoringConfigurationTypeDef] = None


class ParametricConfigurationOverridesTypeDef(BaseValidatorModel):
    applicationConfiguration: Optional[Sequence[ConfigurationTypeDef]] = None
    monitoringConfiguration: Optional[ParametricMonitoringConfigurationTypeDef] = None


class ContainerProviderTypeDef(BaseValidatorModel):
    pass


class CreateVirtualClusterRequestTypeDef(BaseValidatorModel):
    name: str
    containerProvider: ContainerProviderTypeDef
    clientToken: str
    tags: Optional[Mapping[str, str]] = None
    securityConfigurationId: Optional[str] = None


class AuthorizationConfigurationTypeDef(BaseValidatorModel):
    lakeFormationConfiguration: Optional[LakeFormationConfigurationTypeDef] = None
    encryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None


class TemplateParameterConfigurationTypeDef(BaseValidatorModel):
    pass


class JobTemplateDataOutputTypeDef(BaseValidatorModel):
    executionRoleArn: str
    releaseLabel: str
    jobDriver: JobDriverOutputTypeDef
    configurationOverrides: Optional[ParametricConfigurationOverridesOutputTypeDef] = None
    parameterConfiguration: Optional[Dict[str, TemplateParameterConfigurationTypeDef]] = None
    jobTags: Optional[Dict[str, str]] = None


class JobTemplateDataPaginatorTypeDef(BaseValidatorModel):
    executionRoleArn: str
    releaseLabel: str
    jobDriver: JobDriverOutputTypeDef
    configurationOverrides: Optional[ParametricConfigurationOverridesPaginatorTypeDef] = None
    parameterConfiguration: Optional[Dict[str, TemplateParameterConfigurationTypeDef]] = None
    jobTags: Optional[Dict[str, str]] = None


class JobTemplateDataTypeDef(BaseValidatorModel):
    executionRoleArn: str
    releaseLabel: str
    jobDriver: JobDriverTypeDef
    configurationOverrides: Optional[ParametricConfigurationOverridesTypeDef] = None
    parameterConfiguration: Optional[Mapping[str, TemplateParameterConfigurationTypeDef]] = None
    jobTags: Optional[Mapping[str, str]] = None


class VirtualClusterTypeDef(BaseValidatorModel):
    pass


class DescribeVirtualClusterResponseTypeDef(BaseValidatorModel):
    virtualCluster: VirtualClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListVirtualClustersResponseTypeDef(BaseValidatorModel):
    virtualClusters: List[VirtualClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class SecurityConfigurationDataTypeDef(BaseValidatorModel):
    authorizationConfiguration: Optional[AuthorizationConfigurationTypeDef] = None


class EndpointTypeDef(BaseValidatorModel):
    pass


class DescribeManagedEndpointResponseTypeDef(BaseValidatorModel):
    endpoint: EndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListManagedEndpointsResponseTypeDef(BaseValidatorModel):
    endpoints: List[EndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class JobRunTypeDef(BaseValidatorModel):
    pass


class DescribeJobRunResponseTypeDef(BaseValidatorModel):
    jobRun: JobRunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListJobRunsResponseTypeDef(BaseValidatorModel):
    jobRuns: List[JobRunTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class EndpointPaginatorTypeDef(BaseValidatorModel):
    pass


class ListManagedEndpointsResponsePaginatorTypeDef(BaseValidatorModel):
    endpoints: List[EndpointPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class JobRunPaginatorTypeDef(BaseValidatorModel):
    pass


class ListJobRunsResponsePaginatorTypeDef(BaseValidatorModel):
    jobRuns: List[JobRunPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class JobDriverUnionTypeDef(BaseValidatorModel):
    pass


class ConfigurationOverridesUnionTypeDef(BaseValidatorModel):
    pass


class StartJobRunRequestTypeDef(BaseValidatorModel):
    virtualClusterId: str
    clientToken: str
    name: Optional[str] = None
    executionRoleArn: Optional[str] = None
    releaseLabel: Optional[str] = None
    jobDriver: Optional[JobDriverUnionTypeDef] = None
    configurationOverrides: Optional[ConfigurationOverridesUnionTypeDef] = None
    tags: Optional[Mapping[str, str]] = None
    jobTemplateId: Optional[str] = None
    jobTemplateParameters: Optional[Mapping[str, str]] = None
    retryPolicyConfiguration: Optional[RetryPolicyConfigurationTypeDef] = None


class CreateSecurityConfigurationRequestTypeDef(BaseValidatorModel):
    clientToken: str
    name: str
    securityConfigurationData: SecurityConfigurationDataTypeDef
    tags: Optional[Mapping[str, str]] = None


class JobTemplateTypeDef(BaseValidatorModel):
    pass


class DescribeJobTemplateResponseTypeDef(BaseValidatorModel):
    jobTemplate: JobTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListJobTemplatesResponseTypeDef(BaseValidatorModel):
    templates: List[JobTemplateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class JobTemplatePaginatorTypeDef(BaseValidatorModel):
    pass


class ListJobTemplatesResponsePaginatorTypeDef(BaseValidatorModel):
    templates: List[JobTemplatePaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class JobTemplateDataUnionTypeDef(BaseValidatorModel):
    pass


class CreateJobTemplateRequestTypeDef(BaseValidatorModel):
    name: str
    clientToken: str
    jobTemplateData: JobTemplateDataUnionTypeDef
    tags: Optional[Mapping[str, str]] = None
    kmsKeyArn: Optional[str] = None


class SecurityConfigurationTypeDef(BaseValidatorModel):
    pass


class DescribeSecurityConfigurationResponseTypeDef(BaseValidatorModel):
    securityConfiguration: SecurityConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListSecurityConfigurationsResponseTypeDef(BaseValidatorModel):
    securityConfigurations: List[SecurityConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None



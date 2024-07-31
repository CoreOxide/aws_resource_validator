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
from aws_resource_validator.pydantic_models.emr_containers_constants import *

class CancelJobRunRequestRequestTypeDef(BaseModel):
    id: str
    virtualClusterId: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CertificateTypeDef(BaseModel):
    certificateArn: Optional[str] = None
    certificateData: Optional[str] = None

class CloudWatchMonitoringConfigurationTypeDef(BaseModel):
    logGroupName: str
    logStreamNamePrefix: Optional[str] = None

class ConfigurationPaginatorTypeDef(BaseModel):
    classification: str
    properties: Optional[Dict[str, str]] = None
    configurations: Optional[List[Dict[str, Any]]] = None

class ConfigurationTypeDef(BaseModel):
    classification: str
    properties: Optional[Mapping[str, str]] = None
    configurations: Optional[Sequence[Dict[str, Any]]] = None

class EksInfoTypeDef(BaseModel):
    namespace: Optional[str] = None

class ContainerLogRotationConfigurationTypeDef(BaseModel):
    rotationSize: str
    maxFilesToKeep: int

class CredentialsTypeDef(BaseModel):
    token: Optional[str] = None

class DeleteJobTemplateRequestRequestTypeDef(BaseModel):
    id: str

class DeleteManagedEndpointRequestRequestTypeDef(BaseModel):
    id: str
    virtualClusterId: str

class DeleteVirtualClusterRequestRequestTypeDef(BaseModel):
    id: str

class DescribeJobRunRequestRequestTypeDef(BaseModel):
    id: str
    virtualClusterId: str

class DescribeJobTemplateRequestRequestTypeDef(BaseModel):
    id: str

class DescribeManagedEndpointRequestRequestTypeDef(BaseModel):
    id: str
    virtualClusterId: str

class DescribeSecurityConfigurationRequestRequestTypeDef(BaseModel):
    id: str

class DescribeVirtualClusterRequestRequestTypeDef(BaseModel):
    id: str

class GetManagedEndpointSessionCredentialsRequestRequestTypeDef(BaseModel):
    endpointIdentifier: str
    virtualClusterIdentifier: str
    executionRoleArn: str
    credentialType: str
    durationInSeconds: Optional[int] = None
    logContext: Optional[str] = None
    clientToken: Optional[str] = None

class TLSCertificateConfigurationTypeDef(BaseModel):
    certificateProviderType: Optional[Literal["PEM"]] = None
    publicCertificateSecretArn: Optional[str] = None
    privateCertificateSecretArn: Optional[str] = None

class SparkSqlJobDriverTypeDef(BaseModel):
    entryPoint: Optional[str] = None
    sparkSqlParameters: Optional[str] = None

class SparkSubmitJobDriverPaginatorTypeDef(BaseModel):
    entryPoint: str
    entryPointArguments: Optional[List[str]] = None
    sparkSubmitParameters: Optional[str] = None

class SparkSubmitJobDriverTypeDef(BaseModel):
    entryPoint: str
    entryPointArguments: Optional[Sequence[str]] = None
    sparkSubmitParameters: Optional[str] = None

class RetryPolicyConfigurationTypeDef(BaseModel):
    maxAttempts: int

class RetryPolicyExecutionTypeDef(BaseModel):
    currentAttemptCount: int

class TemplateParameterConfigurationTypeDef(BaseModel):
    type: Optional[TemplateParameterDataTypeType] = None
    defaultValue: Optional[str] = None

class SecureNamespaceInfoTypeDef(BaseModel):
    clusterId: Optional[str] = None
    namespace: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class S3MonitoringConfigurationTypeDef(BaseModel):
    logUri: str

class ParametricCloudWatchMonitoringConfigurationTypeDef(BaseModel):
    logGroupName: Optional[str] = None
    logStreamNamePrefix: Optional[str] = None

class ParametricS3MonitoringConfigurationTypeDef(BaseModel):
    logUri: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class CancelJobRunResponseTypeDef(BaseModel):
    id: str
    virtualClusterId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateJobTemplateResponseTypeDef(BaseModel):
    id: str
    name: str
    arn: str
    createdAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateManagedEndpointResponseTypeDef(BaseModel):
    id: str
    name: str
    arn: str
    virtualClusterId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSecurityConfigurationResponseTypeDef(BaseModel):
    id: str
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVirtualClusterResponseTypeDef(BaseModel):
    id: str
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteJobTemplateResponseTypeDef(BaseModel):
    id: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteManagedEndpointResponseTypeDef(BaseModel):
    id: str
    virtualClusterId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVirtualClusterResponseTypeDef(BaseModel):
    id: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartJobRunResponseTypeDef(BaseModel):
    id: str
    name: str
    arn: str
    virtualClusterId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ContainerInfoTypeDef(BaseModel):
    eksInfo: Optional[EksInfoTypeDef] = None

class GetManagedEndpointSessionCredentialsResponseTypeDef(BaseModel):
    id: str
    credentials: CredentialsTypeDef
    expiresAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class InTransitEncryptionConfigurationTypeDef(BaseModel):
    tlsCertificateConfiguration: Optional[TLSCertificateConfigurationTypeDef] = None

class JobDriverPaginatorTypeDef(BaseModel):
    sparkSubmitJobDriver: Optional[SparkSubmitJobDriverPaginatorTypeDef] = None
    sparkSqlJobDriver: Optional[SparkSqlJobDriverTypeDef] = None

class JobDriverTypeDef(BaseModel):
    sparkSubmitJobDriver: Optional[SparkSubmitJobDriverTypeDef] = None
    sparkSqlJobDriver: Optional[SparkSqlJobDriverTypeDef] = None

class LakeFormationConfigurationTypeDef(BaseModel):
    authorizedSessionTagValue: Optional[str] = None
    secureNamespaceInfo: Optional[SecureNamespaceInfoTypeDef] = None
    queryEngineRoleArn: Optional[str] = None

class ListJobRunsRequestListJobRunsPaginateTypeDef(BaseModel):
    virtualClusterId: str
    createdBefore: Optional[TimestampTypeDef] = None
    createdAfter: Optional[TimestampTypeDef] = None
    name: Optional[str] = None
    states: Optional[Sequence[JobRunStateType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobRunsRequestRequestTypeDef(BaseModel):
    virtualClusterId: str
    createdBefore: Optional[TimestampTypeDef] = None
    createdAfter: Optional[TimestampTypeDef] = None
    name: Optional[str] = None
    states: Optional[Sequence[JobRunStateType]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListJobTemplatesRequestListJobTemplatesPaginateTypeDef(BaseModel):
    createdAfter: Optional[TimestampTypeDef] = None
    createdBefore: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobTemplatesRequestRequestTypeDef(BaseModel):
    createdAfter: Optional[TimestampTypeDef] = None
    createdBefore: Optional[TimestampTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListManagedEndpointsRequestListManagedEndpointsPaginateTypeDef(BaseModel):
    virtualClusterId: str
    createdBefore: Optional[TimestampTypeDef] = None
    createdAfter: Optional[TimestampTypeDef] = None
    types: Optional[Sequence[str]] = None
    states: Optional[Sequence[EndpointStateType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListManagedEndpointsRequestRequestTypeDef(BaseModel):
    virtualClusterId: str
    createdBefore: Optional[TimestampTypeDef] = None
    createdAfter: Optional[TimestampTypeDef] = None
    types: Optional[Sequence[str]] = None
    states: Optional[Sequence[EndpointStateType]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListSecurityConfigurationsRequestListSecurityConfigurationsPaginateTypeDef(BaseModel):
    createdAfter: Optional[TimestampTypeDef] = None
    createdBefore: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSecurityConfigurationsRequestRequestTypeDef(BaseModel):
    createdAfter: Optional[TimestampTypeDef] = None
    createdBefore: Optional[TimestampTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListVirtualClustersRequestListVirtualClustersPaginateTypeDef(BaseModel):
    containerProviderId: Optional[str] = None
    containerProviderType: Optional[Literal["EKS"]] = None
    createdAfter: Optional[TimestampTypeDef] = None
    createdBefore: Optional[TimestampTypeDef] = None
    states: Optional[Sequence[VirtualClusterStateType]] = None
    eksAccessEntryIntegrated: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVirtualClustersRequestRequestTypeDef(BaseModel):
    containerProviderId: Optional[str] = None
    containerProviderType: Optional[Literal["EKS"]] = None
    createdAfter: Optional[TimestampTypeDef] = None
    createdBefore: Optional[TimestampTypeDef] = None
    states: Optional[Sequence[VirtualClusterStateType]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    eksAccessEntryIntegrated: Optional[bool] = None

class MonitoringConfigurationTypeDef(BaseModel):
    persistentAppUI: Optional[PersistentAppUIType] = None
    cloudWatchMonitoringConfiguration: Optional[CloudWatchMonitoringConfigurationTypeDef] = None
    s3MonitoringConfiguration: Optional[S3MonitoringConfigurationTypeDef] = None
    containerLogRotationConfiguration: Optional[ContainerLogRotationConfigurationTypeDef] = None

class ParametricMonitoringConfigurationTypeDef(BaseModel):
    persistentAppUI: Optional[str] = None
    cloudWatchMonitoringConfiguration: Optional[       ParametricCloudWatchMonitoringConfigurationTypeDef     ] = None
    s3MonitoringConfiguration: Optional[ParametricS3MonitoringConfigurationTypeDef] = None

class ContainerProviderTypeDef(BaseModel):
    type: Literal["EKS"]
    id: str
    info: Optional[ContainerInfoTypeDef] = None

class EncryptionConfigurationTypeDef(BaseModel):
    inTransitEncryptionConfiguration: Optional[InTransitEncryptionConfigurationTypeDef] = None

class ConfigurationOverridesPaginatorTypeDef(BaseModel):
    applicationConfiguration: Optional[List["ConfigurationPaginatorTypeDef"]] = None
    monitoringConfiguration: Optional[MonitoringConfigurationTypeDef] = None

class ConfigurationOverridesTypeDef(BaseModel):
    applicationConfiguration: Optional[Sequence["ConfigurationTypeDef"]] = None
    monitoringConfiguration: Optional[MonitoringConfigurationTypeDef] = None

class ParametricConfigurationOverridesPaginatorTypeDef(BaseModel):
    applicationConfiguration: Optional[List["ConfigurationPaginatorTypeDef"]] = None
    monitoringConfiguration: Optional[ParametricMonitoringConfigurationTypeDef] = None

class ParametricConfigurationOverridesTypeDef(BaseModel):
    applicationConfiguration: Optional[Sequence["ConfigurationTypeDef"]] = None
    monitoringConfiguration: Optional[ParametricMonitoringConfigurationTypeDef] = None

class CreateVirtualClusterRequestRequestTypeDef(BaseModel):
    name: str
    containerProvider: ContainerProviderTypeDef
    clientToken: str
    tags: Optional[Mapping[str, str]] = None
    securityConfigurationId: Optional[str] = None

class VirtualClusterTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    arn: Optional[str] = None
    state: Optional[VirtualClusterStateType] = None
    containerProvider: Optional[ContainerProviderTypeDef] = None
    createdAt: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None
    securityConfigurationId: Optional[str] = None

class AuthorizationConfigurationTypeDef(BaseModel):
    lakeFormationConfiguration: Optional[LakeFormationConfigurationTypeDef] = None
    encryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None

class EndpointPaginatorTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    arn: Optional[str] = None
    virtualClusterId: Optional[str] = None
    type: Optional[str] = None
    state: Optional[EndpointStateType] = None
    releaseLabel: Optional[str] = None
    executionRoleArn: Optional[str] = None
    certificateArn: Optional[str] = None
    certificateAuthority: Optional[CertificateTypeDef] = None
    configurationOverrides: Optional[ConfigurationOverridesPaginatorTypeDef] = None
    serverUrl: Optional[str] = None
    createdAt: Optional[datetime] = None
    securityGroup: Optional[str] = None
    subnetIds: Optional[List[str]] = None
    stateDetails: Optional[str] = None
    failureReason: Optional[FailureReasonType] = None
    tags: Optional[Dict[str, str]] = None

class JobRunPaginatorTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    virtualClusterId: Optional[str] = None
    arn: Optional[str] = None
    state: Optional[JobRunStateType] = None
    clientToken: Optional[str] = None
    executionRoleArn: Optional[str] = None
    releaseLabel: Optional[str] = None
    configurationOverrides: Optional[ConfigurationOverridesPaginatorTypeDef] = None
    jobDriver: Optional[JobDriverPaginatorTypeDef] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    finishedAt: Optional[datetime] = None
    stateDetails: Optional[str] = None
    failureReason: Optional[FailureReasonType] = None
    tags: Optional[Dict[str, str]] = None
    retryPolicyConfiguration: Optional[RetryPolicyConfigurationTypeDef] = None
    retryPolicyExecution: Optional[RetryPolicyExecutionTypeDef] = None

class CreateManagedEndpointRequestRequestTypeDef(BaseModel):
    name: str
    virtualClusterId: str
    type: str
    releaseLabel: str
    executionRoleArn: str
    clientToken: str
    certificateArn: Optional[str] = None
    configurationOverrides: Optional[ConfigurationOverridesTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class EndpointTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    arn: Optional[str] = None
    virtualClusterId: Optional[str] = None
    type: Optional[str] = None
    state: Optional[EndpointStateType] = None
    releaseLabel: Optional[str] = None
    executionRoleArn: Optional[str] = None
    certificateArn: Optional[str] = None
    certificateAuthority: Optional[CertificateTypeDef] = None
    configurationOverrides: Optional[ConfigurationOverridesTypeDef] = None
    serverUrl: Optional[str] = None
    createdAt: Optional[datetime] = None
    securityGroup: Optional[str] = None
    subnetIds: Optional[List[str]] = None
    stateDetails: Optional[str] = None
    failureReason: Optional[FailureReasonType] = None
    tags: Optional[Dict[str, str]] = None

class JobRunTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    virtualClusterId: Optional[str] = None
    arn: Optional[str] = None
    state: Optional[JobRunStateType] = None
    clientToken: Optional[str] = None
    executionRoleArn: Optional[str] = None
    releaseLabel: Optional[str] = None
    configurationOverrides: Optional[ConfigurationOverridesTypeDef] = None
    jobDriver: Optional[JobDriverTypeDef] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    finishedAt: Optional[datetime] = None
    stateDetails: Optional[str] = None
    failureReason: Optional[FailureReasonType] = None
    tags: Optional[Dict[str, str]] = None
    retryPolicyConfiguration: Optional[RetryPolicyConfigurationTypeDef] = None
    retryPolicyExecution: Optional[RetryPolicyExecutionTypeDef] = None

class StartJobRunRequestRequestTypeDef(BaseModel):
    virtualClusterId: str
    clientToken: str
    name: Optional[str] = None
    executionRoleArn: Optional[str] = None
    releaseLabel: Optional[str] = None
    jobDriver: Optional[JobDriverTypeDef] = None
    configurationOverrides: Optional[ConfigurationOverridesTypeDef] = None
    tags: Optional[Mapping[str, str]] = None
    jobTemplateId: Optional[str] = None
    jobTemplateParameters: Optional[Mapping[str, str]] = None
    retryPolicyConfiguration: Optional[RetryPolicyConfigurationTypeDef] = None

class JobTemplateDataPaginatorTypeDef(BaseModel):
    executionRoleArn: str
    releaseLabel: str
    jobDriver: JobDriverPaginatorTypeDef
    configurationOverrides: Optional[ParametricConfigurationOverridesPaginatorTypeDef] = None
    parameterConfiguration: Optional[Dict[str, TemplateParameterConfigurationTypeDef]] = None
    jobTags: Optional[Dict[str, str]] = None

class JobTemplateDataTypeDef(BaseModel):
    executionRoleArn: str
    releaseLabel: str
    jobDriver: JobDriverTypeDef
    configurationOverrides: Optional[ParametricConfigurationOverridesTypeDef] = None
    parameterConfiguration: Optional[Mapping[str, TemplateParameterConfigurationTypeDef]] = None
    jobTags: Optional[Mapping[str, str]] = None

class DescribeVirtualClusterResponseTypeDef(BaseModel):
    virtualCluster: VirtualClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListVirtualClustersResponseTypeDef(BaseModel):
    virtualClusters: List[VirtualClusterTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SecurityConfigurationDataTypeDef(BaseModel):
    authorizationConfiguration: Optional[AuthorizationConfigurationTypeDef] = None

class ListManagedEndpointsResponsePaginatorTypeDef(BaseModel):
    endpoints: List[EndpointPaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListJobRunsResponsePaginatorTypeDef(BaseModel):
    jobRuns: List[JobRunPaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeManagedEndpointResponseTypeDef(BaseModel):
    endpoint: EndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListManagedEndpointsResponseTypeDef(BaseModel):
    endpoints: List[EndpointTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeJobRunResponseTypeDef(BaseModel):
    jobRun: JobRunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListJobRunsResponseTypeDef(BaseModel):
    jobRuns: List[JobRunTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class JobTemplatePaginatorTypeDef(BaseModel):
    jobTemplateData: JobTemplateDataPaginatorTypeDef
    name: Optional[str] = None
    id: Optional[str] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    kmsKeyArn: Optional[str] = None
    decryptionError: Optional[str] = None

class CreateJobTemplateRequestRequestTypeDef(BaseModel):
    name: str
    clientToken: str
    jobTemplateData: JobTemplateDataTypeDef
    tags: Optional[Mapping[str, str]] = None
    kmsKeyArn: Optional[str] = None

class JobTemplateTypeDef(BaseModel):
    jobTemplateData: JobTemplateDataTypeDef
    name: Optional[str] = None
    id: Optional[str] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    kmsKeyArn: Optional[str] = None
    decryptionError: Optional[str] = None

class CreateSecurityConfigurationRequestRequestTypeDef(BaseModel):
    clientToken: str
    name: str
    securityConfigurationData: SecurityConfigurationDataTypeDef
    tags: Optional[Mapping[str, str]] = None

class SecurityConfigurationTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    securityConfigurationData: Optional[SecurityConfigurationDataTypeDef] = None
    tags: Optional[Dict[str, str]] = None

class ListJobTemplatesResponsePaginatorTypeDef(BaseModel):
    templates: List[JobTemplatePaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeJobTemplateResponseTypeDef(BaseModel):
    jobTemplate: JobTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListJobTemplatesResponseTypeDef(BaseModel):
    templates: List[JobTemplateTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSecurityConfigurationResponseTypeDef(BaseModel):
    securityConfiguration: SecurityConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSecurityConfigurationsResponseTypeDef(BaseModel):
    securityConfigurations: List[SecurityConfigurationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef


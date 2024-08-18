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
from aws_resource_validator.pydantic_models.emr_containers_constants import *

class CancelJobRunRequestRequestTypeDef(BaseValidatorModel):
    id: str
    virtualClusterId: str

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

class ConfigurationPaginatorTypeDef(BaseValidatorModel):
    classification: str
    properties: Optional[Dict[str, str]] = None
    configurations: Optional[List[Dict[str, Any]]] = None

class ConfigurationTypeDef(BaseValidatorModel):
    classification: str
    properties: Optional[Mapping[str, str]] = None
    configurations: Optional[Sequence[Dict[str, Any]]] = None

class EksInfoTypeDef(BaseValidatorModel):
    namespace: Optional[str] = None

class ContainerLogRotationConfigurationTypeDef(BaseValidatorModel):
    rotationSize: str
    maxFilesToKeep: int

class CredentialsTypeDef(BaseValidatorModel):
    token: Optional[str] = None

class DeleteJobTemplateRequestRequestTypeDef(BaseValidatorModel):
    id: str

class DeleteManagedEndpointRequestRequestTypeDef(BaseValidatorModel):
    id: str
    virtualClusterId: str

class DeleteVirtualClusterRequestRequestTypeDef(BaseValidatorModel):
    id: str

class DescribeJobRunRequestRequestTypeDef(BaseValidatorModel):
    id: str
    virtualClusterId: str

class DescribeJobTemplateRequestRequestTypeDef(BaseValidatorModel):
    id: str

class DescribeManagedEndpointRequestRequestTypeDef(BaseValidatorModel):
    id: str
    virtualClusterId: str

class DescribeSecurityConfigurationRequestRequestTypeDef(BaseValidatorModel):
    id: str

class DescribeVirtualClusterRequestRequestTypeDef(BaseValidatorModel):
    id: str

class GetManagedEndpointSessionCredentialsRequestRequestTypeDef(BaseValidatorModel):
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

class SparkSubmitJobDriverPaginatorTypeDef(BaseValidatorModel):
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

class TemplateParameterConfigurationTypeDef(BaseValidatorModel):
    type: Optional[TemplateParameterDataTypeType] = None
    defaultValue: Optional[str] = None

class SecureNamespaceInfoTypeDef(BaseValidatorModel):
    clusterId: Optional[str] = None
    namespace: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class S3MonitoringConfigurationTypeDef(BaseValidatorModel):
    logUri: str

class ParametricCloudWatchMonitoringConfigurationTypeDef(BaseValidatorModel):
    logGroupName: Optional[str] = None
    logStreamNamePrefix: Optional[str] = None

class ParametricS3MonitoringConfigurationTypeDef(BaseValidatorModel):
    logUri: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class CancelJobRunResponseTypeDef(BaseValidatorModel):
    id: str
    virtualClusterId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateJobTemplateResponseTypeDef(BaseValidatorModel):
    id: str
    name: str
    arn: str
    createdAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateManagedEndpointResponseTypeDef(BaseValidatorModel):
    id: str
    name: str
    arn: str
    virtualClusterId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSecurityConfigurationResponseTypeDef(BaseValidatorModel):
    id: str
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVirtualClusterResponseTypeDef(BaseValidatorModel):
    id: str
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteJobTemplateResponseTypeDef(BaseValidatorModel):
    id: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteManagedEndpointResponseTypeDef(BaseValidatorModel):
    id: str
    virtualClusterId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVirtualClusterResponseTypeDef(BaseValidatorModel):
    id: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartJobRunResponseTypeDef(BaseValidatorModel):
    id: str
    name: str
    arn: str
    virtualClusterId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ContainerInfoTypeDef(BaseValidatorModel):
    eksInfo: Optional[EksInfoTypeDef] = None

class GetManagedEndpointSessionCredentialsResponseTypeDef(BaseValidatorModel):
    id: str
    credentials: CredentialsTypeDef
    expiresAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class InTransitEncryptionConfigurationTypeDef(BaseValidatorModel):
    tlsCertificateConfiguration: Optional[TLSCertificateConfigurationTypeDef] = None

class JobDriverPaginatorTypeDef(BaseValidatorModel):
    sparkSubmitJobDriver: Optional[SparkSubmitJobDriverPaginatorTypeDef] = None
    sparkSqlJobDriver: Optional[SparkSqlJobDriverTypeDef] = None

class JobDriverTypeDef(BaseValidatorModel):
    sparkSubmitJobDriver: Optional[SparkSubmitJobDriverTypeDef] = None
    sparkSqlJobDriver: Optional[SparkSqlJobDriverTypeDef] = None

class LakeFormationConfigurationTypeDef(BaseValidatorModel):
    authorizedSessionTagValue: Optional[str] = None
    secureNamespaceInfo: Optional[SecureNamespaceInfoTypeDef] = None
    queryEngineRoleArn: Optional[str] = None

class ListJobRunsRequestListJobRunsPaginateTypeDef(BaseValidatorModel):
    virtualClusterId: str
    createdBefore: Optional[TimestampTypeDef] = None
    createdAfter: Optional[TimestampTypeDef] = None
    name: Optional[str] = None
    states: Optional[Sequence[JobRunStateType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobRunsRequestRequestTypeDef(BaseValidatorModel):
    virtualClusterId: str
    createdBefore: Optional[TimestampTypeDef] = None
    createdAfter: Optional[TimestampTypeDef] = None
    name: Optional[str] = None
    states: Optional[Sequence[JobRunStateType]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListJobTemplatesRequestListJobTemplatesPaginateTypeDef(BaseValidatorModel):
    createdAfter: Optional[TimestampTypeDef] = None
    createdBefore: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobTemplatesRequestRequestTypeDef(BaseValidatorModel):
    createdAfter: Optional[TimestampTypeDef] = None
    createdBefore: Optional[TimestampTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListManagedEndpointsRequestListManagedEndpointsPaginateTypeDef(BaseValidatorModel):
    virtualClusterId: str
    createdBefore: Optional[TimestampTypeDef] = None
    createdAfter: Optional[TimestampTypeDef] = None
    types: Optional[Sequence[str]] = None
    states: Optional[Sequence[EndpointStateType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListManagedEndpointsRequestRequestTypeDef(BaseValidatorModel):
    virtualClusterId: str
    createdBefore: Optional[TimestampTypeDef] = None
    createdAfter: Optional[TimestampTypeDef] = None
    types: Optional[Sequence[str]] = None
    states: Optional[Sequence[EndpointStateType]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListSecurityConfigurationsRequestListSecurityConfigurationsPaginateTypeDef(BaseValidatorModel):
    createdAfter: Optional[TimestampTypeDef] = None
    createdBefore: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSecurityConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    createdAfter: Optional[TimestampTypeDef] = None
    createdBefore: Optional[TimestampTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListVirtualClustersRequestListVirtualClustersPaginateTypeDef(BaseValidatorModel):
    containerProviderId: Optional[str] = None
    containerProviderType: Optional[Literal["EKS"]] = None
    createdAfter: Optional[TimestampTypeDef] = None
    createdBefore: Optional[TimestampTypeDef] = None
    states: Optional[Sequence[VirtualClusterStateType]] = None
    eksAccessEntryIntegrated: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVirtualClustersRequestRequestTypeDef(BaseValidatorModel):
    containerProviderId: Optional[str] = None
    containerProviderType: Optional[Literal["EKS"]] = None
    createdAfter: Optional[TimestampTypeDef] = None
    createdBefore: Optional[TimestampTypeDef] = None
    states: Optional[Sequence[VirtualClusterStateType]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    eksAccessEntryIntegrated: Optional[bool] = None

class MonitoringConfigurationTypeDef(BaseValidatorModel):
    persistentAppUI: Optional[PersistentAppUIType] = None
    cloudWatchMonitoringConfiguration: Optional[CloudWatchMonitoringConfigurationTypeDef] = None
    s3MonitoringConfiguration: Optional[S3MonitoringConfigurationTypeDef] = None
    containerLogRotationConfiguration: Optional[ContainerLogRotationConfigurationTypeDef] = None

class ParametricMonitoringConfigurationTypeDef(BaseValidatorModel):
    persistentAppUI: Optional[str] = None
    cloudWatchMonitoringConfiguration: Optional[       ParametricCloudWatchMonitoringConfigurationTypeDef     ] = None
    s3MonitoringConfiguration: Optional[ParametricS3MonitoringConfigurationTypeDef] = None

class ContainerProviderTypeDef(BaseValidatorModel):
    type: Literal["EKS"]
    id: str
    info: Optional[ContainerInfoTypeDef] = None

class EncryptionConfigurationTypeDef(BaseValidatorModel):
    inTransitEncryptionConfiguration: Optional[InTransitEncryptionConfigurationTypeDef] = None

class ConfigurationOverridesPaginatorTypeDef(BaseValidatorModel):
    applicationConfiguration: Optional[List["ConfigurationPaginatorTypeDef"]] = None
    monitoringConfiguration: Optional[MonitoringConfigurationTypeDef] = None

class ConfigurationOverridesTypeDef(BaseValidatorModel):
    applicationConfiguration: Optional[Sequence["ConfigurationTypeDef"]] = None
    monitoringConfiguration: Optional[MonitoringConfigurationTypeDef] = None

class ParametricConfigurationOverridesPaginatorTypeDef(BaseValidatorModel):
    applicationConfiguration: Optional[List["ConfigurationPaginatorTypeDef"]] = None
    monitoringConfiguration: Optional[ParametricMonitoringConfigurationTypeDef] = None

class ParametricConfigurationOverridesTypeDef(BaseValidatorModel):
    applicationConfiguration: Optional[Sequence["ConfigurationTypeDef"]] = None
    monitoringConfiguration: Optional[ParametricMonitoringConfigurationTypeDef] = None

class CreateVirtualClusterRequestRequestTypeDef(BaseValidatorModel):
    name: str
    containerProvider: ContainerProviderTypeDef
    clientToken: str
    tags: Optional[Mapping[str, str]] = None
    securityConfigurationId: Optional[str] = None

class VirtualClusterTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    arn: Optional[str] = None
    state: Optional[VirtualClusterStateType] = None
    containerProvider: Optional[ContainerProviderTypeDef] = None
    createdAt: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None
    securityConfigurationId: Optional[str] = None

class AuthorizationConfigurationTypeDef(BaseValidatorModel):
    lakeFormationConfiguration: Optional[LakeFormationConfigurationTypeDef] = None
    encryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None

class EndpointPaginatorTypeDef(BaseValidatorModel):
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

class JobRunPaginatorTypeDef(BaseValidatorModel):
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

class CreateManagedEndpointRequestRequestTypeDef(BaseValidatorModel):
    name: str
    virtualClusterId: str
    type: str
    releaseLabel: str
    executionRoleArn: str
    clientToken: str
    certificateArn: Optional[str] = None
    configurationOverrides: Optional[ConfigurationOverridesTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class EndpointTypeDef(BaseValidatorModel):
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

class JobRunTypeDef(BaseValidatorModel):
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

class StartJobRunRequestRequestTypeDef(BaseValidatorModel):
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

class JobTemplateDataPaginatorTypeDef(BaseValidatorModel):
    executionRoleArn: str
    releaseLabel: str
    jobDriver: JobDriverPaginatorTypeDef
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

class DescribeVirtualClusterResponseTypeDef(BaseValidatorModel):
    virtualCluster: VirtualClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListVirtualClustersResponseTypeDef(BaseValidatorModel):
    virtualClusters: List[VirtualClusterTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SecurityConfigurationDataTypeDef(BaseValidatorModel):
    authorizationConfiguration: Optional[AuthorizationConfigurationTypeDef] = None

class ListManagedEndpointsResponsePaginatorTypeDef(BaseValidatorModel):
    endpoints: List[EndpointPaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListJobRunsResponsePaginatorTypeDef(BaseValidatorModel):
    jobRuns: List[JobRunPaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeManagedEndpointResponseTypeDef(BaseValidatorModel):
    endpoint: EndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListManagedEndpointsResponseTypeDef(BaseValidatorModel):
    endpoints: List[EndpointTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeJobRunResponseTypeDef(BaseValidatorModel):
    jobRun: JobRunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListJobRunsResponseTypeDef(BaseValidatorModel):
    jobRuns: List[JobRunTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class JobTemplatePaginatorTypeDef(BaseValidatorModel):
    jobTemplateData: JobTemplateDataPaginatorTypeDef
    name: Optional[str] = None
    id: Optional[str] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    kmsKeyArn: Optional[str] = None
    decryptionError: Optional[str] = None

class CreateJobTemplateRequestRequestTypeDef(BaseValidatorModel):
    name: str
    clientToken: str
    jobTemplateData: JobTemplateDataTypeDef
    tags: Optional[Mapping[str, str]] = None
    kmsKeyArn: Optional[str] = None

class JobTemplateTypeDef(BaseValidatorModel):
    jobTemplateData: JobTemplateDataTypeDef
    name: Optional[str] = None
    id: Optional[str] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    kmsKeyArn: Optional[str] = None
    decryptionError: Optional[str] = None

class CreateSecurityConfigurationRequestRequestTypeDef(BaseValidatorModel):
    clientToken: str
    name: str
    securityConfigurationData: SecurityConfigurationDataTypeDef
    tags: Optional[Mapping[str, str]] = None

class SecurityConfigurationTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    securityConfigurationData: Optional[SecurityConfigurationDataTypeDef] = None
    tags: Optional[Dict[str, str]] = None

class ListJobTemplatesResponsePaginatorTypeDef(BaseValidatorModel):
    templates: List[JobTemplatePaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeJobTemplateResponseTypeDef(BaseValidatorModel):
    jobTemplate: JobTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListJobTemplatesResponseTypeDef(BaseValidatorModel):
    templates: List[JobTemplateTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSecurityConfigurationResponseTypeDef(BaseValidatorModel):
    securityConfiguration: SecurityConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSecurityConfigurationsResponseTypeDef(BaseValidatorModel):
    securityConfigurations: List[SecurityConfigurationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef


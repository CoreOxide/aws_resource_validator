from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.amplify.amplify_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AutoBranchCreationConfigOutput(BaseValidatorModel):
    stage: Optional[StageType] = None
    framework: Optional[str] = None
    enableAutoBuild: Optional[bool] = None
    environmentVariables: Optional[Dict[str, str]] = None
    basicAuthCredentials: Optional[str] = None
    enableBasicAuth: Optional[bool] = None
    enablePerformanceMode: Optional[bool] = None
    buildSpec: Optional[str] = None
    enablePullRequestPreview: Optional[bool] = None
    pullRequestEnvironmentName: Optional[str] = None


class CacheConfig(BaseValidatorModel):
    type: CacheConfigTypeType


class CustomRule(BaseValidatorModel):
    source: str
    target: str
    status: Optional[str] = None
    condition: Optional[str] = None


class ProductionBranch(BaseValidatorModel):
    lastDeployTime: Optional[datetime] = None
    status: Optional[str] = None
    thumbnailUrl: Optional[str] = None
    branchName: Optional[str] = None


class WafConfiguration(BaseValidatorModel):
    webAclArn: Optional[str] = None
    wafStatus: Optional[WafStatusType] = None
    statusReason: Optional[str] = None


class Artifact(BaseValidatorModel):
    artifactFileName: str
    artifactId: str


class AutoBranchCreationConfig(BaseValidatorModel):
    stage: Optional[StageType] = None
    framework: Optional[str] = None
    enableAutoBuild: Optional[bool] = None
    environmentVariables: Optional[Dict[str, str]] = None
    basicAuthCredentials: Optional[str] = None
    enableBasicAuth: Optional[bool] = None
    enablePerformanceMode: Optional[bool] = None
    buildSpec: Optional[str] = None
    enablePullRequestPreview: Optional[bool] = None
    pullRequestEnvironmentName: Optional[str] = None


class BackendEnvironment(BaseValidatorModel):
    backendEnvironmentArn: str
    environmentName: str
    createTime: datetime
    updateTime: datetime
    stackName: Optional[str] = None
    deploymentArtifacts: Optional[str] = None


class Backend(BaseValidatorModel):
    stackArn: Optional[str] = None


class CertificateSettings(BaseValidatorModel):
    type: CertificateTypeType
    customCertificateArn: Optional[str] = None


class Certificate(BaseValidatorModel):
    type: CertificateTypeType
    customCertificateArn: Optional[str] = None
    certificateVerificationDNSRecord: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'create_backend_environment' function.
class CreateBackendEnvironmentRequest(BaseValidatorModel):
    appId: str
    environmentName: str
    stackName: Optional[str] = None
    deploymentArtifacts: Optional[str] = None


# This class is the input for the 'create_deployment' function.
class CreateDeploymentRequest(BaseValidatorModel):
    appId: str
    branchName: str
    fileMap: Optional[Dict[str, str]] = None


class SubDomainSetting(BaseValidatorModel):
    prefix: str
    branchName: str


# This class is the input for the 'create_webhook' function.
class CreateWebhookRequest(BaseValidatorModel):
    appId: str
    branchName: str
    description: Optional[str] = None


class Webhook(BaseValidatorModel):
    webhookArn: str
    webhookId: str
    webhookUrl: str
    branchName: str
    description: str
    createTime: datetime
    updateTime: datetime


# This class is the input for the 'delete_app' function.
class DeleteAppRequest(BaseValidatorModel):
    appId: str


# This class is the input for the 'delete_backend_environment' function.
class DeleteBackendEnvironmentRequest(BaseValidatorModel):
    appId: str
    environmentName: str


# This class is the input for the 'delete_branch' function.
class DeleteBranchRequest(BaseValidatorModel):
    appId: str
    branchName: str


# This class is the input for the 'delete_domain_association' function.
class DeleteDomainAssociationRequest(BaseValidatorModel):
    appId: str
    domainName: str


# This class is the input for the 'delete_job' function.
class DeleteJobRequest(BaseValidatorModel):
    appId: str
    branchName: str
    jobId: str


class JobSummary(BaseValidatorModel):
    jobArn: str
    jobId: str
    commitId: str
    commitMessage: str
    commitTime: datetime
    startTime: datetime
    status: JobStatusType
    jobType: JobTypeType
    endTime: Optional[datetime] = None
    sourceUrl: Optional[str] = None
    sourceUrlType: Optional[SourceUrlTypeType] = None


# This class is the input for the 'delete_webhook' function.
class DeleteWebhookRequest(BaseValidatorModel):
    webhookId: str

Timestamp = Union[datetime, str]


# This class is the input for the 'get_app' function.
class GetAppRequest(BaseValidatorModel):
    appId: str


# This class is the input for the 'get_artifact_url' function.
class GetArtifactUrlRequest(BaseValidatorModel):
    artifactId: str


# This class is the input for the 'get_backend_environment' function.
class GetBackendEnvironmentRequest(BaseValidatorModel):
    appId: str
    environmentName: str


# This class is the input for the 'get_branch' function.
class GetBranchRequest(BaseValidatorModel):
    appId: str
    branchName: str


# This class is the input for the 'get_domain_association' function.
class GetDomainAssociationRequest(BaseValidatorModel):
    appId: str
    domainName: str


# This class is the input for the 'get_job' function.
class GetJobRequest(BaseValidatorModel):
    appId: str
    branchName: str
    jobId: str


# This class is the input for the 'get_webhook' function.
class GetWebhookRequest(BaseValidatorModel):
    webhookId: str


class Step(BaseValidatorModel):
    stepName: str
    startTime: datetime
    status: JobStatusType
    endTime: datetime
    logUrl: Optional[str] = None
    artifactsUrl: Optional[str] = None
    testArtifactsUrl: Optional[str] = None
    testConfigUrl: Optional[str] = None
    screenshots: Optional[Dict[str, str]] = None
    statusReason: Optional[str] = None
    context: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_apps' function.
class ListAppsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_artifacts' function.
class ListArtifactsRequest(BaseValidatorModel):
    appId: str
    branchName: str
    jobId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_backend_environments' function.
class ListBackendEnvironmentsRequest(BaseValidatorModel):
    appId: str
    environmentName: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_branches' function.
class ListBranchesRequest(BaseValidatorModel):
    appId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_domain_associations' function.
class ListDomainAssociationsRequest(BaseValidatorModel):
    appId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_jobs' function.
class ListJobsRequest(BaseValidatorModel):
    appId: str
    branchName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


# This class is the input for the 'list_webhooks' function.
class ListWebhooksRequest(BaseValidatorModel):
    appId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'start_deployment' function.
class StartDeploymentRequest(BaseValidatorModel):
    appId: str
    branchName: str
    jobId: Optional[str] = None
    sourceUrl: Optional[str] = None
    sourceUrlType: Optional[SourceUrlTypeType] = None


# This class is the input for the 'stop_job' function.
class StopJobRequest(BaseValidatorModel):
    appId: str
    branchName: str
    jobId: str


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'update_webhook' function.
class UpdateWebhookRequest(BaseValidatorModel):
    webhookId: str
    branchName: Optional[str] = None
    description: Optional[str] = None


class App(BaseValidatorModel):
    appId: str
    appArn: str
    name: str
    description: str
    repository: str
    platform: PlatformType
    createTime: datetime
    updateTime: datetime
    environmentVariables: Dict[str, str]
    defaultDomain: str
    enableBranchAutoBuild: bool
    enableBasicAuth: bool
    tags: Optional[Dict[str, str]] = None
    computeRoleArn: Optional[str] = None
    iamServiceRoleArn: Optional[str] = None
    enableBranchAutoDeletion: Optional[bool] = None
    basicAuthCredentials: Optional[str] = None
    customRules: Optional[List[CustomRule]] = None
    productionBranch: Optional[ProductionBranch] = None
    buildSpec: Optional[str] = None
    customHeaders: Optional[str] = None
    enableAutoBranchCreation: Optional[bool] = None
    autoBranchCreationPatterns: Optional[List[str]] = None
    autoBranchCreationConfig: Optional[AutoBranchCreationConfigOutput] = None
    repositoryCloneMethod: Optional[RepositoryCloneMethodType] = None
    cacheConfig: Optional[CacheConfig] = None
    webhookCreateTime: Optional[datetime] = None
    wafConfiguration: Optional[WafConfiguration] = None

AutoBranchCreationConfigUnion = Union[AutoBranchCreationConfig, AutoBranchCreationConfigOutput]


class Branch(BaseValidatorModel):
    branchArn: str
    branchName: str
    description: str
    stage: StageType
    displayName: str
    enableNotification: bool
    createTime: datetime
    updateTime: datetime
    environmentVariables: Dict[str, str]
    enableAutoBuild: bool
    customDomains: List[str]
    framework: str
    activeJobId: str
    totalNumberOfJobs: str
    enableBasicAuth: bool
    ttl: str
    enablePullRequestPreview: bool
    tags: Optional[Dict[str, str]] = None
    enablePerformanceMode: Optional[bool] = None
    thumbnailUrl: Optional[str] = None
    basicAuthCredentials: Optional[str] = None
    buildSpec: Optional[str] = None
    associatedResources: Optional[List[str]] = None
    pullRequestEnvironmentName: Optional[str] = None
    destinationBranch: Optional[str] = None
    sourceBranch: Optional[str] = None
    backendEnvironmentArn: Optional[str] = None
    backend: Optional[Backend] = None
    computeRoleArn: Optional[str] = None


# This class is the input for the 'create_branch' function.
class CreateBranchRequest(BaseValidatorModel):
    appId: str
    branchName: str
    description: Optional[str] = None
    stage: Optional[StageType] = None
    framework: Optional[str] = None
    enableNotification: Optional[bool] = None
    enableAutoBuild: Optional[bool] = None
    environmentVariables: Optional[Dict[str, str]] = None
    basicAuthCredentials: Optional[str] = None
    enableBasicAuth: Optional[bool] = None
    enablePerformanceMode: Optional[bool] = None
    tags: Optional[Dict[str, str]] = None
    buildSpec: Optional[str] = None
    ttl: Optional[str] = None
    displayName: Optional[str] = None
    enablePullRequestPreview: Optional[bool] = None
    pullRequestEnvironmentName: Optional[str] = None
    backendEnvironmentArn: Optional[str] = None
    backend: Optional[Backend] = None
    computeRoleArn: Optional[str] = None


# This class is the input for the 'update_branch' function.
class UpdateBranchRequest(BaseValidatorModel):
    appId: str
    branchName: str
    description: Optional[str] = None
    framework: Optional[str] = None
    stage: Optional[StageType] = None
    enableNotification: Optional[bool] = None
    enableAutoBuild: Optional[bool] = None
    environmentVariables: Optional[Dict[str, str]] = None
    basicAuthCredentials: Optional[str] = None
    enableBasicAuth: Optional[bool] = None
    enablePerformanceMode: Optional[bool] = None
    buildSpec: Optional[str] = None
    ttl: Optional[str] = None
    displayName: Optional[str] = None
    enablePullRequestPreview: Optional[bool] = None
    pullRequestEnvironmentName: Optional[str] = None
    backendEnvironmentArn: Optional[str] = None
    backend: Optional[Backend] = None
    computeRoleArn: Optional[str] = None


# This class is the output for the 'create_backend_environment' function.
class CreateBackendEnvironmentResult(BaseValidatorModel):
    backendEnvironment: BackendEnvironment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_deployment' function.
class CreateDeploymentResult(BaseValidatorModel):
    jobId: str
    fileUploadUrls: Dict[str, str]
    zipUploadUrl: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_backend_environment' function.
class DeleteBackendEnvironmentResult(BaseValidatorModel):
    backendEnvironment: BackendEnvironment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'generate_access_logs' function.
class GenerateAccessLogsResult(BaseValidatorModel):
    logUrl: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_artifact_url' function.
class GetArtifactUrlResult(BaseValidatorModel):
    artifactId: str
    artifactUrl: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_backend_environment' function.
class GetBackendEnvironmentResult(BaseValidatorModel):
    backendEnvironment: BackendEnvironment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_artifacts' function.
class ListArtifactsResult(BaseValidatorModel):
    artifacts: List[Artifact]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_backend_environments' function.
class ListBackendEnvironmentsResult(BaseValidatorModel):
    backendEnvironments: List[BackendEnvironment]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_domain_association' function.
class CreateDomainAssociationRequest(BaseValidatorModel):
    appId: str
    domainName: str
    subDomainSettings: List[SubDomainSetting]
    enableAutoSubDomain: Optional[bool] = None
    autoSubDomainCreationPatterns: Optional[List[str]] = None
    autoSubDomainIAMRole: Optional[str] = None
    certificateSettings: Optional[CertificateSettings] = None


class SubDomain(BaseValidatorModel):
    subDomainSetting: SubDomainSetting
    verified: bool
    dnsRecord: str


# This class is the input for the 'update_domain_association' function.
class UpdateDomainAssociationRequest(BaseValidatorModel):
    appId: str
    domainName: str
    enableAutoSubDomain: Optional[bool] = None
    subDomainSettings: Optional[List[SubDomainSetting]] = None
    autoSubDomainCreationPatterns: Optional[List[str]] = None
    autoSubDomainIAMRole: Optional[str] = None
    certificateSettings: Optional[CertificateSettings] = None


# This class is the output for the 'create_webhook' function.
class CreateWebhookResult(BaseValidatorModel):
    webhook: Webhook
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_webhook' function.
class DeleteWebhookResult(BaseValidatorModel):
    webhook: Webhook
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_webhook' function.
class GetWebhookResult(BaseValidatorModel):
    webhook: Webhook
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_webhooks' function.
class ListWebhooksResult(BaseValidatorModel):
    webhooks: List[Webhook]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_webhook' function.
class UpdateWebhookResult(BaseValidatorModel):
    webhook: Webhook
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_job' function.
class DeleteJobResult(BaseValidatorModel):
    jobSummary: JobSummary
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_jobs' function.
class ListJobsResult(BaseValidatorModel):
    jobSummaries: List[JobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'start_deployment' function.
class StartDeploymentResult(BaseValidatorModel):
    jobSummary: JobSummary
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_job' function.
class StartJobResult(BaseValidatorModel):
    jobSummary: JobSummary
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_job' function.
class StopJobResult(BaseValidatorModel):
    jobSummary: JobSummary
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'generate_access_logs' function.
class GenerateAccessLogsRequest(BaseValidatorModel):
    domainName: str
    appId: str
    startTime: Optional[Timestamp] = None
    endTime: Optional[Timestamp] = None


# This class is the input for the 'start_job' function.
class StartJobRequest(BaseValidatorModel):
    appId: str
    branchName: str
    jobType: JobTypeType
    jobId: Optional[str] = None
    jobReason: Optional[str] = None
    commitId: Optional[str] = None
    commitMessage: Optional[str] = None
    commitTime: Optional[Timestamp] = None


class Job(BaseValidatorModel):
    summary: JobSummary
    steps: List[Step]


class ListAppsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListBranchesRequestPaginate(BaseValidatorModel):
    appId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDomainAssociationsRequestPaginate(BaseValidatorModel):
    appId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListJobsRequestPaginate(BaseValidatorModel):
    appId: str
    branchName: str
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'create_app' function.
class CreateAppResult(BaseValidatorModel):
    app: App
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_app' function.
class DeleteAppResult(BaseValidatorModel):
    app: App
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_app' function.
class GetAppResult(BaseValidatorModel):
    app: App
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_apps' function.
class ListAppsResult(BaseValidatorModel):
    apps: List[App]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_app' function.
class UpdateAppResult(BaseValidatorModel):
    app: App
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_app' function.
class CreateAppRequest(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    repository: Optional[str] = None
    platform: Optional[PlatformType] = None
    computeRoleArn: Optional[str] = None
    iamServiceRoleArn: Optional[str] = None
    oauthToken: Optional[str] = None
    accessToken: Optional[str] = None
    environmentVariables: Optional[Dict[str, str]] = None
    enableBranchAutoBuild: Optional[bool] = None
    enableBranchAutoDeletion: Optional[bool] = None
    enableBasicAuth: Optional[bool] = None
    basicAuthCredentials: Optional[str] = None
    customRules: Optional[List[CustomRule]] = None
    tags: Optional[Dict[str, str]] = None
    buildSpec: Optional[str] = None
    customHeaders: Optional[str] = None
    enableAutoBranchCreation: Optional[bool] = None
    autoBranchCreationPatterns: Optional[List[str]] = None
    autoBranchCreationConfig: Optional[AutoBranchCreationConfigUnion] = None
    cacheConfig: Optional[CacheConfig] = None


# This class is the input for the 'update_app' function.
class UpdateAppRequest(BaseValidatorModel):
    appId: str
    name: Optional[str] = None
    description: Optional[str] = None
    platform: Optional[PlatformType] = None
    computeRoleArn: Optional[str] = None
    iamServiceRoleArn: Optional[str] = None
    environmentVariables: Optional[Dict[str, str]] = None
    enableBranchAutoBuild: Optional[bool] = None
    enableBranchAutoDeletion: Optional[bool] = None
    enableBasicAuth: Optional[bool] = None
    basicAuthCredentials: Optional[str] = None
    customRules: Optional[List[CustomRule]] = None
    buildSpec: Optional[str] = None
    customHeaders: Optional[str] = None
    enableAutoBranchCreation: Optional[bool] = None
    autoBranchCreationPatterns: Optional[List[str]] = None
    autoBranchCreationConfig: Optional[AutoBranchCreationConfigUnion] = None
    repository: Optional[str] = None
    oauthToken: Optional[str] = None
    accessToken: Optional[str] = None
    cacheConfig: Optional[CacheConfig] = None


# This class is the output for the 'create_branch' function.
class CreateBranchResult(BaseValidatorModel):
    branch: Branch
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_branch' function.
class DeleteBranchResult(BaseValidatorModel):
    branch: Branch
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_branch' function.
class GetBranchResult(BaseValidatorModel):
    branch: Branch
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_branches' function.
class ListBranchesResult(BaseValidatorModel):
    branches: List[Branch]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_branch' function.
class UpdateBranchResult(BaseValidatorModel):
    branch: Branch
    ResponseMetadata: ResponseMetadata


class DomainAssociation(BaseValidatorModel):
    domainAssociationArn: str
    domainName: str
    enableAutoSubDomain: bool
    domainStatus: DomainStatusType
    statusReason: str
    subDomains: List[SubDomain]
    autoSubDomainCreationPatterns: Optional[List[str]] = None
    autoSubDomainIAMRole: Optional[str] = None
    updateStatus: Optional[UpdateStatusType] = None
    certificateVerificationDNSRecord: Optional[str] = None
    certificate: Optional[Certificate] = None


# This class is the output for the 'get_job' function.
class GetJobResult(BaseValidatorModel):
    job: Job
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_domain_association' function.
class CreateDomainAssociationResult(BaseValidatorModel):
    domainAssociation: DomainAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_domain_association' function.
class DeleteDomainAssociationResult(BaseValidatorModel):
    domainAssociation: DomainAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_domain_association' function.
class GetDomainAssociationResult(BaseValidatorModel):
    domainAssociation: DomainAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_domain_associations' function.
class ListDomainAssociationsResult(BaseValidatorModel):
    domainAssociations: List[DomainAssociation]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_domain_association' function.
class UpdateDomainAssociationResult(BaseValidatorModel):
    domainAssociation: DomainAssociation
    ResponseMetadata: ResponseMetadata
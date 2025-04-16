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
from aws_resource_validator.pydantic_models.amplify_constants import *

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
    environmentVariables: Optional[Mapping[str, str]] = None
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


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateBackendEnvironmentRequest(BaseValidatorModel):
    appId: str
    environmentName: str
    stackName: Optional[str] = None
    deploymentArtifacts: Optional[str] = None


class CreateDeploymentRequest(BaseValidatorModel):
    appId: str
    branchName: str
    fileMap: Optional[Mapping[str, str]] = None


class SubDomainSetting(BaseValidatorModel):
    prefix: str
    branchName: str


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


class DeleteAppRequest(BaseValidatorModel):
    appId: str


class DeleteBackendEnvironmentRequest(BaseValidatorModel):
    appId: str
    environmentName: str


class DeleteBranchRequest(BaseValidatorModel):
    appId: str
    branchName: str


class DeleteDomainAssociationRequest(BaseValidatorModel):
    appId: str
    domainName: str


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


class DeleteWebhookRequest(BaseValidatorModel):
    webhookId: str


class GetAppRequest(BaseValidatorModel):
    appId: str


class GetArtifactUrlRequest(BaseValidatorModel):
    artifactId: str


class GetBackendEnvironmentRequest(BaseValidatorModel):
    appId: str
    environmentName: str


class GetBranchRequest(BaseValidatorModel):
    appId: str
    branchName: str


class GetDomainAssociationRequest(BaseValidatorModel):
    appId: str
    domainName: str


class GetJobRequest(BaseValidatorModel):
    appId: str
    branchName: str
    jobId: str


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


class ListAppsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListArtifactsRequest(BaseValidatorModel):
    appId: str
    branchName: str
    jobId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListBackendEnvironmentsRequest(BaseValidatorModel):
    appId: str
    environmentName: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListBranchesRequest(BaseValidatorModel):
    appId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDomainAssociationsRequest(BaseValidatorModel):
    appId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListJobsRequest(BaseValidatorModel):
    appId: str
    branchName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class ListWebhooksRequest(BaseValidatorModel):
    appId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class StartDeploymentRequest(BaseValidatorModel):
    appId: str
    branchName: str
    jobId: Optional[str] = None
    sourceUrl: Optional[str] = None
    sourceUrlType: Optional[SourceUrlTypeType] = None


class StopJobRequest(BaseValidatorModel):
    appId: str
    branchName: str
    jobId: str


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateWebhookRequest(BaseValidatorModel):
    webhookId: str
    branchName: Optional[str] = None
    description: Optional[str] = None


class CacheConfig(BaseValidatorModel):
    pass


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


class CreateBranchRequest(BaseValidatorModel):
    appId: str
    branchName: str
    description: Optional[str] = None
    stage: Optional[StageType] = None
    framework: Optional[str] = None
    enableNotification: Optional[bool] = None
    enableAutoBuild: Optional[bool] = None
    environmentVariables: Optional[Mapping[str, str]] = None
    basicAuthCredentials: Optional[str] = None
    enableBasicAuth: Optional[bool] = None
    enablePerformanceMode: Optional[bool] = None
    tags: Optional[Mapping[str, str]] = None
    buildSpec: Optional[str] = None
    ttl: Optional[str] = None
    displayName: Optional[str] = None
    enablePullRequestPreview: Optional[bool] = None
    pullRequestEnvironmentName: Optional[str] = None
    backendEnvironmentArn: Optional[str] = None
    backend: Optional[Backend] = None
    computeRoleArn: Optional[str] = None


class UpdateBranchRequest(BaseValidatorModel):
    appId: str
    branchName: str
    description: Optional[str] = None
    framework: Optional[str] = None
    stage: Optional[StageType] = None
    enableNotification: Optional[bool] = None
    enableAutoBuild: Optional[bool] = None
    environmentVariables: Optional[Mapping[str, str]] = None
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


class CreateBackendEnvironmentResult(BaseValidatorModel):
    backendEnvironment: BackendEnvironment
    ResponseMetadata: ResponseMetadata


class CreateDeploymentResult(BaseValidatorModel):
    jobId: str
    fileUploadUrls: Dict[str, str]
    zipUploadUrl: str
    ResponseMetadata: ResponseMetadata


class DeleteBackendEnvironmentResult(BaseValidatorModel):
    backendEnvironment: BackendEnvironment
    ResponseMetadata: ResponseMetadata


class GenerateAccessLogsResult(BaseValidatorModel):
    logUrl: str
    ResponseMetadata: ResponseMetadata


class GetArtifactUrlResult(BaseValidatorModel):
    artifactId: str
    artifactUrl: str
    ResponseMetadata: ResponseMetadata


class GetBackendEnvironmentResult(BaseValidatorModel):
    backendEnvironment: BackendEnvironment
    ResponseMetadata: ResponseMetadata


class ListArtifactsResult(BaseValidatorModel):
    artifacts: List[Artifact]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListBackendEnvironmentsResult(BaseValidatorModel):
    backendEnvironments: List[BackendEnvironment]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CertificateSettings(BaseValidatorModel):
    pass


class CreateDomainAssociationRequest(BaseValidatorModel):
    appId: str
    domainName: str
    subDomainSettings: Sequence[SubDomainSetting]
    enableAutoSubDomain: Optional[bool] = None
    autoSubDomainCreationPatterns: Optional[Sequence[str]] = None
    autoSubDomainIAMRole: Optional[str] = None
    certificateSettings: Optional[CertificateSettings] = None


class SubDomain(BaseValidatorModel):
    subDomainSetting: SubDomainSetting
    verified: bool
    dnsRecord: str


class UpdateDomainAssociationRequest(BaseValidatorModel):
    appId: str
    domainName: str
    enableAutoSubDomain: Optional[bool] = None
    subDomainSettings: Optional[Sequence[SubDomainSetting]] = None
    autoSubDomainCreationPatterns: Optional[Sequence[str]] = None
    autoSubDomainIAMRole: Optional[str] = None
    certificateSettings: Optional[CertificateSettings] = None


class CreateWebhookResult(BaseValidatorModel):
    webhook: Webhook
    ResponseMetadata: ResponseMetadata


class DeleteWebhookResult(BaseValidatorModel):
    webhook: Webhook
    ResponseMetadata: ResponseMetadata


class GetWebhookResult(BaseValidatorModel):
    webhook: Webhook
    ResponseMetadata: ResponseMetadata


class ListWebhooksResult(BaseValidatorModel):
    webhooks: List[Webhook]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateWebhookResult(BaseValidatorModel):
    webhook: Webhook
    ResponseMetadata: ResponseMetadata


class DeleteJobResult(BaseValidatorModel):
    jobSummary: JobSummary
    ResponseMetadata: ResponseMetadata


class ListJobsResult(BaseValidatorModel):
    jobSummaries: List[JobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class StartDeploymentResult(BaseValidatorModel):
    jobSummary: JobSummary
    ResponseMetadata: ResponseMetadata


class StartJobResult(BaseValidatorModel):
    jobSummary: JobSummary
    ResponseMetadata: ResponseMetadata


class StopJobResult(BaseValidatorModel):
    jobSummary: JobSummary
    ResponseMetadata: ResponseMetadata


class Timestamp(BaseValidatorModel):
    pass


class GenerateAccessLogsRequest(BaseValidatorModel):
    domainName: str
    appId: str
    startTime: Optional[Timestamp] = None
    endTime: Optional[Timestamp] = None


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


class CreateAppResult(BaseValidatorModel):
    app: App
    ResponseMetadata: ResponseMetadata


class DeleteAppResult(BaseValidatorModel):
    app: App
    ResponseMetadata: ResponseMetadata


class GetAppResult(BaseValidatorModel):
    app: App
    ResponseMetadata: ResponseMetadata


class ListAppsResult(BaseValidatorModel):
    apps: List[App]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateAppResult(BaseValidatorModel):
    app: App
    ResponseMetadata: ResponseMetadata


class AutoBranchCreationConfigUnion(BaseValidatorModel):
    pass


class CreateAppRequest(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    repository: Optional[str] = None
    platform: Optional[PlatformType] = None
    computeRoleArn: Optional[str] = None
    iamServiceRoleArn: Optional[str] = None
    oauthToken: Optional[str] = None
    accessToken: Optional[str] = None
    environmentVariables: Optional[Mapping[str, str]] = None
    enableBranchAutoBuild: Optional[bool] = None
    enableBranchAutoDeletion: Optional[bool] = None
    enableBasicAuth: Optional[bool] = None
    basicAuthCredentials: Optional[str] = None
    customRules: Optional[Sequence[CustomRule]] = None
    tags: Optional[Mapping[str, str]] = None
    buildSpec: Optional[str] = None
    customHeaders: Optional[str] = None
    enableAutoBranchCreation: Optional[bool] = None
    autoBranchCreationPatterns: Optional[Sequence[str]] = None
    autoBranchCreationConfig: Optional[AutoBranchCreationConfigUnion] = None
    cacheConfig: Optional[CacheConfig] = None


class UpdateAppRequest(BaseValidatorModel):
    appId: str
    name: Optional[str] = None
    description: Optional[str] = None
    platform: Optional[PlatformType] = None
    computeRoleArn: Optional[str] = None
    iamServiceRoleArn: Optional[str] = None
    environmentVariables: Optional[Mapping[str, str]] = None
    enableBranchAutoBuild: Optional[bool] = None
    enableBranchAutoDeletion: Optional[bool] = None
    enableBasicAuth: Optional[bool] = None
    basicAuthCredentials: Optional[str] = None
    customRules: Optional[Sequence[CustomRule]] = None
    buildSpec: Optional[str] = None
    customHeaders: Optional[str] = None
    enableAutoBranchCreation: Optional[bool] = None
    autoBranchCreationPatterns: Optional[Sequence[str]] = None
    autoBranchCreationConfig: Optional[AutoBranchCreationConfigUnion] = None
    repository: Optional[str] = None
    oauthToken: Optional[str] = None
    accessToken: Optional[str] = None
    cacheConfig: Optional[CacheConfig] = None


class CreateBranchResult(BaseValidatorModel):
    branch: Branch
    ResponseMetadata: ResponseMetadata


class DeleteBranchResult(BaseValidatorModel):
    branch: Branch
    ResponseMetadata: ResponseMetadata


class GetBranchResult(BaseValidatorModel):
    branch: Branch
    ResponseMetadata: ResponseMetadata


class ListBranchesResult(BaseValidatorModel):
    branches: List[Branch]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateBranchResult(BaseValidatorModel):
    branch: Branch
    ResponseMetadata: ResponseMetadata


class Certificate(BaseValidatorModel):
    pass


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


class GetJobResult(BaseValidatorModel):
    job: Job
    ResponseMetadata: ResponseMetadata


class CreateDomainAssociationResult(BaseValidatorModel):
    domainAssociation: DomainAssociation
    ResponseMetadata: ResponseMetadata


class DeleteDomainAssociationResult(BaseValidatorModel):
    domainAssociation: DomainAssociation
    ResponseMetadata: ResponseMetadata


class GetDomainAssociationResult(BaseValidatorModel):
    domainAssociation: DomainAssociation
    ResponseMetadata: ResponseMetadata


class ListDomainAssociationsResult(BaseValidatorModel):
    domainAssociations: List[DomainAssociation]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateDomainAssociationResult(BaseValidatorModel):
    domainAssociation: DomainAssociation
    ResponseMetadata: ResponseMetadata



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

class AutoBranchCreationConfigOutputTypeDef(BaseValidatorModel):
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


class CustomRuleTypeDef(BaseValidatorModel):
    source: str
    target: str
    status: Optional[str] = None
    condition: Optional[str] = None


class ProductionBranchTypeDef(BaseValidatorModel):
    lastDeployTime: Optional[datetime] = None
    status: Optional[str] = None
    thumbnailUrl: Optional[str] = None
    branchName: Optional[str] = None


class WafConfigurationTypeDef(BaseValidatorModel):
    webAclArn: Optional[str] = None
    wafStatus: Optional[WafStatusType] = None
    statusReason: Optional[str] = None


class ArtifactTypeDef(BaseValidatorModel):
    artifactFileName: str
    artifactId: str


class AutoBranchCreationConfigTypeDef(BaseValidatorModel):
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


class BackendEnvironmentTypeDef(BaseValidatorModel):
    backendEnvironmentArn: str
    environmentName: str
    createTime: datetime
    updateTime: datetime
    stackName: Optional[str] = None
    deploymentArtifacts: Optional[str] = None


class BackendTypeDef(BaseValidatorModel):
    stackArn: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateBackendEnvironmentRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    stackName: Optional[str] = None
    deploymentArtifacts: Optional[str] = None


class CreateDeploymentRequestTypeDef(BaseValidatorModel):
    appId: str
    branchName: str
    fileMap: Optional[Mapping[str, str]] = None


class SubDomainSettingTypeDef(BaseValidatorModel):
    prefix: str
    branchName: str


class CreateWebhookRequestTypeDef(BaseValidatorModel):
    appId: str
    branchName: str
    description: Optional[str] = None


class WebhookTypeDef(BaseValidatorModel):
    webhookArn: str
    webhookId: str
    webhookUrl: str
    branchName: str
    description: str
    createTime: datetime
    updateTime: datetime


class DeleteAppRequestTypeDef(BaseValidatorModel):
    appId: str


class DeleteBackendEnvironmentRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str


class DeleteBranchRequestTypeDef(BaseValidatorModel):
    appId: str
    branchName: str


class DeleteDomainAssociationRequestTypeDef(BaseValidatorModel):
    appId: str
    domainName: str


class DeleteJobRequestTypeDef(BaseValidatorModel):
    appId: str
    branchName: str
    jobId: str


class JobSummaryTypeDef(BaseValidatorModel):
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


class DeleteWebhookRequestTypeDef(BaseValidatorModel):
    webhookId: str


class GetAppRequestTypeDef(BaseValidatorModel):
    appId: str


class GetArtifactUrlRequestTypeDef(BaseValidatorModel):
    artifactId: str


class GetBackendEnvironmentRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str


class GetBranchRequestTypeDef(BaseValidatorModel):
    appId: str
    branchName: str


class GetDomainAssociationRequestTypeDef(BaseValidatorModel):
    appId: str
    domainName: str


class GetJobRequestTypeDef(BaseValidatorModel):
    appId: str
    branchName: str
    jobId: str


class GetWebhookRequestTypeDef(BaseValidatorModel):
    webhookId: str


class StepTypeDef(BaseValidatorModel):
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


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAppsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListArtifactsRequestTypeDef(BaseValidatorModel):
    appId: str
    branchName: str
    jobId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListBackendEnvironmentsRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListBranchesRequestTypeDef(BaseValidatorModel):
    appId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDomainAssociationsRequestTypeDef(BaseValidatorModel):
    appId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListJobsRequestTypeDef(BaseValidatorModel):
    appId: str
    branchName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class ListWebhooksRequestTypeDef(BaseValidatorModel):
    appId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class StartDeploymentRequestTypeDef(BaseValidatorModel):
    appId: str
    branchName: str
    jobId: Optional[str] = None
    sourceUrl: Optional[str] = None
    sourceUrlType: Optional[SourceUrlTypeType] = None


class StopJobRequestTypeDef(BaseValidatorModel):
    appId: str
    branchName: str
    jobId: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateWebhookRequestTypeDef(BaseValidatorModel):
    webhookId: str
    branchName: Optional[str] = None
    description: Optional[str] = None


class CacheConfigTypeDef(BaseValidatorModel):
    pass


class AppTypeDef(BaseValidatorModel):
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
    customRules: Optional[List[CustomRuleTypeDef]] = None
    productionBranch: Optional[ProductionBranchTypeDef] = None
    buildSpec: Optional[str] = None
    customHeaders: Optional[str] = None
    enableAutoBranchCreation: Optional[bool] = None
    autoBranchCreationPatterns: Optional[List[str]] = None
    autoBranchCreationConfig: Optional[AutoBranchCreationConfigOutputTypeDef] = None
    repositoryCloneMethod: Optional[RepositoryCloneMethodType] = None
    cacheConfig: Optional[CacheConfigTypeDef] = None
    webhookCreateTime: Optional[datetime] = None
    wafConfiguration: Optional[WafConfigurationTypeDef] = None


class BranchTypeDef(BaseValidatorModel):
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
    backend: Optional[BackendTypeDef] = None
    computeRoleArn: Optional[str] = None


class CreateBranchRequestTypeDef(BaseValidatorModel):
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
    backend: Optional[BackendTypeDef] = None
    computeRoleArn: Optional[str] = None


class UpdateBranchRequestTypeDef(BaseValidatorModel):
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
    backend: Optional[BackendTypeDef] = None
    computeRoleArn: Optional[str] = None


class CreateBackendEnvironmentResultTypeDef(BaseValidatorModel):
    backendEnvironment: BackendEnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDeploymentResultTypeDef(BaseValidatorModel):
    jobId: str
    fileUploadUrls: Dict[str, str]
    zipUploadUrl: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteBackendEnvironmentResultTypeDef(BaseValidatorModel):
    backendEnvironment: BackendEnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GenerateAccessLogsResultTypeDef(BaseValidatorModel):
    logUrl: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetArtifactUrlResultTypeDef(BaseValidatorModel):
    artifactId: str
    artifactUrl: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetBackendEnvironmentResultTypeDef(BaseValidatorModel):
    backendEnvironment: BackendEnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListArtifactsResultTypeDef(BaseValidatorModel):
    artifacts: List[ArtifactTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListBackendEnvironmentsResultTypeDef(BaseValidatorModel):
    backendEnvironments: List[BackendEnvironmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class CertificateSettingsTypeDef(BaseValidatorModel):
    pass


class CreateDomainAssociationRequestTypeDef(BaseValidatorModel):
    appId: str
    domainName: str
    subDomainSettings: Sequence[SubDomainSettingTypeDef]
    enableAutoSubDomain: Optional[bool] = None
    autoSubDomainCreationPatterns: Optional[Sequence[str]] = None
    autoSubDomainIAMRole: Optional[str] = None
    certificateSettings: Optional[CertificateSettingsTypeDef] = None


class SubDomainTypeDef(BaseValidatorModel):
    subDomainSetting: SubDomainSettingTypeDef
    verified: bool
    dnsRecord: str


class UpdateDomainAssociationRequestTypeDef(BaseValidatorModel):
    appId: str
    domainName: str
    enableAutoSubDomain: Optional[bool] = None
    subDomainSettings: Optional[Sequence[SubDomainSettingTypeDef]] = None
    autoSubDomainCreationPatterns: Optional[Sequence[str]] = None
    autoSubDomainIAMRole: Optional[str] = None
    certificateSettings: Optional[CertificateSettingsTypeDef] = None


class CreateWebhookResultTypeDef(BaseValidatorModel):
    webhook: WebhookTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteWebhookResultTypeDef(BaseValidatorModel):
    webhook: WebhookTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetWebhookResultTypeDef(BaseValidatorModel):
    webhook: WebhookTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListWebhooksResultTypeDef(BaseValidatorModel):
    webhooks: List[WebhookTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateWebhookResultTypeDef(BaseValidatorModel):
    webhook: WebhookTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteJobResultTypeDef(BaseValidatorModel):
    jobSummary: JobSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListJobsResultTypeDef(BaseValidatorModel):
    jobSummaries: List[JobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class StartDeploymentResultTypeDef(BaseValidatorModel):
    jobSummary: JobSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StartJobResultTypeDef(BaseValidatorModel):
    jobSummary: JobSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StopJobResultTypeDef(BaseValidatorModel):
    jobSummary: JobSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class TimestampTypeDef(BaseValidatorModel):
    pass


class GenerateAccessLogsRequestTypeDef(BaseValidatorModel):
    domainName: str
    appId: str
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None


class StartJobRequestTypeDef(BaseValidatorModel):
    appId: str
    branchName: str
    jobType: JobTypeType
    jobId: Optional[str] = None
    jobReason: Optional[str] = None
    commitId: Optional[str] = None
    commitMessage: Optional[str] = None
    commitTime: Optional[TimestampTypeDef] = None


class JobTypeDef(BaseValidatorModel):
    summary: JobSummaryTypeDef
    steps: List[StepTypeDef]


class ListAppsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListBranchesRequestPaginateTypeDef(BaseValidatorModel):
    appId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDomainAssociationsRequestPaginateTypeDef(BaseValidatorModel):
    appId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListJobsRequestPaginateTypeDef(BaseValidatorModel):
    appId: str
    branchName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class CreateAppResultTypeDef(BaseValidatorModel):
    app: AppTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteAppResultTypeDef(BaseValidatorModel):
    app: AppTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetAppResultTypeDef(BaseValidatorModel):
    app: AppTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListAppsResultTypeDef(BaseValidatorModel):
    apps: List[AppTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateAppResultTypeDef(BaseValidatorModel):
    app: AppTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AutoBranchCreationConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateAppRequestTypeDef(BaseValidatorModel):
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
    customRules: Optional[Sequence[CustomRuleTypeDef]] = None
    tags: Optional[Mapping[str, str]] = None
    buildSpec: Optional[str] = None
    customHeaders: Optional[str] = None
    enableAutoBranchCreation: Optional[bool] = None
    autoBranchCreationPatterns: Optional[Sequence[str]] = None
    autoBranchCreationConfig: Optional[AutoBranchCreationConfigUnionTypeDef] = None
    cacheConfig: Optional[CacheConfigTypeDef] = None


class UpdateAppRequestTypeDef(BaseValidatorModel):
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
    customRules: Optional[Sequence[CustomRuleTypeDef]] = None
    buildSpec: Optional[str] = None
    customHeaders: Optional[str] = None
    enableAutoBranchCreation: Optional[bool] = None
    autoBranchCreationPatterns: Optional[Sequence[str]] = None
    autoBranchCreationConfig: Optional[AutoBranchCreationConfigUnionTypeDef] = None
    repository: Optional[str] = None
    oauthToken: Optional[str] = None
    accessToken: Optional[str] = None
    cacheConfig: Optional[CacheConfigTypeDef] = None


class CreateBranchResultTypeDef(BaseValidatorModel):
    branch: BranchTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteBranchResultTypeDef(BaseValidatorModel):
    branch: BranchTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetBranchResultTypeDef(BaseValidatorModel):
    branch: BranchTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListBranchesResultTypeDef(BaseValidatorModel):
    branches: List[BranchTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateBranchResultTypeDef(BaseValidatorModel):
    branch: BranchTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CertificateTypeDef(BaseValidatorModel):
    pass


class DomainAssociationTypeDef(BaseValidatorModel):
    domainAssociationArn: str
    domainName: str
    enableAutoSubDomain: bool
    domainStatus: DomainStatusType
    statusReason: str
    subDomains: List[SubDomainTypeDef]
    autoSubDomainCreationPatterns: Optional[List[str]] = None
    autoSubDomainIAMRole: Optional[str] = None
    updateStatus: Optional[UpdateStatusType] = None
    certificateVerificationDNSRecord: Optional[str] = None
    certificate: Optional[CertificateTypeDef] = None


class GetJobResultTypeDef(BaseValidatorModel):
    job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDomainAssociationResultTypeDef(BaseValidatorModel):
    domainAssociation: DomainAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDomainAssociationResultTypeDef(BaseValidatorModel):
    domainAssociation: DomainAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetDomainAssociationResultTypeDef(BaseValidatorModel):
    domainAssociation: DomainAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListDomainAssociationsResultTypeDef(BaseValidatorModel):
    domainAssociations: List[DomainAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateDomainAssociationResultTypeDef(BaseValidatorModel):
    domainAssociation: DomainAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef



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
from aws_resource_validator.pydantic_models.amplify_constants import *

class AutoBranchCreationConfigOutputTypeDef(BaseModel):
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

class CustomRuleTypeDef(BaseModel):
    source: str
    target: str
    status: Optional[str] = None
    condition: Optional[str] = None

class ProductionBranchTypeDef(BaseModel):
    lastDeployTime: Optional[datetime] = None
    status: Optional[str] = None
    thumbnailUrl: Optional[str] = None
    branchName: Optional[str] = None

class ArtifactTypeDef(BaseModel):
    artifactFileName: str
    artifactId: str

class AutoBranchCreationConfigExtraOutputTypeDef(BaseModel):
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

class AutoBranchCreationConfigTypeDef(BaseModel):
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

class BackendEnvironmentTypeDef(BaseModel):
    backendEnvironmentArn: str
    environmentName: str
    createTime: datetime
    updateTime: datetime
    stackName: Optional[str] = None
    deploymentArtifacts: Optional[str] = None

class BackendTypeDef(BaseModel):
    stackArn: Optional[str] = None

class CertificateSettingsTypeDef(BaseModel):
    type: CertificateTypeType
    customCertificateArn: Optional[str] = None

class CertificateTypeDef(BaseModel):
    type: CertificateTypeType
    customCertificateArn: Optional[str] = None
    certificateVerificationDNSRecord: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CreateBackendEnvironmentRequestRequestTypeDef(BaseModel):
    appId: str
    environmentName: str
    stackName: Optional[str] = None
    deploymentArtifacts: Optional[str] = None

class CreateDeploymentRequestRequestTypeDef(BaseModel):
    appId: str
    branchName: str
    fileMap: Optional[Mapping[str, str]] = None

class SubDomainSettingTypeDef(BaseModel):
    prefix: str
    branchName: str

class CreateWebhookRequestRequestTypeDef(BaseModel):
    appId: str
    branchName: str
    description: Optional[str] = None

class WebhookTypeDef(BaseModel):
    webhookArn: str
    webhookId: str
    webhookUrl: str
    branchName: str
    description: str
    createTime: datetime
    updateTime: datetime

class DeleteAppRequestRequestTypeDef(BaseModel):
    appId: str

class DeleteBackendEnvironmentRequestRequestTypeDef(BaseModel):
    appId: str
    environmentName: str

class DeleteBranchRequestRequestTypeDef(BaseModel):
    appId: str
    branchName: str

class DeleteDomainAssociationRequestRequestTypeDef(BaseModel):
    appId: str
    domainName: str

class DeleteJobRequestRequestTypeDef(BaseModel):
    appId: str
    branchName: str
    jobId: str

class JobSummaryTypeDef(BaseModel):
    jobArn: str
    jobId: str
    commitId: str
    commitMessage: str
    commitTime: datetime
    startTime: datetime
    status: JobStatusType
    jobType: JobTypeType
    endTime: Optional[datetime] = None

class DeleteWebhookRequestRequestTypeDef(BaseModel):
    webhookId: str

class GetAppRequestRequestTypeDef(BaseModel):
    appId: str

class GetArtifactUrlRequestRequestTypeDef(BaseModel):
    artifactId: str

class GetBackendEnvironmentRequestRequestTypeDef(BaseModel):
    appId: str
    environmentName: str

class GetBranchRequestRequestTypeDef(BaseModel):
    appId: str
    branchName: str

class GetDomainAssociationRequestRequestTypeDef(BaseModel):
    appId: str
    domainName: str

class GetJobRequestRequestTypeDef(BaseModel):
    appId: str
    branchName: str
    jobId: str

class GetWebhookRequestRequestTypeDef(BaseModel):
    webhookId: str

class StepTypeDef(BaseModel):
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

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAppsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListArtifactsRequestRequestTypeDef(BaseModel):
    appId: str
    branchName: str
    jobId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListBackendEnvironmentsRequestRequestTypeDef(BaseModel):
    appId: str
    environmentName: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListBranchesRequestRequestTypeDef(BaseModel):
    appId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDomainAssociationsRequestRequestTypeDef(BaseModel):
    appId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListJobsRequestRequestTypeDef(BaseModel):
    appId: str
    branchName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class ListWebhooksRequestRequestTypeDef(BaseModel):
    appId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class StartDeploymentRequestRequestTypeDef(BaseModel):
    appId: str
    branchName: str
    jobId: Optional[str] = None
    sourceUrl: Optional[str] = None

class StopJobRequestRequestTypeDef(BaseModel):
    appId: str
    branchName: str
    jobId: str

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateWebhookRequestRequestTypeDef(BaseModel):
    webhookId: str
    branchName: Optional[str] = None
    description: Optional[str] = None

class AppTypeDef(BaseModel):
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

class CreateAppRequestRequestTypeDef(BaseModel):
    name: str
    description: Optional[str] = None
    repository: Optional[str] = None
    platform: Optional[PlatformType] = None
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
    autoBranchCreationConfig: Optional[AutoBranchCreationConfigTypeDef] = None

class UpdateAppRequestRequestTypeDef(BaseModel):
    appId: str
    name: Optional[str] = None
    description: Optional[str] = None
    platform: Optional[PlatformType] = None
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
    autoBranchCreationConfig: Optional[AutoBranchCreationConfigTypeDef] = None
    repository: Optional[str] = None
    oauthToken: Optional[str] = None
    accessToken: Optional[str] = None

class BranchTypeDef(BaseModel):
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

class CreateBranchRequestRequestTypeDef(BaseModel):
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

class UpdateBranchRequestRequestTypeDef(BaseModel):
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

class CreateBackendEnvironmentResultTypeDef(BaseModel):
    backendEnvironment: BackendEnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDeploymentResultTypeDef(BaseModel):
    jobId: str
    fileUploadUrls: Dict[str, str]
    zipUploadUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBackendEnvironmentResultTypeDef(BaseModel):
    backendEnvironment: BackendEnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateAccessLogsResultTypeDef(BaseModel):
    logUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetArtifactUrlResultTypeDef(BaseModel):
    artifactId: str
    artifactUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBackendEnvironmentResultTypeDef(BaseModel):
    backendEnvironment: BackendEnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListArtifactsResultTypeDef(BaseModel):
    artifacts: List[ArtifactTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListBackendEnvironmentsResultTypeDef(BaseModel):
    backendEnvironments: List[BackendEnvironmentTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDomainAssociationRequestRequestTypeDef(BaseModel):
    appId: str
    domainName: str
    subDomainSettings: Sequence[SubDomainSettingTypeDef]
    enableAutoSubDomain: Optional[bool] = None
    autoSubDomainCreationPatterns: Optional[Sequence[str]] = None
    autoSubDomainIAMRole: Optional[str] = None
    certificateSettings: Optional[CertificateSettingsTypeDef] = None

class SubDomainTypeDef(BaseModel):
    subDomainSetting: SubDomainSettingTypeDef
    verified: bool
    dnsRecord: str

class UpdateDomainAssociationRequestRequestTypeDef(BaseModel):
    appId: str
    domainName: str
    enableAutoSubDomain: Optional[bool] = None
    subDomainSettings: Optional[Sequence[SubDomainSettingTypeDef]] = None
    autoSubDomainCreationPatterns: Optional[Sequence[str]] = None
    autoSubDomainIAMRole: Optional[str] = None
    certificateSettings: Optional[CertificateSettingsTypeDef] = None

class CreateWebhookResultTypeDef(BaseModel):
    webhook: WebhookTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteWebhookResultTypeDef(BaseModel):
    webhook: WebhookTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetWebhookResultTypeDef(BaseModel):
    webhook: WebhookTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListWebhooksResultTypeDef(BaseModel):
    webhooks: List[WebhookTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWebhookResultTypeDef(BaseModel):
    webhook: WebhookTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteJobResultTypeDef(BaseModel):
    jobSummary: JobSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListJobsResultTypeDef(BaseModel):
    jobSummaries: List[JobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartDeploymentResultTypeDef(BaseModel):
    jobSummary: JobSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartJobResultTypeDef(BaseModel):
    jobSummary: JobSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopJobResultTypeDef(BaseModel):
    jobSummary: JobSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateAccessLogsRequestRequestTypeDef(BaseModel):
    domainName: str
    appId: str
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None

class StartJobRequestRequestTypeDef(BaseModel):
    appId: str
    branchName: str
    jobType: JobTypeType
    jobId: Optional[str] = None
    jobReason: Optional[str] = None
    commitId: Optional[str] = None
    commitMessage: Optional[str] = None
    commitTime: Optional[TimestampTypeDef] = None

class JobTypeDef(BaseModel):
    summary: JobSummaryTypeDef
    steps: List[StepTypeDef]

class ListAppsRequestListAppsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBranchesRequestListBranchesPaginateTypeDef(BaseModel):
    appId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDomainAssociationsRequestListDomainAssociationsPaginateTypeDef(BaseModel):
    appId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobsRequestListJobsPaginateTypeDef(BaseModel):
    appId: str
    branchName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class CreateAppResultTypeDef(BaseModel):
    app: AppTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAppResultTypeDef(BaseModel):
    app: AppTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAppResultTypeDef(BaseModel):
    app: AppTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppsResultTypeDef(BaseModel):
    apps: List[AppTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAppResultTypeDef(BaseModel):
    app: AppTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBranchResultTypeDef(BaseModel):
    branch: BranchTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBranchResultTypeDef(BaseModel):
    branch: BranchTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetBranchResultTypeDef(BaseModel):
    branch: BranchTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListBranchesResultTypeDef(BaseModel):
    branches: List[BranchTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBranchResultTypeDef(BaseModel):
    branch: BranchTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DomainAssociationTypeDef(BaseModel):
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

class GetJobResultTypeDef(BaseModel):
    job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDomainAssociationResultTypeDef(BaseModel):
    domainAssociation: DomainAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDomainAssociationResultTypeDef(BaseModel):
    domainAssociation: DomainAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDomainAssociationResultTypeDef(BaseModel):
    domainAssociation: DomainAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDomainAssociationsResultTypeDef(BaseModel):
    domainAssociations: List[DomainAssociationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDomainAssociationResultTypeDef(BaseModel):
    domainAssociation: DomainAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


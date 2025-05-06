from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.proton.proton_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AcceptEnvironmentAccountConnectionInput(BaseValidatorModel):
    id: str


class EnvironmentAccountConnection(BaseValidatorModel):
    arn: str
    environmentAccountId: str
    environmentName: str
    id: str
    lastModifiedAt: datetime
    managementAccountId: str
    requestedAt: datetime
    roleArn: str
    status: EnvironmentAccountConnectionStatusType
    codebuildRoleArn: Optional[str] = None
    componentRoleArn: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class RepositoryBranch(BaseValidatorModel):
    arn: str
    branch: str
    name: str
    provider: RepositoryProviderType


class CancelComponentDeploymentInput(BaseValidatorModel):
    componentName: str


class Component(BaseValidatorModel):
    arn: str
    createdAt: datetime
    deploymentStatus: DeploymentStatusType
    environmentName: str
    lastModifiedAt: datetime
    name: str
    deploymentStatusMessage: Optional[str] = None
    description: Optional[str] = None
    lastAttemptedDeploymentId: Optional[str] = None
    lastClientRequestToken: Optional[str] = None
    lastDeploymentAttemptedAt: Optional[datetime] = None
    lastDeploymentSucceededAt: Optional[datetime] = None
    lastSucceededDeploymentId: Optional[str] = None
    serviceInstanceName: Optional[str] = None
    serviceName: Optional[str] = None
    serviceSpec: Optional[str] = None


class CancelEnvironmentDeploymentInput(BaseValidatorModel):
    environmentName: str


class CancelServiceInstanceDeploymentInput(BaseValidatorModel):
    serviceInstanceName: str
    serviceName: str


class ServiceInstance(BaseValidatorModel):
    arn: str
    createdAt: datetime
    deploymentStatus: DeploymentStatusType
    environmentName: str
    lastDeploymentAttemptedAt: datetime
    lastDeploymentSucceededAt: datetime
    name: str
    serviceName: str
    templateMajorVersion: str
    templateMinorVersion: str
    templateName: str
    deploymentStatusMessage: Optional[str] = None
    lastAttemptedDeploymentId: Optional[str] = None
    lastClientRequestToken: Optional[str] = None
    lastSucceededDeploymentId: Optional[str] = None
    spec: Optional[str] = None


class CancelServicePipelineDeploymentInput(BaseValidatorModel):
    serviceName: str


class ServicePipeline(BaseValidatorModel):
    arn: str
    createdAt: datetime
    deploymentStatus: DeploymentStatusType
    lastDeploymentAttemptedAt: datetime
    lastDeploymentSucceededAt: datetime
    templateMajorVersion: str
    templateMinorVersion: str
    templateName: str
    deploymentStatusMessage: Optional[str] = None
    lastAttemptedDeploymentId: Optional[str] = None
    lastSucceededDeploymentId: Optional[str] = None
    spec: Optional[str] = None


class CompatibleEnvironmentTemplateInput(BaseValidatorModel):
    majorVersion: str
    templateName: str


class CompatibleEnvironmentTemplate(BaseValidatorModel):
    majorVersion: str
    templateName: str


class ComponentState(BaseValidatorModel):
    serviceInstanceName: Optional[str] = None
    serviceName: Optional[str] = None
    serviceSpec: Optional[str] = None
    templateFile: Optional[str] = None


class ComponentSummary(BaseValidatorModel):
    arn: str
    createdAt: datetime
    deploymentStatus: DeploymentStatusType
    environmentName: str
    lastModifiedAt: datetime
    name: str
    deploymentStatusMessage: Optional[str] = None
    lastAttemptedDeploymentId: Optional[str] = None
    lastDeploymentAttemptedAt: Optional[datetime] = None
    lastDeploymentSucceededAt: Optional[datetime] = None
    lastSucceededDeploymentId: Optional[str] = None
    serviceInstanceName: Optional[str] = None
    serviceName: Optional[str] = None


class ResourceCountsSummary(BaseValidatorModel):
    total: int
    behindMajor: Optional[int] = None
    behindMinor: Optional[int] = None
    failed: Optional[int] = None
    upToDate: Optional[int] = None


class Tag(BaseValidatorModel):
    key: str
    value: str


class RepositoryBranchInput(BaseValidatorModel):
    branch: str
    name: str
    provider: RepositoryProviderType


class EnvironmentTemplate(BaseValidatorModel):
    arn: str
    createdAt: datetime
    lastModifiedAt: datetime
    name: str
    description: Optional[str] = None
    displayName: Optional[str] = None
    encryptionKey: Optional[str] = None
    provisioning: Optional[Literal['CUSTOMER_MANAGED']] = None
    recommendedVersion: Optional[str] = None


class EnvironmentTemplateVersion(BaseValidatorModel):
    arn: str
    createdAt: datetime
    lastModifiedAt: datetime
    majorVersion: str
    minorVersion: str
    status: TemplateVersionStatusType
    templateName: str
    description: Optional[str] = None
    recommendedMinorVersion: Optional[str] = None
    schema: Optional[str] = None
    statusMessage: Optional[str] = None


class Repository(BaseValidatorModel):
    arn: str
    connectionArn: str
    name: str
    provider: RepositoryProviderType
    encryptionKey: Optional[str] = None


class CreateServiceSyncConfigInput(BaseValidatorModel):
    branch: str
    filePath: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    serviceName: str


class ServiceSyncConfig(BaseValidatorModel):
    branch: str
    filePath: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    serviceName: str


class ServiceTemplate(BaseValidatorModel):
    arn: str
    createdAt: datetime
    lastModifiedAt: datetime
    name: str
    description: Optional[str] = None
    displayName: Optional[str] = None
    encryptionKey: Optional[str] = None
    pipelineProvisioning: Optional[Literal['CUSTOMER_MANAGED']] = None
    recommendedVersion: Optional[str] = None


class CreateTemplateSyncConfigInput(BaseValidatorModel):
    branch: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    templateName: str
    templateType: TemplateTypeType
    subdirectory: Optional[str] = None


class TemplateSyncConfig(BaseValidatorModel):
    branch: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    templateName: str
    templateType: TemplateTypeType
    subdirectory: Optional[str] = None


class DeleteComponentInput(BaseValidatorModel):
    name: str


class DeleteDeploymentInput(BaseValidatorModel):
    id: str


class DeleteEnvironmentAccountConnectionInput(BaseValidatorModel):
    id: str


class DeleteEnvironmentInput(BaseValidatorModel):
    name: str


class DeleteEnvironmentTemplateInput(BaseValidatorModel):
    name: str


class DeleteEnvironmentTemplateVersionInput(BaseValidatorModel):
    majorVersion: str
    minorVersion: str
    templateName: str


class DeleteRepositoryInput(BaseValidatorModel):
    name: str
    provider: RepositoryProviderType


class DeleteServiceInput(BaseValidatorModel):
    name: str


class DeleteServiceSyncConfigInput(BaseValidatorModel):
    serviceName: str


class DeleteServiceTemplateInput(BaseValidatorModel):
    name: str


class DeleteServiceTemplateVersionInput(BaseValidatorModel):
    majorVersion: str
    minorVersion: str
    templateName: str


class DeleteTemplateSyncConfigInput(BaseValidatorModel):
    templateName: str
    templateType: TemplateTypeType


class EnvironmentState(BaseValidatorModel):
    templateMajorVersion: str
    templateMinorVersion: str
    templateName: str
    spec: Optional[str] = None


class ServiceInstanceState(BaseValidatorModel):
    spec: str
    templateMajorVersion: str
    templateMinorVersion: str
    templateName: str
    lastSuccessfulComponentDeploymentIds: Optional[List[str]] = None
    lastSuccessfulEnvironmentDeploymentId: Optional[str] = None
    lastSuccessfulServicePipelineDeploymentId: Optional[str] = None


class ServicePipelineState(BaseValidatorModel):
    templateMajorVersion: str
    templateMinorVersion: str
    templateName: str
    spec: Optional[str] = None


class DeploymentSummary(BaseValidatorModel):
    arn: str
    createdAt: datetime
    deploymentStatus: DeploymentStatusType
    environmentName: str
    id: str
    lastModifiedAt: datetime
    targetArn: str
    targetResourceCreatedAt: datetime
    targetResourceType: DeploymentTargetResourceTypeType
    completedAt: Optional[datetime] = None
    componentName: Optional[str] = None
    lastAttemptedDeploymentId: Optional[str] = None
    lastSucceededDeploymentId: Optional[str] = None
    serviceInstanceName: Optional[str] = None
    serviceName: Optional[str] = None


class EnvironmentAccountConnectionSummary(BaseValidatorModel):
    arn: str
    environmentAccountId: str
    environmentName: str
    id: str
    lastModifiedAt: datetime
    managementAccountId: str
    requestedAt: datetime
    roleArn: str
    status: EnvironmentAccountConnectionStatusType
    componentRoleArn: Optional[str] = None


class EnvironmentSummary(BaseValidatorModel):
    arn: str
    createdAt: datetime
    deploymentStatus: DeploymentStatusType
    lastDeploymentAttemptedAt: datetime
    lastDeploymentSucceededAt: datetime
    name: str
    templateMajorVersion: str
    templateMinorVersion: str
    templateName: str
    componentRoleArn: Optional[str] = None
    deploymentStatusMessage: Optional[str] = None
    description: Optional[str] = None
    environmentAccountConnectionId: Optional[str] = None
    environmentAccountId: Optional[str] = None
    lastAttemptedDeploymentId: Optional[str] = None
    lastSucceededDeploymentId: Optional[str] = None
    protonServiceRoleArn: Optional[str] = None
    provisioning: Optional[Literal['CUSTOMER_MANAGED']] = None


class EnvironmentTemplateFilter(BaseValidatorModel):
    majorVersion: str
    templateName: str


class EnvironmentTemplateSummary(BaseValidatorModel):
    arn: str
    createdAt: datetime
    lastModifiedAt: datetime
    name: str
    description: Optional[str] = None
    displayName: Optional[str] = None
    provisioning: Optional[Literal['CUSTOMER_MANAGED']] = None
    recommendedVersion: Optional[str] = None


class EnvironmentTemplateVersionSummary(BaseValidatorModel):
    arn: str
    createdAt: datetime
    lastModifiedAt: datetime
    majorVersion: str
    minorVersion: str
    status: TemplateVersionStatusType
    templateName: str
    description: Optional[str] = None
    recommendedMinorVersion: Optional[str] = None
    statusMessage: Optional[str] = None


class GetComponentInput(BaseValidatorModel):
    name: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class GetDeploymentInput(BaseValidatorModel):
    id: str
    componentName: Optional[str] = None
    environmentName: Optional[str] = None
    serviceInstanceName: Optional[str] = None
    serviceName: Optional[str] = None


class GetEnvironmentAccountConnectionInput(BaseValidatorModel):
    id: str


class GetEnvironmentInput(BaseValidatorModel):
    name: str


class GetEnvironmentTemplateInput(BaseValidatorModel):
    name: str


class GetEnvironmentTemplateVersionInput(BaseValidatorModel):
    majorVersion: str
    minorVersion: str
    templateName: str


class GetRepositoryInput(BaseValidatorModel):
    name: str
    provider: RepositoryProviderType


class GetRepositorySyncStatusInput(BaseValidatorModel):
    branch: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    syncType: SyncTypeType


class GetServiceInput(BaseValidatorModel):
    name: str


class GetServiceInstanceInput(BaseValidatorModel):
    name: str
    serviceName: str


class GetServiceInstanceSyncStatusInput(BaseValidatorModel):
    serviceInstanceName: str
    serviceName: str


class Revision(BaseValidatorModel):
    branch: str
    directory: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    sha: str


class GetServiceSyncBlockerSummaryInput(BaseValidatorModel):
    serviceName: str
    serviceInstanceName: Optional[str] = None


class GetServiceSyncConfigInput(BaseValidatorModel):
    serviceName: str


class GetServiceTemplateInput(BaseValidatorModel):
    name: str


class GetServiceTemplateVersionInput(BaseValidatorModel):
    majorVersion: str
    minorVersion: str
    templateName: str


class GetTemplateSyncConfigInput(BaseValidatorModel):
    templateName: str
    templateType: TemplateTypeType


class GetTemplateSyncStatusInput(BaseValidatorModel):
    templateName: str
    templateType: TemplateTypeType
    templateVersion: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListComponentOutputsInput(BaseValidatorModel):
    componentName: str
    deploymentId: Optional[str] = None
    nextToken: Optional[str] = None


class Output(BaseValidatorModel):
    key: Optional[str] = None
    valueString: Optional[str] = None


class ListComponentProvisionedResourcesInput(BaseValidatorModel):
    componentName: str
    nextToken: Optional[str] = None


class ProvisionedResource(BaseValidatorModel):
    identifier: Optional[str] = None
    name: Optional[str] = None
    provisioningEngine: Optional[ProvisionedResourceEngineType] = None


class ListComponentsInput(BaseValidatorModel):
    environmentName: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    serviceInstanceName: Optional[str] = None
    serviceName: Optional[str] = None


class ListDeploymentsInput(BaseValidatorModel):
    componentName: Optional[str] = None
    environmentName: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    serviceInstanceName: Optional[str] = None
    serviceName: Optional[str] = None


class ListEnvironmentAccountConnectionsInput(BaseValidatorModel):
    requestedBy: EnvironmentAccountConnectionRequesterAccountTypeType
    environmentName: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    statuses: Optional[List[EnvironmentAccountConnectionStatusType]] = None


class ListEnvironmentOutputsInput(BaseValidatorModel):
    environmentName: str
    deploymentId: Optional[str] = None
    nextToken: Optional[str] = None


class ListEnvironmentProvisionedResourcesInput(BaseValidatorModel):
    environmentName: str
    nextToken: Optional[str] = None


class ListEnvironmentTemplateVersionsInput(BaseValidatorModel):
    templateName: str
    majorVersion: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListEnvironmentTemplatesInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListRepositoriesInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class RepositorySummary(BaseValidatorModel):
    arn: str
    connectionArn: str
    name: str
    provider: RepositoryProviderType


class ListRepositorySyncDefinitionsInput(BaseValidatorModel):
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    syncType: SyncTypeType
    nextToken: Optional[str] = None


class RepositorySyncDefinition(BaseValidatorModel):
    branch: str
    directory: str
    parent: str
    target: str


class ListServiceInstanceOutputsInput(BaseValidatorModel):
    serviceInstanceName: str
    serviceName: str
    deploymentId: Optional[str] = None
    nextToken: Optional[str] = None


class ListServiceInstanceProvisionedResourcesInput(BaseValidatorModel):
    serviceInstanceName: str
    serviceName: str
    nextToken: Optional[str] = None


class ListServiceInstancesFilter(BaseValidatorModel):
    key: Optional[ListServiceInstancesFilterByType] = None
    value: Optional[str] = None


class ServiceInstanceSummary(BaseValidatorModel):
    arn: str
    createdAt: datetime
    deploymentStatus: DeploymentStatusType
    environmentName: str
    lastDeploymentAttemptedAt: datetime
    lastDeploymentSucceededAt: datetime
    name: str
    serviceName: str
    templateMajorVersion: str
    templateMinorVersion: str
    templateName: str
    deploymentStatusMessage: Optional[str] = None
    lastAttemptedDeploymentId: Optional[str] = None
    lastSucceededDeploymentId: Optional[str] = None


class ListServicePipelineOutputsInput(BaseValidatorModel):
    serviceName: str
    deploymentId: Optional[str] = None
    nextToken: Optional[str] = None


class ListServicePipelineProvisionedResourcesInput(BaseValidatorModel):
    serviceName: str
    nextToken: Optional[str] = None


class ListServiceTemplateVersionsInput(BaseValidatorModel):
    templateName: str
    majorVersion: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ServiceTemplateVersionSummary(BaseValidatorModel):
    arn: str
    createdAt: datetime
    lastModifiedAt: datetime
    majorVersion: str
    minorVersion: str
    status: TemplateVersionStatusType
    templateName: str
    description: Optional[str] = None
    recommendedMinorVersion: Optional[str] = None
    statusMessage: Optional[str] = None


class ListServiceTemplatesInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ServiceTemplateSummary(BaseValidatorModel):
    arn: str
    createdAt: datetime
    lastModifiedAt: datetime
    name: str
    description: Optional[str] = None
    displayName: Optional[str] = None
    pipelineProvisioning: Optional[Literal['CUSTOMER_MANAGED']] = None
    recommendedVersion: Optional[str] = None


class ListServicesInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ServiceSummary(BaseValidatorModel):
    arn: str
    createdAt: datetime
    lastModifiedAt: datetime
    name: str
    status: ServiceStatusType
    templateName: str
    description: Optional[str] = None
    statusMessage: Optional[str] = None


class ListTagsForResourceInput(BaseValidatorModel):
    resourceArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class RejectEnvironmentAccountConnectionInput(BaseValidatorModel):
    id: str


class RepositorySyncEvent(BaseValidatorModel):
    event: str
    time: datetime
    type: str
    externalId: Optional[str] = None


class ResourceSyncEvent(BaseValidatorModel):
    event: str
    time: datetime
    type: str
    externalId: Optional[str] = None


class S3ObjectSource(BaseValidatorModel):
    bucket: str
    key: str


class SyncBlockerContext(BaseValidatorModel):
    key: str
    value: str


class UntagResourceInput(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class UpdateComponentInput(BaseValidatorModel):
    deploymentType: ComponentDeploymentUpdateTypeType
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    serviceInstanceName: Optional[str] = None
    serviceName: Optional[str] = None
    serviceSpec: Optional[str] = None
    templateFile: Optional[str] = None


class UpdateEnvironmentAccountConnectionInput(BaseValidatorModel):
    id: str
    codebuildRoleArn: Optional[str] = None
    componentRoleArn: Optional[str] = None
    roleArn: Optional[str] = None


class UpdateEnvironmentTemplateInput(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    displayName: Optional[str] = None


class UpdateEnvironmentTemplateVersionInput(BaseValidatorModel):
    majorVersion: str
    minorVersion: str
    templateName: str
    description: Optional[str] = None
    status: Optional[TemplateVersionStatusType] = None


class UpdateServiceInput(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    spec: Optional[str] = None


class UpdateServiceInstanceInput(BaseValidatorModel):
    deploymentType: DeploymentUpdateTypeType
    name: str
    serviceName: str
    clientToken: Optional[str] = None
    spec: Optional[str] = None
    templateMajorVersion: Optional[str] = None
    templateMinorVersion: Optional[str] = None


class UpdateServicePipelineInput(BaseValidatorModel):
    deploymentType: DeploymentUpdateTypeType
    serviceName: str
    spec: str
    templateMajorVersion: Optional[str] = None
    templateMinorVersion: Optional[str] = None


class UpdateServiceSyncBlockerInput(BaseValidatorModel):
    id: str
    resolvedReason: str


class UpdateServiceSyncConfigInput(BaseValidatorModel):
    branch: str
    filePath: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    serviceName: str


class UpdateServiceTemplateInput(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    displayName: Optional[str] = None


class UpdateTemplateSyncConfigInput(BaseValidatorModel):
    branch: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    templateName: str
    templateType: TemplateTypeType
    subdirectory: Optional[str] = None


class AcceptEnvironmentAccountConnectionOutput(BaseValidatorModel):
    environmentAccountConnection: EnvironmentAccountConnection
    ResponseMetadata: ResponseMetadata


class CreateEnvironmentAccountConnectionOutput(BaseValidatorModel):
    environmentAccountConnection: EnvironmentAccountConnection
    ResponseMetadata: ResponseMetadata


class DeleteEnvironmentAccountConnectionOutput(BaseValidatorModel):
    environmentAccountConnection: EnvironmentAccountConnection
    ResponseMetadata: ResponseMetadata


class GetEnvironmentAccountConnectionOutput(BaseValidatorModel):
    environmentAccountConnection: EnvironmentAccountConnection
    ResponseMetadata: ResponseMetadata


class RejectEnvironmentAccountConnectionOutput(BaseValidatorModel):
    environmentAccountConnection: EnvironmentAccountConnection
    ResponseMetadata: ResponseMetadata


class UpdateEnvironmentAccountConnectionOutput(BaseValidatorModel):
    environmentAccountConnection: EnvironmentAccountConnection
    ResponseMetadata: ResponseMetadata


class AccountSettings(BaseValidatorModel):
    pipelineCodebuildRoleArn: Optional[str] = None
    pipelineProvisioningRepository: Optional[RepositoryBranch] = None
    pipelineServiceRoleArn: Optional[str] = None


class Environment(BaseValidatorModel):
    arn: str
    createdAt: datetime
    deploymentStatus: DeploymentStatusType
    lastDeploymentAttemptedAt: datetime
    lastDeploymentSucceededAt: datetime
    name: str
    templateMajorVersion: str
    templateMinorVersion: str
    templateName: str
    codebuildRoleArn: Optional[str] = None
    componentRoleArn: Optional[str] = None
    deploymentStatusMessage: Optional[str] = None
    description: Optional[str] = None
    environmentAccountConnectionId: Optional[str] = None
    environmentAccountId: Optional[str] = None
    lastAttemptedDeploymentId: Optional[str] = None
    lastSucceededDeploymentId: Optional[str] = None
    protonServiceRoleArn: Optional[str] = None
    provisioning: Optional[Literal['CUSTOMER_MANAGED']] = None
    provisioningRepository: Optional[RepositoryBranch] = None
    spec: Optional[str] = None


class CancelComponentDeploymentOutput(BaseValidatorModel):
    component: Component
    ResponseMetadata: ResponseMetadata


class CreateComponentOutput(BaseValidatorModel):
    component: Component
    ResponseMetadata: ResponseMetadata


class DeleteComponentOutput(BaseValidatorModel):
    component: Component
    ResponseMetadata: ResponseMetadata


class GetComponentOutput(BaseValidatorModel):
    component: Component
    ResponseMetadata: ResponseMetadata


class UpdateComponentOutput(BaseValidatorModel):
    component: Component
    ResponseMetadata: ResponseMetadata


class CancelServiceInstanceDeploymentOutput(BaseValidatorModel):
    serviceInstance: ServiceInstance
    ResponseMetadata: ResponseMetadata


class CreateServiceInstanceOutput(BaseValidatorModel):
    serviceInstance: ServiceInstance
    ResponseMetadata: ResponseMetadata


class GetServiceInstanceOutput(BaseValidatorModel):
    serviceInstance: ServiceInstance
    ResponseMetadata: ResponseMetadata


class UpdateServiceInstanceOutput(BaseValidatorModel):
    serviceInstance: ServiceInstance
    ResponseMetadata: ResponseMetadata


class CancelServicePipelineDeploymentOutput(BaseValidatorModel):
    pipeline: ServicePipeline
    ResponseMetadata: ResponseMetadata


class Service(BaseValidatorModel):
    arn: str
    createdAt: datetime
    lastModifiedAt: datetime
    name: str
    spec: str
    status: ServiceStatusType
    templateName: str
    branchName: Optional[str] = None
    description: Optional[str] = None
    pipeline: Optional[ServicePipeline] = None
    repositoryConnectionArn: Optional[str] = None
    repositoryId: Optional[str] = None
    statusMessage: Optional[str] = None


class UpdateServicePipelineOutput(BaseValidatorModel):
    pipeline: ServicePipeline
    ResponseMetadata: ResponseMetadata


class UpdateServiceTemplateVersionInput(BaseValidatorModel):
    majorVersion: str
    minorVersion: str
    templateName: str
    compatibleEnvironmentTemplates: Optional[List[CompatibleEnvironmentTemplateInput]] = None
    description: Optional[str] = None
    status: Optional[TemplateVersionStatusType] = None
    supportedComponentSources: Optional[List[Literal['DIRECTLY_DEFINED']]] = None


class ServiceTemplateVersion(BaseValidatorModel):
    arn: str
    compatibleEnvironmentTemplates: List[CompatibleEnvironmentTemplate]
    createdAt: datetime
    lastModifiedAt: datetime
    majorVersion: str
    minorVersion: str
    status: TemplateVersionStatusType
    templateName: str
    description: Optional[str] = None
    recommendedMinorVersion: Optional[str] = None
    schema: Optional[str] = None
    statusMessage: Optional[str] = None
    supportedComponentSources: Optional[List[Literal['DIRECTLY_DEFINED']]] = None


class ListComponentsOutput(BaseValidatorModel):
    components: List[ComponentSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CountsSummary(BaseValidatorModel):
    components: Optional[ResourceCountsSummary] = None
    environmentTemplates: Optional[ResourceCountsSummary] = None
    environments: Optional[ResourceCountsSummary] = None
    pipelines: Optional[ResourceCountsSummary] = None
    serviceInstances: Optional[ResourceCountsSummary] = None
    serviceTemplates: Optional[ResourceCountsSummary] = None
    services: Optional[ResourceCountsSummary] = None


class CreateComponentInput(BaseValidatorModel):
    manifest: str
    name: str
    templateFile: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    environmentName: Optional[str] = None
    serviceInstanceName: Optional[str] = None
    serviceName: Optional[str] = None
    serviceSpec: Optional[str] = None
    tags: Optional[List[Tag]] = None


class CreateEnvironmentAccountConnectionInput(BaseValidatorModel):
    environmentName: str
    managementAccountId: str
    clientToken: Optional[str] = None
    codebuildRoleArn: Optional[str] = None
    componentRoleArn: Optional[str] = None
    roleArn: Optional[str] = None
    tags: Optional[List[Tag]] = None


class CreateEnvironmentTemplateInput(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    displayName: Optional[str] = None
    encryptionKey: Optional[str] = None
    provisioning: Optional[Literal['CUSTOMER_MANAGED']] = None
    tags: Optional[List[Tag]] = None


class CreateRepositoryInput(BaseValidatorModel):
    connectionArn: str
    name: str
    provider: RepositoryProviderType
    encryptionKey: Optional[str] = None
    tags: Optional[List[Tag]] = None


class CreateServiceInput(BaseValidatorModel):
    name: str
    spec: str
    templateMajorVersion: str
    templateName: str
    branchName: Optional[str] = None
    description: Optional[str] = None
    repositoryConnectionArn: Optional[str] = None
    repositoryId: Optional[str] = None
    tags: Optional[List[Tag]] = None
    templateMinorVersion: Optional[str] = None


class CreateServiceInstanceInput(BaseValidatorModel):
    name: str
    serviceName: str
    spec: str
    clientToken: Optional[str] = None
    tags: Optional[List[Tag]] = None
    templateMajorVersion: Optional[str] = None
    templateMinorVersion: Optional[str] = None


class CreateServiceTemplateInput(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    displayName: Optional[str] = None
    encryptionKey: Optional[str] = None
    pipelineProvisioning: Optional[Literal['CUSTOMER_MANAGED']] = None
    tags: Optional[List[Tag]] = None


class ListTagsForResourceOutput(BaseValidatorModel):
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class TagResourceInput(BaseValidatorModel):
    resourceArn: str
    tags: List[Tag]


class CreateEnvironmentInput(BaseValidatorModel):
    name: str
    spec: str
    templateMajorVersion: str
    templateName: str
    codebuildRoleArn: Optional[str] = None
    componentRoleArn: Optional[str] = None
    description: Optional[str] = None
    environmentAccountConnectionId: Optional[str] = None
    protonServiceRoleArn: Optional[str] = None
    provisioningRepository: Optional[RepositoryBranchInput] = None
    tags: Optional[List[Tag]] = None
    templateMinorVersion: Optional[str] = None


class UpdateAccountSettingsInput(BaseValidatorModel):
    deletePipelineProvisioningRepository: Optional[bool] = None
    pipelineCodebuildRoleArn: Optional[str] = None
    pipelineProvisioningRepository: Optional[RepositoryBranchInput] = None
    pipelineServiceRoleArn: Optional[str] = None


class UpdateEnvironmentInput(BaseValidatorModel):
    deploymentType: DeploymentUpdateTypeType
    name: str
    codebuildRoleArn: Optional[str] = None
    componentRoleArn: Optional[str] = None
    description: Optional[str] = None
    environmentAccountConnectionId: Optional[str] = None
    protonServiceRoleArn: Optional[str] = None
    provisioningRepository: Optional[RepositoryBranchInput] = None
    spec: Optional[str] = None
    templateMajorVersion: Optional[str] = None
    templateMinorVersion: Optional[str] = None


class CreateEnvironmentTemplateOutput(BaseValidatorModel):
    environmentTemplate: EnvironmentTemplate
    ResponseMetadata: ResponseMetadata


class DeleteEnvironmentTemplateOutput(BaseValidatorModel):
    environmentTemplate: EnvironmentTemplate
    ResponseMetadata: ResponseMetadata


class GetEnvironmentTemplateOutput(BaseValidatorModel):
    environmentTemplate: EnvironmentTemplate
    ResponseMetadata: ResponseMetadata


class UpdateEnvironmentTemplateOutput(BaseValidatorModel):
    environmentTemplate: EnvironmentTemplate
    ResponseMetadata: ResponseMetadata


class CreateEnvironmentTemplateVersionOutput(BaseValidatorModel):
    environmentTemplateVersion: EnvironmentTemplateVersion
    ResponseMetadata: ResponseMetadata


class DeleteEnvironmentTemplateVersionOutput(BaseValidatorModel):
    environmentTemplateVersion: EnvironmentTemplateVersion
    ResponseMetadata: ResponseMetadata


class GetEnvironmentTemplateVersionOutput(BaseValidatorModel):
    environmentTemplateVersion: EnvironmentTemplateVersion
    ResponseMetadata: ResponseMetadata


class UpdateEnvironmentTemplateVersionOutput(BaseValidatorModel):
    environmentTemplateVersion: EnvironmentTemplateVersion
    ResponseMetadata: ResponseMetadata


class CreateRepositoryOutput(BaseValidatorModel):
    repository: Repository
    ResponseMetadata: ResponseMetadata


class DeleteRepositoryOutput(BaseValidatorModel):
    repository: Repository
    ResponseMetadata: ResponseMetadata


class GetRepositoryOutput(BaseValidatorModel):
    repository: Repository
    ResponseMetadata: ResponseMetadata


class CreateServiceSyncConfigOutput(BaseValidatorModel):
    serviceSyncConfig: ServiceSyncConfig
    ResponseMetadata: ResponseMetadata


class DeleteServiceSyncConfigOutput(BaseValidatorModel):
    serviceSyncConfig: ServiceSyncConfig
    ResponseMetadata: ResponseMetadata


class GetServiceSyncConfigOutput(BaseValidatorModel):
    serviceSyncConfig: ServiceSyncConfig
    ResponseMetadata: ResponseMetadata


class UpdateServiceSyncConfigOutput(BaseValidatorModel):
    serviceSyncConfig: ServiceSyncConfig
    ResponseMetadata: ResponseMetadata


class CreateServiceTemplateOutput(BaseValidatorModel):
    serviceTemplate: ServiceTemplate
    ResponseMetadata: ResponseMetadata


class DeleteServiceTemplateOutput(BaseValidatorModel):
    serviceTemplate: ServiceTemplate
    ResponseMetadata: ResponseMetadata


class GetServiceTemplateOutput(BaseValidatorModel):
    serviceTemplate: ServiceTemplate
    ResponseMetadata: ResponseMetadata


class UpdateServiceTemplateOutput(BaseValidatorModel):
    serviceTemplate: ServiceTemplate
    ResponseMetadata: ResponseMetadata


class CreateTemplateSyncConfigOutput(BaseValidatorModel):
    templateSyncConfig: TemplateSyncConfig
    ResponseMetadata: ResponseMetadata


class DeleteTemplateSyncConfigOutput(BaseValidatorModel):
    templateSyncConfig: TemplateSyncConfig
    ResponseMetadata: ResponseMetadata


class GetTemplateSyncConfigOutput(BaseValidatorModel):
    templateSyncConfig: TemplateSyncConfig
    ResponseMetadata: ResponseMetadata


class UpdateTemplateSyncConfigOutput(BaseValidatorModel):
    templateSyncConfig: TemplateSyncConfig
    ResponseMetadata: ResponseMetadata


class DeploymentState(BaseValidatorModel):
    component: Optional[ComponentState] = None
    environment: Optional[EnvironmentState] = None
    serviceInstance: Optional[ServiceInstanceState] = None
    servicePipeline: Optional[ServicePipelineState] = None


class ListDeploymentsOutput(BaseValidatorModel):
    deployments: List[DeploymentSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListEnvironmentAccountConnectionsOutput(BaseValidatorModel):
    environmentAccountConnections: List[EnvironmentAccountConnectionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListEnvironmentsOutput(BaseValidatorModel):
    environments: List[EnvironmentSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListEnvironmentsInput(BaseValidatorModel):
    environmentTemplates: Optional[List[EnvironmentTemplateFilter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListEnvironmentTemplatesOutput(BaseValidatorModel):
    templates: List[EnvironmentTemplateSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListEnvironmentTemplateVersionsOutput(BaseValidatorModel):
    templateVersions: List[EnvironmentTemplateVersionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetComponentInputWaitExtra(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetComponentInputWait(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetEnvironmentInputWait(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetEnvironmentTemplateVersionInputWait(BaseValidatorModel):
    majorVersion: str
    minorVersion: str
    templateName: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetServiceInputWaitExtraExtraExtra(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetServiceInputWaitExtraExtra(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetServiceInputWaitExtra(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetServiceInputWait(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetServiceInstanceInputWait(BaseValidatorModel):
    name: str
    serviceName: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetServiceTemplateVersionInputWait(BaseValidatorModel):
    majorVersion: str
    minorVersion: str
    templateName: str
    WaiterConfig: Optional[WaiterConfig] = None


class ListComponentOutputsInputPaginate(BaseValidatorModel):
    componentName: str
    deploymentId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListComponentProvisionedResourcesInputPaginate(BaseValidatorModel):
    componentName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListComponentsInputPaginate(BaseValidatorModel):
    environmentName: Optional[str] = None
    serviceInstanceName: Optional[str] = None
    serviceName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDeploymentsInputPaginate(BaseValidatorModel):
    componentName: Optional[str] = None
    environmentName: Optional[str] = None
    serviceInstanceName: Optional[str] = None
    serviceName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEnvironmentAccountConnectionsInputPaginate(BaseValidatorModel):
    requestedBy: EnvironmentAccountConnectionRequesterAccountTypeType
    environmentName: Optional[str] = None
    statuses: Optional[List[EnvironmentAccountConnectionStatusType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEnvironmentOutputsInputPaginate(BaseValidatorModel):
    environmentName: str
    deploymentId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEnvironmentProvisionedResourcesInputPaginate(BaseValidatorModel):
    environmentName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEnvironmentTemplateVersionsInputPaginate(BaseValidatorModel):
    templateName: str
    majorVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEnvironmentTemplatesInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEnvironmentsInputPaginate(BaseValidatorModel):
    environmentTemplates: Optional[List[EnvironmentTemplateFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRepositoriesInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRepositorySyncDefinitionsInputPaginate(BaseValidatorModel):
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    syncType: SyncTypeType
    PaginationConfig: Optional[PaginatorConfig] = None


class ListServiceInstanceOutputsInputPaginate(BaseValidatorModel):
    serviceInstanceName: str
    serviceName: str
    deploymentId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListServiceInstanceProvisionedResourcesInputPaginate(BaseValidatorModel):
    serviceInstanceName: str
    serviceName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListServicePipelineOutputsInputPaginate(BaseValidatorModel):
    serviceName: str
    deploymentId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListServicePipelineProvisionedResourcesInputPaginate(BaseValidatorModel):
    serviceName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListServiceTemplateVersionsInputPaginate(BaseValidatorModel):
    templateName: str
    majorVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListServiceTemplatesInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListServicesInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTagsForResourceInputPaginate(BaseValidatorModel):
    resourceArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListComponentOutputsOutput(BaseValidatorModel):
    outputs: List[Output]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListEnvironmentOutputsOutput(BaseValidatorModel):
    outputs: List[Output]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListServiceInstanceOutputsOutput(BaseValidatorModel):
    outputs: List[Output]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListServicePipelineOutputsOutput(BaseValidatorModel):
    outputs: List[Output]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class NotifyResourceDeploymentStatusChangeInput(BaseValidatorModel):
    resourceArn: str
    deploymentId: Optional[str] = None
    outputs: Optional[List[Output]] = None
    status: Optional[ResourceDeploymentStatusType] = None
    statusMessage: Optional[str] = None


class ListComponentProvisionedResourcesOutput(BaseValidatorModel):
    provisionedResources: List[ProvisionedResource]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListEnvironmentProvisionedResourcesOutput(BaseValidatorModel):
    provisionedResources: List[ProvisionedResource]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListServiceInstanceProvisionedResourcesOutput(BaseValidatorModel):
    provisionedResources: List[ProvisionedResource]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListServicePipelineProvisionedResourcesOutput(BaseValidatorModel):
    provisionedResources: List[ProvisionedResource]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListRepositoriesOutput(BaseValidatorModel):
    repositories: List[RepositorySummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListRepositorySyncDefinitionsOutput(BaseValidatorModel):
    syncDefinitions: List[RepositorySyncDefinition]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListServiceInstancesInputPaginate(BaseValidatorModel):
    filters: Optional[List[ListServiceInstancesFilter]] = None
    serviceName: Optional[str] = None
    sortBy: Optional[ListServiceInstancesSortByType] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListServiceInstancesInput(BaseValidatorModel):
    filters: Optional[List[ListServiceInstancesFilter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    serviceName: Optional[str] = None
    sortBy: Optional[ListServiceInstancesSortByType] = None
    sortOrder: Optional[SortOrderType] = None


class ListServiceInstancesOutput(BaseValidatorModel):
    serviceInstances: List[ServiceInstanceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListServiceTemplateVersionsOutput(BaseValidatorModel):
    templateVersions: List[ServiceTemplateVersionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListServiceTemplatesOutput(BaseValidatorModel):
    templates: List[ServiceTemplateSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListServicesOutput(BaseValidatorModel):
    services: List[ServiceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class RepositorySyncAttempt(BaseValidatorModel):
    events: List[RepositorySyncEvent]
    startedAt: datetime
    status: RepositorySyncStatusType


class ResourceSyncAttempt(BaseValidatorModel):
    events: List[ResourceSyncEvent]
    initialRevision: Revision
    startedAt: datetime
    status: ResourceSyncStatusType
    target: str
    targetRevision: Revision


class TemplateVersionSourceInput(BaseValidatorModel):
    s3: Optional[S3ObjectSource] = None


class SyncBlocker(BaseValidatorModel):
    createdAt: datetime
    createdReason: str
    id: str
    status: BlockerStatusType
    type: Literal['AUTOMATED']
    contexts: Optional[List[SyncBlockerContext]] = None
    resolvedAt: Optional[datetime] = None
    resolvedReason: Optional[str] = None


class GetAccountSettingsOutput(BaseValidatorModel):
    accountSettings: AccountSettings
    ResponseMetadata: ResponseMetadata


class UpdateAccountSettingsOutput(BaseValidatorModel):
    accountSettings: AccountSettings
    ResponseMetadata: ResponseMetadata


class CancelEnvironmentDeploymentOutput(BaseValidatorModel):
    environment: Environment
    ResponseMetadata: ResponseMetadata


class CreateEnvironmentOutput(BaseValidatorModel):
    environment: Environment
    ResponseMetadata: ResponseMetadata


class DeleteEnvironmentOutput(BaseValidatorModel):
    environment: Environment
    ResponseMetadata: ResponseMetadata


class GetEnvironmentOutput(BaseValidatorModel):
    environment: Environment
    ResponseMetadata: ResponseMetadata


class UpdateEnvironmentOutput(BaseValidatorModel):
    environment: Environment
    ResponseMetadata: ResponseMetadata


class CreateServiceOutput(BaseValidatorModel):
    service: Service
    ResponseMetadata: ResponseMetadata


class DeleteServiceOutput(BaseValidatorModel):
    service: Service
    ResponseMetadata: ResponseMetadata


class GetServiceOutput(BaseValidatorModel):
    service: Service
    ResponseMetadata: ResponseMetadata


class UpdateServiceOutput(BaseValidatorModel):
    service: Service
    ResponseMetadata: ResponseMetadata


class CreateServiceTemplateVersionOutput(BaseValidatorModel):
    serviceTemplateVersion: ServiceTemplateVersion
    ResponseMetadata: ResponseMetadata


class DeleteServiceTemplateVersionOutput(BaseValidatorModel):
    serviceTemplateVersion: ServiceTemplateVersion
    ResponseMetadata: ResponseMetadata


class GetServiceTemplateVersionOutput(BaseValidatorModel):
    serviceTemplateVersion: ServiceTemplateVersion
    ResponseMetadata: ResponseMetadata


class UpdateServiceTemplateVersionOutput(BaseValidatorModel):
    serviceTemplateVersion: ServiceTemplateVersion
    ResponseMetadata: ResponseMetadata


class GetResourcesSummaryOutput(BaseValidatorModel):
    counts: CountsSummary
    ResponseMetadata: ResponseMetadata


class Deployment(BaseValidatorModel):
    arn: str
    createdAt: datetime
    deploymentStatus: DeploymentStatusType
    environmentName: str
    id: str
    lastModifiedAt: datetime
    targetArn: str
    targetResourceCreatedAt: datetime
    targetResourceType: DeploymentTargetResourceTypeType
    completedAt: Optional[datetime] = None
    componentName: Optional[str] = None
    deploymentStatusMessage: Optional[str] = None
    initialState: Optional[DeploymentState] = None
    lastAttemptedDeploymentId: Optional[str] = None
    lastSucceededDeploymentId: Optional[str] = None
    serviceInstanceName: Optional[str] = None
    serviceName: Optional[str] = None
    targetState: Optional[DeploymentState] = None


class GetRepositorySyncStatusOutput(BaseValidatorModel):
    latestSync: RepositorySyncAttempt
    ResponseMetadata: ResponseMetadata


class GetServiceInstanceSyncStatusOutput(BaseValidatorModel):
    desiredState: Revision
    latestSuccessfulSync: ResourceSyncAttempt
    latestSync: ResourceSyncAttempt
    ResponseMetadata: ResponseMetadata


class GetTemplateSyncStatusOutput(BaseValidatorModel):
    desiredState: Revision
    latestSuccessfulSync: ResourceSyncAttempt
    latestSync: ResourceSyncAttempt
    ResponseMetadata: ResponseMetadata


class CreateEnvironmentTemplateVersionInput(BaseValidatorModel):
    source: TemplateVersionSourceInput
    templateName: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    majorVersion: Optional[str] = None
    tags: Optional[List[Tag]] = None


class CreateServiceTemplateVersionInput(BaseValidatorModel):
    compatibleEnvironmentTemplates: List[CompatibleEnvironmentTemplateInput]
    source: TemplateVersionSourceInput
    templateName: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    majorVersion: Optional[str] = None
    supportedComponentSources: Optional[List[Literal['DIRECTLY_DEFINED']]] = None
    tags: Optional[List[Tag]] = None


class ServiceSyncBlockerSummary(BaseValidatorModel):
    serviceName: str
    latestBlockers: Optional[List[SyncBlocker]] = None
    serviceInstanceName: Optional[str] = None


class UpdateServiceSyncBlockerOutput(BaseValidatorModel):
    serviceInstanceName: str
    serviceName: str
    serviceSyncBlocker: SyncBlocker
    ResponseMetadata: ResponseMetadata


class DeleteDeploymentOutput(BaseValidatorModel):
    deployment: Deployment
    ResponseMetadata: ResponseMetadata


class GetDeploymentOutput(BaseValidatorModel):
    deployment: Deployment
    ResponseMetadata: ResponseMetadata


class GetServiceSyncBlockerSummaryOutput(BaseValidatorModel):
    serviceSyncBlockerSummary: ServiceSyncBlockerSummary
    ResponseMetadata: ResponseMetadata
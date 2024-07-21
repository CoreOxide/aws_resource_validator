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
from aws_resource_validator.pydantic_models.proton_constants import *

class AcceptEnvironmentAccountConnectionInputRequestTypeDef(BaseModel):
    id: str

class EnvironmentAccountConnectionTypeDef(BaseModel):
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

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class RepositoryBranchTypeDef(BaseModel):
    arn: str
    branch: str
    name: str
    provider: RepositoryProviderType

class CancelComponentDeploymentInputRequestTypeDef(BaseModel):
    componentName: str

class ComponentTypeDef(BaseModel):
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

class CancelEnvironmentDeploymentInputRequestTypeDef(BaseModel):
    environmentName: str

class CancelServiceInstanceDeploymentInputRequestTypeDef(BaseModel):
    serviceInstanceName: str
    serviceName: str

class ServiceInstanceTypeDef(BaseModel):
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

class CancelServicePipelineDeploymentInputRequestTypeDef(BaseModel):
    serviceName: str

class ServicePipelineTypeDef(BaseModel):
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

class CompatibleEnvironmentTemplateInputTypeDef(BaseModel):
    majorVersion: str
    templateName: str

class CompatibleEnvironmentTemplateTypeDef(BaseModel):
    majorVersion: str
    templateName: str

class ComponentStateTypeDef(BaseModel):
    serviceInstanceName: Optional[str] = None
    serviceName: Optional[str] = None
    serviceSpec: Optional[str] = None
    templateFile: Optional[str] = None

class ComponentSummaryTypeDef(BaseModel):
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

class ResourceCountsSummaryTypeDef(BaseModel):
    total: int
    behindMajor: Optional[int] = None
    behindMinor: Optional[int] = None
    failed: Optional[int] = None
    upToDate: Optional[int] = None

class TagTypeDef(BaseModel):
    key: str
    value: str

class RepositoryBranchInputTypeDef(BaseModel):
    branch: str
    name: str
    provider: RepositoryProviderType

class EnvironmentTemplateTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    lastModifiedAt: datetime
    name: str
    description: Optional[str] = None
    displayName: Optional[str] = None
    encryptionKey: Optional[str] = None
    provisioning: Optional[Literal["CUSTOMER_MANAGED"]] = None
    recommendedVersion: Optional[str] = None

class EnvironmentTemplateVersionTypeDef(BaseModel):
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

class RepositoryTypeDef(BaseModel):
    arn: str
    connectionArn: str
    name: str
    provider: RepositoryProviderType
    encryptionKey: Optional[str] = None

class CreateServiceSyncConfigInputRequestTypeDef(BaseModel):
    branch: str
    filePath: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    serviceName: str

class ServiceSyncConfigTypeDef(BaseModel):
    branch: str
    filePath: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    serviceName: str

class ServiceTemplateTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    lastModifiedAt: datetime
    name: str
    description: Optional[str] = None
    displayName: Optional[str] = None
    encryptionKey: Optional[str] = None
    pipelineProvisioning: Optional[Literal["CUSTOMER_MANAGED"]] = None
    recommendedVersion: Optional[str] = None

class CreateTemplateSyncConfigInputRequestTypeDef(BaseModel):
    branch: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    templateName: str
    templateType: TemplateTypeType
    subdirectory: Optional[str] = None

class TemplateSyncConfigTypeDef(BaseModel):
    branch: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    templateName: str
    templateType: TemplateTypeType
    subdirectory: Optional[str] = None

class DeleteComponentInputRequestTypeDef(BaseModel):
    name: str

class DeleteDeploymentInputRequestTypeDef(BaseModel):
    id: str

class DeleteEnvironmentAccountConnectionInputRequestTypeDef(BaseModel):
    id: str

class DeleteEnvironmentInputRequestTypeDef(BaseModel):
    name: str

class DeleteEnvironmentTemplateInputRequestTypeDef(BaseModel):
    name: str

class DeleteEnvironmentTemplateVersionInputRequestTypeDef(BaseModel):
    majorVersion: str
    minorVersion: str
    templateName: str

class DeleteRepositoryInputRequestTypeDef(BaseModel):
    name: str
    provider: RepositoryProviderType

class DeleteServiceInputRequestTypeDef(BaseModel):
    name: str

class DeleteServiceSyncConfigInputRequestTypeDef(BaseModel):
    serviceName: str

class DeleteServiceTemplateInputRequestTypeDef(BaseModel):
    name: str

class DeleteServiceTemplateVersionInputRequestTypeDef(BaseModel):
    majorVersion: str
    minorVersion: str
    templateName: str

class DeleteTemplateSyncConfigInputRequestTypeDef(BaseModel):
    templateName: str
    templateType: TemplateTypeType

class EnvironmentStateTypeDef(BaseModel):
    templateMajorVersion: str
    templateMinorVersion: str
    templateName: str
    spec: Optional[str] = None

class ServiceInstanceStateTypeDef(BaseModel):
    spec: str
    templateMajorVersion: str
    templateMinorVersion: str
    templateName: str
    lastSuccessfulComponentDeploymentIds: Optional[List[str]] = None
    lastSuccessfulEnvironmentDeploymentId: Optional[str] = None
    lastSuccessfulServicePipelineDeploymentId: Optional[str] = None

class ServicePipelineStateTypeDef(BaseModel):
    templateMajorVersion: str
    templateMinorVersion: str
    templateName: str
    spec: Optional[str] = None

class DeploymentSummaryTypeDef(BaseModel):
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

class EnvironmentAccountConnectionSummaryTypeDef(BaseModel):
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

class EnvironmentSummaryTypeDef(BaseModel):
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
    provisioning: Optional[Literal["CUSTOMER_MANAGED"]] = None

class EnvironmentTemplateFilterTypeDef(BaseModel):
    majorVersion: str
    templateName: str

class EnvironmentTemplateSummaryTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    lastModifiedAt: datetime
    name: str
    description: Optional[str] = None
    displayName: Optional[str] = None
    provisioning: Optional[Literal["CUSTOMER_MANAGED"]] = None
    recommendedVersion: Optional[str] = None

class EnvironmentTemplateVersionSummaryTypeDef(BaseModel):
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

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class GetComponentInputRequestTypeDef(BaseModel):
    name: str

class GetDeploymentInputRequestTypeDef(BaseModel):
    id: str
    componentName: Optional[str] = None
    environmentName: Optional[str] = None
    serviceInstanceName: Optional[str] = None
    serviceName: Optional[str] = None

class GetEnvironmentAccountConnectionInputRequestTypeDef(BaseModel):
    id: str

class GetEnvironmentInputRequestTypeDef(BaseModel):
    name: str

class GetEnvironmentTemplateInputRequestTypeDef(BaseModel):
    name: str

class GetEnvironmentTemplateVersionInputRequestTypeDef(BaseModel):
    majorVersion: str
    minorVersion: str
    templateName: str

class GetRepositoryInputRequestTypeDef(BaseModel):
    name: str
    provider: RepositoryProviderType

class GetRepositorySyncStatusInputRequestTypeDef(BaseModel):
    branch: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    syncType: SyncTypeType

class GetServiceInputRequestTypeDef(BaseModel):
    name: str

class GetServiceInstanceInputRequestTypeDef(BaseModel):
    name: str
    serviceName: str

class GetServiceInstanceSyncStatusInputRequestTypeDef(BaseModel):
    serviceInstanceName: str
    serviceName: str

class RevisionTypeDef(BaseModel):
    branch: str
    directory: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    sha: str

class GetServiceSyncBlockerSummaryInputRequestTypeDef(BaseModel):
    serviceName: str
    serviceInstanceName: Optional[str] = None

class GetServiceSyncConfigInputRequestTypeDef(BaseModel):
    serviceName: str

class GetServiceTemplateInputRequestTypeDef(BaseModel):
    name: str

class GetServiceTemplateVersionInputRequestTypeDef(BaseModel):
    majorVersion: str
    minorVersion: str
    templateName: str

class GetTemplateSyncConfigInputRequestTypeDef(BaseModel):
    templateName: str
    templateType: TemplateTypeType

class GetTemplateSyncStatusInputRequestTypeDef(BaseModel):
    templateName: str
    templateType: TemplateTypeType
    templateVersion: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListComponentOutputsInputRequestTypeDef(BaseModel):
    componentName: str
    deploymentId: Optional[str] = None
    nextToken: Optional[str] = None

class OutputTypeDef(BaseModel):
    key: Optional[str] = None
    valueString: Optional[str] = None

class ListComponentProvisionedResourcesInputRequestTypeDef(BaseModel):
    componentName: str
    nextToken: Optional[str] = None

class ProvisionedResourceTypeDef(BaseModel):
    identifier: Optional[str] = None
    name: Optional[str] = None
    provisioningEngine: Optional[ProvisionedResourceEngineType] = None

class ListComponentsInputRequestTypeDef(BaseModel):
    environmentName: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    serviceInstanceName: Optional[str] = None
    serviceName: Optional[str] = None

class ListDeploymentsInputRequestTypeDef(BaseModel):
    componentName: Optional[str] = None
    environmentName: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    serviceInstanceName: Optional[str] = None
    serviceName: Optional[str] = None

class ListEnvironmentAccountConnectionsInputRequestTypeDef(BaseModel):
    requestedBy: EnvironmentAccountConnectionRequesterAccountTypeType
    environmentName: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    statuses: Optional[Sequence[EnvironmentAccountConnectionStatusType]] = None

class ListEnvironmentOutputsInputRequestTypeDef(BaseModel):
    environmentName: str
    deploymentId: Optional[str] = None
    nextToken: Optional[str] = None

class ListEnvironmentProvisionedResourcesInputRequestTypeDef(BaseModel):
    environmentName: str
    nextToken: Optional[str] = None

class ListEnvironmentTemplateVersionsInputRequestTypeDef(BaseModel):
    templateName: str
    majorVersion: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListEnvironmentTemplatesInputRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListRepositoriesInputRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class RepositorySummaryTypeDef(BaseModel):
    arn: str
    connectionArn: str
    name: str
    provider: RepositoryProviderType

class ListRepositorySyncDefinitionsInputRequestTypeDef(BaseModel):
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    syncType: SyncTypeType
    nextToken: Optional[str] = None

class RepositorySyncDefinitionTypeDef(BaseModel):
    branch: str
    directory: str
    parent: str
    target: str

class ListServiceInstanceOutputsInputRequestTypeDef(BaseModel):
    serviceInstanceName: str
    serviceName: str
    deploymentId: Optional[str] = None
    nextToken: Optional[str] = None

class ListServiceInstanceProvisionedResourcesInputRequestTypeDef(BaseModel):
    serviceInstanceName: str
    serviceName: str
    nextToken: Optional[str] = None

class ListServiceInstancesFilterTypeDef(BaseModel):
    key: Optional[ListServiceInstancesFilterByType] = None
    value: Optional[str] = None

class ServiceInstanceSummaryTypeDef(BaseModel):
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

class ListServicePipelineOutputsInputRequestTypeDef(BaseModel):
    serviceName: str
    deploymentId: Optional[str] = None
    nextToken: Optional[str] = None

class ListServicePipelineProvisionedResourcesInputRequestTypeDef(BaseModel):
    serviceName: str
    nextToken: Optional[str] = None

class ListServiceTemplateVersionsInputRequestTypeDef(BaseModel):
    templateName: str
    majorVersion: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ServiceTemplateVersionSummaryTypeDef(BaseModel):
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

class ListServiceTemplatesInputRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ServiceTemplateSummaryTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    lastModifiedAt: datetime
    name: str
    description: Optional[str] = None
    displayName: Optional[str] = None
    pipelineProvisioning: Optional[Literal["CUSTOMER_MANAGED"]] = None
    recommendedVersion: Optional[str] = None

class ListServicesInputRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ServiceSummaryTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    lastModifiedAt: datetime
    name: str
    status: ServiceStatusType
    templateName: str
    description: Optional[str] = None
    statusMessage: Optional[str] = None

class ListTagsForResourceInputRequestTypeDef(BaseModel):
    resourceArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class RejectEnvironmentAccountConnectionInputRequestTypeDef(BaseModel):
    id: str

class RepositorySyncEventTypeDef(BaseModel):
    event: str
    time: datetime
    type: str
    externalId: Optional[str] = None

class ResourceSyncEventTypeDef(BaseModel):
    event: str
    time: datetime
    type: str
    externalId: Optional[str] = None

class S3ObjectSourceTypeDef(BaseModel):
    bucket: str
    key: str

class SyncBlockerContextTypeDef(BaseModel):
    key: str
    value: str

class UntagResourceInputRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateComponentInputRequestTypeDef(BaseModel):
    deploymentType: ComponentDeploymentUpdateTypeType
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    serviceInstanceName: Optional[str] = None
    serviceName: Optional[str] = None
    serviceSpec: Optional[str] = None
    templateFile: Optional[str] = None

class UpdateEnvironmentAccountConnectionInputRequestTypeDef(BaseModel):
    id: str
    codebuildRoleArn: Optional[str] = None
    componentRoleArn: Optional[str] = None
    roleArn: Optional[str] = None

class UpdateEnvironmentTemplateInputRequestTypeDef(BaseModel):
    name: str
    description: Optional[str] = None
    displayName: Optional[str] = None

class UpdateEnvironmentTemplateVersionInputRequestTypeDef(BaseModel):
    majorVersion: str
    minorVersion: str
    templateName: str
    description: Optional[str] = None
    status: Optional[TemplateVersionStatusType] = None

class UpdateServiceInputRequestTypeDef(BaseModel):
    name: str
    description: Optional[str] = None
    spec: Optional[str] = None

class UpdateServiceInstanceInputRequestTypeDef(BaseModel):
    deploymentType: DeploymentUpdateTypeType
    name: str
    serviceName: str
    clientToken: Optional[str] = None
    spec: Optional[str] = None
    templateMajorVersion: Optional[str] = None
    templateMinorVersion: Optional[str] = None

class UpdateServicePipelineInputRequestTypeDef(BaseModel):
    deploymentType: DeploymentUpdateTypeType
    serviceName: str
    spec: str
    templateMajorVersion: Optional[str] = None
    templateMinorVersion: Optional[str] = None

class UpdateServiceSyncBlockerInputRequestTypeDef(BaseModel):
    id: str
    resolvedReason: str

class UpdateServiceSyncConfigInputRequestTypeDef(BaseModel):
    branch: str
    filePath: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    serviceName: str

class UpdateServiceTemplateInputRequestTypeDef(BaseModel):
    name: str
    description: Optional[str] = None
    displayName: Optional[str] = None

class UpdateTemplateSyncConfigInputRequestTypeDef(BaseModel):
    branch: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    templateName: str
    templateType: TemplateTypeType
    subdirectory: Optional[str] = None

class AcceptEnvironmentAccountConnectionOutputTypeDef(BaseModel):
    environmentAccountConnection: EnvironmentAccountConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEnvironmentAccountConnectionOutputTypeDef(BaseModel):
    environmentAccountConnection: EnvironmentAccountConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEnvironmentAccountConnectionOutputTypeDef(BaseModel):
    environmentAccountConnection: EnvironmentAccountConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetEnvironmentAccountConnectionOutputTypeDef(BaseModel):
    environmentAccountConnection: EnvironmentAccountConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RejectEnvironmentAccountConnectionOutputTypeDef(BaseModel):
    environmentAccountConnection: EnvironmentAccountConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEnvironmentAccountConnectionOutputTypeDef(BaseModel):
    environmentAccountConnection: EnvironmentAccountConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AccountSettingsTypeDef(BaseModel):
    pipelineCodebuildRoleArn: Optional[str] = None
    pipelineProvisioningRepository: Optional[RepositoryBranchTypeDef] = None
    pipelineServiceRoleArn: Optional[str] = None

class EnvironmentTypeDef(BaseModel):
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
    provisioning: Optional[Literal["CUSTOMER_MANAGED"]] = None
    provisioningRepository: Optional[RepositoryBranchTypeDef] = None
    spec: Optional[str] = None

class CancelComponentDeploymentOutputTypeDef(BaseModel):
    component: ComponentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateComponentOutputTypeDef(BaseModel):
    component: ComponentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteComponentOutputTypeDef(BaseModel):
    component: ComponentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetComponentOutputTypeDef(BaseModel):
    component: ComponentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateComponentOutputTypeDef(BaseModel):
    component: ComponentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CancelServiceInstanceDeploymentOutputTypeDef(BaseModel):
    serviceInstance: ServiceInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServiceInstanceOutputTypeDef(BaseModel):
    serviceInstance: ServiceInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceInstanceOutputTypeDef(BaseModel):
    serviceInstance: ServiceInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceInstanceOutputTypeDef(BaseModel):
    serviceInstance: ServiceInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CancelServicePipelineDeploymentOutputTypeDef(BaseModel):
    pipeline: ServicePipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ServiceTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    lastModifiedAt: datetime
    name: str
    spec: str
    status: ServiceStatusType
    templateName: str
    branchName: Optional[str] = None
    description: Optional[str] = None
    pipeline: Optional[ServicePipelineTypeDef] = None
    repositoryConnectionArn: Optional[str] = None
    repositoryId: Optional[str] = None
    statusMessage: Optional[str] = None

class UpdateServicePipelineOutputTypeDef(BaseModel):
    pipeline: ServicePipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceTemplateVersionInputRequestTypeDef(BaseModel):
    majorVersion: str
    minorVersion: str
    templateName: str
    compatibleEnvironmentTemplates: Optional[       Sequence[CompatibleEnvironmentTemplateInputTypeDef]     ] = None
    description: Optional[str] = None
    status: Optional[TemplateVersionStatusType] = None
    supportedComponentSources: Optional[Sequence[Literal["DIRECTLY_DEFINED"]]] = None

class ServiceTemplateVersionTypeDef(BaseModel):
    arn: str
    compatibleEnvironmentTemplates: List[CompatibleEnvironmentTemplateTypeDef]
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
    supportedComponentSources: Optional[List[Literal["DIRECTLY_DEFINED"]]] = None

class ListComponentsOutputTypeDef(BaseModel):
    components: List[ComponentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CountsSummaryTypeDef(BaseModel):
    components: Optional[ResourceCountsSummaryTypeDef] = None
    environmentTemplates: Optional[ResourceCountsSummaryTypeDef] = None
    environments: Optional[ResourceCountsSummaryTypeDef] = None
    pipelines: Optional[ResourceCountsSummaryTypeDef] = None
    serviceInstances: Optional[ResourceCountsSummaryTypeDef] = None
    serviceTemplates: Optional[ResourceCountsSummaryTypeDef] = None
    services: Optional[ResourceCountsSummaryTypeDef] = None

class CreateComponentInputRequestTypeDef(BaseModel):
    manifest: str
    name: str
    templateFile: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    environmentName: Optional[str] = None
    serviceInstanceName: Optional[str] = None
    serviceName: Optional[str] = None
    serviceSpec: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateEnvironmentAccountConnectionInputRequestTypeDef(BaseModel):
    environmentName: str
    managementAccountId: str
    clientToken: Optional[str] = None
    codebuildRoleArn: Optional[str] = None
    componentRoleArn: Optional[str] = None
    roleArn: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateEnvironmentTemplateInputRequestTypeDef(BaseModel):
    name: str
    description: Optional[str] = None
    displayName: Optional[str] = None
    encryptionKey: Optional[str] = None
    provisioning: Optional[Literal["CUSTOMER_MANAGED"]] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateRepositoryInputRequestTypeDef(BaseModel):
    connectionArn: str
    name: str
    provider: RepositoryProviderType
    encryptionKey: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateServiceInputRequestTypeDef(BaseModel):
    name: str
    spec: str
    templateMajorVersion: str
    templateName: str
    branchName: Optional[str] = None
    description: Optional[str] = None
    repositoryConnectionArn: Optional[str] = None
    repositoryId: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    templateMinorVersion: Optional[str] = None

class CreateServiceInstanceInputRequestTypeDef(BaseModel):
    name: str
    serviceName: str
    spec: str
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    templateMajorVersion: Optional[str] = None
    templateMinorVersion: Optional[str] = None

class CreateServiceTemplateInputRequestTypeDef(BaseModel):
    name: str
    description: Optional[str] = None
    displayName: Optional[str] = None
    encryptionKey: Optional[str] = None
    pipelineProvisioning: Optional[Literal["CUSTOMER_MANAGED"]] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceOutputTypeDef(BaseModel):
    nextToken: str
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceInputRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class CreateEnvironmentInputRequestTypeDef(BaseModel):
    name: str
    spec: str
    templateMajorVersion: str
    templateName: str
    codebuildRoleArn: Optional[str] = None
    componentRoleArn: Optional[str] = None
    description: Optional[str] = None
    environmentAccountConnectionId: Optional[str] = None
    protonServiceRoleArn: Optional[str] = None
    provisioningRepository: Optional[RepositoryBranchInputTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    templateMinorVersion: Optional[str] = None

class UpdateAccountSettingsInputRequestTypeDef(BaseModel):
    deletePipelineProvisioningRepository: Optional[bool] = None
    pipelineCodebuildRoleArn: Optional[str] = None
    pipelineProvisioningRepository: Optional[RepositoryBranchInputTypeDef] = None
    pipelineServiceRoleArn: Optional[str] = None

class UpdateEnvironmentInputRequestTypeDef(BaseModel):
    deploymentType: DeploymentUpdateTypeType
    name: str
    codebuildRoleArn: Optional[str] = None
    componentRoleArn: Optional[str] = None
    description: Optional[str] = None
    environmentAccountConnectionId: Optional[str] = None
    protonServiceRoleArn: Optional[str] = None
    provisioningRepository: Optional[RepositoryBranchInputTypeDef] = None
    spec: Optional[str] = None
    templateMajorVersion: Optional[str] = None
    templateMinorVersion: Optional[str] = None

class CreateEnvironmentTemplateOutputTypeDef(BaseModel):
    environmentTemplate: EnvironmentTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEnvironmentTemplateOutputTypeDef(BaseModel):
    environmentTemplate: EnvironmentTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetEnvironmentTemplateOutputTypeDef(BaseModel):
    environmentTemplate: EnvironmentTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEnvironmentTemplateOutputTypeDef(BaseModel):
    environmentTemplate: EnvironmentTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEnvironmentTemplateVersionOutputTypeDef(BaseModel):
    environmentTemplateVersion: EnvironmentTemplateVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEnvironmentTemplateVersionOutputTypeDef(BaseModel):
    environmentTemplateVersion: EnvironmentTemplateVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetEnvironmentTemplateVersionOutputTypeDef(BaseModel):
    environmentTemplateVersion: EnvironmentTemplateVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEnvironmentTemplateVersionOutputTypeDef(BaseModel):
    environmentTemplateVersion: EnvironmentTemplateVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRepositoryOutputTypeDef(BaseModel):
    repository: RepositoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRepositoryOutputTypeDef(BaseModel):
    repository: RepositoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRepositoryOutputTypeDef(BaseModel):
    repository: RepositoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServiceSyncConfigOutputTypeDef(BaseModel):
    serviceSyncConfig: ServiceSyncConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteServiceSyncConfigOutputTypeDef(BaseModel):
    serviceSyncConfig: ServiceSyncConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceSyncConfigOutputTypeDef(BaseModel):
    serviceSyncConfig: ServiceSyncConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceSyncConfigOutputTypeDef(BaseModel):
    serviceSyncConfig: ServiceSyncConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServiceTemplateOutputTypeDef(BaseModel):
    serviceTemplate: ServiceTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteServiceTemplateOutputTypeDef(BaseModel):
    serviceTemplate: ServiceTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceTemplateOutputTypeDef(BaseModel):
    serviceTemplate: ServiceTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceTemplateOutputTypeDef(BaseModel):
    serviceTemplate: ServiceTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTemplateSyncConfigOutputTypeDef(BaseModel):
    templateSyncConfig: TemplateSyncConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTemplateSyncConfigOutputTypeDef(BaseModel):
    templateSyncConfig: TemplateSyncConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTemplateSyncConfigOutputTypeDef(BaseModel):
    templateSyncConfig: TemplateSyncConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTemplateSyncConfigOutputTypeDef(BaseModel):
    templateSyncConfig: TemplateSyncConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeploymentStateTypeDef(BaseModel):
    component: Optional[ComponentStateTypeDef] = None
    environment: Optional[EnvironmentStateTypeDef] = None
    serviceInstance: Optional[ServiceInstanceStateTypeDef] = None
    servicePipeline: Optional[ServicePipelineStateTypeDef] = None

class ListDeploymentsOutputTypeDef(BaseModel):
    deployments: List[DeploymentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnvironmentAccountConnectionsOutputTypeDef(BaseModel):
    environmentAccountConnections: List[EnvironmentAccountConnectionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnvironmentsOutputTypeDef(BaseModel):
    environments: List[EnvironmentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnvironmentsInputRequestTypeDef(BaseModel):
    environmentTemplates: Optional[Sequence[EnvironmentTemplateFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListEnvironmentTemplatesOutputTypeDef(BaseModel):
    nextToken: str
    templates: List[EnvironmentTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnvironmentTemplateVersionsOutputTypeDef(BaseModel):
    nextToken: str
    templateVersions: List[EnvironmentTemplateVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetComponentInputComponentDeletedWaitTypeDef(BaseModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetComponentInputComponentDeployedWaitTypeDef(BaseModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetEnvironmentInputEnvironmentDeployedWaitTypeDef(BaseModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetEnvironmentTemplateVersionInputEnvironmentTemplateVersionRegisteredWaitTypeDef(BaseModel):
    majorVersion: str
    minorVersion: str
    templateName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetServiceInputServiceCreatedWaitTypeDef(BaseModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetServiceInputServiceDeletedWaitTypeDef(BaseModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetServiceInputServicePipelineDeployedWaitTypeDef(BaseModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetServiceInputServiceUpdatedWaitTypeDef(BaseModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetServiceInstanceInputServiceInstanceDeployedWaitTypeDef(BaseModel):
    name: str
    serviceName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetServiceTemplateVersionInputServiceTemplateVersionRegisteredWaitTypeDef(BaseModel):
    majorVersion: str
    minorVersion: str
    templateName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class ListComponentOutputsInputListComponentOutputsPaginateTypeDef(BaseModel):
    componentName: str
    deploymentId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListComponentProvisionedResourcesInputListComponentProvisionedResourcesPaginateTypeDef(BaseModel):
    componentName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListComponentsInputListComponentsPaginateTypeDef(BaseModel):
    environmentName: Optional[str] = None
    serviceInstanceName: Optional[str] = None
    serviceName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeploymentsInputListDeploymentsPaginateTypeDef(BaseModel):
    componentName: Optional[str] = None
    environmentName: Optional[str] = None
    serviceInstanceName: Optional[str] = None
    serviceName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEnvironmentAccountConnectionsInputListEnvironmentAccountConnectionsPaginateTypeDef(BaseModel):
    requestedBy: EnvironmentAccountConnectionRequesterAccountTypeType
    environmentName: Optional[str] = None
    statuses: Optional[Sequence[EnvironmentAccountConnectionStatusType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEnvironmentOutputsInputListEnvironmentOutputsPaginateTypeDef(BaseModel):
    environmentName: str
    deploymentId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEnvironmentProvisionedResourcesInputListEnvironmentProvisionedResourcesPaginateTypeDef(BaseModel):
    environmentName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEnvironmentTemplateVersionsInputListEnvironmentTemplateVersionsPaginateTypeDef(BaseModel):
    templateName: str
    majorVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEnvironmentTemplatesInputListEnvironmentTemplatesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEnvironmentsInputListEnvironmentsPaginateTypeDef(BaseModel):
    environmentTemplates: Optional[Sequence[EnvironmentTemplateFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRepositoriesInputListRepositoriesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRepositorySyncDefinitionsInputListRepositorySyncDefinitionsPaginateTypeDef(BaseModel):
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    syncType: SyncTypeType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServiceInstanceOutputsInputListServiceInstanceOutputsPaginateTypeDef(BaseModel):
    serviceInstanceName: str
    serviceName: str
    deploymentId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServiceInstanceProvisionedResourcesInputListServiceInstanceProvisionedResourcesPaginateTypeDef(BaseModel):
    serviceInstanceName: str
    serviceName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServicePipelineOutputsInputListServicePipelineOutputsPaginateTypeDef(BaseModel):
    serviceName: str
    deploymentId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServicePipelineProvisionedResourcesInputListServicePipelineProvisionedResourcesPaginateTypeDef(BaseModel):
    serviceName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServiceTemplateVersionsInputListServiceTemplateVersionsPaginateTypeDef(BaseModel):
    templateName: str
    majorVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServiceTemplatesInputListServiceTemplatesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServicesInputListServicesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceInputListTagsForResourcePaginateTypeDef(BaseModel):
    resourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListComponentOutputsOutputTypeDef(BaseModel):
    nextToken: str
    outputs: List[OutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnvironmentOutputsOutputTypeDef(BaseModel):
    nextToken: str
    outputs: List[OutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListServiceInstanceOutputsOutputTypeDef(BaseModel):
    nextToken: str
    outputs: List[OutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListServicePipelineOutputsOutputTypeDef(BaseModel):
    nextToken: str
    outputs: List[OutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class NotifyResourceDeploymentStatusChangeInputRequestTypeDef(BaseModel):
    resourceArn: str
    deploymentId: Optional[str] = None
    outputs: Optional[Sequence[OutputTypeDef]] = None
    status: Optional[ResourceDeploymentStatusType] = None
    statusMessage: Optional[str] = None

class ListComponentProvisionedResourcesOutputTypeDef(BaseModel):
    nextToken: str
    provisionedResources: List[ProvisionedResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnvironmentProvisionedResourcesOutputTypeDef(BaseModel):
    nextToken: str
    provisionedResources: List[ProvisionedResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListServiceInstanceProvisionedResourcesOutputTypeDef(BaseModel):
    nextToken: str
    provisionedResources: List[ProvisionedResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListServicePipelineProvisionedResourcesOutputTypeDef(BaseModel):
    nextToken: str
    provisionedResources: List[ProvisionedResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRepositoriesOutputTypeDef(BaseModel):
    nextToken: str
    repositories: List[RepositorySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRepositorySyncDefinitionsOutputTypeDef(BaseModel):
    nextToken: str
    syncDefinitions: List[RepositorySyncDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListServiceInstancesInputListServiceInstancesPaginateTypeDef(BaseModel):
    filters: Optional[Sequence[ListServiceInstancesFilterTypeDef]] = None
    serviceName: Optional[str] = None
    sortBy: Optional[ListServiceInstancesSortByType] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServiceInstancesInputRequestTypeDef(BaseModel):
    filters: Optional[Sequence[ListServiceInstancesFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    serviceName: Optional[str] = None
    sortBy: Optional[ListServiceInstancesSortByType] = None
    sortOrder: Optional[SortOrderType] = None

class ListServiceInstancesOutputTypeDef(BaseModel):
    nextToken: str
    serviceInstances: List[ServiceInstanceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListServiceTemplateVersionsOutputTypeDef(BaseModel):
    nextToken: str
    templateVersions: List[ServiceTemplateVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListServiceTemplatesOutputTypeDef(BaseModel):
    nextToken: str
    templates: List[ServiceTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListServicesOutputTypeDef(BaseModel):
    nextToken: str
    services: List[ServiceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RepositorySyncAttemptTypeDef(BaseModel):
    events: List[RepositorySyncEventTypeDef]
    startedAt: datetime
    status: RepositorySyncStatusType

class ResourceSyncAttemptTypeDef(BaseModel):
    events: List[ResourceSyncEventTypeDef]
    initialRevision: RevisionTypeDef
    startedAt: datetime
    status: ResourceSyncStatusType
    target: str
    targetRevision: RevisionTypeDef

class TemplateVersionSourceInputTypeDef(BaseModel):
    s3: Optional[S3ObjectSourceTypeDef] = None

class SyncBlockerTypeDef(BaseModel):
    createdAt: datetime
    createdReason: str
    id: str
    status: BlockerStatusType
    type: Literal["AUTOMATED"]
    contexts: Optional[List[SyncBlockerContextTypeDef]] = None
    resolvedAt: Optional[datetime] = None
    resolvedReason: Optional[str] = None

class GetAccountSettingsOutputTypeDef(BaseModel):
    accountSettings: AccountSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccountSettingsOutputTypeDef(BaseModel):
    accountSettings: AccountSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CancelEnvironmentDeploymentOutputTypeDef(BaseModel):
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEnvironmentOutputTypeDef(BaseModel):
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEnvironmentOutputTypeDef(BaseModel):
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetEnvironmentOutputTypeDef(BaseModel):
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEnvironmentOutputTypeDef(BaseModel):
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServiceOutputTypeDef(BaseModel):
    service: ServiceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteServiceOutputTypeDef(BaseModel):
    service: ServiceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceOutputTypeDef(BaseModel):
    service: ServiceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceOutputTypeDef(BaseModel):
    service: ServiceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServiceTemplateVersionOutputTypeDef(BaseModel):
    serviceTemplateVersion: ServiceTemplateVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteServiceTemplateVersionOutputTypeDef(BaseModel):
    serviceTemplateVersion: ServiceTemplateVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceTemplateVersionOutputTypeDef(BaseModel):
    serviceTemplateVersion: ServiceTemplateVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceTemplateVersionOutputTypeDef(BaseModel):
    serviceTemplateVersion: ServiceTemplateVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcesSummaryOutputTypeDef(BaseModel):
    counts: CountsSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeploymentTypeDef(BaseModel):
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
    initialState: Optional[DeploymentStateTypeDef] = None
    lastAttemptedDeploymentId: Optional[str] = None
    lastSucceededDeploymentId: Optional[str] = None
    serviceInstanceName: Optional[str] = None
    serviceName: Optional[str] = None
    targetState: Optional[DeploymentStateTypeDef] = None

class GetRepositorySyncStatusOutputTypeDef(BaseModel):
    latestSync: RepositorySyncAttemptTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceInstanceSyncStatusOutputTypeDef(BaseModel):
    desiredState: RevisionTypeDef
    latestSuccessfulSync: ResourceSyncAttemptTypeDef
    latestSync: ResourceSyncAttemptTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTemplateSyncStatusOutputTypeDef(BaseModel):
    desiredState: RevisionTypeDef
    latestSuccessfulSync: ResourceSyncAttemptTypeDef
    latestSync: ResourceSyncAttemptTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEnvironmentTemplateVersionInputRequestTypeDef(BaseModel):
    source: TemplateVersionSourceInputTypeDef
    templateName: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    majorVersion: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateServiceTemplateVersionInputRequestTypeDef(BaseModel):
    compatibleEnvironmentTemplates: Sequence[CompatibleEnvironmentTemplateInputTypeDef]
    source: TemplateVersionSourceInputTypeDef
    templateName: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    majorVersion: Optional[str] = None
    supportedComponentSources: Optional[Sequence[Literal["DIRECTLY_DEFINED"]]] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class ServiceSyncBlockerSummaryTypeDef(BaseModel):
    serviceName: str
    latestBlockers: Optional[List[SyncBlockerTypeDef]] = None
    serviceInstanceName: Optional[str] = None

class UpdateServiceSyncBlockerOutputTypeDef(BaseModel):
    serviceInstanceName: str
    serviceName: str
    serviceSyncBlocker: SyncBlockerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDeploymentOutputTypeDef(BaseModel):
    deployment: DeploymentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeploymentOutputTypeDef(BaseModel):
    deployment: DeploymentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceSyncBlockerSummaryOutputTypeDef(BaseModel):
    serviceSyncBlockerSummary: ServiceSyncBlockerSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


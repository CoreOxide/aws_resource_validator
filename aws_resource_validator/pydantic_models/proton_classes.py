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
from aws_resource_validator.pydantic_models.proton_constants import *

class AcceptEnvironmentAccountConnectionInputRequestTypeDef(BaseValidatorModel):
    id: str

class EnvironmentAccountConnectionTypeDef(BaseValidatorModel):
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

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class RepositoryBranchTypeDef(BaseValidatorModel):
    arn: str
    branch: str
    name: str
    provider: RepositoryProviderType

class CancelComponentDeploymentInputRequestTypeDef(BaseValidatorModel):
    componentName: str

class ComponentTypeDef(BaseValidatorModel):
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

class CancelEnvironmentDeploymentInputRequestTypeDef(BaseValidatorModel):
    environmentName: str

class CancelServiceInstanceDeploymentInputRequestTypeDef(BaseValidatorModel):
    serviceInstanceName: str
    serviceName: str

class ServiceInstanceTypeDef(BaseValidatorModel):
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

class CancelServicePipelineDeploymentInputRequestTypeDef(BaseValidatorModel):
    serviceName: str

class ServicePipelineTypeDef(BaseValidatorModel):
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

class CompatibleEnvironmentTemplateInputTypeDef(BaseValidatorModel):
    majorVersion: str
    templateName: str

class CompatibleEnvironmentTemplateTypeDef(BaseValidatorModel):
    majorVersion: str
    templateName: str

class ComponentStateTypeDef(BaseValidatorModel):
    serviceInstanceName: Optional[str] = None
    serviceName: Optional[str] = None
    serviceSpec: Optional[str] = None
    templateFile: Optional[str] = None

class ComponentSummaryTypeDef(BaseValidatorModel):
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

class ResourceCountsSummaryTypeDef(BaseValidatorModel):
    total: int
    behindMajor: Optional[int] = None
    behindMinor: Optional[int] = None
    failed: Optional[int] = None
    upToDate: Optional[int] = None

class TagTypeDef(BaseValidatorModel):
    key: str
    value: str

class RepositoryBranchInputTypeDef(BaseValidatorModel):
    branch: str
    name: str
    provider: RepositoryProviderType

class EnvironmentTemplateTypeDef(BaseValidatorModel):
    arn: str
    createdAt: datetime
    lastModifiedAt: datetime
    name: str
    description: Optional[str] = None
    displayName: Optional[str] = None
    encryptionKey: Optional[str] = None
    provisioning: Optional[Literal["CUSTOMER_MANAGED"]] = None
    recommendedVersion: Optional[str] = None

class EnvironmentTemplateVersionTypeDef(BaseValidatorModel):
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

class RepositoryTypeDef(BaseValidatorModel):
    arn: str
    connectionArn: str
    name: str
    provider: RepositoryProviderType
    encryptionKey: Optional[str] = None

class CreateServiceSyncConfigInputRequestTypeDef(BaseValidatorModel):
    branch: str
    filePath: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    serviceName: str

class ServiceSyncConfigTypeDef(BaseValidatorModel):
    branch: str
    filePath: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    serviceName: str

class ServiceTemplateTypeDef(BaseValidatorModel):
    arn: str
    createdAt: datetime
    lastModifiedAt: datetime
    name: str
    description: Optional[str] = None
    displayName: Optional[str] = None
    encryptionKey: Optional[str] = None
    pipelineProvisioning: Optional[Literal["CUSTOMER_MANAGED"]] = None
    recommendedVersion: Optional[str] = None

class CreateTemplateSyncConfigInputRequestTypeDef(BaseValidatorModel):
    branch: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    templateName: str
    templateType: TemplateTypeType
    subdirectory: Optional[str] = None

class TemplateSyncConfigTypeDef(BaseValidatorModel):
    branch: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    templateName: str
    templateType: TemplateTypeType
    subdirectory: Optional[str] = None

class DeleteComponentInputRequestTypeDef(BaseValidatorModel):
    name: str

class DeleteDeploymentInputRequestTypeDef(BaseValidatorModel):
    id: str

class DeleteEnvironmentAccountConnectionInputRequestTypeDef(BaseValidatorModel):
    id: str

class DeleteEnvironmentInputRequestTypeDef(BaseValidatorModel):
    name: str

class DeleteEnvironmentTemplateInputRequestTypeDef(BaseValidatorModel):
    name: str

class DeleteEnvironmentTemplateVersionInputRequestTypeDef(BaseValidatorModel):
    majorVersion: str
    minorVersion: str
    templateName: str

class DeleteRepositoryInputRequestTypeDef(BaseValidatorModel):
    name: str
    provider: RepositoryProviderType

class DeleteServiceInputRequestTypeDef(BaseValidatorModel):
    name: str

class DeleteServiceSyncConfigInputRequestTypeDef(BaseValidatorModel):
    serviceName: str

class DeleteServiceTemplateInputRequestTypeDef(BaseValidatorModel):
    name: str

class DeleteServiceTemplateVersionInputRequestTypeDef(BaseValidatorModel):
    majorVersion: str
    minorVersion: str
    templateName: str

class DeleteTemplateSyncConfigInputRequestTypeDef(BaseValidatorModel):
    templateName: str
    templateType: TemplateTypeType

class EnvironmentStateTypeDef(BaseValidatorModel):
    templateMajorVersion: str
    templateMinorVersion: str
    templateName: str
    spec: Optional[str] = None

class ServiceInstanceStateTypeDef(BaseValidatorModel):
    spec: str
    templateMajorVersion: str
    templateMinorVersion: str
    templateName: str
    lastSuccessfulComponentDeploymentIds: Optional[List[str]] = None
    lastSuccessfulEnvironmentDeploymentId: Optional[str] = None
    lastSuccessfulServicePipelineDeploymentId: Optional[str] = None

class ServicePipelineStateTypeDef(BaseValidatorModel):
    templateMajorVersion: str
    templateMinorVersion: str
    templateName: str
    spec: Optional[str] = None

class DeploymentSummaryTypeDef(BaseValidatorModel):
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

class EnvironmentAccountConnectionSummaryTypeDef(BaseValidatorModel):
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

class EnvironmentSummaryTypeDef(BaseValidatorModel):
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

class EnvironmentTemplateFilterTypeDef(BaseValidatorModel):
    majorVersion: str
    templateName: str

class EnvironmentTemplateSummaryTypeDef(BaseValidatorModel):
    arn: str
    createdAt: datetime
    lastModifiedAt: datetime
    name: str
    description: Optional[str] = None
    displayName: Optional[str] = None
    provisioning: Optional[Literal["CUSTOMER_MANAGED"]] = None
    recommendedVersion: Optional[str] = None

class EnvironmentTemplateVersionSummaryTypeDef(BaseValidatorModel):
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

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class GetComponentInputRequestTypeDef(BaseValidatorModel):
    name: str

class GetDeploymentInputRequestTypeDef(BaseValidatorModel):
    id: str
    componentName: Optional[str] = None
    environmentName: Optional[str] = None
    serviceInstanceName: Optional[str] = None
    serviceName: Optional[str] = None

class GetEnvironmentAccountConnectionInputRequestTypeDef(BaseValidatorModel):
    id: str

class GetEnvironmentInputRequestTypeDef(BaseValidatorModel):
    name: str

class GetEnvironmentTemplateInputRequestTypeDef(BaseValidatorModel):
    name: str

class GetEnvironmentTemplateVersionInputRequestTypeDef(BaseValidatorModel):
    majorVersion: str
    minorVersion: str
    templateName: str

class GetRepositoryInputRequestTypeDef(BaseValidatorModel):
    name: str
    provider: RepositoryProviderType

class GetRepositorySyncStatusInputRequestTypeDef(BaseValidatorModel):
    branch: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    syncType: SyncTypeType

class GetServiceInputRequestTypeDef(BaseValidatorModel):
    name: str

class GetServiceInstanceInputRequestTypeDef(BaseValidatorModel):
    name: str
    serviceName: str

class GetServiceInstanceSyncStatusInputRequestTypeDef(BaseValidatorModel):
    serviceInstanceName: str
    serviceName: str

class RevisionTypeDef(BaseValidatorModel):
    branch: str
    directory: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    sha: str

class GetServiceSyncBlockerSummaryInputRequestTypeDef(BaseValidatorModel):
    serviceName: str
    serviceInstanceName: Optional[str] = None

class GetServiceSyncConfigInputRequestTypeDef(BaseValidatorModel):
    serviceName: str

class GetServiceTemplateInputRequestTypeDef(BaseValidatorModel):
    name: str

class GetServiceTemplateVersionInputRequestTypeDef(BaseValidatorModel):
    majorVersion: str
    minorVersion: str
    templateName: str

class GetTemplateSyncConfigInputRequestTypeDef(BaseValidatorModel):
    templateName: str
    templateType: TemplateTypeType

class GetTemplateSyncStatusInputRequestTypeDef(BaseValidatorModel):
    templateName: str
    templateType: TemplateTypeType
    templateVersion: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListComponentOutputsInputRequestTypeDef(BaseValidatorModel):
    componentName: str
    deploymentId: Optional[str] = None
    nextToken: Optional[str] = None

class OutputTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    valueString: Optional[str] = None

class ListComponentProvisionedResourcesInputRequestTypeDef(BaseValidatorModel):
    componentName: str
    nextToken: Optional[str] = None

class ProvisionedResourceTypeDef(BaseValidatorModel):
    identifier: Optional[str] = None
    name: Optional[str] = None
    provisioningEngine: Optional[ProvisionedResourceEngineType] = None

class ListComponentsInputRequestTypeDef(BaseValidatorModel):
    environmentName: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    serviceInstanceName: Optional[str] = None
    serviceName: Optional[str] = None

class ListDeploymentsInputRequestTypeDef(BaseValidatorModel):
    componentName: Optional[str] = None
    environmentName: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    serviceInstanceName: Optional[str] = None
    serviceName: Optional[str] = None

class ListEnvironmentAccountConnectionsInputRequestTypeDef(BaseValidatorModel):
    requestedBy: EnvironmentAccountConnectionRequesterAccountTypeType
    environmentName: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    statuses: Optional[Sequence[EnvironmentAccountConnectionStatusType]] = None

class ListEnvironmentOutputsInputRequestTypeDef(BaseValidatorModel):
    environmentName: str
    deploymentId: Optional[str] = None
    nextToken: Optional[str] = None

class ListEnvironmentProvisionedResourcesInputRequestTypeDef(BaseValidatorModel):
    environmentName: str
    nextToken: Optional[str] = None

class ListEnvironmentTemplateVersionsInputRequestTypeDef(BaseValidatorModel):
    templateName: str
    majorVersion: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListEnvironmentTemplatesInputRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListRepositoriesInputRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class RepositorySummaryTypeDef(BaseValidatorModel):
    arn: str
    connectionArn: str
    name: str
    provider: RepositoryProviderType

class ListRepositorySyncDefinitionsInputRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    syncType: SyncTypeType
    nextToken: Optional[str] = None

class RepositorySyncDefinitionTypeDef(BaseValidatorModel):
    branch: str
    directory: str
    parent: str
    target: str

class ListServiceInstanceOutputsInputRequestTypeDef(BaseValidatorModel):
    serviceInstanceName: str
    serviceName: str
    deploymentId: Optional[str] = None
    nextToken: Optional[str] = None

class ListServiceInstanceProvisionedResourcesInputRequestTypeDef(BaseValidatorModel):
    serviceInstanceName: str
    serviceName: str
    nextToken: Optional[str] = None

class ListServiceInstancesFilterTypeDef(BaseValidatorModel):
    key: Optional[ListServiceInstancesFilterByType] = None
    value: Optional[str] = None

class ServiceInstanceSummaryTypeDef(BaseValidatorModel):
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

class ListServicePipelineOutputsInputRequestTypeDef(BaseValidatorModel):
    serviceName: str
    deploymentId: Optional[str] = None
    nextToken: Optional[str] = None

class ListServicePipelineProvisionedResourcesInputRequestTypeDef(BaseValidatorModel):
    serviceName: str
    nextToken: Optional[str] = None

class ListServiceTemplateVersionsInputRequestTypeDef(BaseValidatorModel):
    templateName: str
    majorVersion: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ServiceTemplateVersionSummaryTypeDef(BaseValidatorModel):
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

class ListServiceTemplatesInputRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ServiceTemplateSummaryTypeDef(BaseValidatorModel):
    arn: str
    createdAt: datetime
    lastModifiedAt: datetime
    name: str
    description: Optional[str] = None
    displayName: Optional[str] = None
    pipelineProvisioning: Optional[Literal["CUSTOMER_MANAGED"]] = None
    recommendedVersion: Optional[str] = None

class ListServicesInputRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ServiceSummaryTypeDef(BaseValidatorModel):
    arn: str
    createdAt: datetime
    lastModifiedAt: datetime
    name: str
    status: ServiceStatusType
    templateName: str
    description: Optional[str] = None
    statusMessage: Optional[str] = None

class ListTagsForResourceInputRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class RejectEnvironmentAccountConnectionInputRequestTypeDef(BaseValidatorModel):
    id: str

class RepositorySyncEventTypeDef(BaseValidatorModel):
    event: str
    time: datetime
    type: str
    externalId: Optional[str] = None

class ResourceSyncEventTypeDef(BaseValidatorModel):
    event: str
    time: datetime
    type: str
    externalId: Optional[str] = None

class S3ObjectSourceTypeDef(BaseValidatorModel):
    bucket: str
    key: str

class SyncBlockerContextTypeDef(BaseValidatorModel):
    key: str
    value: str

class UntagResourceInputRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateComponentInputRequestTypeDef(BaseValidatorModel):
    deploymentType: ComponentDeploymentUpdateTypeType
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    serviceInstanceName: Optional[str] = None
    serviceName: Optional[str] = None
    serviceSpec: Optional[str] = None
    templateFile: Optional[str] = None

class UpdateEnvironmentAccountConnectionInputRequestTypeDef(BaseValidatorModel):
    id: str
    codebuildRoleArn: Optional[str] = None
    componentRoleArn: Optional[str] = None
    roleArn: Optional[str] = None

class UpdateEnvironmentTemplateInputRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    displayName: Optional[str] = None

class UpdateEnvironmentTemplateVersionInputRequestTypeDef(BaseValidatorModel):
    majorVersion: str
    minorVersion: str
    templateName: str
    description: Optional[str] = None
    status: Optional[TemplateVersionStatusType] = None

class UpdateServiceInputRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    spec: Optional[str] = None

class UpdateServiceInstanceInputRequestTypeDef(BaseValidatorModel):
    deploymentType: DeploymentUpdateTypeType
    name: str
    serviceName: str
    clientToken: Optional[str] = None
    spec: Optional[str] = None
    templateMajorVersion: Optional[str] = None
    templateMinorVersion: Optional[str] = None

class UpdateServicePipelineInputRequestTypeDef(BaseValidatorModel):
    deploymentType: DeploymentUpdateTypeType
    serviceName: str
    spec: str
    templateMajorVersion: Optional[str] = None
    templateMinorVersion: Optional[str] = None

class UpdateServiceSyncBlockerInputRequestTypeDef(BaseValidatorModel):
    id: str
    resolvedReason: str

class UpdateServiceSyncConfigInputRequestTypeDef(BaseValidatorModel):
    branch: str
    filePath: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    serviceName: str

class UpdateServiceTemplateInputRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    displayName: Optional[str] = None

class UpdateTemplateSyncConfigInputRequestTypeDef(BaseValidatorModel):
    branch: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    templateName: str
    templateType: TemplateTypeType
    subdirectory: Optional[str] = None

class AcceptEnvironmentAccountConnectionOutputTypeDef(BaseValidatorModel):
    environmentAccountConnection: EnvironmentAccountConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEnvironmentAccountConnectionOutputTypeDef(BaseValidatorModel):
    environmentAccountConnection: EnvironmentAccountConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEnvironmentAccountConnectionOutputTypeDef(BaseValidatorModel):
    environmentAccountConnection: EnvironmentAccountConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetEnvironmentAccountConnectionOutputTypeDef(BaseValidatorModel):
    environmentAccountConnection: EnvironmentAccountConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RejectEnvironmentAccountConnectionOutputTypeDef(BaseValidatorModel):
    environmentAccountConnection: EnvironmentAccountConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEnvironmentAccountConnectionOutputTypeDef(BaseValidatorModel):
    environmentAccountConnection: EnvironmentAccountConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AccountSettingsTypeDef(BaseValidatorModel):
    pipelineCodebuildRoleArn: Optional[str] = None
    pipelineProvisioningRepository: Optional[RepositoryBranchTypeDef] = None
    pipelineServiceRoleArn: Optional[str] = None

class EnvironmentTypeDef(BaseValidatorModel):
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

class CancelComponentDeploymentOutputTypeDef(BaseValidatorModel):
    component: ComponentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateComponentOutputTypeDef(BaseValidatorModel):
    component: ComponentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteComponentOutputTypeDef(BaseValidatorModel):
    component: ComponentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetComponentOutputTypeDef(BaseValidatorModel):
    component: ComponentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateComponentOutputTypeDef(BaseValidatorModel):
    component: ComponentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CancelServiceInstanceDeploymentOutputTypeDef(BaseValidatorModel):
    serviceInstance: ServiceInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServiceInstanceOutputTypeDef(BaseValidatorModel):
    serviceInstance: ServiceInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceInstanceOutputTypeDef(BaseValidatorModel):
    serviceInstance: ServiceInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceInstanceOutputTypeDef(BaseValidatorModel):
    serviceInstance: ServiceInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CancelServicePipelineDeploymentOutputTypeDef(BaseValidatorModel):
    pipeline: ServicePipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ServiceTypeDef(BaseValidatorModel):
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

class UpdateServicePipelineOutputTypeDef(BaseValidatorModel):
    pipeline: ServicePipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceTemplateVersionInputRequestTypeDef(BaseValidatorModel):
    majorVersion: str
    minorVersion: str
    templateName: str
    compatibleEnvironmentTemplates: Optional[       Sequence[CompatibleEnvironmentTemplateInputTypeDef]     ] = None
    description: Optional[str] = None
    status: Optional[TemplateVersionStatusType] = None
    supportedComponentSources: Optional[Sequence[Literal["DIRECTLY_DEFINED"]]] = None

class ServiceTemplateVersionTypeDef(BaseValidatorModel):
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

class ListComponentsOutputTypeDef(BaseValidatorModel):
    components: List[ComponentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CountsSummaryTypeDef(BaseValidatorModel):
    components: Optional[ResourceCountsSummaryTypeDef] = None
    environmentTemplates: Optional[ResourceCountsSummaryTypeDef] = None
    environments: Optional[ResourceCountsSummaryTypeDef] = None
    pipelines: Optional[ResourceCountsSummaryTypeDef] = None
    serviceInstances: Optional[ResourceCountsSummaryTypeDef] = None
    serviceTemplates: Optional[ResourceCountsSummaryTypeDef] = None
    services: Optional[ResourceCountsSummaryTypeDef] = None

class CreateComponentInputRequestTypeDef(BaseValidatorModel):
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

class CreateEnvironmentAccountConnectionInputRequestTypeDef(BaseValidatorModel):
    environmentName: str
    managementAccountId: str
    clientToken: Optional[str] = None
    codebuildRoleArn: Optional[str] = None
    componentRoleArn: Optional[str] = None
    roleArn: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateEnvironmentTemplateInputRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    displayName: Optional[str] = None
    encryptionKey: Optional[str] = None
    provisioning: Optional[Literal["CUSTOMER_MANAGED"]] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateRepositoryInputRequestTypeDef(BaseValidatorModel):
    connectionArn: str
    name: str
    provider: RepositoryProviderType
    encryptionKey: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateServiceInputRequestTypeDef(BaseValidatorModel):
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

class CreateServiceInstanceInputRequestTypeDef(BaseValidatorModel):
    name: str
    serviceName: str
    spec: str
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    templateMajorVersion: Optional[str] = None
    templateMinorVersion: Optional[str] = None

class CreateServiceTemplateInputRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    displayName: Optional[str] = None
    encryptionKey: Optional[str] = None
    pipelineProvisioning: Optional[Literal["CUSTOMER_MANAGED"]] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    nextToken: str
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceInputRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class CreateEnvironmentInputRequestTypeDef(BaseValidatorModel):
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

class UpdateAccountSettingsInputRequestTypeDef(BaseValidatorModel):
    deletePipelineProvisioningRepository: Optional[bool] = None
    pipelineCodebuildRoleArn: Optional[str] = None
    pipelineProvisioningRepository: Optional[RepositoryBranchInputTypeDef] = None
    pipelineServiceRoleArn: Optional[str] = None

class UpdateEnvironmentInputRequestTypeDef(BaseValidatorModel):
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

class CreateEnvironmentTemplateOutputTypeDef(BaseValidatorModel):
    environmentTemplate: EnvironmentTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEnvironmentTemplateOutputTypeDef(BaseValidatorModel):
    environmentTemplate: EnvironmentTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetEnvironmentTemplateOutputTypeDef(BaseValidatorModel):
    environmentTemplate: EnvironmentTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEnvironmentTemplateOutputTypeDef(BaseValidatorModel):
    environmentTemplate: EnvironmentTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEnvironmentTemplateVersionOutputTypeDef(BaseValidatorModel):
    environmentTemplateVersion: EnvironmentTemplateVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEnvironmentTemplateVersionOutputTypeDef(BaseValidatorModel):
    environmentTemplateVersion: EnvironmentTemplateVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetEnvironmentTemplateVersionOutputTypeDef(BaseValidatorModel):
    environmentTemplateVersion: EnvironmentTemplateVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEnvironmentTemplateVersionOutputTypeDef(BaseValidatorModel):
    environmentTemplateVersion: EnvironmentTemplateVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRepositoryOutputTypeDef(BaseValidatorModel):
    repository: RepositoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRepositoryOutputTypeDef(BaseValidatorModel):
    repository: RepositoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRepositoryOutputTypeDef(BaseValidatorModel):
    repository: RepositoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServiceSyncConfigOutputTypeDef(BaseValidatorModel):
    serviceSyncConfig: ServiceSyncConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteServiceSyncConfigOutputTypeDef(BaseValidatorModel):
    serviceSyncConfig: ServiceSyncConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceSyncConfigOutputTypeDef(BaseValidatorModel):
    serviceSyncConfig: ServiceSyncConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceSyncConfigOutputTypeDef(BaseValidatorModel):
    serviceSyncConfig: ServiceSyncConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServiceTemplateOutputTypeDef(BaseValidatorModel):
    serviceTemplate: ServiceTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteServiceTemplateOutputTypeDef(BaseValidatorModel):
    serviceTemplate: ServiceTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceTemplateOutputTypeDef(BaseValidatorModel):
    serviceTemplate: ServiceTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceTemplateOutputTypeDef(BaseValidatorModel):
    serviceTemplate: ServiceTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTemplateSyncConfigOutputTypeDef(BaseValidatorModel):
    templateSyncConfig: TemplateSyncConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTemplateSyncConfigOutputTypeDef(BaseValidatorModel):
    templateSyncConfig: TemplateSyncConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTemplateSyncConfigOutputTypeDef(BaseValidatorModel):
    templateSyncConfig: TemplateSyncConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTemplateSyncConfigOutputTypeDef(BaseValidatorModel):
    templateSyncConfig: TemplateSyncConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeploymentStateTypeDef(BaseValidatorModel):
    component: Optional[ComponentStateTypeDef] = None
    environment: Optional[EnvironmentStateTypeDef] = None
    serviceInstance: Optional[ServiceInstanceStateTypeDef] = None
    servicePipeline: Optional[ServicePipelineStateTypeDef] = None

class ListDeploymentsOutputTypeDef(BaseValidatorModel):
    deployments: List[DeploymentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnvironmentAccountConnectionsOutputTypeDef(BaseValidatorModel):
    environmentAccountConnections: List[EnvironmentAccountConnectionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnvironmentsOutputTypeDef(BaseValidatorModel):
    environments: List[EnvironmentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnvironmentsInputRequestTypeDef(BaseValidatorModel):
    environmentTemplates: Optional[Sequence[EnvironmentTemplateFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListEnvironmentTemplatesOutputTypeDef(BaseValidatorModel):
    nextToken: str
    templates: List[EnvironmentTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnvironmentTemplateVersionsOutputTypeDef(BaseValidatorModel):
    nextToken: str
    templateVersions: List[EnvironmentTemplateVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetComponentInputComponentDeletedWaitTypeDef(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetComponentInputComponentDeployedWaitTypeDef(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetEnvironmentInputEnvironmentDeployedWaitTypeDef(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetEnvironmentTemplateVersionInputEnvironmentTemplateVersionRegisteredWaitTypeDef(BaseValidatorModel):
    majorVersion: str
    minorVersion: str
    templateName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetServiceInputServiceCreatedWaitTypeDef(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetServiceInputServiceDeletedWaitTypeDef(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetServiceInputServicePipelineDeployedWaitTypeDef(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetServiceInputServiceUpdatedWaitTypeDef(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetServiceInstanceInputServiceInstanceDeployedWaitTypeDef(BaseValidatorModel):
    name: str
    serviceName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetServiceTemplateVersionInputServiceTemplateVersionRegisteredWaitTypeDef(BaseValidatorModel):
    majorVersion: str
    minorVersion: str
    templateName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class ListComponentOutputsInputListComponentOutputsPaginateTypeDef(BaseValidatorModel):
    componentName: str
    deploymentId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListComponentProvisionedResourcesInputListComponentProvisionedResourcesPaginateTypeDef(BaseValidatorModel):
    componentName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListComponentsInputListComponentsPaginateTypeDef(BaseValidatorModel):
    environmentName: Optional[str] = None
    serviceInstanceName: Optional[str] = None
    serviceName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeploymentsInputListDeploymentsPaginateTypeDef(BaseValidatorModel):
    componentName: Optional[str] = None
    environmentName: Optional[str] = None
    serviceInstanceName: Optional[str] = None
    serviceName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEnvironmentAccountConnectionsInputListEnvironmentAccountConnectionsPaginateTypeDef(BaseValidatorModel):
    requestedBy: EnvironmentAccountConnectionRequesterAccountTypeType
    environmentName: Optional[str] = None
    statuses: Optional[Sequence[EnvironmentAccountConnectionStatusType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEnvironmentOutputsInputListEnvironmentOutputsPaginateTypeDef(BaseValidatorModel):
    environmentName: str
    deploymentId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEnvironmentProvisionedResourcesInputListEnvironmentProvisionedResourcesPaginateTypeDef(BaseValidatorModel):
    environmentName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEnvironmentTemplateVersionsInputListEnvironmentTemplateVersionsPaginateTypeDef(BaseValidatorModel):
    templateName: str
    majorVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEnvironmentTemplatesInputListEnvironmentTemplatesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEnvironmentsInputListEnvironmentsPaginateTypeDef(BaseValidatorModel):
    environmentTemplates: Optional[Sequence[EnvironmentTemplateFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRepositoriesInputListRepositoriesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRepositorySyncDefinitionsInputListRepositorySyncDefinitionsPaginateTypeDef(BaseValidatorModel):
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    syncType: SyncTypeType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServiceInstanceOutputsInputListServiceInstanceOutputsPaginateTypeDef(BaseValidatorModel):
    serviceInstanceName: str
    serviceName: str
    deploymentId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServiceInstanceProvisionedResourcesInputListServiceInstanceProvisionedResourcesPaginateTypeDef(BaseValidatorModel):
    serviceInstanceName: str
    serviceName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServicePipelineOutputsInputListServicePipelineOutputsPaginateTypeDef(BaseValidatorModel):
    serviceName: str
    deploymentId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServicePipelineProvisionedResourcesInputListServicePipelineProvisionedResourcesPaginateTypeDef(BaseValidatorModel):
    serviceName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServiceTemplateVersionsInputListServiceTemplateVersionsPaginateTypeDef(BaseValidatorModel):
    templateName: str
    majorVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServiceTemplatesInputListServiceTemplatesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServicesInputListServicesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceInputListTagsForResourcePaginateTypeDef(BaseValidatorModel):
    resourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListComponentOutputsOutputTypeDef(BaseValidatorModel):
    nextToken: str
    outputs: List[OutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnvironmentOutputsOutputTypeDef(BaseValidatorModel):
    nextToken: str
    outputs: List[OutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListServiceInstanceOutputsOutputTypeDef(BaseValidatorModel):
    nextToken: str
    outputs: List[OutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListServicePipelineOutputsOutputTypeDef(BaseValidatorModel):
    nextToken: str
    outputs: List[OutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class NotifyResourceDeploymentStatusChangeInputRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    deploymentId: Optional[str] = None
    outputs: Optional[Sequence[OutputTypeDef]] = None
    status: Optional[ResourceDeploymentStatusType] = None
    statusMessage: Optional[str] = None

class ListComponentProvisionedResourcesOutputTypeDef(BaseValidatorModel):
    nextToken: str
    provisionedResources: List[ProvisionedResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnvironmentProvisionedResourcesOutputTypeDef(BaseValidatorModel):
    nextToken: str
    provisionedResources: List[ProvisionedResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListServiceInstanceProvisionedResourcesOutputTypeDef(BaseValidatorModel):
    nextToken: str
    provisionedResources: List[ProvisionedResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListServicePipelineProvisionedResourcesOutputTypeDef(BaseValidatorModel):
    nextToken: str
    provisionedResources: List[ProvisionedResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRepositoriesOutputTypeDef(BaseValidatorModel):
    nextToken: str
    repositories: List[RepositorySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRepositorySyncDefinitionsOutputTypeDef(BaseValidatorModel):
    nextToken: str
    syncDefinitions: List[RepositorySyncDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListServiceInstancesInputListServiceInstancesPaginateTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[ListServiceInstancesFilterTypeDef]] = None
    serviceName: Optional[str] = None
    sortBy: Optional[ListServiceInstancesSortByType] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServiceInstancesInputRequestTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[ListServiceInstancesFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    serviceName: Optional[str] = None
    sortBy: Optional[ListServiceInstancesSortByType] = None
    sortOrder: Optional[SortOrderType] = None

class ListServiceInstancesOutputTypeDef(BaseValidatorModel):
    nextToken: str
    serviceInstances: List[ServiceInstanceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListServiceTemplateVersionsOutputTypeDef(BaseValidatorModel):
    nextToken: str
    templateVersions: List[ServiceTemplateVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListServiceTemplatesOutputTypeDef(BaseValidatorModel):
    nextToken: str
    templates: List[ServiceTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListServicesOutputTypeDef(BaseValidatorModel):
    nextToken: str
    services: List[ServiceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RepositorySyncAttemptTypeDef(BaseValidatorModel):
    events: List[RepositorySyncEventTypeDef]
    startedAt: datetime
    status: RepositorySyncStatusType

class ResourceSyncAttemptTypeDef(BaseValidatorModel):
    events: List[ResourceSyncEventTypeDef]
    initialRevision: RevisionTypeDef
    startedAt: datetime
    status: ResourceSyncStatusType
    target: str
    targetRevision: RevisionTypeDef

class TemplateVersionSourceInputTypeDef(BaseValidatorModel):
    s3: Optional[S3ObjectSourceTypeDef] = None

class SyncBlockerTypeDef(BaseValidatorModel):
    createdAt: datetime
    createdReason: str
    id: str
    status: BlockerStatusType
    type: Literal["AUTOMATED"]
    contexts: Optional[List[SyncBlockerContextTypeDef]] = None
    resolvedAt: Optional[datetime] = None
    resolvedReason: Optional[str] = None

class GetAccountSettingsOutputTypeDef(BaseValidatorModel):
    accountSettings: AccountSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccountSettingsOutputTypeDef(BaseValidatorModel):
    accountSettings: AccountSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CancelEnvironmentDeploymentOutputTypeDef(BaseValidatorModel):
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEnvironmentOutputTypeDef(BaseValidatorModel):
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEnvironmentOutputTypeDef(BaseValidatorModel):
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetEnvironmentOutputTypeDef(BaseValidatorModel):
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEnvironmentOutputTypeDef(BaseValidatorModel):
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServiceOutputTypeDef(BaseValidatorModel):
    service: ServiceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteServiceOutputTypeDef(BaseValidatorModel):
    service: ServiceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceOutputTypeDef(BaseValidatorModel):
    service: ServiceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceOutputTypeDef(BaseValidatorModel):
    service: ServiceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServiceTemplateVersionOutputTypeDef(BaseValidatorModel):
    serviceTemplateVersion: ServiceTemplateVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteServiceTemplateVersionOutputTypeDef(BaseValidatorModel):
    serviceTemplateVersion: ServiceTemplateVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceTemplateVersionOutputTypeDef(BaseValidatorModel):
    serviceTemplateVersion: ServiceTemplateVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceTemplateVersionOutputTypeDef(BaseValidatorModel):
    serviceTemplateVersion: ServiceTemplateVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcesSummaryOutputTypeDef(BaseValidatorModel):
    counts: CountsSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeploymentTypeDef(BaseValidatorModel):
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

class GetRepositorySyncStatusOutputTypeDef(BaseValidatorModel):
    latestSync: RepositorySyncAttemptTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceInstanceSyncStatusOutputTypeDef(BaseValidatorModel):
    desiredState: RevisionTypeDef
    latestSuccessfulSync: ResourceSyncAttemptTypeDef
    latestSync: ResourceSyncAttemptTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTemplateSyncStatusOutputTypeDef(BaseValidatorModel):
    desiredState: RevisionTypeDef
    latestSuccessfulSync: ResourceSyncAttemptTypeDef
    latestSync: ResourceSyncAttemptTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEnvironmentTemplateVersionInputRequestTypeDef(BaseValidatorModel):
    source: TemplateVersionSourceInputTypeDef
    templateName: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    majorVersion: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateServiceTemplateVersionInputRequestTypeDef(BaseValidatorModel):
    compatibleEnvironmentTemplates: Sequence[CompatibleEnvironmentTemplateInputTypeDef]
    source: TemplateVersionSourceInputTypeDef
    templateName: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    majorVersion: Optional[str] = None
    supportedComponentSources: Optional[Sequence[Literal["DIRECTLY_DEFINED"]]] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class ServiceSyncBlockerSummaryTypeDef(BaseValidatorModel):
    serviceName: str
    latestBlockers: Optional[List[SyncBlockerTypeDef]] = None
    serviceInstanceName: Optional[str] = None

class UpdateServiceSyncBlockerOutputTypeDef(BaseValidatorModel):
    serviceInstanceName: str
    serviceName: str
    serviceSyncBlocker: SyncBlockerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDeploymentOutputTypeDef(BaseValidatorModel):
    deployment: DeploymentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeploymentOutputTypeDef(BaseValidatorModel):
    deployment: DeploymentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceSyncBlockerSummaryOutputTypeDef(BaseValidatorModel):
    serviceSyncBlockerSummary: ServiceSyncBlockerSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


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
from aws_resource_validator.pydantic_models.proton_constants import *

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class RepositoryBranchTypeDef(BaseValidatorModel):
    arn: str
    branch: str
    name: str
    provider: RepositoryProviderType


class CancelComponentDeploymentInputTypeDef(BaseValidatorModel):
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


class CancelEnvironmentDeploymentInputTypeDef(BaseValidatorModel):
    environmentName: str


class CancelServiceInstanceDeploymentInputTypeDef(BaseValidatorModel):
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


class CancelServicePipelineDeploymentInputTypeDef(BaseValidatorModel):
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


class CreateServiceSyncConfigInputTypeDef(BaseValidatorModel):
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


class CreateTemplateSyncConfigInputTypeDef(BaseValidatorModel):
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


class DeleteComponentInputTypeDef(BaseValidatorModel):
    name: str


class DeleteEnvironmentInputTypeDef(BaseValidatorModel):
    name: str


class DeleteEnvironmentTemplateInputTypeDef(BaseValidatorModel):
    name: str


class DeleteEnvironmentTemplateVersionInputTypeDef(BaseValidatorModel):
    majorVersion: str
    minorVersion: str
    templateName: str


class DeleteRepositoryInputTypeDef(BaseValidatorModel):
    name: str
    provider: RepositoryProviderType


class DeleteServiceInputTypeDef(BaseValidatorModel):
    name: str


class DeleteServiceSyncConfigInputTypeDef(BaseValidatorModel):
    serviceName: str


class DeleteServiceTemplateInputTypeDef(BaseValidatorModel):
    name: str


class DeleteServiceTemplateVersionInputTypeDef(BaseValidatorModel):
    majorVersion: str
    minorVersion: str
    templateName: str


class DeleteTemplateSyncConfigInputTypeDef(BaseValidatorModel):
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


class GetComponentInputTypeDef(BaseValidatorModel):
    name: str


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class GetEnvironmentInputTypeDef(BaseValidatorModel):
    name: str


class GetEnvironmentTemplateInputTypeDef(BaseValidatorModel):
    name: str


class GetEnvironmentTemplateVersionInputTypeDef(BaseValidatorModel):
    majorVersion: str
    minorVersion: str
    templateName: str


class GetRepositoryInputTypeDef(BaseValidatorModel):
    name: str
    provider: RepositoryProviderType


class GetRepositorySyncStatusInputTypeDef(BaseValidatorModel):
    branch: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    syncType: SyncTypeType


class GetServiceInputTypeDef(BaseValidatorModel):
    name: str


class GetServiceInstanceInputTypeDef(BaseValidatorModel):
    name: str
    serviceName: str


class GetServiceInstanceSyncStatusInputTypeDef(BaseValidatorModel):
    serviceInstanceName: str
    serviceName: str


class RevisionTypeDef(BaseValidatorModel):
    branch: str
    directory: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    sha: str


class GetServiceSyncBlockerSummaryInputTypeDef(BaseValidatorModel):
    serviceName: str
    serviceInstanceName: Optional[str] = None


class GetServiceSyncConfigInputTypeDef(BaseValidatorModel):
    serviceName: str


class GetServiceTemplateInputTypeDef(BaseValidatorModel):
    name: str


class GetServiceTemplateVersionInputTypeDef(BaseValidatorModel):
    majorVersion: str
    minorVersion: str
    templateName: str


class GetTemplateSyncConfigInputTypeDef(BaseValidatorModel):
    templateName: str
    templateType: TemplateTypeType


class GetTemplateSyncStatusInputTypeDef(BaseValidatorModel):
    templateName: str
    templateType: TemplateTypeType
    templateVersion: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListComponentOutputsInputTypeDef(BaseValidatorModel):
    componentName: str
    deploymentId: Optional[str] = None
    nextToken: Optional[str] = None


class OutputTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    valueString: Optional[str] = None


class ListComponentProvisionedResourcesInputTypeDef(BaseValidatorModel):
    componentName: str
    nextToken: Optional[str] = None


class ProvisionedResourceTypeDef(BaseValidatorModel):
    identifier: Optional[str] = None
    name: Optional[str] = None
    provisioningEngine: Optional[ProvisionedResourceEngineType] = None


class ListComponentsInputTypeDef(BaseValidatorModel):
    environmentName: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    serviceInstanceName: Optional[str] = None
    serviceName: Optional[str] = None


class ListDeploymentsInputTypeDef(BaseValidatorModel):
    componentName: Optional[str] = None
    environmentName: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    serviceInstanceName: Optional[str] = None
    serviceName: Optional[str] = None


class ListEnvironmentAccountConnectionsInputTypeDef(BaseValidatorModel):
    requestedBy: EnvironmentAccountConnectionRequesterAccountTypeType
    environmentName: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    statuses: Optional[Sequence[EnvironmentAccountConnectionStatusType]] = None


class ListEnvironmentOutputsInputTypeDef(BaseValidatorModel):
    environmentName: str
    deploymentId: Optional[str] = None
    nextToken: Optional[str] = None


class ListEnvironmentProvisionedResourcesInputTypeDef(BaseValidatorModel):
    environmentName: str
    nextToken: Optional[str] = None


class ListEnvironmentTemplateVersionsInputTypeDef(BaseValidatorModel):
    templateName: str
    majorVersion: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListEnvironmentTemplatesInputTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListRepositoriesInputTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class RepositorySummaryTypeDef(BaseValidatorModel):
    arn: str
    connectionArn: str
    name: str
    provider: RepositoryProviderType


class ListRepositorySyncDefinitionsInputTypeDef(BaseValidatorModel):
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    syncType: SyncTypeType
    nextToken: Optional[str] = None


class RepositorySyncDefinitionTypeDef(BaseValidatorModel):
    branch: str
    directory: str
    parent: str
    target: str


class ListServiceInstanceOutputsInputTypeDef(BaseValidatorModel):
    serviceInstanceName: str
    serviceName: str
    deploymentId: Optional[str] = None
    nextToken: Optional[str] = None


class ListServiceInstanceProvisionedResourcesInputTypeDef(BaseValidatorModel):
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


class ListServicePipelineOutputsInputTypeDef(BaseValidatorModel):
    serviceName: str
    deploymentId: Optional[str] = None
    nextToken: Optional[str] = None


class ListServicePipelineProvisionedResourcesInputTypeDef(BaseValidatorModel):
    serviceName: str
    nextToken: Optional[str] = None


class ListServiceTemplateVersionsInputTypeDef(BaseValidatorModel):
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


class ListServiceTemplatesInputTypeDef(BaseValidatorModel):
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


class ListServicesInputTypeDef(BaseValidatorModel):
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


class ListTagsForResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class S3ObjectSourceTypeDef(BaseValidatorModel):
    bucket: str
    key: str


class SyncBlockerContextTypeDef(BaseValidatorModel):
    key: str
    value: str


class UntagResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateComponentInputTypeDef(BaseValidatorModel):
    deploymentType: ComponentDeploymentUpdateTypeType
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    serviceInstanceName: Optional[str] = None
    serviceName: Optional[str] = None
    serviceSpec: Optional[str] = None
    templateFile: Optional[str] = None


class UpdateEnvironmentTemplateInputTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    displayName: Optional[str] = None


class UpdateEnvironmentTemplateVersionInputTypeDef(BaseValidatorModel):
    majorVersion: str
    minorVersion: str
    templateName: str
    description: Optional[str] = None
    status: Optional[TemplateVersionStatusType] = None


class UpdateServiceInputTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    spec: Optional[str] = None


class UpdateServiceInstanceInputTypeDef(BaseValidatorModel):
    deploymentType: DeploymentUpdateTypeType
    name: str
    serviceName: str
    clientToken: Optional[str] = None
    spec: Optional[str] = None
    templateMajorVersion: Optional[str] = None
    templateMinorVersion: Optional[str] = None


class UpdateServicePipelineInputTypeDef(BaseValidatorModel):
    deploymentType: DeploymentUpdateTypeType
    serviceName: str
    spec: str
    templateMajorVersion: Optional[str] = None
    templateMinorVersion: Optional[str] = None


class UpdateServiceSyncConfigInputTypeDef(BaseValidatorModel):
    branch: str
    filePath: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    serviceName: str


class UpdateServiceTemplateInputTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    displayName: Optional[str] = None


class UpdateTemplateSyncConfigInputTypeDef(BaseValidatorModel):
    branch: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    templateName: str
    templateType: TemplateTypeType
    subdirectory: Optional[str] = None


class EnvironmentAccountConnectionTypeDef(BaseValidatorModel):
    pass


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


class UpdateServiceTemplateVersionInputTypeDef(BaseValidatorModel):
    majorVersion: str
    minorVersion: str
    templateName: str
    compatibleEnvironmentTemplates: Optional[Sequence[CompatibleEnvironmentTemplateInputTypeDef]] = None
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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CountsSummaryTypeDef(BaseValidatorModel):
    components: Optional[ResourceCountsSummaryTypeDef] = None
    environmentTemplates: Optional[ResourceCountsSummaryTypeDef] = None
    environments: Optional[ResourceCountsSummaryTypeDef] = None
    pipelines: Optional[ResourceCountsSummaryTypeDef] = None
    serviceInstances: Optional[ResourceCountsSummaryTypeDef] = None
    serviceTemplates: Optional[ResourceCountsSummaryTypeDef] = None
    services: Optional[ResourceCountsSummaryTypeDef] = None


class CreateComponentInputTypeDef(BaseValidatorModel):
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


class CreateEnvironmentAccountConnectionInputTypeDef(BaseValidatorModel):
    environmentName: str
    managementAccountId: str
    clientToken: Optional[str] = None
    codebuildRoleArn: Optional[str] = None
    componentRoleArn: Optional[str] = None
    roleArn: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateEnvironmentTemplateInputTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    displayName: Optional[str] = None
    encryptionKey: Optional[str] = None
    provisioning: Optional[Literal["CUSTOMER_MANAGED"]] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateRepositoryInputTypeDef(BaseValidatorModel):
    connectionArn: str
    name: str
    provider: RepositoryProviderType
    encryptionKey: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateServiceInputTypeDef(BaseValidatorModel):
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


class CreateServiceInstanceInputTypeDef(BaseValidatorModel):
    name: str
    serviceName: str
    spec: str
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    templateMajorVersion: Optional[str] = None
    templateMinorVersion: Optional[str] = None


class CreateServiceTemplateInputTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    displayName: Optional[str] = None
    encryptionKey: Optional[str] = None
    pipelineProvisioning: Optional[Literal["CUSTOMER_MANAGED"]] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class TagResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]


class CreateEnvironmentInputTypeDef(BaseValidatorModel):
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


class UpdateAccountSettingsInputTypeDef(BaseValidatorModel):
    deletePipelineProvisioningRepository: Optional[bool] = None
    pipelineCodebuildRoleArn: Optional[str] = None
    pipelineProvisioningRepository: Optional[RepositoryBranchInputTypeDef] = None
    pipelineServiceRoleArn: Optional[str] = None


class UpdateEnvironmentInputTypeDef(BaseValidatorModel):
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


class DeploymentSummaryTypeDef(BaseValidatorModel):
    pass


class ListDeploymentsOutputTypeDef(BaseValidatorModel):
    deployments: List[DeploymentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class EnvironmentAccountConnectionSummaryTypeDef(BaseValidatorModel):
    pass


class ListEnvironmentAccountConnectionsOutputTypeDef(BaseValidatorModel):
    environmentAccountConnections: List[EnvironmentAccountConnectionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListEnvironmentsOutputTypeDef(BaseValidatorModel):
    environments: List[EnvironmentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListEnvironmentsInputTypeDef(BaseValidatorModel):
    environmentTemplates: Optional[Sequence[EnvironmentTemplateFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListEnvironmentTemplatesOutputTypeDef(BaseValidatorModel):
    templates: List[EnvironmentTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListEnvironmentTemplateVersionsOutputTypeDef(BaseValidatorModel):
    templateVersions: List[EnvironmentTemplateVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetComponentInputWaitExtraTypeDef(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetComponentInputWaitTypeDef(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetEnvironmentInputWaitTypeDef(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetEnvironmentTemplateVersionInputWaitTypeDef(BaseValidatorModel):
    majorVersion: str
    minorVersion: str
    templateName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetServiceInputWaitExtraExtraExtraTypeDef(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetServiceInputWaitExtraExtraTypeDef(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetServiceInputWaitExtraTypeDef(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetServiceInputWaitTypeDef(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetServiceInstanceInputWaitTypeDef(BaseValidatorModel):
    name: str
    serviceName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetServiceTemplateVersionInputWaitTypeDef(BaseValidatorModel):
    majorVersion: str
    minorVersion: str
    templateName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class ListComponentOutputsInputPaginateTypeDef(BaseValidatorModel):
    componentName: str
    deploymentId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListComponentProvisionedResourcesInputPaginateTypeDef(BaseValidatorModel):
    componentName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListComponentsInputPaginateTypeDef(BaseValidatorModel):
    environmentName: Optional[str] = None
    serviceInstanceName: Optional[str] = None
    serviceName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDeploymentsInputPaginateTypeDef(BaseValidatorModel):
    componentName: Optional[str] = None
    environmentName: Optional[str] = None
    serviceInstanceName: Optional[str] = None
    serviceName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEnvironmentAccountConnectionsInputPaginateTypeDef(BaseValidatorModel):
    requestedBy: EnvironmentAccountConnectionRequesterAccountTypeType
    environmentName: Optional[str] = None
    statuses: Optional[Sequence[EnvironmentAccountConnectionStatusType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEnvironmentOutputsInputPaginateTypeDef(BaseValidatorModel):
    environmentName: str
    deploymentId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEnvironmentProvisionedResourcesInputPaginateTypeDef(BaseValidatorModel):
    environmentName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEnvironmentTemplateVersionsInputPaginateTypeDef(BaseValidatorModel):
    templateName: str
    majorVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEnvironmentTemplatesInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEnvironmentsInputPaginateTypeDef(BaseValidatorModel):
    environmentTemplates: Optional[Sequence[EnvironmentTemplateFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRepositoriesInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRepositorySyncDefinitionsInputPaginateTypeDef(BaseValidatorModel):
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    syncType: SyncTypeType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListServiceInstanceOutputsInputPaginateTypeDef(BaseValidatorModel):
    serviceInstanceName: str
    serviceName: str
    deploymentId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListServiceInstanceProvisionedResourcesInputPaginateTypeDef(BaseValidatorModel):
    serviceInstanceName: str
    serviceName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListServicePipelineOutputsInputPaginateTypeDef(BaseValidatorModel):
    serviceName: str
    deploymentId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListServicePipelineProvisionedResourcesInputPaginateTypeDef(BaseValidatorModel):
    serviceName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListServiceTemplateVersionsInputPaginateTypeDef(BaseValidatorModel):
    templateName: str
    majorVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListServiceTemplatesInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListServicesInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTagsForResourceInputPaginateTypeDef(BaseValidatorModel):
    resourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListComponentOutputsOutputTypeDef(BaseValidatorModel):
    outputs: List[OutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListEnvironmentOutputsOutputTypeDef(BaseValidatorModel):
    outputs: List[OutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListServiceInstanceOutputsOutputTypeDef(BaseValidatorModel):
    outputs: List[OutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListServicePipelineOutputsOutputTypeDef(BaseValidatorModel):
    outputs: List[OutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class NotifyResourceDeploymentStatusChangeInputTypeDef(BaseValidatorModel):
    resourceArn: str
    deploymentId: Optional[str] = None
    outputs: Optional[Sequence[OutputTypeDef]] = None
    status: Optional[ResourceDeploymentStatusType] = None
    statusMessage: Optional[str] = None


class ListComponentProvisionedResourcesOutputTypeDef(BaseValidatorModel):
    provisionedResources: List[ProvisionedResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListEnvironmentProvisionedResourcesOutputTypeDef(BaseValidatorModel):
    provisionedResources: List[ProvisionedResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListServiceInstanceProvisionedResourcesOutputTypeDef(BaseValidatorModel):
    provisionedResources: List[ProvisionedResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListServicePipelineProvisionedResourcesOutputTypeDef(BaseValidatorModel):
    provisionedResources: List[ProvisionedResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListRepositoriesOutputTypeDef(BaseValidatorModel):
    repositories: List[RepositorySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListRepositorySyncDefinitionsOutputTypeDef(BaseValidatorModel):
    syncDefinitions: List[RepositorySyncDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListServiceInstancesInputPaginateTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[ListServiceInstancesFilterTypeDef]] = None
    serviceName: Optional[str] = None
    sortBy: Optional[ListServiceInstancesSortByType] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListServiceInstancesInputTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[ListServiceInstancesFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    serviceName: Optional[str] = None
    sortBy: Optional[ListServiceInstancesSortByType] = None
    sortOrder: Optional[SortOrderType] = None


class ListServiceInstancesOutputTypeDef(BaseValidatorModel):
    serviceInstances: List[ServiceInstanceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListServiceTemplateVersionsOutputTypeDef(BaseValidatorModel):
    templateVersions: List[ServiceTemplateVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListServiceTemplatesOutputTypeDef(BaseValidatorModel):
    templates: List[ServiceTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListServicesOutputTypeDef(BaseValidatorModel):
    services: List[ServiceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class RepositorySyncEventTypeDef(BaseValidatorModel):
    pass


class RepositorySyncAttemptTypeDef(BaseValidatorModel):
    events: List[RepositorySyncEventTypeDef]
    startedAt: datetime
    status: RepositorySyncStatusType


class ResourceSyncEventTypeDef(BaseValidatorModel):
    pass


class ResourceSyncAttemptTypeDef(BaseValidatorModel):
    events: List[ResourceSyncEventTypeDef]
    initialRevision: RevisionTypeDef
    startedAt: datetime
    status: ResourceSyncStatusType
    target: str
    targetRevision: RevisionTypeDef


class TemplateVersionSourceInputTypeDef(BaseValidatorModel):
    s3: Optional[S3ObjectSourceTypeDef] = None


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


class CreateEnvironmentTemplateVersionInputTypeDef(BaseValidatorModel):
    source: TemplateVersionSourceInputTypeDef
    templateName: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    majorVersion: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateServiceTemplateVersionInputTypeDef(BaseValidatorModel):
    compatibleEnvironmentTemplates: Sequence[CompatibleEnvironmentTemplateInputTypeDef]
    source: TemplateVersionSourceInputTypeDef
    templateName: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    majorVersion: Optional[str] = None
    supportedComponentSources: Optional[Sequence[Literal["DIRECTLY_DEFINED"]]] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class SyncBlockerTypeDef(BaseValidatorModel):
    pass


class ServiceSyncBlockerSummaryTypeDef(BaseValidatorModel):
    serviceName: str
    latestBlockers: Optional[List[SyncBlockerTypeDef]] = None
    serviceInstanceName: Optional[str] = None


class UpdateServiceSyncBlockerOutputTypeDef(BaseValidatorModel):
    serviceInstanceName: str
    serviceName: str
    serviceSyncBlocker: SyncBlockerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeploymentTypeDef(BaseValidatorModel):
    pass


class DeleteDeploymentOutputTypeDef(BaseValidatorModel):
    deployment: DeploymentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetDeploymentOutputTypeDef(BaseValidatorModel):
    deployment: DeploymentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetServiceSyncBlockerSummaryOutputTypeDef(BaseValidatorModel):
    serviceSyncBlockerSummary: ServiceSyncBlockerSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef



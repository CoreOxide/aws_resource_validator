from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.proton.proton_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




# This class is the input for the 'accept_environment_account_connection' function.
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


# This class is the input for the 'cancel_component_deployment' function.
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


# This class is the input for the 'cancel_environment_deployment' function.
class CancelEnvironmentDeploymentInput(BaseValidatorModel):
    environmentName: str


# This class is the input for the 'cancel_service_instance_deployment' function.
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


# This class is the input for the 'cancel_service_pipeline_deployment' function.
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


# This class is the input for the 'create_service_sync_config' function.
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


# This class is the input for the 'create_template_sync_config' function.
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


# This class is the input for the 'delete_component' function.
class DeleteComponentInput(BaseValidatorModel):
    name: str


# This class is the input for the 'delete_deployment' function.
class DeleteDeploymentInput(BaseValidatorModel):
    id: str


# This class is the input for the 'delete_environment_account_connection' function.
class DeleteEnvironmentAccountConnectionInput(BaseValidatorModel):
    id: str


# This class is the input for the 'delete_environment' function.
class DeleteEnvironmentInput(BaseValidatorModel):
    name: str


# This class is the input for the 'delete_environment_template' function.
class DeleteEnvironmentTemplateInput(BaseValidatorModel):
    name: str


# This class is the input for the 'delete_environment_template_version' function.
class DeleteEnvironmentTemplateVersionInput(BaseValidatorModel):
    majorVersion: str
    minorVersion: str
    templateName: str


# This class is the input for the 'delete_repository' function.
class DeleteRepositoryInput(BaseValidatorModel):
    name: str
    provider: RepositoryProviderType


# This class is the input for the 'delete_service' function.
class DeleteServiceInput(BaseValidatorModel):
    name: str


# This class is the input for the 'delete_service_sync_config' function.
class DeleteServiceSyncConfigInput(BaseValidatorModel):
    serviceName: str


# This class is the input for the 'delete_service_template' function.
class DeleteServiceTemplateInput(BaseValidatorModel):
    name: str


# This class is the input for the 'delete_service_template_version' function.
class DeleteServiceTemplateVersionInput(BaseValidatorModel):
    majorVersion: str
    minorVersion: str
    templateName: str


# This class is the input for the 'delete_template_sync_config' function.
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


# This class is the input for the 'get_component' function.
class GetComponentInput(BaseValidatorModel):
    name: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


# This class is the input for the 'get_deployment' function.
class GetDeploymentInput(BaseValidatorModel):
    id: str
    componentName: Optional[str] = None
    environmentName: Optional[str] = None
    serviceInstanceName: Optional[str] = None
    serviceName: Optional[str] = None


# This class is the input for the 'get_environment_account_connection' function.
class GetEnvironmentAccountConnectionInput(BaseValidatorModel):
    id: str


# This class is the input for the 'get_environment' function.
class GetEnvironmentInput(BaseValidatorModel):
    name: str


# This class is the input for the 'get_environment_template' function.
class GetEnvironmentTemplateInput(BaseValidatorModel):
    name: str


# This class is the input for the 'get_environment_template_version' function.
class GetEnvironmentTemplateVersionInput(BaseValidatorModel):
    majorVersion: str
    minorVersion: str
    templateName: str


# This class is the input for the 'get_repository' function.
class GetRepositoryInput(BaseValidatorModel):
    name: str
    provider: RepositoryProviderType


# This class is the input for the 'get_repository_sync_status' function.
class GetRepositorySyncStatusInput(BaseValidatorModel):
    branch: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    syncType: SyncTypeType


# This class is the input for the 'get_service' function.
class GetServiceInput(BaseValidatorModel):
    name: str


# This class is the input for the 'get_service_instance' function.
class GetServiceInstanceInput(BaseValidatorModel):
    name: str
    serviceName: str


# This class is the input for the 'get_service_instance_sync_status' function.
class GetServiceInstanceSyncStatusInput(BaseValidatorModel):
    serviceInstanceName: str
    serviceName: str


class Revision(BaseValidatorModel):
    branch: str
    directory: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    sha: str


# This class is the input for the 'get_service_sync_blocker_summary' function.
class GetServiceSyncBlockerSummaryInput(BaseValidatorModel):
    serviceName: str
    serviceInstanceName: Optional[str] = None


# This class is the input for the 'get_service_sync_config' function.
class GetServiceSyncConfigInput(BaseValidatorModel):
    serviceName: str


# This class is the input for the 'get_service_template' function.
class GetServiceTemplateInput(BaseValidatorModel):
    name: str


# This class is the input for the 'get_service_template_version' function.
class GetServiceTemplateVersionInput(BaseValidatorModel):
    majorVersion: str
    minorVersion: str
    templateName: str


# This class is the input for the 'get_template_sync_config' function.
class GetTemplateSyncConfigInput(BaseValidatorModel):
    templateName: str
    templateType: TemplateTypeType


# This class is the input for the 'get_template_sync_status' function.
class GetTemplateSyncStatusInput(BaseValidatorModel):
    templateName: str
    templateType: TemplateTypeType
    templateVersion: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_component_outputs' function.
class ListComponentOutputsInput(BaseValidatorModel):
    componentName: str
    deploymentId: Optional[str] = None
    nextToken: Optional[str] = None


class Output(BaseValidatorModel):
    key: Optional[str] = None
    valueString: Optional[str] = None


# This class is the input for the 'list_component_provisioned_resources' function.
class ListComponentProvisionedResourcesInput(BaseValidatorModel):
    componentName: str
    nextToken: Optional[str] = None


class ProvisionedResource(BaseValidatorModel):
    identifier: Optional[str] = None
    name: Optional[str] = None
    provisioningEngine: Optional[ProvisionedResourceEngineType] = None


# This class is the input for the 'list_components' function.
class ListComponentsInput(BaseValidatorModel):
    environmentName: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    serviceInstanceName: Optional[str] = None
    serviceName: Optional[str] = None


# This class is the input for the 'list_deployments' function.
class ListDeploymentsInput(BaseValidatorModel):
    componentName: Optional[str] = None
    environmentName: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    serviceInstanceName: Optional[str] = None
    serviceName: Optional[str] = None


# This class is the input for the 'list_environment_account_connections' function.
class ListEnvironmentAccountConnectionsInput(BaseValidatorModel):
    requestedBy: EnvironmentAccountConnectionRequesterAccountTypeType
    environmentName: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    statuses: Optional[List[EnvironmentAccountConnectionStatusType]] = None


# This class is the input for the 'list_environment_outputs' function.
class ListEnvironmentOutputsInput(BaseValidatorModel):
    environmentName: str
    deploymentId: Optional[str] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_environment_provisioned_resources' function.
class ListEnvironmentProvisionedResourcesInput(BaseValidatorModel):
    environmentName: str
    nextToken: Optional[str] = None


# This class is the input for the 'list_environment_template_versions' function.
class ListEnvironmentTemplateVersionsInput(BaseValidatorModel):
    templateName: str
    majorVersion: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_environment_templates' function.
class ListEnvironmentTemplatesInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_repositories' function.
class ListRepositoriesInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class RepositorySummary(BaseValidatorModel):
    arn: str
    connectionArn: str
    name: str
    provider: RepositoryProviderType


# This class is the input for the 'list_repository_sync_definitions' function.
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


# This class is the input for the 'list_service_instance_outputs' function.
class ListServiceInstanceOutputsInput(BaseValidatorModel):
    serviceInstanceName: str
    serviceName: str
    deploymentId: Optional[str] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_service_instance_provisioned_resources' function.
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


# This class is the input for the 'list_service_pipeline_outputs' function.
class ListServicePipelineOutputsInput(BaseValidatorModel):
    serviceName: str
    deploymentId: Optional[str] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_service_pipeline_provisioned_resources' function.
class ListServicePipelineProvisionedResourcesInput(BaseValidatorModel):
    serviceName: str
    nextToken: Optional[str] = None


# This class is the input for the 'list_service_template_versions' function.
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


# This class is the input for the 'list_service_templates' function.
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


# This class is the input for the 'list_services' function.
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


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceInput(BaseValidatorModel):
    resourceArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'reject_environment_account_connection' function.
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


# This class is the input for the 'update_component' function.
class UpdateComponentInput(BaseValidatorModel):
    deploymentType: ComponentDeploymentUpdateTypeType
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    serviceInstanceName: Optional[str] = None
    serviceName: Optional[str] = None
    serviceSpec: Optional[str] = None
    templateFile: Optional[str] = None


# This class is the input for the 'update_environment_account_connection' function.
class UpdateEnvironmentAccountConnectionInput(BaseValidatorModel):
    id: str
    codebuildRoleArn: Optional[str] = None
    componentRoleArn: Optional[str] = None
    roleArn: Optional[str] = None


# This class is the input for the 'update_environment_template' function.
class UpdateEnvironmentTemplateInput(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    displayName: Optional[str] = None


# This class is the input for the 'update_environment_template_version' function.
class UpdateEnvironmentTemplateVersionInput(BaseValidatorModel):
    majorVersion: str
    minorVersion: str
    templateName: str
    description: Optional[str] = None
    status: Optional[TemplateVersionStatusType] = None


# This class is the input for the 'update_service' function.
class UpdateServiceInput(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    spec: Optional[str] = None


# This class is the input for the 'update_service_instance' function.
class UpdateServiceInstanceInput(BaseValidatorModel):
    deploymentType: DeploymentUpdateTypeType
    name: str
    serviceName: str
    clientToken: Optional[str] = None
    spec: Optional[str] = None
    templateMajorVersion: Optional[str] = None
    templateMinorVersion: Optional[str] = None


# This class is the input for the 'update_service_pipeline' function.
class UpdateServicePipelineInput(BaseValidatorModel):
    deploymentType: DeploymentUpdateTypeType
    serviceName: str
    spec: str
    templateMajorVersion: Optional[str] = None
    templateMinorVersion: Optional[str] = None


# This class is the input for the 'update_service_sync_blocker' function.
class UpdateServiceSyncBlockerInput(BaseValidatorModel):
    id: str
    resolvedReason: str


# This class is the input for the 'update_service_sync_config' function.
class UpdateServiceSyncConfigInput(BaseValidatorModel):
    branch: str
    filePath: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    serviceName: str


# This class is the input for the 'update_service_template' function.
class UpdateServiceTemplateInput(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    displayName: Optional[str] = None


# This class is the input for the 'update_template_sync_config' function.
class UpdateTemplateSyncConfigInput(BaseValidatorModel):
    branch: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    templateName: str
    templateType: TemplateTypeType
    subdirectory: Optional[str] = None


# This class is the output for the 'accept_environment_account_connection' function.
class AcceptEnvironmentAccountConnectionOutput(BaseValidatorModel):
    environmentAccountConnection: EnvironmentAccountConnection
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_environment_account_connection' function.
class CreateEnvironmentAccountConnectionOutput(BaseValidatorModel):
    environmentAccountConnection: EnvironmentAccountConnection
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_environment_account_connection' function.
class DeleteEnvironmentAccountConnectionOutput(BaseValidatorModel):
    environmentAccountConnection: EnvironmentAccountConnection
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_environment_account_connection' function.
class GetEnvironmentAccountConnectionOutput(BaseValidatorModel):
    environmentAccountConnection: EnvironmentAccountConnection
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reject_environment_account_connection' function.
class RejectEnvironmentAccountConnectionOutput(BaseValidatorModel):
    environmentAccountConnection: EnvironmentAccountConnection
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_environment_account_connection' function.
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


# This class is the output for the 'cancel_component_deployment' function.
class CancelComponentDeploymentOutput(BaseValidatorModel):
    component: Component
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_component' function.
class CreateComponentOutput(BaseValidatorModel):
    component: Component
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_component' function.
class DeleteComponentOutput(BaseValidatorModel):
    component: Component
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_component' function.
class GetComponentOutput(BaseValidatorModel):
    component: Component
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_component' function.
class UpdateComponentOutput(BaseValidatorModel):
    component: Component
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'cancel_service_instance_deployment' function.
class CancelServiceInstanceDeploymentOutput(BaseValidatorModel):
    serviceInstance: ServiceInstance
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_service_instance' function.
class CreateServiceInstanceOutput(BaseValidatorModel):
    serviceInstance: ServiceInstance
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_service_instance' function.
class GetServiceInstanceOutput(BaseValidatorModel):
    serviceInstance: ServiceInstance
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_service_instance' function.
class UpdateServiceInstanceOutput(BaseValidatorModel):
    serviceInstance: ServiceInstance
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'cancel_service_pipeline_deployment' function.
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


# This class is the output for the 'update_service_pipeline' function.
class UpdateServicePipelineOutput(BaseValidatorModel):
    pipeline: ServicePipeline
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_service_template_version' function.
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


# This class is the output for the 'list_components' function.
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


# This class is the input for the 'create_component' function.
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


# This class is the input for the 'create_environment_account_connection' function.
class CreateEnvironmentAccountConnectionInput(BaseValidatorModel):
    environmentName: str
    managementAccountId: str
    clientToken: Optional[str] = None
    codebuildRoleArn: Optional[str] = None
    componentRoleArn: Optional[str] = None
    roleArn: Optional[str] = None
    tags: Optional[List[Tag]] = None


# This class is the input for the 'create_environment_template' function.
class CreateEnvironmentTemplateInput(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    displayName: Optional[str] = None
    encryptionKey: Optional[str] = None
    provisioning: Optional[Literal['CUSTOMER_MANAGED']] = None
    tags: Optional[List[Tag]] = None


# This class is the input for the 'create_repository' function.
class CreateRepositoryInput(BaseValidatorModel):
    connectionArn: str
    name: str
    provider: RepositoryProviderType
    encryptionKey: Optional[str] = None
    tags: Optional[List[Tag]] = None


# This class is the input for the 'create_service' function.
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


# This class is the input for the 'create_service_instance' function.
class CreateServiceInstanceInput(BaseValidatorModel):
    name: str
    serviceName: str
    spec: str
    clientToken: Optional[str] = None
    tags: Optional[List[Tag]] = None
    templateMajorVersion: Optional[str] = None
    templateMinorVersion: Optional[str] = None


# This class is the input for the 'create_service_template' function.
class CreateServiceTemplateInput(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    displayName: Optional[str] = None
    encryptionKey: Optional[str] = None
    pipelineProvisioning: Optional[Literal['CUSTOMER_MANAGED']] = None
    tags: Optional[List[Tag]] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceOutput(BaseValidatorModel):
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class TagResourceInput(BaseValidatorModel):
    resourceArn: str
    tags: List[Tag]


# This class is the input for the 'create_environment' function.
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


# This class is the input for the 'update_account_settings' function.
class UpdateAccountSettingsInput(BaseValidatorModel):
    deletePipelineProvisioningRepository: Optional[bool] = None
    pipelineCodebuildRoleArn: Optional[str] = None
    pipelineProvisioningRepository: Optional[RepositoryBranchInput] = None
    pipelineServiceRoleArn: Optional[str] = None


# This class is the input for the 'update_environment' function.
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


# This class is the output for the 'create_environment_template' function.
class CreateEnvironmentTemplateOutput(BaseValidatorModel):
    environmentTemplate: EnvironmentTemplate
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_environment_template' function.
class DeleteEnvironmentTemplateOutput(BaseValidatorModel):
    environmentTemplate: EnvironmentTemplate
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_environment_template' function.
class GetEnvironmentTemplateOutput(BaseValidatorModel):
    environmentTemplate: EnvironmentTemplate
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_environment_template' function.
class UpdateEnvironmentTemplateOutput(BaseValidatorModel):
    environmentTemplate: EnvironmentTemplate
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_environment_template_version' function.
class CreateEnvironmentTemplateVersionOutput(BaseValidatorModel):
    environmentTemplateVersion: EnvironmentTemplateVersion
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_environment_template_version' function.
class DeleteEnvironmentTemplateVersionOutput(BaseValidatorModel):
    environmentTemplateVersion: EnvironmentTemplateVersion
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_environment_template_version' function.
class GetEnvironmentTemplateVersionOutput(BaseValidatorModel):
    environmentTemplateVersion: EnvironmentTemplateVersion
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_environment_template_version' function.
class UpdateEnvironmentTemplateVersionOutput(BaseValidatorModel):
    environmentTemplateVersion: EnvironmentTemplateVersion
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_repository' function.
class CreateRepositoryOutput(BaseValidatorModel):
    repository: Repository
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_repository' function.
class DeleteRepositoryOutput(BaseValidatorModel):
    repository: Repository
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_repository' function.
class GetRepositoryOutput(BaseValidatorModel):
    repository: Repository
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_service_sync_config' function.
class CreateServiceSyncConfigOutput(BaseValidatorModel):
    serviceSyncConfig: ServiceSyncConfig
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_service_sync_config' function.
class DeleteServiceSyncConfigOutput(BaseValidatorModel):
    serviceSyncConfig: ServiceSyncConfig
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_service_sync_config' function.
class GetServiceSyncConfigOutput(BaseValidatorModel):
    serviceSyncConfig: ServiceSyncConfig
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_service_sync_config' function.
class UpdateServiceSyncConfigOutput(BaseValidatorModel):
    serviceSyncConfig: ServiceSyncConfig
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_service_template' function.
class CreateServiceTemplateOutput(BaseValidatorModel):
    serviceTemplate: ServiceTemplate
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_service_template' function.
class DeleteServiceTemplateOutput(BaseValidatorModel):
    serviceTemplate: ServiceTemplate
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_service_template' function.
class GetServiceTemplateOutput(BaseValidatorModel):
    serviceTemplate: ServiceTemplate
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_service_template' function.
class UpdateServiceTemplateOutput(BaseValidatorModel):
    serviceTemplate: ServiceTemplate
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_template_sync_config' function.
class CreateTemplateSyncConfigOutput(BaseValidatorModel):
    templateSyncConfig: TemplateSyncConfig
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_template_sync_config' function.
class DeleteTemplateSyncConfigOutput(BaseValidatorModel):
    templateSyncConfig: TemplateSyncConfig
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_template_sync_config' function.
class GetTemplateSyncConfigOutput(BaseValidatorModel):
    templateSyncConfig: TemplateSyncConfig
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_template_sync_config' function.
class UpdateTemplateSyncConfigOutput(BaseValidatorModel):
    templateSyncConfig: TemplateSyncConfig
    ResponseMetadata: ResponseMetadata


class DeploymentState(BaseValidatorModel):
    component: Optional[ComponentState] = None
    environment: Optional[EnvironmentState] = None
    serviceInstance: Optional[ServiceInstanceState] = None
    servicePipeline: Optional[ServicePipelineState] = None


# This class is the output for the 'list_deployments' function.
class ListDeploymentsOutput(BaseValidatorModel):
    deployments: List[DeploymentSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_environment_account_connections' function.
class ListEnvironmentAccountConnectionsOutput(BaseValidatorModel):
    environmentAccountConnections: List[EnvironmentAccountConnectionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_environments' function.
class ListEnvironmentsOutput(BaseValidatorModel):
    environments: List[EnvironmentSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'list_environments' function.
class ListEnvironmentsInput(BaseValidatorModel):
    environmentTemplates: Optional[List[EnvironmentTemplateFilter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the output for the 'list_environment_templates' function.
class ListEnvironmentTemplatesOutput(BaseValidatorModel):
    templates: List[EnvironmentTemplateSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_environment_template_versions' function.
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


# This class is the output for the 'list_component_outputs' function.
class ListComponentOutputsOutput(BaseValidatorModel):
    outputs: List[Output]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_environment_outputs' function.
class ListEnvironmentOutputsOutput(BaseValidatorModel):
    outputs: List[Output]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_service_instance_outputs' function.
class ListServiceInstanceOutputsOutput(BaseValidatorModel):
    outputs: List[Output]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_service_pipeline_outputs' function.
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


# This class is the output for the 'list_component_provisioned_resources' function.
class ListComponentProvisionedResourcesOutput(BaseValidatorModel):
    provisionedResources: List[ProvisionedResource]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_environment_provisioned_resources' function.
class ListEnvironmentProvisionedResourcesOutput(BaseValidatorModel):
    provisionedResources: List[ProvisionedResource]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_service_instance_provisioned_resources' function.
class ListServiceInstanceProvisionedResourcesOutput(BaseValidatorModel):
    provisionedResources: List[ProvisionedResource]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_service_pipeline_provisioned_resources' function.
class ListServicePipelineProvisionedResourcesOutput(BaseValidatorModel):
    provisionedResources: List[ProvisionedResource]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_repositories' function.
class ListRepositoriesOutput(BaseValidatorModel):
    repositories: List[RepositorySummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_repository_sync_definitions' function.
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


# This class is the input for the 'list_service_instances' function.
class ListServiceInstancesInput(BaseValidatorModel):
    filters: Optional[List[ListServiceInstancesFilter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    serviceName: Optional[str] = None
    sortBy: Optional[ListServiceInstancesSortByType] = None
    sortOrder: Optional[SortOrderType] = None


# This class is the output for the 'list_service_instances' function.
class ListServiceInstancesOutput(BaseValidatorModel):
    serviceInstances: List[ServiceInstanceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_service_template_versions' function.
class ListServiceTemplateVersionsOutput(BaseValidatorModel):
    templateVersions: List[ServiceTemplateVersionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_service_templates' function.
class ListServiceTemplatesOutput(BaseValidatorModel):
    templates: List[ServiceTemplateSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_services' function.
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


# This class is the output for the 'update_account_settings' function.
class UpdateAccountSettingsOutput(BaseValidatorModel):
    accountSettings: AccountSettings
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'cancel_environment_deployment' function.
class CancelEnvironmentDeploymentOutput(BaseValidatorModel):
    environment: Environment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_environment' function.
class CreateEnvironmentOutput(BaseValidatorModel):
    environment: Environment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_environment' function.
class DeleteEnvironmentOutput(BaseValidatorModel):
    environment: Environment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_environment' function.
class GetEnvironmentOutput(BaseValidatorModel):
    environment: Environment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_environment' function.
class UpdateEnvironmentOutput(BaseValidatorModel):
    environment: Environment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_service' function.
class CreateServiceOutput(BaseValidatorModel):
    service: Service
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_service' function.
class DeleteServiceOutput(BaseValidatorModel):
    service: Service
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_service' function.
class GetServiceOutput(BaseValidatorModel):
    service: Service
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_service' function.
class UpdateServiceOutput(BaseValidatorModel):
    service: Service
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_service_template_version' function.
class CreateServiceTemplateVersionOutput(BaseValidatorModel):
    serviceTemplateVersion: ServiceTemplateVersion
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_service_template_version' function.
class DeleteServiceTemplateVersionOutput(BaseValidatorModel):
    serviceTemplateVersion: ServiceTemplateVersion
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_service_template_version' function.
class GetServiceTemplateVersionOutput(BaseValidatorModel):
    serviceTemplateVersion: ServiceTemplateVersion
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_service_template_version' function.
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


# This class is the output for the 'get_repository_sync_status' function.
class GetRepositorySyncStatusOutput(BaseValidatorModel):
    latestSync: RepositorySyncAttempt
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_service_instance_sync_status' function.
class GetServiceInstanceSyncStatusOutput(BaseValidatorModel):
    desiredState: Revision
    latestSuccessfulSync: ResourceSyncAttempt
    latestSync: ResourceSyncAttempt
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_template_sync_status' function.
class GetTemplateSyncStatusOutput(BaseValidatorModel):
    desiredState: Revision
    latestSuccessfulSync: ResourceSyncAttempt
    latestSync: ResourceSyncAttempt
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_environment_template_version' function.
class CreateEnvironmentTemplateVersionInput(BaseValidatorModel):
    source: TemplateVersionSourceInput
    templateName: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    majorVersion: Optional[str] = None
    tags: Optional[List[Tag]] = None


# This class is the input for the 'create_service_template_version' function.
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


# This class is the output for the 'update_service_sync_blocker' function.
class UpdateServiceSyncBlockerOutput(BaseValidatorModel):
    serviceInstanceName: str
    serviceName: str
    serviceSyncBlocker: SyncBlocker
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_deployment' function.
class DeleteDeploymentOutput(BaseValidatorModel):
    deployment: Deployment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_deployment' function.
class GetDeploymentOutput(BaseValidatorModel):
    deployment: Deployment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_service_sync_blocker_summary' function.
class GetServiceSyncBlockerSummaryOutput(BaseValidatorModel):
    serviceSyncBlockerSummary: ServiceSyncBlockerSummary
    ResponseMetadata: ResponseMetadata
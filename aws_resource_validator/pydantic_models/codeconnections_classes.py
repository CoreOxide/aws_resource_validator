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
from aws_resource_validator.pydantic_models.codeconnections_constants import *

class Connection(BaseValidatorModel):
    ConnectionName: Optional[str] = None
    ConnectionArn: Optional[str] = None
    ProviderType: Optional[ProviderTypeType] = None
    OwnerAccountId: Optional[str] = None
    ConnectionStatus: Optional[ConnectionStatusType] = None
    HostArn: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class RepositoryLinkInfo(BaseValidatorModel):
    ConnectionArn: str
    OwnerId: str
    ProviderType: ProviderTypeType
    RepositoryLinkArn: str
    RepositoryLinkId: str
    RepositoryName: str
    EncryptionKeyArn: Optional[str] = None


class CreateSyncConfigurationInput(BaseValidatorModel):
    Branch: str
    ConfigFile: str
    RepositoryLinkId: str
    ResourceName: str
    RoleArn: str
    SyncType: Literal["CFN_STACK_SYNC"]
    PublishDeploymentStatus: Optional[PublishDeploymentStatusType] = None
    TriggerResourceUpdateOn: Optional[TriggerResourceUpdateOnType] = None
    PullRequestComment: Optional[PullRequestCommentType] = None


class SyncConfiguration(BaseValidatorModel):
    Branch: str
    OwnerId: str
    ProviderType: ProviderTypeType
    RepositoryLinkId: str
    RepositoryName: str
    ResourceName: str
    RoleArn: str
    SyncType: Literal["CFN_STACK_SYNC"]
    ConfigFile: Optional[str] = None
    PublishDeploymentStatus: Optional[PublishDeploymentStatusType] = None
    TriggerResourceUpdateOn: Optional[TriggerResourceUpdateOnType] = None
    PullRequestComment: Optional[PullRequestCommentType] = None


class DeleteConnectionInput(BaseValidatorModel):
    ConnectionArn: str


class DeleteHostInput(BaseValidatorModel):
    HostArn: str


class DeleteRepositoryLinkInput(BaseValidatorModel):
    RepositoryLinkId: str


class DeleteSyncConfigurationInput(BaseValidatorModel):
    SyncType: Literal["CFN_STACK_SYNC"]
    ResourceName: str


class GetConnectionInput(BaseValidatorModel):
    ConnectionArn: str


class GetHostInput(BaseValidatorModel):
    HostArn: str


class VpcConfigurationOutput(BaseValidatorModel):
    VpcId: str
    SubnetIds: List[str]
    SecurityGroupIds: List[str]
    TlsCertificate: Optional[str] = None


class GetRepositoryLinkInput(BaseValidatorModel):
    RepositoryLinkId: str


class GetRepositorySyncStatusInput(BaseValidatorModel):
    Branch: str
    RepositoryLinkId: str
    SyncType: Literal["CFN_STACK_SYNC"]


class GetResourceSyncStatusInput(BaseValidatorModel):
    ResourceName: str
    SyncType: Literal["CFN_STACK_SYNC"]


class Revision(BaseValidatorModel):
    Branch: str
    Directory: str
    OwnerId: str
    RepositoryName: str
    ProviderType: ProviderTypeType
    Sha: str


class GetSyncBlockerSummaryInput(BaseValidatorModel):
    SyncType: Literal["CFN_STACK_SYNC"]
    ResourceName: str


class GetSyncConfigurationInput(BaseValidatorModel):
    SyncType: Literal["CFN_STACK_SYNC"]
    ResourceName: str


class ListConnectionsInput(BaseValidatorModel):
    ProviderTypeFilter: Optional[ProviderTypeType] = None
    HostArnFilter: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListHostsInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListRepositoryLinksInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListRepositorySyncDefinitionsInput(BaseValidatorModel):
    RepositoryLinkId: str
    SyncType: Literal["CFN_STACK_SYNC"]


class RepositorySyncDefinition(BaseValidatorModel):
    Branch: str
    Directory: str
    Parent: str
    Target: str


class ListSyncConfigurationsInput(BaseValidatorModel):
    RepositoryLinkId: str
    SyncType: Literal["CFN_STACK_SYNC"]
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceInput(BaseValidatorModel):
    ResourceArn: str


class SyncBlockerContext(BaseValidatorModel):
    Key: str
    Value: str


class UntagResourceInput(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateRepositoryLinkInput(BaseValidatorModel):
    RepositoryLinkId: str
    ConnectionArn: Optional[str] = None
    EncryptionKeyArn: Optional[str] = None


class UpdateSyncBlockerInput(BaseValidatorModel):
    Id: str
    SyncType: Literal["CFN_STACK_SYNC"]
    ResourceName: str
    ResolvedReason: str


class UpdateSyncConfigurationInput(BaseValidatorModel):
    ResourceName: str
    SyncType: Literal["CFN_STACK_SYNC"]
    Branch: Optional[str] = None
    ConfigFile: Optional[str] = None
    RepositoryLinkId: Optional[str] = None
    RoleArn: Optional[str] = None
    PublishDeploymentStatus: Optional[PublishDeploymentStatusType] = None
    TriggerResourceUpdateOn: Optional[TriggerResourceUpdateOnType] = None
    PullRequestComment: Optional[PullRequestCommentType] = None


class VpcConfiguration(BaseValidatorModel):
    VpcId: str
    SubnetIds: Sequence[str]
    SecurityGroupIds: Sequence[str]
    TlsCertificate: Optional[str] = None


class CreateConnectionInput(BaseValidatorModel):
    ConnectionName: str
    ProviderType: Optional[ProviderTypeType] = None
    Tags: Optional[Sequence[Tag]] = None
    HostArn: Optional[str] = None


class CreateRepositoryLinkInput(BaseValidatorModel):
    ConnectionArn: str
    OwnerId: str
    RepositoryName: str
    EncryptionKeyArn: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class TagResourceInput(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[Tag]


class CreateConnectionOutput(BaseValidatorModel):
    ConnectionArn: str
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class CreateHostOutput(BaseValidatorModel):
    HostArn: str
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class GetConnectionOutput(BaseValidatorModel):
    Connection: Connection
    ResponseMetadata: ResponseMetadata


class ListConnectionsOutput(BaseValidatorModel):
    Connections: List[Connection]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceOutput(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class CreateRepositoryLinkOutput(BaseValidatorModel):
    RepositoryLinkInfo: RepositoryLinkInfo
    ResponseMetadata: ResponseMetadata


class GetRepositoryLinkOutput(BaseValidatorModel):
    RepositoryLinkInfo: RepositoryLinkInfo
    ResponseMetadata: ResponseMetadata


class ListRepositoryLinksOutput(BaseValidatorModel):
    RepositoryLinks: List[RepositoryLinkInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateRepositoryLinkOutput(BaseValidatorModel):
    RepositoryLinkInfo: RepositoryLinkInfo
    ResponseMetadata: ResponseMetadata


class CreateSyncConfigurationOutput(BaseValidatorModel):
    SyncConfiguration: SyncConfiguration
    ResponseMetadata: ResponseMetadata


class GetSyncConfigurationOutput(BaseValidatorModel):
    SyncConfiguration: SyncConfiguration
    ResponseMetadata: ResponseMetadata


class ListSyncConfigurationsOutput(BaseValidatorModel):
    SyncConfigurations: List[SyncConfiguration]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateSyncConfigurationOutput(BaseValidatorModel):
    SyncConfiguration: SyncConfiguration
    ResponseMetadata: ResponseMetadata


class GetHostOutput(BaseValidatorModel):
    Name: str
    Status: str
    ProviderType: ProviderTypeType
    ProviderEndpoint: str
    VpcConfiguration: VpcConfigurationOutput
    ResponseMetadata: ResponseMetadata


class Host(BaseValidatorModel):
    Name: Optional[str] = None
    HostArn: Optional[str] = None
    ProviderType: Optional[ProviderTypeType] = None
    ProviderEndpoint: Optional[str] = None
    VpcConfiguration: Optional[VpcConfigurationOutput] = None
    Status: Optional[str] = None
    StatusMessage: Optional[str] = None


class ListRepositorySyncDefinitionsOutput(BaseValidatorModel):
    RepositorySyncDefinitions: List[RepositorySyncDefinition]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class RepositorySyncEvent(BaseValidatorModel):
    pass


class RepositorySyncAttempt(BaseValidatorModel):
    StartedAt: datetime
    Status: RepositorySyncStatusType
    Events: List[RepositorySyncEvent]


class ResourceSyncEvent(BaseValidatorModel):
    pass


class ResourceSyncAttempt(BaseValidatorModel):
    Events: List[ResourceSyncEvent]
    InitialRevision: Revision
    StartedAt: datetime
    Status: ResourceSyncStatusType
    TargetRevision: Revision
    Target: str


class ListHostsOutput(BaseValidatorModel):
    Hosts: List[Host]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetRepositorySyncStatusOutput(BaseValidatorModel):
    LatestSync: RepositorySyncAttempt
    ResponseMetadata: ResponseMetadata


class GetResourceSyncStatusOutput(BaseValidatorModel):
    DesiredState: Revision
    LatestSuccessfulSync: ResourceSyncAttempt
    LatestSync: ResourceSyncAttempt
    ResponseMetadata: ResponseMetadata


class SyncBlocker(BaseValidatorModel):
    pass


class SyncBlockerSummary(BaseValidatorModel):
    ResourceName: str
    ParentResourceName: Optional[str] = None
    LatestBlockers: Optional[List[SyncBlocker]] = None


class UpdateSyncBlockerOutput(BaseValidatorModel):
    ResourceName: str
    ParentResourceName: str
    SyncBlocker: SyncBlocker
    ResponseMetadata: ResponseMetadata


class VpcConfigurationUnion(BaseValidatorModel):
    pass


class CreateHostInput(BaseValidatorModel):
    Name: str
    ProviderType: ProviderTypeType
    ProviderEndpoint: str
    VpcConfiguration: Optional[VpcConfigurationUnion] = None
    Tags: Optional[Sequence[Tag]] = None


class UpdateHostInput(BaseValidatorModel):
    HostArn: str
    ProviderEndpoint: Optional[str] = None
    VpcConfiguration: Optional[VpcConfigurationUnion] = None


class GetSyncBlockerSummaryOutput(BaseValidatorModel):
    SyncBlockerSummary: SyncBlockerSummary
    ResponseMetadata: ResponseMetadata



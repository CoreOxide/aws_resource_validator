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

class ConnectionTypeDef(BaseValidatorModel):
    ConnectionName: Optional[str] = None
    ConnectionArn: Optional[str] = None
    ProviderType: Optional[ProviderTypeType] = None
    OwnerAccountId: Optional[str] = None
    ConnectionStatus: Optional[ConnectionStatusType] = None
    HostArn: Optional[str] = None


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class RepositoryLinkInfoTypeDef(BaseValidatorModel):
    ConnectionArn: str
    OwnerId: str
    ProviderType: ProviderTypeType
    RepositoryLinkArn: str
    RepositoryLinkId: str
    RepositoryName: str
    EncryptionKeyArn: Optional[str] = None


class CreateSyncConfigurationInputTypeDef(BaseValidatorModel):
    Branch: str
    ConfigFile: str
    RepositoryLinkId: str
    ResourceName: str
    RoleArn: str
    SyncType: Literal["CFN_STACK_SYNC"]
    PublishDeploymentStatus: Optional[PublishDeploymentStatusType] = None
    TriggerResourceUpdateOn: Optional[TriggerResourceUpdateOnType] = None
    PullRequestComment: Optional[PullRequestCommentType] = None


class SyncConfigurationTypeDef(BaseValidatorModel):
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


class DeleteConnectionInputTypeDef(BaseValidatorModel):
    ConnectionArn: str


class DeleteHostInputTypeDef(BaseValidatorModel):
    HostArn: str


class DeleteRepositoryLinkInputTypeDef(BaseValidatorModel):
    RepositoryLinkId: str


class DeleteSyncConfigurationInputTypeDef(BaseValidatorModel):
    SyncType: Literal["CFN_STACK_SYNC"]
    ResourceName: str


class GetConnectionInputTypeDef(BaseValidatorModel):
    ConnectionArn: str


class GetHostInputTypeDef(BaseValidatorModel):
    HostArn: str


class VpcConfigurationOutputTypeDef(BaseValidatorModel):
    VpcId: str
    SubnetIds: List[str]
    SecurityGroupIds: List[str]
    TlsCertificate: Optional[str] = None


class GetRepositoryLinkInputTypeDef(BaseValidatorModel):
    RepositoryLinkId: str


class GetRepositorySyncStatusInputTypeDef(BaseValidatorModel):
    Branch: str
    RepositoryLinkId: str
    SyncType: Literal["CFN_STACK_SYNC"]


class GetResourceSyncStatusInputTypeDef(BaseValidatorModel):
    ResourceName: str
    SyncType: Literal["CFN_STACK_SYNC"]


class RevisionTypeDef(BaseValidatorModel):
    Branch: str
    Directory: str
    OwnerId: str
    RepositoryName: str
    ProviderType: ProviderTypeType
    Sha: str


class GetSyncBlockerSummaryInputTypeDef(BaseValidatorModel):
    SyncType: Literal["CFN_STACK_SYNC"]
    ResourceName: str


class GetSyncConfigurationInputTypeDef(BaseValidatorModel):
    SyncType: Literal["CFN_STACK_SYNC"]
    ResourceName: str


class ListConnectionsInputTypeDef(BaseValidatorModel):
    ProviderTypeFilter: Optional[ProviderTypeType] = None
    HostArnFilter: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListHostsInputTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListRepositoryLinksInputTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListRepositorySyncDefinitionsInputTypeDef(BaseValidatorModel):
    RepositoryLinkId: str
    SyncType: Literal["CFN_STACK_SYNC"]


class RepositorySyncDefinitionTypeDef(BaseValidatorModel):
    Branch: str
    Directory: str
    Parent: str
    Target: str


class ListSyncConfigurationsInputTypeDef(BaseValidatorModel):
    RepositoryLinkId: str
    SyncType: Literal["CFN_STACK_SYNC"]
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceInputTypeDef(BaseValidatorModel):
    ResourceArn: str


class SyncBlockerContextTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class UntagResourceInputTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateRepositoryLinkInputTypeDef(BaseValidatorModel):
    RepositoryLinkId: str
    ConnectionArn: Optional[str] = None
    EncryptionKeyArn: Optional[str] = None


class UpdateSyncBlockerInputTypeDef(BaseValidatorModel):
    Id: str
    SyncType: Literal["CFN_STACK_SYNC"]
    ResourceName: str
    ResolvedReason: str


class UpdateSyncConfigurationInputTypeDef(BaseValidatorModel):
    ResourceName: str
    SyncType: Literal["CFN_STACK_SYNC"]
    Branch: Optional[str] = None
    ConfigFile: Optional[str] = None
    RepositoryLinkId: Optional[str] = None
    RoleArn: Optional[str] = None
    PublishDeploymentStatus: Optional[PublishDeploymentStatusType] = None
    TriggerResourceUpdateOn: Optional[TriggerResourceUpdateOnType] = None
    PullRequestComment: Optional[PullRequestCommentType] = None


class VpcConfigurationTypeDef(BaseValidatorModel):
    VpcId: str
    SubnetIds: Sequence[str]
    SecurityGroupIds: Sequence[str]
    TlsCertificate: Optional[str] = None


class CreateConnectionInputTypeDef(BaseValidatorModel):
    ConnectionName: str
    ProviderType: Optional[ProviderTypeType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    HostArn: Optional[str] = None


class CreateRepositoryLinkInputTypeDef(BaseValidatorModel):
    ConnectionArn: str
    OwnerId: str
    RepositoryName: str
    EncryptionKeyArn: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class TagResourceInputTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]


class CreateConnectionOutputTypeDef(BaseValidatorModel):
    ConnectionArn: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateHostOutputTypeDef(BaseValidatorModel):
    HostArn: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetConnectionOutputTypeDef(BaseValidatorModel):
    Connection: ConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListConnectionsOutputTypeDef(BaseValidatorModel):
    Connections: List[ConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateRepositoryLinkOutputTypeDef(BaseValidatorModel):
    RepositoryLinkInfo: RepositoryLinkInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetRepositoryLinkOutputTypeDef(BaseValidatorModel):
    RepositoryLinkInfo: RepositoryLinkInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListRepositoryLinksOutputTypeDef(BaseValidatorModel):
    RepositoryLinks: List[RepositoryLinkInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateRepositoryLinkOutputTypeDef(BaseValidatorModel):
    RepositoryLinkInfo: RepositoryLinkInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateSyncConfigurationOutputTypeDef(BaseValidatorModel):
    SyncConfiguration: SyncConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetSyncConfigurationOutputTypeDef(BaseValidatorModel):
    SyncConfiguration: SyncConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListSyncConfigurationsOutputTypeDef(BaseValidatorModel):
    SyncConfigurations: List[SyncConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateSyncConfigurationOutputTypeDef(BaseValidatorModel):
    SyncConfiguration: SyncConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetHostOutputTypeDef(BaseValidatorModel):
    Name: str
    Status: str
    ProviderType: ProviderTypeType
    ProviderEndpoint: str
    VpcConfiguration: VpcConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class HostTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    HostArn: Optional[str] = None
    ProviderType: Optional[ProviderTypeType] = None
    ProviderEndpoint: Optional[str] = None
    VpcConfiguration: Optional[VpcConfigurationOutputTypeDef] = None
    Status: Optional[str] = None
    StatusMessage: Optional[str] = None


class ListRepositorySyncDefinitionsOutputTypeDef(BaseValidatorModel):
    RepositorySyncDefinitions: List[RepositorySyncDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class RepositorySyncEventTypeDef(BaseValidatorModel):
    pass


class RepositorySyncAttemptTypeDef(BaseValidatorModel):
    StartedAt: datetime
    Status: RepositorySyncStatusType
    Events: List[RepositorySyncEventTypeDef]


class ResourceSyncEventTypeDef(BaseValidatorModel):
    pass


class ResourceSyncAttemptTypeDef(BaseValidatorModel):
    Events: List[ResourceSyncEventTypeDef]
    InitialRevision: RevisionTypeDef
    StartedAt: datetime
    Status: ResourceSyncStatusType
    TargetRevision: RevisionTypeDef
    Target: str


class ListHostsOutputTypeDef(BaseValidatorModel):
    Hosts: List[HostTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetRepositorySyncStatusOutputTypeDef(BaseValidatorModel):
    LatestSync: RepositorySyncAttemptTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetResourceSyncStatusOutputTypeDef(BaseValidatorModel):
    DesiredState: RevisionTypeDef
    LatestSuccessfulSync: ResourceSyncAttemptTypeDef
    LatestSync: ResourceSyncAttemptTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SyncBlockerTypeDef(BaseValidatorModel):
    pass


class SyncBlockerSummaryTypeDef(BaseValidatorModel):
    ResourceName: str
    ParentResourceName: Optional[str] = None
    LatestBlockers: Optional[List[SyncBlockerTypeDef]] = None


class UpdateSyncBlockerOutputTypeDef(BaseValidatorModel):
    ResourceName: str
    ParentResourceName: str
    SyncBlocker: SyncBlockerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class VpcConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateHostInputTypeDef(BaseValidatorModel):
    Name: str
    ProviderType: ProviderTypeType
    ProviderEndpoint: str
    VpcConfiguration: Optional[VpcConfigurationUnionTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class UpdateHostInputTypeDef(BaseValidatorModel):
    HostArn: str
    ProviderEndpoint: Optional[str] = None
    VpcConfiguration: Optional[VpcConfigurationUnionTypeDef] = None


class GetSyncBlockerSummaryOutputTypeDef(BaseValidatorModel):
    SyncBlockerSummary: SyncBlockerSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef



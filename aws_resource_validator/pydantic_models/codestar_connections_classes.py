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
from aws_resource_validator.pydantic_models.codestar_connections_constants import *

class ConnectionTypeDef(BaseModel):
    ConnectionName: Optional[str] = None
    ConnectionArn: Optional[str] = None
    ProviderType: Optional[ProviderTypeType] = None
    OwnerAccountId: Optional[str] = None
    ConnectionStatus: Optional[ConnectionStatusType] = None
    HostArn: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class VpcConfigurationTypeDef(BaseModel):
    VpcId: str
    SubnetIds: Sequence[str]
    SecurityGroupIds: Sequence[str]
    TlsCertificate: Optional[str] = None

class RepositoryLinkInfoTypeDef(BaseModel):
    ConnectionArn: str
    OwnerId: str
    ProviderType: ProviderTypeType
    RepositoryLinkArn: str
    RepositoryLinkId: str
    RepositoryName: str
    EncryptionKeyArn: Optional[str] = None

class CreateSyncConfigurationInputRequestTypeDef(BaseModel):
    Branch: str
    ConfigFile: str
    RepositoryLinkId: str
    ResourceName: str
    RoleArn: str
    SyncType: Literal["CFN_STACK_SYNC"]
    PublishDeploymentStatus: Optional[PublishDeploymentStatusType] = None
    TriggerResourceUpdateOn: Optional[TriggerResourceUpdateOnType] = None

class SyncConfigurationTypeDef(BaseModel):
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

class DeleteConnectionInputRequestTypeDef(BaseModel):
    ConnectionArn: str

class DeleteHostInputRequestTypeDef(BaseModel):
    HostArn: str

class DeleteRepositoryLinkInputRequestTypeDef(BaseModel):
    RepositoryLinkId: str

class DeleteSyncConfigurationInputRequestTypeDef(BaseModel):
    SyncType: Literal["CFN_STACK_SYNC"]
    ResourceName: str

class GetConnectionInputRequestTypeDef(BaseModel):
    ConnectionArn: str

class GetHostInputRequestTypeDef(BaseModel):
    HostArn: str

class GetRepositoryLinkInputRequestTypeDef(BaseModel):
    RepositoryLinkId: str

class GetRepositorySyncStatusInputRequestTypeDef(BaseModel):
    Branch: str
    RepositoryLinkId: str
    SyncType: Literal["CFN_STACK_SYNC"]

class GetResourceSyncStatusInputRequestTypeDef(BaseModel):
    ResourceName: str
    SyncType: Literal["CFN_STACK_SYNC"]

class RevisionTypeDef(BaseModel):
    Branch: str
    Directory: str
    OwnerId: str
    RepositoryName: str
    ProviderType: ProviderTypeType
    Sha: str

class GetSyncBlockerSummaryInputRequestTypeDef(BaseModel):
    SyncType: Literal["CFN_STACK_SYNC"]
    ResourceName: str

class GetSyncConfigurationInputRequestTypeDef(BaseModel):
    SyncType: Literal["CFN_STACK_SYNC"]
    ResourceName: str

class ListConnectionsInputRequestTypeDef(BaseModel):
    ProviderTypeFilter: Optional[ProviderTypeType] = None
    HostArnFilter: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListHostsInputRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListRepositoryLinksInputRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListRepositorySyncDefinitionsInputRequestTypeDef(BaseModel):
    RepositoryLinkId: str
    SyncType: Literal["CFN_STACK_SYNC"]

class RepositorySyncDefinitionTypeDef(BaseModel):
    Branch: str
    Directory: str
    Parent: str
    Target: str

class ListSyncConfigurationsInputRequestTypeDef(BaseModel):
    RepositoryLinkId: str
    SyncType: Literal["CFN_STACK_SYNC"]
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceInputRequestTypeDef(BaseModel):
    ResourceArn: str

class RepositorySyncEventTypeDef(BaseModel):
    Event: str
    Time: datetime
    Type: str
    ExternalId: Optional[str] = None

class ResourceSyncEventTypeDef(BaseModel):
    Event: str
    Time: datetime
    Type: str
    ExternalId: Optional[str] = None

class SyncBlockerContextTypeDef(BaseModel):
    Key: str
    Value: str

class UntagResourceInputRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateRepositoryLinkInputRequestTypeDef(BaseModel):
    RepositoryLinkId: str
    ConnectionArn: Optional[str] = None
    EncryptionKeyArn: Optional[str] = None

class UpdateSyncBlockerInputRequestTypeDef(BaseModel):
    Id: str
    SyncType: Literal["CFN_STACK_SYNC"]
    ResourceName: str
    ResolvedReason: str

class UpdateSyncConfigurationInputRequestTypeDef(BaseModel):
    ResourceName: str
    SyncType: Literal["CFN_STACK_SYNC"]
    Branch: Optional[str] = None
    ConfigFile: Optional[str] = None
    RepositoryLinkId: Optional[str] = None
    RoleArn: Optional[str] = None
    PublishDeploymentStatus: Optional[PublishDeploymentStatusType] = None
    TriggerResourceUpdateOn: Optional[TriggerResourceUpdateOnType] = None

class CreateConnectionInputRequestTypeDef(BaseModel):
    ConnectionName: str
    ProviderType: Optional[ProviderTypeType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    HostArn: Optional[str] = None

class CreateRepositoryLinkInputRequestTypeDef(BaseModel):
    ConnectionArn: str
    OwnerId: str
    RepositoryName: str
    EncryptionKeyArn: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceInputRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CreateConnectionOutputTypeDef(BaseModel):
    ConnectionArn: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHostOutputTypeDef(BaseModel):
    HostArn: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectionOutputTypeDef(BaseModel):
    Connection: ConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListConnectionsOutputTypeDef(BaseModel):
    Connections: List[ConnectionTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHostInputRequestTypeDef(BaseModel):
    Name: str
    ProviderType: ProviderTypeType
    ProviderEndpoint: str
    VpcConfiguration: Optional[VpcConfigurationTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class GetHostOutputTypeDef(BaseModel):
    Name: str
    Status: str
    ProviderType: ProviderTypeType
    ProviderEndpoint: str
    VpcConfiguration: VpcConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class HostTypeDef(BaseModel):
    Name: Optional[str] = None
    HostArn: Optional[str] = None
    ProviderType: Optional[ProviderTypeType] = None
    ProviderEndpoint: Optional[str] = None
    VpcConfiguration: Optional[VpcConfigurationTypeDef] = None
    Status: Optional[str] = None
    StatusMessage: Optional[str] = None

class UpdateHostInputRequestTypeDef(BaseModel):
    HostArn: str
    ProviderEndpoint: Optional[str] = None
    VpcConfiguration: Optional[VpcConfigurationTypeDef] = None

class CreateRepositoryLinkOutputTypeDef(BaseModel):
    RepositoryLinkInfo: RepositoryLinkInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRepositoryLinkOutputTypeDef(BaseModel):
    RepositoryLinkInfo: RepositoryLinkInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRepositoryLinksOutputTypeDef(BaseModel):
    RepositoryLinks: List[RepositoryLinkInfoTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRepositoryLinkOutputTypeDef(BaseModel):
    RepositoryLinkInfo: RepositoryLinkInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSyncConfigurationOutputTypeDef(BaseModel):
    SyncConfiguration: SyncConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSyncConfigurationOutputTypeDef(BaseModel):
    SyncConfiguration: SyncConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSyncConfigurationsOutputTypeDef(BaseModel):
    SyncConfigurations: List[SyncConfigurationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSyncConfigurationOutputTypeDef(BaseModel):
    SyncConfiguration: SyncConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRepositorySyncDefinitionsOutputTypeDef(BaseModel):
    RepositorySyncDefinitions: List[RepositorySyncDefinitionTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RepositorySyncAttemptTypeDef(BaseModel):
    StartedAt: datetime
    Status: RepositorySyncStatusType
    Events: List[RepositorySyncEventTypeDef]

class ResourceSyncAttemptTypeDef(BaseModel):
    Events: List[ResourceSyncEventTypeDef]
    InitialRevision: RevisionTypeDef
    StartedAt: datetime
    Status: ResourceSyncStatusType
    TargetRevision: RevisionTypeDef
    Target: str

class SyncBlockerTypeDef(BaseModel):
    Id: str
    Type: Literal["AUTOMATED"]
    Status: BlockerStatusType
    CreatedReason: str
    CreatedAt: datetime
    Contexts: Optional[List[SyncBlockerContextTypeDef]] = None
    ResolvedReason: Optional[str] = None
    ResolvedAt: Optional[datetime] = None

class ListHostsOutputTypeDef(BaseModel):
    Hosts: List[HostTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRepositorySyncStatusOutputTypeDef(BaseModel):
    LatestSync: RepositorySyncAttemptTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourceSyncStatusOutputTypeDef(BaseModel):
    DesiredState: RevisionTypeDef
    LatestSuccessfulSync: ResourceSyncAttemptTypeDef
    LatestSync: ResourceSyncAttemptTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SyncBlockerSummaryTypeDef(BaseModel):
    ResourceName: str
    ParentResourceName: Optional[str] = None
    LatestBlockers: Optional[List[SyncBlockerTypeDef]] = None

class UpdateSyncBlockerOutputTypeDef(BaseModel):
    ResourceName: str
    ParentResourceName: str
    SyncBlocker: SyncBlockerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSyncBlockerSummaryOutputTypeDef(BaseModel):
    SyncBlockerSummary: SyncBlockerSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


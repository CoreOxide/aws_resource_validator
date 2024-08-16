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
from aws_resource_validator.pydantic_models.nimble_constants import *

class AcceptEulasRequestRequestTypeDef(BaseValidatorModel):
    studioId: str
    clientToken: Optional[str] = None
    eulaIds: Optional[Sequence[str]] = None

class EulaAcceptanceTypeDef(BaseValidatorModel):
    acceptedAt: Optional[datetime] = None
    acceptedBy: Optional[str] = None
    accepteeId: Optional[str] = None
    eulaAcceptanceId: Optional[str] = None
    eulaId: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class ActiveDirectoryComputerAttributeTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    value: Optional[str] = None

class ComputeFarmConfigurationTypeDef(BaseValidatorModel):
    activeDirectoryUser: Optional[str] = None
    endpoint: Optional[str] = None

class CreateStreamingImageRequestRequestTypeDef(BaseValidatorModel):
    ec2ImageId: str
    name: str
    studioId: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateStreamingSessionRequestRequestTypeDef(BaseValidatorModel):
    launchProfileId: str
    studioId: str
    clientToken: Optional[str] = None
    ec2InstanceType: Optional[StreamingInstanceTypeType] = None
    ownedBy: Optional[str] = None
    streamingImageId: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateStreamingSessionStreamRequestRequestTypeDef(BaseValidatorModel):
    sessionId: str
    studioId: str
    clientToken: Optional[str] = None
    expirationInSeconds: Optional[int] = None

class StreamingSessionStreamTypeDef(BaseValidatorModel):
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    expiresAt: Optional[datetime] = None
    ownedBy: Optional[str] = None
    state: Optional[StreamingSessionStreamStateType] = None
    statusCode: Optional[StreamingSessionStreamStatusCodeType] = None
    streamId: Optional[str] = None
    url: Optional[str] = None

class ScriptParameterKeyValueTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None

class StudioComponentInitializationScriptTypeDef(BaseValidatorModel):
    launchProfileProtocolVersion: Optional[str] = None
    platform: Optional[LaunchProfilePlatformType] = None
    runContext: Optional[StudioComponentInitializationScriptRunContextType] = None
    script: Optional[str] = None

class StudioEncryptionConfigurationTypeDef(BaseValidatorModel):
    keyType: StudioEncryptionConfigurationKeyTypeType
    keyArn: Optional[str] = None

class DeleteLaunchProfileMemberRequestRequestTypeDef(BaseValidatorModel):
    launchProfileId: str
    principalId: str
    studioId: str
    clientToken: Optional[str] = None

class DeleteLaunchProfileRequestRequestTypeDef(BaseValidatorModel):
    launchProfileId: str
    studioId: str
    clientToken: Optional[str] = None

class DeleteStreamingImageRequestRequestTypeDef(BaseValidatorModel):
    streamingImageId: str
    studioId: str
    clientToken: Optional[str] = None

class DeleteStreamingSessionRequestRequestTypeDef(BaseValidatorModel):
    sessionId: str
    studioId: str
    clientToken: Optional[str] = None

class DeleteStudioComponentRequestRequestTypeDef(BaseValidatorModel):
    studioComponentId: str
    studioId: str
    clientToken: Optional[str] = None

class DeleteStudioMemberRequestRequestTypeDef(BaseValidatorModel):
    principalId: str
    studioId: str
    clientToken: Optional[str] = None

class DeleteStudioRequestRequestTypeDef(BaseValidatorModel):
    studioId: str
    clientToken: Optional[str] = None

class EulaTypeDef(BaseValidatorModel):
    content: Optional[str] = None
    createdAt: Optional[datetime] = None
    eulaId: Optional[str] = None
    name: Optional[str] = None
    updatedAt: Optional[datetime] = None

class GetEulaRequestRequestTypeDef(BaseValidatorModel):
    eulaId: str

class GetLaunchProfileDetailsRequestRequestTypeDef(BaseValidatorModel):
    launchProfileId: str
    studioId: str

class StudioComponentSummaryTypeDef(BaseValidatorModel):
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    description: Optional[str] = None
    name: Optional[str] = None
    studioComponentId: Optional[str] = None
    subtype: Optional[StudioComponentSubtypeType] = None
    type: Optional[StudioComponentTypeType] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None

class GetLaunchProfileInitializationRequestRequestTypeDef(BaseValidatorModel):
    launchProfileId: str
    launchProfileProtocolVersions: Sequence[str]
    launchPurpose: str
    platform: str
    studioId: str

class GetLaunchProfileMemberRequestRequestTypeDef(BaseValidatorModel):
    launchProfileId: str
    principalId: str
    studioId: str

class LaunchProfileMembershipTypeDef(BaseValidatorModel):
    identityStoreId: Optional[str] = None
    persona: Optional[Literal["USER"]] = None
    principalId: Optional[str] = None
    sid: Optional[str] = None

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class GetLaunchProfileRequestRequestTypeDef(BaseValidatorModel):
    launchProfileId: str
    studioId: str

class GetStreamingImageRequestRequestTypeDef(BaseValidatorModel):
    streamingImageId: str
    studioId: str

class GetStreamingSessionBackupRequestRequestTypeDef(BaseValidatorModel):
    backupId: str
    studioId: str

class StreamingSessionBackupTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    backupId: Optional[str] = None
    createdAt: Optional[datetime] = None
    launchProfileId: Optional[str] = None
    ownedBy: Optional[str] = None
    sessionId: Optional[str] = None
    state: Optional[StreamingSessionStateType] = None
    statusCode: Optional[StreamingSessionStatusCodeType] = None
    statusMessage: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class GetStreamingSessionRequestRequestTypeDef(BaseValidatorModel):
    sessionId: str
    studioId: str

class GetStreamingSessionStreamRequestRequestTypeDef(BaseValidatorModel):
    sessionId: str
    streamId: str
    studioId: str

class GetStudioComponentRequestRequestTypeDef(BaseValidatorModel):
    studioComponentId: str
    studioId: str

class GetStudioMemberRequestRequestTypeDef(BaseValidatorModel):
    principalId: str
    studioId: str

class StudioMembershipTypeDef(BaseValidatorModel):
    identityStoreId: Optional[str] = None
    persona: Optional[Literal["ADMINISTRATOR"]] = None
    principalId: Optional[str] = None
    sid: Optional[str] = None

class GetStudioRequestRequestTypeDef(BaseValidatorModel):
    studioId: str

class LaunchProfileInitializationScriptTypeDef(BaseValidatorModel):
    runtimeRoleArn: Optional[str] = None
    script: Optional[str] = None
    secureInitializationRoleArn: Optional[str] = None
    studioComponentId: Optional[str] = None
    studioComponentName: Optional[str] = None

class ValidationResultTypeDef(BaseValidatorModel):
    state: LaunchProfileValidationStateType
    statusCode: LaunchProfileValidationStatusCodeType
    statusMessage: str
    type: LaunchProfileValidationTypeType

class LicenseServiceConfigurationTypeDef(BaseValidatorModel):
    endpoint: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListEulaAcceptancesRequestRequestTypeDef(BaseValidatorModel):
    studioId: str
    eulaIds: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None

class ListEulasRequestRequestTypeDef(BaseValidatorModel):
    eulaIds: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None

class ListLaunchProfileMembersRequestRequestTypeDef(BaseValidatorModel):
    launchProfileId: str
    studioId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListLaunchProfilesRequestRequestTypeDef(BaseValidatorModel):
    studioId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    principalId: Optional[str] = None
    states: Optional[Sequence[LaunchProfileStateType]] = None

class ListStreamingImagesRequestRequestTypeDef(BaseValidatorModel):
    studioId: str
    nextToken: Optional[str] = None
    owner: Optional[str] = None

class ListStreamingSessionBackupsRequestRequestTypeDef(BaseValidatorModel):
    studioId: str
    nextToken: Optional[str] = None
    ownedBy: Optional[str] = None

class ListStreamingSessionsRequestRequestTypeDef(BaseValidatorModel):
    studioId: str
    createdBy: Optional[str] = None
    nextToken: Optional[str] = None
    ownedBy: Optional[str] = None
    sessionIds: Optional[str] = None

class ListStudioComponentsRequestRequestTypeDef(BaseValidatorModel):
    studioId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    states: Optional[Sequence[StudioComponentStateType]] = None
    types: Optional[Sequence[StudioComponentTypeType]] = None

class ListStudioMembersRequestRequestTypeDef(BaseValidatorModel):
    studioId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListStudiosRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class NewLaunchProfileMemberTypeDef(BaseValidatorModel):
    persona: Literal["USER"]
    principalId: str

class NewStudioMemberTypeDef(BaseValidatorModel):
    persona: Literal["ADMINISTRATOR"]
    principalId: str

class SharedFileSystemConfigurationTypeDef(BaseValidatorModel):
    endpoint: Optional[str] = None
    fileSystemId: Optional[str] = None
    linuxMountPoint: Optional[str] = None
    shareName: Optional[str] = None
    windowsMountDrive: Optional[str] = None

class StartStreamingSessionRequestRequestTypeDef(BaseValidatorModel):
    sessionId: str
    studioId: str
    backupId: Optional[str] = None
    clientToken: Optional[str] = None

class StartStudioSSOConfigurationRepairRequestRequestTypeDef(BaseValidatorModel):
    studioId: str
    clientToken: Optional[str] = None

class StopStreamingSessionRequestRequestTypeDef(BaseValidatorModel):
    sessionId: str
    studioId: str
    clientToken: Optional[str] = None
    volumeRetentionMode: Optional[VolumeRetentionModeType] = None

class StreamConfigurationSessionBackupTypeDef(BaseValidatorModel):
    maxBackupsToRetain: Optional[int] = None
    mode: Optional[SessionBackupModeType] = None

class VolumeConfigurationTypeDef(BaseValidatorModel):
    iops: Optional[int] = None
    size: Optional[int] = None
    throughput: Optional[int] = None

class StreamingSessionStorageRootTypeDef(BaseValidatorModel):
    linux: Optional[str] = None
    windows: Optional[str] = None

class StreamingImageEncryptionConfigurationTypeDef(BaseValidatorModel):
    keyType: Literal["CUSTOMER_MANAGED_KEY"]
    keyArn: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Optional[Mapping[str, str]] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateLaunchProfileMemberRequestRequestTypeDef(BaseValidatorModel):
    launchProfileId: str
    persona: Literal["USER"]
    principalId: str
    studioId: str
    clientToken: Optional[str] = None

class UpdateStreamingImageRequestRequestTypeDef(BaseValidatorModel):
    streamingImageId: str
    studioId: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    name: Optional[str] = None

class UpdateStudioRequestRequestTypeDef(BaseValidatorModel):
    studioId: str
    adminRoleArn: Optional[str] = None
    clientToken: Optional[str] = None
    displayName: Optional[str] = None
    userRoleArn: Optional[str] = None

class AcceptEulasResponseTypeDef(BaseValidatorModel):
    eulaAcceptances: List[EulaAcceptanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListEulaAcceptancesResponseTypeDef(BaseValidatorModel):
    eulaAcceptances: List[EulaAcceptanceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ActiveDirectoryConfigurationPaginatorTypeDef(BaseValidatorModel):
    computerAttributes: Optional[List[ActiveDirectoryComputerAttributeTypeDef]] = None
    directoryId: Optional[str] = None
    organizationalUnitDistinguishedName: Optional[str] = None

class ActiveDirectoryConfigurationTypeDef(BaseValidatorModel):
    computerAttributes: Optional[Sequence[ActiveDirectoryComputerAttributeTypeDef]] = None
    directoryId: Optional[str] = None
    organizationalUnitDistinguishedName: Optional[str] = None

class LaunchProfileInitializationActiveDirectoryTypeDef(BaseValidatorModel):
    computerAttributes: Optional[List[ActiveDirectoryComputerAttributeTypeDef]] = None
    directoryId: Optional[str] = None
    directoryName: Optional[str] = None
    dnsIpAddresses: Optional[List[str]] = None
    organizationalUnitDistinguishedName: Optional[str] = None
    studioComponentId: Optional[str] = None
    studioComponentName: Optional[str] = None

class CreateStreamingSessionStreamResponseTypeDef(BaseValidatorModel):
    stream: StreamingSessionStreamTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetStreamingSessionStreamResponseTypeDef(BaseValidatorModel):
    stream: StreamingSessionStreamTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStudioRequestRequestTypeDef(BaseValidatorModel):
    adminRoleArn: str
    displayName: str
    studioName: str
    userRoleArn: str
    clientToken: Optional[str] = None
    studioEncryptionConfiguration: Optional[StudioEncryptionConfigurationTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class StudioTypeDef(BaseValidatorModel):
    adminRoleArn: Optional[str] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    displayName: Optional[str] = None
    homeRegion: Optional[str] = None
    ssoClientId: Optional[str] = None
    state: Optional[StudioStateType] = None
    statusCode: Optional[StudioStatusCodeType] = None
    statusMessage: Optional[str] = None
    studioEncryptionConfiguration: Optional[StudioEncryptionConfigurationTypeDef] = None
    studioId: Optional[str] = None
    studioName: Optional[str] = None
    studioUrl: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    updatedAt: Optional[datetime] = None
    userRoleArn: Optional[str] = None

class GetEulaResponseTypeDef(BaseValidatorModel):
    eula: EulaTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEulasResponseTypeDef(BaseValidatorModel):
    eulas: List[EulaTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetLaunchProfileMemberResponseTypeDef(BaseValidatorModel):
    member: LaunchProfileMembershipTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListLaunchProfileMembersResponseTypeDef(BaseValidatorModel):
    members: List[LaunchProfileMembershipTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLaunchProfileMemberResponseTypeDef(BaseValidatorModel):
    member: LaunchProfileMembershipTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetLaunchProfileRequestLaunchProfileDeletedWaitTypeDef(BaseValidatorModel):
    launchProfileId: str
    studioId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetLaunchProfileRequestLaunchProfileReadyWaitTypeDef(BaseValidatorModel):
    launchProfileId: str
    studioId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetStreamingImageRequestStreamingImageDeletedWaitTypeDef(BaseValidatorModel):
    streamingImageId: str
    studioId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetStreamingImageRequestStreamingImageReadyWaitTypeDef(BaseValidatorModel):
    streamingImageId: str
    studioId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetStreamingSessionRequestStreamingSessionDeletedWaitTypeDef(BaseValidatorModel):
    sessionId: str
    studioId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetStreamingSessionRequestStreamingSessionReadyWaitTypeDef(BaseValidatorModel):
    sessionId: str
    studioId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetStreamingSessionRequestStreamingSessionStoppedWaitTypeDef(BaseValidatorModel):
    sessionId: str
    studioId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetStreamingSessionStreamRequestStreamingSessionStreamReadyWaitTypeDef(BaseValidatorModel):
    sessionId: str
    streamId: str
    studioId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetStudioComponentRequestStudioComponentDeletedWaitTypeDef(BaseValidatorModel):
    studioComponentId: str
    studioId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetStudioComponentRequestStudioComponentReadyWaitTypeDef(BaseValidatorModel):
    studioComponentId: str
    studioId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetStudioRequestStudioDeletedWaitTypeDef(BaseValidatorModel):
    studioId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetStudioRequestStudioReadyWaitTypeDef(BaseValidatorModel):
    studioId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetStreamingSessionBackupResponseTypeDef(BaseValidatorModel):
    streamingSessionBackup: StreamingSessionBackupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListStreamingSessionBackupsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    streamingSessionBackups: List[StreamingSessionBackupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetStudioMemberResponseTypeDef(BaseValidatorModel):
    member: StudioMembershipTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListStudioMembersResponseTypeDef(BaseValidatorModel):
    members: List[StudioMembershipTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEulaAcceptancesRequestListEulaAcceptancesPaginateTypeDef(BaseValidatorModel):
    studioId: str
    eulaIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEulasRequestListEulasPaginateTypeDef(BaseValidatorModel):
    eulaIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLaunchProfileMembersRequestListLaunchProfileMembersPaginateTypeDef(BaseValidatorModel):
    launchProfileId: str
    studioId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLaunchProfilesRequestListLaunchProfilesPaginateTypeDef(BaseValidatorModel):
    studioId: str
    principalId: Optional[str] = None
    states: Optional[Sequence[LaunchProfileStateType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStreamingImagesRequestListStreamingImagesPaginateTypeDef(BaseValidatorModel):
    studioId: str
    owner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStreamingSessionBackupsRequestListStreamingSessionBackupsPaginateTypeDef(BaseValidatorModel):
    studioId: str
    ownedBy: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStreamingSessionsRequestListStreamingSessionsPaginateTypeDef(BaseValidatorModel):
    studioId: str
    createdBy: Optional[str] = None
    ownedBy: Optional[str] = None
    sessionIds: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStudioComponentsRequestListStudioComponentsPaginateTypeDef(BaseValidatorModel):
    studioId: str
    states: Optional[Sequence[StudioComponentStateType]] = None
    types: Optional[Sequence[StudioComponentTypeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStudioMembersRequestListStudioMembersPaginateTypeDef(BaseValidatorModel):
    studioId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStudiosRequestListStudiosPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class PutLaunchProfileMembersRequestRequestTypeDef(BaseValidatorModel):
    identityStoreId: str
    launchProfileId: str
    members: Sequence[NewLaunchProfileMemberTypeDef]
    studioId: str
    clientToken: Optional[str] = None

class PutStudioMembersRequestRequestTypeDef(BaseValidatorModel):
    identityStoreId: str
    members: Sequence[NewStudioMemberTypeDef]
    studioId: str
    clientToken: Optional[str] = None

class StreamingSessionTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    automaticTerminationMode: Optional[AutomaticTerminationModeType] = None
    backupMode: Optional[SessionBackupModeType] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    ec2InstanceType: Optional[str] = None
    launchProfileId: Optional[str] = None
    maxBackupsToRetain: Optional[int] = None
    ownedBy: Optional[str] = None
    sessionId: Optional[str] = None
    sessionPersistenceMode: Optional[SessionPersistenceModeType] = None
    startedAt: Optional[datetime] = None
    startedBy: Optional[str] = None
    startedFromBackupId: Optional[str] = None
    state: Optional[StreamingSessionStateType] = None
    statusCode: Optional[StreamingSessionStatusCodeType] = None
    statusMessage: Optional[str] = None
    stopAt: Optional[datetime] = None
    stoppedAt: Optional[datetime] = None
    stoppedBy: Optional[str] = None
    streamingImageId: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    terminateAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None
    volumeConfiguration: Optional[VolumeConfigurationTypeDef] = None
    volumeRetentionMode: Optional[VolumeRetentionModeType] = None

class StreamConfigurationSessionStoragePaginatorTypeDef(BaseValidatorModel):
    mode: List[Literal["UPLOAD"]]
    root: Optional[StreamingSessionStorageRootTypeDef] = None

class StreamConfigurationSessionStorageTypeDef(BaseValidatorModel):
    mode: Sequence[Literal["UPLOAD"]]
    root: Optional[StreamingSessionStorageRootTypeDef] = None

class StreamingImageTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    description: Optional[str] = None
    ec2ImageId: Optional[str] = None
    encryptionConfiguration: Optional[StreamingImageEncryptionConfigurationTypeDef] = None
    eulaIds: Optional[List[str]] = None
    name: Optional[str] = None
    owner: Optional[str] = None
    platform: Optional[str] = None
    state: Optional[StreamingImageStateType] = None
    statusCode: Optional[StreamingImageStatusCodeType] = None
    statusMessage: Optional[str] = None
    streamingImageId: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class StudioComponentConfigurationPaginatorTypeDef(BaseValidatorModel):
    activeDirectoryConfiguration: Optional[ActiveDirectoryConfigurationPaginatorTypeDef] = None
    computeFarmConfiguration: Optional[ComputeFarmConfigurationTypeDef] = None
    licenseServiceConfiguration: Optional[LicenseServiceConfigurationTypeDef] = None
    sharedFileSystemConfiguration: Optional[SharedFileSystemConfigurationTypeDef] = None

class StudioComponentConfigurationTypeDef(BaseValidatorModel):
    activeDirectoryConfiguration: Optional[ActiveDirectoryConfigurationTypeDef] = None
    computeFarmConfiguration: Optional[ComputeFarmConfigurationTypeDef] = None
    licenseServiceConfiguration: Optional[LicenseServiceConfigurationTypeDef] = None
    sharedFileSystemConfiguration: Optional[SharedFileSystemConfigurationTypeDef] = None

class LaunchProfileInitializationTypeDef(BaseValidatorModel):
    activeDirectory: Optional[LaunchProfileInitializationActiveDirectoryTypeDef] = None
    ec2SecurityGroupIds: Optional[List[str]] = None
    launchProfileId: Optional[str] = None
    launchProfileProtocolVersion: Optional[str] = None
    launchPurpose: Optional[str] = None
    name: Optional[str] = None
    platform: Optional[LaunchProfilePlatformType] = None
    systemInitializationScripts: Optional[List[LaunchProfileInitializationScriptTypeDef]] = None
    userInitializationScripts: Optional[List[LaunchProfileInitializationScriptTypeDef]] = None

class CreateStudioResponseTypeDef(BaseValidatorModel):
    studio: StudioTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteStudioResponseTypeDef(BaseValidatorModel):
    studio: StudioTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetStudioResponseTypeDef(BaseValidatorModel):
    studio: StudioTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListStudiosResponseTypeDef(BaseValidatorModel):
    nextToken: str
    studios: List[StudioTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartStudioSSOConfigurationRepairResponseTypeDef(BaseValidatorModel):
    studio: StudioTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateStudioResponseTypeDef(BaseValidatorModel):
    studio: StudioTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStreamingSessionResponseTypeDef(BaseValidatorModel):
    session: StreamingSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteStreamingSessionResponseTypeDef(BaseValidatorModel):
    session: StreamingSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetStreamingSessionResponseTypeDef(BaseValidatorModel):
    session: StreamingSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListStreamingSessionsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    sessions: List[StreamingSessionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartStreamingSessionResponseTypeDef(BaseValidatorModel):
    session: StreamingSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopStreamingSessionResponseTypeDef(BaseValidatorModel):
    session: StreamingSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StreamConfigurationPaginatorTypeDef(BaseValidatorModel):
    clipboardMode: StreamingClipboardModeType
    ec2InstanceTypes: List[StreamingInstanceTypeType]
    streamingImageIds: List[str]
    automaticTerminationMode: Optional[AutomaticTerminationModeType] = None
    maxSessionLengthInMinutes: Optional[int] = None
    maxStoppedSessionLengthInMinutes: Optional[int] = None
    sessionBackup: Optional[StreamConfigurationSessionBackupTypeDef] = None
    sessionPersistenceMode: Optional[SessionPersistenceModeType] = None
    sessionStorage: Optional[StreamConfigurationSessionStoragePaginatorTypeDef] = None
    volumeConfiguration: Optional[VolumeConfigurationTypeDef] = None

class StreamConfigurationCreateTypeDef(BaseValidatorModel):
    clipboardMode: StreamingClipboardModeType
    ec2InstanceTypes: Sequence[StreamingInstanceTypeType]
    streamingImageIds: Sequence[str]
    automaticTerminationMode: Optional[AutomaticTerminationModeType] = None
    maxSessionLengthInMinutes: Optional[int] = None
    maxStoppedSessionLengthInMinutes: Optional[int] = None
    sessionBackup: Optional[StreamConfigurationSessionBackupTypeDef] = None
    sessionPersistenceMode: Optional[SessionPersistenceModeType] = None
    sessionStorage: Optional[StreamConfigurationSessionStorageTypeDef] = None
    volumeConfiguration: Optional[VolumeConfigurationTypeDef] = None

class StreamConfigurationTypeDef(BaseValidatorModel):
    clipboardMode: StreamingClipboardModeType
    ec2InstanceTypes: List[StreamingInstanceTypeType]
    streamingImageIds: List[str]
    automaticTerminationMode: Optional[AutomaticTerminationModeType] = None
    maxSessionLengthInMinutes: Optional[int] = None
    maxStoppedSessionLengthInMinutes: Optional[int] = None
    sessionBackup: Optional[StreamConfigurationSessionBackupTypeDef] = None
    sessionPersistenceMode: Optional[SessionPersistenceModeType] = None
    sessionStorage: Optional[StreamConfigurationSessionStorageTypeDef] = None
    volumeConfiguration: Optional[VolumeConfigurationTypeDef] = None

class CreateStreamingImageResponseTypeDef(BaseValidatorModel):
    streamingImage: StreamingImageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteStreamingImageResponseTypeDef(BaseValidatorModel):
    streamingImage: StreamingImageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetStreamingImageResponseTypeDef(BaseValidatorModel):
    streamingImage: StreamingImageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListStreamingImagesResponseTypeDef(BaseValidatorModel):
    nextToken: str
    streamingImages: List[StreamingImageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateStreamingImageResponseTypeDef(BaseValidatorModel):
    streamingImage: StreamingImageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StudioComponentPaginatorTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    configuration: Optional[StudioComponentConfigurationPaginatorTypeDef] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    description: Optional[str] = None
    ec2SecurityGroupIds: Optional[List[str]] = None
    initializationScripts: Optional[List[StudioComponentInitializationScriptTypeDef]] = None
    name: Optional[str] = None
    runtimeRoleArn: Optional[str] = None
    scriptParameters: Optional[List[ScriptParameterKeyValueTypeDef]] = None
    secureInitializationRoleArn: Optional[str] = None
    state: Optional[StudioComponentStateType] = None
    statusCode: Optional[StudioComponentStatusCodeType] = None
    statusMessage: Optional[str] = None
    studioComponentId: Optional[str] = None
    subtype: Optional[StudioComponentSubtypeType] = None
    tags: Optional[Dict[str, str]] = None
    type: Optional[StudioComponentTypeType] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None

class CreateStudioComponentRequestRequestTypeDef(BaseValidatorModel):
    name: str
    studioId: str
    type: StudioComponentTypeType
    clientToken: Optional[str] = None
    configuration: Optional[StudioComponentConfigurationTypeDef] = None
    description: Optional[str] = None
    ec2SecurityGroupIds: Optional[Sequence[str]] = None
    initializationScripts: Optional[Sequence[StudioComponentInitializationScriptTypeDef]] = None
    runtimeRoleArn: Optional[str] = None
    scriptParameters: Optional[Sequence[ScriptParameterKeyValueTypeDef]] = None
    secureInitializationRoleArn: Optional[str] = None
    subtype: Optional[StudioComponentSubtypeType] = None
    tags: Optional[Mapping[str, str]] = None

class StudioComponentTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    configuration: Optional[StudioComponentConfigurationTypeDef] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    description: Optional[str] = None
    ec2SecurityGroupIds: Optional[List[str]] = None
    initializationScripts: Optional[List[StudioComponentInitializationScriptTypeDef]] = None
    name: Optional[str] = None
    runtimeRoleArn: Optional[str] = None
    scriptParameters: Optional[List[ScriptParameterKeyValueTypeDef]] = None
    secureInitializationRoleArn: Optional[str] = None
    state: Optional[StudioComponentStateType] = None
    statusCode: Optional[StudioComponentStatusCodeType] = None
    statusMessage: Optional[str] = None
    studioComponentId: Optional[str] = None
    subtype: Optional[StudioComponentSubtypeType] = None
    tags: Optional[Dict[str, str]] = None
    type: Optional[StudioComponentTypeType] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None

class UpdateStudioComponentRequestRequestTypeDef(BaseValidatorModel):
    studioComponentId: str
    studioId: str
    clientToken: Optional[str] = None
    configuration: Optional[StudioComponentConfigurationTypeDef] = None
    description: Optional[str] = None
    ec2SecurityGroupIds: Optional[Sequence[str]] = None
    initializationScripts: Optional[Sequence[StudioComponentInitializationScriptTypeDef]] = None
    name: Optional[str] = None
    runtimeRoleArn: Optional[str] = None
    scriptParameters: Optional[Sequence[ScriptParameterKeyValueTypeDef]] = None
    secureInitializationRoleArn: Optional[str] = None
    subtype: Optional[StudioComponentSubtypeType] = None
    type: Optional[StudioComponentTypeType] = None

class GetLaunchProfileInitializationResponseTypeDef(BaseValidatorModel):
    launchProfileInitialization: LaunchProfileInitializationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class LaunchProfilePaginatorTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    description: Optional[str] = None
    ec2SubnetIds: Optional[List[str]] = None
    launchProfileId: Optional[str] = None
    launchProfileProtocolVersions: Optional[List[str]] = None
    name: Optional[str] = None
    state: Optional[LaunchProfileStateType] = None
    statusCode: Optional[LaunchProfileStatusCodeType] = None
    statusMessage: Optional[str] = None
    streamConfiguration: Optional[StreamConfigurationPaginatorTypeDef] = None
    studioComponentIds: Optional[List[str]] = None
    tags: Optional[Dict[str, str]] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None
    validationResults: Optional[List[ValidationResultTypeDef]] = None

class CreateLaunchProfileRequestRequestTypeDef(BaseValidatorModel):
    ec2SubnetIds: Sequence[str]
    launchProfileProtocolVersions: Sequence[str]
    name: str
    streamConfiguration: StreamConfigurationCreateTypeDef
    studioComponentIds: Sequence[str]
    studioId: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateLaunchProfileRequestRequestTypeDef(BaseValidatorModel):
    launchProfileId: str
    studioId: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    launchProfileProtocolVersions: Optional[Sequence[str]] = None
    name: Optional[str] = None
    streamConfiguration: Optional[StreamConfigurationCreateTypeDef] = None
    studioComponentIds: Optional[Sequence[str]] = None

class LaunchProfileTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    description: Optional[str] = None
    ec2SubnetIds: Optional[List[str]] = None
    launchProfileId: Optional[str] = None
    launchProfileProtocolVersions: Optional[List[str]] = None
    name: Optional[str] = None
    state: Optional[LaunchProfileStateType] = None
    statusCode: Optional[LaunchProfileStatusCodeType] = None
    statusMessage: Optional[str] = None
    streamConfiguration: Optional[StreamConfigurationTypeDef] = None
    studioComponentIds: Optional[List[str]] = None
    tags: Optional[Dict[str, str]] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None
    validationResults: Optional[List[ValidationResultTypeDef]] = None

class ListStudioComponentsResponsePaginatorTypeDef(BaseValidatorModel):
    nextToken: str
    studioComponents: List[StudioComponentPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStudioComponentResponseTypeDef(BaseValidatorModel):
    studioComponent: StudioComponentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteStudioComponentResponseTypeDef(BaseValidatorModel):
    studioComponent: StudioComponentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetStudioComponentResponseTypeDef(BaseValidatorModel):
    studioComponent: StudioComponentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListStudioComponentsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    studioComponents: List[StudioComponentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateStudioComponentResponseTypeDef(BaseValidatorModel):
    studioComponent: StudioComponentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListLaunchProfilesResponsePaginatorTypeDef(BaseValidatorModel):
    launchProfiles: List[LaunchProfilePaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLaunchProfileResponseTypeDef(BaseValidatorModel):
    launchProfile: LaunchProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteLaunchProfileResponseTypeDef(BaseValidatorModel):
    launchProfile: LaunchProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetLaunchProfileDetailsResponseTypeDef(BaseValidatorModel):
    launchProfile: LaunchProfileTypeDef
    streamingImages: List[StreamingImageTypeDef]
    studioComponentSummaries: List[StudioComponentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetLaunchProfileResponseTypeDef(BaseValidatorModel):
    launchProfile: LaunchProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListLaunchProfilesResponseTypeDef(BaseValidatorModel):
    launchProfiles: List[LaunchProfileTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLaunchProfileResponseTypeDef(BaseValidatorModel):
    launchProfile: LaunchProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


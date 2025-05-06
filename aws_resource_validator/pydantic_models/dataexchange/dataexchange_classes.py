from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.dataexchange.dataexchange_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AcceptDataGrantRequest(BaseValidatorModel):
    DataGrantArn: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ApiGatewayApiAsset(BaseValidatorModel):
    ApiDescription: Optional[str] = None
    ApiEndpoint: Optional[str] = None
    ApiId: Optional[str] = None
    ApiKey: Optional[str] = None
    ApiName: Optional[str] = None
    ApiSpecificationDownloadUrl: Optional[str] = None
    ApiSpecificationDownloadUrlExpiresAt: Optional[datetime] = None
    ProtocolType: Optional[Literal['REST']] = None
    Stage: Optional[str] = None


class AssetDestinationEntry(BaseValidatorModel):
    AssetId: str
    Bucket: str
    Key: Optional[str] = None


class RedshiftDataShareAsset(BaseValidatorModel):
    Arn: str


class S3SnapshotAsset(BaseValidatorModel):
    Size: float


class AssetSourceEntry(BaseValidatorModel):
    Bucket: str
    Key: str


class AutoExportRevisionDestinationEntry(BaseValidatorModel):
    Bucket: str
    KeyPattern: Optional[str] = None


class ExportServerSideEncryption(BaseValidatorModel):
    Type: ServerSideEncryptionTypesType
    KmsKeyArn: Optional[str] = None


class CancelJobRequest(BaseValidatorModel):
    JobId: str

Timestamp = Union[datetime, str]


class CreateDataSetRequest(BaseValidatorModel):
    AssetType: AssetTypeType
    Description: str
    Name: str
    Tags: Optional[Dict[str, str]] = None


class OriginDetails(BaseValidatorModel):
    ProductId: Optional[str] = None
    DataGrantId: Optional[str] = None


class CreateRevisionRequest(BaseValidatorModel):
    DataSetId: str
    Comment: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class DataGrantSummaryEntry(BaseValidatorModel):
    Name: str
    SenderPrincipal: str
    ReceiverPrincipal: str
    AcceptanceState: DataGrantAcceptanceStateType
    DataSetId: str
    SourceDataSetId: str
    Id: str
    Arn: str
    CreatedAt: datetime
    UpdatedAt: datetime
    AcceptedAt: Optional[datetime] = None
    EndsAt: Optional[datetime] = None


class LFTagOutput(BaseValidatorModel):
    TagKey: str
    TagValues: List[str]


class LFTag(BaseValidatorModel):
    TagKey: str
    TagValues: List[str]


class DeleteAssetRequest(BaseValidatorModel):
    AssetId: str
    DataSetId: str
    RevisionId: str


class DeleteDataGrantRequest(BaseValidatorModel):
    DataGrantId: str


class DeleteDataSetRequest(BaseValidatorModel):
    DataSetId: str


class DeleteEventActionRequest(BaseValidatorModel):
    EventActionId: str


class DeleteRevisionRequest(BaseValidatorModel):
    DataSetId: str
    RevisionId: str


class ImportAssetFromSignedUrlJobErrorDetails(BaseValidatorModel):
    AssetName: str


class RevisionPublished(BaseValidatorModel):
    DataSetId: str


class ExportAssetToSignedUrlRequestDetails(BaseValidatorModel):
    AssetId: str
    DataSetId: str
    RevisionId: str


class ExportAssetToSignedUrlResponseDetails(BaseValidatorModel):
    AssetId: str
    DataSetId: str
    RevisionId: str
    SignedUrl: Optional[str] = None
    SignedUrlExpiresAt: Optional[datetime] = None


class RevisionDestinationEntry(BaseValidatorModel):
    Bucket: str
    RevisionId: str
    KeyPattern: Optional[str] = None


class GetAssetRequest(BaseValidatorModel):
    AssetId: str
    DataSetId: str
    RevisionId: str


class GetDataGrantRequest(BaseValidatorModel):
    DataGrantId: str


class GetDataSetRequest(BaseValidatorModel):
    DataSetId: str


class GetEventActionRequest(BaseValidatorModel):
    EventActionId: str


class GetJobRequest(BaseValidatorModel):
    JobId: str


class GetReceivedDataGrantRequest(BaseValidatorModel):
    DataGrantArn: str


class GetRevisionRequest(BaseValidatorModel):
    DataSetId: str
    RevisionId: str


class ImportAssetFromApiGatewayApiRequestDetails(BaseValidatorModel):
    ApiId: str
    ApiName: str
    ApiSpecificationMd5Hash: str
    DataSetId: str
    ProtocolType: Literal['REST']
    RevisionId: str
    Stage: str
    ApiDescription: Optional[str] = None
    ApiKey: Optional[str] = None


class ImportAssetFromApiGatewayApiResponseDetails(BaseValidatorModel):
    ApiId: str
    ApiName: str
    ApiSpecificationMd5Hash: str
    ApiSpecificationUploadUrl: str
    ApiSpecificationUploadUrlExpiresAt: datetime
    DataSetId: str
    ProtocolType: Literal['REST']
    RevisionId: str
    Stage: str
    ApiDescription: Optional[str] = None
    ApiKey: Optional[str] = None


class ImportAssetFromSignedUrlRequestDetails(BaseValidatorModel):
    AssetName: str
    DataSetId: str
    Md5Hash: str
    RevisionId: str


class ImportAssetFromSignedUrlResponseDetails(BaseValidatorModel):
    AssetName: str
    DataSetId: str
    RevisionId: str
    Md5Hash: Optional[str] = None
    SignedUrl: Optional[str] = None
    SignedUrlExpiresAt: Optional[datetime] = None


class RedshiftDataShareAssetSourceEntry(BaseValidatorModel):
    DataShareArn: str


class KmsKeyToGrant(BaseValidatorModel):
    KmsKeyArn: str


class LakeFormationTagPolicyDetails(BaseValidatorModel):
    Database: Optional[str] = None
    Table: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListDataGrantsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListDataSetRevisionsRequest(BaseValidatorModel):
    DataSetId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class RevisionEntry(BaseValidatorModel):
    Arn: str
    CreatedAt: datetime
    DataSetId: str
    Id: str
    UpdatedAt: datetime
    Comment: Optional[str] = None
    Finalized: Optional[bool] = None
    SourceId: Optional[str] = None
    RevocationComment: Optional[str] = None
    Revoked: Optional[bool] = None
    RevokedAt: Optional[datetime] = None


class ListDataSetsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Origin: Optional[str] = None


class ListEventActionsRequest(BaseValidatorModel):
    EventSourceId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListJobsRequest(BaseValidatorModel):
    DataSetId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    RevisionId: Optional[str] = None


class ListReceivedDataGrantsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    AcceptanceState: Optional[List[AcceptanceStateFilterValueType]] = None


class ReceivedDataGrantSummariesEntry(BaseValidatorModel):
    Name: str
    SenderPrincipal: str
    ReceiverPrincipal: str
    AcceptanceState: DataGrantAcceptanceStateType
    DataSetId: str
    Id: str
    Arn: str
    CreatedAt: datetime
    UpdatedAt: datetime
    AcceptedAt: Optional[datetime] = None
    EndsAt: Optional[datetime] = None


class ListRevisionAssetsRequest(BaseValidatorModel):
    DataSetId: str
    RevisionId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class RedshiftDataShareDetails(BaseValidatorModel):
    Arn: str
    Database: str
    Function: Optional[str] = None
    Table: Optional[str] = None
    Schema: Optional[str] = None
    View: Optional[str] = None


class RevokeRevisionRequest(BaseValidatorModel):
    DataSetId: str
    RevisionId: str
    RevocationComment: str


class S3DataAccessDetails(BaseValidatorModel):
    KeyPrefixes: Optional[List[str]] = None
    Keys: Optional[List[str]] = None


class SchemaChangeDetails(BaseValidatorModel):
    Name: str
    Type: SchemaChangeTypeType
    Description: Optional[str] = None


class SendApiAssetRequest(BaseValidatorModel):
    AssetId: str
    DataSetId: str
    RevisionId: str
    Body: Optional[str] = None
    QueryStringParameters: Optional[Dict[str, str]] = None
    RequestHeaders: Optional[Dict[str, str]] = None
    Method: Optional[str] = None
    Path: Optional[str] = None


class StartJobRequest(BaseValidatorModel):
    JobId: str


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class UpdateAssetRequest(BaseValidatorModel):
    AssetId: str
    DataSetId: str
    Name: str
    RevisionId: str


class UpdateDataSetRequest(BaseValidatorModel):
    DataSetId: str
    Description: Optional[str] = None
    Name: Optional[str] = None


class UpdateRevisionRequest(BaseValidatorModel):
    DataSetId: str
    RevisionId: str
    Comment: Optional[str] = None
    Finalized: Optional[bool] = None


class AcceptDataGrantResponse(BaseValidatorModel):
    Name: str
    SenderPrincipal: str
    ReceiverPrincipal: str
    Description: str
    AcceptanceState: DataGrantAcceptanceStateType
    AcceptedAt: datetime
    EndsAt: datetime
    GrantDistributionScope: GrantDistributionScopeType
    DataSetId: str
    Id: str
    Arn: str
    CreatedAt: datetime
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadata


class CreateDataGrantResponse(BaseValidatorModel):
    Name: str
    SenderPrincipal: str
    ReceiverPrincipal: str
    Description: str
    AcceptanceState: DataGrantAcceptanceStateType
    AcceptedAt: datetime
    EndsAt: datetime
    GrantDistributionScope: GrantDistributionScopeType
    DataSetId: str
    SourceDataSetId: str
    Id: str
    Arn: str
    CreatedAt: datetime
    UpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CreateRevisionResponse(BaseValidatorModel):
    Arn: str
    Comment: str
    CreatedAt: datetime
    DataSetId: str
    Finalized: bool
    Id: str
    SourceId: str
    Tags: Dict[str, str]
    UpdatedAt: datetime
    RevocationComment: str
    Revoked: bool
    RevokedAt: datetime
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetDataGrantResponse(BaseValidatorModel):
    Name: str
    SenderPrincipal: str
    ReceiverPrincipal: str
    Description: str
    AcceptanceState: DataGrantAcceptanceStateType
    AcceptedAt: datetime
    EndsAt: datetime
    GrantDistributionScope: GrantDistributionScopeType
    DataSetId: str
    SourceDataSetId: str
    Id: str
    Arn: str
    CreatedAt: datetime
    UpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetReceivedDataGrantResponse(BaseValidatorModel):
    Name: str
    SenderPrincipal: str
    ReceiverPrincipal: str
    Description: str
    AcceptanceState: DataGrantAcceptanceStateType
    AcceptedAt: datetime
    EndsAt: datetime
    GrantDistributionScope: GrantDistributionScopeType
    DataSetId: str
    Id: str
    Arn: str
    CreatedAt: datetime
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadata


class GetRevisionResponse(BaseValidatorModel):
    Arn: str
    Comment: str
    CreatedAt: datetime
    DataSetId: str
    Finalized: bool
    Id: str
    SourceId: str
    Tags: Dict[str, str]
    UpdatedAt: datetime
    RevocationComment: str
    Revoked: bool
    RevokedAt: datetime
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class RevokeRevisionResponse(BaseValidatorModel):
    Arn: str
    Comment: str
    CreatedAt: datetime
    DataSetId: str
    Finalized: bool
    Id: str
    SourceId: str
    UpdatedAt: datetime
    RevocationComment: str
    Revoked: bool
    RevokedAt: datetime
    ResponseMetadata: ResponseMetadata


class SendApiAssetResponse(BaseValidatorModel):
    Body: str
    ResponseHeaders: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UpdateRevisionResponse(BaseValidatorModel):
    Arn: str
    Comment: str
    CreatedAt: datetime
    DataSetId: str
    Finalized: bool
    Id: str
    SourceId: str
    UpdatedAt: datetime
    RevocationComment: str
    Revoked: bool
    RevokedAt: datetime
    ResponseMetadata: ResponseMetadata


class ImportAssetsFromS3RequestDetails(BaseValidatorModel):
    AssetSources: List[AssetSourceEntry]
    DataSetId: str
    RevisionId: str


class ImportAssetsFromS3ResponseDetails(BaseValidatorModel):
    AssetSources: List[AssetSourceEntry]
    DataSetId: str
    RevisionId: str


class AutoExportRevisionToS3RequestDetails(BaseValidatorModel):
    RevisionDestination: AutoExportRevisionDestinationEntry
    Encryption: Optional[ExportServerSideEncryption] = None


class ExportAssetsToS3RequestDetails(BaseValidatorModel):
    AssetDestinations: List[AssetDestinationEntry]
    DataSetId: str
    RevisionId: str
    Encryption: Optional[ExportServerSideEncryption] = None


class ExportAssetsToS3ResponseDetails(BaseValidatorModel):
    AssetDestinations: List[AssetDestinationEntry]
    DataSetId: str
    RevisionId: str
    Encryption: Optional[ExportServerSideEncryption] = None


class CreateDataGrantRequest(BaseValidatorModel):
    Name: str
    GrantDistributionScope: GrantDistributionScopeType
    ReceiverPrincipal: str
    SourceDataSetId: str
    EndsAt: Optional[Timestamp] = None
    Description: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class DataUpdateRequestDetails(BaseValidatorModel):
    DataUpdatedAt: Optional[Timestamp] = None


class DeprecationRequestDetails(BaseValidatorModel):
    DeprecationAt: Timestamp


class CreateDataSetResponse(BaseValidatorModel):
    Arn: str
    AssetType: AssetTypeType
    CreatedAt: datetime
    Description: str
    Id: str
    Name: str
    Origin: OriginType
    OriginDetails: OriginDetails
    SourceId: str
    Tags: Dict[str, str]
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadata


class DataSetEntry(BaseValidatorModel):
    Arn: str
    AssetType: AssetTypeType
    CreatedAt: datetime
    Description: str
    Id: str
    Name: str
    Origin: OriginType
    UpdatedAt: datetime
    OriginDetails: Optional[OriginDetails] = None
    SourceId: Optional[str] = None


class GetDataSetResponse(BaseValidatorModel):
    Arn: str
    AssetType: AssetTypeType
    CreatedAt: datetime
    Description: str
    Id: str
    Name: str
    Origin: OriginType
    OriginDetails: OriginDetails
    SourceId: str
    Tags: Dict[str, str]
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadata


class UpdateDataSetResponse(BaseValidatorModel):
    Arn: str
    AssetType: AssetTypeType
    CreatedAt: datetime
    Description: str
    Id: str
    Name: str
    Origin: OriginType
    OriginDetails: OriginDetails
    SourceId: str
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadata


class ListDataGrantsResponse(BaseValidatorModel):
    DataGrantSummaries: List[DataGrantSummaryEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DatabaseLFTagPolicyAndPermissionsOutput(BaseValidatorModel):
    Expression: List[LFTagOutput]
    Permissions: List[Literal['DESCRIBE']]


class DatabaseLFTagPolicy(BaseValidatorModel):
    Expression: List[LFTagOutput]


class TableLFTagPolicyAndPermissionsOutput(BaseValidatorModel):
    Expression: List[LFTagOutput]
    Permissions: List[TableTagPolicyLFPermissionType]


class TableLFTagPolicy(BaseValidatorModel):
    Expression: List[LFTagOutput]


class DatabaseLFTagPolicyAndPermissions(BaseValidatorModel):
    Expression: List[LFTag]
    Permissions: List[Literal['DESCRIBE']]

LFTagUnion = Union[LFTag, LFTagOutput]


class Details(BaseValidatorModel):
    ImportAssetFromSignedUrlJobErrorDetails: Optional[ImportAssetFromSignedUrlJobErrorDetails] = None
    ImportAssetsFromS3JobErrorDetails: Optional[List[AssetSourceEntry]] = None


class Event(BaseValidatorModel):
    RevisionPublished: Optional[RevisionPublished] = None


class ExportRevisionsToS3RequestDetails(BaseValidatorModel):
    DataSetId: str
    RevisionDestinations: List[RevisionDestinationEntry]
    Encryption: Optional[ExportServerSideEncryption] = None


class ExportRevisionsToS3ResponseDetails(BaseValidatorModel):
    DataSetId: str
    RevisionDestinations: List[RevisionDestinationEntry]
    Encryption: Optional[ExportServerSideEncryption] = None
    EventActionArn: Optional[str] = None


class ImportAssetsFromRedshiftDataSharesRequestDetails(BaseValidatorModel):
    AssetSources: List[RedshiftDataShareAssetSourceEntry]
    DataSetId: str
    RevisionId: str


class ImportAssetsFromRedshiftDataSharesResponseDetails(BaseValidatorModel):
    AssetSources: List[RedshiftDataShareAssetSourceEntry]
    DataSetId: str
    RevisionId: str


class S3DataAccessAssetSourceEntryOutput(BaseValidatorModel):
    Bucket: str
    KeyPrefixes: Optional[List[str]] = None
    Keys: Optional[List[str]] = None
    KmsKeysToGrant: Optional[List[KmsKeyToGrant]] = None


class S3DataAccessAssetSourceEntry(BaseValidatorModel):
    Bucket: str
    KeyPrefixes: Optional[List[str]] = None
    Keys: Optional[List[str]] = None
    KmsKeysToGrant: Optional[List[KmsKeyToGrant]] = None


class S3DataAccessAsset(BaseValidatorModel):
    Bucket: str
    KeyPrefixes: Optional[List[str]] = None
    Keys: Optional[List[str]] = None
    S3AccessPointAlias: Optional[str] = None
    S3AccessPointArn: Optional[str] = None
    KmsKeysToGrant: Optional[List[KmsKeyToGrant]] = None


class ListDataGrantsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDataSetRevisionsRequestPaginate(BaseValidatorModel):
    DataSetId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDataSetsRequestPaginate(BaseValidatorModel):
    Origin: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEventActionsRequestPaginate(BaseValidatorModel):
    EventSourceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListJobsRequestPaginate(BaseValidatorModel):
    DataSetId: Optional[str] = None
    RevisionId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListReceivedDataGrantsRequestPaginate(BaseValidatorModel):
    AcceptanceState: Optional[List[AcceptanceStateFilterValueType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRevisionAssetsRequestPaginate(BaseValidatorModel):
    DataSetId: str
    RevisionId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDataSetRevisionsResponse(BaseValidatorModel):
    Revisions: List[RevisionEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListReceivedDataGrantsResponse(BaseValidatorModel):
    DataGrantSummaries: List[ReceivedDataGrantSummariesEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ScopeDetails(BaseValidatorModel):
    LakeFormationTagPolicies: Optional[List[LakeFormationTagPolicyDetails]] = None
    RedshiftDataShares: Optional[List[RedshiftDataShareDetails]] = None
    S3DataAccesses: Optional[List[S3DataAccessDetails]] = None


class SchemaChangeRequestDetails(BaseValidatorModel):
    SchemaChangeAt: Timestamp
    Changes: Optional[List[SchemaChangeDetails]] = None


class Action(BaseValidatorModel):
    ExportRevisionToS3: Optional[AutoExportRevisionToS3RequestDetails] = None


class ListDataSetsResponse(BaseValidatorModel):
    DataSets: List[DataSetEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ImportAssetsFromLakeFormationTagPolicyResponseDetails(BaseValidatorModel):
    CatalogId: str
    RoleArn: str
    DataSetId: str
    RevisionId: str
    Database: Optional[DatabaseLFTagPolicyAndPermissionsOutput] = None
    Table: Optional[TableLFTagPolicyAndPermissionsOutput] = None


class LFResourceDetails(BaseValidatorModel):
    Database: Optional[DatabaseLFTagPolicy] = None
    Table: Optional[TableLFTagPolicy] = None

DatabaseLFTagPolicyAndPermissionsUnion = Union[DatabaseLFTagPolicyAndPermissions, DatabaseLFTagPolicyAndPermissionsOutput]


class TableLFTagPolicyAndPermissions(BaseValidatorModel):
    Expression: List[LFTagUnion]
    Permissions: List[TableTagPolicyLFPermissionType]


class JobError(BaseValidatorModel):
    Code: CodeType
    Message: str
    Details: Optional[Details] = None
    LimitName: Optional[JobErrorLimitNameType] = None
    LimitValue: Optional[float] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[JobErrorResourceTypesType] = None


class CreateS3DataAccessFromS3BucketResponseDetails(BaseValidatorModel):
    AssetSource: S3DataAccessAssetSourceEntryOutput
    DataSetId: str
    RevisionId: str

S3DataAccessAssetSourceEntryUnion = Union[S3DataAccessAssetSourceEntry, S3DataAccessAssetSourceEntryOutput]


class NotificationDetails(BaseValidatorModel):
    DataUpdate: Optional[DataUpdateRequestDetails] = None
    Deprecation: Optional[DeprecationRequestDetails] = None
    SchemaChange: Optional[SchemaChangeRequestDetails] = None


class CreateEventActionRequest(BaseValidatorModel):
    Action: Action
    Event: Event


class CreateEventActionResponse(BaseValidatorModel):
    Action: Action
    Arn: str
    CreatedAt: datetime
    Event: Event
    Id: str
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadata


class EventActionEntry(BaseValidatorModel):
    Action: Action
    Arn: str
    CreatedAt: datetime
    Event: Event
    Id: str
    UpdatedAt: datetime


class GetEventActionResponse(BaseValidatorModel):
    Action: Action
    Arn: str
    CreatedAt: datetime
    Event: Event
    Id: str
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadata


class UpdateEventActionRequest(BaseValidatorModel):
    EventActionId: str
    Action: Optional[Action] = None


class UpdateEventActionResponse(BaseValidatorModel):
    Action: Action
    Arn: str
    CreatedAt: datetime
    Event: Event
    Id: str
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadata


class LFTagPolicyDetails(BaseValidatorModel):
    CatalogId: str
    ResourceType: LFResourceTypeType
    ResourceDetails: LFResourceDetails

TableLFTagPolicyAndPermissionsUnion = Union[TableLFTagPolicyAndPermissions, TableLFTagPolicyAndPermissionsOutput]


class ResponseDetails(BaseValidatorModel):
    ExportAssetToSignedUrl: Optional[ExportAssetToSignedUrlResponseDetails] = None
    ExportAssetsToS3: Optional[ExportAssetsToS3ResponseDetails] = None
    ExportRevisionsToS3: Optional[ExportRevisionsToS3ResponseDetails] = None
    ImportAssetFromSignedUrl: Optional[ImportAssetFromSignedUrlResponseDetails] = None
    ImportAssetsFromS3: Optional[ImportAssetsFromS3ResponseDetails] = None
    ImportAssetsFromRedshiftDataShares: Optional[ImportAssetsFromRedshiftDataSharesResponseDetails] = None
    ImportAssetFromApiGatewayApi: Optional[ImportAssetFromApiGatewayApiResponseDetails] = None
    CreateS3DataAccessFromS3Bucket: Optional[CreateS3DataAccessFromS3BucketResponseDetails] = None
    ImportAssetsFromLakeFormationTagPolicy: Optional[ImportAssetsFromLakeFormationTagPolicyResponseDetails] = None


class CreateS3DataAccessFromS3BucketRequestDetails(BaseValidatorModel):
    AssetSource: S3DataAccessAssetSourceEntryUnion
    DataSetId: str
    RevisionId: str


class SendDataSetNotificationRequest(BaseValidatorModel):
    DataSetId: str
    Type: NotificationTypeType
    Scope: Optional[ScopeDetails] = None
    ClientToken: Optional[str] = None
    Comment: Optional[str] = None
    Details: Optional[NotificationDetails] = None


class ListEventActionsResponse(BaseValidatorModel):
    EventActions: List[EventActionEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class LakeFormationDataPermissionDetails(BaseValidatorModel):
    LFTagPolicy: Optional[LFTagPolicyDetails] = None


class ImportAssetsFromLakeFormationTagPolicyRequestDetails(BaseValidatorModel):
    CatalogId: str
    RoleArn: str
    DataSetId: str
    RevisionId: str
    Database: Optional[DatabaseLFTagPolicyAndPermissionsUnion] = None
    Table: Optional[TableLFTagPolicyAndPermissionsUnion] = None


class CreateJobResponse(BaseValidatorModel):
    Arn: str
    CreatedAt: datetime
    Details: ResponseDetails
    Errors: List[JobError]
    Id: str
    State: StateType
    Type: TypeType
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadata


class GetJobResponse(BaseValidatorModel):
    Arn: str
    CreatedAt: datetime
    Details: ResponseDetails
    Errors: List[JobError]
    Id: str
    State: StateType
    Type: TypeType
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadata


class JobEntry(BaseValidatorModel):
    Arn: str
    CreatedAt: datetime
    Details: ResponseDetails
    Id: str
    State: StateType
    Type: TypeType
    UpdatedAt: datetime
    Errors: Optional[List[JobError]] = None


class LakeFormationDataPermissionAsset(BaseValidatorModel):
    LakeFormationDataPermissionDetails: LakeFormationDataPermissionDetails
    LakeFormationDataPermissionType: Literal['LFTagPolicy']
    Permissions: List[LFPermissionType]
    RoleArn: Optional[str] = None


class RequestDetails(BaseValidatorModel):
    ExportAssetToSignedUrl: Optional[ExportAssetToSignedUrlRequestDetails] = None
    ExportAssetsToS3: Optional[ExportAssetsToS3RequestDetails] = None
    ExportRevisionsToS3: Optional[ExportRevisionsToS3RequestDetails] = None
    ImportAssetFromSignedUrl: Optional[ImportAssetFromSignedUrlRequestDetails] = None
    ImportAssetsFromS3: Optional[ImportAssetsFromS3RequestDetails] = None
    ImportAssetsFromRedshiftDataShares: Optional[ImportAssetsFromRedshiftDataSharesRequestDetails] = None
    ImportAssetFromApiGatewayApi: Optional[ImportAssetFromApiGatewayApiRequestDetails] = None
    CreateS3DataAccessFromS3Bucket: Optional[CreateS3DataAccessFromS3BucketRequestDetails] = None
    ImportAssetsFromLakeFormationTagPolicy: Optional[ImportAssetsFromLakeFormationTagPolicyRequestDetails] = None


class ListJobsResponse(BaseValidatorModel):
    Jobs: List[JobEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AssetDetails(BaseValidatorModel):
    S3SnapshotAsset: Optional[S3SnapshotAsset] = None
    RedshiftDataShareAsset: Optional[RedshiftDataShareAsset] = None
    ApiGatewayApiAsset: Optional[ApiGatewayApiAsset] = None
    S3DataAccessAsset: Optional[S3DataAccessAsset] = None
    LakeFormationDataPermissionAsset: Optional[LakeFormationDataPermissionAsset] = None


class CreateJobRequest(BaseValidatorModel):
    Details: RequestDetails
    Type: TypeType


class AssetEntry(BaseValidatorModel):
    Arn: str
    AssetDetails: AssetDetails
    AssetType: AssetTypeType
    CreatedAt: datetime
    DataSetId: str
    Id: str
    Name: str
    RevisionId: str
    UpdatedAt: datetime
    SourceId: Optional[str] = None


class GetAssetResponse(BaseValidatorModel):
    Arn: str
    AssetDetails: AssetDetails
    AssetType: AssetTypeType
    CreatedAt: datetime
    DataSetId: str
    Id: str
    Name: str
    RevisionId: str
    SourceId: str
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadata


class UpdateAssetResponse(BaseValidatorModel):
    Arn: str
    AssetDetails: AssetDetails
    AssetType: AssetTypeType
    CreatedAt: datetime
    DataSetId: str
    Id: str
    Name: str
    RevisionId: str
    SourceId: str
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadata


class ListRevisionAssetsResponse(BaseValidatorModel):
    Assets: List[AssetEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None
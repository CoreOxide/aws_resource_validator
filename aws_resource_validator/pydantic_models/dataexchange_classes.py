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
from aws_resource_validator.pydantic_models.dataexchange_constants import *

class ApiGatewayApiAssetTypeDef(BaseModel):
    ApiDescription: Optional[str] = None
    ApiEndpoint: Optional[str] = None
    ApiId: Optional[str] = None
    ApiKey: Optional[str] = None
    ApiName: Optional[str] = None
    ApiSpecificationDownloadUrl: Optional[str] = None
    ApiSpecificationDownloadUrlExpiresAt: Optional[datetime] = None
    ProtocolType: Optional[Literal["REST"]] = None
    Stage: Optional[str] = None

class AssetDestinationEntryTypeDef(BaseModel):
    AssetId: str
    Bucket: str
    Key: Optional[str] = None

class RedshiftDataShareAssetTypeDef(BaseModel):
    Arn: str

class S3SnapshotAssetTypeDef(BaseModel):
    Size: float

class AssetSourceEntryTypeDef(BaseModel):
    Bucket: str
    Key: str

class AutoExportRevisionDestinationEntryTypeDef(BaseModel):
    Bucket: str
    KeyPattern: Optional[str] = None

class ExportServerSideEncryptionTypeDef(BaseModel):
    Type: ServerSideEncryptionTypesType
    KmsKeyArn: Optional[str] = None

class CancelJobRequestRequestTypeDef(BaseModel):
    JobId: str

class CreateDataSetRequestRequestTypeDef(BaseModel):
    AssetType: AssetTypeType
    Description: str
    Name: str
    Tags: Optional[Mapping[str, str]] = None

class OriginDetailsTypeDef(BaseModel):
    ProductId: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateRevisionRequestRequestTypeDef(BaseModel):
    DataSetId: str
    Comment: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class LFTagPaginatorTypeDef(BaseModel):
    TagKey: str
    TagValues: List[str]

class LFTagTypeDef(BaseModel):
    TagKey: str
    TagValues: Sequence[str]

class DeleteAssetRequestRequestTypeDef(BaseModel):
    AssetId: str
    DataSetId: str
    RevisionId: str

class DeleteDataSetRequestRequestTypeDef(BaseModel):
    DataSetId: str

class DeleteEventActionRequestRequestTypeDef(BaseModel):
    EventActionId: str

class DeleteRevisionRequestRequestTypeDef(BaseModel):
    DataSetId: str
    RevisionId: str

class ImportAssetFromSignedUrlJobErrorDetailsTypeDef(BaseModel):
    AssetName: str

class RevisionPublishedTypeDef(BaseModel):
    DataSetId: str

class ExportAssetToSignedUrlRequestDetailsTypeDef(BaseModel):
    AssetId: str
    DataSetId: str
    RevisionId: str

class ExportAssetToSignedUrlResponseDetailsTypeDef(BaseModel):
    AssetId: str
    DataSetId: str
    RevisionId: str
    SignedUrl: Optional[str] = None
    SignedUrlExpiresAt: Optional[datetime] = None

class RevisionDestinationEntryTypeDef(BaseModel):
    Bucket: str
    RevisionId: str
    KeyPattern: Optional[str] = None

class GetAssetRequestRequestTypeDef(BaseModel):
    AssetId: str
    DataSetId: str
    RevisionId: str

class GetDataSetRequestRequestTypeDef(BaseModel):
    DataSetId: str

class GetEventActionRequestRequestTypeDef(BaseModel):
    EventActionId: str

class GetJobRequestRequestTypeDef(BaseModel):
    JobId: str

class GetRevisionRequestRequestTypeDef(BaseModel):
    DataSetId: str
    RevisionId: str

class ImportAssetFromApiGatewayApiRequestDetailsTypeDef(BaseModel):
    ApiId: str
    ApiName: str
    ApiSpecificationMd5Hash: str
    DataSetId: str
    ProtocolType: Literal["REST"]
    RevisionId: str
    Stage: str
    ApiDescription: Optional[str] = None
    ApiKey: Optional[str] = None

class ImportAssetFromApiGatewayApiResponseDetailsTypeDef(BaseModel):
    ApiId: str
    ApiName: str
    ApiSpecificationMd5Hash: str
    ApiSpecificationUploadUrl: str
    ApiSpecificationUploadUrlExpiresAt: datetime
    DataSetId: str
    ProtocolType: Literal["REST"]
    RevisionId: str
    Stage: str
    ApiDescription: Optional[str] = None
    ApiKey: Optional[str] = None

class ImportAssetFromSignedUrlRequestDetailsTypeDef(BaseModel):
    AssetName: str
    DataSetId: str
    Md5Hash: str
    RevisionId: str

class ImportAssetFromSignedUrlResponseDetailsTypeDef(BaseModel):
    AssetName: str
    DataSetId: str
    RevisionId: str
    Md5Hash: Optional[str] = None
    SignedUrl: Optional[str] = None
    SignedUrlExpiresAt: Optional[datetime] = None

class RedshiftDataShareAssetSourceEntryTypeDef(BaseModel):
    DataShareArn: str

class KmsKeyToGrantTypeDef(BaseModel):
    KmsKeyArn: str

class LakeFormationTagPolicyDetailsTypeDef(BaseModel):
    Database: Optional[str] = None
    Table: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListDataSetRevisionsRequestRequestTypeDef(BaseModel):
    DataSetId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class RevisionEntryTypeDef(BaseModel):
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

class ListDataSetsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Origin: Optional[str] = None

class ListEventActionsRequestRequestTypeDef(BaseModel):
    EventSourceId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListJobsRequestRequestTypeDef(BaseModel):
    DataSetId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    RevisionId: Optional[str] = None

class ListRevisionAssetsRequestRequestTypeDef(BaseModel):
    DataSetId: str
    RevisionId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class RedshiftDataShareDetailsTypeDef(BaseModel):
    Arn: str
    Database: str
    Function: Optional[str] = None
    Table: Optional[str] = None
    Schema: Optional[str] = None
    View: Optional[str] = None

class RevokeRevisionRequestRequestTypeDef(BaseModel):
    DataSetId: str
    RevisionId: str
    RevocationComment: str

class S3DataAccessDetailsTypeDef(BaseModel):
    KeyPrefixes: Optional[Sequence[str]] = None
    Keys: Optional[Sequence[str]] = None

class SchemaChangeDetailsTypeDef(BaseModel):
    Name: str
    Type: SchemaChangeTypeType
    Description: Optional[str] = None

class SendApiAssetRequestRequestTypeDef(BaseModel):
    AssetId: str
    DataSetId: str
    RevisionId: str
    Body: Optional[str] = None
    QueryStringParameters: Optional[Mapping[str, str]] = None
    RequestHeaders: Optional[Mapping[str, str]] = None
    Method: Optional[str] = None
    Path: Optional[str] = None

class StartJobRequestRequestTypeDef(BaseModel):
    JobId: str

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateAssetRequestRequestTypeDef(BaseModel):
    AssetId: str
    DataSetId: str
    Name: str
    RevisionId: str

class UpdateDataSetRequestRequestTypeDef(BaseModel):
    DataSetId: str
    Description: Optional[str] = None
    Name: Optional[str] = None

class UpdateRevisionRequestRequestTypeDef(BaseModel):
    DataSetId: str
    RevisionId: str
    Comment: Optional[str] = None
    Finalized: Optional[bool] = None

class ImportAssetsFromS3RequestDetailsTypeDef(BaseModel):
    AssetSources: Sequence[AssetSourceEntryTypeDef]
    DataSetId: str
    RevisionId: str

class ImportAssetsFromS3ResponseDetailsTypeDef(BaseModel):
    AssetSources: List[AssetSourceEntryTypeDef]
    DataSetId: str
    RevisionId: str

class AutoExportRevisionToS3RequestDetailsTypeDef(BaseModel):
    RevisionDestination: AutoExportRevisionDestinationEntryTypeDef
    Encryption: Optional[ExportServerSideEncryptionTypeDef] = None

class ExportAssetsToS3RequestDetailsTypeDef(BaseModel):
    AssetDestinations: Sequence[AssetDestinationEntryTypeDef]
    DataSetId: str
    RevisionId: str
    Encryption: Optional[ExportServerSideEncryptionTypeDef] = None

class ExportAssetsToS3ResponseDetailsTypeDef(BaseModel):
    AssetDestinations: List[AssetDestinationEntryTypeDef]
    DataSetId: str
    RevisionId: str
    Encryption: Optional[ExportServerSideEncryptionTypeDef] = None

class DataSetEntryTypeDef(BaseModel):
    Arn: str
    AssetType: AssetTypeType
    CreatedAt: datetime
    Description: str
    Id: str
    Name: str
    Origin: OriginType
    UpdatedAt: datetime
    OriginDetails: Optional[OriginDetailsTypeDef] = None
    SourceId: Optional[str] = None

class CreateDataSetResponseTypeDef(BaseModel):
    Arn: str
    AssetType: AssetTypeType
    CreatedAt: datetime
    Description: str
    Id: str
    Name: str
    Origin: OriginType
    OriginDetails: OriginDetailsTypeDef
    SourceId: str
    Tags: Dict[str, str]
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRevisionResponseTypeDef(BaseModel):
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
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetDataSetResponseTypeDef(BaseModel):
    Arn: str
    AssetType: AssetTypeType
    CreatedAt: datetime
    Description: str
    Id: str
    Name: str
    Origin: OriginType
    OriginDetails: OriginDetailsTypeDef
    SourceId: str
    Tags: Dict[str, str]
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetRevisionResponseTypeDef(BaseModel):
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
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class RevokeRevisionResponseTypeDef(BaseModel):
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
    ResponseMetadata: ResponseMetadataTypeDef

class SendApiAssetResponseTypeDef(BaseModel):
    Body: str
    ResponseHeaders: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDataSetResponseTypeDef(BaseModel):
    Arn: str
    AssetType: AssetTypeType
    CreatedAt: datetime
    Description: str
    Id: str
    Name: str
    Origin: OriginType
    OriginDetails: OriginDetailsTypeDef
    SourceId: str
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRevisionResponseTypeDef(BaseModel):
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
    ResponseMetadata: ResponseMetadataTypeDef

class DataUpdateRequestDetailsTypeDef(BaseModel):
    DataUpdatedAt: Optional[TimestampTypeDef] = None

class DeprecationRequestDetailsTypeDef(BaseModel):
    DeprecationAt: TimestampTypeDef

class DatabaseLFTagPolicyAndPermissionsPaginatorTypeDef(BaseModel):
    Expression: List[LFTagPaginatorTypeDef]
    Permissions: List[Literal["DESCRIBE"]]

class DatabaseLFTagPolicyPaginatorTypeDef(BaseModel):
    Expression: List[LFTagPaginatorTypeDef]

class TableLFTagPolicyAndPermissionsPaginatorTypeDef(BaseModel):
    Expression: List[LFTagPaginatorTypeDef]
    Permissions: List[TableTagPolicyLFPermissionType]

class TableLFTagPolicyPaginatorTypeDef(BaseModel):
    Expression: List[LFTagPaginatorTypeDef]

class DatabaseLFTagPolicyAndPermissionsTypeDef(BaseModel):
    Expression: Sequence[LFTagTypeDef]
    Permissions: Sequence[Literal["DESCRIBE"]]

class DatabaseLFTagPolicyTypeDef(BaseModel):
    Expression: List[LFTagTypeDef]

class TableLFTagPolicyAndPermissionsTypeDef(BaseModel):
    Expression: Sequence[LFTagTypeDef]
    Permissions: Sequence[TableTagPolicyLFPermissionType]

class TableLFTagPolicyTypeDef(BaseModel):
    Expression: List[LFTagTypeDef]

class DetailsTypeDef(BaseModel):
    ImportAssetFromSignedUrlJobErrorDetails: Optional[       ImportAssetFromSignedUrlJobErrorDetailsTypeDef     ] = None
    ImportAssetsFromS3JobErrorDetails: Optional[List[AssetSourceEntryTypeDef]] = None

class EventTypeDef(BaseModel):
    RevisionPublished: Optional[RevisionPublishedTypeDef] = None

class ExportRevisionsToS3RequestDetailsTypeDef(BaseModel):
    DataSetId: str
    RevisionDestinations: Sequence[RevisionDestinationEntryTypeDef]
    Encryption: Optional[ExportServerSideEncryptionTypeDef] = None

class ExportRevisionsToS3ResponseDetailsTypeDef(BaseModel):
    DataSetId: str
    RevisionDestinations: List[RevisionDestinationEntryTypeDef]
    Encryption: Optional[ExportServerSideEncryptionTypeDef] = None
    EventActionArn: Optional[str] = None

class ImportAssetsFromRedshiftDataSharesRequestDetailsTypeDef(BaseModel):
    AssetSources: Sequence[RedshiftDataShareAssetSourceEntryTypeDef]
    DataSetId: str
    RevisionId: str

class ImportAssetsFromRedshiftDataSharesResponseDetailsTypeDef(BaseModel):
    AssetSources: List[RedshiftDataShareAssetSourceEntryTypeDef]
    DataSetId: str
    RevisionId: str

class S3DataAccessAssetSourceEntryPaginatorTypeDef(BaseModel):
    Bucket: str
    KeyPrefixes: Optional[List[str]] = None
    Keys: Optional[List[str]] = None
    KmsKeysToGrant: Optional[List[KmsKeyToGrantTypeDef]] = None

class S3DataAccessAssetSourceEntryTypeDef(BaseModel):
    Bucket: str
    KeyPrefixes: Optional[Sequence[str]] = None
    Keys: Optional[Sequence[str]] = None
    KmsKeysToGrant: Optional[Sequence[KmsKeyToGrantTypeDef]] = None

class S3DataAccessAssetTypeDef(BaseModel):
    Bucket: str
    KeyPrefixes: Optional[List[str]] = None
    Keys: Optional[List[str]] = None
    S3AccessPointAlias: Optional[str] = None
    S3AccessPointArn: Optional[str] = None
    KmsKeysToGrant: Optional[List[KmsKeyToGrantTypeDef]] = None

class ListDataSetRevisionsRequestListDataSetRevisionsPaginateTypeDef(BaseModel):
    DataSetId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataSetsRequestListDataSetsPaginateTypeDef(BaseModel):
    Origin: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEventActionsRequestListEventActionsPaginateTypeDef(BaseModel):
    EventSourceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobsRequestListJobsPaginateTypeDef(BaseModel):
    DataSetId: Optional[str] = None
    RevisionId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRevisionAssetsRequestListRevisionAssetsPaginateTypeDef(BaseModel):
    DataSetId: str
    RevisionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataSetRevisionsResponseTypeDef(BaseModel):
    NextToken: str
    Revisions: List[RevisionEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ScopeDetailsTypeDef(BaseModel):
    LakeFormationTagPolicies: Optional[Sequence[LakeFormationTagPolicyDetailsTypeDef]] = None
    RedshiftDataShares: Optional[Sequence[RedshiftDataShareDetailsTypeDef]] = None
    S3DataAccesses: Optional[Sequence[S3DataAccessDetailsTypeDef]] = None

class SchemaChangeRequestDetailsTypeDef(BaseModel):
    SchemaChangeAt: TimestampTypeDef
    Changes: Optional[Sequence[SchemaChangeDetailsTypeDef]] = None

class ActionTypeDef(BaseModel):
    ExportRevisionToS3: Optional[AutoExportRevisionToS3RequestDetailsTypeDef] = None

class ListDataSetsResponseTypeDef(BaseModel):
    DataSets: List[DataSetEntryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportAssetsFromLakeFormationTagPolicyResponseDetailsPaginatorTypeDef(BaseModel):
    CatalogId: str
    RoleArn: str
    DataSetId: str
    RevisionId: str
    Database: Optional[DatabaseLFTagPolicyAndPermissionsPaginatorTypeDef] = None
    Table: Optional[TableLFTagPolicyAndPermissionsPaginatorTypeDef] = None

class LFResourceDetailsPaginatorTypeDef(BaseModel):
    Database: Optional[DatabaseLFTagPolicyPaginatorTypeDef] = None
    Table: Optional[TableLFTagPolicyPaginatorTypeDef] = None

class ImportAssetsFromLakeFormationTagPolicyRequestDetailsTypeDef(BaseModel):
    CatalogId: str
    RoleArn: str
    DataSetId: str
    RevisionId: str
    Database: Optional[DatabaseLFTagPolicyAndPermissionsTypeDef] = None
    Table: Optional[TableLFTagPolicyAndPermissionsTypeDef] = None

class ImportAssetsFromLakeFormationTagPolicyResponseDetailsTypeDef(BaseModel):
    CatalogId: str
    RoleArn: str
    DataSetId: str
    RevisionId: str
    Database: Optional[DatabaseLFTagPolicyAndPermissionsTypeDef] = None
    Table: Optional[TableLFTagPolicyAndPermissionsTypeDef] = None

class LFResourceDetailsTypeDef(BaseModel):
    Database: Optional[DatabaseLFTagPolicyTypeDef] = None
    Table: Optional[TableLFTagPolicyTypeDef] = None

class JobErrorTypeDef(BaseModel):
    Code: CodeType
    Message: str
    Details: Optional[DetailsTypeDef] = None
    LimitName: Optional[JobErrorLimitNameType] = None
    LimitValue: Optional[float] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[JobErrorResourceTypesType] = None

class CreateS3DataAccessFromS3BucketResponseDetailsPaginatorTypeDef(BaseModel):
    AssetSource: S3DataAccessAssetSourceEntryPaginatorTypeDef
    DataSetId: str
    RevisionId: str

class CreateS3DataAccessFromS3BucketRequestDetailsTypeDef(BaseModel):
    AssetSource: S3DataAccessAssetSourceEntryTypeDef
    DataSetId: str
    RevisionId: str

class CreateS3DataAccessFromS3BucketResponseDetailsTypeDef(BaseModel):
    AssetSource: S3DataAccessAssetSourceEntryTypeDef
    DataSetId: str
    RevisionId: str

class NotificationDetailsTypeDef(BaseModel):
    DataUpdate: Optional[DataUpdateRequestDetailsTypeDef] = None
    Deprecation: Optional[DeprecationRequestDetailsTypeDef] = None
    SchemaChange: Optional[SchemaChangeRequestDetailsTypeDef] = None

class CreateEventActionRequestRequestTypeDef(BaseModel):
    Action: ActionTypeDef
    Event: EventTypeDef

class CreateEventActionResponseTypeDef(BaseModel):
    Action: ActionTypeDef
    Arn: str
    CreatedAt: datetime
    Event: EventTypeDef
    Id: str
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class EventActionEntryTypeDef(BaseModel):
    Action: ActionTypeDef
    Arn: str
    CreatedAt: datetime
    Event: EventTypeDef
    Id: str
    UpdatedAt: datetime

class GetEventActionResponseTypeDef(BaseModel):
    Action: ActionTypeDef
    Arn: str
    CreatedAt: datetime
    Event: EventTypeDef
    Id: str
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEventActionRequestRequestTypeDef(BaseModel):
    EventActionId: str
    Action: Optional[ActionTypeDef] = None

class UpdateEventActionResponseTypeDef(BaseModel):
    Action: ActionTypeDef
    Arn: str
    CreatedAt: datetime
    Event: EventTypeDef
    Id: str
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class LFTagPolicyDetailsPaginatorTypeDef(BaseModel):
    CatalogId: str
    ResourceType: LFResourceTypeType
    ResourceDetails: LFResourceDetailsPaginatorTypeDef

class LFTagPolicyDetailsTypeDef(BaseModel):
    CatalogId: str
    ResourceType: LFResourceTypeType
    ResourceDetails: LFResourceDetailsTypeDef

class ResponseDetailsPaginatorTypeDef(BaseModel):
    ExportAssetToSignedUrl: Optional[ExportAssetToSignedUrlResponseDetailsTypeDef] = None
    ExportAssetsToS3: Optional[ExportAssetsToS3ResponseDetailsTypeDef] = None
    ExportRevisionsToS3: Optional[ExportRevisionsToS3ResponseDetailsTypeDef] = None
    ImportAssetFromSignedUrl: Optional[ImportAssetFromSignedUrlResponseDetailsTypeDef] = None
    ImportAssetsFromS3: Optional[ImportAssetsFromS3ResponseDetailsTypeDef] = None
    ImportAssetsFromRedshiftDataShares: Optional[       ImportAssetsFromRedshiftDataSharesResponseDetailsTypeDef     ] = None
    ImportAssetFromApiGatewayApi: Optional[       ImportAssetFromApiGatewayApiResponseDetailsTypeDef     ] = None
    CreateS3DataAccessFromS3Bucket: Optional[       CreateS3DataAccessFromS3BucketResponseDetailsPaginatorTypeDef     ] = None
    ImportAssetsFromLakeFormationTagPolicy: Optional[       ImportAssetsFromLakeFormationTagPolicyResponseDetailsPaginatorTypeDef     ] = None

class RequestDetailsTypeDef(BaseModel):
    ExportAssetToSignedUrl: Optional[ExportAssetToSignedUrlRequestDetailsTypeDef] = None
    ExportAssetsToS3: Optional[ExportAssetsToS3RequestDetailsTypeDef] = None
    ExportRevisionsToS3: Optional[ExportRevisionsToS3RequestDetailsTypeDef] = None
    ImportAssetFromSignedUrl: Optional[ImportAssetFromSignedUrlRequestDetailsTypeDef] = None
    ImportAssetsFromS3: Optional[ImportAssetsFromS3RequestDetailsTypeDef] = None
    ImportAssetsFromRedshiftDataShares: Optional[       ImportAssetsFromRedshiftDataSharesRequestDetailsTypeDef     ] = None
    ImportAssetFromApiGatewayApi: Optional[       ImportAssetFromApiGatewayApiRequestDetailsTypeDef     ] = None
    CreateS3DataAccessFromS3Bucket: Optional[       CreateS3DataAccessFromS3BucketRequestDetailsTypeDef     ] = None
    ImportAssetsFromLakeFormationTagPolicy: Optional[       ImportAssetsFromLakeFormationTagPolicyRequestDetailsTypeDef     ] = None

class ResponseDetailsTypeDef(BaseModel):
    ExportAssetToSignedUrl: Optional[ExportAssetToSignedUrlResponseDetailsTypeDef] = None
    ExportAssetsToS3: Optional[ExportAssetsToS3ResponseDetailsTypeDef] = None
    ExportRevisionsToS3: Optional[ExportRevisionsToS3ResponseDetailsTypeDef] = None
    ImportAssetFromSignedUrl: Optional[ImportAssetFromSignedUrlResponseDetailsTypeDef] = None
    ImportAssetsFromS3: Optional[ImportAssetsFromS3ResponseDetailsTypeDef] = None
    ImportAssetsFromRedshiftDataShares: Optional[       ImportAssetsFromRedshiftDataSharesResponseDetailsTypeDef     ] = None
    ImportAssetFromApiGatewayApi: Optional[       ImportAssetFromApiGatewayApiResponseDetailsTypeDef     ] = None
    CreateS3DataAccessFromS3Bucket: Optional[       CreateS3DataAccessFromS3BucketResponseDetailsTypeDef     ] = None
    ImportAssetsFromLakeFormationTagPolicy: Optional[       ImportAssetsFromLakeFormationTagPolicyResponseDetailsTypeDef     ] = None

class SendDataSetNotificationRequestRequestTypeDef(BaseModel):
    DataSetId: str
    Type: NotificationTypeType
    Scope: Optional[ScopeDetailsTypeDef] = None
    ClientToken: Optional[str] = None
    Comment: Optional[str] = None
    Details: Optional[NotificationDetailsTypeDef] = None

class ListEventActionsResponseTypeDef(BaseModel):
    EventActions: List[EventActionEntryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class LakeFormationDataPermissionDetailsPaginatorTypeDef(BaseModel):
    LFTagPolicy: Optional[LFTagPolicyDetailsPaginatorTypeDef] = None

class LakeFormationDataPermissionDetailsTypeDef(BaseModel):
    LFTagPolicy: Optional[LFTagPolicyDetailsTypeDef] = None

class JobEntryPaginatorTypeDef(BaseModel):
    Arn: str
    CreatedAt: datetime
    Details: ResponseDetailsPaginatorTypeDef
    Id: str
    State: StateType
    Type: TypeType
    UpdatedAt: datetime
    Errors: Optional[List[JobErrorTypeDef]] = None

class CreateJobRequestRequestTypeDef(BaseModel):
    Details: RequestDetailsTypeDef
    Type: TypeType

class CreateJobResponseTypeDef(BaseModel):
    Arn: str
    CreatedAt: datetime
    Details: ResponseDetailsTypeDef
    Errors: List[JobErrorTypeDef]
    Id: str
    State: StateType
    Type: TypeType
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetJobResponseTypeDef(BaseModel):
    Arn: str
    CreatedAt: datetime
    Details: ResponseDetailsTypeDef
    Errors: List[JobErrorTypeDef]
    Id: str
    State: StateType
    Type: TypeType
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class JobEntryTypeDef(BaseModel):
    Arn: str
    CreatedAt: datetime
    Details: ResponseDetailsTypeDef
    Id: str
    State: StateType
    Type: TypeType
    UpdatedAt: datetime
    Errors: Optional[List[JobErrorTypeDef]] = None

class LakeFormationDataPermissionAssetPaginatorTypeDef(BaseModel):
    LakeFormationDataPermissionDetails: LakeFormationDataPermissionDetailsPaginatorTypeDef
    LakeFormationDataPermissionType: Literal["LFTagPolicy"]
    Permissions: List[LFPermissionType]
    RoleArn: Optional[str] = None

class LakeFormationDataPermissionAssetTypeDef(BaseModel):
    LakeFormationDataPermissionDetails: LakeFormationDataPermissionDetailsTypeDef
    LakeFormationDataPermissionType: Literal["LFTagPolicy"]
    Permissions: List[LFPermissionType]
    RoleArn: Optional[str] = None

class ListJobsResponsePaginatorTypeDef(BaseModel):
    Jobs: List[JobEntryPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListJobsResponseTypeDef(BaseModel):
    Jobs: List[JobEntryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssetDetailsPaginatorTypeDef(BaseModel):
    S3SnapshotAsset: Optional[S3SnapshotAssetTypeDef] = None
    RedshiftDataShareAsset: Optional[RedshiftDataShareAssetTypeDef] = None
    ApiGatewayApiAsset: Optional[ApiGatewayApiAssetTypeDef] = None
    S3DataAccessAsset: Optional[S3DataAccessAssetTypeDef] = None
    LakeFormationDataPermissionAsset: Optional[       LakeFormationDataPermissionAssetPaginatorTypeDef     ] = None

class AssetDetailsTypeDef(BaseModel):
    S3SnapshotAsset: Optional[S3SnapshotAssetTypeDef] = None
    RedshiftDataShareAsset: Optional[RedshiftDataShareAssetTypeDef] = None
    ApiGatewayApiAsset: Optional[ApiGatewayApiAssetTypeDef] = None
    S3DataAccessAsset: Optional[S3DataAccessAssetTypeDef] = None
    LakeFormationDataPermissionAsset: Optional[LakeFormationDataPermissionAssetTypeDef] = None

class AssetEntryPaginatorTypeDef(BaseModel):
    Arn: str
    AssetDetails: AssetDetailsPaginatorTypeDef
    AssetType: AssetTypeType
    CreatedAt: datetime
    DataSetId: str
    Id: str
    Name: str
    RevisionId: str
    UpdatedAt: datetime
    SourceId: Optional[str] = None

class AssetEntryTypeDef(BaseModel):
    Arn: str
    AssetDetails: AssetDetailsTypeDef
    AssetType: AssetTypeType
    CreatedAt: datetime
    DataSetId: str
    Id: str
    Name: str
    RevisionId: str
    UpdatedAt: datetime
    SourceId: Optional[str] = None

class GetAssetResponseTypeDef(BaseModel):
    Arn: str
    AssetDetails: AssetDetailsTypeDef
    AssetType: AssetTypeType
    CreatedAt: datetime
    DataSetId: str
    Id: str
    Name: str
    RevisionId: str
    SourceId: str
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAssetResponseTypeDef(BaseModel):
    Arn: str
    AssetDetails: AssetDetailsTypeDef
    AssetType: AssetTypeType
    CreatedAt: datetime
    DataSetId: str
    Id: str
    Name: str
    RevisionId: str
    SourceId: str
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListRevisionAssetsResponsePaginatorTypeDef(BaseModel):
    Assets: List[AssetEntryPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRevisionAssetsResponseTypeDef(BaseModel):
    Assets: List[AssetEntryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef


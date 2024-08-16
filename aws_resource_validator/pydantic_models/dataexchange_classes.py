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
from aws_resource_validator.pydantic_models.dataexchange_constants import *

class ApiGatewayApiAssetTypeDef(BaseValidatorModel):
    ApiDescription: Optional[str] = None
    ApiEndpoint: Optional[str] = None
    ApiId: Optional[str] = None
    ApiKey: Optional[str] = None
    ApiName: Optional[str] = None
    ApiSpecificationDownloadUrl: Optional[str] = None
    ApiSpecificationDownloadUrlExpiresAt: Optional[datetime] = None
    ProtocolType: Optional[Literal["REST"]] = None
    Stage: Optional[str] = None

class AssetDestinationEntryTypeDef(BaseValidatorModel):
    AssetId: str
    Bucket: str
    Key: Optional[str] = None

class RedshiftDataShareAssetTypeDef(BaseValidatorModel):
    Arn: str

class S3SnapshotAssetTypeDef(BaseValidatorModel):
    Size: float

class AssetSourceEntryTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str

class AutoExportRevisionDestinationEntryTypeDef(BaseValidatorModel):
    Bucket: str
    KeyPattern: Optional[str] = None

class ExportServerSideEncryptionTypeDef(BaseValidatorModel):
    Type: ServerSideEncryptionTypesType
    KmsKeyArn: Optional[str] = None

class CancelJobRequestRequestTypeDef(BaseValidatorModel):
    JobId: str

class CreateDataSetRequestRequestTypeDef(BaseValidatorModel):
    AssetType: AssetTypeType
    Description: str
    Name: str
    Tags: Optional[Mapping[str, str]] = None

class OriginDetailsTypeDef(BaseValidatorModel):
    ProductId: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateRevisionRequestRequestTypeDef(BaseValidatorModel):
    DataSetId: str
    Comment: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class LFTagPaginatorTypeDef(BaseValidatorModel):
    TagKey: str
    TagValues: List[str]

class LFTagTypeDef(BaseValidatorModel):
    TagKey: str
    TagValues: Sequence[str]

class DeleteAssetRequestRequestTypeDef(BaseValidatorModel):
    AssetId: str
    DataSetId: str
    RevisionId: str

class DeleteDataSetRequestRequestTypeDef(BaseValidatorModel):
    DataSetId: str

class DeleteEventActionRequestRequestTypeDef(BaseValidatorModel):
    EventActionId: str

class DeleteRevisionRequestRequestTypeDef(BaseValidatorModel):
    DataSetId: str
    RevisionId: str

class ImportAssetFromSignedUrlJobErrorDetailsTypeDef(BaseValidatorModel):
    AssetName: str

class RevisionPublishedTypeDef(BaseValidatorModel):
    DataSetId: str

class ExportAssetToSignedUrlRequestDetailsTypeDef(BaseValidatorModel):
    AssetId: str
    DataSetId: str
    RevisionId: str

class ExportAssetToSignedUrlResponseDetailsTypeDef(BaseValidatorModel):
    AssetId: str
    DataSetId: str
    RevisionId: str
    SignedUrl: Optional[str] = None
    SignedUrlExpiresAt: Optional[datetime] = None

class RevisionDestinationEntryTypeDef(BaseValidatorModel):
    Bucket: str
    RevisionId: str
    KeyPattern: Optional[str] = None

class GetAssetRequestRequestTypeDef(BaseValidatorModel):
    AssetId: str
    DataSetId: str
    RevisionId: str

class GetDataSetRequestRequestTypeDef(BaseValidatorModel):
    DataSetId: str

class GetEventActionRequestRequestTypeDef(BaseValidatorModel):
    EventActionId: str

class GetJobRequestRequestTypeDef(BaseValidatorModel):
    JobId: str

class GetRevisionRequestRequestTypeDef(BaseValidatorModel):
    DataSetId: str
    RevisionId: str

class ImportAssetFromApiGatewayApiRequestDetailsTypeDef(BaseValidatorModel):
    ApiId: str
    ApiName: str
    ApiSpecificationMd5Hash: str
    DataSetId: str
    ProtocolType: Literal["REST"]
    RevisionId: str
    Stage: str
    ApiDescription: Optional[str] = None
    ApiKey: Optional[str] = None

class ImportAssetFromApiGatewayApiResponseDetailsTypeDef(BaseValidatorModel):
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

class ImportAssetFromSignedUrlRequestDetailsTypeDef(BaseValidatorModel):
    AssetName: str
    DataSetId: str
    Md5Hash: str
    RevisionId: str

class ImportAssetFromSignedUrlResponseDetailsTypeDef(BaseValidatorModel):
    AssetName: str
    DataSetId: str
    RevisionId: str
    Md5Hash: Optional[str] = None
    SignedUrl: Optional[str] = None
    SignedUrlExpiresAt: Optional[datetime] = None

class RedshiftDataShareAssetSourceEntryTypeDef(BaseValidatorModel):
    DataShareArn: str

class KmsKeyToGrantTypeDef(BaseValidatorModel):
    KmsKeyArn: str

class LakeFormationTagPolicyDetailsTypeDef(BaseValidatorModel):
    Database: Optional[str] = None
    Table: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListDataSetRevisionsRequestRequestTypeDef(BaseValidatorModel):
    DataSetId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class RevisionEntryTypeDef(BaseValidatorModel):
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

class ListDataSetsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Origin: Optional[str] = None

class ListEventActionsRequestRequestTypeDef(BaseValidatorModel):
    EventSourceId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListJobsRequestRequestTypeDef(BaseValidatorModel):
    DataSetId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    RevisionId: Optional[str] = None

class ListRevisionAssetsRequestRequestTypeDef(BaseValidatorModel):
    DataSetId: str
    RevisionId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class RedshiftDataShareDetailsTypeDef(BaseValidatorModel):
    Arn: str
    Database: str
    Function: Optional[str] = None
    Table: Optional[str] = None
    Schema: Optional[str] = None
    View: Optional[str] = None

class RevokeRevisionRequestRequestTypeDef(BaseValidatorModel):
    DataSetId: str
    RevisionId: str
    RevocationComment: str

class S3DataAccessDetailsTypeDef(BaseValidatorModel):
    KeyPrefixes: Optional[Sequence[str]] = None
    Keys: Optional[Sequence[str]] = None

class SchemaChangeDetailsTypeDef(BaseValidatorModel):
    Name: str
    Type: SchemaChangeTypeType
    Description: Optional[str] = None

class SendApiAssetRequestRequestTypeDef(BaseValidatorModel):
    AssetId: str
    DataSetId: str
    RevisionId: str
    Body: Optional[str] = None
    QueryStringParameters: Optional[Mapping[str, str]] = None
    RequestHeaders: Optional[Mapping[str, str]] = None
    Method: Optional[str] = None
    Path: Optional[str] = None

class StartJobRequestRequestTypeDef(BaseValidatorModel):
    JobId: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateAssetRequestRequestTypeDef(BaseValidatorModel):
    AssetId: str
    DataSetId: str
    Name: str
    RevisionId: str

class UpdateDataSetRequestRequestTypeDef(BaseValidatorModel):
    DataSetId: str
    Description: Optional[str] = None
    Name: Optional[str] = None

class UpdateRevisionRequestRequestTypeDef(BaseValidatorModel):
    DataSetId: str
    RevisionId: str
    Comment: Optional[str] = None
    Finalized: Optional[bool] = None

class ImportAssetsFromS3RequestDetailsTypeDef(BaseValidatorModel):
    AssetSources: Sequence[AssetSourceEntryTypeDef]
    DataSetId: str
    RevisionId: str

class ImportAssetsFromS3ResponseDetailsTypeDef(BaseValidatorModel):
    AssetSources: List[AssetSourceEntryTypeDef]
    DataSetId: str
    RevisionId: str

class AutoExportRevisionToS3RequestDetailsTypeDef(BaseValidatorModel):
    RevisionDestination: AutoExportRevisionDestinationEntryTypeDef
    Encryption: Optional[ExportServerSideEncryptionTypeDef] = None

class ExportAssetsToS3RequestDetailsTypeDef(BaseValidatorModel):
    AssetDestinations: Sequence[AssetDestinationEntryTypeDef]
    DataSetId: str
    RevisionId: str
    Encryption: Optional[ExportServerSideEncryptionTypeDef] = None

class ExportAssetsToS3ResponseDetailsTypeDef(BaseValidatorModel):
    AssetDestinations: List[AssetDestinationEntryTypeDef]
    DataSetId: str
    RevisionId: str
    Encryption: Optional[ExportServerSideEncryptionTypeDef] = None

class DataSetEntryTypeDef(BaseValidatorModel):
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

class CreateDataSetResponseTypeDef(BaseValidatorModel):
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

class CreateRevisionResponseTypeDef(BaseValidatorModel):
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

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetDataSetResponseTypeDef(BaseValidatorModel):
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

class GetRevisionResponseTypeDef(BaseValidatorModel):
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

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class RevokeRevisionResponseTypeDef(BaseValidatorModel):
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

class SendApiAssetResponseTypeDef(BaseValidatorModel):
    Body: str
    ResponseHeaders: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDataSetResponseTypeDef(BaseValidatorModel):
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

class UpdateRevisionResponseTypeDef(BaseValidatorModel):
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

class DataUpdateRequestDetailsTypeDef(BaseValidatorModel):
    DataUpdatedAt: Optional[TimestampTypeDef] = None

class DeprecationRequestDetailsTypeDef(BaseValidatorModel):
    DeprecationAt: TimestampTypeDef

class DatabaseLFTagPolicyAndPermissionsPaginatorTypeDef(BaseValidatorModel):
    Expression: List[LFTagPaginatorTypeDef]
    Permissions: List[Literal["DESCRIBE"]]

class DatabaseLFTagPolicyPaginatorTypeDef(BaseValidatorModel):
    Expression: List[LFTagPaginatorTypeDef]

class TableLFTagPolicyAndPermissionsPaginatorTypeDef(BaseValidatorModel):
    Expression: List[LFTagPaginatorTypeDef]
    Permissions: List[TableTagPolicyLFPermissionType]

class TableLFTagPolicyPaginatorTypeDef(BaseValidatorModel):
    Expression: List[LFTagPaginatorTypeDef]

class DatabaseLFTagPolicyAndPermissionsTypeDef(BaseValidatorModel):
    Expression: Sequence[LFTagTypeDef]
    Permissions: Sequence[Literal["DESCRIBE"]]

class DatabaseLFTagPolicyTypeDef(BaseValidatorModel):
    Expression: List[LFTagTypeDef]

class TableLFTagPolicyAndPermissionsTypeDef(BaseValidatorModel):
    Expression: Sequence[LFTagTypeDef]
    Permissions: Sequence[TableTagPolicyLFPermissionType]

class TableLFTagPolicyTypeDef(BaseValidatorModel):
    Expression: List[LFTagTypeDef]

class DetailsTypeDef(BaseValidatorModel):
    ImportAssetFromSignedUrlJobErrorDetails: Optional[       ImportAssetFromSignedUrlJobErrorDetailsTypeDef     ] = None
    ImportAssetsFromS3JobErrorDetails: Optional[List[AssetSourceEntryTypeDef]] = None

class EventTypeDef(BaseValidatorModel):
    RevisionPublished: Optional[RevisionPublishedTypeDef] = None

class ExportRevisionsToS3RequestDetailsTypeDef(BaseValidatorModel):
    DataSetId: str
    RevisionDestinations: Sequence[RevisionDestinationEntryTypeDef]
    Encryption: Optional[ExportServerSideEncryptionTypeDef] = None

class ExportRevisionsToS3ResponseDetailsTypeDef(BaseValidatorModel):
    DataSetId: str
    RevisionDestinations: List[RevisionDestinationEntryTypeDef]
    Encryption: Optional[ExportServerSideEncryptionTypeDef] = None
    EventActionArn: Optional[str] = None

class ImportAssetsFromRedshiftDataSharesRequestDetailsTypeDef(BaseValidatorModel):
    AssetSources: Sequence[RedshiftDataShareAssetSourceEntryTypeDef]
    DataSetId: str
    RevisionId: str

class ImportAssetsFromRedshiftDataSharesResponseDetailsTypeDef(BaseValidatorModel):
    AssetSources: List[RedshiftDataShareAssetSourceEntryTypeDef]
    DataSetId: str
    RevisionId: str

class S3DataAccessAssetSourceEntryPaginatorTypeDef(BaseValidatorModel):
    Bucket: str
    KeyPrefixes: Optional[List[str]] = None
    Keys: Optional[List[str]] = None
    KmsKeysToGrant: Optional[List[KmsKeyToGrantTypeDef]] = None

class S3DataAccessAssetSourceEntryTypeDef(BaseValidatorModel):
    Bucket: str
    KeyPrefixes: Optional[Sequence[str]] = None
    Keys: Optional[Sequence[str]] = None
    KmsKeysToGrant: Optional[Sequence[KmsKeyToGrantTypeDef]] = None

class S3DataAccessAssetTypeDef(BaseValidatorModel):
    Bucket: str
    KeyPrefixes: Optional[List[str]] = None
    Keys: Optional[List[str]] = None
    S3AccessPointAlias: Optional[str] = None
    S3AccessPointArn: Optional[str] = None
    KmsKeysToGrant: Optional[List[KmsKeyToGrantTypeDef]] = None

class ListDataSetRevisionsRequestListDataSetRevisionsPaginateTypeDef(BaseValidatorModel):
    DataSetId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataSetsRequestListDataSetsPaginateTypeDef(BaseValidatorModel):
    Origin: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEventActionsRequestListEventActionsPaginateTypeDef(BaseValidatorModel):
    EventSourceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobsRequestListJobsPaginateTypeDef(BaseValidatorModel):
    DataSetId: Optional[str] = None
    RevisionId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRevisionAssetsRequestListRevisionAssetsPaginateTypeDef(BaseValidatorModel):
    DataSetId: str
    RevisionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataSetRevisionsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    Revisions: List[RevisionEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ScopeDetailsTypeDef(BaseValidatorModel):
    LakeFormationTagPolicies: Optional[Sequence[LakeFormationTagPolicyDetailsTypeDef]] = None
    RedshiftDataShares: Optional[Sequence[RedshiftDataShareDetailsTypeDef]] = None
    S3DataAccesses: Optional[Sequence[S3DataAccessDetailsTypeDef]] = None

class SchemaChangeRequestDetailsTypeDef(BaseValidatorModel):
    SchemaChangeAt: TimestampTypeDef
    Changes: Optional[Sequence[SchemaChangeDetailsTypeDef]] = None

class ActionTypeDef(BaseValidatorModel):
    ExportRevisionToS3: Optional[AutoExportRevisionToS3RequestDetailsTypeDef] = None

class ListDataSetsResponseTypeDef(BaseValidatorModel):
    DataSets: List[DataSetEntryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportAssetsFromLakeFormationTagPolicyResponseDetailsPaginatorTypeDef(BaseValidatorModel):
    CatalogId: str
    RoleArn: str
    DataSetId: str
    RevisionId: str
    Database: Optional[DatabaseLFTagPolicyAndPermissionsPaginatorTypeDef] = None
    Table: Optional[TableLFTagPolicyAndPermissionsPaginatorTypeDef] = None

class LFResourceDetailsPaginatorTypeDef(BaseValidatorModel):
    Database: Optional[DatabaseLFTagPolicyPaginatorTypeDef] = None
    Table: Optional[TableLFTagPolicyPaginatorTypeDef] = None

class ImportAssetsFromLakeFormationTagPolicyRequestDetailsTypeDef(BaseValidatorModel):
    CatalogId: str
    RoleArn: str
    DataSetId: str
    RevisionId: str
    Database: Optional[DatabaseLFTagPolicyAndPermissionsTypeDef] = None
    Table: Optional[TableLFTagPolicyAndPermissionsTypeDef] = None

class ImportAssetsFromLakeFormationTagPolicyResponseDetailsTypeDef(BaseValidatorModel):
    CatalogId: str
    RoleArn: str
    DataSetId: str
    RevisionId: str
    Database: Optional[DatabaseLFTagPolicyAndPermissionsTypeDef] = None
    Table: Optional[TableLFTagPolicyAndPermissionsTypeDef] = None

class LFResourceDetailsTypeDef(BaseValidatorModel):
    Database: Optional[DatabaseLFTagPolicyTypeDef] = None
    Table: Optional[TableLFTagPolicyTypeDef] = None

class JobErrorTypeDef(BaseValidatorModel):
    Code: CodeType
    Message: str
    Details: Optional[DetailsTypeDef] = None
    LimitName: Optional[JobErrorLimitNameType] = None
    LimitValue: Optional[float] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[JobErrorResourceTypesType] = None

class CreateS3DataAccessFromS3BucketResponseDetailsPaginatorTypeDef(BaseValidatorModel):
    AssetSource: S3DataAccessAssetSourceEntryPaginatorTypeDef
    DataSetId: str
    RevisionId: str

class CreateS3DataAccessFromS3BucketRequestDetailsTypeDef(BaseValidatorModel):
    AssetSource: S3DataAccessAssetSourceEntryTypeDef
    DataSetId: str
    RevisionId: str

class CreateS3DataAccessFromS3BucketResponseDetailsTypeDef(BaseValidatorModel):
    AssetSource: S3DataAccessAssetSourceEntryTypeDef
    DataSetId: str
    RevisionId: str

class NotificationDetailsTypeDef(BaseValidatorModel):
    DataUpdate: Optional[DataUpdateRequestDetailsTypeDef] = None
    Deprecation: Optional[DeprecationRequestDetailsTypeDef] = None
    SchemaChange: Optional[SchemaChangeRequestDetailsTypeDef] = None

class CreateEventActionRequestRequestTypeDef(BaseValidatorModel):
    Action: ActionTypeDef
    Event: EventTypeDef

class CreateEventActionResponseTypeDef(BaseValidatorModel):
    Action: ActionTypeDef
    Arn: str
    CreatedAt: datetime
    Event: EventTypeDef
    Id: str
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class EventActionEntryTypeDef(BaseValidatorModel):
    Action: ActionTypeDef
    Arn: str
    CreatedAt: datetime
    Event: EventTypeDef
    Id: str
    UpdatedAt: datetime

class GetEventActionResponseTypeDef(BaseValidatorModel):
    Action: ActionTypeDef
    Arn: str
    CreatedAt: datetime
    Event: EventTypeDef
    Id: str
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEventActionRequestRequestTypeDef(BaseValidatorModel):
    EventActionId: str
    Action: Optional[ActionTypeDef] = None

class UpdateEventActionResponseTypeDef(BaseValidatorModel):
    Action: ActionTypeDef
    Arn: str
    CreatedAt: datetime
    Event: EventTypeDef
    Id: str
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class LFTagPolicyDetailsPaginatorTypeDef(BaseValidatorModel):
    CatalogId: str
    ResourceType: LFResourceTypeType
    ResourceDetails: LFResourceDetailsPaginatorTypeDef

class LFTagPolicyDetailsTypeDef(BaseValidatorModel):
    CatalogId: str
    ResourceType: LFResourceTypeType
    ResourceDetails: LFResourceDetailsTypeDef

class ResponseDetailsPaginatorTypeDef(BaseValidatorModel):
    ExportAssetToSignedUrl: Optional[ExportAssetToSignedUrlResponseDetailsTypeDef] = None
    ExportAssetsToS3: Optional[ExportAssetsToS3ResponseDetailsTypeDef] = None
    ExportRevisionsToS3: Optional[ExportRevisionsToS3ResponseDetailsTypeDef] = None
    ImportAssetFromSignedUrl: Optional[ImportAssetFromSignedUrlResponseDetailsTypeDef] = None
    ImportAssetsFromS3: Optional[ImportAssetsFromS3ResponseDetailsTypeDef] = None
    ImportAssetsFromRedshiftDataShares: Optional[       ImportAssetsFromRedshiftDataSharesResponseDetailsTypeDef     ] = None
    ImportAssetFromApiGatewayApi: Optional[       ImportAssetFromApiGatewayApiResponseDetailsTypeDef     ] = None
    CreateS3DataAccessFromS3Bucket: Optional[       CreateS3DataAccessFromS3BucketResponseDetailsPaginatorTypeDef     ] = None
    ImportAssetsFromLakeFormationTagPolicy: Optional[       ImportAssetsFromLakeFormationTagPolicyResponseDetailsPaginatorTypeDef     ] = None

class RequestDetailsTypeDef(BaseValidatorModel):
    ExportAssetToSignedUrl: Optional[ExportAssetToSignedUrlRequestDetailsTypeDef] = None
    ExportAssetsToS3: Optional[ExportAssetsToS3RequestDetailsTypeDef] = None
    ExportRevisionsToS3: Optional[ExportRevisionsToS3RequestDetailsTypeDef] = None
    ImportAssetFromSignedUrl: Optional[ImportAssetFromSignedUrlRequestDetailsTypeDef] = None
    ImportAssetsFromS3: Optional[ImportAssetsFromS3RequestDetailsTypeDef] = None
    ImportAssetsFromRedshiftDataShares: Optional[       ImportAssetsFromRedshiftDataSharesRequestDetailsTypeDef     ] = None
    ImportAssetFromApiGatewayApi: Optional[       ImportAssetFromApiGatewayApiRequestDetailsTypeDef     ] = None
    CreateS3DataAccessFromS3Bucket: Optional[       CreateS3DataAccessFromS3BucketRequestDetailsTypeDef     ] = None
    ImportAssetsFromLakeFormationTagPolicy: Optional[       ImportAssetsFromLakeFormationTagPolicyRequestDetailsTypeDef     ] = None

class ResponseDetailsTypeDef(BaseValidatorModel):
    ExportAssetToSignedUrl: Optional[ExportAssetToSignedUrlResponseDetailsTypeDef] = None
    ExportAssetsToS3: Optional[ExportAssetsToS3ResponseDetailsTypeDef] = None
    ExportRevisionsToS3: Optional[ExportRevisionsToS3ResponseDetailsTypeDef] = None
    ImportAssetFromSignedUrl: Optional[ImportAssetFromSignedUrlResponseDetailsTypeDef] = None
    ImportAssetsFromS3: Optional[ImportAssetsFromS3ResponseDetailsTypeDef] = None
    ImportAssetsFromRedshiftDataShares: Optional[       ImportAssetsFromRedshiftDataSharesResponseDetailsTypeDef     ] = None
    ImportAssetFromApiGatewayApi: Optional[       ImportAssetFromApiGatewayApiResponseDetailsTypeDef     ] = None
    CreateS3DataAccessFromS3Bucket: Optional[       CreateS3DataAccessFromS3BucketResponseDetailsTypeDef     ] = None
    ImportAssetsFromLakeFormationTagPolicy: Optional[       ImportAssetsFromLakeFormationTagPolicyResponseDetailsTypeDef     ] = None

class SendDataSetNotificationRequestRequestTypeDef(BaseValidatorModel):
    DataSetId: str
    Type: NotificationTypeType
    Scope: Optional[ScopeDetailsTypeDef] = None
    ClientToken: Optional[str] = None
    Comment: Optional[str] = None
    Details: Optional[NotificationDetailsTypeDef] = None

class ListEventActionsResponseTypeDef(BaseValidatorModel):
    EventActions: List[EventActionEntryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class LakeFormationDataPermissionDetailsPaginatorTypeDef(BaseValidatorModel):
    LFTagPolicy: Optional[LFTagPolicyDetailsPaginatorTypeDef] = None

class LakeFormationDataPermissionDetailsTypeDef(BaseValidatorModel):
    LFTagPolicy: Optional[LFTagPolicyDetailsTypeDef] = None

class JobEntryPaginatorTypeDef(BaseValidatorModel):
    Arn: str
    CreatedAt: datetime
    Details: ResponseDetailsPaginatorTypeDef
    Id: str
    State: StateType
    Type: TypeType
    UpdatedAt: datetime
    Errors: Optional[List[JobErrorTypeDef]] = None

class CreateJobRequestRequestTypeDef(BaseValidatorModel):
    Details: RequestDetailsTypeDef
    Type: TypeType

class CreateJobResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreatedAt: datetime
    Details: ResponseDetailsTypeDef
    Errors: List[JobErrorTypeDef]
    Id: str
    State: StateType
    Type: TypeType
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetJobResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreatedAt: datetime
    Details: ResponseDetailsTypeDef
    Errors: List[JobErrorTypeDef]
    Id: str
    State: StateType
    Type: TypeType
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class JobEntryTypeDef(BaseValidatorModel):
    Arn: str
    CreatedAt: datetime
    Details: ResponseDetailsTypeDef
    Id: str
    State: StateType
    Type: TypeType
    UpdatedAt: datetime
    Errors: Optional[List[JobErrorTypeDef]] = None

class LakeFormationDataPermissionAssetPaginatorTypeDef(BaseValidatorModel):
    LakeFormationDataPermissionDetails: LakeFormationDataPermissionDetailsPaginatorTypeDef
    LakeFormationDataPermissionType: Literal["LFTagPolicy"]
    Permissions: List[LFPermissionType]
    RoleArn: Optional[str] = None

class LakeFormationDataPermissionAssetTypeDef(BaseValidatorModel):
    LakeFormationDataPermissionDetails: LakeFormationDataPermissionDetailsTypeDef
    LakeFormationDataPermissionType: Literal["LFTagPolicy"]
    Permissions: List[LFPermissionType]
    RoleArn: Optional[str] = None

class ListJobsResponsePaginatorTypeDef(BaseValidatorModel):
    Jobs: List[JobEntryPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListJobsResponseTypeDef(BaseValidatorModel):
    Jobs: List[JobEntryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssetDetailsPaginatorTypeDef(BaseValidatorModel):
    S3SnapshotAsset: Optional[S3SnapshotAssetTypeDef] = None
    RedshiftDataShareAsset: Optional[RedshiftDataShareAssetTypeDef] = None
    ApiGatewayApiAsset: Optional[ApiGatewayApiAssetTypeDef] = None
    S3DataAccessAsset: Optional[S3DataAccessAssetTypeDef] = None
    LakeFormationDataPermissionAsset: Optional[       LakeFormationDataPermissionAssetPaginatorTypeDef     ] = None

class AssetDetailsTypeDef(BaseValidatorModel):
    S3SnapshotAsset: Optional[S3SnapshotAssetTypeDef] = None
    RedshiftDataShareAsset: Optional[RedshiftDataShareAssetTypeDef] = None
    ApiGatewayApiAsset: Optional[ApiGatewayApiAssetTypeDef] = None
    S3DataAccessAsset: Optional[S3DataAccessAssetTypeDef] = None
    LakeFormationDataPermissionAsset: Optional[LakeFormationDataPermissionAssetTypeDef] = None

class AssetEntryPaginatorTypeDef(BaseValidatorModel):
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

class AssetEntryTypeDef(BaseValidatorModel):
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

class GetAssetResponseTypeDef(BaseValidatorModel):
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

class UpdateAssetResponseTypeDef(BaseValidatorModel):
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

class ListRevisionAssetsResponsePaginatorTypeDef(BaseValidatorModel):
    Assets: List[AssetEntryPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRevisionAssetsResponseTypeDef(BaseValidatorModel):
    Assets: List[AssetEntryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef


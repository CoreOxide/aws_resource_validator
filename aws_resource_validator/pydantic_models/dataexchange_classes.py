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
from aws_resource_validator.pydantic_models.dataexchange_constants import *

class AcceptDataGrantRequestTypeDef(BaseValidatorModel):
    DataGrantArn: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


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


class CancelJobRequestTypeDef(BaseValidatorModel):
    JobId: str


class CreateDataSetRequestTypeDef(BaseValidatorModel):
    AssetType: AssetTypeType
    Description: str
    Name: str
    Tags: Optional[Mapping[str, str]] = None


class OriginDetailsTypeDef(BaseValidatorModel):
    ProductId: Optional[str] = None
    DataGrantId: Optional[str] = None


class CreateRevisionRequestTypeDef(BaseValidatorModel):
    DataSetId: str
    Comment: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class DataGrantSummaryEntryTypeDef(BaseValidatorModel):
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


class LFTagOutputTypeDef(BaseValidatorModel):
    TagKey: str
    TagValues: List[str]


class LFTagTypeDef(BaseValidatorModel):
    TagKey: str
    TagValues: Sequence[str]


class DeleteAssetRequestTypeDef(BaseValidatorModel):
    AssetId: str
    DataSetId: str
    RevisionId: str


class DeleteDataGrantRequestTypeDef(BaseValidatorModel):
    DataGrantId: str


class DeleteDataSetRequestTypeDef(BaseValidatorModel):
    DataSetId: str


class DeleteEventActionRequestTypeDef(BaseValidatorModel):
    EventActionId: str


class DeleteRevisionRequestTypeDef(BaseValidatorModel):
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


class GetAssetRequestTypeDef(BaseValidatorModel):
    AssetId: str
    DataSetId: str
    RevisionId: str


class GetDataGrantRequestTypeDef(BaseValidatorModel):
    DataGrantId: str


class GetDataSetRequestTypeDef(BaseValidatorModel):
    DataSetId: str


class GetEventActionRequestTypeDef(BaseValidatorModel):
    EventActionId: str


class GetJobRequestTypeDef(BaseValidatorModel):
    JobId: str


class GetReceivedDataGrantRequestTypeDef(BaseValidatorModel):
    DataGrantArn: str


class GetRevisionRequestTypeDef(BaseValidatorModel):
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


class ListDataGrantsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListDataSetRevisionsRequestTypeDef(BaseValidatorModel):
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


class ListDataSetsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Origin: Optional[str] = None


class ListEventActionsRequestTypeDef(BaseValidatorModel):
    EventSourceId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListJobsRequestTypeDef(BaseValidatorModel):
    DataSetId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    RevisionId: Optional[str] = None


class ListReceivedDataGrantsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    AcceptanceState: Optional[Sequence[AcceptanceStateFilterValueType]] = None


class ReceivedDataGrantSummariesEntryTypeDef(BaseValidatorModel):
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


class ListRevisionAssetsRequestTypeDef(BaseValidatorModel):
    DataSetId: str
    RevisionId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class RedshiftDataShareDetailsTypeDef(BaseValidatorModel):
    Arn: str
    Database: str
    Function: Optional[str] = None
    Table: Optional[str] = None
    Schema: Optional[str] = None
    View: Optional[str] = None


class RevokeRevisionRequestTypeDef(BaseValidatorModel):
    DataSetId: str
    RevisionId: str
    RevocationComment: str


class S3DataAccessDetailsTypeDef(BaseValidatorModel):
    KeyPrefixes: Optional[Sequence[str]] = None
    Keys: Optional[Sequence[str]] = None


class SendApiAssetRequestTypeDef(BaseValidatorModel):
    AssetId: str
    DataSetId: str
    RevisionId: str
    Body: Optional[str] = None
    QueryStringParameters: Optional[Mapping[str, str]] = None
    RequestHeaders: Optional[Mapping[str, str]] = None
    Method: Optional[str] = None
    Path: Optional[str] = None


class StartJobRequestTypeDef(BaseValidatorModel):
    JobId: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateAssetRequestTypeDef(BaseValidatorModel):
    AssetId: str
    DataSetId: str
    Name: str
    RevisionId: str


class UpdateDataSetRequestTypeDef(BaseValidatorModel):
    DataSetId: str
    Description: Optional[str] = None
    Name: Optional[str] = None


class UpdateRevisionRequestTypeDef(BaseValidatorModel):
    DataSetId: str
    RevisionId: str
    Comment: Optional[str] = None
    Finalized: Optional[bool] = None


class AcceptDataGrantResponseTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDataGrantResponseTypeDef(BaseValidatorModel):
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


class GetDataGrantResponseTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef


class GetReceivedDataGrantResponseTypeDef(BaseValidatorModel):
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


class ImportAssetsFromS3RequestDetailsTypeDef(BaseValidatorModel):
    AssetSources: Sequence[AssetSourceEntryTypeDef]
    DataSetId: str
    RevisionId: str


class ImportAssetsFromS3ResponseDetailsTypeDef(BaseValidatorModel):
    AssetSources: List[AssetSourceEntryTypeDef]
    DataSetId: str
    RevisionId: str


class ExportServerSideEncryptionTypeDef(BaseValidatorModel):
    pass


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


class TimestampTypeDef(BaseValidatorModel):
    pass


class CreateDataGrantRequestTypeDef(BaseValidatorModel):
    Name: str
    GrantDistributionScope: GrantDistributionScopeType
    ReceiverPrincipal: str
    SourceDataSetId: str
    EndsAt: Optional[TimestampTypeDef] = None
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class DataUpdateRequestDetailsTypeDef(BaseValidatorModel):
    DataUpdatedAt: Optional[TimestampTypeDef] = None


class DeprecationRequestDetailsTypeDef(BaseValidatorModel):
    DeprecationAt: TimestampTypeDef


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


class ListDataGrantsResponseTypeDef(BaseValidatorModel):
    DataGrantSummaries: List[DataGrantSummaryEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DatabaseLFTagPolicyAndPermissionsOutputTypeDef(BaseValidatorModel):
    Expression: List[LFTagOutputTypeDef]
    Permissions: List[Literal["DESCRIBE"]]


class DatabaseLFTagPolicyTypeDef(BaseValidatorModel):
    Expression: List[LFTagOutputTypeDef]


class TableLFTagPolicyAndPermissionsOutputTypeDef(BaseValidatorModel):
    Expression: List[LFTagOutputTypeDef]
    Permissions: List[TableTagPolicyLFPermissionType]


class TableLFTagPolicyTypeDef(BaseValidatorModel):
    Expression: List[LFTagOutputTypeDef]


class DatabaseLFTagPolicyAndPermissionsTypeDef(BaseValidatorModel):
    Expression: Sequence[LFTagTypeDef]
    Permissions: Sequence[Literal["DESCRIBE"]]


class DetailsTypeDef(BaseValidatorModel):
    ImportAssetFromSignedUrlJobErrorDetails: Optional[ ImportAssetFromSignedUrlJobErrorDetailsTypeDef ] = None
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


class S3DataAccessAssetSourceEntryOutputTypeDef(BaseValidatorModel):
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


class ListDataGrantsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDataSetRevisionsRequestPaginateTypeDef(BaseValidatorModel):
    DataSetId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDataSetsRequestPaginateTypeDef(BaseValidatorModel):
    Origin: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEventActionsRequestPaginateTypeDef(BaseValidatorModel):
    EventSourceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListJobsRequestPaginateTypeDef(BaseValidatorModel):
    DataSetId: Optional[str] = None
    RevisionId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListReceivedDataGrantsRequestPaginateTypeDef(BaseValidatorModel):
    AcceptanceState: Optional[Sequence[AcceptanceStateFilterValueType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRevisionAssetsRequestPaginateTypeDef(BaseValidatorModel):
    DataSetId: str
    RevisionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDataSetRevisionsResponseTypeDef(BaseValidatorModel):
    Revisions: List[RevisionEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListReceivedDataGrantsResponseTypeDef(BaseValidatorModel):
    DataGrantSummaries: List[ReceivedDataGrantSummariesEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ScopeDetailsTypeDef(BaseValidatorModel):
    LakeFormationTagPolicies: Optional[Sequence[LakeFormationTagPolicyDetailsTypeDef]] = None
    RedshiftDataShares: Optional[Sequence[RedshiftDataShareDetailsTypeDef]] = None
    S3DataAccesses: Optional[Sequence[S3DataAccessDetailsTypeDef]] = None


class SchemaChangeDetailsTypeDef(BaseValidatorModel):
    pass


class SchemaChangeRequestDetailsTypeDef(BaseValidatorModel):
    SchemaChangeAt: TimestampTypeDef
    Changes: Optional[Sequence[SchemaChangeDetailsTypeDef]] = None


class ActionTypeDef(BaseValidatorModel):
    ExportRevisionToS3: Optional[AutoExportRevisionToS3RequestDetailsTypeDef] = None


class ListDataSetsResponseTypeDef(BaseValidatorModel):
    DataSets: List[DataSetEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ImportAssetsFromLakeFormationTagPolicyResponseDetailsTypeDef(BaseValidatorModel):
    CatalogId: str
    RoleArn: str
    DataSetId: str
    RevisionId: str
    Database: Optional[DatabaseLFTagPolicyAndPermissionsOutputTypeDef] = None
    Table: Optional[TableLFTagPolicyAndPermissionsOutputTypeDef] = None


class LFResourceDetailsTypeDef(BaseValidatorModel):
    Database: Optional[DatabaseLFTagPolicyTypeDef] = None
    Table: Optional[TableLFTagPolicyTypeDef] = None


class LFTagUnionTypeDef(BaseValidatorModel):
    pass


class TableLFTagPolicyAndPermissionsTypeDef(BaseValidatorModel):
    Expression: Sequence[LFTagUnionTypeDef]
    Permissions: Sequence[TableTagPolicyLFPermissionType]


class JobErrorTypeDef(BaseValidatorModel):
    Code: CodeType
    Message: str
    Details: Optional[DetailsTypeDef] = None
    LimitName: Optional[JobErrorLimitNameType] = None
    LimitValue: Optional[float] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[JobErrorResourceTypesType] = None


class CreateS3DataAccessFromS3BucketResponseDetailsTypeDef(BaseValidatorModel):
    AssetSource: S3DataAccessAssetSourceEntryOutputTypeDef
    DataSetId: str
    RevisionId: str


class NotificationDetailsTypeDef(BaseValidatorModel):
    DataUpdate: Optional[DataUpdateRequestDetailsTypeDef] = None
    Deprecation: Optional[DeprecationRequestDetailsTypeDef] = None
    SchemaChange: Optional[SchemaChangeRequestDetailsTypeDef] = None


class CreateEventActionRequestTypeDef(BaseValidatorModel):
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


class UpdateEventActionRequestTypeDef(BaseValidatorModel):
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


class LFTagPolicyDetailsTypeDef(BaseValidatorModel):
    CatalogId: str
    ResourceType: LFResourceTypeType
    ResourceDetails: LFResourceDetailsTypeDef


class ResponseDetailsTypeDef(BaseValidatorModel):
    ExportAssetToSignedUrl: Optional[ExportAssetToSignedUrlResponseDetailsTypeDef] = None
    ExportAssetsToS3: Optional[ExportAssetsToS3ResponseDetailsTypeDef] = None
    ExportRevisionsToS3: Optional[ExportRevisionsToS3ResponseDetailsTypeDef] = None
    ImportAssetFromSignedUrl: Optional[ImportAssetFromSignedUrlResponseDetailsTypeDef] = None
    ImportAssetsFromS3: Optional[ImportAssetsFromS3ResponseDetailsTypeDef] = None
    ImportAssetsFromRedshiftDataShares: Optional[ ImportAssetsFromRedshiftDataSharesResponseDetailsTypeDef ] = None
    ImportAssetFromApiGatewayApi: Optional[ImportAssetFromApiGatewayApiResponseDetailsTypeDef] = None
    CreateS3DataAccessFromS3Bucket: Optional[ CreateS3DataAccessFromS3BucketResponseDetailsTypeDef ] = None
    ImportAssetsFromLakeFormationTagPolicy: Optional[ ImportAssetsFromLakeFormationTagPolicyResponseDetailsTypeDef ] = None


class S3DataAccessAssetSourceEntryUnionTypeDef(BaseValidatorModel):
    pass


class CreateS3DataAccessFromS3BucketRequestDetailsTypeDef(BaseValidatorModel):
    AssetSource: S3DataAccessAssetSourceEntryUnionTypeDef
    DataSetId: str
    RevisionId: str


class ListEventActionsResponseTypeDef(BaseValidatorModel):
    EventActions: List[EventActionEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class LakeFormationDataPermissionDetailsTypeDef(BaseValidatorModel):
    LFTagPolicy: Optional[LFTagPolicyDetailsTypeDef] = None


class TableLFTagPolicyAndPermissionsUnionTypeDef(BaseValidatorModel):
    pass


class DatabaseLFTagPolicyAndPermissionsUnionTypeDef(BaseValidatorModel):
    pass


class ImportAssetsFromLakeFormationTagPolicyRequestDetailsTypeDef(BaseValidatorModel):
    CatalogId: str
    RoleArn: str
    DataSetId: str
    RevisionId: str
    Database: Optional[DatabaseLFTagPolicyAndPermissionsUnionTypeDef] = None
    Table: Optional[TableLFTagPolicyAndPermissionsUnionTypeDef] = None


class LakeFormationDataPermissionAssetTypeDef(BaseValidatorModel):
    LakeFormationDataPermissionDetails: LakeFormationDataPermissionDetailsTypeDef
    LakeFormationDataPermissionType: Literal["LFTagPolicy"]
    Permissions: List[LFPermissionType]
    RoleArn: Optional[str] = None


class RequestDetailsTypeDef(BaseValidatorModel):
    ExportAssetToSignedUrl: Optional[ExportAssetToSignedUrlRequestDetailsTypeDef] = None
    ExportAssetsToS3: Optional[ExportAssetsToS3RequestDetailsTypeDef] = None
    ExportRevisionsToS3: Optional[ExportRevisionsToS3RequestDetailsTypeDef] = None
    ImportAssetFromSignedUrl: Optional[ImportAssetFromSignedUrlRequestDetailsTypeDef] = None
    ImportAssetsFromS3: Optional[ImportAssetsFromS3RequestDetailsTypeDef] = None
    ImportAssetsFromRedshiftDataShares: Optional[ ImportAssetsFromRedshiftDataSharesRequestDetailsTypeDef ] = None
    ImportAssetFromApiGatewayApi: Optional[ImportAssetFromApiGatewayApiRequestDetailsTypeDef] = None
    CreateS3DataAccessFromS3Bucket: Optional[CreateS3DataAccessFromS3BucketRequestDetailsTypeDef] = None
    ImportAssetsFromLakeFormationTagPolicy: Optional[ ImportAssetsFromLakeFormationTagPolicyRequestDetailsTypeDef ] = None


class JobEntryTypeDef(BaseValidatorModel):
    pass


class ListJobsResponseTypeDef(BaseValidatorModel):
    Jobs: List[JobEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class AssetDetailsTypeDef(BaseValidatorModel):
    S3SnapshotAsset: Optional[S3SnapshotAssetTypeDef] = None
    RedshiftDataShareAsset: Optional[RedshiftDataShareAssetTypeDef] = None
    ApiGatewayApiAsset: Optional[ApiGatewayApiAssetTypeDef] = None
    S3DataAccessAsset: Optional[S3DataAccessAssetTypeDef] = None
    LakeFormationDataPermissionAsset: Optional[LakeFormationDataPermissionAssetTypeDef] = None


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


class ListRevisionAssetsResponseTypeDef(BaseValidatorModel):
    Assets: List[AssetEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None



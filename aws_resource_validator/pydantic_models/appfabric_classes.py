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
from aws_resource_validator.pydantic_models.appfabric_constants import *

class ApiKeyCredentialTypeDef(BaseValidatorModel):
    apiKey: str


class TenantTypeDef(BaseValidatorModel):
    tenantIdentifier: str
    tenantDisplayName: str


class AppBundleSummaryTypeDef(BaseValidatorModel):
    arn: str


class AppBundleTypeDef(BaseValidatorModel):
    arn: str
    customerManagedKeyArn: Optional[str] = None


class AuthRequestTypeDef(BaseValidatorModel):
    redirectUri: str
    code: str


class BatchGetUserAccessTasksRequestTypeDef(BaseValidatorModel):
    appBundleIdentifier: str
    taskIdList: Sequence[str]


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class TagTypeDef(BaseValidatorModel):
    key: str
    value: str


class IngestionTypeDef(BaseValidatorModel):
    arn: str
    appBundleArn: str
    app: str
    tenantId: str
    createdAt: datetime
    updatedAt: datetime
    state: IngestionStateType
    ingestionType: Literal["auditLog"]


class Oauth2CredentialTypeDef(BaseValidatorModel):
    clientId: str
    clientSecret: str


class DeleteAppAuthorizationRequestTypeDef(BaseValidatorModel):
    appBundleIdentifier: str
    appAuthorizationIdentifier: str


class DeleteAppBundleRequestTypeDef(BaseValidatorModel):
    appBundleIdentifier: str


class DeleteIngestionDestinationRequestTypeDef(BaseValidatorModel):
    appBundleIdentifier: str
    ingestionIdentifier: str
    ingestionDestinationIdentifier: str


class DeleteIngestionRequestTypeDef(BaseValidatorModel):
    appBundleIdentifier: str
    ingestionIdentifier: str


class FirehoseStreamTypeDef(BaseValidatorModel):
    streamName: str


class S3BucketTypeDef(BaseValidatorModel):
    bucketName: str
    prefix: Optional[str] = None


class GetAppAuthorizationRequestTypeDef(BaseValidatorModel):
    appBundleIdentifier: str
    appAuthorizationIdentifier: str


class GetAppBundleRequestTypeDef(BaseValidatorModel):
    appBundleIdentifier: str


class GetIngestionDestinationRequestTypeDef(BaseValidatorModel):
    appBundleIdentifier: str
    ingestionIdentifier: str
    ingestionDestinationIdentifier: str


class GetIngestionRequestTypeDef(BaseValidatorModel):
    appBundleIdentifier: str
    ingestionIdentifier: str


class IngestionDestinationSummaryTypeDef(BaseValidatorModel):
    arn: str


class IngestionSummaryTypeDef(BaseValidatorModel):
    arn: str
    app: str
    tenantId: str
    state: IngestionStateType


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAppAuthorizationsRequestTypeDef(BaseValidatorModel):
    appBundleIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAppBundlesRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListIngestionDestinationsRequestTypeDef(BaseValidatorModel):
    appBundleIdentifier: str
    ingestionIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListIngestionsRequestTypeDef(BaseValidatorModel):
    appBundleIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class StartIngestionRequestTypeDef(BaseValidatorModel):
    ingestionIdentifier: str
    appBundleIdentifier: str


class StartUserAccessTasksRequestTypeDef(BaseValidatorModel):
    appBundleIdentifier: str
    email: str


class StopIngestionRequestTypeDef(BaseValidatorModel):
    ingestionIdentifier: str
    appBundleIdentifier: str


class TaskErrorTypeDef(BaseValidatorModel):
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class AppAuthorizationSummaryTypeDef(BaseValidatorModel):
    appAuthorizationArn: str
    appBundleArn: str
    app: str
    tenant: TenantTypeDef
    status: AppAuthorizationStatusType
    updatedAt: datetime


class AppAuthorizationTypeDef(BaseValidatorModel):
    appAuthorizationArn: str
    appBundleArn: str
    app: str
    tenant: TenantTypeDef
    authType: AuthTypeType
    status: AppAuthorizationStatusType
    createdAt: datetime
    updatedAt: datetime
    persona: Optional[PersonaType] = None
    authUrl: Optional[str] = None


class AuditLogProcessingConfigurationTypeDef(BaseValidatorModel):
    pass


class ProcessingConfigurationTypeDef(BaseValidatorModel):
    auditLog: Optional[AuditLogProcessingConfigurationTypeDef] = None


class ConnectAppAuthorizationRequestTypeDef(BaseValidatorModel):
    appBundleIdentifier: str
    appAuthorizationIdentifier: str
    authRequest: Optional[AuthRequestTypeDef] = None


class CreateAppBundleResponseTypeDef(BaseValidatorModel):
    appBundle: AppBundleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetAppBundleResponseTypeDef(BaseValidatorModel):
    appBundle: AppBundleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListAppBundlesResponseTypeDef(BaseValidatorModel):
    appBundleSummaryList: List[AppBundleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CreateAppBundleRequestTypeDef(BaseValidatorModel):
    clientToken: Optional[str] = None
    customerManagedKeyIdentifier: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateIngestionRequestTypeDef(BaseValidatorModel):
    appBundleIdentifier: str
    app: str
    tenantId: str
    ingestionType: Literal["auditLog"]
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]


class CreateIngestionResponseTypeDef(BaseValidatorModel):
    ingestion: IngestionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetIngestionResponseTypeDef(BaseValidatorModel):
    ingestion: IngestionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CredentialTypeDef(BaseValidatorModel):
    oauth2Credential: Optional[Oauth2CredentialTypeDef] = None
    apiKeyCredential: Optional[ApiKeyCredentialTypeDef] = None


class DestinationTypeDef(BaseValidatorModel):
    s3Bucket: Optional[S3BucketTypeDef] = None
    firehoseStream: Optional[FirehoseStreamTypeDef] = None


class ListIngestionDestinationsResponseTypeDef(BaseValidatorModel):
    ingestionDestinations: List[IngestionDestinationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListIngestionsResponseTypeDef(BaseValidatorModel):
    ingestions: List[IngestionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListAppAuthorizationsRequestPaginateTypeDef(BaseValidatorModel):
    appBundleIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAppBundlesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListIngestionDestinationsRequestPaginateTypeDef(BaseValidatorModel):
    appBundleIdentifier: str
    ingestionIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListIngestionsRequestPaginateTypeDef(BaseValidatorModel):
    appBundleIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class UserAccessResultItemTypeDef(BaseValidatorModel):
    app: Optional[str] = None
    tenantId: Optional[str] = None
    tenantDisplayName: Optional[str] = None
    taskId: Optional[str] = None
    resultStatus: Optional[ResultStatusType] = None
    email: Optional[str] = None
    userId: Optional[str] = None
    userFullName: Optional[str] = None
    userFirstName: Optional[str] = None
    userLastName: Optional[str] = None
    userStatus: Optional[str] = None
    taskError: Optional[TaskErrorTypeDef] = None


class UserAccessTaskItemTypeDef(BaseValidatorModel):
    app: str
    tenantId: str
    taskId: Optional[str] = None
    error: Optional[TaskErrorTypeDef] = None


class ConnectAppAuthorizationResponseTypeDef(BaseValidatorModel):
    appAuthorizationSummary: AppAuthorizationSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListAppAuthorizationsResponseTypeDef(BaseValidatorModel):
    appAuthorizationSummaryList: List[AppAuthorizationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CreateAppAuthorizationResponseTypeDef(BaseValidatorModel):
    appAuthorization: AppAuthorizationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetAppAuthorizationResponseTypeDef(BaseValidatorModel):
    appAuthorization: AppAuthorizationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAppAuthorizationResponseTypeDef(BaseValidatorModel):
    appAuthorization: AppAuthorizationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateAppAuthorizationRequestTypeDef(BaseValidatorModel):
    appBundleIdentifier: str
    app: str
    credential: CredentialTypeDef
    tenant: TenantTypeDef
    authType: AuthTypeType
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class UpdateAppAuthorizationRequestTypeDef(BaseValidatorModel):
    appBundleIdentifier: str
    appAuthorizationIdentifier: str
    credential: Optional[CredentialTypeDef] = None
    tenant: Optional[TenantTypeDef] = None


class AuditLogDestinationConfigurationTypeDef(BaseValidatorModel):
    destination: DestinationTypeDef


class BatchGetUserAccessTasksResponseTypeDef(BaseValidatorModel):
    userAccessResultsList: List[UserAccessResultItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class StartUserAccessTasksResponseTypeDef(BaseValidatorModel):
    userAccessTasksList: List[UserAccessTaskItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DestinationConfigurationTypeDef(BaseValidatorModel):
    auditLog: Optional[AuditLogDestinationConfigurationTypeDef] = None


class CreateIngestionDestinationRequestTypeDef(BaseValidatorModel):
    appBundleIdentifier: str
    ingestionIdentifier: str
    processingConfiguration: ProcessingConfigurationTypeDef
    destinationConfiguration: DestinationConfigurationTypeDef
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class IngestionDestinationTypeDef(BaseValidatorModel):
    arn: str
    ingestionArn: str
    processingConfiguration: ProcessingConfigurationTypeDef
    destinationConfiguration: DestinationConfigurationTypeDef
    status: Optional[IngestionDestinationStatusType] = None
    statusReason: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None


class UpdateIngestionDestinationRequestTypeDef(BaseValidatorModel):
    appBundleIdentifier: str
    ingestionIdentifier: str
    ingestionDestinationIdentifier: str
    destinationConfiguration: DestinationConfigurationTypeDef


class CreateIngestionDestinationResponseTypeDef(BaseValidatorModel):
    ingestionDestination: IngestionDestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetIngestionDestinationResponseTypeDef(BaseValidatorModel):
    ingestionDestination: IngestionDestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateIngestionDestinationResponseTypeDef(BaseValidatorModel):
    ingestionDestination: IngestionDestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef



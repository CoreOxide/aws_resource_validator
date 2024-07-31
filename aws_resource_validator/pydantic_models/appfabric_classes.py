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
from aws_resource_validator.pydantic_models.appfabric_constants import *

class ApiKeyCredentialTypeDef(BaseModel):
    apiKey: str

class TenantTypeDef(BaseModel):
    tenantIdentifier: str
    tenantDisplayName: str

class AppBundleSummaryTypeDef(BaseModel):
    arn: str

class AppBundleTypeDef(BaseModel):
    arn: str
    customerManagedKeyArn: Optional[str] = None

class AuditLogProcessingConfigurationTypeDef(BaseModel):
    schema: SchemaType
    format: FormatType

class AuthRequestTypeDef(BaseModel):
    redirectUri: str
    code: str

class BatchGetUserAccessTasksRequestRequestTypeDef(BaseModel):
    appBundleIdentifier: str
    taskIdList: Sequence[str]

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class TagTypeDef(BaseModel):
    key: str
    value: str

class IngestionTypeDef(BaseModel):
    arn: str
    appBundleArn: str
    app: str
    tenantId: str
    createdAt: datetime
    updatedAt: datetime
    state: IngestionStateType
    ingestionType: Literal["auditLog"]

class Oauth2CredentialTypeDef(BaseModel):
    clientId: str
    clientSecret: str

class DeleteAppAuthorizationRequestRequestTypeDef(BaseModel):
    appBundleIdentifier: str
    appAuthorizationIdentifier: str

class DeleteAppBundleRequestRequestTypeDef(BaseModel):
    appBundleIdentifier: str

class DeleteIngestionDestinationRequestRequestTypeDef(BaseModel):
    appBundleIdentifier: str
    ingestionIdentifier: str
    ingestionDestinationIdentifier: str

class DeleteIngestionRequestRequestTypeDef(BaseModel):
    appBundleIdentifier: str
    ingestionIdentifier: str

class FirehoseStreamTypeDef(BaseModel):
    streamName: str

class S3BucketTypeDef(BaseModel):
    bucketName: str
    prefix: Optional[str] = None

class GetAppAuthorizationRequestRequestTypeDef(BaseModel):
    appBundleIdentifier: str
    appAuthorizationIdentifier: str

class GetAppBundleRequestRequestTypeDef(BaseModel):
    appBundleIdentifier: str

class GetIngestionDestinationRequestRequestTypeDef(BaseModel):
    appBundleIdentifier: str
    ingestionIdentifier: str
    ingestionDestinationIdentifier: str

class GetIngestionRequestRequestTypeDef(BaseModel):
    appBundleIdentifier: str
    ingestionIdentifier: str

class IngestionDestinationSummaryTypeDef(BaseModel):
    arn: str

class IngestionSummaryTypeDef(BaseModel):
    arn: str
    app: str
    tenantId: str
    state: IngestionStateType

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAppAuthorizationsRequestRequestTypeDef(BaseModel):
    appBundleIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAppBundlesRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListIngestionDestinationsRequestRequestTypeDef(BaseModel):
    appBundleIdentifier: str
    ingestionIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListIngestionsRequestRequestTypeDef(BaseModel):
    appBundleIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class StartIngestionRequestRequestTypeDef(BaseModel):
    ingestionIdentifier: str
    appBundleIdentifier: str

class StartUserAccessTasksRequestRequestTypeDef(BaseModel):
    appBundleIdentifier: str
    email: str

class StopIngestionRequestRequestTypeDef(BaseModel):
    ingestionIdentifier: str
    appBundleIdentifier: str

class TaskErrorTypeDef(BaseModel):
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class AppAuthorizationSummaryTypeDef(BaseModel):
    appAuthorizationArn: str
    appBundleArn: str
    app: str
    tenant: TenantTypeDef
    status: AppAuthorizationStatusType
    updatedAt: datetime

class AppAuthorizationTypeDef(BaseModel):
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

class ProcessingConfigurationTypeDef(BaseModel):
    auditLog: Optional[AuditLogProcessingConfigurationTypeDef] = None

class ConnectAppAuthorizationRequestRequestTypeDef(BaseModel):
    appBundleIdentifier: str
    appAuthorizationIdentifier: str
    authRequest: Optional[AuthRequestTypeDef] = None

class CreateAppBundleResponseTypeDef(BaseModel):
    appBundle: AppBundleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAppBundleResponseTypeDef(BaseModel):
    appBundle: AppBundleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppBundlesResponseTypeDef(BaseModel):
    appBundleSummaryList: List[AppBundleSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAppBundleRequestRequestTypeDef(BaseModel):
    clientToken: Optional[str] = None
    customerManagedKeyIdentifier: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateIngestionRequestRequestTypeDef(BaseModel):
    appBundleIdentifier: str
    app: str
    tenantId: str
    ingestionType: Literal["auditLog"]
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class CreateIngestionResponseTypeDef(BaseModel):
    ingestion: IngestionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetIngestionResponseTypeDef(BaseModel):
    ingestion: IngestionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CredentialTypeDef(BaseModel):
    oauth2Credential: Optional[Oauth2CredentialTypeDef] = None
    apiKeyCredential: Optional[ApiKeyCredentialTypeDef] = None

class DestinationTypeDef(BaseModel):
    s3Bucket: Optional[S3BucketTypeDef] = None
    firehoseStream: Optional[FirehoseStreamTypeDef] = None

class ListIngestionDestinationsResponseTypeDef(BaseModel):
    ingestionDestinations: List[IngestionDestinationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListIngestionsResponseTypeDef(BaseModel):
    ingestions: List[IngestionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppAuthorizationsRequestListAppAuthorizationsPaginateTypeDef(BaseModel):
    appBundleIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAppBundlesRequestListAppBundlesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIngestionDestinationsRequestListIngestionDestinationsPaginateTypeDef(BaseModel):
    appBundleIdentifier: str
    ingestionIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIngestionsRequestListIngestionsPaginateTypeDef(BaseModel):
    appBundleIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class UserAccessResultItemTypeDef(BaseModel):
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

class UserAccessTaskItemTypeDef(BaseModel):
    app: str
    tenantId: str
    taskId: Optional[str] = None
    error: Optional[TaskErrorTypeDef] = None

class ConnectAppAuthorizationResponseTypeDef(BaseModel):
    appAuthorizationSummary: AppAuthorizationSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppAuthorizationsResponseTypeDef(BaseModel):
    appAuthorizationSummaryList: List[AppAuthorizationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAppAuthorizationResponseTypeDef(BaseModel):
    appAuthorization: AppAuthorizationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAppAuthorizationResponseTypeDef(BaseModel):
    appAuthorization: AppAuthorizationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAppAuthorizationResponseTypeDef(BaseModel):
    appAuthorization: AppAuthorizationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAppAuthorizationRequestRequestTypeDef(BaseModel):
    appBundleIdentifier: str
    app: str
    credential: CredentialTypeDef
    tenant: TenantTypeDef
    authType: AuthTypeType
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class UpdateAppAuthorizationRequestRequestTypeDef(BaseModel):
    appBundleIdentifier: str
    appAuthorizationIdentifier: str
    credential: Optional[CredentialTypeDef] = None
    tenant: Optional[TenantTypeDef] = None

class AuditLogDestinationConfigurationTypeDef(BaseModel):
    destination: DestinationTypeDef

class BatchGetUserAccessTasksResponseTypeDef(BaseModel):
    userAccessResultsList: List[UserAccessResultItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartUserAccessTasksResponseTypeDef(BaseModel):
    userAccessTasksList: List[UserAccessTaskItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DestinationConfigurationTypeDef(BaseModel):
    auditLog: Optional[AuditLogDestinationConfigurationTypeDef] = None

class CreateIngestionDestinationRequestRequestTypeDef(BaseModel):
    appBundleIdentifier: str
    ingestionIdentifier: str
    processingConfiguration: ProcessingConfigurationTypeDef
    destinationConfiguration: DestinationConfigurationTypeDef
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class IngestionDestinationTypeDef(BaseModel):
    arn: str
    ingestionArn: str
    processingConfiguration: ProcessingConfigurationTypeDef
    destinationConfiguration: DestinationConfigurationTypeDef
    status: Optional[IngestionDestinationStatusType] = None
    statusReason: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None

class UpdateIngestionDestinationRequestRequestTypeDef(BaseModel):
    appBundleIdentifier: str
    ingestionIdentifier: str
    ingestionDestinationIdentifier: str
    destinationConfiguration: DestinationConfigurationTypeDef

class CreateIngestionDestinationResponseTypeDef(BaseModel):
    ingestionDestination: IngestionDestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetIngestionDestinationResponseTypeDef(BaseModel):
    ingestionDestination: IngestionDestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIngestionDestinationResponseTypeDef(BaseModel):
    ingestionDestination: IngestionDestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


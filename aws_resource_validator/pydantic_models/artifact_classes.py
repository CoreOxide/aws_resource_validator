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
from aws_resource_validator.pydantic_models.artifact_constants import *

class AccountSettingsTypeDef(BaseModel):
    notificationSubscriptionStatus: Optional[NotificationSubscriptionStatusType] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class GetReportMetadataRequestRequestTypeDef(BaseModel):
    reportId: str
    reportVersion: Optional[int] = None

class ReportDetailTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    periodStart: Optional[datetime] = None
    periodEnd: Optional[datetime] = None
    createdAt: Optional[datetime] = None
    lastModifiedAt: Optional[datetime] = None
    deletedAt: Optional[datetime] = None
    state: Optional[PublishedStateType] = None
    arn: Optional[str] = None
    series: Optional[str] = None
    category: Optional[str] = None
    companyName: Optional[str] = None
    productName: Optional[str] = None
    termArn: Optional[str] = None
    version: Optional[int] = None
    acceptanceType: Optional[AcceptanceTypeType] = None
    sequenceNumber: Optional[int] = None
    uploadState: Optional[UploadStateType] = None
    statusMessage: Optional[str] = None

class GetReportRequestRequestTypeDef(BaseModel):
    reportId: str
    termToken: str
    reportVersion: Optional[int] = None

class GetTermForReportRequestRequestTypeDef(BaseModel):
    reportId: str
    reportVersion: Optional[int] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListReportsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ReportSummaryTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    state: Optional[PublishedStateType] = None
    arn: Optional[str] = None
    version: Optional[int] = None
    uploadState: Optional[UploadStateType] = None
    description: Optional[str] = None
    periodStart: Optional[datetime] = None
    periodEnd: Optional[datetime] = None
    series: Optional[str] = None
    category: Optional[str] = None
    companyName: Optional[str] = None
    productName: Optional[str] = None
    statusMessage: Optional[str] = None
    acceptanceType: Optional[AcceptanceTypeType] = None

class PutAccountSettingsRequestRequestTypeDef(BaseModel):
    notificationSubscriptionStatus: Optional[NotificationSubscriptionStatusType] = None

class GetAccountSettingsResponseTypeDef(BaseModel):
    accountSettings: AccountSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetReportResponseTypeDef(BaseModel):
    documentPresignedUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTermForReportResponseTypeDef(BaseModel):
    documentPresignedUrl: str
    termToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutAccountSettingsResponseTypeDef(BaseModel):
    accountSettings: AccountSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetReportMetadataResponseTypeDef(BaseModel):
    reportDetails: ReportDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListReportsRequestListReportsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReportsResponseTypeDef(BaseModel):
    reports: List[ReportSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef


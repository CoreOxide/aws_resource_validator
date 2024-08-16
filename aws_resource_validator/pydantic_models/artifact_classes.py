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
from aws_resource_validator.pydantic_models.artifact_constants import *

class AccountSettingsTypeDef(BaseValidatorModel):
    notificationSubscriptionStatus: Optional[NotificationSubscriptionStatusType] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class GetReportMetadataRequestRequestTypeDef(BaseValidatorModel):
    reportId: str
    reportVersion: Optional[int] = None

class ReportDetailTypeDef(BaseValidatorModel):
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

class GetReportRequestRequestTypeDef(BaseValidatorModel):
    reportId: str
    termToken: str
    reportVersion: Optional[int] = None

class GetTermForReportRequestRequestTypeDef(BaseValidatorModel):
    reportId: str
    reportVersion: Optional[int] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListReportsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ReportSummaryTypeDef(BaseValidatorModel):
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

class PutAccountSettingsRequestRequestTypeDef(BaseValidatorModel):
    notificationSubscriptionStatus: Optional[NotificationSubscriptionStatusType] = None

class GetAccountSettingsResponseTypeDef(BaseValidatorModel):
    accountSettings: AccountSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetReportResponseTypeDef(BaseValidatorModel):
    documentPresignedUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTermForReportResponseTypeDef(BaseValidatorModel):
    documentPresignedUrl: str
    termToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutAccountSettingsResponseTypeDef(BaseValidatorModel):
    accountSettings: AccountSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetReportMetadataResponseTypeDef(BaseValidatorModel):
    reportDetails: ReportDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListReportsRequestListReportsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReportsResponseTypeDef(BaseValidatorModel):
    reports: List[ReportSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef


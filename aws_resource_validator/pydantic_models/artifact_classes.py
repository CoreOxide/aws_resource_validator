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
from aws_resource_validator.pydantic_models.artifact_constants import *

class AccountSettingsTypeDef(BaseValidatorModel):
    notificationSubscriptionStatus: Optional[NotificationSubscriptionStatusType] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class GetReportMetadataRequestTypeDef(BaseValidatorModel):
    reportId: str
    reportVersion: Optional[int] = None


class GetReportRequestTypeDef(BaseValidatorModel):
    reportId: str
    termToken: str
    reportVersion: Optional[int] = None


class GetTermForReportRequestTypeDef(BaseValidatorModel):
    reportId: str
    reportVersion: Optional[int] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListCustomerAgreementsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListReportsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class PutAccountSettingsRequestTypeDef(BaseValidatorModel):
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


class CustomerAgreementSummaryTypeDef(BaseValidatorModel):
    pass


class ListCustomerAgreementsResponseTypeDef(BaseValidatorModel):
    customerAgreements: List[CustomerAgreementSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class PutAccountSettingsResponseTypeDef(BaseValidatorModel):
    accountSettings: AccountSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ReportDetailTypeDef(BaseValidatorModel):
    pass


class GetReportMetadataResponseTypeDef(BaseValidatorModel):
    reportDetails: ReportDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListCustomerAgreementsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListReportsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ReportSummaryTypeDef(BaseValidatorModel):
    pass


class ListReportsResponseTypeDef(BaseValidatorModel):
    reports: List[ReportSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None



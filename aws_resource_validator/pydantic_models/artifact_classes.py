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

class AccountSettings(BaseValidatorModel):
    notificationSubscriptionStatus: Optional[NotificationSubscriptionStatusType] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class GetReportMetadataRequest(BaseValidatorModel):
    reportId: str
    reportVersion: Optional[int] = None


class GetReportRequest(BaseValidatorModel):
    reportId: str
    termToken: str
    reportVersion: Optional[int] = None


class GetTermForReportRequest(BaseValidatorModel):
    reportId: str
    reportVersion: Optional[int] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListCustomerAgreementsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListReportsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class PutAccountSettingsRequest(BaseValidatorModel):
    notificationSubscriptionStatus: Optional[NotificationSubscriptionStatusType] = None


class GetAccountSettingsResponse(BaseValidatorModel):
    accountSettings: AccountSettings
    ResponseMetadata: ResponseMetadata


class GetReportResponse(BaseValidatorModel):
    documentPresignedUrl: str
    ResponseMetadata: ResponseMetadata


class GetTermForReportResponse(BaseValidatorModel):
    documentPresignedUrl: str
    termToken: str
    ResponseMetadata: ResponseMetadata


class CustomerAgreementSummary(BaseValidatorModel):
    pass


class ListCustomerAgreementsResponse(BaseValidatorModel):
    customerAgreements: List[CustomerAgreementSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class PutAccountSettingsResponse(BaseValidatorModel):
    accountSettings: AccountSettings
    ResponseMetadata: ResponseMetadata


class ReportDetail(BaseValidatorModel):
    pass


class GetReportMetadataResponse(BaseValidatorModel):
    reportDetails: ReportDetail
    ResponseMetadata: ResponseMetadata


class ListCustomerAgreementsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListReportsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ReportSummary(BaseValidatorModel):
    pass


class ListReportsResponse(BaseValidatorModel):
    reports: List[ReportSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None



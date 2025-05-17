from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.artifact.artifact_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AccountSettings(BaseValidatorModel):
    notificationSubscriptionStatus: Optional[NotificationSubscriptionStatusType] = None


class CustomerAgreementSummary(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    id: Optional[str] = None
    agreementArn: Optional[str] = None
    awsAccountId: Optional[str] = None
    organizationArn: Optional[str] = None
    effectiveStart: Optional[datetime] = None
    effectiveEnd: Optional[datetime] = None
    state: Optional[CustomerAgreementStateType] = None
    description: Optional[str] = None
    acceptanceTerms: Optional[List[str]] = None
    terminateTerms: Optional[List[str]] = None
    type: Optional[AgreementTypeType] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'get_report_metadata' function.
class GetReportMetadataRequest(BaseValidatorModel):
    reportId: str
    reportVersion: Optional[int] = None


class ReportDetail(BaseValidatorModel):
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


# This class is the input for the 'get_report' function.
class GetReportRequest(BaseValidatorModel):
    reportId: str
    termToken: str
    reportVersion: Optional[int] = None


# This class is the input for the 'get_term_for_report' function.
class GetTermForReportRequest(BaseValidatorModel):
    reportId: str
    reportVersion: Optional[int] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_customer_agreements' function.
class ListCustomerAgreementsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_reports' function.
class ListReportsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ReportSummary(BaseValidatorModel):
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


# This class is the input for the 'put_account_settings' function.
class PutAccountSettingsRequest(BaseValidatorModel):
    notificationSubscriptionStatus: Optional[NotificationSubscriptionStatusType] = None


class GetAccountSettingsResponse(BaseValidatorModel):
    accountSettings: AccountSettings
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_report' function.
class GetReportResponse(BaseValidatorModel):
    documentPresignedUrl: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_term_for_report' function.
class GetTermForReportResponse(BaseValidatorModel):
    documentPresignedUrl: str
    termToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_customer_agreements' function.
class ListCustomerAgreementsResponse(BaseValidatorModel):
    customerAgreements: List[CustomerAgreementSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'put_account_settings' function.
class PutAccountSettingsResponse(BaseValidatorModel):
    accountSettings: AccountSettings
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_report_metadata' function.
class GetReportMetadataResponse(BaseValidatorModel):
    reportDetails: ReportDetail
    ResponseMetadata: ResponseMetadata


class ListCustomerAgreementsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListReportsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_reports' function.
class ListReportsResponse(BaseValidatorModel):
    reports: List[ReportSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None
from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.service_quotas.service_quotas_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class DeleteServiceQuotaIncreaseRequestFromTemplateRequest(BaseValidatorModel):
    ServiceCode: str
    QuotaCode: str
    AwsRegion: str


class ErrorReason(BaseValidatorModel):
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None


# This class is the input for the 'get_aws_default_service_quota' function.
class GetAWSDefaultServiceQuotaRequest(BaseValidatorModel):
    ServiceCode: str
    QuotaCode: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'get_requested_service_quota_change' function.
class GetRequestedServiceQuotaChangeRequest(BaseValidatorModel):
    RequestId: str


# This class is the input for the 'get_service_quota_increase_request_from_template' function.
class GetServiceQuotaIncreaseRequestFromTemplateRequest(BaseValidatorModel):
    ServiceCode: str
    QuotaCode: str
    AwsRegion: str


class ServiceQuotaIncreaseRequestInTemplate(BaseValidatorModel):
    ServiceCode: Optional[str] = None
    ServiceName: Optional[str] = None
    QuotaCode: Optional[str] = None
    QuotaName: Optional[str] = None
    DesiredValue: Optional[float] = None
    AwsRegion: Optional[str] = None
    Unit: Optional[str] = None
    GlobalQuota: Optional[bool] = None


# This class is the input for the 'get_service_quota' function.
class GetServiceQuotaRequest(BaseValidatorModel):
    ServiceCode: str
    QuotaCode: str
    ContextId: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_aws_default_service_quotas' function.
class ListAWSDefaultServiceQuotasRequest(BaseValidatorModel):
    ServiceCode: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_requested_service_quota_change_history_by_quota' function.
class ListRequestedServiceQuotaChangeHistoryByQuotaRequest(BaseValidatorModel):
    ServiceCode: str
    QuotaCode: str
    Status: Optional[RequestStatusType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    QuotaRequestedAtLevel: Optional[AppliedLevelEnumType] = None


# This class is the input for the 'list_requested_service_quota_change_history' function.
class ListRequestedServiceQuotaChangeHistoryRequest(BaseValidatorModel):
    ServiceCode: Optional[str] = None
    Status: Optional[RequestStatusType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    QuotaRequestedAtLevel: Optional[AppliedLevelEnumType] = None


# This class is the input for the 'list_service_quota_increase_requests_in_template' function.
class ListServiceQuotaIncreaseRequestsInTemplateRequest(BaseValidatorModel):
    ServiceCode: Optional[str] = None
    AwsRegion: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_service_quotas' function.
class ListServiceQuotasRequest(BaseValidatorModel):
    ServiceCode: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    QuotaCode: Optional[str] = None
    QuotaAppliedAtLevel: Optional[AppliedLevelEnumType] = None


# This class is the input for the 'list_services' function.
class ListServicesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ServiceInfo(BaseValidatorModel):
    ServiceCode: Optional[str] = None
    ServiceName: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class MetricInfo(BaseValidatorModel):
    MetricNamespace: Optional[str] = None
    MetricName: Optional[str] = None
    MetricDimensions: Optional[Dict[str, str]] = None
    MetricStatisticRecommendation: Optional[str] = None


# This class is the input for the 'put_service_quota_increase_request_into_template' function.
class PutServiceQuotaIncreaseRequestIntoTemplateRequest(BaseValidatorModel):
    QuotaCode: str
    ServiceCode: str
    AwsRegion: str
    DesiredValue: float


class QuotaContextInfo(BaseValidatorModel):
    ContextScope: Optional[QuotaContextScopeType] = None
    ContextScopeType: Optional[str] = None
    ContextId: Optional[str] = None


class QuotaPeriod(BaseValidatorModel):
    PeriodValue: Optional[int] = None
    PeriodUnit: Optional[PeriodUnitType] = None


# This class is the input for the 'request_service_quota_increase' function.
class RequestServiceQuotaIncreaseRequest(BaseValidatorModel):
    ServiceCode: str
    QuotaCode: str
    DesiredValue: float
    ContextId: Optional[str] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: List[str]


class GetAssociationForServiceQuotaTemplateResponse(BaseValidatorModel):
    ServiceQuotaTemplateAssociationStatus: ServiceQuotaTemplateAssociationStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_service_quota_increase_request_from_template' function.
class GetServiceQuotaIncreaseRequestFromTemplateResponse(BaseValidatorModel):
    ServiceQuotaIncreaseRequestInTemplate: ServiceQuotaIncreaseRequestInTemplate
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_service_quota_increase_requests_in_template' function.
class ListServiceQuotaIncreaseRequestsInTemplateResponse(BaseValidatorModel):
    ServiceQuotaIncreaseRequestInTemplateList: List[ServiceQuotaIncreaseRequestInTemplate]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'put_service_quota_increase_request_into_template' function.
class PutServiceQuotaIncreaseRequestIntoTemplateResponse(BaseValidatorModel):
    ServiceQuotaIncreaseRequestInTemplate: ServiceQuotaIncreaseRequestInTemplate
    ResponseMetadata: ResponseMetadata


class ListAWSDefaultServiceQuotasRequestPaginate(BaseValidatorModel):
    ServiceCode: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRequestedServiceQuotaChangeHistoryByQuotaRequestPaginate(BaseValidatorModel):
    ServiceCode: str
    QuotaCode: str
    Status: Optional[RequestStatusType] = None
    QuotaRequestedAtLevel: Optional[AppliedLevelEnumType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRequestedServiceQuotaChangeHistoryRequestPaginate(BaseValidatorModel):
    ServiceCode: Optional[str] = None
    Status: Optional[RequestStatusType] = None
    QuotaRequestedAtLevel: Optional[AppliedLevelEnumType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListServiceQuotaIncreaseRequestsInTemplateRequestPaginate(BaseValidatorModel):
    ServiceCode: Optional[str] = None
    AwsRegion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListServiceQuotasRequestPaginate(BaseValidatorModel):
    ServiceCode: str
    QuotaCode: Optional[str] = None
    QuotaAppliedAtLevel: Optional[AppliedLevelEnumType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListServicesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_services' function.
class ListServicesResponse(BaseValidatorModel):
    Services: List[ServiceInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: List[Tag]


class RequestedServiceQuotaChange(BaseValidatorModel):
    Id: Optional[str] = None
    CaseId: Optional[str] = None
    ServiceCode: Optional[str] = None
    ServiceName: Optional[str] = None
    QuotaCode: Optional[str] = None
    QuotaName: Optional[str] = None
    DesiredValue: Optional[float] = None
    Status: Optional[RequestStatusType] = None
    Created: Optional[datetime] = None
    LastUpdated: Optional[datetime] = None
    Requester: Optional[str] = None
    QuotaArn: Optional[str] = None
    GlobalQuota: Optional[bool] = None
    Unit: Optional[str] = None
    QuotaRequestedAtLevel: Optional[AppliedLevelEnumType] = None
    QuotaContext: Optional[QuotaContextInfo] = None


class ServiceQuota(BaseValidatorModel):
    ServiceCode: Optional[str] = None
    ServiceName: Optional[str] = None
    QuotaArn: Optional[str] = None
    QuotaCode: Optional[str] = None
    QuotaName: Optional[str] = None
    Value: Optional[float] = None
    Unit: Optional[str] = None
    Adjustable: Optional[bool] = None
    GlobalQuota: Optional[bool] = None
    UsageMetric: Optional[MetricInfo] = None
    Period: Optional[QuotaPeriod] = None
    ErrorReason: Optional[ErrorReason] = None
    QuotaAppliedAtLevel: Optional[AppliedLevelEnumType] = None
    QuotaContext: Optional[QuotaContextInfo] = None


# This class is the output for the 'get_requested_service_quota_change' function.
class GetRequestedServiceQuotaChangeResponse(BaseValidatorModel):
    RequestedQuota: RequestedServiceQuotaChange
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_requested_service_quota_change_history_by_quota' function.
class ListRequestedServiceQuotaChangeHistoryByQuotaResponse(BaseValidatorModel):
    RequestedQuotas: List[RequestedServiceQuotaChange]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_requested_service_quota_change_history' function.
class ListRequestedServiceQuotaChangeHistoryResponse(BaseValidatorModel):
    RequestedQuotas: List[RequestedServiceQuotaChange]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'request_service_quota_increase' function.
class RequestServiceQuotaIncreaseResponse(BaseValidatorModel):
    RequestedQuota: RequestedServiceQuotaChange
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_aws_default_service_quota' function.
class GetAWSDefaultServiceQuotaResponse(BaseValidatorModel):
    Quota: ServiceQuota
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_service_quota' function.
class GetServiceQuotaResponse(BaseValidatorModel):
    Quota: ServiceQuota
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_aws_default_service_quotas' function.
class ListAWSDefaultServiceQuotasResponse(BaseValidatorModel):
    Quotas: List[ServiceQuota]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_service_quotas' function.
class ListServiceQuotasResponse(BaseValidatorModel):
    Quotas: List[ServiceQuota]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None
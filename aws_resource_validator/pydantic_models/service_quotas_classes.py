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
from aws_resource_validator.pydantic_models.service_quotas_constants import *

class DeleteServiceQuotaIncreaseRequestFromTemplateRequestTypeDef(BaseValidatorModel):
    ServiceCode: str
    QuotaCode: str
    AwsRegion: str


class ErrorReasonTypeDef(BaseValidatorModel):
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None


class GetAWSDefaultServiceQuotaRequestTypeDef(BaseValidatorModel):
    ServiceCode: str
    QuotaCode: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class GetRequestedServiceQuotaChangeRequestTypeDef(BaseValidatorModel):
    RequestId: str


class GetServiceQuotaIncreaseRequestFromTemplateRequestTypeDef(BaseValidatorModel):
    ServiceCode: str
    QuotaCode: str
    AwsRegion: str


class GetServiceQuotaRequestTypeDef(BaseValidatorModel):
    ServiceCode: str
    QuotaCode: str
    ContextId: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAWSDefaultServiceQuotasRequestTypeDef(BaseValidatorModel):
    ServiceCode: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListRequestedServiceQuotaChangeHistoryByQuotaRequestTypeDef(BaseValidatorModel):
    ServiceCode: str
    QuotaCode: str
    Status: Optional[RequestStatusType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    QuotaRequestedAtLevel: Optional[AppliedLevelEnumType] = None


class ListRequestedServiceQuotaChangeHistoryRequestTypeDef(BaseValidatorModel):
    ServiceCode: Optional[str] = None
    Status: Optional[RequestStatusType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    QuotaRequestedAtLevel: Optional[AppliedLevelEnumType] = None


class ListServiceQuotaIncreaseRequestsInTemplateRequestTypeDef(BaseValidatorModel):
    ServiceCode: Optional[str] = None
    AwsRegion: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListServiceQuotasRequestTypeDef(BaseValidatorModel):
    ServiceCode: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    QuotaCode: Optional[str] = None
    QuotaAppliedAtLevel: Optional[AppliedLevelEnumType] = None


class ListServicesRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class MetricInfoTypeDef(BaseValidatorModel):
    MetricNamespace: Optional[str] = None
    MetricName: Optional[str] = None
    MetricDimensions: Optional[Dict[str, str]] = None
    MetricStatisticRecommendation: Optional[str] = None


class PutServiceQuotaIncreaseRequestIntoTemplateRequestTypeDef(BaseValidatorModel):
    QuotaCode: str
    ServiceCode: str
    AwsRegion: str
    DesiredValue: float


class QuotaContextInfoTypeDef(BaseValidatorModel):
    ContextScope: Optional[QuotaContextScopeType] = None
    ContextScopeType: Optional[str] = None
    ContextId: Optional[str] = None


class QuotaPeriodTypeDef(BaseValidatorModel):
    PeriodValue: Optional[int] = None
    PeriodUnit: Optional[PeriodUnitType] = None


class RequestServiceQuotaIncreaseRequestTypeDef(BaseValidatorModel):
    ServiceCode: str
    QuotaCode: str
    DesiredValue: float
    ContextId: Optional[str] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class GetAssociationForServiceQuotaTemplateResponseTypeDef(BaseValidatorModel):
    ServiceQuotaTemplateAssociationStatus: ServiceQuotaTemplateAssociationStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class ServiceQuotaIncreaseRequestInTemplateTypeDef(BaseValidatorModel):
    pass


class GetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef(BaseValidatorModel):
    ServiceQuotaIncreaseRequestInTemplate: ServiceQuotaIncreaseRequestInTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef(BaseValidatorModel):
    ServiceQuotaIncreaseRequestInTemplateList: List[ServiceQuotaIncreaseRequestInTemplateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class PutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef(BaseValidatorModel):
    ServiceQuotaIncreaseRequestInTemplate: ServiceQuotaIncreaseRequestInTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListAWSDefaultServiceQuotasRequestPaginateTypeDef(BaseValidatorModel):
    ServiceCode: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRequestedServiceQuotaChangeHistoryByQuotaRequestPaginateTypeDef(BaseValidatorModel):
    ServiceCode: str
    QuotaCode: str
    Status: Optional[RequestStatusType] = None
    QuotaRequestedAtLevel: Optional[AppliedLevelEnumType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRequestedServiceQuotaChangeHistoryRequestPaginateTypeDef(BaseValidatorModel):
    ServiceCode: Optional[str] = None
    Status: Optional[RequestStatusType] = None
    QuotaRequestedAtLevel: Optional[AppliedLevelEnumType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListServiceQuotaIncreaseRequestsInTemplateRequestPaginateTypeDef(BaseValidatorModel):
    ServiceCode: Optional[str] = None
    AwsRegion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListServiceQuotasRequestPaginateTypeDef(BaseValidatorModel):
    ServiceCode: str
    QuotaCode: Optional[str] = None
    QuotaAppliedAtLevel: Optional[AppliedLevelEnumType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListServicesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ServiceInfoTypeDef(BaseValidatorModel):
    pass


class ListServicesResponseTypeDef(BaseValidatorModel):
    Services: List[ServiceInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]


class RequestedServiceQuotaChangeTypeDef(BaseValidatorModel):
    pass


class GetRequestedServiceQuotaChangeResponseTypeDef(BaseValidatorModel):
    RequestedQuota: RequestedServiceQuotaChangeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef(BaseValidatorModel):
    RequestedQuotas: List[RequestedServiceQuotaChangeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListRequestedServiceQuotaChangeHistoryResponseTypeDef(BaseValidatorModel):
    RequestedQuotas: List[RequestedServiceQuotaChangeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class RequestServiceQuotaIncreaseResponseTypeDef(BaseValidatorModel):
    RequestedQuota: RequestedServiceQuotaChangeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ServiceQuotaTypeDef(BaseValidatorModel):
    pass


class GetAWSDefaultServiceQuotaResponseTypeDef(BaseValidatorModel):
    Quota: ServiceQuotaTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetServiceQuotaResponseTypeDef(BaseValidatorModel):
    Quota: ServiceQuotaTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListAWSDefaultServiceQuotasResponseTypeDef(BaseValidatorModel):
    Quotas: List[ServiceQuotaTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListServiceQuotasResponseTypeDef(BaseValidatorModel):
    Quotas: List[ServiceQuotaTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None



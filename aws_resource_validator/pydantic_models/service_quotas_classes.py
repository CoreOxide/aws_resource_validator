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
from aws_resource_validator.pydantic_models.service_quotas_constants import *

class DeleteServiceQuotaIncreaseRequestFromTemplateRequestRequestTypeDef(BaseModel):
    ServiceCode: str
    QuotaCode: str
    AwsRegion: str

class ErrorReasonTypeDef(BaseModel):
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None

class GetAWSDefaultServiceQuotaRequestRequestTypeDef(BaseModel):
    ServiceCode: str
    QuotaCode: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class GetRequestedServiceQuotaChangeRequestRequestTypeDef(BaseModel):
    RequestId: str

class GetServiceQuotaIncreaseRequestFromTemplateRequestRequestTypeDef(BaseModel):
    ServiceCode: str
    QuotaCode: str
    AwsRegion: str

class ServiceQuotaIncreaseRequestInTemplateTypeDef(BaseModel):
    ServiceCode: Optional[str] = None
    ServiceName: Optional[str] = None
    QuotaCode: Optional[str] = None
    QuotaName: Optional[str] = None
    DesiredValue: Optional[float] = None
    AwsRegion: Optional[str] = None
    Unit: Optional[str] = None
    GlobalQuota: Optional[bool] = None

class GetServiceQuotaRequestRequestTypeDef(BaseModel):
    ServiceCode: str
    QuotaCode: str
    ContextId: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAWSDefaultServiceQuotasRequestRequestTypeDef(BaseModel):
    ServiceCode: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListRequestedServiceQuotaChangeHistoryByQuotaRequestRequestTypeDef(BaseModel):
    ServiceCode: str
    QuotaCode: str
    Status: Optional[RequestStatusType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    QuotaRequestedAtLevel: Optional[AppliedLevelEnumType] = None

class ListRequestedServiceQuotaChangeHistoryRequestRequestTypeDef(BaseModel):
    ServiceCode: Optional[str] = None
    Status: Optional[RequestStatusType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    QuotaRequestedAtLevel: Optional[AppliedLevelEnumType] = None

class ListServiceQuotaIncreaseRequestsInTemplateRequestRequestTypeDef(BaseModel):
    ServiceCode: Optional[str] = None
    AwsRegion: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListServiceQuotasRequestRequestTypeDef(BaseModel):
    ServiceCode: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    QuotaCode: Optional[str] = None
    QuotaAppliedAtLevel: Optional[AppliedLevelEnumType] = None

class ListServicesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ServiceInfoTypeDef(BaseModel):
    ServiceCode: Optional[str] = None
    ServiceName: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class MetricInfoTypeDef(BaseModel):
    MetricNamespace: Optional[str] = None
    MetricName: Optional[str] = None
    MetricDimensions: Optional[Dict[str, str]] = None
    MetricStatisticRecommendation: Optional[str] = None

class PutServiceQuotaIncreaseRequestIntoTemplateRequestRequestTypeDef(BaseModel):
    QuotaCode: str
    ServiceCode: str
    AwsRegion: str
    DesiredValue: float

class QuotaContextInfoTypeDef(BaseModel):
    ContextScope: Optional[QuotaContextScopeType] = None
    ContextScopeType: Optional[str] = None
    ContextId: Optional[str] = None

class QuotaPeriodTypeDef(BaseModel):
    PeriodValue: Optional[int] = None
    PeriodUnit: Optional[PeriodUnitType] = None

class RequestServiceQuotaIncreaseRequestRequestTypeDef(BaseModel):
    ServiceCode: str
    QuotaCode: str
    DesiredValue: float
    ContextId: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class GetAssociationForServiceQuotaTemplateResponseTypeDef(BaseModel):
    ServiceQuotaTemplateAssociationStatus: ServiceQuotaTemplateAssociationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef(BaseModel):
    ServiceQuotaIncreaseRequestInTemplate: ServiceQuotaIncreaseRequestInTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef(BaseModel):
    ServiceQuotaIncreaseRequestInTemplateList: List[       ServiceQuotaIncreaseRequestInTemplateTypeDef     ]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef(BaseModel):
    ServiceQuotaIncreaseRequestInTemplate: ServiceQuotaIncreaseRequestInTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAWSDefaultServiceQuotasRequestListAWSDefaultServiceQuotasPaginateTypeDef(BaseModel):
    ServiceCode: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRequestedServiceQuotaChangeHistoryByQuotaRequestListRequestedServiceQuotaChangeHistoryByQuotaPaginateTypeDef(BaseModel):
    ServiceCode: str
    QuotaCode: str
    Status: Optional[RequestStatusType] = None
    QuotaRequestedAtLevel: Optional[AppliedLevelEnumType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRequestedServiceQuotaChangeHistoryRequestListRequestedServiceQuotaChangeHistoryPaginateTypeDef(BaseModel):
    ServiceCode: Optional[str] = None
    Status: Optional[RequestStatusType] = None
    QuotaRequestedAtLevel: Optional[AppliedLevelEnumType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServiceQuotaIncreaseRequestsInTemplateRequestListServiceQuotaIncreaseRequestsInTemplatePaginateTypeDef(BaseModel):
    ServiceCode: Optional[str] = None
    AwsRegion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServiceQuotasRequestListServiceQuotasPaginateTypeDef(BaseModel):
    ServiceCode: str
    QuotaCode: Optional[str] = None
    QuotaAppliedAtLevel: Optional[AppliedLevelEnumType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServicesRequestListServicesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServicesResponseTypeDef(BaseModel):
    NextToken: str
    Services: List[ServiceInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class RequestedServiceQuotaChangeTypeDef(BaseModel):
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
    QuotaContext: Optional[QuotaContextInfoTypeDef] = None

class ServiceQuotaTypeDef(BaseModel):
    ServiceCode: Optional[str] = None
    ServiceName: Optional[str] = None
    QuotaArn: Optional[str] = None
    QuotaCode: Optional[str] = None
    QuotaName: Optional[str] = None
    Value: Optional[float] = None
    Unit: Optional[str] = None
    Adjustable: Optional[bool] = None
    GlobalQuota: Optional[bool] = None
    UsageMetric: Optional[MetricInfoTypeDef] = None
    Period: Optional[QuotaPeriodTypeDef] = None
    ErrorReason: Optional[ErrorReasonTypeDef] = None
    QuotaAppliedAtLevel: Optional[AppliedLevelEnumType] = None
    QuotaContext: Optional[QuotaContextInfoTypeDef] = None

class GetRequestedServiceQuotaChangeResponseTypeDef(BaseModel):
    RequestedQuota: RequestedServiceQuotaChangeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef(BaseModel):
    NextToken: str
    RequestedQuotas: List[RequestedServiceQuotaChangeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRequestedServiceQuotaChangeHistoryResponseTypeDef(BaseModel):
    NextToken: str
    RequestedQuotas: List[RequestedServiceQuotaChangeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RequestServiceQuotaIncreaseResponseTypeDef(BaseModel):
    RequestedQuota: RequestedServiceQuotaChangeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAWSDefaultServiceQuotaResponseTypeDef(BaseModel):
    Quota: ServiceQuotaTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceQuotaResponseTypeDef(BaseModel):
    Quota: ServiceQuotaTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAWSDefaultServiceQuotasResponseTypeDef(BaseModel):
    NextToken: str
    Quotas: List[ServiceQuotaTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListServiceQuotasResponseTypeDef(BaseModel):
    NextToken: str
    Quotas: List[ServiceQuotaTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


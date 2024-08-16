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
from aws_resource_validator.pydantic_models.service_quotas_constants import *

class DeleteServiceQuotaIncreaseRequestFromTemplateRequestRequestTypeDef(BaseValidatorModel):
    ServiceCode: str
    QuotaCode: str
    AwsRegion: str

class ErrorReasonTypeDef(BaseValidatorModel):
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None

class GetAWSDefaultServiceQuotaRequestRequestTypeDef(BaseValidatorModel):
    ServiceCode: str
    QuotaCode: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class GetRequestedServiceQuotaChangeRequestRequestTypeDef(BaseValidatorModel):
    RequestId: str

class GetServiceQuotaIncreaseRequestFromTemplateRequestRequestTypeDef(BaseValidatorModel):
    ServiceCode: str
    QuotaCode: str
    AwsRegion: str

class ServiceQuotaIncreaseRequestInTemplateTypeDef(BaseValidatorModel):
    ServiceCode: Optional[str] = None
    ServiceName: Optional[str] = None
    QuotaCode: Optional[str] = None
    QuotaName: Optional[str] = None
    DesiredValue: Optional[float] = None
    AwsRegion: Optional[str] = None
    Unit: Optional[str] = None
    GlobalQuota: Optional[bool] = None

class GetServiceQuotaRequestRequestTypeDef(BaseValidatorModel):
    ServiceCode: str
    QuotaCode: str
    ContextId: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAWSDefaultServiceQuotasRequestRequestTypeDef(BaseValidatorModel):
    ServiceCode: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListRequestedServiceQuotaChangeHistoryByQuotaRequestRequestTypeDef(BaseValidatorModel):
    ServiceCode: str
    QuotaCode: str
    Status: Optional[RequestStatusType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    QuotaRequestedAtLevel: Optional[AppliedLevelEnumType] = None

class ListRequestedServiceQuotaChangeHistoryRequestRequestTypeDef(BaseValidatorModel):
    ServiceCode: Optional[str] = None
    Status: Optional[RequestStatusType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    QuotaRequestedAtLevel: Optional[AppliedLevelEnumType] = None

class ListServiceQuotaIncreaseRequestsInTemplateRequestRequestTypeDef(BaseValidatorModel):
    ServiceCode: Optional[str] = None
    AwsRegion: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListServiceQuotasRequestRequestTypeDef(BaseValidatorModel):
    ServiceCode: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    QuotaCode: Optional[str] = None
    QuotaAppliedAtLevel: Optional[AppliedLevelEnumType] = None

class ListServicesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ServiceInfoTypeDef(BaseValidatorModel):
    ServiceCode: Optional[str] = None
    ServiceName: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class MetricInfoTypeDef(BaseValidatorModel):
    MetricNamespace: Optional[str] = None
    MetricName: Optional[str] = None
    MetricDimensions: Optional[Dict[str, str]] = None
    MetricStatisticRecommendation: Optional[str] = None

class PutServiceQuotaIncreaseRequestIntoTemplateRequestRequestTypeDef(BaseValidatorModel):
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

class RequestServiceQuotaIncreaseRequestRequestTypeDef(BaseValidatorModel):
    ServiceCode: str
    QuotaCode: str
    DesiredValue: float
    ContextId: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class GetAssociationForServiceQuotaTemplateResponseTypeDef(BaseValidatorModel):
    ServiceQuotaTemplateAssociationStatus: ServiceQuotaTemplateAssociationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef(BaseValidatorModel):
    ServiceQuotaIncreaseRequestInTemplate: ServiceQuotaIncreaseRequestInTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef(BaseValidatorModel):
    ServiceQuotaIncreaseRequestInTemplateList: List[       ServiceQuotaIncreaseRequestInTemplateTypeDef     ]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef(BaseValidatorModel):
    ServiceQuotaIncreaseRequestInTemplate: ServiceQuotaIncreaseRequestInTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAWSDefaultServiceQuotasRequestListAWSDefaultServiceQuotasPaginateTypeDef(BaseValidatorModel):
    ServiceCode: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRequestedServiceQuotaChangeHistoryByQuotaRequestListRequestedServiceQuotaChangeHistoryByQuotaPaginateTypeDef(BaseValidatorModel):
    ServiceCode: str
    QuotaCode: str
    Status: Optional[RequestStatusType] = None
    QuotaRequestedAtLevel: Optional[AppliedLevelEnumType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRequestedServiceQuotaChangeHistoryRequestListRequestedServiceQuotaChangeHistoryPaginateTypeDef(BaseValidatorModel):
    ServiceCode: Optional[str] = None
    Status: Optional[RequestStatusType] = None
    QuotaRequestedAtLevel: Optional[AppliedLevelEnumType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServiceQuotaIncreaseRequestsInTemplateRequestListServiceQuotaIncreaseRequestsInTemplatePaginateTypeDef(BaseValidatorModel):
    ServiceCode: Optional[str] = None
    AwsRegion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServiceQuotasRequestListServiceQuotasPaginateTypeDef(BaseValidatorModel):
    ServiceCode: str
    QuotaCode: Optional[str] = None
    QuotaAppliedAtLevel: Optional[AppliedLevelEnumType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServicesRequestListServicesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServicesResponseTypeDef(BaseValidatorModel):
    NextToken: str
    Services: List[ServiceInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class RequestedServiceQuotaChangeTypeDef(BaseValidatorModel):
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

class ServiceQuotaTypeDef(BaseValidatorModel):
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

class GetRequestedServiceQuotaChangeResponseTypeDef(BaseValidatorModel):
    RequestedQuota: RequestedServiceQuotaChangeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef(BaseValidatorModel):
    NextToken: str
    RequestedQuotas: List[RequestedServiceQuotaChangeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRequestedServiceQuotaChangeHistoryResponseTypeDef(BaseValidatorModel):
    NextToken: str
    RequestedQuotas: List[RequestedServiceQuotaChangeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RequestServiceQuotaIncreaseResponseTypeDef(BaseValidatorModel):
    RequestedQuota: RequestedServiceQuotaChangeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAWSDefaultServiceQuotaResponseTypeDef(BaseValidatorModel):
    Quota: ServiceQuotaTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceQuotaResponseTypeDef(BaseValidatorModel):
    Quota: ServiceQuotaTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAWSDefaultServiceQuotasResponseTypeDef(BaseValidatorModel):
    NextToken: str
    Quotas: List[ServiceQuotaTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListServiceQuotasResponseTypeDef(BaseValidatorModel):
    NextToken: str
    Quotas: List[ServiceQuotaTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


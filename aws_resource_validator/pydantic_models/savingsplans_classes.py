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
from aws_resource_validator.pydantic_models.savingsplans_constants import *

class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteQueuedSavingsPlanRequest(BaseValidatorModel):
    savingsPlanId: str


class SavingsPlanRateFilter(BaseValidatorModel):
    name: Optional[SavingsPlanRateFilterNameType] = None
    values: Optional[Sequence[str]] = None


class SavingsPlanOfferingRateFilterElement(BaseValidatorModel):
    name: Optional[SavingsPlanRateFilterAttributeType] = None
    values: Optional[Sequence[str]] = None


class SavingsPlanOfferingFilterElement(BaseValidatorModel):
    name: Optional[SavingsPlanOfferingFilterAttributeType] = None
    values: Optional[Sequence[str]] = None


class SavingsPlanFilter(BaseValidatorModel):
    name: Optional[SavingsPlansFilterNameType] = None
    values: Optional[Sequence[str]] = None


class SavingsPlan(BaseValidatorModel):
    offeringId: Optional[str] = None
    savingsPlanId: Optional[str] = None
    savingsPlanArn: Optional[str] = None
    description: Optional[str] = None
    start: Optional[str] = None
    end: Optional[str] = None
    state: Optional[SavingsPlanStateType] = None
    region: Optional[str] = None
    ec2InstanceFamily: Optional[str] = None
    savingsPlanType: Optional[SavingsPlanTypeType] = None
    paymentOption: Optional[SavingsPlanPaymentOptionType] = None
    productTypes: Optional[List[SavingsPlanProductTypeType]] = None
    currency: Optional[CurrencyCodeType] = None
    commitment: Optional[str] = None
    upfrontPaymentAmount: Optional[str] = None
    recurringPaymentAmount: Optional[str] = None
    termDurationInSeconds: Optional[int] = None
    tags: Optional[Dict[str, str]] = None
    returnableUntil: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class ParentSavingsPlanOffering(BaseValidatorModel):
    offeringId: Optional[str] = None
    paymentOption: Optional[SavingsPlanPaymentOptionType] = None
    planType: Optional[SavingsPlanTypeType] = None
    durationSeconds: Optional[int] = None
    currency: Optional[CurrencyCodeType] = None
    planDescription: Optional[str] = None


class ReturnSavingsPlanRequest(BaseValidatorModel):
    savingsPlanId: str
    clientToken: Optional[str] = None


class SavingsPlanOfferingProperty(BaseValidatorModel):
    name: Optional[SavingsPlanOfferingPropertyKeyType] = None
    value: Optional[str] = None


class SavingsPlanOfferingRateProperty(BaseValidatorModel):
    name: Optional[str] = None
    value: Optional[str] = None


class SavingsPlanRateProperty(BaseValidatorModel):
    name: Optional[SavingsPlanRatePropertyKeyType] = None
    value: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class Timestamp(BaseValidatorModel):
    pass


class CreateSavingsPlanRequest(BaseValidatorModel):
    savingsPlanOfferingId: str
    commitment: str
    upfrontPaymentAmount: Optional[str] = None
    purchaseTime: Optional[Timestamp] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class CreateSavingsPlanResponse(BaseValidatorModel):
    savingsPlanId: str
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ReturnSavingsPlanResponse(BaseValidatorModel):
    savingsPlanId: str
    ResponseMetadata: ResponseMetadata


class DescribeSavingsPlanRatesRequest(BaseValidatorModel):
    savingsPlanId: str
    filters: Optional[Sequence[SavingsPlanRateFilter]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class DescribeSavingsPlansOfferingRatesRequest(BaseValidatorModel):
    savingsPlanOfferingIds: Optional[Sequence[str]] = None
    savingsPlanPaymentOptions: Optional[Sequence[SavingsPlanPaymentOptionType]] = None
    savingsPlanTypes: Optional[Sequence[SavingsPlanTypeType]] = None
    products: Optional[Sequence[SavingsPlanProductTypeType]] = None
    serviceCodes: Optional[Sequence[SavingsPlanRateServiceCodeType]] = None
    usageTypes: Optional[Sequence[str]] = None
    operations: Optional[Sequence[str]] = None
    filters: Optional[Sequence[SavingsPlanOfferingRateFilterElement]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class DescribeSavingsPlansOfferingsRequest(BaseValidatorModel):
    offeringIds: Optional[Sequence[str]] = None
    paymentOptions: Optional[Sequence[SavingsPlanPaymentOptionType]] = None
    productType: Optional[SavingsPlanProductTypeType] = None
    planTypes: Optional[Sequence[SavingsPlanTypeType]] = None
    durations: Optional[Sequence[int]] = None
    currencies: Optional[Sequence[CurrencyCodeType]] = None
    descriptions: Optional[Sequence[str]] = None
    serviceCodes: Optional[Sequence[str]] = None
    usageTypes: Optional[Sequence[str]] = None
    operations: Optional[Sequence[str]] = None
    filters: Optional[Sequence[SavingsPlanOfferingFilterElement]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class DescribeSavingsPlansRequest(BaseValidatorModel):
    savingsPlanArns: Optional[Sequence[str]] = None
    savingsPlanIds: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    states: Optional[Sequence[SavingsPlanStateType]] = None
    filters: Optional[Sequence[SavingsPlanFilter]] = None


class DescribeSavingsPlansResponse(BaseValidatorModel):
    savingsPlans: List[SavingsPlan]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SavingsPlanOffering(BaseValidatorModel):
    offeringId: Optional[str] = None
    productTypes: Optional[List[SavingsPlanProductTypeType]] = None
    planType: Optional[SavingsPlanTypeType] = None
    description: Optional[str] = None
    paymentOption: Optional[SavingsPlanPaymentOptionType] = None
    durationSeconds: Optional[int] = None
    currency: Optional[CurrencyCodeType] = None
    serviceCode: Optional[str] = None
    usageType: Optional[str] = None
    operation: Optional[str] = None
    properties: Optional[List[SavingsPlanOfferingProperty]] = None


class SavingsPlanOfferingRate(BaseValidatorModel):
    savingsPlanOffering: Optional[ParentSavingsPlanOffering] = None
    rate: Optional[str] = None
    unit: Optional[SavingsPlanRateUnitType] = None
    productType: Optional[SavingsPlanProductTypeType] = None
    serviceCode: Optional[SavingsPlanRateServiceCodeType] = None
    usageType: Optional[str] = None
    operation: Optional[str] = None
    properties: Optional[List[SavingsPlanOfferingRateProperty]] = None


class SavingsPlanRate(BaseValidatorModel):
    rate: Optional[str] = None
    currency: Optional[CurrencyCodeType] = None
    unit: Optional[SavingsPlanRateUnitType] = None
    productType: Optional[SavingsPlanProductTypeType] = None
    serviceCode: Optional[SavingsPlanRateServiceCodeType] = None
    usageType: Optional[str] = None
    operation: Optional[str] = None
    properties: Optional[List[SavingsPlanRateProperty]] = None


class DescribeSavingsPlansOfferingsResponse(BaseValidatorModel):
    searchResults: List[SavingsPlanOffering]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DescribeSavingsPlansOfferingRatesResponse(BaseValidatorModel):
    searchResults: List[SavingsPlanOfferingRate]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DescribeSavingsPlanRatesResponse(BaseValidatorModel):
    savingsPlanId: str
    searchResults: List[SavingsPlanRate]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None



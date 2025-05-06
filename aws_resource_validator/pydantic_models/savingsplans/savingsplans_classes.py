from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.savingsplans.savingsplans_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream



Timestamp = Union[datetime, str]


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
    values: Optional[List[str]] = None


class SavingsPlanOfferingRateFilterElement(BaseValidatorModel):
    name: Optional[SavingsPlanRateFilterAttributeType] = None
    values: Optional[List[str]] = None


class SavingsPlanOfferingFilterElement(BaseValidatorModel):
    name: Optional[SavingsPlanOfferingFilterAttributeType] = None
    values: Optional[List[str]] = None


class SavingsPlanFilter(BaseValidatorModel):
    name: Optional[SavingsPlansFilterNameType] = None
    values: Optional[List[str]] = None


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
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class CreateSavingsPlanRequest(BaseValidatorModel):
    savingsPlanOfferingId: str
    commitment: str
    upfrontPaymentAmount: Optional[str] = None
    purchaseTime: Optional[Timestamp] = None
    clientToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


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
    filters: Optional[List[SavingsPlanRateFilter]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class DescribeSavingsPlansOfferingRatesRequest(BaseValidatorModel):
    savingsPlanOfferingIds: Optional[List[str]] = None
    savingsPlanPaymentOptions: Optional[List[SavingsPlanPaymentOptionType]] = None
    savingsPlanTypes: Optional[List[SavingsPlanTypeType]] = None
    products: Optional[List[SavingsPlanProductTypeType]] = None
    serviceCodes: Optional[List[SavingsPlanRateServiceCodeType]] = None
    usageTypes: Optional[List[str]] = None
    operations: Optional[List[str]] = None
    filters: Optional[List[SavingsPlanOfferingRateFilterElement]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class DescribeSavingsPlansOfferingsRequest(BaseValidatorModel):
    offeringIds: Optional[List[str]] = None
    paymentOptions: Optional[List[SavingsPlanPaymentOptionType]] = None
    productType: Optional[SavingsPlanProductTypeType] = None
    planTypes: Optional[List[SavingsPlanTypeType]] = None
    durations: Optional[List[int]] = None
    currencies: Optional[List[CurrencyCodeType]] = None
    descriptions: Optional[List[str]] = None
    serviceCodes: Optional[List[str]] = None
    usageTypes: Optional[List[str]] = None
    operations: Optional[List[str]] = None
    filters: Optional[List[SavingsPlanOfferingFilterElement]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class DescribeSavingsPlansRequest(BaseValidatorModel):
    savingsPlanArns: Optional[List[str]] = None
    savingsPlanIds: Optional[List[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    states: Optional[List[SavingsPlanStateType]] = None
    filters: Optional[List[SavingsPlanFilter]] = None


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
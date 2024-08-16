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
from aws_resource_validator.pydantic_models.savingsplans_constants import *

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DeleteQueuedSavingsPlanRequestRequestTypeDef(BaseValidatorModel):
    savingsPlanId: str

class SavingsPlanRateFilterTypeDef(BaseValidatorModel):
    name: Optional[SavingsPlanRateFilterNameType] = None
    values: Optional[Sequence[str]] = None

class SavingsPlanOfferingRateFilterElementTypeDef(BaseValidatorModel):
    name: Optional[SavingsPlanRateFilterAttributeType] = None
    values: Optional[Sequence[str]] = None

class SavingsPlanOfferingFilterElementTypeDef(BaseValidatorModel):
    name: Optional[SavingsPlanOfferingFilterAttributeType] = None
    values: Optional[Sequence[str]] = None

class SavingsPlanFilterTypeDef(BaseValidatorModel):
    name: Optional[SavingsPlansFilterNameType] = None
    values: Optional[Sequence[str]] = None

class SavingsPlanTypeDef(BaseValidatorModel):
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

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class ParentSavingsPlanOfferingTypeDef(BaseValidatorModel):
    offeringId: Optional[str] = None
    paymentOption: Optional[SavingsPlanPaymentOptionType] = None
    planType: Optional[SavingsPlanTypeType] = None
    durationSeconds: Optional[int] = None
    currency: Optional[CurrencyCodeType] = None
    planDescription: Optional[str] = None

class ReturnSavingsPlanRequestRequestTypeDef(BaseValidatorModel):
    savingsPlanId: str
    clientToken: Optional[str] = None

class SavingsPlanOfferingPropertyTypeDef(BaseValidatorModel):
    name: Optional[SavingsPlanOfferingPropertyKeyType] = None
    value: Optional[str] = None

class SavingsPlanOfferingRatePropertyTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    value: Optional[str] = None

class SavingsPlanRatePropertyTypeDef(BaseValidatorModel):
    name: Optional[SavingsPlanRatePropertyKeyType] = None
    value: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class CreateSavingsPlanRequestRequestTypeDef(BaseValidatorModel):
    savingsPlanOfferingId: str
    commitment: str
    upfrontPaymentAmount: Optional[str] = None
    purchaseTime: Optional[TimestampTypeDef] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateSavingsPlanResponseTypeDef(BaseValidatorModel):
    savingsPlanId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ReturnSavingsPlanResponseTypeDef(BaseValidatorModel):
    savingsPlanId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSavingsPlanRatesRequestRequestTypeDef(BaseValidatorModel):
    savingsPlanId: str
    filters: Optional[Sequence[SavingsPlanRateFilterTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class DescribeSavingsPlansOfferingRatesRequestRequestTypeDef(BaseValidatorModel):
    savingsPlanOfferingIds: Optional[Sequence[str]] = None
    savingsPlanPaymentOptions: Optional[Sequence[SavingsPlanPaymentOptionType]] = None
    savingsPlanTypes: Optional[Sequence[SavingsPlanTypeType]] = None
    products: Optional[Sequence[SavingsPlanProductTypeType]] = None
    serviceCodes: Optional[Sequence[SavingsPlanRateServiceCodeType]] = None
    usageTypes: Optional[Sequence[str]] = None
    operations: Optional[Sequence[str]] = None
    filters: Optional[Sequence[SavingsPlanOfferingRateFilterElementTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class DescribeSavingsPlansOfferingsRequestRequestTypeDef(BaseValidatorModel):
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
    filters: Optional[Sequence[SavingsPlanOfferingFilterElementTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class DescribeSavingsPlansRequestRequestTypeDef(BaseValidatorModel):
    savingsPlanArns: Optional[Sequence[str]] = None
    savingsPlanIds: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    states: Optional[Sequence[SavingsPlanStateType]] = None
    filters: Optional[Sequence[SavingsPlanFilterTypeDef]] = None

class DescribeSavingsPlansResponseTypeDef(BaseValidatorModel):
    savingsPlans: List[SavingsPlanTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SavingsPlanOfferingTypeDef(BaseValidatorModel):
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
    properties: Optional[List[SavingsPlanOfferingPropertyTypeDef]] = None

class SavingsPlanOfferingRateTypeDef(BaseValidatorModel):
    savingsPlanOffering: Optional[ParentSavingsPlanOfferingTypeDef] = None
    rate: Optional[str] = None
    unit: Optional[SavingsPlanRateUnitType] = None
    productType: Optional[SavingsPlanProductTypeType] = None
    serviceCode: Optional[SavingsPlanRateServiceCodeType] = None
    usageType: Optional[str] = None
    operation: Optional[str] = None
    properties: Optional[List[SavingsPlanOfferingRatePropertyTypeDef]] = None

class SavingsPlanRateTypeDef(BaseValidatorModel):
    rate: Optional[str] = None
    currency: Optional[CurrencyCodeType] = None
    unit: Optional[SavingsPlanRateUnitType] = None
    productType: Optional[SavingsPlanProductTypeType] = None
    serviceCode: Optional[SavingsPlanRateServiceCodeType] = None
    usageType: Optional[str] = None
    operation: Optional[str] = None
    properties: Optional[List[SavingsPlanRatePropertyTypeDef]] = None

class DescribeSavingsPlansOfferingsResponseTypeDef(BaseValidatorModel):
    searchResults: List[SavingsPlanOfferingTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSavingsPlansOfferingRatesResponseTypeDef(BaseValidatorModel):
    searchResults: List[SavingsPlanOfferingRateTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSavingsPlanRatesResponseTypeDef(BaseValidatorModel):
    savingsPlanId: str
    searchResults: List[SavingsPlanRateTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef


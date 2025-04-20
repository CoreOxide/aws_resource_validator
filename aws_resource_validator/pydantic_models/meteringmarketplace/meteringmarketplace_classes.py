from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.meteringmarketplace.meteringmarketplace_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

Timestamp = Union[datetime, str]


class RegisterUsageRequest(BaseValidatorModel):
    ProductCode: str
    PublicKeyVersion: int
    Nonce: Optional[str] = None


class ResolveCustomerRequest(BaseValidatorModel):
    RegistrationToken: str


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class MeterUsageResult(BaseValidatorModel):
    MeteringRecordId: str
    ResponseMetadata: ResponseMetadata


class RegisterUsageResult(BaseValidatorModel):
    PublicKeyRotationTimestamp: datetime
    Signature: str
    ResponseMetadata: ResponseMetadata


class ResolveCustomerResult(BaseValidatorModel):
    CustomerIdentifier: str
    ProductCode: str
    CustomerAWSAccountId: str
    ResponseMetadata: ResponseMetadata


class UsageAllocationOutput(BaseValidatorModel):
    AllocatedUsageQuantity: int
    Tags: Optional[List[Tag]] = None


class UsageAllocation(BaseValidatorModel):
    AllocatedUsageQuantity: int
    Tags: Optional[List[Tag]] = None


class UsageRecordOutput(BaseValidatorModel):
    Timestamp: datetime
    CustomerIdentifier: str
    Dimension: str
    Quantity: Optional[int] = None
    UsageAllocations: Optional[List[UsageAllocationOutput]] = None

UsageAllocationUnion = Union[UsageAllocation, UsageAllocationOutput]


class UsageRecordResult(BaseValidatorModel):
    UsageRecord: Optional[UsageRecordOutput] = None
    MeteringRecordId: Optional[str] = None
    Status: Optional[UsageRecordResultStatusType] = None


class MeterUsageRequest(BaseValidatorModel):
    ProductCode: str
    Timestamp: Timestamp
    UsageDimension: str
    UsageQuantity: Optional[int] = None
    DryRun: Optional[bool] = None
    UsageAllocations: Optional[List[UsageAllocationUnion]] = None


class UsageRecord(BaseValidatorModel):
    Timestamp: Timestamp
    CustomerIdentifier: str
    Dimension: str
    Quantity: Optional[int] = None
    UsageAllocations: Optional[List[UsageAllocationUnion]] = None


class BatchMeterUsageResult(BaseValidatorModel):
    Results: List[UsageRecordResult]
    UnprocessedRecords: List[UsageRecordOutput]
    ResponseMetadata: ResponseMetadata

UsageRecordUnion = Union[UsageRecord, UsageRecordOutput]


class BatchMeterUsageRequest(BaseValidatorModel):
    UsageRecords: List[UsageRecordUnion]
    ProductCode: str
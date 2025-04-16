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
from aws_resource_validator.pydantic_models.meteringmarketplace_constants import *

class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


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
    Tags: Optional[Sequence[Tag]] = None


class UsageRecordOutput(BaseValidatorModel):
    Timestamp: datetime
    CustomerIdentifier: str
    Dimension: str
    Quantity: Optional[int] = None
    UsageAllocations: Optional[List[UsageAllocationOutput]] = None


class UsageRecordResult(BaseValidatorModel):
    UsageRecord: Optional[UsageRecordOutput] = None
    MeteringRecordId: Optional[str] = None
    Status: Optional[UsageRecordResultStatusType] = None


class UsageAllocationUnion(BaseValidatorModel):
    pass


class Timestamp(BaseValidatorModel):
    pass


class MeterUsageRequest(BaseValidatorModel):
    ProductCode: str
    Timestamp: Timestamp
    UsageDimension: str
    UsageQuantity: Optional[int] = None
    DryRun: Optional[bool] = None
    UsageAllocations: Optional[Sequence[UsageAllocationUnion]] = None


class UsageRecord(BaseValidatorModel):
    Timestamp: Timestamp
    CustomerIdentifier: str
    Dimension: str
    Quantity: Optional[int] = None
    UsageAllocations: Optional[Sequence[UsageAllocationUnion]] = None


class BatchMeterUsageResult(BaseValidatorModel):
    Results: List[UsageRecordResult]
    UnprocessedRecords: List[UsageRecordOutput]
    ResponseMetadata: ResponseMetadata


class UsageRecordUnion(BaseValidatorModel):
    pass


class BatchMeterUsageRequest(BaseValidatorModel):
    UsageRecords: Sequence[UsageRecordUnion]
    ProductCode: str



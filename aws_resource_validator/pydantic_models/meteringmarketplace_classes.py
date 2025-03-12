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

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class RegisterUsageRequestTypeDef(BaseValidatorModel):
    ProductCode: str
    PublicKeyVersion: int
    Nonce: Optional[str] = None


class ResolveCustomerRequestTypeDef(BaseValidatorModel):
    RegistrationToken: str


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class MeterUsageResultTypeDef(BaseValidatorModel):
    MeteringRecordId: str
    ResponseMetadata: ResponseMetadataTypeDef


class RegisterUsageResultTypeDef(BaseValidatorModel):
    PublicKeyRotationTimestamp: datetime
    Signature: str
    ResponseMetadata: ResponseMetadataTypeDef


class ResolveCustomerResultTypeDef(BaseValidatorModel):
    CustomerIdentifier: str
    ProductCode: str
    CustomerAWSAccountId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UsageAllocationOutputTypeDef(BaseValidatorModel):
    AllocatedUsageQuantity: int
    Tags: Optional[List[TagTypeDef]] = None


class UsageAllocationTypeDef(BaseValidatorModel):
    AllocatedUsageQuantity: int
    Tags: Optional[Sequence[TagTypeDef]] = None


class UsageRecordOutputTypeDef(BaseValidatorModel):
    Timestamp: datetime
    CustomerIdentifier: str
    Dimension: str
    Quantity: Optional[int] = None
    UsageAllocations: Optional[List[UsageAllocationOutputTypeDef]] = None


class UsageRecordResultTypeDef(BaseValidatorModel):
    UsageRecord: Optional[UsageRecordOutputTypeDef] = None
    MeteringRecordId: Optional[str] = None
    Status: Optional[UsageRecordResultStatusType] = None


class UsageAllocationUnionTypeDef(BaseValidatorModel):
    pass


class TimestampTypeDef(BaseValidatorModel):
    pass


class MeterUsageRequestTypeDef(BaseValidatorModel):
    ProductCode: str
    Timestamp: TimestampTypeDef
    UsageDimension: str
    UsageQuantity: Optional[int] = None
    DryRun: Optional[bool] = None
    UsageAllocations: Optional[Sequence[UsageAllocationUnionTypeDef]] = None


class UsageRecordTypeDef(BaseValidatorModel):
    Timestamp: TimestampTypeDef
    CustomerIdentifier: str
    Dimension: str
    Quantity: Optional[int] = None
    UsageAllocations: Optional[Sequence[UsageAllocationUnionTypeDef]] = None


class BatchMeterUsageResultTypeDef(BaseValidatorModel):
    Results: List[UsageRecordResultTypeDef]
    UnprocessedRecords: List[UsageRecordOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UsageRecordUnionTypeDef(BaseValidatorModel):
    pass


class BatchMeterUsageRequestTypeDef(BaseValidatorModel):
    UsageRecords: Sequence[UsageRecordUnionTypeDef]
    ProductCode: str



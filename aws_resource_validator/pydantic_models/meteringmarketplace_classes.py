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
from aws_resource_validator.pydantic_models.meteringmarketplace_constants import *

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class RegisterUsageRequestRequestTypeDef(BaseValidatorModel):
    ProductCode: str
    PublicKeyVersion: int
    Nonce: Optional[str] = None

class ResolveCustomerRequestRequestTypeDef(BaseValidatorModel):
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

class UsageAllocationTypeDef(BaseValidatorModel):
    AllocatedUsageQuantity: int
    Tags: Optional[Sequence[TagTypeDef]] = None

class MeterUsageRequestRequestTypeDef(BaseValidatorModel):
    ProductCode: str
    Timestamp: TimestampTypeDef
    UsageDimension: str
    UsageQuantity: Optional[int] = None
    DryRun: Optional[bool] = None
    UsageAllocations: Optional[Sequence[UsageAllocationTypeDef]] = None

class UsageRecordTypeDef(BaseValidatorModel):
    Timestamp: TimestampTypeDef
    CustomerIdentifier: str
    Dimension: str
    Quantity: Optional[int] = None
    UsageAllocations: Optional[Sequence[UsageAllocationTypeDef]] = None

class BatchMeterUsageRequestRequestTypeDef(BaseValidatorModel):
    UsageRecords: Sequence[UsageRecordTypeDef]
    ProductCode: str

class UsageRecordResultTypeDef(BaseValidatorModel):
    UsageRecord: Optional[UsageRecordTypeDef] = None
    MeteringRecordId: Optional[str] = None
    Status: Optional[UsageRecordResultStatusType] = None

class BatchMeterUsageResultTypeDef(BaseValidatorModel):
    Results: List[UsageRecordResultTypeDef]
    UnprocessedRecords: List[UsageRecordTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


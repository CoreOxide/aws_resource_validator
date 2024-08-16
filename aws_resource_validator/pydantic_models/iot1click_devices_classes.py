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
from aws_resource_validator.pydantic_models.iot1click_devices_constants import *

class ClaimDevicesByClaimCodeRequestRequestTypeDef(BaseValidatorModel):
    ClaimCode: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DescribeDeviceRequestRequestTypeDef(BaseValidatorModel):
    DeviceId: str

class DeviceDescriptionTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None
    DeviceId: Optional[str] = None
    Enabled: Optional[bool] = None
    RemainingLife: Optional[float] = None
    Type: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

class DeviceTypeDef(BaseValidatorModel):
    Attributes: Optional[Dict[str, Any]] = None
    DeviceId: Optional[str] = None
    Type: Optional[str] = None

class DeviceMethodTypeDef(BaseValidatorModel):
    DeviceType: Optional[str] = None
    MethodName: Optional[str] = None

class FinalizeDeviceClaimRequestRequestTypeDef(BaseValidatorModel):
    DeviceId: str
    Tags: Optional[Mapping[str, str]] = None

class GetDeviceMethodsRequestRequestTypeDef(BaseValidatorModel):
    DeviceId: str

class InitiateDeviceClaimRequestRequestTypeDef(BaseValidatorModel):
    DeviceId: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListDevicesRequestRequestTypeDef(BaseValidatorModel):
    DeviceType: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UnclaimDeviceRequestRequestTypeDef(BaseValidatorModel):
    DeviceId: str

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateDeviceStateRequestRequestTypeDef(BaseValidatorModel):
    DeviceId: str
    Enabled: Optional[bool] = None

class ClaimDevicesByClaimCodeResponseTypeDef(BaseValidatorModel):
    ClaimCode: str
    Total: int
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class FinalizeDeviceClaimResponseTypeDef(BaseValidatorModel):
    State: str
    ResponseMetadata: ResponseMetadataTypeDef

class InitiateDeviceClaimResponseTypeDef(BaseValidatorModel):
    State: str
    ResponseMetadata: ResponseMetadataTypeDef

class InvokeDeviceMethodResponseTypeDef(BaseValidatorModel):
    DeviceMethodResponse: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UnclaimDeviceResponseTypeDef(BaseValidatorModel):
    State: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDeviceResponseTypeDef(BaseValidatorModel):
    DeviceDescription: DeviceDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDevicesResponseTypeDef(BaseValidatorModel):
    Devices: List[DeviceDescriptionTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeviceEventTypeDef(BaseValidatorModel):
    Device: Optional[DeviceTypeDef] = None
    StdEvent: Optional[str] = None

class GetDeviceMethodsResponseTypeDef(BaseValidatorModel):
    DeviceMethods: List[DeviceMethodTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class InvokeDeviceMethodRequestRequestTypeDef(BaseValidatorModel):
    DeviceId: str
    DeviceMethod: Optional[DeviceMethodTypeDef] = None
    DeviceMethodParameters: Optional[str] = None

class ListDevicesRequestListDevicesPaginateTypeDef(BaseValidatorModel):
    DeviceType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeviceEventsRequestListDeviceEventsPaginateTypeDef(BaseValidatorModel):
    DeviceId: str
    FromTimeStamp: TimestampTypeDef
    ToTimeStamp: TimestampTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeviceEventsRequestRequestTypeDef(BaseValidatorModel):
    DeviceId: str
    FromTimeStamp: TimestampTypeDef
    ToTimeStamp: TimestampTypeDef
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListDeviceEventsResponseTypeDef(BaseValidatorModel):
    Events: List[DeviceEventTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef


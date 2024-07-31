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
from aws_resource_validator.pydantic_models.iot1click_devices_constants import *

class ClaimDevicesByClaimCodeRequestRequestTypeDef(BaseModel):
    ClaimCode: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DescribeDeviceRequestRequestTypeDef(BaseModel):
    DeviceId: str

class DeviceDescriptionTypeDef(BaseModel):
    Arn: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None
    DeviceId: Optional[str] = None
    Enabled: Optional[bool] = None
    RemainingLife: Optional[float] = None
    Type: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

class DeviceTypeDef(BaseModel):
    Attributes: Optional[Dict[str, Any]] = None
    DeviceId: Optional[str] = None
    Type: Optional[str] = None

class DeviceMethodTypeDef(BaseModel):
    DeviceType: Optional[str] = None
    MethodName: Optional[str] = None

class FinalizeDeviceClaimRequestRequestTypeDef(BaseModel):
    DeviceId: str
    Tags: Optional[Mapping[str, str]] = None

class GetDeviceMethodsRequestRequestTypeDef(BaseModel):
    DeviceId: str

class InitiateDeviceClaimRequestRequestTypeDef(BaseModel):
    DeviceId: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListDevicesRequestRequestTypeDef(BaseModel):
    DeviceType: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UnclaimDeviceRequestRequestTypeDef(BaseModel):
    DeviceId: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateDeviceStateRequestRequestTypeDef(BaseModel):
    DeviceId: str
    Enabled: Optional[bool] = None

class ClaimDevicesByClaimCodeResponseTypeDef(BaseModel):
    ClaimCode: str
    Total: int
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class FinalizeDeviceClaimResponseTypeDef(BaseModel):
    State: str
    ResponseMetadata: ResponseMetadataTypeDef

class InitiateDeviceClaimResponseTypeDef(BaseModel):
    State: str
    ResponseMetadata: ResponseMetadataTypeDef

class InvokeDeviceMethodResponseTypeDef(BaseModel):
    DeviceMethodResponse: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UnclaimDeviceResponseTypeDef(BaseModel):
    State: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDeviceResponseTypeDef(BaseModel):
    DeviceDescription: DeviceDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDevicesResponseTypeDef(BaseModel):
    Devices: List[DeviceDescriptionTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeviceEventTypeDef(BaseModel):
    Device: Optional[DeviceTypeDef] = None
    StdEvent: Optional[str] = None

class GetDeviceMethodsResponseTypeDef(BaseModel):
    DeviceMethods: List[DeviceMethodTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class InvokeDeviceMethodRequestRequestTypeDef(BaseModel):
    DeviceId: str
    DeviceMethod: Optional[DeviceMethodTypeDef] = None
    DeviceMethodParameters: Optional[str] = None

class ListDevicesRequestListDevicesPaginateTypeDef(BaseModel):
    DeviceType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeviceEventsRequestListDeviceEventsPaginateTypeDef(BaseModel):
    DeviceId: str
    FromTimeStamp: TimestampTypeDef
    ToTimeStamp: TimestampTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeviceEventsRequestRequestTypeDef(BaseModel):
    DeviceId: str
    FromTimeStamp: TimestampTypeDef
    ToTimeStamp: TimestampTypeDef
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListDeviceEventsResponseTypeDef(BaseModel):
    Events: List[DeviceEventTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef


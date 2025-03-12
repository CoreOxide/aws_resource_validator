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
from aws_resource_validator.pydantic_models.geo_maps_constants import *

class GetGlyphsRequestTypeDef(BaseValidatorModel):
    FontStack: str
    FontUnicodeRange: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class GetSpritesRequestTypeDef(BaseValidatorModel):
    FileName: str
    Style: MapStyleType
    ColorScheme: ColorSchemeType
    Variant: Literal["Default"]


class GetStaticMapRequestTypeDef(BaseValidatorModel):
    Height: int
    FileName: str
    Width: int
    BoundingBox: Optional[str] = None
    BoundedPositions: Optional[str] = None
    Center: Optional[str] = None
    CompactOverlay: Optional[str] = None
    GeoJsonOverlay: Optional[str] = None
    Key: Optional[str] = None
    Padding: Optional[int] = None
    Radius: Optional[int] = None
    ScaleBarUnit: Optional[ScaleBarUnitType] = None
    Style: Optional[Literal["Satellite"]] = None
    Zoom: Optional[float] = None


class GetStyleDescriptorRequestTypeDef(BaseValidatorModel):
    Style: MapStyleType
    ColorScheme: Optional[ColorSchemeType] = None
    PoliticalView: Optional[str] = None
    Key: Optional[str] = None


class GetTileRequestTypeDef(BaseValidatorModel):
    Tileset: str
    Z: str
    X: str
    Y: str
    Key: Optional[str] = None


class GetGlyphsResponseTypeDef(BaseValidatorModel):
    Blob: StreamingBody
    ContentType: str
    CacheControl: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetSpritesResponseTypeDef(BaseValidatorModel):
    Blob: StreamingBody
    ContentType: str
    CacheControl: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetStaticMapResponseTypeDef(BaseValidatorModel):
    Blob: StreamingBody
    ContentType: str
    CacheControl: str
    ETag: str
    PricingBucket: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetStyleDescriptorResponseTypeDef(BaseValidatorModel):
    Blob: StreamingBody
    ContentType: str
    CacheControl: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetTileResponseTypeDef(BaseValidatorModel):
    Blob: StreamingBody
    ContentType: str
    CacheControl: str
    ETag: str
    PricingBucket: str
    ResponseMetadata: ResponseMetadataTypeDef



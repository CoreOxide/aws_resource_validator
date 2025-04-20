from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.geo_maps.geo_maps_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class GetGlyphsRequest(BaseValidatorModel):
    FontStack: str
    FontUnicodeRange: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class GetSpritesRequest(BaseValidatorModel):
    FileName: str
    Style: MapStyleType
    ColorScheme: ColorSchemeType
    Variant: Literal['Default']


class GetStaticMapRequest(BaseValidatorModel):
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
    Style: Optional[Literal['Satellite']] = None
    Zoom: Optional[float] = None


class GetStyleDescriptorRequest(BaseValidatorModel):
    Style: MapStyleType
    ColorScheme: Optional[ColorSchemeType] = None
    PoliticalView: Optional[str] = None
    Key: Optional[str] = None


class GetTileRequest(BaseValidatorModel):
    Tileset: str
    Z: str
    X: str
    Y: str
    Key: Optional[str] = None


class GetGlyphsResponse(BaseValidatorModel):
    Blob: StreamingBody
    ContentType: str
    CacheControl: str
    ETag: str
    ResponseMetadata: ResponseMetadata


class GetSpritesResponse(BaseValidatorModel):
    Blob: StreamingBody
    ContentType: str
    CacheControl: str
    ETag: str
    ResponseMetadata: ResponseMetadata


class GetStaticMapResponse(BaseValidatorModel):
    Blob: StreamingBody
    ContentType: str
    CacheControl: str
    ETag: str
    PricingBucket: str
    ResponseMetadata: ResponseMetadata


class GetStyleDescriptorResponse(BaseValidatorModel):
    Blob: StreamingBody
    ContentType: str
    CacheControl: str
    ETag: str
    ResponseMetadata: ResponseMetadata


class GetTileResponse(BaseValidatorModel):
    Blob: StreamingBody
    ContentType: str
    CacheControl: str
    ETag: str
    PricingBucket: str
    ResponseMetadata: ResponseMetadata
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
from aws_resource_validator.pydantic_models.cloudsearchdomain_constants import *

class BucketTypeDef(BaseValidatorModel):
    value: Optional[str] = None
    count: Optional[int] = None

class DocumentServiceWarningTypeDef(BaseValidatorModel):
    message: Optional[str] = None

class FieldStatsTypeDef(BaseValidatorModel):
    min: Optional[str] = None
    max: Optional[str] = None
    count: Optional[int] = None
    missing: Optional[int] = None
    sum: Optional[float] = None
    sumOfSquares: Optional[float] = None
    mean: Optional[str] = None
    stddev: Optional[float] = None

class HitTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    fields: Optional[Dict[str, List[str]]] = None
    exprs: Optional[Dict[str, str]] = None
    highlights: Optional[Dict[str, str]] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class SearchRequestRequestTypeDef(BaseValidatorModel):
    query: str
    cursor: Optional[str] = None
    expr: Optional[str] = None
    facet: Optional[str] = None
    filterQuery: Optional[str] = None
    highlight: Optional[str] = None
    partial: Optional[bool] = None
    queryOptions: Optional[str] = None
    queryParser: Optional[QueryParserType] = None
    returnFields: Optional[str] = None
    size: Optional[int] = None
    sort: Optional[str] = None
    start: Optional[int] = None
    stats: Optional[str] = None

class SearchStatusTypeDef(BaseValidatorModel):
    timems: Optional[int] = None
    rid: Optional[str] = None

class SuggestionMatchTypeDef(BaseValidatorModel):
    suggestion: Optional[str] = None
    score: Optional[int] = None
    id: Optional[str] = None

class SuggestRequestRequestTypeDef(BaseValidatorModel):
    query: str
    suggester: str
    size: Optional[int] = None

class SuggestStatusTypeDef(BaseValidatorModel):
    timems: Optional[int] = None
    rid: Optional[str] = None

class UploadDocumentsRequestRequestTypeDef(BaseValidatorModel):
    documents: BlobTypeDef
    contentType: ContentTypeType

class BucketInfoTypeDef(BaseValidatorModel):
    buckets: Optional[List[BucketTypeDef]] = None

class HitsTypeDef(BaseValidatorModel):
    found: Optional[int] = None
    start: Optional[int] = None
    cursor: Optional[str] = None
    hit: Optional[List[HitTypeDef]] = None

class UploadDocumentsResponseTypeDef(BaseValidatorModel):
    status: str
    adds: int
    deletes: int
    warnings: List[DocumentServiceWarningTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SuggestModelTypeDef(BaseValidatorModel):
    query: Optional[str] = None
    found: Optional[int] = None
    suggestions: Optional[List[SuggestionMatchTypeDef]] = None

class SearchResponseTypeDef(BaseValidatorModel):
    status: SearchStatusTypeDef
    hits: HitsTypeDef
    facets: Dict[str, BucketInfoTypeDef]
    stats: Dict[str, FieldStatsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SuggestResponseTypeDef(BaseValidatorModel):
    status: SuggestStatusTypeDef
    suggest: SuggestModelTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


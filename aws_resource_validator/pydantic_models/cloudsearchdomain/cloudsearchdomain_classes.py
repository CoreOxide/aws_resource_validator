from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.cloudsearchdomain.cloudsearchdomain_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream



Blob = Union[str, bytes, IO[Any], StreamingBody]


class Bucket(BaseValidatorModel):
    value: Optional[str] = None
    count: Optional[int] = None


class DocumentServiceWarning(BaseValidatorModel):
    message: Optional[str] = None


class FieldStats(BaseValidatorModel):
    min: Optional[str] = None
    max: Optional[str] = None
    count: Optional[int] = None
    missing: Optional[int] = None
    sum: Optional[float] = None
    sumOfSquares: Optional[float] = None
    mean: Optional[str] = None
    stddev: Optional[float] = None


class Hit(BaseValidatorModel):
    id: Optional[str] = None
    fields: Optional[Dict[str, List[str]]] = None
    exprs: Optional[Dict[str, str]] = None
    highlights: Optional[Dict[str, str]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class SearchRequest(BaseValidatorModel):
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


class SearchStatus(BaseValidatorModel):
    timems: Optional[int] = None
    rid: Optional[str] = None


class SuggestionMatch(BaseValidatorModel):
    suggestion: Optional[str] = None
    score: Optional[int] = None
    id: Optional[str] = None


class SuggestRequest(BaseValidatorModel):
    query: str
    suggester: str
    size: Optional[int] = None


class SuggestStatus(BaseValidatorModel):
    timems: Optional[int] = None
    rid: Optional[str] = None


class UploadDocumentsRequest(BaseValidatorModel):
    documents: Blob
    contentType: ContentTypeType


class BucketInfo(BaseValidatorModel):
    buckets: Optional[List[Bucket]] = None


class Hits(BaseValidatorModel):
    found: Optional[int] = None
    start: Optional[int] = None
    cursor: Optional[str] = None
    hit: Optional[List[Hit]] = None


class UploadDocumentsResponse(BaseValidatorModel):
    status: str
    adds: int
    deletes: int
    warnings: List[DocumentServiceWarning]
    ResponseMetadata: ResponseMetadata


class SuggestModel(BaseValidatorModel):
    query: Optional[str] = None
    found: Optional[int] = None
    suggestions: Optional[List[SuggestionMatch]] = None


class SearchResponse(BaseValidatorModel):
    status: SearchStatus
    hits: Hits
    facets: Dict[str, BucketInfo]
    stats: Dict[str, FieldStats]
    ResponseMetadata: ResponseMetadata


class SuggestResponse(BaseValidatorModel):
    status: SuggestStatus
    suggest: SuggestModel
    ResponseMetadata: ResponseMetadata
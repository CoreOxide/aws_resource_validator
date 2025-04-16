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
from aws_resource_validator.pydantic_models.cloudsearchdomain_constants import *

class Bucket(BaseValidatorModel):
    value: Optional[str] = None
    count: Optional[int] = None


class DocumentServiceWarning(BaseValidatorModel):
    message: Optional[str] = None


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


class SuggestRequest(BaseValidatorModel):
    query: str
    suggester: str
    size: Optional[int] = None


class SuggestStatus(BaseValidatorModel):
    timems: Optional[int] = None
    rid: Optional[str] = None


class Blob(BaseValidatorModel):
    pass


class UploadDocumentsRequest(BaseValidatorModel):
    documents: Blob
    contentType: ContentTypeType


class BucketInfo(BaseValidatorModel):
    buckets: Optional[List[Bucket]] = None


class Hit(BaseValidatorModel):
    pass


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


class SuggestionMatch(BaseValidatorModel):
    pass


class SuggestModel(BaseValidatorModel):
    query: Optional[str] = None
    found: Optional[int] = None
    suggestions: Optional[List[SuggestionMatch]] = None


class FieldStats(BaseValidatorModel):
    pass


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



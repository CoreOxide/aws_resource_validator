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
from aws_resource_validator.pydantic_models.cloudsearch_constants import *

class OptionStatus(BaseValidatorModel):
    CreationDate: datetime
    UpdateDate: datetime
    State: OptionStateType
    UpdateVersion: Optional[int] = None
    PendingDeletion: Optional[bool] = None


class AnalysisOptions(BaseValidatorModel):
    Synonyms: Optional[str] = None
    Stopwords: Optional[str] = None
    StemmingDictionary: Optional[str] = None
    JapaneseTokenizationDictionary: Optional[str] = None
    AlgorithmicStemming: Optional[AlgorithmicStemmingType] = None


class BuildSuggestersRequest(BaseValidatorModel):
    DomainName: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateDomainRequest(BaseValidatorModel):
    DomainName: str


class DateArrayOptions(BaseValidatorModel):
    DefaultValue: Optional[str] = None
    SourceFields: Optional[str] = None
    FacetEnabled: Optional[bool] = None
    SearchEnabled: Optional[bool] = None
    ReturnEnabled: Optional[bool] = None


class DateOptions(BaseValidatorModel):
    DefaultValue: Optional[str] = None
    SourceField: Optional[str] = None
    FacetEnabled: Optional[bool] = None
    SearchEnabled: Optional[bool] = None
    ReturnEnabled: Optional[bool] = None
    SortEnabled: Optional[bool] = None


class Expression(BaseValidatorModel):
    ExpressionName: str
    ExpressionValue: str


class DeleteAnalysisSchemeRequest(BaseValidatorModel):
    DomainName: str
    AnalysisSchemeName: str


class DeleteDomainRequest(BaseValidatorModel):
    DomainName: str


class DeleteExpressionRequest(BaseValidatorModel):
    DomainName: str
    ExpressionName: str


class DeleteIndexFieldRequest(BaseValidatorModel):
    DomainName: str
    IndexFieldName: str


class DeleteSuggesterRequest(BaseValidatorModel):
    DomainName: str
    SuggesterName: str


class DescribeAnalysisSchemesRequest(BaseValidatorModel):
    DomainName: str
    AnalysisSchemeNames: Optional[Sequence[str]] = None
    Deployed: Optional[bool] = None


class DescribeAvailabilityOptionsRequest(BaseValidatorModel):
    DomainName: str
    Deployed: Optional[bool] = None


class DescribeDomainEndpointOptionsRequest(BaseValidatorModel):
    DomainName: str
    Deployed: Optional[bool] = None


class DescribeDomainsRequest(BaseValidatorModel):
    DomainNames: Optional[Sequence[str]] = None


class DescribeExpressionsRequest(BaseValidatorModel):
    DomainName: str
    ExpressionNames: Optional[Sequence[str]] = None
    Deployed: Optional[bool] = None


class DescribeIndexFieldsRequest(BaseValidatorModel):
    DomainName: str
    FieldNames: Optional[Sequence[str]] = None
    Deployed: Optional[bool] = None


class DescribeScalingParametersRequest(BaseValidatorModel):
    DomainName: str


class DescribeServiceAccessPoliciesRequest(BaseValidatorModel):
    DomainName: str
    Deployed: Optional[bool] = None


class DescribeSuggestersRequest(BaseValidatorModel):
    DomainName: str
    SuggesterNames: Optional[Sequence[str]] = None
    Deployed: Optional[bool] = None


class DocumentSuggesterOptions(BaseValidatorModel):
    SourceField: str
    FuzzyMatching: Optional[SuggesterFuzzyMatchingType] = None
    SortExpression: Optional[str] = None


class DomainEndpointOptions(BaseValidatorModel):
    EnforceHTTPS: Optional[bool] = None
    TLSSecurityPolicy: Optional[TLSSecurityPolicyType] = None


class Limits(BaseValidatorModel):
    MaximumReplicationCount: int
    MaximumPartitionCount: int


class ServiceEndpoint(BaseValidatorModel):
    Endpoint: Optional[str] = None


class DoubleArrayOptions(BaseValidatorModel):
    DefaultValue: Optional[float] = None
    SourceFields: Optional[str] = None
    FacetEnabled: Optional[bool] = None
    SearchEnabled: Optional[bool] = None
    ReturnEnabled: Optional[bool] = None


class DoubleOptions(BaseValidatorModel):
    DefaultValue: Optional[float] = None
    SourceField: Optional[str] = None
    FacetEnabled: Optional[bool] = None
    SearchEnabled: Optional[bool] = None
    ReturnEnabled: Optional[bool] = None
    SortEnabled: Optional[bool] = None


class IndexDocumentsRequest(BaseValidatorModel):
    DomainName: str


class IntArrayOptions(BaseValidatorModel):
    DefaultValue: Optional[int] = None
    SourceFields: Optional[str] = None
    FacetEnabled: Optional[bool] = None
    SearchEnabled: Optional[bool] = None
    ReturnEnabled: Optional[bool] = None


class IntOptions(BaseValidatorModel):
    DefaultValue: Optional[int] = None
    SourceField: Optional[str] = None
    FacetEnabled: Optional[bool] = None
    SearchEnabled: Optional[bool] = None
    ReturnEnabled: Optional[bool] = None
    SortEnabled: Optional[bool] = None


class LatLonOptions(BaseValidatorModel):
    DefaultValue: Optional[str] = None
    SourceField: Optional[str] = None
    FacetEnabled: Optional[bool] = None
    SearchEnabled: Optional[bool] = None
    ReturnEnabled: Optional[bool] = None
    SortEnabled: Optional[bool] = None


class LiteralArrayOptions(BaseValidatorModel):
    DefaultValue: Optional[str] = None
    SourceFields: Optional[str] = None
    FacetEnabled: Optional[bool] = None
    SearchEnabled: Optional[bool] = None
    ReturnEnabled: Optional[bool] = None


class LiteralOptions(BaseValidatorModel):
    DefaultValue: Optional[str] = None
    SourceField: Optional[str] = None
    FacetEnabled: Optional[bool] = None
    SearchEnabled: Optional[bool] = None
    ReturnEnabled: Optional[bool] = None
    SortEnabled: Optional[bool] = None


class TextArrayOptions(BaseValidatorModel):
    DefaultValue: Optional[str] = None
    SourceFields: Optional[str] = None
    ReturnEnabled: Optional[bool] = None
    HighlightEnabled: Optional[bool] = None
    AnalysisScheme: Optional[str] = None


class TextOptions(BaseValidatorModel):
    DefaultValue: Optional[str] = None
    SourceField: Optional[str] = None
    ReturnEnabled: Optional[bool] = None
    SortEnabled: Optional[bool] = None
    HighlightEnabled: Optional[bool] = None
    AnalysisScheme: Optional[str] = None


class ScalingParameters(BaseValidatorModel):
    DesiredInstanceType: Optional[PartitionInstanceTypeType] = None
    DesiredReplicationCount: Optional[int] = None
    DesiredPartitionCount: Optional[int] = None


class UpdateAvailabilityOptionsRequest(BaseValidatorModel):
    DomainName: str
    MultiAZ: bool


class UpdateServiceAccessPoliciesRequest(BaseValidatorModel):
    DomainName: str
    AccessPolicies: str


class AccessPoliciesStatus(BaseValidatorModel):
    Options: str
    Status: OptionStatus


class AvailabilityOptionsStatus(BaseValidatorModel):
    Options: bool
    Status: OptionStatus


class AnalysisScheme(BaseValidatorModel):
    AnalysisSchemeName: str
    AnalysisSchemeLanguage: AnalysisSchemeLanguageType
    AnalysisOptions: Optional[AnalysisOptions] = None


class BuildSuggestersResponse(BaseValidatorModel):
    FieldNames: List[str]
    ResponseMetadata: ResponseMetadata


class IndexDocumentsResponse(BaseValidatorModel):
    FieldNames: List[str]
    ResponseMetadata: ResponseMetadata


class ListDomainNamesResponse(BaseValidatorModel):
    DomainNames: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class DefineExpressionRequest(BaseValidatorModel):
    DomainName: str
    Expression: Expression


class ExpressionStatus(BaseValidatorModel):
    Options: Expression
    Status: OptionStatus


class Suggester(BaseValidatorModel):
    SuggesterName: str
    DocumentSuggesterOptions: DocumentSuggesterOptions


class DomainEndpointOptionsStatus(BaseValidatorModel):
    Options: DomainEndpointOptions
    Status: OptionStatus


class UpdateDomainEndpointOptionsRequest(BaseValidatorModel):
    DomainName: str
    DomainEndpointOptions: DomainEndpointOptions


class DomainStatus(BaseValidatorModel):
    DomainId: str
    DomainName: str
    RequiresIndexDocuments: bool
    ARN: Optional[str] = None
    Created: Optional[bool] = None
    Deleted: Optional[bool] = None
    DocService: Optional[ServiceEndpoint] = None
    SearchService: Optional[ServiceEndpoint] = None
    Processing: Optional[bool] = None
    SearchInstanceType: Optional[str] = None
    SearchPartitionCount: Optional[int] = None
    SearchInstanceCount: Optional[int] = None
    Limits: Optional[Limits] = None


class IndexField(BaseValidatorModel):
    IndexFieldName: str
    IndexFieldType: IndexFieldTypeType
    IntOptions: Optional[IntOptions] = None
    DoubleOptions: Optional[DoubleOptions] = None
    LiteralOptions: Optional[LiteralOptions] = None
    TextOptions: Optional[TextOptions] = None
    DateOptions: Optional[DateOptions] = None
    LatLonOptions: Optional[LatLonOptions] = None
    IntArrayOptions: Optional[IntArrayOptions] = None
    DoubleArrayOptions: Optional[DoubleArrayOptions] = None
    LiteralArrayOptions: Optional[LiteralArrayOptions] = None
    TextArrayOptions: Optional[TextArrayOptions] = None
    DateArrayOptions: Optional[DateArrayOptions] = None


class ScalingParametersStatus(BaseValidatorModel):
    Options: ScalingParameters
    Status: OptionStatus


class UpdateScalingParametersRequest(BaseValidatorModel):
    DomainName: str
    ScalingParameters: ScalingParameters


class DescribeServiceAccessPoliciesResponse(BaseValidatorModel):
    AccessPolicies: AccessPoliciesStatus
    ResponseMetadata: ResponseMetadata


class UpdateServiceAccessPoliciesResponse(BaseValidatorModel):
    AccessPolicies: AccessPoliciesStatus
    ResponseMetadata: ResponseMetadata


class DescribeAvailabilityOptionsResponse(BaseValidatorModel):
    AvailabilityOptions: AvailabilityOptionsStatus
    ResponseMetadata: ResponseMetadata


class UpdateAvailabilityOptionsResponse(BaseValidatorModel):
    AvailabilityOptions: AvailabilityOptionsStatus
    ResponseMetadata: ResponseMetadata


class AnalysisSchemeStatus(BaseValidatorModel):
    Options: AnalysisScheme
    Status: OptionStatus


class DefineAnalysisSchemeRequest(BaseValidatorModel):
    DomainName: str
    AnalysisScheme: AnalysisScheme


class DefineExpressionResponse(BaseValidatorModel):
    Expression: ExpressionStatus
    ResponseMetadata: ResponseMetadata


class DeleteExpressionResponse(BaseValidatorModel):
    Expression: ExpressionStatus
    ResponseMetadata: ResponseMetadata


class DescribeExpressionsResponse(BaseValidatorModel):
    Expressions: List[ExpressionStatus]
    ResponseMetadata: ResponseMetadata


class DefineSuggesterRequest(BaseValidatorModel):
    DomainName: str
    Suggester: Suggester


class SuggesterStatus(BaseValidatorModel):
    Options: Suggester
    Status: OptionStatus


class DescribeDomainEndpointOptionsResponse(BaseValidatorModel):
    DomainEndpointOptions: DomainEndpointOptionsStatus
    ResponseMetadata: ResponseMetadata


class UpdateDomainEndpointOptionsResponse(BaseValidatorModel):
    DomainEndpointOptions: DomainEndpointOptionsStatus
    ResponseMetadata: ResponseMetadata


class CreateDomainResponse(BaseValidatorModel):
    DomainStatus: DomainStatus
    ResponseMetadata: ResponseMetadata


class DeleteDomainResponse(BaseValidatorModel):
    DomainStatus: DomainStatus
    ResponseMetadata: ResponseMetadata


class DescribeDomainsResponse(BaseValidatorModel):
    DomainStatusList: List[DomainStatus]
    ResponseMetadata: ResponseMetadata


class DefineIndexFieldRequest(BaseValidatorModel):
    DomainName: str
    IndexField: IndexField


class IndexFieldStatus(BaseValidatorModel):
    Options: IndexField
    Status: OptionStatus


class DescribeScalingParametersResponse(BaseValidatorModel):
    ScalingParameters: ScalingParametersStatus
    ResponseMetadata: ResponseMetadata


class UpdateScalingParametersResponse(BaseValidatorModel):
    ScalingParameters: ScalingParametersStatus
    ResponseMetadata: ResponseMetadata


class DefineAnalysisSchemeResponse(BaseValidatorModel):
    AnalysisScheme: AnalysisSchemeStatus
    ResponseMetadata: ResponseMetadata


class DeleteAnalysisSchemeResponse(BaseValidatorModel):
    AnalysisScheme: AnalysisSchemeStatus
    ResponseMetadata: ResponseMetadata


class DescribeAnalysisSchemesResponse(BaseValidatorModel):
    AnalysisSchemes: List[AnalysisSchemeStatus]
    ResponseMetadata: ResponseMetadata


class DefineSuggesterResponse(BaseValidatorModel):
    Suggester: SuggesterStatus
    ResponseMetadata: ResponseMetadata


class DeleteSuggesterResponse(BaseValidatorModel):
    Suggester: SuggesterStatus
    ResponseMetadata: ResponseMetadata


class DescribeSuggestersResponse(BaseValidatorModel):
    Suggesters: List[SuggesterStatus]
    ResponseMetadata: ResponseMetadata


class DefineIndexFieldResponse(BaseValidatorModel):
    IndexField: IndexFieldStatus
    ResponseMetadata: ResponseMetadata


class DeleteIndexFieldResponse(BaseValidatorModel):
    IndexField: IndexFieldStatus
    ResponseMetadata: ResponseMetadata


class DescribeIndexFieldsResponse(BaseValidatorModel):
    IndexFields: List[IndexFieldStatus]
    ResponseMetadata: ResponseMetadata



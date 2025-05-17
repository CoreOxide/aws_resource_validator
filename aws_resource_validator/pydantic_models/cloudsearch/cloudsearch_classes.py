from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




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


# This class is the input for the 'build_suggesters' function.
class BuildSuggestersRequest(BaseValidatorModel):
    DomainName: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'create_domain' function.
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


# This class is the input for the 'delete_analysis_scheme' function.
class DeleteAnalysisSchemeRequest(BaseValidatorModel):
    DomainName: str
    AnalysisSchemeName: str


# This class is the input for the 'delete_domain' function.
class DeleteDomainRequest(BaseValidatorModel):
    DomainName: str


# This class is the input for the 'delete_expression' function.
class DeleteExpressionRequest(BaseValidatorModel):
    DomainName: str
    ExpressionName: str


# This class is the input for the 'delete_index_field' function.
class DeleteIndexFieldRequest(BaseValidatorModel):
    DomainName: str
    IndexFieldName: str


# This class is the input for the 'delete_suggester' function.
class DeleteSuggesterRequest(BaseValidatorModel):
    DomainName: str
    SuggesterName: str


# This class is the input for the 'describe_analysis_schemes' function.
class DescribeAnalysisSchemesRequest(BaseValidatorModel):
    DomainName: str
    AnalysisSchemeNames: Optional[List[str]] = None
    Deployed: Optional[bool] = None


# This class is the input for the 'describe_availability_options' function.
class DescribeAvailabilityOptionsRequest(BaseValidatorModel):
    DomainName: str
    Deployed: Optional[bool] = None


# This class is the input for the 'describe_domain_endpoint_options' function.
class DescribeDomainEndpointOptionsRequest(BaseValidatorModel):
    DomainName: str
    Deployed: Optional[bool] = None


# This class is the input for the 'describe_domains' function.
class DescribeDomainsRequest(BaseValidatorModel):
    DomainNames: Optional[List[str]] = None


# This class is the input for the 'describe_expressions' function.
class DescribeExpressionsRequest(BaseValidatorModel):
    DomainName: str
    ExpressionNames: Optional[List[str]] = None
    Deployed: Optional[bool] = None


# This class is the input for the 'describe_index_fields' function.
class DescribeIndexFieldsRequest(BaseValidatorModel):
    DomainName: str
    FieldNames: Optional[List[str]] = None
    Deployed: Optional[bool] = None


# This class is the input for the 'describe_scaling_parameters' function.
class DescribeScalingParametersRequest(BaseValidatorModel):
    DomainName: str


# This class is the input for the 'describe_service_access_policies' function.
class DescribeServiceAccessPoliciesRequest(BaseValidatorModel):
    DomainName: str
    Deployed: Optional[bool] = None


# This class is the input for the 'describe_suggesters' function.
class DescribeSuggestersRequest(BaseValidatorModel):
    DomainName: str
    SuggesterNames: Optional[List[str]] = None
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


# This class is the input for the 'index_documents' function.
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


# This class is the input for the 'update_availability_options' function.
class UpdateAvailabilityOptionsRequest(BaseValidatorModel):
    DomainName: str
    MultiAZ: bool


# This class is the input for the 'update_service_access_policies' function.
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


# This class is the output for the 'build_suggesters' function.
class BuildSuggestersResponse(BaseValidatorModel):
    FieldNames: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'index_documents' function.
class IndexDocumentsResponse(BaseValidatorModel):
    FieldNames: List[str]
    ResponseMetadata: ResponseMetadata


class ListDomainNamesResponse(BaseValidatorModel):
    DomainNames: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'define_expression' function.
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


# This class is the input for the 'update_domain_endpoint_options' function.
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


# This class is the input for the 'update_scaling_parameters' function.
class UpdateScalingParametersRequest(BaseValidatorModel):
    DomainName: str
    ScalingParameters: ScalingParameters


# This class is the output for the 'describe_service_access_policies' function.
class DescribeServiceAccessPoliciesResponse(BaseValidatorModel):
    AccessPolicies: AccessPoliciesStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_service_access_policies' function.
class UpdateServiceAccessPoliciesResponse(BaseValidatorModel):
    AccessPolicies: AccessPoliciesStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_availability_options' function.
class DescribeAvailabilityOptionsResponse(BaseValidatorModel):
    AvailabilityOptions: AvailabilityOptionsStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_availability_options' function.
class UpdateAvailabilityOptionsResponse(BaseValidatorModel):
    AvailabilityOptions: AvailabilityOptionsStatus
    ResponseMetadata: ResponseMetadata


class AnalysisSchemeStatus(BaseValidatorModel):
    Options: AnalysisScheme
    Status: OptionStatus


# This class is the input for the 'define_analysis_scheme' function.
class DefineAnalysisSchemeRequest(BaseValidatorModel):
    DomainName: str
    AnalysisScheme: AnalysisScheme


# This class is the output for the 'define_expression' function.
class DefineExpressionResponse(BaseValidatorModel):
    Expression: ExpressionStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_expression' function.
class DeleteExpressionResponse(BaseValidatorModel):
    Expression: ExpressionStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_expressions' function.
class DescribeExpressionsResponse(BaseValidatorModel):
    Expressions: List[ExpressionStatus]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'define_suggester' function.
class DefineSuggesterRequest(BaseValidatorModel):
    DomainName: str
    Suggester: Suggester


class SuggesterStatus(BaseValidatorModel):
    Options: Suggester
    Status: OptionStatus


# This class is the output for the 'describe_domain_endpoint_options' function.
class DescribeDomainEndpointOptionsResponse(BaseValidatorModel):
    DomainEndpointOptions: DomainEndpointOptionsStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_domain_endpoint_options' function.
class UpdateDomainEndpointOptionsResponse(BaseValidatorModel):
    DomainEndpointOptions: DomainEndpointOptionsStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_domain' function.
class CreateDomainResponse(BaseValidatorModel):
    DomainStatus: DomainStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_domain' function.
class DeleteDomainResponse(BaseValidatorModel):
    DomainStatus: DomainStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_domains' function.
class DescribeDomainsResponse(BaseValidatorModel):
    DomainStatusList: List[DomainStatus]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'define_index_field' function.
class DefineIndexFieldRequest(BaseValidatorModel):
    DomainName: str
    IndexField: IndexField


class IndexFieldStatus(BaseValidatorModel):
    Options: IndexField
    Status: OptionStatus


# This class is the output for the 'describe_scaling_parameters' function.
class DescribeScalingParametersResponse(BaseValidatorModel):
    ScalingParameters: ScalingParametersStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_scaling_parameters' function.
class UpdateScalingParametersResponse(BaseValidatorModel):
    ScalingParameters: ScalingParametersStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'define_analysis_scheme' function.
class DefineAnalysisSchemeResponse(BaseValidatorModel):
    AnalysisScheme: AnalysisSchemeStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_analysis_scheme' function.
class DeleteAnalysisSchemeResponse(BaseValidatorModel):
    AnalysisScheme: AnalysisSchemeStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_analysis_schemes' function.
class DescribeAnalysisSchemesResponse(BaseValidatorModel):
    AnalysisSchemes: List[AnalysisSchemeStatus]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'define_suggester' function.
class DefineSuggesterResponse(BaseValidatorModel):
    Suggester: SuggesterStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_suggester' function.
class DeleteSuggesterResponse(BaseValidatorModel):
    Suggester: SuggesterStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_suggesters' function.
class DescribeSuggestersResponse(BaseValidatorModel):
    Suggesters: List[SuggesterStatus]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'define_index_field' function.
class DefineIndexFieldResponse(BaseValidatorModel):
    IndexField: IndexFieldStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_index_field' function.
class DeleteIndexFieldResponse(BaseValidatorModel):
    IndexField: IndexFieldStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_index_fields' function.
class DescribeIndexFieldsResponse(BaseValidatorModel):
    IndexFields: List[IndexFieldStatus]
    ResponseMetadata: ResponseMetadata
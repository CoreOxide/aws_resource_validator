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
from aws_resource_validator.pydantic_models.cloudsearch_constants import *

class OptionStatusTypeDef(BaseValidatorModel):
    CreationDate: datetime
    UpdateDate: datetime
    State: OptionStateType
    UpdateVersion: Optional[int] = None
    PendingDeletion: Optional[bool] = None

class AnalysisOptionsTypeDef(BaseValidatorModel):
    Synonyms: Optional[str] = None
    Stopwords: Optional[str] = None
    StemmingDictionary: Optional[str] = None
    JapaneseTokenizationDictionary: Optional[str] = None
    AlgorithmicStemming: Optional[AlgorithmicStemmingType] = None

class BuildSuggestersRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateDomainRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str

class DateArrayOptionsTypeDef(BaseValidatorModel):
    DefaultValue: Optional[str] = None
    SourceFields: Optional[str] = None
    FacetEnabled: Optional[bool] = None
    SearchEnabled: Optional[bool] = None
    ReturnEnabled: Optional[bool] = None

class DateOptionsTypeDef(BaseValidatorModel):
    DefaultValue: Optional[str] = None
    SourceField: Optional[str] = None
    FacetEnabled: Optional[bool] = None
    SearchEnabled: Optional[bool] = None
    ReturnEnabled: Optional[bool] = None
    SortEnabled: Optional[bool] = None

class ExpressionTypeDef(BaseValidatorModel):
    ExpressionName: str
    ExpressionValue: str

class DeleteAnalysisSchemeRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    AnalysisSchemeName: str

class DeleteDomainRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str

class DeleteExpressionRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    ExpressionName: str

class DeleteIndexFieldRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    IndexFieldName: str

class DeleteSuggesterRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    SuggesterName: str

class DescribeAnalysisSchemesRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    AnalysisSchemeNames: Optional[Sequence[str]] = None
    Deployed: Optional[bool] = None

class DescribeAvailabilityOptionsRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    Deployed: Optional[bool] = None

class DescribeDomainEndpointOptionsRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    Deployed: Optional[bool] = None

class DescribeDomainsRequestRequestTypeDef(BaseValidatorModel):
    DomainNames: Optional[Sequence[str]] = None

class DescribeExpressionsRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    ExpressionNames: Optional[Sequence[str]] = None
    Deployed: Optional[bool] = None

class DescribeIndexFieldsRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    FieldNames: Optional[Sequence[str]] = None
    Deployed: Optional[bool] = None

class DescribeScalingParametersRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str

class DescribeServiceAccessPoliciesRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    Deployed: Optional[bool] = None

class DescribeSuggestersRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    SuggesterNames: Optional[Sequence[str]] = None
    Deployed: Optional[bool] = None

class DocumentSuggesterOptionsTypeDef(BaseValidatorModel):
    SourceField: str
    FuzzyMatching: Optional[SuggesterFuzzyMatchingType] = None
    SortExpression: Optional[str] = None

class DomainEndpointOptionsTypeDef(BaseValidatorModel):
    EnforceHTTPS: Optional[bool] = None
    TLSSecurityPolicy: Optional[TLSSecurityPolicyType] = None

class LimitsTypeDef(BaseValidatorModel):
    MaximumReplicationCount: int
    MaximumPartitionCount: int

class ServiceEndpointTypeDef(BaseValidatorModel):
    Endpoint: Optional[str] = None

class DoubleArrayOptionsTypeDef(BaseValidatorModel):
    DefaultValue: Optional[float] = None
    SourceFields: Optional[str] = None
    FacetEnabled: Optional[bool] = None
    SearchEnabled: Optional[bool] = None
    ReturnEnabled: Optional[bool] = None

class DoubleOptionsTypeDef(BaseValidatorModel):
    DefaultValue: Optional[float] = None
    SourceField: Optional[str] = None
    FacetEnabled: Optional[bool] = None
    SearchEnabled: Optional[bool] = None
    ReturnEnabled: Optional[bool] = None
    SortEnabled: Optional[bool] = None

class IndexDocumentsRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str

class IntArrayOptionsTypeDef(BaseValidatorModel):
    DefaultValue: Optional[int] = None
    SourceFields: Optional[str] = None
    FacetEnabled: Optional[bool] = None
    SearchEnabled: Optional[bool] = None
    ReturnEnabled: Optional[bool] = None

class IntOptionsTypeDef(BaseValidatorModel):
    DefaultValue: Optional[int] = None
    SourceField: Optional[str] = None
    FacetEnabled: Optional[bool] = None
    SearchEnabled: Optional[bool] = None
    ReturnEnabled: Optional[bool] = None
    SortEnabled: Optional[bool] = None

class LatLonOptionsTypeDef(BaseValidatorModel):
    DefaultValue: Optional[str] = None
    SourceField: Optional[str] = None
    FacetEnabled: Optional[bool] = None
    SearchEnabled: Optional[bool] = None
    ReturnEnabled: Optional[bool] = None
    SortEnabled: Optional[bool] = None

class LiteralArrayOptionsTypeDef(BaseValidatorModel):
    DefaultValue: Optional[str] = None
    SourceFields: Optional[str] = None
    FacetEnabled: Optional[bool] = None
    SearchEnabled: Optional[bool] = None
    ReturnEnabled: Optional[bool] = None

class LiteralOptionsTypeDef(BaseValidatorModel):
    DefaultValue: Optional[str] = None
    SourceField: Optional[str] = None
    FacetEnabled: Optional[bool] = None
    SearchEnabled: Optional[bool] = None
    ReturnEnabled: Optional[bool] = None
    SortEnabled: Optional[bool] = None

class TextArrayOptionsTypeDef(BaseValidatorModel):
    DefaultValue: Optional[str] = None
    SourceFields: Optional[str] = None
    ReturnEnabled: Optional[bool] = None
    HighlightEnabled: Optional[bool] = None
    AnalysisScheme: Optional[str] = None

class TextOptionsTypeDef(BaseValidatorModel):
    DefaultValue: Optional[str] = None
    SourceField: Optional[str] = None
    ReturnEnabled: Optional[bool] = None
    SortEnabled: Optional[bool] = None
    HighlightEnabled: Optional[bool] = None
    AnalysisScheme: Optional[str] = None

class ScalingParametersTypeDef(BaseValidatorModel):
    DesiredInstanceType: Optional[PartitionInstanceTypeType] = None
    DesiredReplicationCount: Optional[int] = None
    DesiredPartitionCount: Optional[int] = None

class UpdateAvailabilityOptionsRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    MultiAZ: bool

class UpdateServiceAccessPoliciesRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    AccessPolicies: str

class AccessPoliciesStatusTypeDef(BaseValidatorModel):
    Options: str
    Status: OptionStatusTypeDef

class AvailabilityOptionsStatusTypeDef(BaseValidatorModel):
    Options: bool
    Status: OptionStatusTypeDef

class AnalysisSchemeTypeDef(BaseValidatorModel):
    AnalysisSchemeName: str
    AnalysisSchemeLanguage: AnalysisSchemeLanguageType
    AnalysisOptions: Optional[AnalysisOptionsTypeDef] = None

class BuildSuggestersResponseTypeDef(BaseValidatorModel):
    FieldNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class IndexDocumentsResponseTypeDef(BaseValidatorModel):
    FieldNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDomainNamesResponseTypeDef(BaseValidatorModel):
    DomainNames: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DefineExpressionRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    Expression: ExpressionTypeDef

class ExpressionStatusTypeDef(BaseValidatorModel):
    Options: ExpressionTypeDef
    Status: OptionStatusTypeDef

class SuggesterTypeDef(BaseValidatorModel):
    SuggesterName: str
    DocumentSuggesterOptions: DocumentSuggesterOptionsTypeDef

class DomainEndpointOptionsStatusTypeDef(BaseValidatorModel):
    Options: DomainEndpointOptionsTypeDef
    Status: OptionStatusTypeDef

class UpdateDomainEndpointOptionsRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    DomainEndpointOptions: DomainEndpointOptionsTypeDef

class DomainStatusTypeDef(BaseValidatorModel):
    DomainId: str
    DomainName: str
    RequiresIndexDocuments: bool
    ARN: Optional[str] = None
    Created: Optional[bool] = None
    Deleted: Optional[bool] = None
    DocService: Optional[ServiceEndpointTypeDef] = None
    SearchService: Optional[ServiceEndpointTypeDef] = None
    Processing: Optional[bool] = None
    SearchInstanceType: Optional[str] = None
    SearchPartitionCount: Optional[int] = None
    SearchInstanceCount: Optional[int] = None
    Limits: Optional[LimitsTypeDef] = None

class IndexFieldTypeDef(BaseValidatorModel):
    IndexFieldName: str
    IndexFieldType: IndexFieldTypeType
    IntOptions: Optional[IntOptionsTypeDef] = None
    DoubleOptions: Optional[DoubleOptionsTypeDef] = None
    LiteralOptions: Optional[LiteralOptionsTypeDef] = None
    TextOptions: Optional[TextOptionsTypeDef] = None
    DateOptions: Optional[DateOptionsTypeDef] = None
    LatLonOptions: Optional[LatLonOptionsTypeDef] = None
    IntArrayOptions: Optional[IntArrayOptionsTypeDef] = None
    DoubleArrayOptions: Optional[DoubleArrayOptionsTypeDef] = None
    LiteralArrayOptions: Optional[LiteralArrayOptionsTypeDef] = None
    TextArrayOptions: Optional[TextArrayOptionsTypeDef] = None
    DateArrayOptions: Optional[DateArrayOptionsTypeDef] = None

class ScalingParametersStatusTypeDef(BaseValidatorModel):
    Options: ScalingParametersTypeDef
    Status: OptionStatusTypeDef

class UpdateScalingParametersRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    ScalingParameters: ScalingParametersTypeDef

class DescribeServiceAccessPoliciesResponseTypeDef(BaseValidatorModel):
    AccessPolicies: AccessPoliciesStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceAccessPoliciesResponseTypeDef(BaseValidatorModel):
    AccessPolicies: AccessPoliciesStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAvailabilityOptionsResponseTypeDef(BaseValidatorModel):
    AvailabilityOptions: AvailabilityOptionsStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAvailabilityOptionsResponseTypeDef(BaseValidatorModel):
    AvailabilityOptions: AvailabilityOptionsStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AnalysisSchemeStatusTypeDef(BaseValidatorModel):
    Options: AnalysisSchemeTypeDef
    Status: OptionStatusTypeDef

class DefineAnalysisSchemeRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    AnalysisScheme: AnalysisSchemeTypeDef

class DefineExpressionResponseTypeDef(BaseValidatorModel):
    Expression: ExpressionStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteExpressionResponseTypeDef(BaseValidatorModel):
    Expression: ExpressionStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeExpressionsResponseTypeDef(BaseValidatorModel):
    Expressions: List[ExpressionStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DefineSuggesterRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    Suggester: SuggesterTypeDef

class SuggesterStatusTypeDef(BaseValidatorModel):
    Options: SuggesterTypeDef
    Status: OptionStatusTypeDef

class DescribeDomainEndpointOptionsResponseTypeDef(BaseValidatorModel):
    DomainEndpointOptions: DomainEndpointOptionsStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDomainEndpointOptionsResponseTypeDef(BaseValidatorModel):
    DomainEndpointOptions: DomainEndpointOptionsStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDomainResponseTypeDef(BaseValidatorModel):
    DomainStatus: DomainStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDomainResponseTypeDef(BaseValidatorModel):
    DomainStatus: DomainStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDomainsResponseTypeDef(BaseValidatorModel):
    DomainStatusList: List[DomainStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DefineIndexFieldRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    IndexField: IndexFieldTypeDef

class IndexFieldStatusTypeDef(BaseValidatorModel):
    Options: IndexFieldTypeDef
    Status: OptionStatusTypeDef

class DescribeScalingParametersResponseTypeDef(BaseValidatorModel):
    ScalingParameters: ScalingParametersStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateScalingParametersResponseTypeDef(BaseValidatorModel):
    ScalingParameters: ScalingParametersStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DefineAnalysisSchemeResponseTypeDef(BaseValidatorModel):
    AnalysisScheme: AnalysisSchemeStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAnalysisSchemeResponseTypeDef(BaseValidatorModel):
    AnalysisScheme: AnalysisSchemeStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAnalysisSchemesResponseTypeDef(BaseValidatorModel):
    AnalysisSchemes: List[AnalysisSchemeStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DefineSuggesterResponseTypeDef(BaseValidatorModel):
    Suggester: SuggesterStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSuggesterResponseTypeDef(BaseValidatorModel):
    Suggester: SuggesterStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSuggestersResponseTypeDef(BaseValidatorModel):
    Suggesters: List[SuggesterStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DefineIndexFieldResponseTypeDef(BaseValidatorModel):
    IndexField: IndexFieldStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteIndexFieldResponseTypeDef(BaseValidatorModel):
    IndexField: IndexFieldStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeIndexFieldsResponseTypeDef(BaseValidatorModel):
    IndexFields: List[IndexFieldStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


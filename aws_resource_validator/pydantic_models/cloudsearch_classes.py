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
from aws_resource_validator.pydantic_models.cloudsearch_constants import *

class OptionStatusTypeDef(BaseModel):
    CreationDate: datetime
    UpdateDate: datetime
    State: OptionStateType
    UpdateVersion: Optional[int] = None
    PendingDeletion: Optional[bool] = None

class AnalysisOptionsTypeDef(BaseModel):
    Synonyms: Optional[str] = None
    Stopwords: Optional[str] = None
    StemmingDictionary: Optional[str] = None
    JapaneseTokenizationDictionary: Optional[str] = None
    AlgorithmicStemming: Optional[AlgorithmicStemmingType] = None

class BuildSuggestersRequestRequestTypeDef(BaseModel):
    DomainName: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateDomainRequestRequestTypeDef(BaseModel):
    DomainName: str

class DateArrayOptionsTypeDef(BaseModel):
    DefaultValue: Optional[str] = None
    SourceFields: Optional[str] = None
    FacetEnabled: Optional[bool] = None
    SearchEnabled: Optional[bool] = None
    ReturnEnabled: Optional[bool] = None

class DateOptionsTypeDef(BaseModel):
    DefaultValue: Optional[str] = None
    SourceField: Optional[str] = None
    FacetEnabled: Optional[bool] = None
    SearchEnabled: Optional[bool] = None
    ReturnEnabled: Optional[bool] = None
    SortEnabled: Optional[bool] = None

class ExpressionTypeDef(BaseModel):
    ExpressionName: str
    ExpressionValue: str

class DeleteAnalysisSchemeRequestRequestTypeDef(BaseModel):
    DomainName: str
    AnalysisSchemeName: str

class DeleteDomainRequestRequestTypeDef(BaseModel):
    DomainName: str

class DeleteExpressionRequestRequestTypeDef(BaseModel):
    DomainName: str
    ExpressionName: str

class DeleteIndexFieldRequestRequestTypeDef(BaseModel):
    DomainName: str
    IndexFieldName: str

class DeleteSuggesterRequestRequestTypeDef(BaseModel):
    DomainName: str
    SuggesterName: str

class DescribeAnalysisSchemesRequestRequestTypeDef(BaseModel):
    DomainName: str
    AnalysisSchemeNames: Optional[Sequence[str]] = None
    Deployed: Optional[bool] = None

class DescribeAvailabilityOptionsRequestRequestTypeDef(BaseModel):
    DomainName: str
    Deployed: Optional[bool] = None

class DescribeDomainEndpointOptionsRequestRequestTypeDef(BaseModel):
    DomainName: str
    Deployed: Optional[bool] = None

class DescribeDomainsRequestRequestTypeDef(BaseModel):
    DomainNames: Optional[Sequence[str]] = None

class DescribeExpressionsRequestRequestTypeDef(BaseModel):
    DomainName: str
    ExpressionNames: Optional[Sequence[str]] = None
    Deployed: Optional[bool] = None

class DescribeIndexFieldsRequestRequestTypeDef(BaseModel):
    DomainName: str
    FieldNames: Optional[Sequence[str]] = None
    Deployed: Optional[bool] = None

class DescribeScalingParametersRequestRequestTypeDef(BaseModel):
    DomainName: str

class DescribeServiceAccessPoliciesRequestRequestTypeDef(BaseModel):
    DomainName: str
    Deployed: Optional[bool] = None

class DescribeSuggestersRequestRequestTypeDef(BaseModel):
    DomainName: str
    SuggesterNames: Optional[Sequence[str]] = None
    Deployed: Optional[bool] = None

class DocumentSuggesterOptionsTypeDef(BaseModel):
    SourceField: str
    FuzzyMatching: Optional[SuggesterFuzzyMatchingType] = None
    SortExpression: Optional[str] = None

class DomainEndpointOptionsTypeDef(BaseModel):
    EnforceHTTPS: Optional[bool] = None
    TLSSecurityPolicy: Optional[TLSSecurityPolicyType] = None

class LimitsTypeDef(BaseModel):
    MaximumReplicationCount: int
    MaximumPartitionCount: int

class ServiceEndpointTypeDef(BaseModel):
    Endpoint: Optional[str] = None

class DoubleArrayOptionsTypeDef(BaseModel):
    DefaultValue: Optional[float] = None
    SourceFields: Optional[str] = None
    FacetEnabled: Optional[bool] = None
    SearchEnabled: Optional[bool] = None
    ReturnEnabled: Optional[bool] = None

class DoubleOptionsTypeDef(BaseModel):
    DefaultValue: Optional[float] = None
    SourceField: Optional[str] = None
    FacetEnabled: Optional[bool] = None
    SearchEnabled: Optional[bool] = None
    ReturnEnabled: Optional[bool] = None
    SortEnabled: Optional[bool] = None

class IndexDocumentsRequestRequestTypeDef(BaseModel):
    DomainName: str

class IntArrayOptionsTypeDef(BaseModel):
    DefaultValue: Optional[int] = None
    SourceFields: Optional[str] = None
    FacetEnabled: Optional[bool] = None
    SearchEnabled: Optional[bool] = None
    ReturnEnabled: Optional[bool] = None

class IntOptionsTypeDef(BaseModel):
    DefaultValue: Optional[int] = None
    SourceField: Optional[str] = None
    FacetEnabled: Optional[bool] = None
    SearchEnabled: Optional[bool] = None
    ReturnEnabled: Optional[bool] = None
    SortEnabled: Optional[bool] = None

class LatLonOptionsTypeDef(BaseModel):
    DefaultValue: Optional[str] = None
    SourceField: Optional[str] = None
    FacetEnabled: Optional[bool] = None
    SearchEnabled: Optional[bool] = None
    ReturnEnabled: Optional[bool] = None
    SortEnabled: Optional[bool] = None

class LiteralArrayOptionsTypeDef(BaseModel):
    DefaultValue: Optional[str] = None
    SourceFields: Optional[str] = None
    FacetEnabled: Optional[bool] = None
    SearchEnabled: Optional[bool] = None
    ReturnEnabled: Optional[bool] = None

class LiteralOptionsTypeDef(BaseModel):
    DefaultValue: Optional[str] = None
    SourceField: Optional[str] = None
    FacetEnabled: Optional[bool] = None
    SearchEnabled: Optional[bool] = None
    ReturnEnabled: Optional[bool] = None
    SortEnabled: Optional[bool] = None

class TextArrayOptionsTypeDef(BaseModel):
    DefaultValue: Optional[str] = None
    SourceFields: Optional[str] = None
    ReturnEnabled: Optional[bool] = None
    HighlightEnabled: Optional[bool] = None
    AnalysisScheme: Optional[str] = None

class TextOptionsTypeDef(BaseModel):
    DefaultValue: Optional[str] = None
    SourceField: Optional[str] = None
    ReturnEnabled: Optional[bool] = None
    SortEnabled: Optional[bool] = None
    HighlightEnabled: Optional[bool] = None
    AnalysisScheme: Optional[str] = None

class ScalingParametersTypeDef(BaseModel):
    DesiredInstanceType: Optional[PartitionInstanceTypeType] = None
    DesiredReplicationCount: Optional[int] = None
    DesiredPartitionCount: Optional[int] = None

class UpdateAvailabilityOptionsRequestRequestTypeDef(BaseModel):
    DomainName: str
    MultiAZ: bool

class UpdateServiceAccessPoliciesRequestRequestTypeDef(BaseModel):
    DomainName: str
    AccessPolicies: str

class AccessPoliciesStatusTypeDef(BaseModel):
    Options: str
    Status: OptionStatusTypeDef

class AvailabilityOptionsStatusTypeDef(BaseModel):
    Options: bool
    Status: OptionStatusTypeDef

class AnalysisSchemeTypeDef(BaseModel):
    AnalysisSchemeName: str
    AnalysisSchemeLanguage: AnalysisSchemeLanguageType
    AnalysisOptions: Optional[AnalysisOptionsTypeDef] = None

class BuildSuggestersResponseTypeDef(BaseModel):
    FieldNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class IndexDocumentsResponseTypeDef(BaseModel):
    FieldNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDomainNamesResponseTypeDef(BaseModel):
    DomainNames: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DefineExpressionRequestRequestTypeDef(BaseModel):
    DomainName: str
    Expression: ExpressionTypeDef

class ExpressionStatusTypeDef(BaseModel):
    Options: ExpressionTypeDef
    Status: OptionStatusTypeDef

class SuggesterTypeDef(BaseModel):
    SuggesterName: str
    DocumentSuggesterOptions: DocumentSuggesterOptionsTypeDef

class DomainEndpointOptionsStatusTypeDef(BaseModel):
    Options: DomainEndpointOptionsTypeDef
    Status: OptionStatusTypeDef

class UpdateDomainEndpointOptionsRequestRequestTypeDef(BaseModel):
    DomainName: str
    DomainEndpointOptions: DomainEndpointOptionsTypeDef

class DomainStatusTypeDef(BaseModel):
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

class IndexFieldTypeDef(BaseModel):
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

class ScalingParametersStatusTypeDef(BaseModel):
    Options: ScalingParametersTypeDef
    Status: OptionStatusTypeDef

class UpdateScalingParametersRequestRequestTypeDef(BaseModel):
    DomainName: str
    ScalingParameters: ScalingParametersTypeDef

class DescribeServiceAccessPoliciesResponseTypeDef(BaseModel):
    AccessPolicies: AccessPoliciesStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceAccessPoliciesResponseTypeDef(BaseModel):
    AccessPolicies: AccessPoliciesStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAvailabilityOptionsResponseTypeDef(BaseModel):
    AvailabilityOptions: AvailabilityOptionsStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAvailabilityOptionsResponseTypeDef(BaseModel):
    AvailabilityOptions: AvailabilityOptionsStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AnalysisSchemeStatusTypeDef(BaseModel):
    Options: AnalysisSchemeTypeDef
    Status: OptionStatusTypeDef

class DefineAnalysisSchemeRequestRequestTypeDef(BaseModel):
    DomainName: str
    AnalysisScheme: AnalysisSchemeTypeDef

class DefineExpressionResponseTypeDef(BaseModel):
    Expression: ExpressionStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteExpressionResponseTypeDef(BaseModel):
    Expression: ExpressionStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeExpressionsResponseTypeDef(BaseModel):
    Expressions: List[ExpressionStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DefineSuggesterRequestRequestTypeDef(BaseModel):
    DomainName: str
    Suggester: SuggesterTypeDef

class SuggesterStatusTypeDef(BaseModel):
    Options: SuggesterTypeDef
    Status: OptionStatusTypeDef

class DescribeDomainEndpointOptionsResponseTypeDef(BaseModel):
    DomainEndpointOptions: DomainEndpointOptionsStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDomainEndpointOptionsResponseTypeDef(BaseModel):
    DomainEndpointOptions: DomainEndpointOptionsStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDomainResponseTypeDef(BaseModel):
    DomainStatus: DomainStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDomainResponseTypeDef(BaseModel):
    DomainStatus: DomainStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDomainsResponseTypeDef(BaseModel):
    DomainStatusList: List[DomainStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DefineIndexFieldRequestRequestTypeDef(BaseModel):
    DomainName: str
    IndexField: IndexFieldTypeDef

class IndexFieldStatusTypeDef(BaseModel):
    Options: IndexFieldTypeDef
    Status: OptionStatusTypeDef

class DescribeScalingParametersResponseTypeDef(BaseModel):
    ScalingParameters: ScalingParametersStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateScalingParametersResponseTypeDef(BaseModel):
    ScalingParameters: ScalingParametersStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DefineAnalysisSchemeResponseTypeDef(BaseModel):
    AnalysisScheme: AnalysisSchemeStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAnalysisSchemeResponseTypeDef(BaseModel):
    AnalysisScheme: AnalysisSchemeStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAnalysisSchemesResponseTypeDef(BaseModel):
    AnalysisSchemes: List[AnalysisSchemeStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DefineSuggesterResponseTypeDef(BaseModel):
    Suggester: SuggesterStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSuggesterResponseTypeDef(BaseModel):
    Suggester: SuggesterStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSuggestersResponseTypeDef(BaseModel):
    Suggesters: List[SuggesterStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DefineIndexFieldResponseTypeDef(BaseModel):
    IndexField: IndexFieldStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteIndexFieldResponseTypeDef(BaseModel):
    IndexField: IndexFieldStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeIndexFieldsResponseTypeDef(BaseModel):
    IndexFields: List[IndexFieldStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


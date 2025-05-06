from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class Trait(BaseValidatorModel):
    Name: Optional[AttributeNameType] = None
    Score: Optional[float] = None


class Characters(BaseValidatorModel):
    OriginalTextCharacters: Optional[int] = None

Timestamp = Union[datetime, str]


class InputDataConfig(BaseValidatorModel):
    S3Bucket: str
    S3Key: Optional[str] = None


class OutputDataConfig(BaseValidatorModel):
    S3Bucket: str
    S3Key: Optional[str] = None


class DescribeEntitiesDetectionV2JobRequest(BaseValidatorModel):
    JobId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DescribeICD10CMInferenceJobRequest(BaseValidatorModel):
    JobId: str


class DescribePHIDetectionJobRequest(BaseValidatorModel):
    JobId: str


class DescribeRxNormInferenceJobRequest(BaseValidatorModel):
    JobId: str


class DescribeSNOMEDCTInferenceJobRequest(BaseValidatorModel):
    JobId: str


class DetectEntitiesRequest(BaseValidatorModel):
    Text: str


class DetectEntitiesV2Request(BaseValidatorModel):
    Text: str


class DetectPHIRequest(BaseValidatorModel):
    Text: str


class ICD10CMTrait(BaseValidatorModel):
    Name: Optional[ICD10CMTraitNameType] = None
    Score: Optional[float] = None


class ICD10CMConcept(BaseValidatorModel):
    Description: Optional[str] = None
    Code: Optional[str] = None
    Score: Optional[float] = None


class InferICD10CMRequest(BaseValidatorModel):
    Text: str


class InferRxNormRequest(BaseValidatorModel):
    Text: str


class InferSNOMEDCTRequest(BaseValidatorModel):
    Text: str


class SNOMEDCTDetails(BaseValidatorModel):
    Edition: Optional[str] = None
    Language: Optional[str] = None
    VersionDate: Optional[str] = None


class RxNormTrait(BaseValidatorModel):
    Name: Optional[RxNormTraitNameType] = None
    Score: Optional[float] = None


class RxNormConcept(BaseValidatorModel):
    Description: Optional[str] = None
    Code: Optional[str] = None
    Score: Optional[float] = None


class SNOMEDCTConcept(BaseValidatorModel):
    Description: Optional[str] = None
    Code: Optional[str] = None
    Score: Optional[float] = None


class SNOMEDCTTrait(BaseValidatorModel):
    Name: Optional[SNOMEDCTTraitNameType] = None
    Score: Optional[float] = None


class StopEntitiesDetectionV2JobRequest(BaseValidatorModel):
    JobId: str


class StopICD10CMInferenceJobRequest(BaseValidatorModel):
    JobId: str


class StopPHIDetectionJobRequest(BaseValidatorModel):
    JobId: str


class StopRxNormInferenceJobRequest(BaseValidatorModel):
    JobId: str


class StopSNOMEDCTInferenceJobRequest(BaseValidatorModel):
    JobId: str


class Attribute(BaseValidatorModel):
    Type: Optional[EntitySubTypeType] = None
    Score: Optional[float] = None
    RelationshipScore: Optional[float] = None
    RelationshipType: Optional[RelationshipTypeType] = None
    Id: Optional[int] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None
    Text: Optional[str] = None
    Category: Optional[EntityTypeType] = None
    Traits: Optional[List[Trait]] = None


class ComprehendMedicalAsyncJobFilter(BaseValidatorModel):
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmitTimeBefore: Optional[Timestamp] = None
    SubmitTimeAfter: Optional[Timestamp] = None


class ComprehendMedicalAsyncJobProperties(BaseValidatorModel):
    JobId: Optional[str] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    ExpirationTime: Optional[datetime] = None
    InputDataConfig: Optional[InputDataConfig] = None
    OutputDataConfig: Optional[OutputDataConfig] = None
    LanguageCode: Optional[Literal['en']] = None
    DataAccessRoleArn: Optional[str] = None
    ManifestFilePath: Optional[str] = None
    KMSKey: Optional[str] = None
    ModelVersion: Optional[str] = None


class StartEntitiesDetectionV2JobRequest(BaseValidatorModel):
    InputDataConfig: InputDataConfig
    OutputDataConfig: OutputDataConfig
    DataAccessRoleArn: str
    LanguageCode: Literal['en']
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    KMSKey: Optional[str] = None


class StartICD10CMInferenceJobRequest(BaseValidatorModel):
    InputDataConfig: InputDataConfig
    OutputDataConfig: OutputDataConfig
    DataAccessRoleArn: str
    LanguageCode: Literal['en']
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    KMSKey: Optional[str] = None


class StartPHIDetectionJobRequest(BaseValidatorModel):
    InputDataConfig: InputDataConfig
    OutputDataConfig: OutputDataConfig
    DataAccessRoleArn: str
    LanguageCode: Literal['en']
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    KMSKey: Optional[str] = None


class StartRxNormInferenceJobRequest(BaseValidatorModel):
    InputDataConfig: InputDataConfig
    OutputDataConfig: OutputDataConfig
    DataAccessRoleArn: str
    LanguageCode: Literal['en']
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    KMSKey: Optional[str] = None


class StartSNOMEDCTInferenceJobRequest(BaseValidatorModel):
    InputDataConfig: InputDataConfig
    OutputDataConfig: OutputDataConfig
    DataAccessRoleArn: str
    LanguageCode: Literal['en']
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    KMSKey: Optional[str] = None


class StartEntitiesDetectionV2JobResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


class StartICD10CMInferenceJobResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


class StartPHIDetectionJobResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


class StartRxNormInferenceJobResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


class StartSNOMEDCTInferenceJobResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


class StopEntitiesDetectionV2JobResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


class StopICD10CMInferenceJobResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


class StopPHIDetectionJobResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


class StopRxNormInferenceJobResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


class StopSNOMEDCTInferenceJobResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


class ICD10CMAttribute(BaseValidatorModel):
    Type: Optional[ICD10CMAttributeTypeType] = None
    Score: Optional[float] = None
    RelationshipScore: Optional[float] = None
    Id: Optional[int] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None
    Text: Optional[str] = None
    Traits: Optional[List[ICD10CMTrait]] = None
    Category: Optional[ICD10CMEntityTypeType] = None
    RelationshipType: Optional[ICD10CMRelationshipTypeType] = None


class RxNormAttribute(BaseValidatorModel):
    Type: Optional[RxNormAttributeTypeType] = None
    Score: Optional[float] = None
    RelationshipScore: Optional[float] = None
    Id: Optional[int] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None
    Text: Optional[str] = None
    Traits: Optional[List[RxNormTrait]] = None


class SNOMEDCTAttribute(BaseValidatorModel):
    Category: Optional[SNOMEDCTEntityCategoryType] = None
    Type: Optional[SNOMEDCTAttributeTypeType] = None
    Score: Optional[float] = None
    RelationshipScore: Optional[float] = None
    RelationshipType: Optional[SNOMEDCTRelationshipTypeType] = None
    Id: Optional[int] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None
    Text: Optional[str] = None
    Traits: Optional[List[SNOMEDCTTrait]] = None
    SNOMEDCTConcepts: Optional[List[SNOMEDCTConcept]] = None


class Entity(BaseValidatorModel):
    Id: Optional[int] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None
    Score: Optional[float] = None
    Text: Optional[str] = None
    Category: Optional[EntityTypeType] = None
    Type: Optional[EntitySubTypeType] = None
    Traits: Optional[List[Trait]] = None
    Attributes: Optional[List[Attribute]] = None


class UnmappedAttribute(BaseValidatorModel):
    Type: Optional[EntityTypeType] = None
    Attribute: Optional[Attribute] = None


class ListEntitiesDetectionV2JobsRequest(BaseValidatorModel):
    Filter: Optional[ComprehendMedicalAsyncJobFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListICD10CMInferenceJobsRequest(BaseValidatorModel):
    Filter: Optional[ComprehendMedicalAsyncJobFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListPHIDetectionJobsRequest(BaseValidatorModel):
    Filter: Optional[ComprehendMedicalAsyncJobFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListRxNormInferenceJobsRequest(BaseValidatorModel):
    Filter: Optional[ComprehendMedicalAsyncJobFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListSNOMEDCTInferenceJobsRequest(BaseValidatorModel):
    Filter: Optional[ComprehendMedicalAsyncJobFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeEntitiesDetectionV2JobResponse(BaseValidatorModel):
    ComprehendMedicalAsyncJobProperties: ComprehendMedicalAsyncJobProperties
    ResponseMetadata: ResponseMetadata


class DescribeICD10CMInferenceJobResponse(BaseValidatorModel):
    ComprehendMedicalAsyncJobProperties: ComprehendMedicalAsyncJobProperties
    ResponseMetadata: ResponseMetadata


class DescribePHIDetectionJobResponse(BaseValidatorModel):
    ComprehendMedicalAsyncJobProperties: ComprehendMedicalAsyncJobProperties
    ResponseMetadata: ResponseMetadata


class DescribeRxNormInferenceJobResponse(BaseValidatorModel):
    ComprehendMedicalAsyncJobProperties: ComprehendMedicalAsyncJobProperties
    ResponseMetadata: ResponseMetadata


class DescribeSNOMEDCTInferenceJobResponse(BaseValidatorModel):
    ComprehendMedicalAsyncJobProperties: ComprehendMedicalAsyncJobProperties
    ResponseMetadata: ResponseMetadata


class ListEntitiesDetectionV2JobsResponse(BaseValidatorModel):
    ComprehendMedicalAsyncJobPropertiesList: List[ComprehendMedicalAsyncJobProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListICD10CMInferenceJobsResponse(BaseValidatorModel):
    ComprehendMedicalAsyncJobPropertiesList: List[ComprehendMedicalAsyncJobProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListPHIDetectionJobsResponse(BaseValidatorModel):
    ComprehendMedicalAsyncJobPropertiesList: List[ComprehendMedicalAsyncJobProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListRxNormInferenceJobsResponse(BaseValidatorModel):
    ComprehendMedicalAsyncJobPropertiesList: List[ComprehendMedicalAsyncJobProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListSNOMEDCTInferenceJobsResponse(BaseValidatorModel):
    ComprehendMedicalAsyncJobPropertiesList: List[ComprehendMedicalAsyncJobProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ICD10CMEntity(BaseValidatorModel):
    Id: Optional[int] = None
    Text: Optional[str] = None
    Category: Optional[Literal['MEDICAL_CONDITION']] = None
    Type: Optional[ICD10CMEntityTypeType] = None
    Score: Optional[float] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None
    Attributes: Optional[List[ICD10CMAttribute]] = None
    Traits: Optional[List[ICD10CMTrait]] = None
    ICD10CMConcepts: Optional[List[ICD10CMConcept]] = None


class RxNormEntity(BaseValidatorModel):
    Id: Optional[int] = None
    Text: Optional[str] = None
    Category: Optional[Literal['MEDICATION']] = None
    Type: Optional[RxNormEntityTypeType] = None
    Score: Optional[float] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None
    Attributes: Optional[List[RxNormAttribute]] = None
    Traits: Optional[List[RxNormTrait]] = None
    RxNormConcepts: Optional[List[RxNormConcept]] = None


class SNOMEDCTEntity(BaseValidatorModel):
    Id: Optional[int] = None
    Text: Optional[str] = None
    Category: Optional[SNOMEDCTEntityCategoryType] = None
    Type: Optional[SNOMEDCTEntityTypeType] = None
    Score: Optional[float] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None
    Attributes: Optional[List[SNOMEDCTAttribute]] = None
    Traits: Optional[List[SNOMEDCTTrait]] = None
    SNOMEDCTConcepts: Optional[List[SNOMEDCTConcept]] = None


class DetectPHIResponse(BaseValidatorModel):
    Entities: List[Entity]
    PaginationToken: str
    ModelVersion: str
    ResponseMetadata: ResponseMetadata


class DetectEntitiesResponse(BaseValidatorModel):
    Entities: List[Entity]
    UnmappedAttributes: List[UnmappedAttribute]
    PaginationToken: str
    ModelVersion: str
    ResponseMetadata: ResponseMetadata


class DetectEntitiesV2Response(BaseValidatorModel):
    Entities: List[Entity]
    UnmappedAttributes: List[UnmappedAttribute]
    PaginationToken: str
    ModelVersion: str
    ResponseMetadata: ResponseMetadata


class InferICD10CMResponse(BaseValidatorModel):
    Entities: List[ICD10CMEntity]
    PaginationToken: str
    ModelVersion: str
    ResponseMetadata: ResponseMetadata


class InferRxNormResponse(BaseValidatorModel):
    Entities: List[RxNormEntity]
    PaginationToken: str
    ModelVersion: str
    ResponseMetadata: ResponseMetadata


class InferSNOMEDCTResponse(BaseValidatorModel):
    Entities: List[SNOMEDCTEntity]
    PaginationToken: str
    ModelVersion: str
    SNOMEDCTDetails: SNOMEDCTDetails
    Characters: Characters
    ResponseMetadata: ResponseMetadata
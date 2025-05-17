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


# This class is the input for the 'describe_entities_detection_v2_job' function.
class DescribeEntitiesDetectionV2JobRequest(BaseValidatorModel):
    JobId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'describe_icd10_cm_inference_job' function.
class DescribeICD10CMInferenceJobRequest(BaseValidatorModel):
    JobId: str


# This class is the input for the 'describe_phi_detection_job' function.
class DescribePHIDetectionJobRequest(BaseValidatorModel):
    JobId: str


# This class is the input for the 'describe_rx_norm_inference_job' function.
class DescribeRxNormInferenceJobRequest(BaseValidatorModel):
    JobId: str


# This class is the input for the 'describe_snomedct_inference_job' function.
class DescribeSNOMEDCTInferenceJobRequest(BaseValidatorModel):
    JobId: str


# This class is the input for the 'detect_entities' function.
class DetectEntitiesRequest(BaseValidatorModel):
    Text: str


# This class is the input for the 'detect_entities_v2' function.
class DetectEntitiesV2Request(BaseValidatorModel):
    Text: str


# This class is the input for the 'detect_phi' function.
class DetectPHIRequest(BaseValidatorModel):
    Text: str


class ICD10CMTrait(BaseValidatorModel):
    Name: Optional[ICD10CMTraitNameType] = None
    Score: Optional[float] = None


class ICD10CMConcept(BaseValidatorModel):
    Description: Optional[str] = None
    Code: Optional[str] = None
    Score: Optional[float] = None


# This class is the input for the 'infer_icd10_cm' function.
class InferICD10CMRequest(BaseValidatorModel):
    Text: str


# This class is the input for the 'infer_rx_norm' function.
class InferRxNormRequest(BaseValidatorModel):
    Text: str


# This class is the input for the 'infer_snomedct' function.
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


# This class is the input for the 'stop_entities_detection_v2_job' function.
class StopEntitiesDetectionV2JobRequest(BaseValidatorModel):
    JobId: str


# This class is the input for the 'stop_icd10_cm_inference_job' function.
class StopICD10CMInferenceJobRequest(BaseValidatorModel):
    JobId: str


# This class is the input for the 'stop_phi_detection_job' function.
class StopPHIDetectionJobRequest(BaseValidatorModel):
    JobId: str


# This class is the input for the 'stop_rx_norm_inference_job' function.
class StopRxNormInferenceJobRequest(BaseValidatorModel):
    JobId: str


# This class is the input for the 'stop_snomedct_inference_job' function.
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


# This class is the input for the 'start_entities_detection_v2_job' function.
class StartEntitiesDetectionV2JobRequest(BaseValidatorModel):
    InputDataConfig: InputDataConfig
    OutputDataConfig: OutputDataConfig
    DataAccessRoleArn: str
    LanguageCode: Literal['en']
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    KMSKey: Optional[str] = None


# This class is the input for the 'start_icd10_cm_inference_job' function.
class StartICD10CMInferenceJobRequest(BaseValidatorModel):
    InputDataConfig: InputDataConfig
    OutputDataConfig: OutputDataConfig
    DataAccessRoleArn: str
    LanguageCode: Literal['en']
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    KMSKey: Optional[str] = None


# This class is the input for the 'start_phi_detection_job' function.
class StartPHIDetectionJobRequest(BaseValidatorModel):
    InputDataConfig: InputDataConfig
    OutputDataConfig: OutputDataConfig
    DataAccessRoleArn: str
    LanguageCode: Literal['en']
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    KMSKey: Optional[str] = None


# This class is the input for the 'start_rx_norm_inference_job' function.
class StartRxNormInferenceJobRequest(BaseValidatorModel):
    InputDataConfig: InputDataConfig
    OutputDataConfig: OutputDataConfig
    DataAccessRoleArn: str
    LanguageCode: Literal['en']
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    KMSKey: Optional[str] = None


# This class is the input for the 'start_snomedct_inference_job' function.
class StartSNOMEDCTInferenceJobRequest(BaseValidatorModel):
    InputDataConfig: InputDataConfig
    OutputDataConfig: OutputDataConfig
    DataAccessRoleArn: str
    LanguageCode: Literal['en']
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    KMSKey: Optional[str] = None


# This class is the output for the 'start_entities_detection_v2_job' function.
class StartEntitiesDetectionV2JobResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_icd10_cm_inference_job' function.
class StartICD10CMInferenceJobResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_phi_detection_job' function.
class StartPHIDetectionJobResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_rx_norm_inference_job' function.
class StartRxNormInferenceJobResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_snomedct_inference_job' function.
class StartSNOMEDCTInferenceJobResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_entities_detection_v2_job' function.
class StopEntitiesDetectionV2JobResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_icd10_cm_inference_job' function.
class StopICD10CMInferenceJobResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_phi_detection_job' function.
class StopPHIDetectionJobResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_rx_norm_inference_job' function.
class StopRxNormInferenceJobResponse(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_snomedct_inference_job' function.
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


# This class is the input for the 'list_entities_detection_v2_jobs' function.
class ListEntitiesDetectionV2JobsRequest(BaseValidatorModel):
    Filter: Optional[ComprehendMedicalAsyncJobFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_icd10_cm_inference_jobs' function.
class ListICD10CMInferenceJobsRequest(BaseValidatorModel):
    Filter: Optional[ComprehendMedicalAsyncJobFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_phi_detection_jobs' function.
class ListPHIDetectionJobsRequest(BaseValidatorModel):
    Filter: Optional[ComprehendMedicalAsyncJobFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_rx_norm_inference_jobs' function.
class ListRxNormInferenceJobsRequest(BaseValidatorModel):
    Filter: Optional[ComprehendMedicalAsyncJobFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_snomedct_inference_jobs' function.
class ListSNOMEDCTInferenceJobsRequest(BaseValidatorModel):
    Filter: Optional[ComprehendMedicalAsyncJobFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the output for the 'describe_entities_detection_v2_job' function.
class DescribeEntitiesDetectionV2JobResponse(BaseValidatorModel):
    ComprehendMedicalAsyncJobProperties: ComprehendMedicalAsyncJobProperties
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_icd10_cm_inference_job' function.
class DescribeICD10CMInferenceJobResponse(BaseValidatorModel):
    ComprehendMedicalAsyncJobProperties: ComprehendMedicalAsyncJobProperties
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_phi_detection_job' function.
class DescribePHIDetectionJobResponse(BaseValidatorModel):
    ComprehendMedicalAsyncJobProperties: ComprehendMedicalAsyncJobProperties
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_rx_norm_inference_job' function.
class DescribeRxNormInferenceJobResponse(BaseValidatorModel):
    ComprehendMedicalAsyncJobProperties: ComprehendMedicalAsyncJobProperties
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_snomedct_inference_job' function.
class DescribeSNOMEDCTInferenceJobResponse(BaseValidatorModel):
    ComprehendMedicalAsyncJobProperties: ComprehendMedicalAsyncJobProperties
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_entities_detection_v2_jobs' function.
class ListEntitiesDetectionV2JobsResponse(BaseValidatorModel):
    ComprehendMedicalAsyncJobPropertiesList: List[ComprehendMedicalAsyncJobProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_icd10_cm_inference_jobs' function.
class ListICD10CMInferenceJobsResponse(BaseValidatorModel):
    ComprehendMedicalAsyncJobPropertiesList: List[ComprehendMedicalAsyncJobProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_phi_detection_jobs' function.
class ListPHIDetectionJobsResponse(BaseValidatorModel):
    ComprehendMedicalAsyncJobPropertiesList: List[ComprehendMedicalAsyncJobProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_rx_norm_inference_jobs' function.
class ListRxNormInferenceJobsResponse(BaseValidatorModel):
    ComprehendMedicalAsyncJobPropertiesList: List[ComprehendMedicalAsyncJobProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_snomedct_inference_jobs' function.
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


# This class is the output for the 'detect_phi' function.
class DetectPHIResponse(BaseValidatorModel):
    Entities: List[Entity]
    PaginationToken: str
    ModelVersion: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'detect_entities' function.
class DetectEntitiesResponse(BaseValidatorModel):
    Entities: List[Entity]
    UnmappedAttributes: List[UnmappedAttribute]
    PaginationToken: str
    ModelVersion: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'detect_entities_v2' function.
class DetectEntitiesV2Response(BaseValidatorModel):
    Entities: List[Entity]
    UnmappedAttributes: List[UnmappedAttribute]
    PaginationToken: str
    ModelVersion: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'infer_icd10_cm' function.
class InferICD10CMResponse(BaseValidatorModel):
    Entities: List[ICD10CMEntity]
    PaginationToken: str
    ModelVersion: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'infer_rx_norm' function.
class InferRxNormResponse(BaseValidatorModel):
    Entities: List[RxNormEntity]
    PaginationToken: str
    ModelVersion: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'infer_snomedct' function.
class InferSNOMEDCTResponse(BaseValidatorModel):
    Entities: List[SNOMEDCTEntity]
    PaginationToken: str
    ModelVersion: str
    SNOMEDCTDetails: SNOMEDCTDetails
    Characters: Characters
    ResponseMetadata: ResponseMetadata
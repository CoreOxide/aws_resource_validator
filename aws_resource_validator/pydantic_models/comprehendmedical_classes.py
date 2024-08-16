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
from aws_resource_validator.pydantic_models.comprehendmedical_constants import *

class TraitTypeDef(BaseValidatorModel):
    Name: Optional[AttributeNameType] = None
    Score: Optional[float] = None

class CharactersTypeDef(BaseValidatorModel):
    OriginalTextCharacters: Optional[int] = None

class InputDataConfigTypeDef(BaseValidatorModel):
    S3Bucket: str
    S3Key: Optional[str] = None

class OutputDataConfigTypeDef(BaseValidatorModel):
    S3Bucket: str
    S3Key: Optional[str] = None

class DescribeEntitiesDetectionV2JobRequestRequestTypeDef(BaseValidatorModel):
    JobId: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DescribeICD10CMInferenceJobRequestRequestTypeDef(BaseValidatorModel):
    JobId: str

class DescribePHIDetectionJobRequestRequestTypeDef(BaseValidatorModel):
    JobId: str

class DescribeRxNormInferenceJobRequestRequestTypeDef(BaseValidatorModel):
    JobId: str

class DescribeSNOMEDCTInferenceJobRequestRequestTypeDef(BaseValidatorModel):
    JobId: str

class DetectEntitiesRequestRequestTypeDef(BaseValidatorModel):
    Text: str

class DetectEntitiesV2RequestRequestTypeDef(BaseValidatorModel):
    Text: str

class DetectPHIRequestRequestTypeDef(BaseValidatorModel):
    Text: str

class ICD10CMTraitTypeDef(BaseValidatorModel):
    Name: Optional[ICD10CMTraitNameType] = None
    Score: Optional[float] = None

class ICD10CMConceptTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    Code: Optional[str] = None
    Score: Optional[float] = None

class InferICD10CMRequestRequestTypeDef(BaseValidatorModel):
    Text: str

class InferRxNormRequestRequestTypeDef(BaseValidatorModel):
    Text: str

class InferSNOMEDCTRequestRequestTypeDef(BaseValidatorModel):
    Text: str

class SNOMEDCTDetailsTypeDef(BaseValidatorModel):
    Edition: Optional[str] = None
    Language: Optional[str] = None
    VersionDate: Optional[str] = None

class RxNormTraitTypeDef(BaseValidatorModel):
    Name: Optional[RxNormTraitNameType] = None
    Score: Optional[float] = None

class RxNormConceptTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    Code: Optional[str] = None
    Score: Optional[float] = None

class SNOMEDCTConceptTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    Code: Optional[str] = None
    Score: Optional[float] = None

class SNOMEDCTTraitTypeDef(BaseValidatorModel):
    Name: Optional[SNOMEDCTTraitNameType] = None
    Score: Optional[float] = None

class StopEntitiesDetectionV2JobRequestRequestTypeDef(BaseValidatorModel):
    JobId: str

class StopICD10CMInferenceJobRequestRequestTypeDef(BaseValidatorModel):
    JobId: str

class StopPHIDetectionJobRequestRequestTypeDef(BaseValidatorModel):
    JobId: str

class StopRxNormInferenceJobRequestRequestTypeDef(BaseValidatorModel):
    JobId: str

class StopSNOMEDCTInferenceJobRequestRequestTypeDef(BaseValidatorModel):
    JobId: str

class AttributeTypeDef(BaseValidatorModel):
    Type: Optional[EntitySubTypeType] = None
    Score: Optional[float] = None
    RelationshipScore: Optional[float] = None
    RelationshipType: Optional[RelationshipTypeType] = None
    Id: Optional[int] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None
    Text: Optional[str] = None
    Category: Optional[EntityTypeType] = None
    Traits: Optional[List[TraitTypeDef]] = None

class ComprehendMedicalAsyncJobFilterTypeDef(BaseValidatorModel):
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmitTimeBefore: Optional[TimestampTypeDef] = None
    SubmitTimeAfter: Optional[TimestampTypeDef] = None

class ComprehendMedicalAsyncJobPropertiesTypeDef(BaseValidatorModel):
    JobId: Optional[str] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    Message: Optional[str] = None
    SubmitTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    ExpirationTime: Optional[datetime] = None
    InputDataConfig: Optional[InputDataConfigTypeDef] = None
    OutputDataConfig: Optional[OutputDataConfigTypeDef] = None
    LanguageCode: Optional[Literal["en"]] = None
    DataAccessRoleArn: Optional[str] = None
    ManifestFilePath: Optional[str] = None
    KMSKey: Optional[str] = None
    ModelVersion: Optional[str] = None

class StartEntitiesDetectionV2JobRequestRequestTypeDef(BaseValidatorModel):
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    LanguageCode: Literal["en"]
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    KMSKey: Optional[str] = None

class StartICD10CMInferenceJobRequestRequestTypeDef(BaseValidatorModel):
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    LanguageCode: Literal["en"]
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    KMSKey: Optional[str] = None

class StartPHIDetectionJobRequestRequestTypeDef(BaseValidatorModel):
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    LanguageCode: Literal["en"]
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    KMSKey: Optional[str] = None

class StartRxNormInferenceJobRequestRequestTypeDef(BaseValidatorModel):
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    LanguageCode: Literal["en"]
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    KMSKey: Optional[str] = None

class StartSNOMEDCTInferenceJobRequestRequestTypeDef(BaseValidatorModel):
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    LanguageCode: Literal["en"]
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    KMSKey: Optional[str] = None

class StartEntitiesDetectionV2JobResponseTypeDef(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartICD10CMInferenceJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartPHIDetectionJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartRxNormInferenceJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartSNOMEDCTInferenceJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopEntitiesDetectionV2JobResponseTypeDef(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopICD10CMInferenceJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopPHIDetectionJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopRxNormInferenceJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopSNOMEDCTInferenceJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ICD10CMAttributeTypeDef(BaseValidatorModel):
    Type: Optional[ICD10CMAttributeTypeType] = None
    Score: Optional[float] = None
    RelationshipScore: Optional[float] = None
    Id: Optional[int] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None
    Text: Optional[str] = None
    Traits: Optional[List[ICD10CMTraitTypeDef]] = None
    Category: Optional[ICD10CMEntityTypeType] = None
    RelationshipType: Optional[ICD10CMRelationshipTypeType] = None

class RxNormAttributeTypeDef(BaseValidatorModel):
    Type: Optional[RxNormAttributeTypeType] = None
    Score: Optional[float] = None
    RelationshipScore: Optional[float] = None
    Id: Optional[int] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None
    Text: Optional[str] = None
    Traits: Optional[List[RxNormTraitTypeDef]] = None

class SNOMEDCTAttributeTypeDef(BaseValidatorModel):
    Category: Optional[SNOMEDCTEntityCategoryType] = None
    Type: Optional[SNOMEDCTAttributeTypeType] = None
    Score: Optional[float] = None
    RelationshipScore: Optional[float] = None
    RelationshipType: Optional[SNOMEDCTRelationshipTypeType] = None
    Id: Optional[int] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None
    Text: Optional[str] = None
    Traits: Optional[List[SNOMEDCTTraitTypeDef]] = None
    SNOMEDCTConcepts: Optional[List[SNOMEDCTConceptTypeDef]] = None

class EntityTypeDef(BaseValidatorModel):
    Id: Optional[int] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None
    Score: Optional[float] = None
    Text: Optional[str] = None
    Category: Optional[EntityTypeType] = None
    Type: Optional[EntitySubTypeType] = None
    Traits: Optional[List[TraitTypeDef]] = None
    Attributes: Optional[List[AttributeTypeDef]] = None

class UnmappedAttributeTypeDef(BaseValidatorModel):
    Type: Optional[EntityTypeType] = None
    Attribute: Optional[AttributeTypeDef] = None

class ListEntitiesDetectionV2JobsRequestRequestTypeDef(BaseValidatorModel):
    Filter: Optional[ComprehendMedicalAsyncJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListICD10CMInferenceJobsRequestRequestTypeDef(BaseValidatorModel):
    Filter: Optional[ComprehendMedicalAsyncJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListPHIDetectionJobsRequestRequestTypeDef(BaseValidatorModel):
    Filter: Optional[ComprehendMedicalAsyncJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListRxNormInferenceJobsRequestRequestTypeDef(BaseValidatorModel):
    Filter: Optional[ComprehendMedicalAsyncJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListSNOMEDCTInferenceJobsRequestRequestTypeDef(BaseValidatorModel):
    Filter: Optional[ComprehendMedicalAsyncJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeEntitiesDetectionV2JobResponseTypeDef(BaseValidatorModel):
    ComprehendMedicalAsyncJobProperties: ComprehendMedicalAsyncJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeICD10CMInferenceJobResponseTypeDef(BaseValidatorModel):
    ComprehendMedicalAsyncJobProperties: ComprehendMedicalAsyncJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePHIDetectionJobResponseTypeDef(BaseValidatorModel):
    ComprehendMedicalAsyncJobProperties: ComprehendMedicalAsyncJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRxNormInferenceJobResponseTypeDef(BaseValidatorModel):
    ComprehendMedicalAsyncJobProperties: ComprehendMedicalAsyncJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSNOMEDCTInferenceJobResponseTypeDef(BaseValidatorModel):
    ComprehendMedicalAsyncJobProperties: ComprehendMedicalAsyncJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEntitiesDetectionV2JobsResponseTypeDef(BaseValidatorModel):
    ComprehendMedicalAsyncJobPropertiesList: List[ComprehendMedicalAsyncJobPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListICD10CMInferenceJobsResponseTypeDef(BaseValidatorModel):
    ComprehendMedicalAsyncJobPropertiesList: List[ComprehendMedicalAsyncJobPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPHIDetectionJobsResponseTypeDef(BaseValidatorModel):
    ComprehendMedicalAsyncJobPropertiesList: List[ComprehendMedicalAsyncJobPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRxNormInferenceJobsResponseTypeDef(BaseValidatorModel):
    ComprehendMedicalAsyncJobPropertiesList: List[ComprehendMedicalAsyncJobPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSNOMEDCTInferenceJobsResponseTypeDef(BaseValidatorModel):
    ComprehendMedicalAsyncJobPropertiesList: List[ComprehendMedicalAsyncJobPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ICD10CMEntityTypeDef(BaseValidatorModel):
    Id: Optional[int] = None
    Text: Optional[str] = None
    Category: Optional[Literal["MEDICAL_CONDITION"]] = None
    Type: Optional[ICD10CMEntityTypeType] = None
    Score: Optional[float] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None
    Attributes: Optional[List[ICD10CMAttributeTypeDef]] = None
    Traits: Optional[List[ICD10CMTraitTypeDef]] = None
    ICD10CMConcepts: Optional[List[ICD10CMConceptTypeDef]] = None

class RxNormEntityTypeDef(BaseValidatorModel):
    Id: Optional[int] = None
    Text: Optional[str] = None
    Category: Optional[Literal["MEDICATION"]] = None
    Type: Optional[RxNormEntityTypeType] = None
    Score: Optional[float] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None
    Attributes: Optional[List[RxNormAttributeTypeDef]] = None
    Traits: Optional[List[RxNormTraitTypeDef]] = None
    RxNormConcepts: Optional[List[RxNormConceptTypeDef]] = None

class SNOMEDCTEntityTypeDef(BaseValidatorModel):
    Id: Optional[int] = None
    Text: Optional[str] = None
    Category: Optional[SNOMEDCTEntityCategoryType] = None
    Type: Optional[SNOMEDCTEntityTypeType] = None
    Score: Optional[float] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None
    Attributes: Optional[List[SNOMEDCTAttributeTypeDef]] = None
    Traits: Optional[List[SNOMEDCTTraitTypeDef]] = None
    SNOMEDCTConcepts: Optional[List[SNOMEDCTConceptTypeDef]] = None

class DetectPHIResponseTypeDef(BaseValidatorModel):
    Entities: List[EntityTypeDef]
    PaginationToken: str
    ModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class DetectEntitiesResponseTypeDef(BaseValidatorModel):
    Entities: List[EntityTypeDef]
    UnmappedAttributes: List[UnmappedAttributeTypeDef]
    PaginationToken: str
    ModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class DetectEntitiesV2ResponseTypeDef(BaseValidatorModel):
    Entities: List[EntityTypeDef]
    UnmappedAttributes: List[UnmappedAttributeTypeDef]
    PaginationToken: str
    ModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class InferICD10CMResponseTypeDef(BaseValidatorModel):
    Entities: List[ICD10CMEntityTypeDef]
    PaginationToken: str
    ModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class InferRxNormResponseTypeDef(BaseValidatorModel):
    Entities: List[RxNormEntityTypeDef]
    PaginationToken: str
    ModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class InferSNOMEDCTResponseTypeDef(BaseValidatorModel):
    Entities: List[SNOMEDCTEntityTypeDef]
    PaginationToken: str
    ModelVersion: str
    SNOMEDCTDetails: SNOMEDCTDetailsTypeDef
    Characters: CharactersTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


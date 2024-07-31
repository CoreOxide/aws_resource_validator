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
from aws_resource_validator.pydantic_models.comprehendmedical_constants import *

class TraitTypeDef(BaseModel):
    Name: Optional[AttributeNameType] = None
    Score: Optional[float] = None

class CharactersTypeDef(BaseModel):
    OriginalTextCharacters: Optional[int] = None

class InputDataConfigTypeDef(BaseModel):
    S3Bucket: str
    S3Key: Optional[str] = None

class OutputDataConfigTypeDef(BaseModel):
    S3Bucket: str
    S3Key: Optional[str] = None

class DescribeEntitiesDetectionV2JobRequestRequestTypeDef(BaseModel):
    JobId: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DescribeICD10CMInferenceJobRequestRequestTypeDef(BaseModel):
    JobId: str

class DescribePHIDetectionJobRequestRequestTypeDef(BaseModel):
    JobId: str

class DescribeRxNormInferenceJobRequestRequestTypeDef(BaseModel):
    JobId: str

class DescribeSNOMEDCTInferenceJobRequestRequestTypeDef(BaseModel):
    JobId: str

class DetectEntitiesRequestRequestTypeDef(BaseModel):
    Text: str

class DetectEntitiesV2RequestRequestTypeDef(BaseModel):
    Text: str

class DetectPHIRequestRequestTypeDef(BaseModel):
    Text: str

class ICD10CMTraitTypeDef(BaseModel):
    Name: Optional[ICD10CMTraitNameType] = None
    Score: Optional[float] = None

class ICD10CMConceptTypeDef(BaseModel):
    Description: Optional[str] = None
    Code: Optional[str] = None
    Score: Optional[float] = None

class InferICD10CMRequestRequestTypeDef(BaseModel):
    Text: str

class InferRxNormRequestRequestTypeDef(BaseModel):
    Text: str

class InferSNOMEDCTRequestRequestTypeDef(BaseModel):
    Text: str

class SNOMEDCTDetailsTypeDef(BaseModel):
    Edition: Optional[str] = None
    Language: Optional[str] = None
    VersionDate: Optional[str] = None

class RxNormTraitTypeDef(BaseModel):
    Name: Optional[RxNormTraitNameType] = None
    Score: Optional[float] = None

class RxNormConceptTypeDef(BaseModel):
    Description: Optional[str] = None
    Code: Optional[str] = None
    Score: Optional[float] = None

class SNOMEDCTConceptTypeDef(BaseModel):
    Description: Optional[str] = None
    Code: Optional[str] = None
    Score: Optional[float] = None

class SNOMEDCTTraitTypeDef(BaseModel):
    Name: Optional[SNOMEDCTTraitNameType] = None
    Score: Optional[float] = None

class StopEntitiesDetectionV2JobRequestRequestTypeDef(BaseModel):
    JobId: str

class StopICD10CMInferenceJobRequestRequestTypeDef(BaseModel):
    JobId: str

class StopPHIDetectionJobRequestRequestTypeDef(BaseModel):
    JobId: str

class StopRxNormInferenceJobRequestRequestTypeDef(BaseModel):
    JobId: str

class StopSNOMEDCTInferenceJobRequestRequestTypeDef(BaseModel):
    JobId: str

class AttributeTypeDef(BaseModel):
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

class ComprehendMedicalAsyncJobFilterTypeDef(BaseModel):
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmitTimeBefore: Optional[TimestampTypeDef] = None
    SubmitTimeAfter: Optional[TimestampTypeDef] = None

class ComprehendMedicalAsyncJobPropertiesTypeDef(BaseModel):
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

class StartEntitiesDetectionV2JobRequestRequestTypeDef(BaseModel):
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    LanguageCode: Literal["en"]
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    KMSKey: Optional[str] = None

class StartICD10CMInferenceJobRequestRequestTypeDef(BaseModel):
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    LanguageCode: Literal["en"]
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    KMSKey: Optional[str] = None

class StartPHIDetectionJobRequestRequestTypeDef(BaseModel):
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    LanguageCode: Literal["en"]
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    KMSKey: Optional[str] = None

class StartRxNormInferenceJobRequestRequestTypeDef(BaseModel):
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    LanguageCode: Literal["en"]
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    KMSKey: Optional[str] = None

class StartSNOMEDCTInferenceJobRequestRequestTypeDef(BaseModel):
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    LanguageCode: Literal["en"]
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    KMSKey: Optional[str] = None

class StartEntitiesDetectionV2JobResponseTypeDef(BaseModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartICD10CMInferenceJobResponseTypeDef(BaseModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartPHIDetectionJobResponseTypeDef(BaseModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartRxNormInferenceJobResponseTypeDef(BaseModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartSNOMEDCTInferenceJobResponseTypeDef(BaseModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopEntitiesDetectionV2JobResponseTypeDef(BaseModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopICD10CMInferenceJobResponseTypeDef(BaseModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopPHIDetectionJobResponseTypeDef(BaseModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopRxNormInferenceJobResponseTypeDef(BaseModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopSNOMEDCTInferenceJobResponseTypeDef(BaseModel):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ICD10CMAttributeTypeDef(BaseModel):
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

class RxNormAttributeTypeDef(BaseModel):
    Type: Optional[RxNormAttributeTypeType] = None
    Score: Optional[float] = None
    RelationshipScore: Optional[float] = None
    Id: Optional[int] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None
    Text: Optional[str] = None
    Traits: Optional[List[RxNormTraitTypeDef]] = None

class SNOMEDCTAttributeTypeDef(BaseModel):
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

class EntityTypeDef(BaseModel):
    Id: Optional[int] = None
    BeginOffset: Optional[int] = None
    EndOffset: Optional[int] = None
    Score: Optional[float] = None
    Text: Optional[str] = None
    Category: Optional[EntityTypeType] = None
    Type: Optional[EntitySubTypeType] = None
    Traits: Optional[List[TraitTypeDef]] = None
    Attributes: Optional[List[AttributeTypeDef]] = None

class UnmappedAttributeTypeDef(BaseModel):
    Type: Optional[EntityTypeType] = None
    Attribute: Optional[AttributeTypeDef] = None

class ListEntitiesDetectionV2JobsRequestRequestTypeDef(BaseModel):
    Filter: Optional[ComprehendMedicalAsyncJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListICD10CMInferenceJobsRequestRequestTypeDef(BaseModel):
    Filter: Optional[ComprehendMedicalAsyncJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListPHIDetectionJobsRequestRequestTypeDef(BaseModel):
    Filter: Optional[ComprehendMedicalAsyncJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListRxNormInferenceJobsRequestRequestTypeDef(BaseModel):
    Filter: Optional[ComprehendMedicalAsyncJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListSNOMEDCTInferenceJobsRequestRequestTypeDef(BaseModel):
    Filter: Optional[ComprehendMedicalAsyncJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeEntitiesDetectionV2JobResponseTypeDef(BaseModel):
    ComprehendMedicalAsyncJobProperties: ComprehendMedicalAsyncJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeICD10CMInferenceJobResponseTypeDef(BaseModel):
    ComprehendMedicalAsyncJobProperties: ComprehendMedicalAsyncJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePHIDetectionJobResponseTypeDef(BaseModel):
    ComprehendMedicalAsyncJobProperties: ComprehendMedicalAsyncJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRxNormInferenceJobResponseTypeDef(BaseModel):
    ComprehendMedicalAsyncJobProperties: ComprehendMedicalAsyncJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSNOMEDCTInferenceJobResponseTypeDef(BaseModel):
    ComprehendMedicalAsyncJobProperties: ComprehendMedicalAsyncJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEntitiesDetectionV2JobsResponseTypeDef(BaseModel):
    ComprehendMedicalAsyncJobPropertiesList: List[ComprehendMedicalAsyncJobPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListICD10CMInferenceJobsResponseTypeDef(BaseModel):
    ComprehendMedicalAsyncJobPropertiesList: List[ComprehendMedicalAsyncJobPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPHIDetectionJobsResponseTypeDef(BaseModel):
    ComprehendMedicalAsyncJobPropertiesList: List[ComprehendMedicalAsyncJobPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRxNormInferenceJobsResponseTypeDef(BaseModel):
    ComprehendMedicalAsyncJobPropertiesList: List[ComprehendMedicalAsyncJobPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSNOMEDCTInferenceJobsResponseTypeDef(BaseModel):
    ComprehendMedicalAsyncJobPropertiesList: List[ComprehendMedicalAsyncJobPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ICD10CMEntityTypeDef(BaseModel):
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

class RxNormEntityTypeDef(BaseModel):
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

class SNOMEDCTEntityTypeDef(BaseModel):
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

class DetectPHIResponseTypeDef(BaseModel):
    Entities: List[EntityTypeDef]
    PaginationToken: str
    ModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class DetectEntitiesResponseTypeDef(BaseModel):
    Entities: List[EntityTypeDef]
    UnmappedAttributes: List[UnmappedAttributeTypeDef]
    PaginationToken: str
    ModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class DetectEntitiesV2ResponseTypeDef(BaseModel):
    Entities: List[EntityTypeDef]
    UnmappedAttributes: List[UnmappedAttributeTypeDef]
    PaginationToken: str
    ModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class InferICD10CMResponseTypeDef(BaseModel):
    Entities: List[ICD10CMEntityTypeDef]
    PaginationToken: str
    ModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class InferRxNormResponseTypeDef(BaseModel):
    Entities: List[RxNormEntityTypeDef]
    PaginationToken: str
    ModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class InferSNOMEDCTResponseTypeDef(BaseModel):
    Entities: List[SNOMEDCTEntityTypeDef]
    PaginationToken: str
    ModelVersion: str
    SNOMEDCTDetails: SNOMEDCTDetailsTypeDef
    Characters: CharactersTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


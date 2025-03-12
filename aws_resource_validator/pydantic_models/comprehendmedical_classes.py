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


class DescribeEntitiesDetectionV2JobRequestTypeDef(BaseValidatorModel):
    JobId: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DescribeICD10CMInferenceJobRequestTypeDef(BaseValidatorModel):
    JobId: str


class DescribePHIDetectionJobRequestTypeDef(BaseValidatorModel):
    JobId: str


class DescribeRxNormInferenceJobRequestTypeDef(BaseValidatorModel):
    JobId: str


class DescribeSNOMEDCTInferenceJobRequestTypeDef(BaseValidatorModel):
    JobId: str


class ICD10CMTraitTypeDef(BaseValidatorModel):
    Name: Optional[ICD10CMTraitNameType] = None
    Score: Optional[float] = None


class ICD10CMConceptTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    Code: Optional[str] = None
    Score: Optional[float] = None


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


class StopEntitiesDetectionV2JobRequestTypeDef(BaseValidatorModel):
    JobId: str


class StopICD10CMInferenceJobRequestTypeDef(BaseValidatorModel):
    JobId: str


class StopPHIDetectionJobRequestTypeDef(BaseValidatorModel):
    JobId: str


class StopRxNormInferenceJobRequestTypeDef(BaseValidatorModel):
    JobId: str


class StopSNOMEDCTInferenceJobRequestTypeDef(BaseValidatorModel):
    JobId: str


class TimestampTypeDef(BaseValidatorModel):
    pass


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


class StartEntitiesDetectionV2JobRequestTypeDef(BaseValidatorModel):
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    LanguageCode: Literal["en"]
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    KMSKey: Optional[str] = None


class StartICD10CMInferenceJobRequestTypeDef(BaseValidatorModel):
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    LanguageCode: Literal["en"]
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    KMSKey: Optional[str] = None


class StartPHIDetectionJobRequestTypeDef(BaseValidatorModel):
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    LanguageCode: Literal["en"]
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    KMSKey: Optional[str] = None


class StartRxNormInferenceJobRequestTypeDef(BaseValidatorModel):
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    LanguageCode: Literal["en"]
    JobName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    KMSKey: Optional[str] = None


class StartSNOMEDCTInferenceJobRequestTypeDef(BaseValidatorModel):
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


class ListEntitiesDetectionV2JobsRequestTypeDef(BaseValidatorModel):
    Filter: Optional[ComprehendMedicalAsyncJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListICD10CMInferenceJobsRequestTypeDef(BaseValidatorModel):
    Filter: Optional[ComprehendMedicalAsyncJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListPHIDetectionJobsRequestTypeDef(BaseValidatorModel):
    Filter: Optional[ComprehendMedicalAsyncJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListRxNormInferenceJobsRequestTypeDef(BaseValidatorModel):
    Filter: Optional[ComprehendMedicalAsyncJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListSNOMEDCTInferenceJobsRequestTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListICD10CMInferenceJobsResponseTypeDef(BaseValidatorModel):
    ComprehendMedicalAsyncJobPropertiesList: List[ComprehendMedicalAsyncJobPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListPHIDetectionJobsResponseTypeDef(BaseValidatorModel):
    ComprehendMedicalAsyncJobPropertiesList: List[ComprehendMedicalAsyncJobPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListRxNormInferenceJobsResponseTypeDef(BaseValidatorModel):
    ComprehendMedicalAsyncJobPropertiesList: List[ComprehendMedicalAsyncJobPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListSNOMEDCTInferenceJobsResponseTypeDef(BaseValidatorModel):
    ComprehendMedicalAsyncJobPropertiesList: List[ComprehendMedicalAsyncJobPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class EntityTypeDef(BaseValidatorModel):
    pass


class DetectPHIResponseTypeDef(BaseValidatorModel):
    Entities: List[EntityTypeDef]
    PaginationToken: str
    ModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef


class UnmappedAttributeTypeDef(BaseValidatorModel):
    pass


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


class ICD10CMEntityTypeDef(BaseValidatorModel):
    pass


class InferICD10CMResponseTypeDef(BaseValidatorModel):
    Entities: List[ICD10CMEntityTypeDef]
    PaginationToken: str
    ModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef


class RxNormEntityTypeDef(BaseValidatorModel):
    pass


class InferRxNormResponseTypeDef(BaseValidatorModel):
    Entities: List[RxNormEntityTypeDef]
    PaginationToken: str
    ModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef


class SNOMEDCTEntityTypeDef(BaseValidatorModel):
    pass


class InferSNOMEDCTResponseTypeDef(BaseValidatorModel):
    Entities: List[SNOMEDCTEntityTypeDef]
    PaginationToken: str
    ModelVersion: str
    SNOMEDCTDetails: SNOMEDCTDetailsTypeDef
    Characters: CharactersTypeDef
    ResponseMetadata: ResponseMetadataTypeDef



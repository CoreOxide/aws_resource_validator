# qldb_session_classes

# AbortTransactionResultTypeDef

### TimingInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qldb_session_classes.TimingInformationTypeDef]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CommitTransactionRequestTypeDef

### TransactionId
- **Type**: <class 'str'>
- **Required**: Yes

### CommitDigest
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes


# CommitTransactionResultTypeDef

### TransactionId
- **Type**: typing.Optional[str]

### CommitDigest
- **Type**: typing.Optional[bytes]

### TimingInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qldb_session_classes.TimingInformationTypeDef]

### ConsumedIOs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qldb_session_classes.IOUsageTypeDef]


# EndSessionResultTypeDef

### TimingInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qldb_session_classes.TimingInformationTypeDef]


# ExecuteStatementRequestTypeDef

### TransactionId
- **Type**: <class 'str'>
- **Required**: Yes

### Statement
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qldb_session_classes.ValueHolderTypeDef]]


# ExecuteStatementResultTypeDef

### FirstPage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qldb_session_classes.PageTypeDef]

### TimingInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qldb_session_classes.TimingInformationTypeDef]

### ConsumedIOs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qldb_session_classes.IOUsageTypeDef]


# FetchPageRequestTypeDef

### TransactionId
- **Type**: <class 'str'>
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes


# FetchPageResultTypeDef

### Page
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qldb_session_classes.PageTypeDef]

### TimingInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qldb_session_classes.TimingInformationTypeDef]

### ConsumedIOs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qldb_session_classes.IOUsageTypeDef]


# IOUsageTypeDef

### ReadIOs
- **Type**: typing.Optional[int]

### WriteIOs
- **Type**: typing.Optional[int]


# PageTypeDef

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qldb_session_classes.ValueHolderTypeDef]]

### NextPageToken
- **Type**: typing.Optional[str]


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HostId
- **Type**: <class 'str'>
- **Required**: Yes

### HTTPStatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### HTTPHeaders
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RetryAttempts
- **Type**: <class 'int'>
- **Required**: Yes


# SendCommandRequestRequestTypeDef

### SessionToken
- **Type**: typing.Optional[str]

### StartSession
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qldb_session_classes.StartSessionRequestTypeDef]

### StartTransaction
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### EndSession
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### CommitTransaction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qldb_session_classes.CommitTransactionRequestTypeDef]

### AbortTransaction
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### ExecuteStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qldb_session_classes.ExecuteStatementRequestTypeDef]

### FetchPage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qldb_session_classes.FetchPageRequestTypeDef]


# SendCommandResultTypeDef

### StartSession
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_session_classes.StartSessionResultTypeDef'>
- **Required**: Yes

### StartTransaction
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_session_classes.StartTransactionResultTypeDef'>
- **Required**: Yes

### EndSession
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_session_classes.EndSessionResultTypeDef'>
- **Required**: Yes

### CommitTransaction
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_session_classes.CommitTransactionResultTypeDef'>
- **Required**: Yes

### AbortTransaction
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_session_classes.AbortTransactionResultTypeDef'>
- **Required**: Yes

### ExecuteStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_session_classes.ExecuteStatementResultTypeDef'>
- **Required**: Yes

### FetchPage
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_session_classes.FetchPageResultTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_session_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartSessionRequestTypeDef

### LedgerName
- **Type**: <class 'str'>
- **Required**: Yes


# StartSessionResultTypeDef

### SessionToken
- **Type**: typing.Optional[str]

### TimingInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qldb_session_classes.TimingInformationTypeDef]


# StartTransactionResultTypeDef

### TransactionId
- **Type**: typing.Optional[str]

### TimingInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qldb_session_classes.TimingInformationTypeDef]


# TimingInformationTypeDef

### ProcessingTimeMilliseconds
- **Type**: typing.Optional[int]


# ValueHolderTypeDef

### IonBinary
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]

### IonText
- **Type**: typing.Optional[str]



# Qldb Session Classes

# AbortTransactionResult

### TimingInformation
- **Type**: <class 'NoneType'>


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CommitTransactionRequest

### TransactionId
- **Type**: <class 'str'>
- **Required**: Yes

### CommitDigest
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes


# CommitTransactionResult

### TransactionId
- **Type**: typing.Optional[str]

### CommitDigest
- **Type**: typing.Optional[bytes]

### TimingInformation
- **Type**: <class 'NoneType'>

### ConsumedIOs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qldb_session.qldb_session_classes.IOUsage]


# EndSessionResult

### TimingInformation
- **Type**: <class 'NoneType'>


# ExecuteStatementRequest

### TransactionId
- **Type**: <class 'str'>
- **Required**: Yes

### Statement
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.qldb_session.qldb_session_classes.ValueHolder, aws_resource_validator.pydantic_models.qldb_session.qldb_session_classes.ValueHolderOutput]]]


# ExecuteStatementResult

### FirstPage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qldb_session.qldb_session_classes.Page]

### TimingInformation
- **Type**: <class 'NoneType'>

### ConsumedIOs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qldb_session.qldb_session_classes.IOUsage]


# FetchPageRequest

### TransactionId
- **Type**: <class 'str'>
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes


# FetchPageResult

### Page
- **Type**: <class 'NoneType'>

### TimingInformation
- **Type**: <class 'NoneType'>

### ConsumedIOs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qldb_session.qldb_session_classes.IOUsage]


# IOUsage

### ReadIOs
- **Type**: typing.Optional[int]

### WriteIOs
- **Type**: typing.Optional[int]


# Page

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qldb_session.qldb_session_classes.ValueHolderOutput]]

### NextPageToken
- **Type**: typing.Optional[str]


# ResponseMetadata

### RequestId
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

### HostId
- **Type**: typing.Optional[str]


# SendCommandRequest

### SessionToken
- **Type**: typing.Optional[str]

### StartSession
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qldb_session.qldb_session_classes.StartSessionRequest]

### StartTransaction
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### EndSession
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### CommitTransaction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qldb_session.qldb_session_classes.CommitTransactionRequest]

### AbortTransaction
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### ExecuteStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qldb_session.qldb_session_classes.ExecuteStatementRequest]

### FetchPage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qldb_session.qldb_session_classes.FetchPageRequest]


# SendCommandResult

### StartSession
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_session.qldb_session_classes.StartSessionResult'>
- **Required**: Yes

### StartTransaction
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_session.qldb_session_classes.StartTransactionResult'>
- **Required**: Yes

### EndSession
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_session.qldb_session_classes.EndSessionResult'>
- **Required**: Yes

### CommitTransaction
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_session.qldb_session_classes.CommitTransactionResult'>
- **Required**: Yes

### AbortTransaction
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_session.qldb_session_classes.AbortTransactionResult'>
- **Required**: Yes

### ExecuteStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_session.qldb_session_classes.ExecuteStatementResult'>
- **Required**: Yes

### FetchPage
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_session.qldb_session_classes.FetchPageResult'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_session.qldb_session_classes.ResponseMetadata'>
- **Required**: Yes


# StartSessionRequest

### LedgerName
- **Type**: <class 'str'>
- **Required**: Yes


# StartSessionResult

### SessionToken
- **Type**: typing.Optional[str]

### TimingInformation
- **Type**: <class 'NoneType'>


# StartTransactionResult

### TransactionId
- **Type**: typing.Optional[str]

### TimingInformation
- **Type**: <class 'NoneType'>


# TimingInformation

### ProcessingTimeMilliseconds
- **Type**: typing.Optional[int]


# ValueHolder

### IonBinary
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]

### IonText
- **Type**: typing.Optional[str]


# ValueHolderOutput

### IonBinary
- **Type**: typing.Optional[bytes]

### IonText
- **Type**: typing.Optional[str]



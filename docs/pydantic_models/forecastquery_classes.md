# Forecastquery Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataPointTypeDef

### Timestamp
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[float]


# ForecastTypeDef

### Predictions
- **Type**: typing.Optional[typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.forecastquery_classes.DataPointTypeDef]]]


# QueryForecastRequestRequestTypeDef

### ForecastArn
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### StartDate
- **Type**: typing.Optional[str]

### EndDate
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# QueryForecastResponseTypeDef

### Forecast
- **Type**: <class 'aws_resource_validator.pydantic_models.forecastquery_classes.ForecastTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecastquery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# QueryWhatIfForecastRequestRequestTypeDef

### WhatIfForecastArn
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### StartDate
- **Type**: typing.Optional[str]

### EndDate
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# QueryWhatIfForecastResponseTypeDef

### Forecast
- **Type**: <class 'aws_resource_validator.pydantic_models.forecastquery_classes.ForecastTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecastquery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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



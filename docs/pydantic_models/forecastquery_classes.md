# Forecastquery Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataPoint

### Timestamp
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[float]


# Forecast

### Predictions
- **Type**: typing.Optional[typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.forecastquery.forecastquery_classes.DataPoint]]]


# QueryForecastRequest

### ForecastArn
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### StartDate
- **Type**: typing.Optional[str]

### EndDate
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# QueryForecastResponse

### Forecast
- **Type**: <class 'aws_resource_validator.pydantic_models.forecastquery.forecastquery_classes.Forecast'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecastquery.forecastquery_classes.ResponseMetadata'>
- **Required**: Yes


# QueryWhatIfForecastRequest

### WhatIfForecastArn
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### StartDate
- **Type**: typing.Optional[str]

### EndDate
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# QueryWhatIfForecastResponse

### Forecast
- **Type**: <class 'aws_resource_validator.pydantic_models.forecastquery.forecastquery_classes.Forecast'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecastquery.forecastquery_classes.ResponseMetadata'>
- **Required**: Yes


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



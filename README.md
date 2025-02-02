
# AWS Resource Validator

![version](https://img.shields.io/github/v/release/CoreOxide/aws_resource_validator)
![PythonSupport](https://img.shields.io/static/v1?label=python&message=3.9-3.13&color=blue?style=flat-square&logo=python)
[![GitHub License](https://img.shields.io/github/license/CoreOxide/aws_resource_validator)](https://github.com/CoreOxide/aws_resource_validator/blob/main/LICENSE)]
![github-star-badge](https://img.shields.io/github/stars/CoreOxide/aws_resource_validator.svg?style=social)
![issues](https://img.shields.io/github/issues/CoreOxide/aws_resource_validator)

`aws_resource_validator` is a Python package that creates objects to validate, show constraints of common AWS resource names, and generate compatible patterns for tests. This helps ensure that AWS resource names comply with AWS naming rules and can be used for testing and validation purposes.

**[📜Documentation](https://coreoxide.github.io/aws_resource_validator/)** | **[Blogs website](https://alexy-grabov.medium.com/aws-resource-names-validation-and-generation-24ceb127e609)**

## Features

- **Validation**: Check if a given AWS resource name meets the AWS naming constraints.
- **Constraint Display**: Display constraints for different AWS resource names.
- **Pattern Generation**: Generate compatible patterns for AWS resource names for testing purposes.

## Installation

You can install the package via pip:

```sh
pip install aws_resource_validator
```

## Usage Example

Here's a simple example demonstrating how to use `aws_resource_validator`:

```python
from aws_resource_validator.class_definitions import Acm, class_registry

# Use type hint so that you can use `api_registry` with full class definitions
acm: Acm = class_registry.Acm

print(acm.Arn.pattern)
print(acm.Arn.type)
print(acm.Arn.validate("example-arn"))
print(acm.Arn.generate())
```

Using Pydantic models for boto3 models:

```python
import boto3

from aws_resource_validator.pydantic_models.dynamodb_classes import ListTablesOutputTypeDef

dynamodb = boto3.client('dynamodb')

def list_dynamo_tables() -> List[str]:
    return ListTablesOutputTypeDef(**dynamodb.list_tables()).TableNames


if __name__ == "__main__":
    tables: List[str] = list_dynamo_tables()
    print("DynamoDB Tables:", tables)
```


## Contributing

We welcome contributions from everyone. Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## Security

For information on reporting security vulnerabilities, please see our [SECURITY.md](SECURITY.md).

## Code of Conduct

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions, feel free to reach out to us:

- Alexy Grabov: [alexy.grabov@gmail.com](mailto:alexy.grabov@gmail.com) ![linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white&link=https://www.linkedin.com/in/alexygrabov)
- Yafit Tupman: [ytupman@gmail.com](mailto:ytupman@gmail.com) ![linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white&link=https://www.linkedin.com/in/yafit-tupman)

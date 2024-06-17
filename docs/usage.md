
# Usage

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

from api_registry_definitions import api_registry

# Now you can use `api_registry` with full class definitions
try:
    print(api_registry.Acm.arn.pattern)
    print(api_registry.Acm.arn.validate("example-arn"))
except AttributeError as e:
    print(e)

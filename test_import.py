from api_registry_definitions import api_registry, Acm

# Now you can use `api_registry` with full class definitions
acm: Acm = api_registry.Acm
try:
    print(acm.Arn.pattern)
    print(acm.arn.validate("example-arn"))
    print(acm.Arn.generate())
except AttributeError as e:
    print(e)

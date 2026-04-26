"""Container of :class:`~.APIObject` instances representing one AWS service."""

from __future__ import annotations

from collections.abc import Iterable, Iterator, Mapping
from types import MappingProxyType

from aws_resource_validator.core.api_object import APIObject
from aws_resource_validator.core.naming import to_pascal_case, to_snake_case


class Service:
    """A single AWS service, keyed by its API object names.

    API objects can be looked up by their original PascalCase name, by their
    snake_case equivalent, by dict-style indexing, or by attribute access.
    All four routes resolve through a single internal dict, avoiding the
    dynamic :func:`setattr` aliasing used by the previous implementation.
    """

    __slots__ = ("_aliases", "_api_objects", "_service_name")

    def __init__(self, name: str, api_objects: Iterable[APIObject] = ()) -> None:
        self._service_name = to_pascal_case(name)
        self._api_objects: dict[str, APIObject] = {}
        self._aliases: dict[str, str] = {}
        for obj in api_objects:
            self.add_api_object(obj)

    @property
    def service_name(self) -> str:
        """The service's canonical PascalCase name."""
        return self._service_name

    @property
    def api_objects(self) -> Mapping[str, APIObject]:
        """A read-only view of API objects keyed by their PascalCase names."""
        return MappingProxyType(self._api_objects)

    def add_api_object(self, *args: object) -> None:
        """Register an API object and build its snake_case alias.

        Accepts either ``add_api_object(api_object)`` (current) or the legacy
        ``add_api_object(name, api_object)`` form used by the previously
        committed ``class_definitions.py`` (the redundant name is discarded).
        The legacy form is dropped once Pipeline A regenerates that file.
        """
        if not args:
            raise TypeError("add_api_object requires at least one argument")
        obj = args[-1]
        if not isinstance(obj, APIObject):
            raise TypeError(f"expected APIObject, got {type(obj).__name__}")
        pascal = obj.name
        snake = to_snake_case(pascal)
        self._api_objects[pascal] = obj
        self._aliases[pascal] = pascal
        if snake != pascal:
            self._aliases[snake] = pascal

    def __getitem__(self, name: str) -> APIObject:
        canonical = self._aliases.get(name)
        if canonical is None:
            raise KeyError(name)
        return self._api_objects[canonical]

    def __contains__(self, name: object) -> bool:
        return isinstance(name, str) and name in self._aliases

    def __iter__(self) -> Iterator[str]:
        return iter(self._api_objects)

    def __len__(self) -> int:
        return len(self._api_objects)

    def __getattr__(self, name: str) -> APIObject:
        aliases: dict[str, str] = object.__getattribute__(self, "_aliases")
        if name in aliases:
            api_objects: dict[str, APIObject] = object.__getattribute__(self, "_api_objects")
            return api_objects[aliases[name]]
        raise AttributeError(f"{type(self).__name__!r} has no API object {name!r}")

    def __repr__(self) -> str:
        return f"{type(self).__name__}(name={self._service_name!r}, objects={len(self)})"

"""Type definitions for mdfy package."""

from __future__ import annotations
from typing import Union, Iterable

from .elements import MdElement

MdWritableItem = Union[str, MdElement]
MdContents = Union[MdWritableItem, Iterable["MdContents"]]

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional

from pydantic import BaseModel, Field


class ItemIndex:
    id: int
    project: str


Tag = str


class GlobalConfig(BaseModel):
    all_projects: List[str] = []
    items_counter: int = 0
    tags_index: Dict[Tag, ItemIndex]

    def increase_items_counter(self) -> None:
        self.items_counter += 1


class ItemState(str, Enum):
    NEW = "NEW"
    TODO = "TODO"
    DONE = "DONE"


class Item(BaseModel):
    id: int
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None
    state: ItemState = ItemState.NEW
    tags: List[Tag] = []
    title: str

    class Config:
        use_enum_values = True

class ItemWithProject(Item):
    project: str


class Data(BaseModel):
    created_at: datetime = Field(default_factory=datetime.now)
    items: List[Item] = []


DataPerProject = Dict[str, Data]

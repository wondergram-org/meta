from typing import List, Optional

from pydantic import BaseModel

from src.body.recent_changes import RecentChanges
from src.body.version import Version
from src.methods.method import Method
from src.objects.object import Object


class Body(BaseModel):
    version: Optional[Version] = None
    recent_changes: Optional[RecentChanges] = None
    methods: Optional[List[Method]] = None
    objects: Optional[List[Object]] = None

    def sorted_objects(self) -> List[Object]:
        return sorted(self.objects, key=lambda x: x.name)

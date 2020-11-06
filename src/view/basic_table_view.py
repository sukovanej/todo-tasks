from typing import List, Optional

from rich import print
from rich.console import Console
from rich.table import Table

from ..models import Data, Item
from ..time import get_time_difference

from .table import TableView
from .item_mixin import ItemMixin


class BasicTableView(TableView, ItemMixin):
    def _create_table(self) -> Table:
        table = Table()
        table.add_column("ID", justify="right", style="cyan", no_wrap=True)
        table.add_column("Title", style="magenta")
        table.add_column("Tags", style="red")
        table.add_column("Status")
        table.add_column("Created", justify="right", style="green")
        return table

    def _get_row(self, item: Item) -> List[str]:
        return super()._item_to_row(item)

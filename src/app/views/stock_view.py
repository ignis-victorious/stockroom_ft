#  ___________________
#  Import LIBRARIES
# from sqlite3 import Cursor

import flet as ft  # type: ignore
from flet import (  # type: ignore
    AppBar,
    Column,
    # Divider,
    Dropdown,
    ElevatedButton,
    IconButton,
    Icons,
    # ListTile,
    # ListView,
    Page,
    Row,
    Text,
    TextField,
)

#  Import FILES
# from ..models.database import get_connection

#  ___________________


class StockView:
    def __init__(self, page: Page) -> None:
        self.page: Page = page
        #  Producto: Product
        self.product_dropdown: Dropdown = Dropdown(label="Product", options=[])
        # #  Quantidade: Quantity
        self.product_quantity_field: TextField = TextField(label="Quantity")

    def build(self) -> None:
        self.page.controls.clear()  # pyright: ignore[reportOptionalMemberAccess]

        self.page.appbar = AppBar(
            #  Estoque: Stock
            title=Text(value="Stock", size=24, weight=ft.FontWeight.BOLD),
            leading=IconButton(icon=Icons.ARROW_BACK, on_click=lambda e: self._go_back()),
        )

        self.page.add(Text(value="Inside StockView - Why this will not display?"))

        self.page.add(
            Column(
                controls=[
                    self.product_dropdown,
                    # self.product_price,
                    self.product_quantity_field,
                    Row(
                        controls=[
                            ElevatedButton(
                                #  Entrada (Adicionar): Add a product
                                text="Add a product",
                                on_click=self._product_in,
                            ),
                            ElevatedButton(
                                #  Saida (Remover): Remove a product
                                text="Remove a product",
                                on_click=self._product_out,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    # Divider(),
                    #  Produtos cadastrados: Products registered
                    #     Text(value="Products registered", size=20, weight=ft.FontWeight.BOLD),
                    #     self.list_products_view,
                ],
                expand=True,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                scroll=ft.ScrollMode.AUTO,
            )
        )

        # self.products_list()
        # self.page.update()

    def _product_in(self, e: ft.ControlEvent): ...

    def _product_out(self, e: ft.ControlEvent): ...

    #  Função de recuar
    def _go_back(self) -> None:
        from app.views.home_view import HomeView

        home: HomeView = HomeView(page=self.page)
        home.build()

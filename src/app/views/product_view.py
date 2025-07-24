#  ___________________
#  Import LIBRARIES
import flet as ft  # type: ignore
from flet import AppBar, Column, ElevatedButton, IconButton, Icons, Page, Row, Text, TextField  # type: ignore

#  Import FILES
# from ..models.database import get_connection
#  ___________________


class ProdutsView:
    def __init__(self, page: Page) -> None:
        self.page = page
        # Nome do produto: Product's name
        self.product_name = TextField(label="Product's name")
        # Preço do produto: Product's Price
        self.product_price = TextField(label="Product's Price")
        # Quantidade do produto: Product's Quantity
        self.product_quantity = TextField(label="Product's Quantity")

    def build(self) -> None:
        self.page.controls.clear()

        self.page.appbar = AppBar(
            #  Cadastro de Produtos: Product registration
            title=Text(value="Product registration", size=24, weight=ft.FontWeight.BOLD),
            leading=IconButton(icon=Icons.ARROW_BACK, on_click=lambda e: self._go_back()),
        )

        self.page.add(
            Column(
                controls=[
                    self.product_name,
                    self.product_price,
                    self.product_quantity,
                    Row(
                        controls=[
                            ElevatedButton(
                                #  Cadastar produto: Product's registration
                                text="Product's registration",
                                on_click=self._register_product,
                            )
                        ]
                    ),
                ]
            )
        )

    # Função para cadastrar produto
    def _register_product(self, e: ft.ControlEvent): ...

    def _go_back(self) -> None:
        from app.views.home_view import HomeView

        home = HomeView(page=self.page)
        home.build()

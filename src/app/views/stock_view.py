#  ___________________
#  Import LIBRARIES

from sqlite3 import Cursor

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
from ..models.database import get_connection

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
                alignment=ft.MainAxisAlignment.CENTER,
                scroll=ft.ScrollMode.AUTO,
            )
        )

        # Função para pegar produtos banco de dados - Function to retrieve products from the database

        self._take_product()
        self.page.update()

    def _take_product(self) -> None:
        self.product_dropdown.options.clear()

        with get_connection() as conn:
            cursor: Cursor = conn.cursor()
            #  produtos: products
            cursor.execute("SELECT id, name FROM products")
            for id_product, name in cursor.fetchall():
                self.product_dropdown.options.append(ft.dropdown.Option(str(id_product), name))

        self.page.update()

    def _product_in(self, e: ft.ControlEvent) -> None:
        self._refresh_stock(product_in=True)

    def _product_out(self, e: ft.ControlEvent) -> None:
        self._refresh_stock(product_in=False)

    def _refresh_stock(self, product_in=True):
        id_product = self.product_dropdown.value

        if not id_product:
            # Selecione um produto!: Select a product!
            print("Select a product!")
            return

        try:
            quantity = int(self.product_quantity_field.value)
            if quantity <= 0:
                raise ValueError
        except:
            print("Digite uma quantidade válida!")
            return

        with get_connection() as conn:
            cursor: Cursor = conn.cursor()
            # produtos: products
            cursor.execute("SELECT quantity FROM products WHERE id = ?", (id_product))
            result = cursor.fetchone()

            if not result:
                #  Produto não encontrado!: Product not found!
                print("Product not found!")
                return

            current_quantity = result[0]
            new_quantity = current_quantity + quantity if product_in else current_quantity - quantity

            if new_quantity < 0:
                #  Quantidade insufuciente no estoque!: Insufficient quantity in stock
                print("Insufficient quantity in stock")
                return
            cursor.execute("UPDATE products SET quantity = ? WHERE id = ?", (new_quantity, id_product))
            conn.commit()

            #  Estoque atualizado com sucesso!: Inventory succesfully updated!
            print("Inventory succesfully updated!")
            self.product_quantity_field.value = ""
            self.page.update()

    #  Função de recuar
    def _go_back(self) -> None:
        from app.views.home_view import HomeView

        home: HomeView = HomeView(page=self.page)
        home.build()

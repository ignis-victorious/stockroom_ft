#  ___________________
#  Import LIBRARIES
from sqlite3 import Cursor

import flet as ft  # type: ignore
from flet import (  # type: ignore
    AppBar,
    Column,
    Divider,
    ElevatedButton,
    IconButton,
    Icons,
    ListTile,
    ListView,
    Page,
    Row,
    Text,
    TextField,
)

#  Import FILES
from ..models.database import get_connection

#  ___________________


class ProdutsView:
    def __init__(self, page: Page) -> None:
        self.page: Page = page
        # Nome do produto: Product's name
        self.product_name = TextField(label="Product's name")
        # Preço do produto: Product's Price
        self.product_price = TextField(label="Product's Price")
        # Quantidade do produto: Product's Quantity
        self.product_quantity = TextField(label="Product's Quantity")
        self.list_products_view = ListView()

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
                                #  Cadastar produto: Product's registration: Product registration function
                                text="Product's registration",
                                on_click=self._register_product,
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    Divider(),
                    #  Produtos cadastrados: Products registered
                    Text(value="Products registered", size=20, weight=ft.FontWeight.BOLD),
                    self.list_products_view,
                ],
                expand=True,
                scroll=ft.ScrollMode.AUTO,
            )
        )
        self.products_list()
        self.page.update()

    # Função para cadastrar produto
    def _register_product(self, e: ft.ControlEvent) -> None:
        name = self.product_name.value.strip()
        try:
            price = float(self.product_price.value.strip())
            quantity = int(self.product_quantity.value.strip())
        except:
            #  O preço e a quantidade devem ser números!: The price and quantity must be numbers!
            print("The price and quantity must be numbers!")
            return

        if not name:
            print("Preencha o nome do produto.")
            return

        with get_connection() as conn:
            cursor: Cursor = conn.cursor()
            # produtos: products
            cursor.execute("""INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)""", (name, price, quantity))
            conn.commit()

            #  Produto cadastrado com sucesso!: Product successfully registered!
            print("Product successfully registered!")

            self.product_name.value = ""
            self.product_price.value = ""
            self.product_quantity.value = ""
            self.product_list()
            self.page.update()

    def products_list(self) -> None:
        self.list_products_view.controls.clear()
        # self.list_products.controls.clear()
        with get_connection() as conn:
            cursor: Cursor = conn.cursor()
            #  produtos: products
            cursor.execute("SELECT name, price, quantity FROM products")
            for name, price, quantity in cursor.fetchall():
                self.list_products_view.controls.append(
                    ListTile(
                        title=Text(value=f"{name}"),
                        #  Preço: (price: 2f) MZN | Quantidade: [quantity} =
                        subtitle=Text(value=f"Price: {price: .2f} MZN | Quantity: {quantity}"),
                    )
                )
                self.page.update()

    def _go_back(self) -> None:
        from app.views.home_view import HomeView

        home: HomeView = HomeView(page=self.page)
        home: HomeView = HomeView(page=self.page)
        home.build()

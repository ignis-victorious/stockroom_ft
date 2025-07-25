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


class SupplierView:
    def __init__(self, page: Page) -> None:
        self.page: Page = page
        self.supplier_name = TextField(label="Supplier's name")  # None do fornecedor
        self.supplier_telephone = TextField(label="Supplier's telephone")  # Contato
        self.supplier_email = TextField(label="Supplier's email")  # Email
        self.list_supplier_view = ListView()

    def build(self) -> None:
        # self.page.controls.clear()

        self.page.appbar = AppBar(
            #  Fornecedores: Suppliers registration
            title=Text(value="Suppliers", size=24, weight=ft.FontWeight.BOLD),
            leading=IconButton(icon=Icons.ARROW_BACK, on_click=lambda e: self._go_back()),
        )

        self.page.add(
            Column(
                controls=[
                    self.supplier_name,
                    self.supplier_telephone,
                    self.supplier_email,
                    Row(
                        controls=[
                            ElevatedButton(
                                #  Cadastar fornecedores: Suppliers' registration:
                                text="Supplier's registration",
                                on_click=self._register_supplier,
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    Divider(),
                    #  Produtos cadastrados: Products registered
                    Text(value="Supplier registered", size=20, weight=ft.FontWeight.BOLD),
                    self.list_supplier_view,
                ],
                expand=True,
                scroll=ft.ScrollMode.AUTO,
            )
        )
        self.supplier_list()
        self.page.update()

    # Função para cadastrar produto
    def _register_supplier(self, e: ft.ControlEvent) -> None:
        name: str = self.supplier_name.value.strip()
        telephone: str = self.supplier_telephone.value.strip()
        email: str = self.supplier_email.value.strip()

        if not name or not telephone or not email:
            print("Preencha todos campos.")
            return

        with get_connection() as conn:
            cursor: Cursor = conn.cursor()
            # produtos: products
            cursor.execute(
                """INSERT INTO supplies (name, telephone, email) VALUES (?, ?, ?)""", (name, telephone, email)
            )
            conn.commit()

            #  Produto cadastrado com sucesso!: Product successfully registered!
            print("Product successfully registered!")

            self.supplier_name.value = ""
            self.supplier_telephone.value = ""
            self.supplier_email.value = ""
            self.supplier_list()
            self.page.update()

    def supplier_list(self) -> None:
        self.list_supplier_view.controls.clear()
        # self.list_products.controls.clear()
        with get_connection() as conn:
            cursor: Cursor = conn.cursor()
            #  produtos: products
            cursor.execute("SELECT name, telephone, email FROM suppliers")
            for name, telephone, email in cursor.fetchall():
                self.list_supplier_view.controls.append(
                    ListTile(
                        title=Text(value=f"{name}"),
                        #  Contacto: Contacts (price: 2f) MZN | Quantidade: [quantity} =
                        subtitle=Text(value=f"Contacts: {telephone} | Email: {email}"),
                    )
                )
                self.page.update()

    def _go_back(self) -> None:
        from app.views.home_view import HomeView

        home: HomeView = HomeView(page=self.page)
        home.build()

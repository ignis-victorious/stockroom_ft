#  ___________________
#  Import LIBRARIES
import flet as ft  # type: ignore
from flet import (  # type: ignore
    AppBar,
    Column,
    # Container,
    # FontWeight,
    IconButton,
    Icons,
    # NavigationDrawer,
    # NavigationDrawerDestination,
    Page,
    Text,
)

#  Import FILES
#  ___________________


class DashboardView:
    def __init__(self, page: Page) -> None:
        super().__init__()  # This class does not inherit from any Flet widget class it does NOT need to call super()
        self.page: Page = page
        self.chart = (
            ft.BarChart(
                expand=True,
                border=ft.border.all(1, color=ft.Colors.GREY),
                horizontal_grid_lines=ft.ChartGridLines(width=1),
                vertical_grid_lines=ft.ChartGridLines(width=1),
                left_axis=ft.ChartAxis(labels_size=40),
                bottom_axis=ft.ChartAxis(labels_size=40),
                tooltip_bgcolor=ft.Colors.with_opacity(0.8, ft.Colors.BLACK),
                max_y=100,
                bar_groups=[],
            ),
        )

        self.total_products_text = Text(size=24, weight=ft.FontWeight.BOLD)

    def build(self) -> None:
        self.page.controls.clear()  # type: ignore

        self.page.appbar = AppBar(
            #  Estoque: Stock
            title=Text(value="Stock", size=24, weight=ft.FontWeight.BOLD),
            leading=IconButton(icon=Icons.ARROW_BACK, on_click=lambda e: self._go_back()),
        )

        self.page.add(
            Column(
                controls=[
                    # Estoque atual: Current inventory
                    Text(value="Current inventory", size=30, weight=ft.FontWeight.BOLD),
                    self.total_products_text,
                    self.chart,
                ],
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                scroll=ft.ScrollMode.AUTO,
            )
        )
        self.page.update()

    # Função para pegar dados do nosso banco de dados
    def _take_data(self):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name, quantity FROM products")
            products = cursor.fetchall()

            # Actualizar o total de produtos
            total_products: int = len(products)
            self.total_products_text.value = f"Total de produtos: {total_products}"

    #  Função de recuar
    def _go_back(self) -> None:
        from app.views.home_view import HomeView

        home: HomeView = HomeView(page=self.page)
        home.build()

#  ___________________
#  Import LIBRARIES
from flet import (  # type: ignore
    AppBar,
    Column,
    Container,
    FontWeight,
    IconButton,
    Icons,
    NavigationDrawer,
    NavigationDrawerDestination,
    Page,
    Text,
)

#  Import FILES
#  ___________________


class HomeView:
    def __init__(self, page: Page) -> None:
        # super().__init__()  # This class does not inherit from any Flet widget class it does NOT need to call super()
        self.page: Page = page

    def build(self) -> None:
        self.page.controls.clear()

        self.page.drawer = NavigationDrawer(
            controls=[
                Container(height=50),
                # DashBoard: Dashboard, Produtos: Products, Fornecedores: Suppliers, Estoque: Stock / Inventory, Sair: exit,
                NavigationDrawerDestination(icon=Icons.HOME, label="DashBoard"),
                NavigationDrawerDestination(icon=Icons.INVENTORY, label="Products"),
                NavigationDrawerDestination(icon=Icons.LOCAL_SHIPPING, label="Suppliers"),
                NavigationDrawerDestination(icon=Icons.STORAGE, label="Inventory"),
                NavigationDrawerDestination(icon=Icons.LOGOUT, label="Exit"),
            ]
        )

        self.page.add(Text(value="Hello, Hello, Hello", size=28))

        self.page.appbar = AppBar(
            # Sistema de Gestão de Estoque: Stock Management System
            title=Text(
                value="Stock Management System",
                # value="Welcome to the Stock Management System",
                size=24,
                weight=FontWeight.BOLD,
            ),
            leading=IconButton(icon=Icons.MENU, on_click=lambda e: self._open_drawer()),
        )

        self.page.add(Text(value="Again Hello, Hello, Hello", size=28))

        self.page.add(
            Column(
                controls=[
                    Text(
                        # Bem vindo ao Sistema de Gestão de Estoque: Welcome to the Stock Management System
                        value="Welcome to the Stock Management System",
                        size=24,
                        weight=FontWeight.BOLD,
                    ),
                    #  Selecione uma copção no menu: Select an option from the menu
                    Text(value="Select an option from the menu", size=16),
                ]
            )
        )

        # Página Inicial: Starting page
        # self.page.controls.append(Text(value="Starting page", size=25))
        #

        self.page.add(Text(value="Near page.update(), Hello, Hello, Hello", size=28))

        self.page.update()

    def _open_drawer(self) -> None:
        self.page.drawer.open = True
        self.page.update()


# class HomeView:
#     def __init__(self, page: Page) -> None:
#         self.page: Page = page

#     def build(self) -> None:
#         # Assign the drawer first, so it's available when the AppBar's button is clicked
#         self.page.drawer = NavigationDrawer(
#             controls=[
#                 Container(height=50),
#                 NavigationBarDestination(icon=Icons.HOME, label="DashBoard"),
#                 NavigationBarDestination(icon=Icons.INVENTORY, label="Products"),
#                 NavigationBarDestination(icon=Icons.LOCAL_SHIPPING, label="Suppliers"),
#                 NavigationBarDestination(icon=Icons.STORAGE, label="Inventory"),
#                 NavigationBarDestination(icon=Icons.LOGOUT, label="Exit"),
#             ]
#         )

#         # Now, define the main controls for the page
#         self.page.controls = [
#             AppBar(
#                 title=Text(value="My Dashboard"),
#                 # CORRECTED LINE: Use setattr to assign True to the 'open' property
#                 leading=IconButton(icon=Icons.MENU, on_click=lambda e: setattr(self.page.drawer, "open", True)),
#                 actions=[IconButton(icon=Icons.INFO)],
#             ),
#             Text(value="Starting page content", size=25),
#         ]

#         # After opening/closing the drawer, you generally need to call self.page.update()
#         # to reflect the change in its 'open' property.
#         # This is often done *after* the drawer.open = True line within the on_click handler
#         # but in this setup where build() is called once, and update() is at the end,
#         # Flet often figures it out. However, if you add an on_dismiss, you'd update there.
#         self.page.update()  # This should now be fine once the lambda is fixed


# class HomeView:
#     def __init__(self, page: Page) -> None:
#         self.page: Page = page
#         # Initialize controls property as an empty list to prevent potential None issues
#         self.page.controls = []

#     def build(self) -> None:
#         # self.page.controls.clear()

#         self.page.controls = [
#             NavigationDrawer(
#                 controls=[
#                     Container(height=50),
#                     NavigationBarDestination(icon=Icons.HOME, label="DashBoard"),
#                     NavigationBarDestination(icon=Icons.INVENTORY, label="Products"),
#                     NavigationBarDestination(icon=Icons.LOCAL_SHIPPING, label="Suppliers"),
#                     NavigationBarDestination(icon=Icons.STORAGE, label="Inventory"),
#                     NavigationBarDestination(icon=Icons.LOGOUT, label="Exit"),
#                 ]
#             )
#         ]

#         self.page.update()  # This should now be fine

#  ___________________
#  Import LIBRARIES
import flet as ft  # type: ignore
from flet import Column, CrossAxisAlignment, MainAxisAlignment, Page  # type: ignore

#  Import FILES
#  ___________________


class LoginView:
    def __init__(self, page: Page):
        self.page: Page = page

    def build(self) -> None:
        self.page.controls.clear()
        # The error occurs because self.page.controls is likely None by default; you should assign a Column to self.page.controls instead of clearing and appending to it.
        self.page.controls.append(
            Column(
                controls=[
                    ft.Text(value="Login", size=24, weight=ft.FontWeight.BOLD),
                    # Usuário: Username
                    ft.TextField(label="Username"),
                    # Senha: Password
                    ft.TextField(
                        label="Password",
                        password=True,
                        can_reveal_password=False,
                    ),
                    # entrar no sistema: Log in / Sign in
                    ft.ElevatedButton(text="Sign in"),
                ],
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            )
        )
        self.page.update()

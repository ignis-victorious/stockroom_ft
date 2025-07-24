#  ___________________
#  Import LIBRARIES
import sqlite3

import flet as ft  # type: ignore
from flet import (  # type: ignore
    Column,
    ControlEvent,
    CrossAxisAlignment,
    ElevatedButton,
    MainAxisAlignment,
    Page,
    TextField,
)
from passlib.hash import pbkdf2_sha256

#  Import FILES
from ..models.database import get_connection

#  ___________________


class LoginView:
    def __init__(self, page: Page) -> None:
        self.page: Page = page
        self.username: TextField = TextField(label="Username")
        self.password: TextField = TextField(
            label="Password",
            password=True,
            can_reveal_password=False,
        )

        # Initialize controls property as an empty list to prevent potential None issues
        self.page.controls = []

    def build(self) -> None:
        # Instead of clearing, you can directly assign the new controls to self.page.controls
        # self.page.controls.clear()
        # If you want to clear previous content, ensure self.page.controls is a list first,
        # but in this setup, assigning a new list is often cleaner.
        self.page.controls = [  # Assign a new list containing your login UI
            # self.page.controls.append(
            # The error occurs because self.page.controls is likely None by default; you should assign a Column to self.page.controls instead of clearing and appending to it.
            Column(
                controls=[
                    ft.Text(value="Login", size=24, weight=ft.FontWeight.BOLD),
                    # Usuário: Username
                    # ft.TextField(label="Username"),
                    self.username,
                    # Senha: Password
                    # TextField(label="Password",password=True,can_reveal_password=False,),
                    self.password,
                    # entrar no sistema: Log in / Sign in
                    ElevatedButton(text="Sign in", on_click=self._handle_login),
                    # 'Cadastrar-se no sistema: Register in the system/Sign up for the system
                    ElevatedButton(text="Register", on_click=self._handle_register),
                ],
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            )
        ]
        self.page.update()  # pyright: ignore[reportUnknownMemberType]

        # Check if self.username.value exists before trying to access it

    def _handle_login(self, e: ControlEvent) -> None:
        # Initialize user and passw with empty strings to ensure they are always defined
        user: str = ""
        passw: str = ""

        # Check if self.username.value exists before trying to access it
        if self.username and self.username.value is not None:
            user: str = str(object=self.username.value).strip()  # Ensure it's a string

        # Check if self.password.value exists before trying to access it
        if self.password and self.password.value is not None:
            passw: str = str(object=self.password.value).strip()  # Ensure it's a string

        if not user or not passw:
            print("Please fill in all fields")
            # print("Preencha todos campos")
            return

        with get_connection() as conn:
            cursor: sqlite3.Cursor = conn.cursor()
            cursor.execute("SELECT password FROM users WHERE username = ?", (user,))
            result = cursor.fetchone()

            if result and pbkdf2_sha256.verify(passw, result[e]):
                print("Login successful!")
                # print('Login feito com sucesso! ')

                # Tela inicial - Home screen

            else:
                print("Incorrect username or password!")
                # print( 'Login ou senha incorretos!')

                # conn.commit

    def _handle_register(self, e: ControlEvent):
        user: str = ""
        passw: str = ""

        if self.username and self.username.value is not None:
            user: str = str(object=self.username.value).strip()  # Ensure it's a string
        if self.password and self.password.value is not None:
            passw: str = str(object=self.password.value).strip()  # Ensure it's a string

        if not user or not passw:
            print("Please fill in all fields")
            return

        hashed_password = pbkdf2_sha256.hash(secret=passw)

        try:
            with get_connection() as conn:
                cursor: sqlite3.Cursor = conn.cursor()
                cursor.execute(
                    " INSERT INTO users (username, password) VALUES (?, ?)",
                    (user, hashed_password),
                )
                conn.commit

                print("User registered successfully!")
                # print( 'Usuário cadastrado com sucesso!')

        except Exception as ex:
            print(f"Error registering: {ex}")
            # print(f'Erro ao cadastrar: {ex}')

#  ___________________
#  Import LIBRARIES
from flet import Page, app  # type: ignore

# from app.models.database import create_table
#  Import FILES
from app.views.auth_view import LoginView

#  ___________________


def main(page: Page) -> None:
    page.title = "Stock Manafement System"

    # create_table()  # This creates the Auth table

    # page.add(ft.Text(value="Hello", size=20))

    login_view = LoginView(page=page)
    login_view.build()


app(target=main)


# if __name__ == "__main__":
#     main()

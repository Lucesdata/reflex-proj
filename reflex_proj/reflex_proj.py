import reflex as rx

class State(rx.State):
    pass






def index() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Giovanny"
        )
    )


app = rx.App()
app.add_page(index)

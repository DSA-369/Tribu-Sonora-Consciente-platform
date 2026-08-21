import reflex as rx

from sound_healing_platform.components.layout import plantilla_tribu


def terminos_page() -> rx.Component:
    """Vista 'Términos y Condiciones'."""
    contenido = rx.center(
        rx.vstack(
            rx.heading(
                "Términos y Condiciones",
                size="7",
                color="#2C3639",
                font_weight="normal",
                style={"font-family": "Georgia, serif"},
                margin_bottom="20px"
            ),
            rx.vstack(
                rx.text(
                    "Bienvenido a Tribu Sonora Consciente. Al acceder y utilizar este sitio web, usted acepta cumplir con los siguientes términos y condiciones de uso.",
                    size="3",
                    color="#4B5563",
                    line_height="1.7"
                ),
                rx.heading("1. Reservas y Pagos", size="4", color="#2C3639", margin_top="15px"),
                rx.text(
                    "Las reservas para las sesiones grupales y talleres quedan confirmadas una vez que el pago correspondiente haya sido verificado por nuestro equipo.",
                    size="2",
                    color="#4B5563",
                    line_height="1.6"
                ),
                rx.heading("2. Cancelaciones y Reembolsos", size="4", color="#2C3639", margin_top="15px"),
                rx.text(
                    "Para reprogramaciones o solicitudes de cancelación, se requiere una notificación previa con al menos 24 horas de anticipación a la fecha agendada de la sesión.",
                    size="2",
                    color="#4B5563",
                    line_height="1.6"
                ),
                rx.heading("3. Propiedad Intelectual", size="4", color="#2C3639", margin_top="15px"),
                rx.text(
                    "Todo el contenido presente en este sitio, incluyendo marcas, imágenes, textos y diseño general, es propiedad exclusiva de Tribu Sonora Consciente y está protegido por las leyes de derecho de autor.",
                    size="2",
                    color="#4B5563",
                    line_height="1.6"
                ),
                align="start",
                spacing="3",
                width="100%"
            ),
            width="100%",
            max_width="850px",
            padding="30px",
            background_color="#FFFFFF",
            border_radius="12px",
            border="1px solid #EAE5DF",
            box_shadow="0px 2px 10px rgba(0,0,0,0.03)"
        ),
        width="100%",
        background_color="#FAF6F0",
        padding_y="50px"
    )
    return plantilla_tribu(contenido, pagina_activa="terminos")
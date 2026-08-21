import reflex as rx

from sound_healing_platform.components.layout import plantilla_tribu


def privacidad_page() -> rx.Component:
    """Vista 'Política de Privacidad'."""
    contenido = rx.center(
        rx.vstack(
            rx.heading(
                "Política de Privacidad",
                size="7",
                color="#2C3639",
                font_weight="normal",
                style={"font-family": "Georgia, serif"},
                margin_bottom="20px"
            ),
            rx.vstack(
                rx.text(
                    "En Tribu Sonora Consciente valoramos y respetamos la privacidad de nuestros usuarios y clientes. Esta política detalla la forma en que recopilamos, utilizamos y protegemos su información personal.",
                    size="3",
                    color="#4B5563",
                    line_height="1.7"
                ),
                rx.heading("1. Recopilación de Información", size="4", color="#2C3639", margin_top="15px"),
                rx.text(
                    "Recopilamos información personal únicamente cuando se registra voluntariamente en nuestra plataforma, solicita una reserva de sesión, adquiere productos en nuestra tienda o se suscribe a nuestro boletín de noticias.",
                    size="2",
                    color="#4B5563",
                    line_height="1.6"
                ),
                rx.heading("2. Uso de los Datos", size="4", color="#2C3639", margin_top="15px"),
                rx.text(
                    "Los datos proporcionados son utilizados exclusivamente para procesar sus reservas, gestionar pedidos, enviar actualizaciones relevantes sobre nuestras actividades y mejorar la experiencia de usuario en nuestro sitio web.",
                    size="2",
                    color="#4B5563",
                    line_height="1.6"
                ),
                rx.heading("3. Protección y Confidencialidad", size="4", color="#2C3639", margin_top="15px"),
                rx.text(
                    "No vendemos, alquilamos ni compartimos sus datos personales con terceros para fines comerciales. Implementamos medidas de seguridad administrativas y técnicas para salvaguardar su información.",
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
    return plantilla_tribu(contenido, pagina_activa="privacidad")
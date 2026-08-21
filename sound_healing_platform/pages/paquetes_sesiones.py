# sound_healing_platform/pages/paquetes_sesiones.py
import reflex as rx

from sound_healing_platform.components.layout import plantilla_tribu


def tarjeta_paquete(titulo: str, precio: str, frecuencia: str, caracteristicas: list[str], popular: bool = False) -> rx.Component:
    """Tarjeta comparativa de tarifas y paquetes de sesiones."""
    return rx.box(
        rx.vstack(
            rx.cond(
                popular,
                rx.box(
                    rx.text("MÁS POPULAR", size="1", font_weight="bold", color="#FFFFFF", letter_spacing="0.1em"),
                    background_color="#8E6F54",
                    padding="4px 12px",
                    border_radius="15px",
                    align_self="center",
                    margin_bottom="10px"
                )
            ),
            rx.heading(titulo, size="5", color="#2C3639", font_weight="normal", style={"font-family": "Georgia, serif"}),
            rx.hstack(
                rx.text("$", size="6", font_weight="bold", color="#2C3639"),
                rx.text(precio, size="8", font_weight="bold", color="#2C3639"),
                rx.text("USD", size="2", color="#7F7F7F"),
                spacing="1",
                align="baseline"
            ),
            rx.text(frecuencia, size="1", color="#8E6F54", font_weight="bold"),
            
            rx.divider(color_scheme="gray", margin_y="15px"),

            rx.vstack(
                *[
                    rx.hstack(
                        rx.icon(tag="check", size=16, color="#2E7D32"),
                        rx.text(item, size="2", color="#4B5563"),
                        spacing="2",
                        align="center"
                    )
                    for item in caracteristicas
                ],
                align="start",
                spacing="2",
                width="100%",
                margin_bottom="20px"
            ),

            rx.button(
                "Solicitar por WhatsApp",
                size="3",
                width="100%",
                background_color=rx.cond(popular, "#8E6F54", "#2C3639"),
                color="#FFFFFF",
                font_weight="bold",
                border_radius="25px",
                cursor="pointer",
                _hover={"opacity": "0.9"},
                on_click=rx.redirect(
                    f"https://wa.me/584241359530?text=¡Hola%20Tribu!%20✨%20Quiero%20solicitar%20información%20sobre%20el%20plan:%20*{titulo}*",
                    is_external=True
                )
            ),
            align="center",
            width="100%",
            spacing="2"
        ),
        background_color="#FFFFFF",
        border_radius="12px",
        border=rx.cond(popular, "2px solid #8E6F54", "1px solid #EAE5DF"),
        padding="30px 20px",
        box_shadow=rx.cond(popular, "0px 8px 30px rgba(142, 111, 84, 0.15)", "0px 2px 10px rgba(0,0,0,0.03)"),
        width=rx.breakpoints(initial="100%", md="31%"),
        position="relative"
    )

def paquetes_sesiones_page() -> rx.Component:
    """Vista Principal 'Precios, Paquetes y Membresías'."""
    contenido = rx.center(
        rx.vstack(
            rx.vstack(
                rx.heading(
                    "Precios, Paquetes y Membresías",
                    size="8",
                    color="#2C3639",
                    font_weight="normal",
                    text_align="center",
                    style={"font-family": "Georgia, serif"},
                    margin_bottom="12px"
                ),
                rx.text(
                    "Elige la modalidad que mejor se adapte a tu ritmo de práctica personal o familiar.",
                    size=rx.breakpoints(initial="2", md="3"),
                    color="#7F7F7F",
                    text_align="center",
                    max_width="750px",
                    margin_bottom="45px"
                ),
                align="center",
                width="100%"
            ),

            rx.flex(
                tarjeta_paquete(
                    titulo="Gota Individual",
                    precio="20",
                    frecuencia="Acceso a 1 Sesión",
                    caracteristicas=[
                        "Valido en cualquier sede activa",
                        "Materiales e instrumentos incluidos",
                        "Atención personalizada",
                        "Reserva con 24h de anticipación"
                    ],
                    popular=False
                ),
                tarjeta_paquete(
                    titulo="Pack 4 Frecuencias",
                    precio="68",
                    frecuencia="4 Sesiones / Ahorras 12$ USD",
                    caracteristicas=[
                        "4 Pases de Sound Healing",
                        "Transferible a acompañantes",
                        "Vigencia de 60 días",
                        "Prioridad en lista de reserva",
                        "Descuento en la tienda virtual"
                    ],
                    popular=True
                ),
                tarjeta_paquete(
                    titulo="Membresía Pase Libre",
                    precio="99",
                    frecuencia="Mensual Ilimitado",
                    caracteristicas=[
                        "Acceso a todas las sedes del mes",
                        "Pase de invitado mensual gratuito",
                        "10% OFF en Talleres y Tienda",
                        "Acceso al canal privado de meditación"
                    ],
                    popular=False
                ),
                flex_direction=rx.breakpoints(initial="column", md="row"),
                justify="between",
                align_items="stretch",
                gap="20px",
                width="100%"
            ),
            width="100%",
            max_width="1150px",
            padding_x=rx.breakpoints(initial="10px", sm="20px"),
            padding_y="40px"
        ),
        width="100%",
        background_color="#FAF6F0"
    )
    return plantilla_tribu(contenido, pagina_activa="sesiones")
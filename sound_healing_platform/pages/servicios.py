# sound_healing_platform/pages/servicios.py
import reflex as rx

from sound_healing_platform.components.layout import plantilla_tribu
from sound_healing_platform.state import State


def tarjeta_servicio(servicio: rx.Var) -> rx.Component:
    """Tarjeta minimalista estilo editorial con esquinas cuadradas originales y zoom fluido."""
    return rx.box(
        rx.vstack(
            # 1. 🖼️ CONTENEDOR DE IMAGEN INTEGRADA CUADRADA ORIGINAL
            rx.box(
                rx.image(
                    src=servicio["foto"],
                    width="100%",
                    height="180px",
                    object_fit="cover",
                    border_radius="0px",  # Esquinas totalmente cuadradas
                    transition="transform 0.4s ease-in-out",
                    _hover={"transform": "scale(1.06)"},
                    cursor="pointer"
                ),
                width="100%",
                overflow="hidden",
                border_radius="0px"
            ),
            
            # 2. 📝 CONTENEDOR DE TEXTO
            rx.vstack(
                rx.heading(
                    servicio["nombre"],
                    size="5",
                    color="#2C3639",
                    font_weight="normal",
                    style={"font-family": "Georgia, serif"},
                    margin_top="4px",
                    margin_bottom="4px"
                ),
                rx.text(
                    servicio["descripcion"],
                    size="1",
                    color="#788392",
                    line_height="1.6",
                    font_weight="400"
                ),
                # 📲 BOTÓN / ENLACE DE ACCIÓN MINIMALISTA "Reserva ahora ->"
                rx.hstack(
                    rx.text(
                        "Reserva ahora",
                        size="2",
                        font_weight="bold",
                        color="#8E6F54",
                        style={"font-family": "Georgia, serif"}
                    ),
                    rx.icon(tag="arrow_right", size=15, color="#8E6F54"),
                    spacing="2",
                    align="center",
                    cursor="pointer",
                    margin_top="10px",
                    _hover={
                        "opacity": "0.75",
                        "transform": "translateX(3px)",
                        "transition": "all 0.2s ease-in-out"
                    },
                    on_click=rx.redirect(
                        f"https://wa.me/584241359530?text=¡Hola%20Tribu%20Sonora!%20✨%20Quisiera%20solicitar%20información%20y%20agendar%20una%20sesión%20de:%20*{servicio['nombre']}*",
                        is_external=True
                    )
                ),
                align="start",
                spacing="2",
                padding="16px 20px 20px 20px",
                width="100%"
            ),
            spacing="0",
            width="100%"
        ),
        background_color="#FFFFFF",
        border_radius="0px",  # Esquinas cuadradas en el contenedor principal
        box_shadow="0px 4px 20px rgba(0, 0, 0, 0.04)",
        border="1px solid #EAE5DF",
        width="100%"
    )

def servicios_page() -> rx.Component:
    """Vista Principal del Módulo 'Tipo de Servicios'."""
    contenido = rx.center(
        rx.vstack(
            rx.vstack(
                # Cabecera / Título de Sección
                rx.heading(
                    "Nuestros Servicios",
                    size="8",
                    color="#2C3639",
                    font_weight="normal",
                    text_align="center",
                    style={"font-family": "Georgia, serif"},
                    margin_bottom="12px"
                ),
                
                # Subtítulo: Adaptable a cualquier pantalla sin desbordamiento
                rx.text(
                    "Experiencias diseñadas para facilitar estados meditativos profundos y la restauración energética integral.",
                    size=rx.breakpoints(initial="2", md="3"),
                    color="#7F7F7F",
                    text_align="center",
                    max_width="750px",
                    margin_bottom="45px"
                ),
                
                # 🧱 GRID DE 3 COLUMNAS ESTRICTAS (Garantiza 3 de 3 en PC/MD sin caer en 2 por 2)
                rx.grid(
                    rx.foreach(
                        State.servicios_tribu,
                        tarjeta_servicio
                    ),
                    columns=rx.breakpoints(initial="1", sm="1", md="3"),
                    spacing="6",
                    width="100%"
                ),
                width="100%",
                align="center",
                padding_y="30px"
            ),
            width="100%",
            max_width="1200px",
            padding_x=rx.breakpoints(initial="12px", sm="20px")
        ),
        width="100%",
        background_color="#FAF6F0",
        padding_y="50px"
    )
    return plantilla_tribu(contenido, pagina_activa="servicios")
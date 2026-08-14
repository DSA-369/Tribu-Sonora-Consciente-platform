# sound_healing_platform/pages/detalle_guia.py
import reflex as rx
from sound_healing_platform.state import State
from sound_healing_platform.components.layout import plantilla_tribu

def detalle_guia_page() -> rx.Component:
    return plantilla_tribu(
        rx.center(
            rx.vstack(
                # Botón de retorno minimalista
                rx.link(
                    rx.hstack(
                        rx.icon(tag="arrow-left", size=14, color="#7F7F7F"),
                        rx.text("Volver a Acerca de", size="2", color="#7F7F7F", font_weight="medium"),
                        spacing="1", align="center"
                    ),
                    href="/acerca-de#guias",
                    text_decoration="none",
                    margin_bottom="40px",
                    align_self="start"
                ),
                
                # Flex de Dos Columnas (Foto Izquierda - Biografía Derecha)
                rx.flex(
                    # Columna de Foto Rectangular Completa
                    rx.center(
                        rx.image(
                            src=State.selected_guide["foto"], 
                            width="100%", 
                            max_width="420px", 
                            height="auto", 
                            object_fit="cover", 
                            border_radius="0px"
                        ),
                        width=rx.breakpoints(initial="100%", md="45%"),
                        padding="10px"
                    ),
                    
                    # Columna de Texto
                    rx.vstack(
                        rx.heading(
                            State.selected_guide["nombre"], 
                            size="8", 
                            color="#2C3639", 
                            font_weight="light", 
                            style={"font-family": "Georgia, serif"}
                        ),
                        rx.text(
                            State.selected_guide["descripcion"], 
                            size="2", 
                            color="#A27B5C", 
                            text_transform="uppercase", 
                            letter_spacing="0.15em", 
                            font_weight="medium",
                            margin_top="5px",
                            margin_bottom="25px",
                            style={"font-family": "Georgia, serif"}
                        ),
                        rx.text(
                            State.selected_guide["biografia"], 
                            size="3", 
                            color="#4B5563", 
                            line_height="1.8", 
                            white_space="pre-line", # Respeta saltos de línea de la DB
                            style={"font-family": "Georgia, serif"}
                        ),
                        width=rx.breakpoints(initial="100%", md="55%"),
                        align_items="start",
                        text_align="left",
                        padding_x=rx.breakpoints(initial="10px", md="30px"),
                        padding_y="10px"
                    ),
                    
                    flex_direction=rx.breakpoints(initial="column", md="row"),
                    align_items="start",
                    gap="8",
                    width="100%"
                ),
                width="100%", max_width="950px", align="center", padding_x="20px"
            ),
            width="100%", padding_y="80px", background_color="#FAF6F0"
        ),
        pagina_activa="acerca_de"
    )
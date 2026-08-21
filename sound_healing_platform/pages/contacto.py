# sound_healing_platform/pages/contacto.py
import reflex as rx

from sound_healing_platform.components.layout import plantilla_tribu
from sound_healing_platform.state import State


def contacto_page() -> rx.Component:
    return plantilla_tribu(
        rx.vstack(
            # Bloque Formulario de Contacto
            rx.center(
                rx.vstack(
                    rx.heading("CONTÁCTANOS", size="8", color="#2C3639", font_weight="light", letter_spacing="0.1em", style={"font-family": "Georgia, serif"}),
                    rx.text("Nos encantaría saber de ti. Si tienes alguna pregunta, solicitud de reserva o simplemente quieres saludarnos, nuestras puertas siempre están abiertas.", size="3", color="#7F7F7F", text_align="center", max_width="650px", margin_top="10px", margin_bottom="30px"),
                    rx.flex(
                        rx.input(placeholder="Nombre", value=State.nombre, on_change=State.asignar_nombre, variant="surface", size="3", flex="1"),
                        rx.input(placeholder="Correo electrónico *", value=State.correo, on_change=State.asignar_correo, variant="surface", size="3", flex="1"),
                        width="100%", gap="4", flex_direction=rx.breakpoints(initial="column", sm="row"),
                    ),
                    rx.input(placeholder="Número de teléfono", value=State.telefono, on_change=State.asignar_telefono, variant="surface", size="3", width="100%", margin_y="15px"),
                    rx.text_area(placeholder="Comentario", value=State.comentario, on_change=State.asignar_comentario, variant="surface", size="3", width="100%", height="120px"),
                    rx.button("Enviar", background_color="#8E6F54", color="#FFFFFF", size="3", padding_x="40px", margin_top="20px", cursor="pointer", _hover={"background_color": "#73573F"}, on_click=State.enviar_formulario),
                    width="100%", max_width="750px", align="center", padding_x="20px"
                ),
                width="100%", padding_y="60px", background_color="#FAF6F0",
            ),
            # Bloque Datos de Contacto Reales
            rx.center(
                rx.vstack(
                    rx.heading("CONTÁCTANOS", size="7", color="#2C3639", font_weight="normal", letter_spacing="0.05em", style={"font-family": "Georgia, serif"}, margin_bottom="10px"),
                    rx.text("Canales directos de atención telefónica y soporte de la Tribu", size="2", color="#7F7F7F", margin_bottom="30px"),
                    rx.flex(
                        rx.vstack(rx.text("Danibeth García", size="3", font_weight="bold", color="#2C3639"), rx.text("+58 424-1359530", size="3", color="#7F7F7F"), align="center", bg="rgba(142, 111, 84, 0.03)", padding="20px", border_radius="6px", min_width="220px", border="1px solid #EAE5DF"),
                        rx.vstack(rx.text("Jarold Gonzalez", size="3", font_weight="bold", color="#2C3639"), rx.text("+58 412-0116355", size="3", color="#7F7F7F"), align="center", bg="rgba(142, 111, 84, 0.03)", padding="20px", border_radius="6px", min_width="220px", border="1px solid #EAE5DF"),
                        rx.vstack(rx.text("Jesús Buraglia", size="3", font_weight="bold", color="#2C3639"), rx.text("+58 412-3445369", size="3", color="#7F7F7F"), align="center", bg="rgba(142, 111, 84, 0.03)", padding="20px", border_radius="6px", min_width="220px", border="1px solid #EAE5DF"),
                        gap="5", flex_wrap="wrap", justify="center", width="100%"
                    ),
                    rx.link(rx.button("WhatsApp Directo", size="3", background_color="#8E6F54", color="#FFFFFF", font_weight="bold", margin_top="35px", padding_x="30px", cursor="pointer", _hover={"background_color": "#73573F"}), href="https://wa.link/hx4w38", is_external=True),
                    width="100%", max_width="900px", align="center", padding_x="20px"
                ),
                width="100%", padding_y="50px", background_color="#FAF6F0", border_top="1px solid #EAE5DF"
            ),
            # Franja de Preguntas Frecuentes
            rx.vstack(
                rx.heading("PREGUNTAS FRECUENTES", size="7", color="#FFFFFF", font_weight="light", letter_spacing="0.1em", style={"font-family": "Georgia, serif"}, margin_bottom="40px"),
                rx.flex(
                    rx.vstack(
                        rx.heading("¿Qué debo llevar?", size="4", color="#FFFFFF", font_weight="medium", margin_bottom="10px", style={"font-family": "Georgia, serif"}),
                        rx.vstack(
                            rx.text("• Ropa cómoda", color="#F3EFEA", size="2"),
                            rx.text("• Agua personal para hidratarse", color="#F3EFEA", size="2"),
                            rx.text("• Mat o Esterilla", color="#F3EFEA", size="2"),
                            rx.text("• Manta o cobija", color="#F3EFEA", size="2"),
                            rx.text("• Antifaz/Tapa ojos", color="#F3EFEA", size="2"),
                            rx.text("• Almohada o cojín pequeño", color="#F3EFEA", size="2"),
                            align="start", spacing="1"
                        ),
                        width=rx.breakpoints(initial="100%", md="45%"), align="start", padding="20px"
                    ),
                    rx.vstack(
                        rx.heading("¿A qué hora debo llegar?", size="4", color="#FFFFFF", font_weight="medium", margin_bottom="10px", style={"font-family": "Georgia, serif"}),
                        rx.text("Recomendamos llegar 15 minutos antes para acomodarse en el sitio.", color="#F3EFEA", size="2", line_height="1.6"),
                        width=rx.breakpoints(initial="100%", md="45%"), align="start", padding="20px"
                    ),
                    width="100%", max_width="1100px", flex_direction=rx.breakpoints(initial="column", md="row"), justify_content="space-around", align_items="start", gap="30px"
                ),
                width="100%", padding_y="60px", background_color="#966F53", align="center", 
            ),
            spacing="0", width="100%",
        ),
        pagina_activa="contacto" # Parámetro asignado
    )
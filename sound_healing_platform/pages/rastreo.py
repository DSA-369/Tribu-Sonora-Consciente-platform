# sound_healing_platform/pages/rastreo.py
import reflex as rx
from sound_healing_platform.state import State
from sound_healing_platform.components.layout import plantilla_tribu


def badge_estado_orden(estado: rx.Var) -> rx.Component:
    """Renderiza un badge de color según el estado de la orden en Supabase."""
    return rx.match(
        estado,
        ("PENDING_VERIFICATION", rx.badge("🟡 En Verificación de Pago", color_scheme="yellow", size="2")),
        ("VERIFIED", rx.badge("🟢 Pago Confirmado", color_scheme="green", size="2")),
        ("PROCESSING", rx.badge("🔵 En Preparación", color_scheme="blue", size="2")),
        ("SHIPPED", rx.badge("🚚 Enviado / Listo", color_scheme="purple", size="2")),
        ("COMPLETED", rx.badge("✨ Completado", color_scheme="gray", size="2")),
        ("CANCELLED", rx.badge("🔴 Cancelado", color_scheme="red", size="2")),
        rx.badge("🟡 En Revisión", color_scheme="yellow", size="2")
    )


def tarjeta_orden(orden: rx.Var) -> rx.Component:
    """Renderiza los detalles visuales de una orden encontrada."""
    return rx.vstack(
        rx.hstack(
            rx.vstack(
                rx.hstack(
                    rx.text("Orden Ref:", size="2", font_weight="bold", color="#2C3639"),
                    rx.text(orden["numero_referencia"], size="2", font_weight="bold", color="#8E6F54"),
                    spacing="2"
                ),
                rx.text(f"Cliente: {orden['cliente_nombre']} {orden['cliente_apellido']}", size="2", color="#4A5568"),
                align="start",
                spacing="1"
            ),
            badge_estado_orden(orden["estado"]),
            justify="between",
            align="center",
            width="100%"
        ),
        
        rx.divider(color_scheme="gray", margin_y="10px"),
        
        rx.hstack(
            rx.vstack(
                rx.text("Método de Pago:", size="1", color="#7F7F7F"),
                rx.text(orden["metodo_pago"], size="2", font_weight="medium", color="#2C3639"),
                align="start",
                spacing="0"
            ),
            rx.vstack(
                rx.text("Total Pagado:", size="1", color="#7F7F7F"),
                rx.text(f"${orden['monto_total']} USD", size="3", font_weight="bold", color="#2C3639"),
                align="end",
                spacing="0"
            ),
            justify="between",
            align="center",
            width="100%"
        ),
        
        padding="20px",
        border="1.5px solid #EAE5DF",
        border_radius="12px",
        background_color="#FAF6F0",
        width="100%",
        spacing="3"
    )


def rastreo_page() -> rx.Component:
    """Vista pública de rastreo de pedidos por número de referencia y contacto."""
    input_style = {
        "size": "3",
        "border_radius": "8px",
        "border": "1.5px solid #718096",
        "background_color": "#FFFFFF",
        "color": "#2C3639",
        "font_weight": "500",
        "width": "100%"
    }

    contenido = rx.center(
        rx.vstack(
            rx.vstack(
                rx.heading("Rastrear mi Orden ✨", size="7", color="#2C3639", font_weight="bold"),
                rx.text(
                    "Consulta el estado en tiempo real de tu compra ingresando tu número de contacto y la referencia de pago.",
                    size="3",
                    color="#4A5568",
                    text_align="center"
                ),
                align="center",
                spacing="2",
                max_width="600px"
            ),
            
            # Formulario de Búsqueda
            rx.vstack(
                rx.vstack(
                    rx.text("Correo electrónico o WhatsApp*", size="1", font_weight="bold", color="#2C3639"),
                    rx.input(
                        placeholder="ejemplo@correo.com o +58412...",
                        value=State.rastreo_contacto,
                        on_change=State.set_rastreo_contacto,
                        **input_style
                    ),
                    spacing="1",
                    align="start",
                    width="100%"
                ),
                rx.vstack(
                    rx.text("Número de Referencia / Confirmación*", size="1", font_weight="bold", color="#2C3639"),
                    rx.input(
                        placeholder="Ej. 894123",
                        value=State.rastreo_referencia,
                        on_change=State.set_rastreo_referencia,
                        **input_style
                    ),
                    spacing="1",
                    align="start",
                    width="100%"
                ),
                rx.button(
                    rx.hstack(
                        rx.icon(tag="search", size=18),
                        rx.text("Buscar Orden", font_weight="bold"),
                        spacing="2"
                    ),
                    on_click=State.buscar_orden_rastreo,
                    width="100%",
                    height="48px",
                    background_color="#2C3639",
                    color="#FFFFFF",
                    border_radius="30px",
                    cursor="pointer",
                    _hover={"background_color": "#8E6F54"}
                ),
                padding="30px",
                background_color="#FFFFFF",
                border="1.5px solid #EAE5DF",
                border_radius="16px",
                box_shadow="0px 4px 20px rgba(0,0,0,0.05)",
                width="100%",
                max_width="500px",
                spacing="4"
            ),
            
            # Área de Resultados
            rx.cond(
                State.busqueda_realizada,
                rx.cond(
                    State.ordenes_encontradas.length() > 0,
                    rx.vstack(
                        rx.heading("Órdenes Encontradas", size="4", color="#2C3639", font_weight="bold"),
                        rx.foreach(
                            State.ordenes_encontradas,
                            lambda ord: tarjeta_orden(ord)
                        ),
                        width="100%",
                        max_width="500px",
                        spacing="3"
                    ),
                    rx.box(
                        rx.text("🔍 No se encontraron órdenes que coincidan con estos datos. Verifica tu correo/teléfono y número de referencia.", color="#7F7F7F", text_align="center"),
                        padding="20px",
                        background_color="#FAF6F0",
                        border_radius="12px",
                        width="100%",
                        max_width="500px"
                    )
                )
            ),
            
            spacing="6",
            padding_y="60px",
            padding_x="20px",
            width="100%",
            align="center"
        ),
        width="100%",
        background_color="#FDFBF9"
    )
    return plantilla_tribu(contenido, pagina_activa="rastreo")
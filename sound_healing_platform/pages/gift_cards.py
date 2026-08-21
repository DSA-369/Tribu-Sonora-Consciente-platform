import reflex as rx

from sound_healing_platform.components.layout import plantilla_tribu
from sound_healing_platform.state import State


def vista_previa_voucher_experiencia() -> rx.Component:
    """Componente visual del Voucher de Experiencia para previsualización en vivo."""
    return rx.box(
        rx.vstack(
            # 1. Cabecera con Logo Oficial y Distintivo Editorial
            rx.vstack(
                rx.image(
                    src="https://ufjkeqqwgyauzujrbfcv.supabase.co/storage/v1/object/public/portfolio/logo%20tribu.png",
                    width="140px",
                    height="auto",
                    alt="Tribu Sonora Consciente Logo"
                ),
                rx.heading(
                    "TRIBU SONORA CONSCIENTE",
                    size="3",
                    letter_spacing="0.18em",
                    color="#2C3639",
                    font_weight="light",
                    margin_top="6px"
                ),
                rx.text(
                    "VOUCHER DE EXPERIENCIA HOLÍSTICA",
                    size="1",
                    letter_spacing="0.2em",
                    color="#8E6F54",
                    font_weight="bold",
                    margin_top="2px"
                ),
                align="center",
                spacing="0",
                width="100%"
            ),

            rx.divider(color_scheme="gray", margin_y="18px"),

            # 2. Cuerpo Central del Voucher (Cinta de Experiencia y Dedicatoria)
            rx.vstack(
                rx.box(
                    rx.vstack(
                        rx.text("EXPERIENCIA REGALADA", size="1", color="#A27B5C", font_weight="bold", letter_spacing="0.1em"),
                        rx.text(
                            State.gc_experiencia_seleccionada,
                            size="4",
                            color="#2C3639",
                            font_weight="normal",
                            style={"font-family": "Georgia, serif"},
                            text_align="center"
                        ),
                        rx.text(
                            f"VALOR: ${State.gc_monto_experiencia} USD",
                            size="2",
                            color="#8E6F54",
                            font_weight="bold"
                        ),
                        align="center",
                        spacing="1"
                    ),
                    background_color="#F4EBE1",
                    border="1px dashed #A27B5C",
                    padding="16px 20px",
                    width="100%",
                    border_radius="6px"
                ),

                rx.hstack(
                    rx.vstack(
                        rx.text("PARA:", size="1", color="#7F7F7F", font_weight="bold"),
                        rx.text(
                            rx.cond(State.gc_para_nombre != "", State.gc_para_nombre, "Nombre del Destinatario"),
                            size="3",
                            color="#2C3639",
                            font_weight="bold",
                            style={"font-family": "Georgia, serif"}
                        ),
                        align="start",
                        spacing="0"
                    ),
                    rx.vstack(
                        rx.text("DE:", size="1", color="#7F7F7F", font_weight="bold"),
                        rx.text(
                            rx.cond(State.gc_de_nombre != "", State.gc_de_nombre, "Tu Nombre"),
                            size="3",
                            color="#2C3639",
                            font_weight="bold",
                            style={"font-family": "Georgia, serif"}
                        ),
                        align="start",
                        spacing="0"
                    ),
                    justify="between",
                    width="100%",
                    padding_top="10px"
                ),

                rx.cond(
                    State.gc_mensaje != "",
                    rx.box(
                        rx.text(
                            f'"{State.gc_mensaje}"',
                            size="2",
                            color="#4A5568",
                            italic=True,
                            text_align="center"
                        ),
                        padding="10px 15px",
                        background_color="#FAF6F0",
                        border_left="3px solid #8E6F54",
                        width="100%",
                        margin_top="8px"
                    )
                ),

                spacing="3",
                width="100%"
            ),

            rx.divider(color_scheme="gray", margin_y="18px"),

            # 3. Pie del Voucher (Código Único de Muestra y Términos)
            rx.hstack(
                rx.vstack(
                    rx.text("CÓDIGO ÚNICO DE CANJE", size="1", color="#7F7F7F", font_weight="bold"),
                    rx.box(
                        rx.text("TRIBU-EXP-PREVIEW", size="2", color="#FFFFFF", font_weight="bold", letter_spacing="0.15em"),
                        background_color="#2C3639",
                        padding="6px 12px",
                        border_radius="4px"
                    ),
                    align="start",
                    spacing="1"
                ),
                rx.vstack(
                    rx.text("• Válido por 6 meses tras activación.", size="1", color="#7F7F7F"),
                    rx.text("• Canjeable en checkout o WhatsApp.", size="1", color="#7F7F7F"),
                    rx.text("www.tribusonoraconsciente.com", size="1", color="#8E6F54", font_weight="bold"),
                    align="end",
                    spacing="0"
                ),
                justify="between",
                align="center",
                width="100%"
            ),
            width="100%"
        ),
        background_color="#FAF6F0",
        border="2px solid #8E6F54",
        border_radius="12px",
        padding="28px",
        box_shadow="0px 8px 24px rgba(44, 54, 57, 0.12)",
        width="100%"
    )


def tarjeta_experiencia_opcion(exp: rx.Var) -> rx.Component:
    """Tarjeta de selección de experiencia con indicador activo."""
    es_sel = State.gc_experiencia_seleccionada == exp["nombre"]
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.badge(exp["badge"], color_scheme="bronze", size="1"),
                rx.text("$" + exp["precio"].to_string() + " USD", font_weight="bold", color="#8E6F54", size="2"),
                justify="between",
                width="100%",
                align="center"
            ),
            rx.heading(exp["nombre"], size="3", color="#2C3639", font_weight="bold", style={"font-family": "Georgia, serif"}),
            rx.text(exp["descripcion"], size="2", color="#7F7F7F"),
            spacing="2",
            align="start",
            width="100%"
        ),
        padding="18px",
        border_radius="10px",
        background_color=rx.cond(es_sel, "#FAF6F0", "#FFFFFF"),
        border=rx.cond(es_sel, "2px solid #8E6F54", "1px solid #EAE5DF"),
        box_shadow=rx.cond(es_sel, "0px 4px 12px rgba(142, 111, 84, 0.15)", "0px 2px 6px rgba(0,0,0,0.03)"),
        cursor="pointer",
        on_click=lambda: State.seleccionar_experiencia_gc(exp["nombre"], exp["precio"]),
        transition="all 0.2s ease",
        width="100%"
    )


def gift_cards_page() -> rx.Component:
    """Vista principal de Tarjetas de Regalo / Vouchers de Experiencias."""
    contenido = rx.center(
        rx.vstack(
            # Banner Editorial
            rx.vstack(
                rx.heading(
                    "Regala Presencia, Sonido y Sanación",
                    size="7",
                    color="#2C3639",
                    style={"font-family": "Georgia, serif"},
                    text_align="center"
                ),
                rx.text(
                    "Obsequia una vivencia holística inolvidable. Elige un voucher temático y personalízalo con una dedicatoria sagrada.",
                    size="3",
                    color="#7F7F7F",
                    text_align="center",
                    max_width="650px"
                ),
                align="center",
                spacing="2",
                padding_bottom="30px"
            ),

            rx.flex(
                # Columna Izquierda: Selección de Experiencia + Formulario
                rx.vstack(
                    rx.heading("1. Selecciona la Experiencia", size="4", color="#2C3639", font_weight="bold"),
                    rx.vstack(
                        rx.foreach(State.experiencias_disponibles, tarjeta_experiencia_opcion),
                        spacing="3",
                        width="100%"
                    ),

                    rx.divider(color_scheme="gray", margin_y="15px"),

                    rx.heading("2. Personaliza la Dedicatoria", size="4", color="#2C3639", font_weight="bold"),
                    rx.flex(
                        rx.vstack(
                            rx.text("¿Para quién es el regalo?*", size="1", font_weight="bold", color="#2C3639"),
                            rx.input(
                                placeholder="Ej. Sofia",
                                value=State.gc_para_nombre,
                                on_change=State.set_gc_para_nombre,
                                size="3",
                                width="100%",
                                color="#2C3639"
                            ),
                            spacing="1",
                            width="100%"
                        ),
                        rx.vstack(
                            rx.text("¿De parte de quién?*", size="1", font_weight="bold", color="#2C3639"),
                            rx.input(
                                placeholder="Ej. Carlos",
                                value=State.gc_de_nombre,
                                on_change=State.set_gc_de_nombre,
                                size="3",
                                width="100%",
                                color="#2C3639"
                            ),
                            spacing="1",
                            width="100%"
                        ),
                        flex_direction=rx.breakpoints(initial="column", sm="row"),
                        gap="3",
                        width="100%"
                    ),

                    rx.flex(
                        rx.vstack(
                            rx.text("Email del Destinatario (Opcional)", size="1", font_weight="bold", color="#2C3639"),
                            rx.input(
                                placeholder="sofia@ejemplo.com",
                                value=State.gc_destinatario_email,
                                on_change=State.set_gc_destinatario_email,
                                size="2",
                                width="100%",
                                color="#2C3639"
                            ),
                            spacing="1",
                            width="100%"
                        ),
                        rx.vstack(
                            rx.text("WhatsApp del Destinatario (Opcional)", size="1", font_weight="bold", color="#2C3639"),
                            rx.input(
                                placeholder="+58412...",
                                value=State.gc_destinatario_whatsapp,
                                on_change=State.set_gc_destinatario_whatsapp,
                                size="2",
                                width="100%",
                                color="#2C3639"
                            ),
                            spacing="1",
                            width="100%"
                        ),
                        flex_direction=rx.breakpoints(initial="column", sm="row"),
                        gap="3",
                        width="100%"
                    ),

                    rx.vstack(
                        rx.text("Mensaje Especial / Dedicatoria", size="1", font_weight="bold", color="#2C3639"),
                        rx.text_area(
                            placeholder="Escribe unas palabras llenas de intencion...",
                            value=State.gc_mensaje,
                            on_change=State.set_gc_mensaje,
                            size="2",
                            width="100%",
                            color="#2C3639"
                        ),
                        spacing="1",
                        width="100%"
                    ),

                    rx.button(
                        rx.hstack(
                            rx.icon(tag="gift", size=18),
                            rx.text("Agregar Voucher al Carrito", size="3", font_weight="bold"),
                            spacing="2",
                            align="center"
                        ),
                        on_click=State.agregar_voucher_al_carrito,
                        width="100%",
                        height="48px",
                        background_color="#8E6F54",
                        color="#FFFFFF",
                        border_radius="30px",
                        cursor="pointer",
                        _hover={"background_color": "#2C3639"},
                        margin_top="15px"
                    ),

                    width=rx.breakpoints(initial="100%", md="50%"),
                    spacing="3",
                    align="start"
                ),

                # Columna Derecha: Previsualización en Vivo del Voucher
                rx.box(
                    rx.vstack(
                        rx.heading("Previsualización en Vivo", size="3", color="#7F7F7F", text_align="center", width="100%"),
                        vista_previa_voucher_experiencia(),
                        spacing="3",
                        width="100%"
                    ),
                    width=rx.breakpoints(initial="100%", md="50%"),
                    position=rx.breakpoints(initial="static", md="sticky"),
                    top=rx.breakpoints(initial="auto", md="100px"),
                    align_self="start"
                ),

                flex_direction=rx.breakpoints(initial="column-reverse", md="row"),
                gap="30px",
                width="100%",
                align_items="start"
            ),
            width="100%",
            max_width="1100px",
            padding_x="15px",
            padding_y="40px"
        ),
        width="100%",
        background_color="#FAF6F0"
    )
    return plantilla_tribu(contenido, pagina_activa="gift_cards")
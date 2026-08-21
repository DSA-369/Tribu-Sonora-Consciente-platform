# sound_healing_platform/pages/asistencia.py
import reflex as rx

from sound_healing_platform.state import State


def badge_estado_reserva(estado: rx.Var) -> rx.Component:
    """Badge de estado de pago de la reserva."""
    return rx.match(
        estado,
        ("CONFIRMADO", rx.badge("CONFIRMADO", color_scheme="green", size="1")),
        ("PENDIENTE_PAGO", rx.badge("PENDIENTE PAGO", color_scheme="amber", size="1")),
        ("RECHAZADO", rx.badge("CANCELADO", color_scheme="red", size="1")),
        rx.badge("REGISTRADO", color_scheme="gray", size="1")
    )

def tarjeta_asistente_tactil(asistente: rx.Var) -> rx.Component:
    """Tarjeta de asistencia minimalista adaptada exactamente al diseño de 25%.png (Sin íconos)."""
    es_presente = asistente["asistio"]
    monto_pend = asistente["monto_pendiente"].to(float)
    pct_pago = asistente["porcentaje_pago"].to(float)
    tiene_deuda = monto_pend > 0

    return rx.box(
        rx.flex(
            # Columna Izquierda: Badge Estado + Nombre + Teléfono + Cuadritos %
            rx.vstack(
                badge_estado_reserva(asistente["estado"]),
                rx.heading(
                    asistente["nombre_cliente"],
                    size="4",
                    color="#2C3639",
                    font_weight="bold"
                ),
                rx.hstack(
                    rx.link(
                        asistente["whatsapp_cliente"],
                        href="https://wa.me/" + asistente["whatsapp_cliente"].to_string(),
                        is_external=True,
                        color="#8E6F54",
                        size="2",
                        text_decoration="underline"
                    ),
                    # Indicadores inline de % reservado (25%, 50%, 100%)
                    rx.hstack(
                        rx.box(
                            rx.hstack(
                                rx.cond(pct_pago == 25.0, rx.text("✓", font_weight="bold", color="#2C3639"), rx.box(width="8px")),
                                rx.text("25%", size="1", color="#2C3639"),
                                spacing="1",
                                align="center"
                            ),
                            padding="2px 6px",
                            border="1px solid #EAE5DF",
                            border_radius="4px",
                            background_color=rx.cond(pct_pago == 25.0, "#FAF6F0", "#FFFFFF")
                        ),
                        rx.box(
                            rx.hstack(
                                rx.cond(pct_pago == 50.0, rx.text("✓", font_weight="bold", color="#2C3639"), rx.box(width="8px")),
                                rx.text("50%", size="1", color="#2C3639"),
                                spacing="1",
                                align="center"
                            ),
                            padding="2px 6px",
                            border="1px solid #EAE5DF",
                            border_radius="4px",
                            background_color=rx.cond(pct_pago == 50.0, "#FAF6F0", "#FFFFFF")
                        ),
                        rx.box(
                            rx.hstack(
                                rx.cond(pct_pago == 100.0, rx.text("✓", font_weight="bold", color="#2C3639"), rx.box(width="8px")),
                                rx.text("100%", size="1", color="#2C3639"),
                                spacing="1",
                                align="center"
                            ),
                            padding="2px 6px",
                            border="1px solid #EAE5DF",
                            border_radius="4px",
                            background_color=rx.cond(pct_pago == 100.0, "#FAF6F0", "#FFFFFF")
                        ),
                        spacing="2",
                        align="center",
                        margin_left="10px"
                    ),
                    spacing="2",
                    align="center",
                    flex_wrap="wrap"
                ),
                align="start",
                spacing="1",
                flex="1"
            ),

            # Columna Derecha: Botón INGRESAR + Píldora de Pendiente en Puerta
            rx.vstack(
                rx.button(
                    rx.text(
                        rx.cond(es_presente, "PRESENTE", "INGRESAR"),
                        font_weight="bold",
                        size="2"
                    ),
                    size="3",
                    background_color=rx.cond(es_presente, "#2E7D32", "#FAF6F0"),
                    color=rx.cond(es_presente, "#FFFFFF", "#2C3639"),
                    border=rx.cond(es_presente, "none", "1.5px solid #2C3639"),
                    border_radius="10px",
                    padding_x="22px",
                    height="42px",
                    cursor="pointer",
                    width="100%",
                    _hover={"opacity": "0.9"},
                    on_click=lambda: State.toggle_asistencia_participante(asistente["id"])
                ),
                rx.box(
                    rx.text(
                        rx.cond(
                            tiene_deuda,
                            "Pendiente: " + asistente["monto_pendiente"].to_string() + "$",
                            "100% Pagado"
                        ),
                        size="1",
                        font_weight="bold",
                        color=rx.cond(tiene_deuda, "#DC2626", "#2E7D32"),
                        text_align="center"
                    ),
                    padding="3px 12px",
                    border_radius="15px",
                    border=rx.cond(tiene_deuda, "1.5px solid #DC2626", "1.5px solid #2E7D32"),
                    background_color="#FFFFFF",
                    width="100%",
                    text_align="center"
                ),
                align="center",
                spacing="2",
                min_width="140px"
            ),

            flex_direction=rx.breakpoints(initial="column", sm="row"),
            justify="between",
            align_items=rx.breakpoints(initial="stretch", sm="center"),
            gap="15px",
            width="100%"
        ),
        background_color="#FFFFFF",
        border="1px solid #EAE5DF",
        border_radius="12px",
        padding="16px",
        box_shadow="0px 2px 8px rgba(0,0,0,0.03)",
        width="100%"
    )      

def asistencia_page() -> rx.Component:
    """Vista Documento Digital de Asistencia Accesible vía Token."""
    return rx.center(
        rx.box(
            rx.cond(
                State.sesion_asistencia_info["nombre"] != None,
                rx.vstack(
                    # 1. Cabecera Informativa de la Sesión
                    rx.box(
                        rx.vstack(
                            rx.hstack(
                                rx.badge("DOCUMENTO DE CONTROL DE ASISTENCIA", color_scheme="brown", size="1"),
                                rx.icon(tag="shield_check", size=18, color="#8E6F54"),
                                justify="between",
                                align="center",
                                width="100%"
                            ),
                            rx.heading(
                                State.sesion_asistencia_info["nombre"],
                                size="6",
                                color="#2C3639",
                                style={"font-family": "Georgia, serif"},
                                margin_top="6px"
                            ),
                            rx.hstack(
                                rx.hstack(
                                    rx.icon(tag="calendar", size=14, color="#8E6F54"),
                                    rx.text(State.sesion_asistencia_info["fecha_texto"], " • ", State.sesion_asistencia_info["hora_texto"], size="2", color="#2C3639"),
                                    spacing="1",
                                    align="center"
                                ),
                                rx.hstack(
                                    rx.icon(tag="map_pin", size=14, color="#8E6F54"),
                                    rx.text(State.sesion_asistencia_info["ubicacion"], size="2", color="#2C3639"),
                                    spacing="1",
                                    align="center"
                                ),
                                flex_wrap="wrap",
                                gap="15px",
                                margin_top="4px"
                            ),
                            align="start",
                            width="100%"
                        ),
                        background_color="#FFFFFF",
                        border_radius="12px",
                        padding="20px",
                        border="1px solid #EAE5DF",
                        width="100%",
                        margin_bottom="15px"
                    ),

                    # 2. Indicadores Rápidos de Quórum
                    rx.flex(
                        rx.box(
                            rx.vstack(
                                rx.text("Asistencia Actual", size="1", color="#7F7F7F", font_weight="bold"),
                                rx.hstack(
                                    rx.text(State.total_presentes_asistencia, size="6", font_weight="bold", color="#2E7D32"),
                                    rx.text("/", size="4", color="#7F7F7F"),
                                    rx.text(State.total_cupos_reservados_asistencia, size="4", font_weight="bold", color="#2C3639"),
                                    rx.text("asistentes", size="2", color="#7F7F7F"),
                                    align="baseline",
                                    spacing="1"
                                ),
                                align="start",
                                spacing="0"
                            ),
                            background_color="#FFFFFF",
                            border_radius="10px",
                            padding="14px 18px",
                            border="1px solid #EAE5DF",
                            flex="1",
                            min_width="160px"
                        ),
                        rx.box(
                            rx.vstack(
                                rx.text("Capacidad Total Sede", size="1", color="#7F7F7F", font_weight="bold"),
                                rx.hstack(
                                    rx.text(State.sesion_asistencia_info["plazas_totales"], size="6", font_weight="bold", color="#2C3639"),
                                    rx.text("plazas", size="2", color="#7F7F7F"),
                                    align="baseline",
                                    spacing="1"
                                ),
                                align="start",
                                spacing="0"
                            ),
                            background_color="#FFFFFF",
                            border_radius="10px",
                            padding="14px 18px",
                            border="1px solid #EAE5DF",
                            flex="1",
                            min_width="160px"
                        ),
                        gap="10px",
                        width="100%",
                        flex_wrap="wrap",
                        margin_bottom="15px"
                    ),

                    # 3. Buscador de Asistentes
                    rx.input(
                        placeholder="🔍 Buscar por nombre o teléfono...",
                        value=State.busqueda_asistente,
                        on_change=State.set_busqueda_asistente,
                        size="3",
                        border_radius="10px",
                        border="1.5px solid #2C3639",
                        background_color="#FFFFFF",
                        width="100%",
                        margin_bottom="15px"
                    ),

                    # 4. Listado Táctil de Participantes
                    rx.cond(
                        State.lista_asistentes_filtrada.length() == 0,
                        rx.vstack(
                            rx.icon(tag="users", size=36, color="#C8C2BC"),
                            rx.text("No se encontraron reservas registradas.", size="2", color="#7F7F7F"),
                            align="center",
                            padding_y="30px",
                            width="100%"
                        ),
                        rx.vstack(
                            rx.foreach(
                                State.lista_asistentes_filtrada,
                                tarjeta_asistente_tactil
                            ),
                            spacing="3",
                            width="100%"
                        )
                    ),
                    width="100%"
                ),
                rx.vstack(
                    rx.icon(tag="circle_alert", size=48, color="#C8C2BC"),
                    rx.heading("Enlace No Válido", size="5", color="#2C3639"),
                    rx.text("No se encontró ninguna sesión asociada a este enlace.", size="2", color="#7F7F7F"),
                    align="center",
                    padding_y="60px",
                    width="100%"
                )
            ),
            width="100%",
            max_width="650px",
            padding_x=rx.breakpoints(initial="12px", sm="20px"),
            padding_y="25px"
        ),
        width="100%",
        background_color="#FAF6F0",
        min_height="100vh"
    )
# sound_healing_platform/pages/horario_sesiones.py
import reflex as rx

from sound_healing_platform.components.layout import plantilla_tribu
from sound_healing_platform.state import State


def badge_plazas(disponibles: rx.Var, totales: rx.Var) -> rx.Component:
    """Badge dinámico de disponibilidad con alertas por color e indicación explícita de enteros."""
    disp_int = disponibles.to(int)
    disp_str = disponibles.to_string()
    tot_str = totales.to_string()
    
    return rx.cond(
        disp_int <= 0,
        rx.badge("🔴 Agotado", color_scheme="red", size="2"),
        rx.cond(
            disp_int <= 5,
            rx.badge("🔥 ¡Últimos " + disp_str + " cupos!", color_scheme="amber", size="2"),
            rx.badge("🟢 " + disp_str + " de " + tot_str + " cupos disponibles", color_scheme="green", size="2")
        )
    )

def tarjeta_sesion(sesion: rx.Var) -> rx.Component:
    """Tarjeta responsiva para cada sede de sesión recurrente."""
    return rx.box(
        rx.flex(
            # Galería interactiva de la sede (Portada + Carrusel de miniaturas)
            rx.vstack(
                rx.box(
                    rx.image(
                        src=sesion["foto"],
                        width="100%",
                        height="180px",
                        object_fit="cover",
                        border_radius="8px",
                        transition="transform 0.3s ease",
                        _hover={"transform": "scale(1.03)"}
                    ),
                    rx.box(
                        rx.hstack(
                            rx.icon(tag="search", size=12, color="#FFFFFF"),
                            rx.text("Ampliar fotos", size="1", color="#FFFFFF", font_weight="bold"),
                            spacing="1",
                            align="center"
                        ),
                        position="absolute",
                        bottom="8px",
                        left="8px",
                        background_color="rgba(44, 54, 57, 0.8)",
                        padding="4px 8px",
                        border_radius="4px",
                        pointer_events="none"
                    ),
                    position="relative",
                    overflow="hidden",
                    border_radius="8px",
                    cursor="pointer",
                    width="100%",
                    on_click=lambda: State.abrir_lightbox_galeria(sesion["fotos"], sesion["foto"])
                ),
                # Carrusel horizontal de miniaturas
                rx.cond(
                    sesion["fotos"],
                    rx.hstack(
                        rx.foreach(
                            sesion["fotos"].to(list),
                            lambda img_url: rx.image(
                                src=img_url,
                                width="45px",
                                height="45px",
                                object_fit="cover",
                                border_radius="4px",
                                cursor="pointer",
                                border="1px solid #EAE5DF",
                                _hover={"border": "2px solid #8E6F54", "transform": "scale(1.05)"},
                                on_click=lambda: State.abrir_lightbox_galeria(sesion["fotos"], img_url)
                            )
                        ),
                        spacing="2",
                        overflow_x="auto",
                        width="100%",
                        padding_y="4px"
                    )
                ),
                width=rx.breakpoints(initial="100%", md="220px"),
                min_width="220px",
                align="start",
                spacing="2"
            ),
            
            # Detalles de la sesión
            rx.vstack(
                rx.hstack(
                    rx.vstack(
                        badge_plazas(sesion["plazas_disponibles"], sesion["plazas_totales"]),
                        rx.heading(
                            sesion["nombre"],
                            size="5",
                            color="#2C3639",
                            font_weight="normal",
                            style={"font-family": "Georgia, serif"},
                            word_break="break-word"
                        ),
                        align="start",
                        spacing="1",
                        flex="1",
                        min_width="0"
                    ),
                    rx.hstack(
                        rx.text("$", size="5", font_weight="bold", color="#2C3639"),
                        rx.text(sesion["inversion"], size="5", font_weight="bold", color="#2C3639"),
                        rx.text("USD", size="1", color="#7F7F7F"),
                        spacing="1",
                        align="baseline"
                    ),
                    justify="between",
                    align="start",
                    width="100%",
                    gap="2"
                ),
                
                # Frecuencia y fecha/hora
                rx.vstack(
                    rx.hstack(
                        rx.icon(tag="repeat", size=15, color="#8E6F54"),
                        rx.text(sesion["frecuencia_texto"], size="2", font_weight="bold", color="#8E6F54"),
                        spacing="2",
                        align="center"
                    ),
                    rx.hstack(
                        rx.icon(tag="calendar", size=15, color="#2C3639"),
                        rx.text("Próxima cita: ", sesion["fecha_texto"], " • ", sesion["hora_texto"], size="2", color="#2C3639"),
                        spacing="2",
                        align="center"
                    ),
                    rx.hstack(
                        rx.icon(tag="map_pin", size=15, color="#2C3639"),
                        rx.text(sesion["ubicacion"], size="2", color="#2C3639"),
                        spacing="2",
                        align="center"
                    ),
                    rx.hstack(
                        rx.icon(tag="clock", size=15, color="#2C3639"),
                        rx.text("HORA DE RECEPCIÓN ", sesion["hora_recepcion_texto"], size="2", color="#2C3639"),
                        spacing="2",
                        align="center"
                    ),
                    align="start",
                    spacing="1"
                ),

                # Recomendaciones
                rx.box(
                    rx.text("🎒 Recomendaciones para llevar:", size="1", font_weight="bold", color="#A27B5C"),
                    rx.text(sesion["recomendaciones"], size="1", color="#4B5563"),
                    background_color="#FAF6F0",
                    padding="10px 14px",
                    border_radius="6px",
                    width="100%"
                ),

                # Botones de Acción (Instagram & Reserva)
                rx.flex(
                    rx.link(
                        rx.hstack(
                            rx.icon(tag="camera", size=15, color="#8E6F54"),
                            rx.text("Ver publicación en Instagram", size="2", color="#8E6F54", text_decoration="underline"),
                            spacing="1",
                            align="center"
                        ),
                        href=sesion["instagram_url"],
                        is_external=True
                    ),
                    rx.button(
                        "Reservar mi Cupo",
                        size="3",
                        background_color="#8E6F54",
                        color="#FFFFFF",
                        border_radius="6px",
                        font_weight="bold",
                        padding_x="22px",
                        width=rx.breakpoints(initial="100%", sm="auto"),
                        cursor="pointer",
                        _hover={"background_color": "#73573F"},
                        on_click=lambda: State.abrir_modal_reserva_sesion(sesion)
                    ),
                    justify="between",
                    align="center",
                    width="100%",
                    flex_wrap="wrap",
                    gap="3",
                    margin_top="10px"
                ),
                width="100%",
                spacing="3",
                align="start",
                flex="1",
                min_width="0"
            ),
            flex_direction=rx.breakpoints(initial="column", md="row"),
            gap="20px",
            width="100%",
            align_items="start"
        ),
        background_color="#FFFFFF",
        border_radius="12px",
        border="1px solid #EAE5DF",
        padding="20px",
        box_shadow="0px 2px 12px rgba(0,0,0,0.03)",
        margin_bottom="20px",
        width="100%"
    )

def modal_reserva_sesion() -> rx.Component:
    """Modal interactivo para solicitar cupos con campos dinámicos y WhatsApp."""
    return rx.dialog.root(
        rx.dialog.content(
            rx.vstack(
                rx.hstack(
                    rx.heading("Reservar Cupo de Sesión", size="5", color="#2C3639", style={"font-family": "Georgia, serif"}),
                    rx.icon(tag="x", size=20, color="#2C3639", cursor="pointer", on_click=State.cerrar_modal_reserva_sesion),
                    justify="between",
                    align="center",
                    width="100%"
                ),
                
                rx.divider(color_scheme="gray", margin_y="10px"),

                # Resumen de la sesión elegida
                rx.vstack(
                    rx.text(State.sesion_seleccionada_reserva["nombre"], size="3", font_weight="bold", color="#8E6F54"),
                    rx.text("📍 ", State.sesion_seleccionada_reserva["ubicacion"], size="2", color="#2C3639"),
                    rx.text("📅 ", State.sesion_seleccionada_reserva["fecha_texto"], " (", State.sesion_seleccionada_reserva["hora_texto"], ")", size="2", color="#2C3639"),
                    align="start",
                    spacing="1",
                    padding="12px",
                    background_color="#FAF6F0",
                    border_radius="8px",
                    width="100%"
                ),

                # Selector de número de cupos
                rx.hstack(
                    rx.vstack(
                        rx.text("Número de Cupos", size="1", font_weight="bold", color="#2C3639"),
                        rx.text("Inversión unitaria: $", State.sesion_seleccionada_reserva["inversion"].to_string(), " USD", size="1", color="#7F7F7F"),
                        align="start",
                        spacing="0"
                    ),
                    rx.hstack(
                        rx.button("-", size="2", variant="outline", on_click=State.decrementar_cupos_reserva),
                        rx.text(State.reserva_cantidad_cupos, size="4", font_weight="bold", color="#2C3639", padding_x="10px"),
                        rx.button("+", size="2", variant="outline", on_click=State.incrementar_cupos_reserva),
                        align="center"
                    ),
                    justify="between",
                    align="center",
                    width="100%",
                    padding_y="5px"
                ),

                # Selector de Porcentaje de Pago / Abono Inicial
                rx.vstack(
                    rx.text("Porcentaje de Abono para Reservar (Opcional)", size="1", font_weight="bold", color="#2C3639"),
                    rx.hstack(
                        rx.box(
                            rx.hstack(
                                rx.cond(State.reserva_porcentaje_pago == 25.0, rx.text("✓", font_weight="bold", color="#2C3639"), rx.box(width="8px")),
                                rx.text("25%", size="2", font_weight="bold", color="#2C3639"),
                                spacing="1",
                                align="center"
                            ),
                            padding="8px 16px",
                            border_radius="6px",
                            border=rx.cond(State.reserva_porcentaje_pago == 25.0, "1.5px solid #2C3639", "1px solid #D1D5DB"),
                            background_color=rx.cond(State.reserva_porcentaje_pago == 25.0, "#FAF6F0", "#FFFFFF"),
                            cursor="pointer",
                            on_click=lambda: State.set_reserva_porcentaje_pago(25.0)
                        ),
                        rx.box(
                            rx.hstack(
                                rx.cond(State.reserva_porcentaje_pago == 50.0, rx.text("✓", font_weight="bold", color="#2C3639"), rx.box(width="8px")),
                                rx.text("50%", size="2", font_weight="bold", color="#2C3639"),
                                spacing="1",
                                align="center"
                            ),
                            padding="8px 16px",
                            border_radius="6px",
                            border=rx.cond(State.reserva_porcentaje_pago == 50.0, "1.5px solid #2C3639", "1px solid #D1D5DB"),
                            background_color=rx.cond(State.reserva_porcentaje_pago == 50.0, "#FAF6F0", "#FFFFFF"),
                            cursor="pointer",
                            on_click=lambda: State.set_reserva_porcentaje_pago(50.0)
                        ),
                        rx.box(
                            rx.hstack(
                                rx.cond(State.reserva_porcentaje_pago == 100.0, rx.text("✓", font_weight="bold", color="#2C3639"), rx.box(width="8px")),
                                rx.text("100%", size="2", font_weight="bold", color="#2C3639"),
                                spacing="1",
                                align="center"
                            ),
                            padding="8px 16px",
                            border_radius="6px",
                            border=rx.cond(State.reserva_porcentaje_pago == 100.0, "1.5px solid #2C3639", "1px solid #D1D5DB"),
                            background_color=rx.cond(State.reserva_porcentaje_pago == 100.0, "#FAF6F0", "#FFFFFF"),
                            cursor="pointer",
                            on_click=lambda: State.set_reserva_porcentaje_pago(100.0)
                        ),
                        gap="2",
                        width="100%"
                    ),
                    # 🎟️ CAMPO Y BOTÓN PARA APLICAR CUPÓN EN RESERVAS
rx.vstack(
    rx.text("¿Tienes un Cupón de Descuento o Especial?", size="1", font_weight="bold", color="#2C3639"),
    rx.hstack(
        rx.input(
            placeholder="Ej. ESPECIAL15 o TRIBU10",
            value=State.reserva_cupon_input,
            on_change=State.set_reserva_cupon_input,
            size="2",
            border_radius="6px",
            border="1px solid #A0AEC0",
            background_color="#FFFFFF",
            color="#2C3639",
            width="70%"
        ),
        rx.button(
            "Aplicar",
            on_click=State.aplicar_cupon_reserva,
            size="2",
            background_color="#8E6F54",
            color="#FFFFFF",
            font_weight="bold",
            border_radius="6px",
            width="30%"
        ),
        width="100%",
        spacing="2"
    ),
    rx.cond(
        State.reserva_descuento_monto > 0,
        rx.hstack(
            rx.text("Descuento aplicado:", size="1", color="#2E7D32", font_weight="bold"),
            rx.text("-$" + State.reserva_descuento_monto.to_string() + " USD", size="1", color="#2E7D32", font_weight="bold"),
            justify="between",
            width="100%"
        )
    ),
    spacing="1",
    width="100%",
    padding_y="8px"
),
                    # Resumen financiero dinámico
                 rx.box(
                     rx.cond(
                         State.reserva_porcentaje_pago == 0.0,
                         rx.hstack(
                             rx.vstack(
                                 rx.text("Abono Inicial:", size="1", color="#7F7F7F"),
                                 rx.text("Por convenir en WhatsApp", size="2", font_weight="bold", color="#8E6F54"),
                                 align="start",
                                 spacing="0"
                             ),
                             rx.vstack(
                                 rx.text("Monto Total de la Sesión:", size="1", color="#7F7F7F"),
                                 rx.text("$" + State.reserva_monto_total_calculado.to_string() + " USD", size="3", font_weight="bold", color="#2C3639"),
                                 align="start",
                                 spacing="0"
                             ),
                             justify="between",
                             width="100%"
                         ),
                         rx.hstack(
                             rx.vstack(
                                 rx.text("Abono Hoy (" + State.reserva_porcentaje_pago.to_string() + "%):", size="1", color="#7F7F7F"),
                                 rx.text("$" + State.reserva_monto_pagado_calculado.to_string() + " USD", size="3", font_weight="bold", color="#2E7D32"),
                                 align="start",
                                 spacing="0"
                             ),
                             rx.vstack(
                                 rx.text("Pendiente en Puerta:", size="1", color="#7F7F7F"),
                                 rx.text("$" + State.reserva_monto_pendiente_calculado.to_string() + " USD", size="3", font_weight="bold", color="#DC2626"),
                                 align="start",
                                 spacing="0"
                             ),
                             justify="between",
                             width="100%"
                         )
                     ),
                     background_color="#FAF6F0",
                     padding="10px 14px",
                     border_radius="8px",
                     border="1px solid #EAE5DF",
                     width="100%",
                     margin_top="4px"
                 ),
                    width="100%",
                    spacing="2",
                    align="start"
                ),

                # Campos Dinámicos para N Participantes
                rx.vstack(
                    rx.foreach(
                        State.reserva_participantes,
                        lambda val, idx: rx.vstack(
                            rx.text("Nombre y Apellido del Participante " + (idx + 1).to_string() + "*", size="1", font_weight="bold", color="#8E6F54"),
                            rx.input(
                                placeholder="Ej. Nombre Completo",
                                value=val,
                                on_change=lambda nuevo_val: State.actualizar_nombre_participante(idx, nuevo_val),
                                size="3",
                                width="100%"
                            ),
                            spacing="1",
                            align="start",
                            width="100%"
                        )
                    ),
                    spacing="3",
                    width="100%"
                ),

                # Correo y WhatsApp de Contacto Principal
                rx.vstack(
                    rx.text("Correo Electrónico de Contacto*", size="1", font_weight="bold", color="#2C3639"),
                    rx.input(
                        placeholder="ejemplo@correo.com",
                        value=State.reserva_email_cliente,
                        on_change=State.set_reserva_email,
                        size="3",
                        width="100%"
                    ),
                    spacing="1",
                    align="start",
                    width="100%"
                ),

                rx.vstack(
                    rx.text("Teléfono WhatsApp*", size="1", font_weight="bold", color="#2C3639"),
                    rx.input(
                        placeholder="Ej. +584123445369",
                        value=State.reserva_whatsapp_cliente,
                        on_change=State.set_reserva_whatsapp,
                        size="3",
                        width="100%"
                    ),
                    spacing="1",
                    align="start",
                    width="100%"
                ),

                rx.button(
                    "Confirmar y Redirigir a WhatsApp",
                    size="3",
                    width="100%",
                    background_color="#2C3639",
                    color="#FFFFFF",
                    font_weight="bold",
                    border_radius="25px",
                    cursor="pointer",
                    _hover={"background_color": "#8E6F54"},
                    on_click=State.confirmar_reserva_sesion
                ),
                spacing="4",
                width="100%"
            ),
            background_color="#FFFFFF",
            padding="25px",
            border_radius="12px",
            max_width="480px"
        ),
        open=State.modal_reserva_sesion_abierto
    )
def modal_lightbox() -> rx.Component:
    """Modal flotante de pantalla completa para explorar la galería de fotos."""
    return rx.dialog.root(
        rx.dialog.content(
            rx.vstack(
                # Encabezado con indicador de orden y botón cerrar
                rx.hstack(
                    rx.hstack(
                        rx.icon(tag="image", size=18, color="#FFFFFF"),
                        rx.text("Galería del Espacio", size="2", color="#FFFFFF", font_weight="bold"),
                        spacing="2",
                        align="center"
                    ),
                    rx.icon(tag="x", size=22, color="#FFFFFF", cursor="pointer", on_click=State.cerrar_lightbox),
                    justify="between",
                    align="center",
                    width="100%",
                    margin_bottom="10px"
                ),
                # Visor principal con flechas laterales
                rx.hstack(
                    rx.cond(
                        State.fotos_lightbox,
                        rx.button(
                            rx.icon(tag="chevron-left", size=24, color="#FFFFFF"),
                            variant="soft",
                            color_scheme="gray",
                            on_click=State.foto_anterior_lightbox,
                            cursor="pointer",
                            padding="8px"
                        )
                    ),
                    rx.image(
                     src=State.foto_lightbox_actual,
                     max_width=rx.breakpoints(initial="55vw", sm="75vw"),
                     max_height="70vh",
                     object_fit="contain",
                     border_radius="8px"
                 ),
                    rx.cond(
                        State.fotos_lightbox,
                        rx.button(
                            rx.icon(tag="chevron-right", size=24, color="#FFFFFF"),
                            variant="soft",
                            color_scheme="gray",
                            on_click=State.foto_siguiente_lightbox,
                            cursor="pointer",
                            padding="8px"
                        )
                    ),
                    justify="center",
                    align="center",
                    width="100%",
                    gap="3"
                ),
                align="center",
                width="100%"
            ),
            background_color="rgba(20, 20, 20, 0.95)",
         padding=rx.breakpoints(initial="14px", sm="20px"),
         border_radius="12px",
         border="1px solid rgba(255, 255, 255, 0.1)",
         width=rx.breakpoints(initial="92vw", sm="auto"),
         max_width="90vw"
        ),
        open=State.modal_lightbox_abierto
    )

def horario_sesiones_page() -> rx.Component:
    """Vista Principal 'Horario de Sesiones'."""
    contenido = rx.center(
        rx.vstack(
            rx.vstack(
                rx.heading(
                    "Horario de Sesiones Grupales",
                    id="seccion-horarios-sesiones",
                    size="8",
                    color="#2C3639",
                    font_weight="normal",
                    text_align="center",
                    style={"font-family": "Georgia, serif", "scroll-margin-top": "120px"},
                    margin_bottom="12px"
                ),
                rx.text(
                    "Consulta nuestro calendario de encuentros periódicos de sanación sonora en las distintas sedes aliadas.",
                    size=rx.breakpoints(initial="2", md="3"),
                    color="#7F7F7F",
                    text_align="center",
                    max_width="750px",
                    margin_bottom="35px"
                ),
                align="center",
                width="100%"
            ),

            # Listado dinámico
            rx.vstack(
                rx.foreach(
                    State.sesiones_tribu,
                    tarjeta_sesion
                ),
                width="100%",
                spacing="3"
            ),
            modal_reserva_sesion(),
            modal_lightbox(),
            width="100%",
            max_width="1050px",
            padding_x=rx.breakpoints(initial="10px", sm="20px"),
            padding_y="40px"
        ),
        width="100%",
        background_color="#FAF6F0"
    )
    return plantilla_tribu(contenido, pagina_activa="sesiones")
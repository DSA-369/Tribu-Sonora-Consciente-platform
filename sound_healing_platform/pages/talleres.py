# sound_healing_platform/pages/talleres.py
import reflex as rx

from sound_healing_platform.components.layout import plantilla_tribu
from sound_healing_platform.state import State


def tarjeta_taller(taller: rx.Var) -> rx.Component:
    """Tarjeta de taller/evento estilo editorial alineada con la referencia visual."""
    return rx.box(
        rx.flex(
            # 🖼️ COLUMNA IZQUIERDA: IMAGEN DEL EVENTO
            rx.box(
                rx.image(
                    src=taller["foto"],
                    width="100%",
                    height="180px",
                    object_fit="cover",
                    border_radius="8px"
                ),
                width=rx.breakpoints(initial="100%", md="180px"),
                min_width="180px",
                overflow="hidden"
            ),
            
            # 📝 COLUMNA CENTRAL & DERECHA: INFORMACIÓN Y PRECIO (RESPONSIVO MÓVIL)
            rx.vstack(
                rx.flex(
                    rx.vstack(
                        # Etiqueta / Categoría
                        rx.text(
                            taller["tipo"],
                            size="1",
                            letter_spacing="0.12em",
                            color="#A27B5C",
                            font_weight="bold"
                        ),
                        # Título del Evento con ajuste automático de palabra
                        rx.heading(
                            taller["titulo"],
                            size=rx.breakpoints(initial="4", sm="5"),
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
                    # Precio
                    rx.hstack(
                        rx.text("$", size=rx.breakpoints(initial="4", sm="5"), font_weight="bold", color="#2C3639"),
                        rx.text(taller["precio"], size=rx.breakpoints(initial="4", sm="5"), font_weight="bold", color="#2C3639"),
                        spacing="1",
                        align="baseline"
                    ),
                    justify="between",
                    align="start",
                    width="100%",
                    gap="2"
                ),
                
                # Facilitador con enlace a su biografía (envolvente en móviles)
                rx.flex(
                    rx.hstack(
                        rx.icon(tag="user", size=14, color="#7F7F7F"),
                        rx.text(taller["facilitador"], size="2", font_weight="medium", color="#2C3639"),
                        spacing="2",
                        align="center"
                    ),
                    rx.text(
                        "• Ver biografía", 
                        size="1", 
                        color="#8E6F54", 
                        cursor="pointer", 
                        text_decoration="underline",
                        on_click=lambda: State.ir_a_biografia_facilitador(taller["facilitador"])
                    ),
                    spacing="2",
                    align="center",
                    flex_wrap="wrap",
                    gap="2"
                ),
                
                # Descripción corta
                rx.text(
                    taller["descripcion"],
                    size="2",
                    color="#4B5563",
                    line_height="1.5",
                    margin_y="4px"
                ),
                
                # Detalles de Metadatos (Fecha, Hora, Lugar) + Botón Reservar
                rx.flex(
                    rx.vstack(
                        rx.hstack(
                            rx.icon(tag="calendar", size=14, color="#8E6F54"),
                            rx.text(taller["fecha_texto"], size="2", color="#2C3639"),
                            spacing="2",
                            align="center"
                        ),
                        rx.hstack(
                            rx.icon(tag="clock", size=14, color="#8E6F54"),
                            rx.text(f"{taller['hora_texto']} • {taller['duracion_texto']}", size="2", color="#2C3639"),
                            spacing="2",
                            align="center"
                        ),
                        rx.hstack(
                            rx.icon(tag="map_pin", size=14, color="#8E6F54"),
                            rx.text(taller["ubicacion"], size="2", color="#2C3639"),
                            spacing="2",
                            align="center"
                        ),
                        align="start",
                        spacing="1"
                    ),
                    
                    # 📲 Botón de Reserva Inteligente (Ancho completo en celular para táctil cómodo)
                    rx.button(
                        "Reservar ahora",
                        size="3",
                        background_color="#8E6F54",
                        color="#FFFFFF",
                        border_radius="6px",
                        font_weight="bold",
                        padding_x="22px",
                        width=rx.breakpoints(initial="100%", sm="auto"),
                        cursor="pointer",
                        _hover={"background_color": "#73573F"},
                        on_click=lambda: State.agendar_taller(taller)
                    ),
                    flex_direction=rx.breakpoints(initial="column", sm="row"),
                    justify="between",
                    align_items=rx.breakpoints(initial="stretch", sm="end"),
                    width="100%",
                    gap="3",
                    margin_top="10px"
                ),
                width="100%",
                spacing="2",
                align="start"
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

def talleres_page() -> rx.Component:
    """Vista Principal del Módulo 'Talleres y Eventos' con Vista de Semanas y Meses."""
    contenido = rx.center(
        rx.vstack(
            # Título Principal
            rx.heading(
                "Talleres y Eventos",
                size="8",
                color="#2C3639",
                font_weight="normal",
                text_align="center",
                style={"font-family": "Georgia, serif"},
                margin_bottom="10px"
            ),
            rx.text(
                "Explora nuestras actividades, talleres y encuentros comunitarios de sanación sonora.",
                size="3",
                color="#7F7F7F",
                text_align="center",
                margin_bottom="25px"
            ),
            
            # 🎛️ CONTENEDOR PRINCIPAL TIPO TARJETA EDITORIAL
            rx.box(
                rx.vstack(
                    # 1. CABECERA: ZONA HORARIA Y BOTONES VISTA (WEEK / MONTH)
                    rx.flex(
                        rx.hstack(
                            rx.text("Caracas GMT-4", size="2", font_weight="medium", color="#2C3639"),
                            rx.icon(tag="chevron_down", size=14, color="#2C3639"),
                            border="1px solid #EAE5DF",
                            border_radius="25px",
                            padding="6px 18px",
                            background_color="#FFFFFF",
                            cursor="pointer",
                            box_shadow="0px 2px 6px rgba(0,0,0,0.02)"
                        ),
                        rx.hstack(
                            rx.hstack(
                                rx.icon(tag="list_todo", size=14, color=rx.cond(State.filtro_vista_talleres == "Week", "#8E6F54", "#7F7F7F")),
                                rx.text("Week", size="2", font_weight="medium", color=rx.cond(State.filtro_vista_talleres == "Week", "#8E6F54", "#7F7F7F")),
                                spacing="1",
                                align="center",
                                padding="5px 14px",
                                border_radius="20px",
                                background_color=rx.cond(State.filtro_vista_talleres == "Week", "#FFFFFF", "transparent"),
                                border=rx.cond(State.filtro_vista_talleres == "Week", "1px solid #8E6F54", "none"),
                                cursor="pointer",
                                on_click=lambda: State.set_filtro_vista_talleres("Week")
                            ),
                            rx.hstack(
                                rx.icon(tag="calendar", size=14, color=rx.cond(State.filtro_vista_talleres == "Month", "#8E6F54", "#7F7F7F")),
                                rx.text("Month", size="2", font_weight="medium", color=rx.cond(State.filtro_vista_talleres == "Month", "#8E6F54", "#7F7F7F")),
                                spacing="1",
                                align="center",
                                padding="5px 14px",
                                border_radius="20px",
                                background_color=rx.cond(State.filtro_vista_talleres == "Month", "#FFFFFF", "transparent"),
                                border=rx.cond(State.filtro_vista_talleres == "Month", "1px solid #8E6F54", "none"),
                                cursor="pointer",
                                on_click=lambda: State.set_filtro_vista_talleres("Month")
                            ),
                            border="1px solid #EAE5DF",
                            border_radius="25px",
                            padding="3px",
                            background_color="#FAF6F0"
                        ),
                        justify="between",
                        align="center",
                        width="100%",
                        flex_wrap="wrap",
                        gap="3",
                        margin_bottom="20px"
                    ),

                    # 2. CALENDARIO INTERACTIVO DINÁMICO (SEMANAL vs MENSUAL)
                    rx.cond(
                        State.filtro_vista_talleres == "Week",
                        # VISTA DE 7 DÍAS (SEMANAL)
                        rx.hstack(
                            rx.center(
                                rx.icon(tag="chevron_left", size=20, color="#2C3639"),
                                width="44px",
                                height="44px",
                                min_width="44px",
                                border_radius="50%",
                                border="1px solid #EAE5DF",
                                background_color="#FFFFFF",
                                cursor="pointer",
                                _hover={"background_color": "#FAF6F0", "border_color": "#8E6F54"},
                                on_click=State.semana_anterior
                            ),
                            rx.flex(
                                rx.foreach(
                                    State.dias_semana_actual,
                                    lambda d: rx.vstack(
                                        rx.text(
                                            d["dia_nombre"], 
                                            size="1", 
                                            color=rx.cond(State.fecha_filtro_seleccionada == d["fecha"], "#8E6F54", "#7F7F7F"), 
                                            font_weight="medium"
                                        ),
                                        rx.text(
                                            d["dia_num"], 
                                            size=rx.breakpoints(initial="3", sm="4"), 
                                            color=rx.cond(State.fecha_filtro_seleccionada == d["fecha"], "#8E6F54", "#2C3639"), 
                                            font_weight=rx.cond(State.fecha_filtro_seleccionada == d["fecha"], "bold", "normal")
                                        ),
                                        rx.cond(
                                            d["tiene_eventos"],
                                            rx.hstack(
                                                rx.box(width="4px", height="4px", border_radius="50%", background_color="#8E6F54"),
                                                rx.box(width="4px", height="4px", border_radius="50%", background_color="#8E6F54"),
                                                spacing="1"
                                            ),
                                            rx.box(height="4px")
                                        ),
                                        align="center",
                                        justify="center",
                                        spacing="1",
                                        padding=rx.breakpoints(initial="6px 2px", sm="8px 12px"),
                                        border_radius="12px",
                                        background_color=rx.cond(State.fecha_filtro_seleccionada == d["fecha"], "#FAF3E0", "transparent"),
                                        border=rx.cond(State.fecha_filtro_seleccionada == d["fecha"], "1px solid #8E6F54", "1px solid transparent"),
                                        cursor="pointer",
                                        on_click=lambda: State.seleccionar_fecha_calendario(d["fecha"]),
                                        flex="1",
                                        min_width="0"
                                    )
                                ),
                                width="100%",
                                justify="between",
                                align="center",
                                gap=rx.breakpoints(initial="1", sm="2")
                            ),
                            rx.center(
                                rx.icon(tag="chevron_right", size=20, color="#2C3639"),
                                width="44px",
                                height="44px",
                                min_width="44px",
                                border_radius="50%",
                                border="1px solid #EAE5DF",
                                background_color="#FFFFFF",
                                cursor="pointer",
                                _hover={"background_color": "#FAF6F0", "border_color": "#8E6F54"},
                                on_click=State.semana_siguiente
                            ),
                            justify="between",
                            align="center",
                            width="100%",
                            margin_bottom="25px",
                            gap=rx.breakpoints(initial="2", sm="4")
                        ),
                        # VISTA DE MESES (MENSUAL)
                        rx.hstack(
                            rx.center(
                                rx.icon(tag="chevron_left", size=20, color="#2C3639"),
                                width="44px",
                                height="44px",
                                min_width="44px",
                                border_radius="50%",
                                border="1px solid #EAE5DF",
                                background_color="#FFFFFF",
                                cursor="pointer",
                                _hover={"background_color": "#FAF6F0", "border_color": "#8E6F54"},
                                on_click=State.anio_anterior
                            ),
                            rx.flex(
                                rx.foreach(
                                    State.meses_anio_actual,
                                    lambda m: rx.vstack(
                                        rx.text(
                                            m["mes_nombre"], 
                                            size="2", 
                                            color=rx.cond(State.mes_filtro_seleccionado == m["fecha_mes"], "#8E6F54", "#2C3639"), 
                                            font_weight=rx.cond(State.mes_filtro_seleccionado == m["fecha_mes"], "bold", "medium")
                                        ),
                                        rx.text(m["anio"], size="1", color="#7F7F7F"),
                                        rx.cond(
                                            m["tiene_eventos"],
                                            rx.box(width="5px", height="5px", border_radius="50%", background_color="#8E6F54"),
                                            rx.box(height="5px")
                                        ),
                                        align="center",
                                        justify="center",
                                        spacing="1",
                                        padding=rx.breakpoints(initial="6px 4px", sm="8px 10px"),
                                        border_radius="12px",
                                        background_color=rx.cond(State.mes_filtro_seleccionado == m["fecha_mes"], "#FAF3E0", "transparent"),
                                        border=rx.cond(State.mes_filtro_seleccionado == m["fecha_mes"], "1px solid #8E6F54", "1px solid transparent"),
                                        cursor="pointer",
                                        on_click=lambda: State.seleccionar_mes_calendario(m["fecha_mes"]),
                                        flex="1",
                                        min_width="0"
                                    )
                                ),
                                width="100%",
                                justify="between",
                                align="center",
                                gap=rx.breakpoints(initial="1", sm="2")
                            ),
                            rx.center(
                                rx.icon(tag="chevron_right", size=20, color="#2C3639"),
                                width="44px",
                                height="44px",
                                min_width="44px",
                                border_radius="50%",
                                border="1px solid #EAE5DF",
                                background_color="#FFFFFF",
                                cursor="pointer",
                                _hover={"background_color": "#FAF6F0", "border_color": "#8E6F54"},
                                on_click=State.anio_siguiente
                            ),
                            justify="between",
                            align="center",
                            width="100%",
                            margin_bottom="25px",
                            gap=rx.breakpoints(initial="2", sm="4")
                        )
                    ),

                    # 3. FILTROS RÁPIDOS EN PÍLDORAS
                    rx.flex(
                        rx.button(
                            "MOSTRAR TODO", 
                            size="2", 
                            variant="outline", 
                            color="#2C3639", 
                            border="1px solid #EAE5DF",
                            border_radius="25px",
                            background_color="#FFFFFF",
                            font_weight="medium",
                            padding_x="18px",
                            cursor="pointer",
                            _hover={"background_color": "#FAF6F0"},
                            on_click=State.limpiar_filtros_talleres
                        ),
                        rx.button(
                            "HOY", 
                            size="2", 
                            variant="outline",
                            background_color=rx.cond(State.filtro_solo_hoy, "#8E6F54", "#FFFFFF"),
                            color=rx.cond(State.filtro_solo_hoy, "#FFFFFF", "#2C3639"),
                            border="1px solid #EAE5DF",
                            border_radius="25px",
                            font_weight="medium",
                            padding_x="18px",
                            cursor="pointer",
                            _hover={"background_color": "#FAF6F0"},
                            on_click=State.filtrar_hoy
                        ),
                        
                        rx.box(width="1px", height="24px", background_color="#EAE5DF", display=rx.breakpoints(initial="none", sm="block")),

                        rx.select(
                            State.opciones_facilitadores,
                            value=State.filtro_facilitador,
                            on_change=State.set_filtro_facilitador,
                            size="2",
                            variant="surface",
                            radius="full",
                            color="#2C3639",
                            border="1px solid #EAE5DF",
                            background_color="#FFFFFF",
                            cursor="pointer"
                        ),
                        rx.select(
                            State.opciones_ubicaciones,
                            value=State.filtro_ubicacion,
                            on_change=State.set_filtro_ubicacion,
                            size="2",
                            variant="surface",
                            radius="full",
                            color="#2C3639",
                            border="1px solid #EAE5DF",
                            background_color="#FFFFFF",
                            cursor="pointer"
                        ),
                        rx.select(
                            State.opciones_etiquetas,
                            value=State.filtro_etiqueta,
                            on_change=State.set_filtro_etiqueta,
                            size="2",
                            variant="surface",
                            radius="full",
                            color="#2C3639",
                            border="1px solid #EAE5DF",
                            background_color="#FFFFFF",
                            cursor="pointer"
                        ),

                        gap="3",
                        flex_wrap="wrap",
                        align_items="center",
                        width="100%",
                        margin_bottom="30px"
                    ),

                    # 4. LISTADO DINÁMICO DE TARJETAS
                    rx.cond(
                        State.talleres_filtrados.length() == 0,
                        rx.vstack(
                            rx.icon(tag="calendar", size=40, color="#C8C2BC"),
                            rx.text("No hay talleres programados con los filtros seleccionados.", size="3", color="#7F7F7F"),
                            rx.button(
                                "Restablecer todos los filtros", 
                                size="2", 
                                variant="soft", 
                                color_scheme="brown",
                                cursor="pointer",
                                on_click=State.limpiar_filtros_talleres
                            ),
                            align="center",
                            spacing="3",
                            padding_y="40px"
                        ),
                        rx.vstack(
                            rx.foreach(
                                State.talleres_filtrados,
                                tarjeta_taller
                            ),
                            width="100%",
                            spacing="3"
                        )
                    ),
                    width="100%"
                ),
                background_color="#FFFFFF",
                border_radius="16px",
                border="1px solid #EAE5DF",
                padding=rx.breakpoints(initial="15px", md="30px"),
                box_shadow="0px 4px 20px rgba(0,0,0,0.03)",
                width="100%"
            ),
            width="100%",
            max_width="1050px",
            padding_x=rx.breakpoints(initial="10px", sm="15px")
        ),
        width="100%",
        background_color="#FAF6F0",
        padding_y="40px"
    )
    return plantilla_tribu(contenido, pagina_activa="talleres")
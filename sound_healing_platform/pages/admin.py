# sound_healing_platform/pages/admin.py
import reflex as rx

from sound_healing_platform.components.layout import plantilla_tribu
from sound_healing_platform.state import State


def tarjeta_orden_admin(ord_item: rx.Var) -> rx.Component:
    """Tarjeta individual para la confirmación de compras y Vouchers en el Panel Admin."""
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.vstack(
                    rx.heading("Orden #", ord_item["id"], " • Ref: ", ord_item["referencia"], size="3", color="#2C3639", font_weight="bold"),
                    rx.text("👤 Cliente: ", ord_item["cliente_nombre"], " (", ord_item["cliente_email"], ")", size="2", color="#2C3639"),
                    rx.cond(
                        ord_item["cliente_telefono"] != "",
                        rx.text("📞 Teléfono: ", ord_item["cliente_telefono"], size="2", color="#7F7F7F")
                    ),
                    rx.text("💳 Método: ", ord_item["metodo_pago"], " | Total: $", ord_item["monto_total"], " USD", size="2", font_weight="bold", color="#8E6F54"),
                    align="start",
                    spacing="0"
                ),
                rx.badge(
                    ord_item["estado"],
                    color_scheme=rx.match(
                        ord_item["estado"],
                        ("COMPLETADO", "green"),
                        ("RECHAZADO", "red"),
                        "amber"
                    ),
                    size="2"
                ),
                justify="between",
                align="start",
                width="100%"
            ),

            rx.divider(color_scheme="gray", margin_y="8px"),

            # 📦 Lista de Productos / Vouchers Adquiridos
            rx.vstack(
                rx.text("📦 Ítems Comprados:", size="1", font_weight="bold", color="#8E6F54"),
                rx.foreach(
                    ord_item["items"].to(list[dict]),
                    lambda item: rx.hstack(
                        rx.hstack(
                            rx.text("• ", item["cantidad"], "x ", item["nombre"], size="2", color="#2C3639", font_weight="bold"),
                            rx.cond(
                                item["variante"] != "",
                                rx.badge(item["variante"], color_scheme="bronze", size="1")
                            ),
                            spacing="2",
                            align="center"
                        ),
                        rx.text("$", item["precio"], " USD c/u", size="2", color="#8E6F54", font_weight="bold"),
                        justify="between",
                        width="100%",
                        align="center"
                    )
                ),
                background_color="#FAF6F0",
                padding="10px 14px",
                border_radius="6px",
                border="1px solid #EAE5DF",
                width="100%",
                spacing="1"
            ),

            rx.divider(color_scheme="gray", margin_y="8px"),

            # Link al Comprobante Adjunto
            rx.cond(
                ord_item["comprobante_url"] != "",
                rx.hstack(
                    rx.icon(tag="image", size=16, color="#8E6F54"),
                    rx.link("Ver Comprobante de Pago Adjunto", href=ord_item["comprobante_url"], is_external=True, size="2", color="#8E6F54", font_weight="bold"),
                    spacing="2",
                    align="center"
                )
            ),

            rx.divider(color_scheme="gray", margin_y="8px"),

            # Botonera de Acción
            rx.hstack(
                rx.button(
                    "Aprobar y Confirmar Pedido",
                    size="2",
                    color_scheme="green",
                    variant="solid",
                    on_click=lambda: State.aprobar_orden_producto(ord_item["id"])
                ),
                rx.button(
                    "Rechazar",
                    size="2",
                    color_scheme="red",
                    variant="soft",
                    on_click=lambda: State.rechazar_orden_producto(ord_item["id"])
                ),
                spacing="2",
                width="100%",
                justify="end"
            ),
            width="100%",
            spacing="2"
        ),
        background_color="#FFFFFF",
        border="1px solid #EAE5DF",
        border_radius="10px",
        padding="15px",
        margin_bottom="12px",
        width="100%"
    )
    
def boton_metodo_pago_admin(reserva: rx.Var, metodo_clave: str, nombre_logo: str, img_src: str) -> rx.Component:
    """Botón interactivo de método de pago para la tarjeta de reserva admin."""
    metodo_actual = reserva["metodo_pago_reserva"].to_string().lower()
    esta_seleccionado = (metodo_actual == metodo_clave.lower())

    return rx.box(
        rx.hstack(
            rx.cond(
                esta_seleccionado,
                rx.text("✓", font_weight="bold", color="#16A34A", size="1"),
                rx.fragment()
            ),
            rx.image(
                src=img_src,
                alt=nombre_logo,
                height="20px",
                object_fit="contain"
            ),
            spacing="1",
            align="center"
        ),
        padding="4px 8px",
        border_radius="6px",
        cursor="pointer",
        border=rx.cond(esta_seleccionado, "2px solid #16A34A", "1px solid #EAE5DF"),
        background_color=rx.cond(esta_seleccionado, "#DCFCE7", "#FFFFFF"),
        box_shadow=rx.cond(esta_seleccionado, "0px 0px 6px rgba(22, 163, 74, 0.4)", "0px 1px 3px rgba(0,0,0,0.05)"),
        transform=rx.cond(esta_seleccionado, "translateY(1px)", "none"),
        _hover={"border_color": "#16A34A"},
        on_click=lambda: State.seleccionar_metodo_pago_reserva_admin(reserva["id"], metodo_clave)
    )

def tarjeta_reserva_admin(reserva: rx.Var) -> rx.Component:
    """Tarjeta individual de reserva para el panel administrador adaptada a la vista de control."""
    pct_pago = reserva["porcentaje_pago"].to(float)
    monto_pend = reserva["monto_pendiente"].to(float)
    tiene_deuda = monto_pend > 0
    tiene_metodo_reserva = (reserva["metodo_pago_reserva"].to_string() != "")

    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.vstack(
                    rx.heading(reserva["sesion_nombre"], size="3", color="#2C3639", font_weight="bold"),
                    rx.text("📅 Fecha: ", reserva["fecha_texto"], " | Evento: ", reserva.get("fecha_evento", reserva["fecha_texto"]), size="2", color="#8E6F54"),
                    align="start",
                    spacing="0"
                ),
                rx.hstack(
                    rx.cond(
                        reserva["estado"] == "CONFIRMADO",
                        rx.badge(
                            "CONFIRMADO",
                            color="#000000",
                            background_color="#22C55E",
                            border="2px solid #15803D",
                            font_weight="bold",
                            size="2"
                        ),
                        rx.badge(
                            reserva["estado"],
                            color_scheme=rx.match(
                                reserva["estado"],
                                ("RECHAZADO", "red"),
                                "amber"
                            ),
                            size="2"
                        )
                    ),
                    rx.cond(
                        tiene_metodo_reserva,
                        rx.text(
                            "Reserva: " + reserva["metodo_pago_reserva"].to_string().upper(),
                            size="2",
                            color="#2C3639",
                            font_weight="medium"
                        )
                    ),
                    spacing="3",
                    align="center"
                ),
                justify="between",
                align="start",
                width="100%"
            ),

            rx.divider(color_scheme="gray", margin_y="8px"),

            rx.vstack(
                rx.text("👤 Cliente: ", reserva["nombre_cliente"], font_weight="bold", size="2", color="#2C3639"),
                rx.text("📞 WhatsApp: ", reserva["whatsapp_cliente"], size="2", color="#4B5563"),
                rx.text("🎟️ Cupos: ", reserva["cupos"].to_string(), " | Total: $", reserva["monto_total"].to_string(), " USD", size="2", font_weight="bold", color="#2C3639"),
                align="start",
                spacing="1"
            ),

            # Fila de Selector de Porcentaje + Píldora de Pendiente + Métodos de Pago
            rx.vstack(
                rx.text("Reservó con:", size="1", font_weight="bold", color="#2C3639"),
                rx.hstack(
                    rx.hstack(
                        rx.box(
                            rx.hstack(
                                rx.cond(pct_pago == 25.0, rx.text("✓", font_weight="bold", color="#2C3639"), rx.box(width="8px")),
                                rx.text("25%", size="1", color="#2C3639"),
                                spacing="1",
                                align="center"
                            ),
                            padding="4px 8px",
                            border="1px solid #D1D5DB",
                            border_radius="4px",
                            background_color=rx.cond(pct_pago == 25.0, "#FAF6F0", "#FFFFFF"),
                            cursor="pointer",
                            on_click=lambda: State.cambiar_porcentaje_reserva_admin(reserva["id"], 25.0)
                        ),
                        rx.box(
                            rx.hstack(
                                rx.cond(pct_pago == 50.0, rx.text("✓", font_weight="bold", color="#2C3639"), rx.box(width="8px")),
                                rx.text("50%", size="1", color="#2C3639"),
                                spacing="1",
                                align="center"
                            ),
                            padding="4px 8px",
                            border="1px solid #D1D5DB",
                            border_radius="4px",
                            background_color=rx.cond(pct_pago == 50.0, "#FAF6F0", "#FFFFFF"),
                            cursor="pointer",
                            on_click=lambda: State.cambiar_porcentaje_reserva_admin(reserva["id"], 50.0)
                        ),
                        rx.box(
                            rx.hstack(
                                rx.cond(pct_pago == 100.0, rx.text("✓", font_weight="bold", color="#2C3639"), rx.box(width="8px")),
                                rx.text("100%", size="1", color="#2C3639"),
                                spacing="1",
                                align="center"
                            ),
                            padding="4px 8px",
                            border="1px solid #D1D5DB",
                            border_radius="4px",
                            background_color=rx.cond(pct_pago == 100.0, "#FAF6F0", "#FFFFFF"),
                            cursor="pointer",
                            on_click=lambda: State.cambiar_porcentaje_reserva_admin(reserva["id"], 100.0)
                        ),
                        spacing="2",
                        align="center"
                    ),

                    # Píldora de Saldo Restante
                    rx.box(
                        rx.text(
                            rx.cond(
                                reserva["metodo_pago_reserva"].to_string().upper() == "CORTESIA",
                                "🎟️ Pase de Cortesía ($0)",
                                rx.cond(tiene_deuda, "Pendiente: " + reserva["monto_pendiente"].to_string() + "$", "100% Pagado")
                            ),
                            size="1",
                            font_weight="bold",
                            color=rx.cond(
                                reserva["metodo_pago_reserva"].to_string().upper() == "CORTESIA",
                                "#7C3AED",
                                rx.cond(tiene_deuda, "#DC2626", "#2E7D32")
                            )
                        ),
                        padding="4px 12px",
                        border_radius="15px",
                        border=rx.cond(
                            reserva["metodo_pago_reserva"].to_string().upper() == "CORTESIA",
                            "1.5px solid #7C3AED",
                            rx.cond(tiene_deuda, "1.5px solid #DC2626", "1.5px solid #2E7D32")
                        ),
                        background_color="#FFFFFF"
                    ),
                    spacing="3",
                    align="center",
                    flex_wrap="wrap"
                ),

                # Botones Interactivos de Métodos de Pago con Confirmación Visual
                rx.vstack(
                    rx.cond(
                        reserva["metodo_pago_reserva"] != "",
                        rx.hstack(
                            rx.text("Método Pago Seleccionado:", size="1", font_weight="bold", color="#2C3639"),
                            rx.text(reserva["metodo_pago_reserva"].to_string().upper(), size="2", color="#2C3639", font_weight="medium"),
                            spacing="2",
                            align="center"
                        )
                    ),
                    rx.hstack(
                        boton_metodo_pago_admin(reserva, "mastercard", "MasterCard", "/mastercard.png"),
                        boton_metodo_pago_admin(reserva, "zelle", "Zelle", "/zelle.png"),
                        boton_metodo_pago_admin(reserva, "binance", "Binance", "/binance.png"),
                        boton_metodo_pago_admin(reserva, "cash", "Cash", "/cash.png"),
                        boton_metodo_pago_admin(reserva, "transferencia", "Transferencia", "/tb.png"),
                        boton_metodo_pago_admin(reserva, "cortesia", "Pase de Cortesía", "/pdc.png"),
                        spacing="1",
                        align="center",
                        flex_wrap="wrap",
                        margin_top="2px"
                    ),
                    spacing="1",
                    align="start"
                ),

                align="start",
                spacing="1",
                padding_y="4px"
            ),

            rx.divider(color_scheme="gray", margin_y="8px"),

            # Acciones de Aprobación
            rx.hstack(
                rx.button(
                    "Aprobar y Confirmar",
                    size="2",
                    background_color=rx.cond(reserva["estado"] == "CONFIRMADO", "#9CA3AF", "#16A34A"),
                    color=rx.cond(reserva["estado"] == "CONFIRMADO", "#000000", "#FFFFFF"),
                    disabled=reserva["estado"] == "CONFIRMADO",
                    variant="solid",
                    on_click=lambda: State.aprobar_reserva_sesion(reserva["id"])
                ),
                rx.button(
                    "Rechazar",
                    size="2",
                    color_scheme="red",
                    variant="soft",
                    on_click=lambda: State.rechazar_reserva_sesion(reserva["id"])
                ),
                spacing="2",
                width="100%",
                justify="end"
            ),
            width="100%",
            spacing="2"
        ),
        background_color="#FFFFFF",
        border="1px solid #EAE5DF",
        border_radius="10px",
        padding="15px",
        box_shadow="0px 2px 8px rgba(0,0,0,0.04)",
        margin_bottom="12px",
        width="100%"
    )

def tarjeta_sesion_admin(sesion: rx.Var) -> rx.Component:
    """Tarjeta de gestión de sesión grupal para el panel administrador."""
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.vstack(
                    rx.hstack(
                        rx.heading(sesion["nombre"], size="3", color="#2C3639", font_weight="bold"),
                        rx.badge(
                            rx.cond(sesion["is_active"], "VISIBLE", "OCULTA"),
                            color_scheme=rx.cond(sesion["is_active"], "green", "gray"),
                            size="1"
                        ),
                        rx.cond(
                            sesion["patron_recurrencia"] != "MANUAL",
                            rx.badge(sesion["patron_recurrencia"], color_scheme="purple", size="1")
                        ),
                        spacing="2",
                        align="center"
                    ),
                    rx.text("📍 ", sesion["ubicacion"], size="2", color="#7F7F7F"),
                    rx.text("📅 Próxima cita: ", sesion["fecha_texto"], " • ", sesion["hora_texto"], size="2", font_weight="bold", color="#8E6F54"),
                    align="start",
                    spacing="0"
                ),
                rx.badge(
                    sesion["plazas_disponibles"].to_string() + " / " + sesion["plazas_totales"].to_string() + " cupos",
                    color_scheme="bronze",
                    size="2"
                ),
                justify="between",
                align="start",
                width="100%"
            ),

            rx.divider(color_scheme="gray", margin_y="8px"),

            # Botonera de Administración CRUD
            rx.hstack(
                rx.button(
                    "✏️ Editar",
                    size="2",
                    variant="outline",
                    color_scheme="bronze",
                    on_click=lambda: State.abrir_modal_editar_sesion(sesion)
                ),
                rx.button(
                    rx.cond(sesion["is_active"], "👁️ Ocultar", "🟢 Mostrar"),
                    size="2",
                    variant="soft",
                    color_scheme=rx.cond(sesion["is_active"], "amber", "green"),
                    on_click=lambda: State.toggle_estado_sesion_db(sesion["id"])
                ),
                rx.button(
                    "📋 Link Asistencia",
                    size="2",
                    variant="soft",
                    color_scheme="blue",
                    on_click=lambda: State.compartir_asistencia_whatsapp(sesion)
                ),
                rx.button(
                    "📝 Ver Lista",
                    size="2",
                    variant="soft",
                    color_scheme="bronze",
                    cursor="pointer",
                    on_click=lambda: State.abrir_lista_asistencia_admin(sesion)
                ),
                rx.button(
                    "🔑 Renov. Token",
                    size="2",
                    variant="ghost",
                    color_scheme="gray",
                    on_click=lambda: State.generar_nuevo_token_asistencia(sesion["id"])
                ),
                spacing="2",
                flex_wrap="wrap",
                width="100%"
            ),
            width="100%"
        ),
        background_color="#FFFFFF",
        border="1px solid #EAE5DF",
        border_radius="10px",
        padding="15px",
        margin_bottom="12px",
        width="100%"
    )

def modal_editor_sesion() -> rx.Component:
    """Modal para Crear o Editar Sesiones Grupales con contraste legible y botones de salida."""
    return rx.dialog.root(
        rx.dialog.content(
            rx.vstack(
                # Cabecera con título e icono de cerrar visible
                rx.hstack(
                    rx.heading(
                        rx.cond(State.sesion_id_edicion, "Editar Sesión Grupal", "Crear Nueva Sesión Grupal"),
                        size="4",
                        color="#2C3639",
                        style={"font-family": "Georgia, serif"}
                    ),
                    rx.icon(
                        tag="x",
                        size=20,
                        color="#2C3639",
                        cursor="pointer",
                        on_click=State.cerrar_modal_editor_sesion
                    ),
                    justify="between",
                    align="center",
                    width="100%"
                ),
                
                rx.divider(color_scheme="gray", margin_y="8px"),

                # Inputs de Edición con contraste de texto fijado (#2C3639 / #1A1A1A)
                rx.vstack(
                    rx.text("Nombre de la Sesión / Sede*", size="1", font_weight="bold", color="#2C3639"),
                    rx.input(
                        value=State.edit_sesion_nombre,
                        on_change=State.set_edit_sesion_nombre,
                        width="100%",
                        size="2",
                        color="#1A1A1A"
                    ),

                    rx.text("Ubicación / Ciudad*", size="1", font_weight="bold", color="#2C3639"),
                    rx.input(
                        value=State.edit_sesion_ubicacion,
                        on_change=State.set_edit_sesion_ubicacion,
                        width="100%",
                        size="2",
                        color="#1A1A1A"
                    ),

                    # 🔄 RECURRENCIA AUTOMÁTICA COMPLETA (CUALQUIER DÍA Y ORDEN)
                    rx.text("Patrón de Recurrencia (Renovación Automática)", size="1", font_weight="bold", color="#2C3639"),
                    rx.select(
                        State.lista_patrones_recurrencia_disponibles,
                        value=State.edit_sesion_patron_recurrencia,
                        on_change=State.set_edit_sesion_patron_recurrencia,
                        width="100%",
                        size="2",
                        color="#1A1A1A"
                    ),
                    rx.text("• Ejemplos: PRIMER_LUNES, SEGUNDO_MARTES, ULTIMO_JUEVES, etc.", size="1", color="#7F7F7F"),
                    rx.text("• El sistema calculará la fecha exacta del mes sin importar si la fecha numérica cambia.", size="1", color="#7F7F7F"),

                    rx.hstack(
                        rx.vstack(
                            rx.text("Fecha Texto", size="1", font_weight="bold", color="#2C3639"),
                            rx.input(
                                placeholder="Ej. 27/08/2026",
                                value=State.edit_sesion_fecha,
                                on_change=State.set_edit_sesion_fecha,
                                width="100%",
                                size="2",
                                color="#1A1A1A"
                            ),
                            width="33%"
                        ),
                        rx.vstack(
                            rx.text("Hora Cita (Duración)", size="1", font_weight="bold", color="#2C3639"),
                            rx.input(
                                placeholder="Ej. 5:30 pm a 6:30 pm",
                                value=State.edit_sesion_hora,
                                on_change=State.set_edit_sesion_hora,
                                width="100%",
                                size="2",
                                color="#1A1A1A"
                            ),
                            width="34%"
                        ),
                        rx.vstack(
                            rx.text("Hora de Recepción", size="1", font_weight="bold", color="#2C3639"),
                            rx.input(
                                placeholder="Ej. 5:00 PM",
                                value=State.edit_sesion_hora_recepcion,
                                on_change=State.set_edit_sesion_hora_recepcion,
                                width="100%",
                                size="2",
                                color="#1A1A1A"
                            ),
                            width="33%"
                        ),
                        width="100%"
                    ),

                    rx.hstack(
                        rx.vstack(
                            rx.text("Inversión (USD)", size="1", font_weight="bold", color="#2C3639"),
                            rx.input(
                                type="number",
                                value=State.edit_sesion_inversion.to_string(),
                                on_change=State.set_edit_sesion_inversion,
                                width="100%",
                                size="2",
                                color="#1A1A1A"
                            ),
                            width="50%"
                        ),
                        rx.vstack(
                            rx.text("Cupos Totales", size="1", font_weight="bold", color="#2C3639"),
                            rx.input(
                                type="number",
                                value=State.edit_sesion_plazas_totales.to_string(),
                                on_change=State.set_edit_sesion_plazas_totales,
                                width="100%",
                                size="2",
                                color="#1A1A1A"
                            ),
                            width="50%"
                        ),
                        width="100%"
                    ),

                    rx.text("URL Publicación Instagram", size="1", font_weight="bold", color="#2C3639"),
                    rx.input(
                        placeholder="https://instagram.com/reel/...",
                        value=State.edit_sesion_instagram,
                        on_change=State.set_edit_sesion_instagram,
                        width="100%",
                        size="2",
                        color="#1A1A1A"
                    ),

                    rx.text("Recomendaciones", size="1", font_weight="bold", color="#2C3639"),
                    rx.text_area(
                        value=State.edit_sesion_recomendaciones,
                        on_change=State.set_edit_sesion_recomendaciones,
                        width="100%",
                        size="2",
                        color="#1A1A1A"
                    ),

                    rx.divider(color_scheme="gray", margin_y="6px"),

                    # 🎛️ SWITCHES DE OBLIGATORIEDAD (CORREO Y PORCENTAJE DE RESERVA)
                    rx.vstack(
                        rx.text("⚙️ Configuración de Campos Obligatorios en Formulario", size="1", font_weight="bold", color="#8E6F54"),
                        rx.hstack(
                            rx.switch(
                                checked=State.edit_sesion_requiere_correo,
                                on_change=State.set_edit_sesion_requiere_correo,
                                color_scheme="bronze"
                            ),
                            rx.text("Hacer el Correo Electrónico OBLIGATORIO para cada participante", size="2", color="#2C3639"),
                            align="center",
                            spacing="2"
                        ),
                        rx.hstack(
                            rx.switch(
                                checked=State.edit_sesion_requiere_porcentaje,
                                on_change=State.set_edit_sesion_requiere_porcentaje,
                                color_scheme="bronze"
                            ),
                            rx.text("Hacer la Selección de Porcentaje de Reserva OBLIGATORIA", size="2", color="#2C3639"),
                            align="center",
                            spacing="2"
                        ),
                        spacing="2",
                        align="start",
                        width="100%",
                        background_color="#FAF6F0",
                        padding="10px",
                        border_radius="8px"
                    ),

                    spacing="2",
                    width="100%"
                ),

                # Botonera de Acción (Cancelar y Guardar)
                rx.hstack(
                    rx.button(
                        "Cancelar",
                        size="3",
                        variant="outline",
                        color_scheme="gray",
                        width="40%",
                        cursor="pointer",
                        on_click=State.cerrar_modal_editor_sesion
                    ),
                    rx.button(
                        "Guardar Sesión en Supabase",
                        size="3",
                        width="60%",
                        background_color="#8E6F54",
                        color="#FFFFFF",
                        font_weight="bold",
                        cursor="pointer",
                        _hover={"background_color": "#2C3639"},
                        on_click=State.guardar_sesion_db
                    ),
                    spacing="3",
                    width="100%",
                    padding_top="10px"
                ),
                spacing="3",
                width="100%"
            ),
            background_color="#FFFFFF",
            padding="25px",
            border_radius="12px",
            max_width="480px"
        ),
        open=State.modal_editor_sesion_abierto,
        on_open_change=State.set_modal_editor_sesion_abierto
    )
def tarjeta_producto_admin(prod: rx.Var) -> rx.Component:
    """Tarjeta individual de gestión de producto e inventario."""
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src=prod["foto_principal"],
                        width="50px",
                        height="50px",
                        object_fit="cover",
                        border_radius="6px"
                    ),
                    rx.vstack(
                        rx.hstack(
                            rx.heading(prod["nombre"], size="3", color="#2C3639", font_weight="bold"),
                            rx.badge(
                                rx.cond(prod["is_active"], "ACTIVO", "OCULTO"),
                                color_scheme=rx.cond(prod["is_active"], "green", "gray"),
                                size="1"
                            ),
                            spacing="2",
                            align="center"
                        ),
                        rx.text("Categoría: ", prod["categoria"], " | Proveedor: ", rx.cond(prod["proveedor"] != "", prod["proveedor"], "Sin proveedor"), " | Intención: ", rx.cond(prod["intencion"] != "", prod["intencion"], "Sin intención"), " | Precio: $", prod["precio"].to_string(), " USD", size="2", color="#8E6F54"),
                        align="start",
                        spacing="0"
                    ),
                    spacing="3",
                    align="center"
                ),
                
                # Control rápido de Stock en vivo
                rx.hstack(
                    rx.text("Stock:", size="2", font_weight="bold", color="#2C3639"),
                    rx.button("-", size="1", variant="outline", on_click=lambda: State.cambiar_stock_rapido(prod["id"], -1)),
                    rx.text(prod["stock"].to_string(), size="3", font_weight="bold", color="#2C3639", padding_x="4px"),
                    rx.button("+", size="1", variant="outline", on_click=lambda: State.cambiar_stock_rapido(prod["id"], 1)),
                    spacing="2",
                    align="center"
                ),
                justify="between",
                align="center",
                width="100%"
            ),

            rx.divider(color_scheme="gray", margin_y="8px"),

            # Acciones CRUD
            rx.hstack(
                rx.button(
                    "✏️ Editar Producto",
                    size="2",
                    variant="outline",
                    color_scheme="bronze",
                    on_click=lambda: State.abrir_modal_editar_producto(prod)
                ),
                rx.button(
                    rx.cond(prod["is_active"], "👁️ Ocultar", "🟢 Mostrar"),
                    size="2",
                    variant="soft",
                    color_scheme=rx.cond(prod["is_active"], "amber", "green"),
                    on_click=lambda: State.toggle_estado_producto_db(prod["id"])
                ),
                spacing="2",
                justify="end",
                width="100%"
            ),
            width="100%"
        ),
        background_color="#FFFFFF",
        border="1px solid #EAE5DF",
        border_radius="10px",
        padding="12px 15px",
        margin_bottom="10px",
        width="100%"
    )

def modal_editor_producto() -> rx.Component:
    """Modal para Crear o Editar Productos con autocompletado de categorías/proveedores y subida múltiple de fotos."""
    return rx.dialog.root(
        rx.dialog.content(
            rx.vstack(
                rx.hstack(
                    rx.heading(
                        rx.cond(State.producto_id_edicion, "Editar Producto", "Crear Nuevo Producto"),
                        size="4",
                        color="#2C3639",
                        style={"font-family": "Georgia, serif"}
                    ),
                    rx.icon(
                        tag="x",
                        size=20,
                        color="#2C3639",
                        cursor="pointer",
                        on_click=State.cerrar_modal_editor_producto
                    ),
                    justify="between",
                    align="center",
                    width="100%"
                ),

                rx.divider(color_scheme="gray", margin_y="8px"),

                rx.vstack(
                    rx.text("Nombre del Producto*", size="1", font_weight="bold", color="#2C3639"),
                    rx.input(
                        value=State.edit_prod_nombre,
                        on_change=State.set_edit_prod_nombre,
                        width="100%",
                        size="2",
                        color="#1A1A1A"
                    ),

                    # 🏷️ CAMPO CATEGORÍA CON AUTOCOMPLETADO DE SUPABASE O ESCRITURA LIBRE
                    rx.text("Categoría*", size="1", font_weight="bold", color="#2C3639"),
                    rx.input(
                        placeholder="Selecciona o escribe una nueva categoría...",
                        value=State.edit_prod_categoria,
                        on_change=State.set_edit_prod_categoria,
                        list="categorias-list",
                        width="100%",
                        size="2",
                        color="#1A1A1A"
                    ),
                    rx.el.datalist(
                        rx.foreach(
                            State.lista_categorias_unicas,
                            lambda cat: rx.el.option(value=cat)
                        ),
                        id="categorias-list"
                    ),

                    # 🏭 CAMPO PROVEEDOR CON AUTOCOMPLETADO
                    rx.text("Proveedor*", size="1", font_weight="bold", color="#2C3639"),
                    rx.input(
                        placeholder="Ej. Tiendas C.A",
                        value=State.edit_prod_proveedor,
                        on_change=State.set_edit_prod_proveedor,
                        list="proveedores-list",
                        width="100%",
                        size="2",
                        color="#1A1A1A"
                    ),
                    rx.el.datalist(
                        rx.foreach(
                            State.lista_proveedores_unicos,
                            lambda prov: rx.el.option(value=prov)
                        ),
                        id="proveedores-list"
                    ),

                    rx.text("Comprar según la Intención (Opcional)", size="1", font_weight="bold", color="#2C3639"),
                    rx.select(
                        ["Ninguna", "Plantar y restaurar", "Claridad y enfoque", "Corazón y conexión", "Descanso y sueño"],
                        value=rx.cond(State.edit_prod_intencion != "", State.edit_prod_intencion, "Ninguna"),
                        on_change=State.set_edit_prod_intencion,
                        width="100%",
                        size="2",
                        color="#1A1A1A"
                    ),

                    rx.hstack(
                        rx.vstack(
                            rx.text("Precio (USD)*", size="1", font_weight="bold", color="#2C3639"),
                            rx.input(
                                type="number",
                                value=State.edit_prod_precio.to_string(),
                                on_change=State.set_edit_prod_precio,
                                width="100%",
                                size="2",
                                color="#1A1A1A"
                            ),
                            width="50%"
                        ),
                        rx.vstack(
                            rx.text("Stock Inicial*", size="1", font_weight="bold", color="#2C3639"),
                            rx.input(
                                type="number",
                                value=State.edit_prod_stock.to_string(),
                                on_change=State.set_edit_prod_stock,
                                width="100%",
                                size="2",
                                color="#1A1A1A"
                            ),
                            width="50%"
                        ),
                        width="100%"
                    ),

                    # 🖼️ GALERÍA DE MÚLTIPLES FOTOS CON VISTA PREVIA Y SUBIDA
                    rx.text("Galería de Fotos del Producto (JSONB)", size="1", font_weight="bold", color="#2C3639"),
                    rx.cond(
                        State.edit_prod_fotos.length() > 0,
                        rx.flex(
                            rx.foreach(
                                State.edit_prod_fotos,
                                lambda url: rx.box(
                                    rx.image(
                                        src=url,
                                        width="65px",
                                        height="65px",
                                        object_fit="cover",
                                        border_radius="6px",
                                        border="1px solid #EAE5DF"
                                    ),
                                    rx.button(
                                        "❌",
                                        size="1",
                                        variant="solid",
                                        color_scheme="red",
                                        position="absolute",
                                        top="-6px",
                                        right="-6px",
                                        border_radius="50%",
                                        width="18px",
                                        height="18px",
                                        padding="0",
                                        font_size="9px",
                                        cursor="pointer",
                                        on_click=lambda: State.eliminar_foto_producto(url)
                                    ),
                                    position="relative",
                                    margin_right="8px",
                                    margin_bottom="8px"
                                )
                            ),
                            flex_wrap="wrap",
                            padding_y="4px"
                        ),
                        rx.text("Sin fotos agregadas aún.", size="1", color="#7F7F7F")
                    ),

                    rx.hstack(
                        rx.input(
                            placeholder="Añadir URL manual (/ig_post1.png o https://...)",
                            value=State.edit_prod_foto,
                            on_change=State.set_edit_prod_foto,
                            width="70%",
                            size="2",
                            color="#1A1A1A"
                        ),
                        rx.button(
                            "➕ Añadir",
                            size="2",
                            variant="soft",
                            color_scheme="bronze",
                            width="30%",
                            on_click=State.agregar_url_foto_manual
                        ),
                        width="100%"
                    ),

                    rx.upload(
                        rx.vstack(
                            rx.button("📁 Seleccionar Fotos del Producto (Múltiples)", size="1", variant="soft", color_scheme="bronze", type="button"),
                            rx.text("Selecciona o arrastra una o varias imágenes", size="1", color="#7F7F7F"),
                            align="center",
                            spacing="1"
                        ),
                        id="upload_prod_foto",
                        multiple=True,
                        border="1px dashed #EAE5DF",
                        padding="8px",
                        border_radius="6px",
                        width="100%",
                        accept={"image/*": [".png", ".jpg", ".jpeg", ".webp"]}
                    ),
                    rx.cond(
                        rx.selected_files("upload_prod_foto").length() > 0,
                        rx.button(
                            "☁️ Subir Imágenes a Supabase",
                            size="2",
                            color_scheme="green",
                            width="100%",
                            on_click=State.subir_foto_producto(rx.upload_files(upload_id="upload_prod_foto"))
                        )
                    ),

                    rx.text("Descripción", size="1", font_weight="bold", color="#2C3639"),
                    rx.text_area(
                        value=State.edit_prod_descripcion,
                        on_change=State.set_edit_prod_descripcion,
                        width="100%",
                        size="2",
                        color="#1A1A1A"
                    ),

                    rx.hstack(
                        rx.checkbox(
                            "Más Vendido",
                            checked=State.edit_prod_is_best_seller,
                            on_change=State.set_edit_prod_is_best_seller,
                            color_scheme="brown"
                        ),
                        rx.checkbox(
                            "Favorito Seleccionado",
                            checked=State.edit_prod_is_favorite,
                            on_change=State.set_edit_prod_is_favorite,
                            color_scheme="brown"
                        ),
                        spacing="4",
                        padding_y="5px"
                    ),

                    spacing="2",
                    width="100%"
                ),

                rx.hstack(
                    rx.button(
                        "Cancelar",
                        size="3",
                        variant="outline",
                        color_scheme="gray",
                        width="40%",
                        cursor="pointer",
                        on_click=State.cerrar_modal_editor_producto
                    ),
                    rx.button(
                        "Guardar Producto",
                        size="3",
                        width="60%",
                        background_color="#8E6F54",
                        color="#FFFFFF",
                        font_weight="bold",
                        cursor="pointer",
                        _hover={"background_color": "#2C3639"},
                        on_click=State.guardar_producto_db
                    ),
                    spacing="3",
                    width="100%",
                    padding_top="10px"
                ),
                spacing="3",
                width="100%"
            ),
            background_color="#FFFFFF",
            padding="25px",
            border_radius="12px",
            max_width="480px"
        ),
        open=State.modal_editor_producto_abierto,
        on_open_change=State.set_modal_editor_producto_abierto
    )


def tarjeta_taller_admin(taller: rx.Var) -> rx.Component:
    """Tarjeta individual de gestión de Talleres y Eventos."""
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.vstack(
                    rx.hstack(
                        rx.heading(taller["titulo"], size="3", color="#2C3639", font_weight="bold"),
                        rx.badge(
                            taller["tipo"],
                            color_scheme="bronze",
                            size="1"
                        ),
                        spacing="2",
                        align="center"
                    ),
                    rx.text("📍 ", taller["ubicacion"], " • 👤 Facilitador: ", taller["facilitador"], size="2", color="#7F7F7F"),
                    rx.text("📅 ", taller["fecha_texto"], " • ", taller["hora_texto"], " ($", taller["precio"].to_string(), " ", taller["moneda"], ")", size="2", color="#8E6F54"),
                    align="start",
                    spacing="0"
                ),
                rx.button(
                    "✏️ Editar",
                    size="2",
                    variant="outline",
                    color_scheme="bronze",
                    on_click=lambda: State.abrir_modal_editar_taller(taller)
                ),
                justify="between",
                align="start",
                width="100%"
            ),

            rx.divider(color_scheme="gray", margin_y="8px"),

            rx.hstack(
                rx.text("WhatsApp Contacto: ", taller["whatsapp_contacto"], size="2", color="#4B5563"),
                spacing="2",
                justify="between",
                align="center",
                width="100%"
            ),
            width="100%"
        ),
        background_color="#FFFFFF",
        border="1px solid #EAE5DF",
        border_radius="10px",
        padding="12px 15px",
        margin_bottom="10px",
        width="100%"
    )

def modal_editor_taller() -> rx.Component:
    """Modal para Crear o Editar Talleres y Eventos."""
    return rx.dialog.root(
        rx.dialog.content(
            rx.vstack(
                rx.hstack(
                    rx.heading(
                        rx.cond(State.taller_id_edicion, "Editar Taller / Evento", "Crear Nuevo Taller"),
                        size="4",
                        color="#2C3639",
                        style={"font-family": "Georgia, serif"}
                    ),
                    rx.icon(
                        tag="x",
                        size=20,
                        color="#2C3639",
                        cursor="pointer",
                        on_click=State.cerrar_modal_editor_taller
                    ),
                    justify="between",
                    align="center",
                    width="100%"
                ),

                rx.divider(color_scheme="gray", margin_y="8px"),

                rx.vstack(
                    rx.text("Título del Taller / Evento*", size="1", font_weight="bold", color="#2C3639"),
                    rx.input(
                        value=State.edit_taller_titulo,
                        on_change=State.set_edit_taller_titulo,
                        width="100%",
                        size="2",
                        color="#1A1A1A"
                    ),

                    rx.hstack(
                        rx.vstack(
                            rx.text("Tipo / Etiqueta", size="1", font_weight="bold", color="#2C3639"),
                            rx.input(
                                placeholder="Ej. Taller, Ceremonia, Concierto",
                                value=State.edit_taller_tipo,
                                on_change=State.set_edit_taller_tipo,
                                width="100%",
                                size="2",
                                color="#1A1A1A"
                            ),
                            width="50%"
                        ),
                        rx.vstack(
                            rx.text("Facilitador Principal", size="1", font_weight="bold", color="#2C3639"),
                            rx.input(
                                placeholder="Ej. Danibeth / Jesús Buraglia",
                                value=State.edit_taller_facilitador,
                                on_change=State.set_edit_taller_facilitador,
                                width="100%",
                                size="2",
                                color="#1A1A1A"
                            ),
                            width="50%"
                        ),
                        width="100%"
                    ),

                    rx.text("Ubicación / Lugar*", size="1", font_weight="bold", color="#2C3639"),
                    rx.input(
                        placeholder="Ej. Casa Morada, Caracas",
                        value=State.edit_taller_ubicacion,
                        on_change=State.set_edit_taller_ubicacion,
                        width="100%",
                        size="2",
                        color="#1A1A1A"
                    ),

                    rx.hstack(
                        rx.vstack(
                            rx.text("Fecha Texto", size="1", font_weight="bold", color="#2C3639"),
                            rx.input(
                                placeholder="Ej. Sábado 25 Nov",
                                value=State.edit_taller_fecha_texto,
                                on_change=State.set_edit_taller_fecha_texto,
                                width="100%",
                                size="2",
                                color="#1A1A1A"
                            ),
                            width="50%"
                        ),
                        rx.vstack(
                            rx.text("Hora Texto", size="1", font_weight="bold", color="#2C3639"),
                            rx.input(
                                placeholder="Ej. 4:00 PM",
                                value=State.edit_taller_hora_texto,
                                on_change=State.set_edit_taller_hora_texto,
                                width="100%",
                                size="2",
                                color="#1A1A1A"
                            ),
                            width="50%"
                        ),
                        width="100%"
                    ),

                    rx.hstack(
                        rx.vstack(
                            rx.text("Inversión / Precio", size="1", font_weight="bold", color="#2C3639"),
                            rx.input(
                                type="number",
                                value=State.edit_taller_precio.to_string(),
                                on_change=State.set_edit_taller_precio,
                                width="100%",
                                size="2",
                                color="#1A1A1A"
                            ),
                            width="50%"
                        ),
                        rx.vstack(
                            rx.text("WhatsApp de Contacto", size="1", font_weight="bold", color="#2C3639"),
                            rx.input(
                                placeholder="Ej. 584241359530",
                                value=State.edit_taller_whatsapp,
                                on_change=State.set_edit_taller_whatsapp,
                                width="100%",
                                size="2",
                                color="#1A1A1A"
                            ),
                            width="50%"
                        ),
                        width="100%"
                    ),

                    rx.text("URL Foto / Portada", size="1", font_weight="bold", color="#2C3639"),
                    rx.input(
                        placeholder="/Galeria_foto2d.jpg o https://...",
                        value=State.edit_taller_foto,
                        on_change=State.set_edit_taller_foto,
                        width="100%",
                        size="2",
                        color="#1A1A1A"
                    ),

                    rx.text("Descripción Corta", size="1", font_weight="bold", color="#2C3639"),
                    rx.text_area(
                        value=State.edit_taller_descripcion,
                        on_change=State.set_edit_taller_descripcion,
                        width="100%",
                        size="2",
                        color="#1A1A1A"
                    ),

                    spacing="2",
                    width="100%"
                ),

                rx.hstack(
                    rx.button(
                        "Cancelar",
                        size="3",
                        variant="outline",
                        color_scheme="gray",
                        width="40%",
                        cursor="pointer",
                        on_click=State.cerrar_modal_editor_taller
                    ),
                    rx.button(
                        "Guardar Taller",
                        size="3",
                        width="60%",
                        background_color="#8E6F54",
                        color="#FFFFFF",
                        font_weight="bold",
                        cursor="pointer",
                        _hover={"background_color": "#2C3639"},
                        on_click=State.guardar_taller_db
                    ),
                    spacing="3",
                    width="100%",
                    padding_top="10px"
                ),
                spacing="3",
                width="100%"
            ),
            background_color="#FFFFFF",
            padding="25px",
            border_radius="12px",
            max_width="480px"
        ),
        open=State.modal_editor_taller_abierto,
        on_open_change=State.set_modal_editor_taller_abierto
    )
def tarjeta_servicio_admin(servicio: rx.Var) -> rx.Component:
    """Tarjeta individual de gestión de Servicios."""
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src=servicio["foto"],
                        width="50px",
                        height="50px",
                        object_fit="cover",
                        border_radius="6px"
                    ),
                    rx.vstack(
                        rx.hstack(
                            rx.heading(servicio["nombre"], size="3", color="#2C3639", font_weight="bold"),
                            rx.badge(
                                rx.cond(servicio["is_active"], "ACTIVO", "OCULTO"),
                                color_scheme=rx.cond(servicio["is_active"], "green", "gray"),
                                size="1"
                            ),
                            spacing="2",
                            align="center"
                        ),
                        rx.text(servicio["descripcion"], size="2", color="#7F7F7F", line_clamp="1"),
                        align="start",
                        spacing="0"
                    ),
                    spacing="3",
                    align="center"
                ),
                rx.hstack(
                    rx.button(
                        "✏️ Editar",
                        size="2",
                        variant="outline",
                        color_scheme="bronze",
                        on_click=lambda: State.abrir_modal_editar_servicio(servicio)
                    ),
                    rx.button(
                        rx.cond(servicio["is_active"], "👁️ Ocultar", "🟢 Mostrar"),
                        size="2",
                        variant="soft",
                        color_scheme=rx.cond(servicio["is_active"], "amber", "green"),
                        on_click=lambda: State.toggle_estado_servicio_db(servicio["id"])
                    ),
                    spacing="2"
                ),
                justify="between",
                align="center",
                width="100%"
            ),
            width="100%"
        ),
        background_color="#FFFFFF",
        border="1px solid #EAE5DF",
        border_radius="10px",
        padding="12px 15px",
        margin_bottom="10px",
        width="100%"
    )

def modal_editor_servicio() -> rx.Component:
    """Modal para Crear o Editar Servicios."""
    return rx.dialog.root(
        rx.dialog.content(
            rx.vstack(
                rx.hstack(
                    rx.heading(
                        rx.cond(State.servicio_id_edicion, "Editar Servicio", "Crear Nuevo Servicio"),
                        size="4",
                        color="#2C3639",
                        style={"font-family": "Georgia, serif"}
                    ),
                    rx.icon(
                        tag="x",
                        size=20,
                        color="#2C3639",
                        cursor="pointer",
                        on_click=State.cerrar_modal_editor_servicio
                    ),
                    justify="between",
                    align="center",
                    width="100%"
                ),

                rx.divider(color_scheme="gray", margin_y="8px"),

                rx.vstack(
                    rx.text("Nombre del Servicio*", size="1", font_weight="bold", color="#2C3639"),
                    rx.input(
                        value=State.edit_servicio_nombre,
                        on_change=State.set_edit_servicio_nombre,
                        width="100%",
                        size="2",
                        color="#1A1A1A"
                    ),

                    rx.text("URL Foto / Imagen", size="1", font_weight="bold", color="#2C3639"),
                    rx.input(
                        placeholder="/Galeria_foto1.jpg o https://...",
                        value=State.edit_servicio_foto,
                        on_change=State.set_edit_servicio_foto,
                        width="100%",
                        size="2",
                        color="#1A1A1A"
                    ),

                    rx.text("Descripción", size="1", font_weight="bold", color="#2C3639"),
                    rx.text_area(
                        value=State.edit_servicio_descripcion,
                        on_change=State.set_edit_servicio_descripcion,
                        width="100%",
                        size="2",
                        color="#1A1A1A"
                    ),

                    spacing="2",
                    width="100%"
                ),

                rx.hstack(
                    rx.button(
                        "Cancelar",
                        size="3",
                        variant="outline",
                        color_scheme="gray",
                        width="40%",
                        cursor="pointer",
                        on_click=State.cerrar_modal_editor_servicio
                    ),
                    rx.button(
                        "Guardar Servicio",
                        size="3",
                        width="60%",
                        background_color="#8E6F54",
                        color="#FFFFFF",
                        font_weight="bold",
                        cursor="pointer",
                        _hover={"background_color": "#2C3639"},
                        on_click=State.guardar_servicio_db
                    ),
                    spacing="3",
                    width="100%",
                    padding_top="10px"
                ),
                spacing="3",
                width="100%"
            ),
            background_color="#FFFFFF",
            padding="25px",
            border_radius="12px",
            max_width="480px"
        ),
        open=State.modal_editor_servicio_abierto,
        on_open_change=State.set_modal_editor_servicio_abierto
    )
def modal_editor_crm() -> rx.Component:
    """Modal flotante para actualizar notas internas y etiquetas de clientes."""
    return rx.dialog.root(
        rx.dialog.content(
            rx.vstack(
                rx.hstack(
                    rx.heading("📝 Editar Cliente / Notas Internas", size="4", color="#2C3639", style={"font-family": "Georgia, serif"}),
                    rx.icon(
                        tag="x",
                        size=20,
                        color="#2C3639",
                        cursor="pointer",
                        on_click=lambda: State.set_modal_editor_crm_abierto(False)
                    ),
                    justify="between",
                    align="center",
                    width="100%"
                ),
                rx.divider(color_scheme="gray", margin_y="8px"),
                rx.vstack(
                    rx.text("Categoría / Etiqueta del Cliente:", size="2", font_weight="bold", color="#2C3639"),
                    rx.select(
                        ["NUEVO", "FRECUENTE", "INACTIVO", "VIP"],
                        value=State.edit_crm_etiqueta,
                        on_change=State.set_edit_crm_etiqueta,
                        width="100%"
                    ),
                    rx.text("Notas Internas del Facilitador:", size="2", font_weight="bold", color="#2C3639", margin_top="10px"),
                    rx.text_area(
                        placeholder="Ej: Prefiere sentarse cerca de los cuencos, sensible a la vibración...",
                        value=State.edit_crm_notas,
                        on_change=State.set_edit_crm_notas,
                        rows="4",
                        width="100%"
                    ),
                    rx.hstack(
                        rx.button(
                            "Cancelar",
                            size="2",
                            variant="outline",
                            color_scheme="gray",
                            cursor="pointer",
                            on_click=lambda: State.set_modal_editor_crm_abierto(False)
                        ),
                        rx.button(
                            "Guardar Cambios",
                            size="2",
                            background_color="#8E6F54",
                            color="#FFFFFF",
                            cursor="pointer",
                            on_click=State.guardar_nota_cliente_crm
                        ),
                        justify="end",
                        width="100%",
                        margin_top="15px"
                    ),
                    spacing="3",
                    width="100%"
                ),
                spacing="3",
                width="100%"
            ),
            background_color="#FFFFFF",
            padding="25px",
            border_radius="12px",
            max_width="480px"
        ),
        open=State.modal_editor_crm_abierto,
        on_open_change=State.set_modal_editor_crm_abierto
    )

def modal_mensaje_1a1_crm() -> rx.Component:
    """Modal flotante para redactar y enviar mensajes personalizados 1-a-1 vía WhatsApp."""
    return rx.dialog.root(
        rx.dialog.content(
            rx.vstack(
                rx.hstack(
                    rx.heading(
                        "💬 Mensaje 1-a-1: " + State.mensaje_1a1_destinatario_nombre,
                        size=rx.breakpoints(initial="3", sm="4"),
                        color="#2C3639",
                        style={"font-family": "Georgia, serif"}
                    ),
                    rx.icon(
                        tag="x",
                        size=20,
                        color="#2C3639",
                        cursor="pointer",
                        on_click=State.cerrar_modal_mensaje_1a1
                    ),
                    justify="between",
                    align="center",
                    width="100%"
                ),
                rx.divider(color_scheme="gray", margin_y="8px"),
                rx.vstack(
                    rx.flex(
                        rx.vstack(
                            rx.text("Destinatario (WhatsApp):", size="2", font_weight="bold", color="#2C3639"),
                            rx.badge(State.mensaje_1a1_destinatario_wa, color_scheme="green", size="2"),
                            align="start",
                            spacing="1",
                            min_width="150px"
                        ),
                        rx.vstack(
                            rx.text("Sesión a promocionar:", size="2", font_weight="bold", color="#2C3639"),
                            rx.select(
                                State.opciones_sesiones_invitacion,
                                value=State.mensaje_1a1_sesion_id_seleccionada,
                                on_change=State.cambiar_sesion_invitacion,
                                size="2",
                                width="100%"
                            ),
                            align="start",
                            spacing="1",
                            flex="1",
                            width="100%"
                        ),
                        width="100%",
                        gap="12px",
                        flex_direction=rx.breakpoints(initial="column", sm="row"),
                        align_items=rx.breakpoints(initial="stretch", sm="center")
                    ),
                    rx.text("Mensaje Personalizado (Plantilla Auto-generada):", size="2", font_weight="bold", color="#2C3639", margin_top="10px"),
                    rx.text_area(
                        placeholder="Escribe el mensaje directo para el cliente...",
                        value=State.mensaje_1a1_texto,
                        on_change=State.set_mensaje_1a1_texto,
                        rows="10",
                        width="100%",
                        style={"font-size": "14px"}
                    ),
                    rx.hstack(
                        rx.button(
                            "Cancelar",
                            size="2",
                            variant="outline",
                            color_scheme="gray",
                            cursor="pointer",
                            on_click=State.cerrar_modal_mensaje_1a1
                        ),
                        rx.button(
                            "📱 Enviar por WhatsApp",
                            size="2",
                            background_color="#25D366",
                            color="#FFFFFF",
                            font_weight="bold",
                            cursor="pointer",
                            on_click=State.enviar_mensaje_1a1_whatsapp
                        ),
                        justify="end",
                        width="100%",
                        margin_top="15px"
                    ),
                    spacing="3",
                    width="100%"
                ),
                spacing="3",
                width="100%"
            ),
            background_color="#FFFFFF",
            padding=rx.breakpoints(initial="16px", sm="25px"),
            border_radius="12px",
            max_width="600px",
            width=rx.breakpoints(initial="95vw", sm="100%"),
            max_height="90vh",
            overflow_y="auto"
        ),
        open=State.modal_mensaje_1a1_abierto,
        on_open_change=State.set_modal_mensaje_1a1_abierto
    )

def tarjeta_cliente_crm(cliente: rx.Var) -> rx.Component:
    """Tarjeta individual de cliente consolidado en el CRM optimizada para pantallas móviles."""
    return rx.box(
        rx.flex(
            rx.vstack(
                rx.hstack(
                    rx.badge(
                        cliente["etiqueta"],
                        color_scheme=rx.cond(
                            cliente["etiqueta"] == "FRECUENTE", "green",
                            rx.cond(cliente["etiqueta"] == "VIP", "purple", "blue")
                        ),
                        size="1"
                    ),
                    rx.heading(cliente["nombre"], size="3", color="#2C3639", font_weight="bold"),
                    align="center",
                    spacing="2",
                    flex_wrap="wrap"
                ),
                rx.hstack(
                    rx.icon(tag="phone", size=14, color="#8E6F54"),
                    rx.link(
                        cliente["whatsapp"],
                        href="https://wa.me/" + cliente["whatsapp"].to_string(),
                        is_external=True,
                        size="2",
                        color="#8E6F54",
                        text_decoration="underline"
                    ),
                    rx.cond(
                        cliente["email"] != "",
                        rx.hstack(
                            rx.icon(tag="mail", size=14, color="#7F7F7F"),
                            rx.text(cliente["email"], size="2", color="#7F7F7F", style={"word-break": "break-all"}),
                            spacing="1",
                            align="center"
                        )
                    ),
                    spacing="3",
                    align="center",
                    flex_wrap="wrap"
                ),
                rx.cond(
                    cliente["notas_internas"] != "",
                    rx.box(
                        rx.text("📌 ", cliente["notas_internas"], size="2", color="#4A5568", font_style="italic"),
                        padding="6px 10px",
                        background_color="#FAF6F0",
                        border_left="3px solid #8E6F54",
                        border_radius="4px",
                        margin_top="4px",
                        width="100%"
                    )
                ),
                align="start",
                spacing="1",
                width="100%"
            ),
            rx.flex(
                rx.hstack(
                    rx.vstack(
                        rx.text("Reservas", size="1", color="#7F7F7F"),
                        rx.text(cliente["total_reservas"], size="3", font_weight="bold", color="#2C3639"),
                        align="center",
                        spacing="0"
                    ),
                    rx.vstack(
                        rx.text("Asistencias", size="1", color="#7F7F7F"),
                        rx.text(cliente["asistencias"], size="3", font_weight="bold", color="#2E7D32"),
                        align="center",
                        spacing="0"
                    ),
                    rx.vstack(
                        rx.text("Inversión", size="1", color="#7F7F7F"),
                        rx.text("$", cliente["inversion_total"], size="3", font_weight="bold", color="#8E6F54"),
                        align="center",
                        spacing="0"
                    ),
                    spacing="4",
                    align="center"
                ),
                rx.hstack(
                    rx.button(
                        "💬 Mensaje 1-a-1",
                        size="2",
                        variant="solid",
                        color_scheme="green",
                        cursor="pointer",
                        on_click=lambda: State.abrir_modal_mensaje_1a1(cliente)
                    ),
                    rx.button(
                        "✏️ Notas",
                        size="2",
                        variant="soft",
                        color_scheme="brown",
                        cursor="pointer",
                        on_click=lambda: State.abrir_modal_editar_crm(cliente)
                    ),
                    spacing="2",
                    align="center",
                    flex_wrap="wrap"
                ),
                justify="between",
                align="center",
                flex_wrap="wrap",
                gap="10px",
                width="100%"
            ),
            justify="between",
            align_items="stretch",
            flex_direction="column",
            gap="12px",
            width="100%"
        ),
        background_color="#FFFFFF",
        border="1px solid #EAE5DF",
        border_radius="10px",
        padding="14px",
        margin_bottom="10px",
        width="100%"
    )

def panel_admin_logueado() -> rx.Component:
    """Panel principal de administración autenticado con módulos unificados CRM."""
    return rx.vstack(
        # Cabecera Admin
        rx.hstack(
            rx.heading(
                "Panel de Control Administrador",
                id="seccion-admin-panel",
                size="6",
                color="#2C3639",
                style={"font-family": "Georgia, serif", "scroll-margin-top": "120px"}
            ),
            rx.button("Cerrar Sesión Admin", size="2", variant="outline", color_scheme="red", on_click=State.logout_admin),
            justify="between",
            align="center",
            width="100%"
        ),
        
        rx.divider(margin_y="15px"),

        # Pestañas de Navegación Administrador
        rx.hstack(
            rx.button(
                "👥 Clientes / CRM",
                size="2",
                variant=rx.cond(State.admin_tab_activa == "crm", "solid", "ghost"),
                background_color=rx.cond(State.admin_tab_activa == "crm", "#8E6F54", "transparent"),
                color=rx.cond(State.admin_tab_activa == "crm", "#FFFFFF", "#2C3639"),
                on_click=lambda: State.set_admin_tab("crm")
            ),
            rx.button(
                "📋 Reservas",
                size="2",
                variant=rx.cond(State.admin_tab_activa == "reservas", "solid", "ghost"),
                background_color=rx.cond(State.admin_tab_activa == "reservas", "#8E6F54", "transparent"),
                color=rx.cond(State.admin_tab_activa == "reservas", "#FFFFFF", "#2C3639"),
                on_click=lambda: State.set_admin_tab("reservas")
            ),
            rx.button(
                "📦 Confirmar Pedidos",
                size="2",
                variant=rx.cond(State.admin_tab_activa == "pedidos", "solid", "ghost"),
                background_color=rx.cond(State.admin_tab_activa == "pedidos", "#8E6F54", "transparent"),
                color=rx.cond(State.admin_tab_activa == "pedidos", "#FFFFFF", "#2C3639"),
                on_click=lambda: State.set_admin_tab("pedidos")
            ),
            rx.button(
                "🧘‍♂️ Sesiones",
                size="2",
                variant=rx.cond(State.admin_tab_activa == "sesiones", "solid", "ghost"),
                background_color=rx.cond(State.admin_tab_activa == "sesiones", "#8E6F54", "transparent"),
                color=rx.cond(State.admin_tab_activa == "sesiones", "#FFFFFF", "#2C3639"),
                on_click=lambda: State.set_admin_tab("sesiones")
            ),
            rx.button(
                "🛒 Productos y Stock",
                size="2",
                variant=rx.cond(State.admin_tab_activa == "productos", "solid", "ghost"),
                background_color=rx.cond(State.admin_tab_activa == "productos", "#8E6F54", "transparent"),
                color=rx.cond(State.admin_tab_activa == "productos", "#FFFFFF", "#2C3639"),
                on_click=lambda: State.set_admin_tab("productos")
            ),
            rx.button(
                "🛖 Talleres",
                size="2",
                variant=rx.cond(State.admin_tab_activa == "talleres", "solid", "ghost"),
                background_color=rx.cond(State.admin_tab_activa == "talleres", "#8E6F54", "transparent"),
                color=rx.cond(State.admin_tab_activa == "talleres", "#FFFFFF", "#2C3639"),
                on_click=lambda: State.set_admin_tab("talleres")
            ),
            rx.button(
                "✨ Servicios",
                size="2",
                variant=rx.cond(State.admin_tab_activa == "servicios", "solid", "ghost"),
                background_color=rx.cond(State.admin_tab_activa == "servicios", "#8E6F54", "transparent"),
                color=rx.cond(State.admin_tab_activa == "servicios", "#FFFFFF", "#2C3639"),
                on_click=lambda: State.set_admin_tab("servicios")
            ),
            rx.button(
                "🎟️ Cupones",
                size="2",
                variant=rx.cond(State.admin_tab_activa == "cupones", "solid", "ghost"),
                background_color=rx.cond(State.admin_tab_activa == "cupones", "#8E6F54", "transparent"),
                color=rx.cond(State.admin_tab_activa == "cupones", "#FFFFFF", "#2C3639"),
                on_click=lambda: State.set_admin_tab("cupones")
            ),
            spacing="2",
            flex_wrap="wrap",
            width="100%"
        ),

        rx.divider(margin_y="10px"),

        # Contenido Dinámico de Pestañas con rx.match (Estructura Limpia)
        rx.match(
            State.admin_tab_activa,
            # Pestaña CRM
            (
                "crm",
                rx.vstack(
                    modal_editor_crm(),
                    modal_mensaje_1a1_crm(),
                    rx.heading("Directorio de Clientes y Comunidad (CRM)", size="4", color="#2C3639"),
                    rx.hstack(
                        rx.input(
                            placeholder="🔍 Buscar por nombre, teléfono o correo...",
                            value=State.busqueda_cliente_crm,
                            on_change=State.set_busqueda_cliente_crm,
                            size="2",
                            border_radius="8px",
                            flex="1"
                        ),
                        rx.select(
                            ["TODOS", "NUEVO", "FRECUENTE", "INACTIVO", "VIP"],
                            value=State.filtro_etiqueta_crm,
                            on_change=State.set_filtro_etiqueta_crm,
                            size="2",
                            border_radius="8px"
                        ),
                        rx.button(
                            "📥 Exportar CSV",
                            size="2",
                            variant="soft",
                            color_scheme="green",
                            cursor="pointer",
                            on_click=State.exportar_clientes_csv
                        ),
                        width="100%",
                        gap="10px",
                        flex_wrap="wrap",
                        margin_bottom="15px"
                    ),
                    rx.cond(
                        State.clientes_crm_filtrados.length() == 0,
                        rx.text("No se encontraron clientes registrados en la base de datos.", color="#7F7F7F"),
                        rx.foreach(State.clientes_crm_filtrados, tarjeta_cliente_crm)
                    ),
                    width="100%",
                    spacing="3"
                )
            ),
            # Pestaña Pedidos
            (
                "pedidos",
                rx.vstack(
                    rx.heading("Confirmación de Pedidos y Compras Recibidas", size="4", color="#2C3639"),
                    rx.cond(
                        State.ordenes_admin_list.length() == 0,
                        rx.text("No hay pedidos registrados actualmente.", color="#7F7F7F"),
                        rx.foreach(State.ordenes_admin_list, tarjeta_orden_admin)
                    ),
                    width="100%",
                    spacing="3"
                )
            ),
            # Pestaña Reservas
            (
                "reservas",
                rx.vstack(
                    rx.heading("Solicitudes de Reservas Recibidas", size="4", color="#2C3639"),
                    rx.cond(
                        State.reservas_admin_list.length() == 0,
                        rx.text("No hay solicitudes de reserva registradas actualmente.", color="#7F7F7F"),
                        rx.foreach(State.reservas_admin_list, tarjeta_reserva_admin)
                    ),
                    width="100%",
                    spacing="3"
                )
            ),
            # Pestaña Sesiones
            (
                "sesiones",
                rx.vstack(
                    rx.hstack(
                        rx.heading("Catálogo de Sesiones Grupales", size="4", color="#2C3639"),
                        rx.button(
                            "+ Crear Nueva Sesión",
                            size="2",
                            background_color="#2C3639",
                            color="#FFFFFF",
                            font_weight="bold",
                            on_click=State.abrir_modal_nueva_sesion
                        ),
                        justify="between",
                        align="center",
                        width="100%"
                    ),
                    rx.foreach(State.sesiones_tribu, tarjeta_sesion_admin),
                    modal_editor_sesion(),
                    width="100%",
                    spacing="3"
                )
            ),
            # Pestaña Productos
            (
                "productos",
                rx.vstack(
                    rx.input(
                        rx.input.slot(rx.icon(tag="search", size=16, color="#7F7F7F")),
                        placeholder="Buscar producto por nombre o categoría...",
                        value=State.busqueda_producto_admin,
                        on_change=State.set_busqueda_producto_admin,
                        width="100%",
                        size="2",
                        background_color="#FFFFFF",
                        border="1px solid #EAE5DF",
                        border_radius="8px"
                    ),
                    rx.hstack(
                        rx.heading("Inventario de Productos", size="4", color="#2C3639"),
                        rx.button(
                            "+ Crear Nuevo Producto",
                            size="2",
                            background_color="#2C3639",
                            color="#FFFFFF",
                            font_weight="bold",
                            on_click=State.abrir_modal_nuevo_producto
                        ),
                        justify="between",
                        align="center",
                        width="100%"
                    ),
                    rx.cond(
                        State.productos_admin_filtrados.length() == 0,
                        rx.text("No se encontraron productos coincidentes.", color="#7F7F7F"),
                        rx.foreach(State.productos_admin_filtrados, tarjeta_producto_admin)
                    ),
                    modal_editor_producto(),
                    width="100%",
                    spacing="3"
                )
            ),
            # Pestaña Talleres
            (
                "talleres",
                rx.vstack(
                    rx.hstack(
                        rx.heading("Agenda de Talleres y Eventos", size="4", color="#2C3639"),
                        rx.button(
                            "+ Crear Nuevo Taller",
                            size="2",
                            background_color="#2C3639",
                            color="#FFFFFF",
                            font_weight="bold",
                            on_click=State.abrir_modal_nuevo_taller
                        ),
                        justify="between",
                        align="center",
                        width="100%"
                    ),
                    rx.cond(
                        State.talleres_tribu.length() == 0,
                        rx.text("No hay talleres ni eventos registrados actualmente.", color="#7F7F7F"),
                        rx.foreach(State.talleres_tribu, tarjeta_taller_admin)
                    ),
                    modal_editor_taller(),
                    width="100%",
                    spacing="3"
                )
            ),
            # Pestaña Servicios
            (
                "servicios",
                rx.vstack(
                    rx.hstack(
                        rx.heading("Catálogo de Servicios", size="4", color="#2C3639"),
                        rx.button(
                            "+ Crear Nuevo Servicio",
                            size="2",
                            background_color="#2C3639",
                            color="#FFFFFF",
                            font_weight="bold",
                            on_click=State.abrir_modal_nuevo_servicio
                        ),
                        justify="between",
                        align="center",
                        width="100%"
                    ),
                    rx.cond(
                        State.servicios_tribu.length() == 0,
                        rx.text("No hay servicios registrados actualmente.", color="#7F7F7F"),
                        rx.foreach(State.servicios_tribu, tarjeta_servicio_admin)
                    ),
                    modal_editor_servicio(),
                    width="100%",
                    spacing="3"
                )
            ),
            # Fallback / Pestaña Cupones
            rx.vstack(
                rx.heading("Gestión de Cupones Especiales y Promociones", size="4", color="#2C3639"),
                rx.hstack(
                    rx.input(
                        placeholder="Código (Ej. PROMO15)",
                        value=State.edit_cupon_codigo,
                        on_change=State.set_edit_cupon_codigo,
                        size="2",
                        width="30%"
                    ),
                    rx.select(
                        ["PORCENTAJE", "FIJO"],
                        value=State.edit_cupon_tipo,
                        on_change=State.set_edit_cupon_tipo,
                        size="2",
                        width="20%"
                    ),
                    rx.input(
                        placeholder="Valor (% o $)",
                        type="number",
                        value=State.edit_cupon_valor.to_string(),
                        on_change=State.set_edit_cupon_valor,
                        size="2",
                        width="20%"
                    ),
                    rx.input(
                        placeholder="Usos Máx.",
                        type="number",
                        value=State.edit_cupon_usos_maximos.to_string(),
                        on_change=State.set_edit_cupon_usos_maximos,
                        size="2",
                        width="15%"
                    ),
                    rx.button(
                        "Crear Cupón",
                        on_click=State.crear_cupon_especial_admin,
                        size="2",
                        background_color="#8E6F54",
                        color="#FFFFFF",
                        font_weight="bold",
                        width="15%"
                    ),
                    width="100%",
                    spacing="2"
                ),
                rx.divider(margin_y="10px"),
                rx.text("Cupones Registrados", font_weight="bold", color="#2C3639"),
                rx.cond(
                    State.cupones_admin_list.length() == 0,
                    rx.text("No hay cupones creados aún.", color="#7F7F7F"),
                    rx.foreach(
                        State.cupones_admin_list,
                        lambda c: rx.hstack(
                            rx.hstack(
                                rx.text("🎟️ ", c["codigo"], font_weight="bold", size="2", color="#2C3639"),
                                rx.badge(c["tipo"], color_scheme="bronze", size="1"),
                                rx.badge(
                                    c["usos_actuales"].to_string() + " / " + c["usos_maximos"].to_string() + " usos",
                                    color_scheme=rx.cond(c["agotado"], "red", "green"),
                                    size="1"
                                ),
                                spacing="2",
                                align="center"
                            ),
                            rx.text("Valor: ", c["valor"].to_string(), rx.cond(c["tipo"] == "PORCENTAJE", "%", " USD"), font_weight="bold", color="#8E6F54", size="2"),
                            rx.button(
                                rx.cond(c["is_active"], "Inactivar", "Activar"),
                                size="1",
                                color_scheme=rx.cond(c["is_active"], "red", "green"),
                                variant="soft",
                                on_click=lambda: State.toggle_estado_cupon_admin(c["id"])
                            ),
                            justify="between",
                            align="center",
                            width="100%",
                            padding="10px 14px",
                            border="1px solid #EAE5DF",
                            border_radius="8px",
                            background_color="#FFFFFF"
                        )
                    )
                ),
                width="100%",
                spacing="3"
            )
        ),
        width="100%",
        max_width="850px",
        padding="20px",
        background_color="#FAF6F0",
        border_radius="12px"
    )

def admin_page() -> rx.Component:
    """Vista '/admin' accesible solo para administradores."""
    contenido = rx.center(
        rx.cond(
            State.admin_logged_in,
            panel_admin_logueado(),
            rx.vstack(
                rx.heading("Acceso Restringido", size="6", color="#2C3639", style={"font-family": "Georgia, serif"}),
                rx.text("Inicia sesión con credenciales de administrador para acceder a este panel.", color="#7F7F7F"),
                rx.button("Ir a Iniciar Sesión", size="3", background_color="#8E6F54", color="#FFFFFF", font_weight="bold", on_click=State.ir_a_login),
                spacing="3",
                align="center",
                padding="40px",
                background_color="#FFFFFF",
                border_radius="12px",
                box_shadow="0px 2px 10px rgba(0,0,0,0.05)"
            )
        ),
        width="100%",
        padding_y="40px"
    )
    return plantilla_tribu(contenido, pagina_activa="admin")
# sound_healing_platform/pages/login.py
import reflex as rx
from sound_healing_platform.state import State
from sound_healing_platform.components.layout import plantilla_tribu

def tarjeta_orden_usuario(ord_item: rx.Var) -> rx.Component:
    """Tarjeta individual de compra en el historial del cliente con desglose de ítems."""
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.vstack(
                    rx.heading("Orden # ", ord_item["referencia"], size="3", color="#2C3639", font_weight="bold"),
                    rx.text("Fecha: ", ord_item["fecha"], size="2", color="#7F7F7F"),
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

            # Desglose de Productos / Vouchers
            rx.vstack(
                rx.text("Detalle del Pedido:", size="1", font_weight="bold", color="#8E6F54"),
                rx.foreach(
                    ord_item["items"].to(list[dict]),
                    lambda item: rx.hstack(
                        rx.hstack(
                            rx.text("• ", item["cantidad"], "x ", item["nombre"], size="2", color="#2C3639", font_weight="medium"),
                            rx.cond(
                                item["variante"] != "",
                                rx.badge(item["variante"], color_scheme="bronze", size="1")
                            ),
                            spacing="2",
                            align="center"
                        ),
                        rx.text("$", item["precio"], " USD", size="2", font_weight="bold", color="#8E6F54"),
                        justify="between",
                        width="100%",
                        align="center"
                    )
                ),
                background_color="#FAF6F0",
                padding="10px 12px",
                border_radius="6px",
                width="100%",
                spacing="1"
            ),

            rx.divider(color_scheme="gray", margin_y="8px"),

            rx.hstack(
                rx.text("Método: ", ord_item["metodo_pago"], size="2", color="#2C3639"),
                rx.text("Total: $", ord_item["monto_total"], " USD", size="3", font_weight="bold", color="#2C3639"),
                justify="between",
                align="center",
                width="100%"
            ),
            width="100%",
            spacing="2"
        ),
        background_color="#FFFFFF",
        border="1px solid #EAE5DF",
        border_radius="10px",
        padding="15px",
        margin_bottom="10px",
        width="100%"
    )

def tarjeta_reserva_usuario(reserva: rx.Var) -> rx.Component:
    """Tarjeta de historial de reserva de sesión grupal."""
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.vstack(
                    rx.heading(reserva["sesion_nombre"], size="3", color="#2C3639", font_weight="bold"),
                    rx.text("📅 ", reserva["fecha_texto"], " (", reserva["hora_texto"], ")", size="1", color="#8E6F54"),
                    rx.text("📍 ", reserva["ubicacion"], size="1", color="#4B5563"),
                    align="start",
                    spacing="0"
                ),
                rx.badge(
                    reserva["estado"],
                    color_scheme=rx.match(
                        reserva["estado"],
                        ("CONFIRMADO", "green"),
                        ("RECHAZADO", "red"),
                        "amber"
                    ),
                    size="1"
                ),
                justify="between",
                align="start",
                width="100%"
            ),

            rx.divider(color_scheme="gray", margin_y="6px"),

            rx.hstack(
                rx.text("Cupos: ", reserva["cupos"].to_string(), size="1", font_weight="bold", color="#2C3639"),
                rx.text("Inversión: $", reserva["monto_total"].to_string(), " USD", size="1", font_weight="bold", color="#2C3639"),
                justify="between",
                width="100%"
            ),
            width="100%",
            spacing="1"
        ),
        background_color="#FAF6F0",
        border="1px solid #EAE5DF",
        border_radius="8px",
        padding="12px",
        margin_bottom="10px",
        width="100%"
    )

def vista_perfil_logueado() -> rx.Component:
    """Tarjeta de Perfil de Usuario con Historial Unificado Estilo Amazon/Mercado Libre."""
    return rx.box(
        rx.vstack(
            # Cabecera de Usuario
            rx.hstack(
                rx.vstack(
                    rx.heading(
                        "Hola, " + State.nombre_usuario_activo,
                        size="5",
                        color="#2C3639",
                        style={"font-family": "Georgia, serif"}
                    ),
                    rx.text(
                        rx.cond(State.admin_logged_in, "admin@tribusonora.com", State.usuario_datos["email"]),
                        size="2",
                        color="#7F7F7F"
                    ),
                    align="start",
                    spacing="0"
                ),
                rx.vstack(
                    rx.badge(
                        rx.cond(State.admin_logged_in, "ADMINISTRADOR", "CLIENTE TRIBU"),
                        color_scheme=rx.cond(State.admin_logged_in, "amber", "green"),
                        size="2"
                    ),
                    # 🎧 Botón Minimalista de Soporte Técnico (Ubicación Óvalo Naranja)
                    rx.button(
                        rx.hstack(
                            rx.icon(tag="headphone", size=13, color="#8E6F54"),
                            rx.text("Soporte Técnico", size="1", color="#8E6F54", font_weight="medium"),
                            spacing="1",
                            align="center"
                        ),
                        size="1",
                        variant="ghost",
                        cursor="pointer",
                        padding="2px 6px",
                        border_radius="4px",
                        _hover={"background_color": "#FAF6F0"},
                        on_click=State.contactar_soporte_whatsapp
                    ),
                    align="end",
                    spacing="1"
                ),
                justify="between",
                align="center",
                width="100%"
            ),
            
            rx.divider(color_scheme="gray", margin_y="10px"),

            # Conmutador de Pestañas: Mis Compras vs. Mis Reservas
            rx.hstack(
                rx.button(
                    "🛒 Mis Compras",
                    size="2",
                    variant=rx.cond(State.perfil_tab_activa == "compras", "solid", "ghost"),
                    background_color=rx.cond(State.perfil_tab_activa == "compras", "#8E6F54", "transparent"),
                    color=rx.cond(State.perfil_tab_activa == "compras", "#FFFFFF", "#2C3639"),
                    on_click=lambda: State.set_perfil_tab("compras"),
                    flex="1"
                ),
                rx.button(
                    "🧘‍♂️ Mis Reservas",
                    size="2",
                    variant=rx.cond(State.perfil_tab_activa == "reservas", "solid", "ghost"),
                    background_color=rx.cond(State.perfil_tab_activa == "reservas", "#8E6F54", "transparent"),
                    color=rx.cond(State.perfil_tab_activa == "reservas", "#FFFFFF", "#2C3639"),
                    on_click=lambda: State.set_perfil_tab("reservas"),
                    flex="1"
                ),
                width="100%",
                background_color="#FAF6F0",
                padding="4px",
                border_radius="8px"
            ),

            # Pestaña 1: Mis Compras
            rx.cond(
                State.perfil_tab_activa == "compras",
                rx.vstack(
                    rx.cond(
                        State.historial_ordenes_usuario.length() == 0,
                        rx.text("No tienes compras registradas aún.", size="2", color="#7F7F7F", padding_y="20px"),
                        rx.foreach(
                            State.historial_ordenes_usuario,
                            tarjeta_orden_usuario
                        )
                    ),
                    width="100%",
                    max_height="300px",
                    overflow_y="auto"
                ),
                # Pestaña 2: Mis Reservas
                rx.vstack(
                    rx.cond(
                        State.historial_reservas_usuario.length() == 0,
                        rx.text("No tienes reservas de sesiones registradas.", size="2", color="#7F7F7F", padding_y="20px"),
                        rx.foreach(
                            State.historial_reservas_usuario,
                            tarjeta_reserva_usuario
                        )
                    ),
                    width="100%",
                    max_height="300px",
                    overflow_y="auto"
                )
            ),

            rx.divider(color_scheme="gray", margin_y="10px"),

            # Acciones Rápidas y Cierre de Sesión
            rx.cond(
                State.admin_logged_in,
                rx.button(
                    "Ir al Panel Administrador",
                    size="3",
                    width="100%",
                    background_color="#2C3639",
                    color="#FFFFFF",
                    font_weight="bold",
                    border_radius="25px",
                    cursor="pointer",
                    _hover={"background_color": "#8E6F54"},
                    on_click=lambda: rx.redirect("/admin")
                )
            ),

            rx.button(
                "Cerrar Sesión",
                size="3",
                width="100%",
                variant="outline",
                color_scheme="red",
                font_weight="bold",
                border_radius="25px",
                cursor="pointer",
                on_click=rx.cond(State.admin_logged_in, State.logout_admin, State.logout_user)
            ),
            spacing="3",
            align="center",
            width="100%"
        ),
        background_color="#FFFFFF",
        padding=rx.breakpoints(initial="18px", sm="25px"),
        border_radius="12px",
        border="1px solid #D5D9D9",
        box_shadow="0px 4px 20px rgba(0,0,0,0.06)",
        width="100%",
        max_width="450px"
    )

def vista_formulario_login() -> rx.Component:
    """Formulario flotante de Inicio de Sesión / Registro."""
    return rx.box(
        rx.vstack(
            # Conmutador Iniciar Sesión / Registro
            rx.hstack(
                rx.button(
                    "Iniciar Sesión",
                    size="2",
                    variant=rx.cond(State.auth_modo == "login", "solid", "ghost"),
                    background_color=rx.cond(State.auth_modo == "login", "#2C3639", "transparent"),
                    color=rx.cond(State.auth_modo == "login", "#FFFFFF", "#2C3639"),
                    width="50%",
                    font_weight="bold",
                    border_radius="20px",
                    on_click=lambda: State.set_auth_modo("login")
                ),
                rx.button(
                    "Crear Cuenta",
                    size="2",
                    variant=rx.cond(State.auth_modo == "registro", "solid", "ghost"),
                    background_color=rx.cond(State.auth_modo == "registro", "#8E6F54", "transparent"),
                    color=rx.cond(State.auth_modo == "registro", "#FFFFFF", "#2C3639"),
                    width="50%",
                    font_weight="bold",
                    border_radius="20px",
                    on_click=lambda: State.set_auth_modo("registro")
                ),
                background_color="#FAF6F0",
                padding="4px",
                border_radius="25px",
                width="100%",
                margin_bottom="20px"
            ),

            # Campos Dinámicos de Nombre y Apellido (Solo en modo Registro)
            rx.cond(
                State.auth_modo == "registro",
                rx.flex(
                    rx.vstack(
                        rx.text("Nombre*", size="1", font_weight="bold", color="#2C3639"),
                        rx.input(
                            placeholder="Tu nombre",
                            value=State.auth_nombre_input,
                            on_change=State.set_auth_nombre,
                            size="3",
                            border_radius="8px",
                            border="1.5px solid #A0AEC0",
                            background_color="#FFFFFF",
                            width="100%"
                        ),
                        align="start",
                        width="100%",
                        flex="1"
                    ),
                    rx.vstack(
                        rx.text("Apellido", size="1", font_weight="bold", color="#2C3639"),
                        rx.input(
                            placeholder="Tu apellido",
                            value=State.auth_apellido_input,
                            on_change=State.set_auth_apellido,
                            size="3",
                            border_radius="8px",
                            border="1.5px solid #A0AEC0",
                            background_color="#FFFFFF",
                            width="100%"
                        ),
                        align="start",
                        width="100%",
                        flex="1"
                    ),
                    flex_direction=rx.breakpoints(initial="column", sm="row"),
                    gap="3",
                    width="100%"
                )
            ),

            # Campo Correo Electrónico
            rx.vstack(
                rx.text("Correo electrónico*", size="1", font_weight="bold", color="#2C3639"),
                rx.input(
                    placeholder="ejemplo@correo.com",
                    value=State.auth_email_input,
                    on_change=State.set_auth_email,
                    size="3",
                    border_radius="8px",
                    border="1.5px solid #A0AEC0",
                    background_color="#FFFFFF",
                    width="100%"
                ),
                align="start",
                width="100%"
            ),

            # Checkbox para Novedades y Ofertas
            rx.checkbox(
                "Envíame un correo electrónico con noticias y ofertas",
                checked=State.auth_newsletter,
                on_change=State.set_auth_newsletter,
                color_scheme="brown",
                size="2",
                style={"color": "#2C3639", "font_weight": "500"},
                margin_y="4px"
            ),

            # Campo Contraseña
            rx.vstack(
                rx.text("Contraseña*", size="1", font_weight="bold", color="#2C3639"),
                rx.input(
                    type="password",
                    placeholder="••••••••",
                    value=State.auth_pass_input,
                    on_change=State.set_auth_pass,
                    size="3",
                    border_radius="8px",
                    border="1.5px solid #A0AEC0",
                    background_color="#FFFFFF",
                    width="100%"
                ),
                align="start",
                width="100%"
            ),

            # Botón Principal de Acción
            rx.button(
                rx.cond(State.auth_modo == "login", "Entrar a mi Cuenta", "Registrarme"),
                size="3",
                width="100%",
                background_color="#2C3639",
                color="#FFFFFF",
                font_weight="bold",
                border_radius="25px",
                cursor="pointer",
                _hover={"background_color": "#8E6F54"},
                margin_top="10px",
                on_click=State.procesar_autenticacion
            ),
            spacing="3",
            width="100%"
        ),
        background_color="#FFFFFF",
        padding=rx.breakpoints(initial="20px", sm="30px"),
        border_radius="12px",
        border="1px solid #D5D9D9",
        box_shadow="0px 4px 20px rgba(0,0,0,0.06)",
        width="100%",
        max_width="430px"
    )

def login_page() -> rx.Component:
    """Vista Unificada de Autenticación / Mi Perfil."""
    contenido = rx.center(
        rx.vstack(
            rx.vstack(
                rx.heading(
                    "Mi Cuenta Tribu",
                    size="8",
                    color="#2C3639",
                    text_align="center",
                    style={"font-family": "Georgia, serif"},
                    margin_bottom="8px"
                ),
                rx.text(
                    "Gestiona tu sesión, tus reservas y tus preferencias de perfil.",
                    size="2",
                    color="#7F7F7F",
                    text_align="center",
                    max_width="400px",
                    margin_bottom="25px"
                ),
                align="center",
                width="100%"
            ),

            # Renderizado condicional: Perfil si está logueado, Formulario si no lo está
            rx.cond(
                State.user_logged_in | State.admin_logged_in,
                vista_perfil_logueado(),
                vista_formulario_login()
            ),
            align="center",
            width="100%",
            max_width="480px"
        ),
        width="100%",
        min_height="75vh",
        padding_y="50px",
        padding_x=rx.breakpoints(initial="12px", sm="20px"),
        background_color="#FAF6F0"
    )
    return plantilla_tribu(contenido, pagina_activa="login")
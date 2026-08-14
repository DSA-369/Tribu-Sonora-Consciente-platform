# sound_healing_platform/pages/checkout.py
import reflex as rx
from sound_healing_platform.state import State
from sound_healing_platform.components.layout import plantilla_tribu


def render_icono_metodo(tipo_var: rx.Var, es_seleccionado: rx.Var) -> rx.Component:
    """Renderiza el icono de Lucide correspondiente evaluando el tipo de forma reactiva."""
    color_icono = rx.cond(es_seleccionado, "#8E6F54", "#2C3639")
    return rx.match(
        tipo_var,
        ("pago_movil", rx.icon(tag="smartphone", size=18, color=color_icono)),
        ("zelle", rx.icon(tag="dollar_sign", size=18, color=color_icono)),
        ("binance", rx.icon(tag="wallet", size=18, color=color_icono)),
        ("paypal", rx.icon(tag="globe", size=18, color=color_icono)),
        ("transferencia", rx.icon(tag="building_2", size=18, color=color_icono)),
        rx.icon(tag="credit_card", size=18, color=color_icono)
    )


def datos_metodo_pago(metodo: rx.Var) -> rx.Component:
    """Componente auxiliar para renderizar cada opción de pago P2P desde el foreach de Supabase."""
    metodo_id = metodo["tipo"]
    es_seleccionado = State.metodo_pago_seleccionado == metodo_id
    
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.hstack(
                    render_icono_metodo(metodo_id, es_seleccionado),
                    rx.text(metodo["titulo"], font_weight="bold", color="#2C3639", size="2"),
                    spacing="2",
                    align="center"
                ),
                rx.box(
                    rx.box(
                        width="10px",
                        height="10px",
                        border_radius="50%",
                        background_color=rx.cond(es_seleccionado, "#8E6F54", "transparent")
                    ),
                    width="18px",
                    height="18px",
                    border_radius="50%",
                    border=rx.cond(es_seleccionado, "2px solid #8E6F54", "2px solid #A0AEC0"),
                    display="flex",
                    align_items="center",
                    justify_content="center"
                ),
                justify="between",
                align="center",
                width="100%",
                padding="14px 16px",
                cursor="pointer",
                on_click=State.seleccionar_metodo_pago(metodo_id)
            ),
            rx.cond(
                es_seleccionado,
                rx.box(
                    rx.vstack(
                        rx.text("📌 Datos para transferir:", size="1", font_weight="bold", color="#8E6F54"),
                        rx.text(
                            metodo["detalles_texto"], 
                            size="2", 
                            color="#2C3639", 
                            font_weight="medium",
                            white_space="pre-line"
                        ),
                        spacing="1",
                        align="start"
                    ),
                    padding="15px 16px",
                    background_color="#FAF6F0",
                    border_top="1px solid #EAE5DF",
                    width="100%"
                )
            ),
            spacing="0",
            width="100%"
        ),
        border=rx.cond(es_seleccionado, "1.5px solid #8E6F54", "1.5px solid #EAE5DF"),
        border_radius="8px",
        background_color="#FFFFFF",
        width="100%",
        overflow="hidden",
        transition="all 0.2s ease"
    )


def campo_formulario(label: str, placeholder: str, value: rx.Var, on_change, width_val="100%") -> rx.Component:
    """Genera un campo de formulario con etiqueta visible en negrita de alta legibilidad."""
    return rx.vstack(
        rx.text(label, size="1", font_weight="bold", color="#2C3639"),
        rx.input(
            placeholder=placeholder,
            value=value,
            on_change=on_change,
            size="3",
            border_radius="8px",
            border="1.5px solid #718096",
            background_color="#FFFFFF",
            color="#2C3639",
            font_weight="500",
            width="100%"
        ),
        spacing="1",
        align="start",
        width=width_val,
        flex="1",
        min_width="0"
    )


def formulario_izquierda() -> rx.Component:
    """Columna Izquierda: Formulario multi-pantalla con etiquetas claras y legibilidad garantizada."""
    return rx.vstack(
        # 🧪 BOTÓN DE AUTOCOMPLETADO RÁPIDO PARA PRUEBAS
        rx.button(
            rx.hstack(
                rx.icon(tag="sparkles", size=16),
                rx.text("🧪 Autocompletar Datos de Prueba", font_weight="bold"),
                spacing="2"
            ),
            on_click=State.llenar_datos_prueba_checkout,
            size="2",
            variant="soft",
            color_scheme="amber",
            cursor="pointer",
            margin_bottom="15px"
        ),

        # 1. CONTACTO INTEGLIGENTE (ADAPTABLE SEGÚN SESIÓN)
        rx.vstack(
            rx.hstack(
                rx.heading("Contacto", size="4", color="#2C3639", font_weight="bold"),
                rx.cond(
                    State.user_logged_in | State.admin_logged_in,
                    rx.hstack(
                        rx.icon(tag="user_check", size=14, color="#2E7D32"),
                        rx.text("Sesión activa (" + State.nombre_usuario_activo + ")", size="1", color="#2E7D32", font_weight="bold"),
                        rx.text("•", size="1", color="#7F7F7F"),
                        rx.text("Cerrar sesión", size="1", color="#CC0C39", font_weight="bold", cursor="pointer", text_decoration="underline", on_click=rx.cond(State.admin_logged_in, State.logout_admin, State.logout_user)),
                        spacing="1",
                        align="center"
                    ),
                    rx.hstack(
                        rx.text("¿Tienes cuenta?", size="1", color="#2C3639", font_weight="medium"),
                        rx.text("Iniciar sesión", size="1", color="#8E6F54", font_weight="bold", cursor="pointer", text_decoration="underline", on_click=State.ir_a_login),
                        spacing="1",
                        align="center"
                    )
                ),
                justify="between",
                align="center",
                width="100%"
            ),
            campo_formulario(
                "Correo electrónico / Teléfono*", 
                "ejemplo@correo.com o +58412...", 
                State.checkout_email, 
                State.set_checkout_email
            ),
            rx.checkbox(
                "Envíame un correo electrónico con noticias y ofertas",
                checked=State.checkout_newsletter,
                on_change=State.set_checkout_newsletter,
                color_scheme="brown",
                size="2",
                style={"color": "#2C3639", "font_weight": "500"}
            ),
            spacing="3",
            width="100%"
        ),

        rx.divider(color_scheme="gray", margin_y="10px"),

        # 2. ENTREGA / DATOS DEL ASISTENTE
        rx.vstack(
            rx.heading("Entrega / Datos del Asistente", size="4", color="#2C3639", font_weight="bold"),
            
            rx.vstack(
                rx.text("País / Región*", size="1", font_weight="bold", color="#2C3639"),
                rx.select(
                    ["Venezuela", "Colombia", "España", "Estados Unidos", "México", "Otro país"],
                    value=State.checkout_pais,
                    on_change=State.set_checkout_pais,
                    size="3",
                    border_radius="8px",
                    border="1.5px solid #718096",
                    background_color="#FFFFFF",
                    width="100%",
                    color="#2C3639",
                    style={"color": "#2C3639", "font_weight": "600"}
                ),
                spacing="1",
                align="start",
                width="100%"
            ),
            
            rx.flex(
                campo_formulario("Nombre*", "Tu nombre", State.checkout_nombre, State.set_checkout_nombre, "100%"),
                campo_formulario("Apellido*", "Tu apellido", State.checkout_apellido, State.set_checkout_apellido, "100%"),
                flex_direction=rx.breakpoints(initial="column", sm="row"),
                width="100%",
                gap="3"
            ),
            
            campo_formulario("Dirección*", "Lugar de encuentro / Domicilio", State.checkout_direccion, State.set_checkout_direccion),
            campo_formulario("Apartamento / Referencia", "Suite, apto, referencia (opcional)", State.checkout_apartamento, State.set_checkout_apartamento),
            
            rx.flex(
                campo_formulario("Ciudad*", "Caracas, Medellín, Madrid...", State.checkout_ciudad, State.set_checkout_ciudad, "100%"),
                campo_formulario("Código postal", "1010, 28001...", State.checkout_codigo_postal, State.set_checkout_codigo_postal, "100%"),
                flex_direction=rx.breakpoints(initial="column", sm="row"),
                width="100%",
                gap="3"
            ),
            
            campo_formulario("Teléfono WhatsApp*", "+58 412...", State.checkout_telefono, State.set_checkout_telefono),
            spacing="3",
            width="100%"
        ),

        rx.divider(color_scheme="gray", margin_y="10px"),

        # 3. MÉTODOS DE PAGO P2P DINÁMICOS
        rx.vstack(
            rx.heading("Método de Pago", size="4", color="#2C3639", font_weight="bold"),
            rx.text("Todas las transacciones son verificadas directamente por el equipo.", size="1", color="#4A5568"),
            
            rx.foreach(
                State.metodos_pago_db,
                lambda metodo: datos_metodo_pago(metodo)
            ),
            spacing="2",
            width="100%"
        ),

        rx.divider(color_scheme="gray", margin_y="10px"),

        # 4. REPORTE DE PAGO
        rx.vstack(
            rx.heading("Reporte de Pago", size="4", color="#2C3639", font_weight="bold"),
            rx.text("Ingresa la referencia y adjunta la captura del pago.", size="1", color="#4A5568"),
            
            campo_formulario("Número de referencia / confirmación*", "Ej. 894123", State.numero_referencia, State.set_numero_referencia),
            
            rx.vstack(
                rx.upload(
                    rx.vstack(
                        rx.icon(tag="cloud_upload", size=28, color="#8E6F54"),
                        rx.text("Haz clic o arrastra la captura del pago (JPG / PNG)*", size="2", color="#2C3639", font_weight="bold"),
                        rx.text("Obligatorio para la verificación de la orden", size="1", color="#4A5568"),
                        align="center",
                        spacing="1"
                    ),
                    id="upload_comprobante",
                    border="2px dashed #A0AEC0",
                    border_radius="8px",
                    padding="20px",
                    background_color="#FAF6F0",
                    cursor="pointer",
                    width="100%",
                    on_drop=State.handle_upload(rx.upload_files(upload_id="upload_comprobante"))
                ),
                rx.cond(
                    State.comprobante_cargado,
                    rx.hstack(
                        rx.image(
                            src=rx.get_upload_url(State.comprobante_filename),
                            width="68px",
                            height="68px",
                            object_fit="cover",
                            border_radius="8px",
                            border="1px solid #EAE5DF"
                        ),
                        rx.vstack(
                            rx.hstack(
                                rx.icon(tag="circle_check", size=16, color="#2E7D32"),
                                rx.text("Comprobante adjuntado con éxito", size="2", font_weight="bold", color="#2C3639"),
                                spacing="1",
                                align="center"
                            ),
                            rx.text(
                                State.comprobante_filename, 
                                size="1", 
                                color="#4A5568",
                                word_break="break-all"
                            ),
                            rx.button(
                                "Cambiar imagen",
                                on_click=State.limpiar_comprobante,
                                size="1",
                                background_color="#EAE5DF",
                                color="#2C3639",
                                font_weight="bold",
                                border_radius="6px",
                                _hover={"background_color": "#D5CEC5"},
                                cursor="pointer"
                            ),
                            align="start",
                            spacing="1",
                            flex="1",
                            min_width="0"
                        ),
                        padding="12px",
                        border_radius="8px",
                        background_color="#FAF6F0",
                        border="1px solid #EAE5DF",
                        align="center",
                        spacing="3",
                        width="100%"
                    )
                ),
                width="100%",
                spacing="2"
            ),
            spacing="3",
            width="100%"
        ),

        # 5. BOTÓN PÍLDORA FINAL
        rx.button(
            rx.hstack(
                rx.text("Confirmar y Finalizar Pedido", size="3", font_weight="bold"),
                rx.icon(tag="arrow_right", size=18),
                spacing="2",
                align="center"
            ),
            on_click=State.procesar_orden(rx.upload_files(upload_id="upload_comprobante")),
            width="100%",
            height="52px",
            background_color="#2C3639",
            color="#FFFFFF",
            border_radius="30px",
            cursor="pointer",
            _hover={
                "background_color": "#8E6F54",
                "transform": "translateY(-2px)",
                "box_shadow": "0px 4px 12px rgba(0,0,0,0.15)"
            },
            transition="all 0.2s ease",
            margin_top="20px"
        ),
        spacing="4",
        width="100%",
        align="start"
    )


def resumen_orden_derecha() -> rx.Component:
    """Columna Derecha: Resumen dinámico con BADGE CENTRADO PERFECTO."""
    return rx.vstack(
        rx.vstack(
            rx.foreach(
                State.carrito,
                lambda item: rx.hstack(
                    rx.box(
                        rx.image(
                            src=item["foto"],
                            width="68px",
                            height="68px",
                            object_fit="cover",
                            border_radius="10px",
                            border="1px solid #EAE5DF"
                        ),
                        # Badge con Centrado Absoluto de Flexbox
                        rx.box(
                            rx.text(
                                item["cantidad"],
                                color="#FFFFFF",
                                size="1",
                                font_weight="bold",
                                line_height="1"
                            ),
                            position="absolute",
                            top="-8px",
                            right="-8px",
                            background_color="#2C3639",
                            border_radius="50%",
                            width="22px",
                            height="22px",
                            display="flex",
                            align_items="center",
                            justify_content="center",
                            box_shadow="0px 2px 5px rgba(0,0,0,0.2)"
                        ),
                        position="relative"
                    ),
                    rx.vstack(
                        rx.text(
                            item["nombre"],
                            size="2",
                            font_weight="bold",
                            color="#2C3639",
                            line_height="1.2",
                            word_break="break-word"
                        ),
                        align="start",
                        spacing="1",
                        flex="1",
                        min_width="0",
                        padding_left="10px"
                    ),

                    rx.hstack(
                        rx.text("$", size="2", font_weight="bold", color="#2C3639"),
                        rx.text(item["precio"], size="2", font_weight="bold", color="#2C3639"),
                        rx.text("USD", size="1", color="#4A5568"),
                        spacing="1",
                        align="center"
                    ),
                    justify="between",
                    align="center",
                    width="100%",
                    padding_y="10px"
                )
            ),
            width="100%",
            max_height="320px",
            overflow_y="auto",
            spacing="2"
        ),

        rx.divider(color_scheme="gray", margin_y="15px"),

        # CÓDIGO DE DESCUENTO
        rx.hstack(
            rx.input(
                placeholder="Código de descuento",
                value=State.checkout_cupon,
                on_change=State.set_checkout_cupon,
                variant="surface",
                size="3",
                border_radius="8px",
                border="1.5px solid #A0AEC0",
                background_color="#FFFFFF",
                width="100%",
                color="#2C3639",
                font_weight="600"
            ),
            rx.button(
                "Aplicar",
                on_click=State.aplicar_cupon,
                size="3",
                background_color="#EAE5DF",
                color="#2C3639",
                font_weight="bold",
                border_radius="8px",
                _hover={"background_color": "#8E6F54", "color": "#FFFFFF"},
                cursor="pointer"
            ),
            width="100%",
            spacing="3"
        ),

        rx.divider(color_scheme="gray", margin_y="15px"),

        # DESGLOSE DE PRECIOS Y TOTAL
        rx.vstack(
            rx.hstack(
                rx.text("Subtotal", size="2", color="#4A5568"),
                rx.hstack(
                    rx.text("$", size="2", font_weight="bold", color="#2C3639"),
                    rx.text(State.subtotal_carrito, size="2", font_weight="bold", color="#2C3639"),
                    rx.text("USD", size="1", color="#4A5568"),
                    spacing="1"
                ),
                justify="between",
                width="100%"
            ),
            
            rx.cond(
                State.descuento_cupon_monto > 0,
                rx.hstack(
                    rx.text("Descuento aplicado", size="2", color="#8E6F54", font_weight="bold"),
                    rx.hstack(
                        rx.text("-$", size="2", font_weight="bold", color="#8E6F54"),
                        rx.text(State.descuento_cupon_monto, size="2", font_weight="bold", color="#8E6F54"),
                        rx.text("USD", size="1", color="#8E6F54"),
                        spacing="1"
                    ),
                    justify="between",
                    width="100%"
                )
            ),

            rx.hstack(
                rx.text("Envío / Gestión", size="2", color="#4A5568"),
                rx.text("Gratis", size="2", color="#4A5568", italic=True),
                justify="between",
                width="100%"
            ),

            rx.divider(color_scheme="gray", margin_y="10px"),

            # TOTAL FINAL
            rx.hstack(
                rx.text("Total", size="4", font_weight="bold", color="#2C3639"),
                rx.hstack(
                    rx.text("USD", size="2", color="#4A5568", font_weight="medium"),
                    rx.text("$", size="5", font_weight="bold", color="#2C3639"),
                    rx.text(State.total_checkout, size="5", font_weight="bold", color="#2C3639"),
                    spacing="1",
                    align="baseline"
                ),
                justify="between",
                align="center",
                width="100%"
            ),
            width="100%",
            spacing="2"
        ),
        
        width="100%",
        padding=rx.breakpoints(initial="20px", md="30px"),
        background_color="#FAF6F0",
        border_radius="12px",
        border="1px solid #EAE5DF"
    )


def vista_checkout() -> rx.Component:
    """Vista Principal Responsiva dividida en 2 Columnas con Sticky Activo."""
    contenido = rx.center(
        rx.vstack(
            rx.flex(
                # 👈 COLUMNA IZQUIERDA (Se desliza normalmente al hacer scroll)
                rx.box(
                    formulario_izquierda(),
                    width=rx.breakpoints(initial="100%", md="55%"),
                    padding_right=rx.breakpoints(initial="0px", md="30px")
                ),

                # 👉 COLUMNA DERECHA (Flotante y fija a la vista en pantallas de escritorio)
                rx.box(
                    resumen_orden_derecha(),
                    width=rx.breakpoints(initial="100%", md="45%"),
                    position=rx.breakpoints(initial="static", md="sticky"),
                    top=rx.breakpoints(initial="auto", md="100px"),
                    align_self="start"
                ),
                
                flex_direction=rx.breakpoints(initial="column-reverse", md="row"),
                gap=rx.breakpoints(initial="30px", md="20px"),
                width="100%",
                align_items="start"
            ),
            width="100%",
            max_width="1150px",
            padding_x=rx.breakpoints(initial="10px", sm="20px"),
            padding_y="40px"
        ),
        width="100%",
        background_color="#FFFFFF"
    )
    return plantilla_tribu(contenido, pagina_activa="checkout")
# sound_healing_platform/components/layout.py
import reflex as rx

from sound_healing_platform.state import State


def plantilla_tribu(contenido_central: rx.Component, pagina_activa: str) -> rx.Component:
    """
    Molde maestro que envuelve a todas las páginas de la plataforma.
    Corregido con contenedores puente transparentes y breakpoints para perfecta visualización móvil.
    """
    return rx.box(
        rx.html("<style>.reflex-badge, a[href*='reflex.dev'] { display: none !important; visibility: hidden !important; opacity: 0 !important; pointer-events: none !important; }</style>"),
        rx.el.style("""
            @keyframes infinito {
                0% { transform: translateX(0); }
                100% { transform: translateX(-50%); }
            }
            @keyframes glowing-pulse {
                0% {
                    transform: scale(1);
                    box-shadow: 0 0 0 0 rgba(234, 179, 8, 0.7);
                }
                50% {
                    transform: scale(1.05);
                    box-shadow: 0 0 16px 6px rgba(234, 179, 8, 0.45);
                }
                100% {
                    transform: scale(1);
                    box-shadow: 0 0 0 0 rgba(234, 179, 8, 0);
                }
            }
            .btn-glowing-pulse {
                animation: glowing-pulse 2.2s infinite ease-in-out;
            }
            .btn-glowing-pulse:hover {
                animation-play-state: paused;
            }
        """),

        # 1. BARRA DE ANUNCIO SUPERIOR (ESTILO PÍLDORA + COPYWRITING RESPONSIVO)
        rx.center(
            rx.hstack(
                rx.text(
                    "¡Bienvenidos a Tribu Sonora Consciente! Regálate un espacio de conexión y sanación acústica",
                    color="#FFFFFF",
                    size=rx.breakpoints(initial="1", md="2"),
                    font_weight="medium",
                    text_align="center"
                ),
                # 💊 PÍLDORA DE ACCIÓN DESTACADA Y ADAPTABLE A MÓVILES
                rx.box(
                    rx.hstack(
                        rx.text(
                            "Agendar Sesión", 
                            size=rx.breakpoints(initial="1", md="2"), 
                            font_weight="bold", 
                            color="#FFFFFF",
                            white_space="nowrap"
                        ),
                        rx.icon(tag="arrow-right", size=14, color="#FFFFFF"),
                        spacing="2",
                        align="center"
                    ),
                    class_name="btn-glowing-pulse",
                    background_color="#2C3639",
                    padding=rx.breakpoints(initial="3px 10px", md="4px 14px"),
                    border_radius="20px",
                    cursor="pointer",
                    _hover={
                        "background_color": "#8E6F54",
                        "transform": "translateY(-1px)",
                        "box_shadow": "0px 4px 10px rgba(0,0,0,0.2)"
                    },
                    transition="all 0.2s ease",
                    on_click=State.ir_a_horario_sesiones
                ),
                spacing=rx.breakpoints(initial="2", md="3"),
                align="center",
                justify="center",
                flex_wrap="wrap",
                padding_y=rx.breakpoints(initial="6px", md="8px")
            ),
            background_color="#A27B5C",
            width="100%",
            padding_x="15px"
        ),

        # 2. CABECERA PRINCIPAL (NAVBAR OPTIMIZADO CON PUENTES DE HOVER)
        rx.vstack(
            rx.flex(
                # Lado Izquierdo: Lupa + Campana de Notificaciones unificada
                rx.hstack(
                    rx.icon(tag="search", size=20, color="#2C3639", cursor="pointer", on_click=State.abrir_modal_busqueda_global),
                    rx.box(
                        rx.hstack(
                            rx.icon(tag="bell", size=20, color="#2C3639", cursor="pointer", on_click=State.toggle_menu_notificaciones),
                            rx.cond(
                                State.total_notificaciones_no_leidas > 0,
                                rx.box(
                                    rx.text(
                                        State.total_notificaciones_no_leidas,
                                        color="#FFFFFF",
                                        size="1",
                                        font_weight="bold",
                                        line_height="1",
                                        margin="0",
                                        padding="0",
                                        text_align="center"
                                    ),
                                    position="absolute",
                                    top="-5px",
                                    right="-7px",
                                    background_color="#CC0C39",
                                    border_radius="50%",
                                    width="16px",
                                    height="16px",
                                    display="flex",
                                    align_items="center",
                                    justify_content="center",
                                    pointer_events="none"
                                )
                            ),
                            spacing="0",
                            align="center"
                        ),
                        # Popover de Notificaciones
                        rx.cond(
                            State.show_popover_notificaciones,
                            rx.box(
                                rx.vstack(
                                    rx.hstack(
                                        rx.heading("Notificaciones", size="3", color="#2C3639"),
                                        rx.icon(tag="x", size=16, color="#7F7F7F", cursor="pointer", on_click=State.cerrar_menu_notificaciones),
                                        justify="between",
                                        align="center",
                                        width="100%"
                                    ),
                                    rx.divider(color_scheme="gray"),
                                    rx.cond(
                                        State.notificaciones_lista.length() == 0,
                                        rx.text("No tienes notificaciones por el momento.", size="2", color="#7F7F7F", padding="10px 0"),
                                        rx.vstack(
                                            rx.foreach(
                                                State.notificaciones_lista,
                                                lambda n: rx.box(
                                                    rx.vstack(
                                                        rx.hstack(
                                                            rx.text(n["titulo"], font_weight="bold", size="2", color="#2C3639"),
                                                            rx.cond(
                                                                ~n["leido"],
                                                                rx.badge("NUEVA", color_scheme="red", size="1")
                                                            ),
                                                            justify="between",
                                                            width="100%"
                                                        ),
                                                        rx.text(n["mensaje"], size="1", color="#7F7F7F"),
                                                        spacing="1",
                                                        align="start"
                                                    ),
                                                    padding="8px 10px",
                                                    border_radius="6px",
                                                    background_color=rx.cond(n["leido"], "#FAF6F0", "#FFF8E7"),
                                                    border="1px solid #EAE5DF",
                                                    cursor="pointer",
                                                    _hover={"background_color": "#F4EBE1"},
                                                    on_click=lambda: State.clic_notificacion_redireccionar(n["id"], n["target_url"]),
                                                    width="100%"
                                                )
                                            ),
                                            spacing="2",
                                            max_height="300px",
                                            overflow_y="auto",
                                            width="100%"
                                        )
                                    ),
                                    width="100%",
                                    padding="15px"
                                ),
                                position="absolute",
                                top="100%",
                                left="0",
                                background_color="#FFFFFF",
                                border="1px solid #2C3639",
                                border_radius="8px",
                                width="310px",
                                box_shadow="0px 8px 24px rgba(0,0,0,0.15)",
                                z_index="1100"
                            )
                        ),
                        position="relative",
                        on_mouse_leave=State.cerrar_menu_notificaciones
                    ),
                    spacing="4",
                    align="center",
                    width="20%"
                ),
                rx.vstack(
                    rx.image(src="/logo_tribu.png", width="162px", height="auto"), 
                    rx.heading("TRIBU SONORA CONSCIENTE", size="6", letter_spacing="0.18em", color="#2C3639", font_weight="light", margin_top="4px", text_align="center"), 
                    align="center", spacing="1", width="60%",
                ),
                rx.hstack(
                    rx.hstack(
                        rx.icon(
                            tag="user", 
                            size=20, 
                            color="#2C3639", 
                            cursor="pointer",
                            on_click=State.ir_a_login
                        ),
                        rx.cond(
                            State.nombre_usuario_activo != "",
                            rx.vstack(
                                rx.text("Hola,", size="1", color="#7F7F7F", line_height="1"),
                                rx.text(
                                    State.nombre_usuario_activo, 
                                    size="2", 
                                    font_weight="bold", 
                                    color="#2C3639", 
                                    line_height="1",
                                    max_width="100px",
                                    overflow="hidden",
                                    text_overflow="ellipsis",
                                    white_space="nowrap"
                                ),
                                spacing="0",
                                align="start",
                                cursor="pointer",
                                on_click=State.ir_a_login
                            )
                        ),
                        spacing="2",
                        align="center"
                    ),
                    rx.box(
                        rx.icon(tag="shopping-cart", size=20, color="#2C3639"),
                        rx.cond(
                            State.total_items_carrito > 0,
                            rx.box(
                                rx.text(
                                    State.total_items_carrito,
                                    color="#FFFFFF",
                                    size="1",
                                    font_weight="bold",
                                    line_height="1"
                                ),
                                position="absolute",
                                top="-6px",
                                right="-8px",
                                background_color="#8E6F54",
                                border_radius="50%",
                                width="18px",
                                height="18px",
                                display="flex",
                                align_items="center",
                                justify_content="center",
                                padding="2px"
                            )
                        ),
                        position="relative",
                        cursor="pointer",
                        on_click=State.toggle_carrito
                    ),
                    spacing="4", 
                    justify="end", 
                    width="20%"
                ),                width="100%", align="center", justify="between", padding_x="40px", padding_top="25px",
            ),
            # Bloque de navegación inteligente continuo
            rx.flex(
                # Enlace HOME
                rx.link(
                    rx.text(
                        "HOME", 
                        color="#2C3639", 
                        size="3", 
                        cursor="pointer",
                        font_weight="bold" if pagina_activa == "home" else "normal",
                        text_decoration="underline" if pagina_activa == "home" else "none"
                    ), 
                    href="/", 
                    text_decoration="none"
                ),
                
                # DROPDOWN 1: SESIONES (Alineación adaptable para evitar desbordamiento en móviles)
                rx.box(
                    rx.hstack(
                        rx.text("Sesiones", color="#2C3639", size="3"), 
                        rx.icon(tag=rx.cond(State.show_menu_sesiones, "chevron-up", "chevron-down"), size=12, color="#2C3639"),
                        spacing="1", 
                        cursor="pointer",
                        on_click=State.toggle_menu_sesiones,
                    ),
                    rx.cond(
                        State.show_menu_sesiones,
                        rx.box( 
                            rx.vstack(
                                # Enlaces conectados a las páginas de Paquetes y Horarios
                                rx.link(
                                    rx.text("Precios - Paquetes de sesiones - Membresías", color="#2C3639", size="3", cursor="pointer", _hover={"color": "#A27B5C"}, white_space=rx.breakpoints(initial="normal", md="nowrap"), on_click=State.cerrar_menu_sesiones),
                                    href="/sesiones/paquetes",
                                    text_decoration="none"
                                ),
                                rx.link(
                                    rx.text("Horario de sesiones", color="#2C3639", size="3", cursor="pointer", _hover={"color": "#A27B5C"}, white_space=rx.breakpoints(initial="normal", md="nowrap"), on_click=State.cerrar_menu_sesiones),
                                    href="/sesiones/horario",
                                    text_decoration="none"
                                ),
                                background_color="#FAF6F0",
                                border="1px solid #2C3639",
                                padding="16px 24px",
                                spacing="3",
                                align="start",
                                min_width=rx.breakpoints(initial="250px", md="340px"), # Ancho adaptable inteligente
                                box_shadow="0px 6px 16px rgba(0,0,0,0.06)",
                            ),
                            position="absolute",
                            top="100%", 
                            left=rx.breakpoints(initial="0", md="50%"), # Al ras en móvil, centrado en PC
                            transform=rx.breakpoints(initial="none", md="translateX(-50%)"), # Sin desplazamiento en móvil
                            padding_top="12px", 
                            z_index="1000",
                        )
                    ),
                    position="relative",
                    on_mouse_leave=State.cerrar_menu_sesiones,
                ),
                
                # LINKS ESTÁTICOS
                rx.link(
    rx.text(
        "Tipo de servicios", 
        color="#2C3639", 
        size="3", 
        cursor="pointer",
        font_weight="bold" if pagina_activa == "servicios" else "normal",
        text_decoration="underline" if pagina_activa == "servicios" else "none"
    ), 
    href="/servicios", 
    text_decoration="none"
), 
                rx.link(
    rx.text(
        "Talleres", 
        color="#2C3639", 
        size="3", 
        cursor="pointer",
        font_weight="bold" if pagina_activa == "talleres" else "normal",
        text_decoration="underline" if pagina_activa == "talleres" else "none"
    ), 
    href="/talleres", 
    text_decoration="none"
),
                
                # DROPDOWN 2: SHOP (Con puente invisible e Instrumentos asimilado)
                rx.box(
                    rx.hstack(
                        rx.text("Shop", color="#2C3639", size="3", on_click=State.navegar_revista_principal), 
                        rx.icon(tag=rx.cond(State.show_menu_shop, "chevron-up", "chevron-down"), size=12, color="#2C3639", on_click=State.toggle_menu_shop),
                        spacing="1", 
                        cursor="pointer",
                     ),
                    rx.cond(
                        State.show_menu_shop,
                        rx.box( 
                            rx.vstack(
                                rx.text("Los más vendidos", color="#2C3639", size="3", cursor="pointer", _hover={"color": "#A27B5C"}, white_space="nowrap", on_click=State.navegar_vista_mas_vendidos),
                                rx.text("Favoritos seleccionados", color="#2C3639", size="3", cursor="pointer", _hover={"color": "#A27B5C"}, white_space="nowrap", on_click=State.navegar_vista_favoritos),
                            
                                # SUB-MENÚ INTERNO 1: Comprar según la intención
                                rx.vstack(
                                    rx.hstack(
                                        rx.text("Comprar según la intención", color="#2C3639", size="3", cursor="pointer", _hover={"color": "#A27B5C"}, white_space="nowrap"),
                                        rx.icon(tag=rx.cond(State.show_sub_intencion, "chevron-up", "chevron-down"), size=12, color="#2C3639"),
                                        justify="between", align="center", width="100%", spacing="2", cursor="pointer", on_click=State.toggle_sub_intencion
                                    ),
                                    rx.cond(
                                        State.show_sub_intencion,
                                        rx.vstack(
                                            rx.text("Plantar y restaurar", color="#7F7F7F", size="2", cursor="pointer", _hover={"color": "#A27B5C"}, on_click=State.navegar_vista_intencion("Plantar y restaurar")),
                                            rx.text("Claridad y enfoque", color="#7F7F7F", size="2", cursor="pointer", _hover={"color": "#A27B5C"}, on_click=State.navegar_vista_intencion("Claridad y enfoque")),
                                            rx.text("Corazón y conexión", color="#7F7F7F", size="2", cursor="pointer", _hover={"color": "#A27B5C"}, on_click=State.navegar_vista_intencion("Corazón y conexión")),
                                            rx.text("Descanso y sueño", color="#7F7F7F", size="2", cursor="pointer", _hover={"color": "#A27B5C"}, on_click=State.navegar_vista_intencion("Descanso y sueño")),
                                            align="start", spacing="2", padding_left="14px", width="100%"
                                        )
                                    ),
                                    width="100%", align="start", spacing="1"
                                ),
# SUB-MENÚ INTERNO 2: Comprar por categoría
                                rx.vstack(
                                    rx.hstack(
                                        rx.text("Comprar por categoría", color="#2C3639", size="3", cursor="pointer", _hover={"color": "#A27B5C"}, white_space="nowrap"),
                                        rx.icon(tag=rx.cond(State.show_sub_categoria, "chevron-up", "chevron-down"), size=12, color="#2C3639"),
                                        justify="between", align="center", width="100%", spacing="2", cursor="pointer", on_click=State.toggle_sub_categoria
                                    ),
                                    rx.cond(
                                        State.show_sub_categoria,
                                        rx.vstack(
                                            rx.foreach(
                                                State.lista_categorias_unicas,
                                                lambda cat_nombre: rx.text(
                                                    cat_nombre,
                                                    color="#7F7F7F",
                                                    size="2",
                                                    cursor="pointer",
                                                    _hover={"color": "#A27B5C"},
                                                    on_click=State.navegar_vista_categoria(cat_nombre)
                                                )
                                            ),
                                            align="start", spacing="2", padding_left="14px", width="100%"
                                        )
                                    ),
                                    width="100%", align="start", spacing="1"
                                ),

                                rx.text("Colección Soulmat", color="#2C3639", size="3", cursor="pointer", _hover={"color": "#A27B5C"}, white_space="nowrap"),
                                rx.link(
                                    rx.text("Tarjetas de regalo", color="#2C3639", size="3", cursor="pointer", _hover={"color": "#A27B5C"}, white_space="nowrap", on_click=State.cerrar_menu_shop),
                                    href="/tarjetas-de-regalo",
                                    text_decoration="none"
                                ),
                                rx.text("Ver todo", color="#2C3639", size="3", cursor="pointer", _hover={"color": "#A27B5C"}, white_space="nowrap", on_click=State.navegar_vista_ver_todo),
                                background_color="#FAF6F0",
                                border="1px solid #2C3639",
                                padding="16px 24px",
                                spacing="3",
                                align="start",
                                min_width="260px",
                                box_shadow="0px 6px 16px rgba(0,0,0,0.06)",
                            ),
                            position="absolute",
                            top="100%",
                            left=rx.breakpoints(initial="0px", md="50%"),
                            transform=rx.breakpoints(initial="none", md="translateX(-50%)"),
                            max_width="calc(100vw - 30px)",
                            padding_top="12px",
                            z_index="1000",
                        )
                    ),
                    position="relative",
                    on_mouse_leave=State.cerrar_menu_shop,
                ),
                
                # DROPDOWN 3: ACERCA DE (Estructura colapsable con subrayado activo restaurado)
                rx.box(
                    rx.hstack(
                        rx.text(
                            "Acerca de", 
                            color="#2C3639", 
                            size="3",
                            font_weight="bold" if pagina_activa == "acerca_de" else "normal",
                            text_decoration="underline" if pagina_activa == "acerca_de" else "none"
                        ), 
                        rx.icon(tag=rx.cond(State.show_menu_acerca_de, "chevron-up", "chevron-down"), size=12, color="#2C3639"),
                        spacing="1", 
                        cursor="pointer",
                        on_click=State.toggle_menu_acerca_de,
                    ),
                    rx.cond(
                        State.show_menu_acerca_de,
                        rx.box( 
                            rx.vstack(
                                rx.link(
                                    rx.text("Nuestra filosofía", color="#2C3639", size="3", cursor="pointer", _hover={"color": "#A27B5C"}, white_space="nowrap", on_click=State.cerrar_menu_acerca_de),
                                    href="/acerca-de#filosofia",
                                    text_decoration="none"
                                ),
                                rx.link(
                                    rx.text("Historia", color="#2C3639", size="3", cursor="pointer", _hover={"color": "#A27B5C"}, white_space="nowrap", on_click=State.cerrar_menu_acerca_de),
                                    href="/acerca-de#historia",
                                    text_decoration="none"
                                ),
                                rx.link(
                                    rx.text("Conozca a los guías", color="#2C3639", size="3", cursor="pointer", _hover={"color": "#A27B5C"}, white_space="nowrap", on_click=State.cerrar_menu_acerca_de),
                                    href="/acerca-de#guias",
                                    text_decoration="none"
                                ),
                                rx.link(
                                    rx.text("Conozca nuestros aliados", color="#2C3639", size="3", cursor="pointer", _hover={"color": "#A27B5C"}, white_space="nowrap", on_click=State.cerrar_menu_acerca_de),
                                    href="/acerca-de#aliados",
                                    text_decoration="none"
                                ),
                                rx.link(
                                    rx.text("Diario", color="#2C3639", size="3", cursor="pointer", _hover={"color": "#A27B5C"}, white_space="nowrap", on_click=State.cerrar_menu_acerca_de),
                                    href="/acerca-de#diario",
                                    text_decoration="none"
                                ),
                                background_color="#FAF6F0",
                                border="1px solid #2C3639", 
                                padding="16px 24px",
                                spacing="3",
                                align="start",
                                min_width="250px", 
                                box_shadow="0px 6px 16px rgba(0,0,0,0.06)",
                            ),
                            position="absolute",
                            top="100%",       
                            left="50%",       
                            transform="translateX(-50%)",
                            padding_top="12px", 
                            z_index="1000",   
                        )
                    ),
                    position="relative",
                    on_mouse_leave=State.cerrar_menu_acerca_de,
                ),
                
                # Enlace Contacto
                rx.link(
                    rx.text(
                        "Contacto", 
                        color="#2C3639", 
                        size="3", 
                        cursor="pointer",
                        font_weight="bold" if pagina_activa == "contacto" else "normal",
                        text_decoration="underline" if pagina_activa == "contacto" else "none"
                    ), 
                    href="/contacto", 
                    text_decoration="none"
                ),
                style={
                    "display": "flex",
                    "flex-wrap": "wrap",
                    "justify-content": "center",
                    "gap": "28px"
                },
                width="100%", padding_y="20px", border_bottom="1px solid #EAE5DF",
            ),
            width="100%", background_color="#FAF6F0",
        ),

        # 3. CONTENIDO CENTRAL DINÁMICO
        rx.box(
            contenido_central,
            width="100%",
        ),

        # 4. PIE DE PÁGINA EDITORIAL COMPARTIDO (CONEXIONES ACTIVAS CON PRECISIÓN QUIRÚRGICA)
        rx.vstack(
            rx.vstack(
                rx.heading("Mantente conectado", size="6", color="#2C3639", font_weight="normal", style={"font-family": "Georgia, serif"}),
                rx.text("Actualizaciones sobre temas y tips relacionados con el sonido, rituales de limpieza y noticias sobre eventos.", size="2", color="#7F7F7F", text_align="center", max_width="600px"),
                rx.hstack(
                    rx.input(placeholder="Correo electrónico", value=State.email_newsletter, on_change=State.asignar_email, variant="surface", size="2", color="#2C3639", width="260px"),
                    rx.icon(tag="arrow-right", size=16, color="#7F7F7F", cursor="pointer", on_click=State.registrar_suscripcion),
                    border="1px solid #7F7F7F", padding_x="14px", padding_y="8px", margin_top="15px", background_color="transparent",
                ),
                align="center", spacing="2", padding_y="40px",
            ),
            # Bloque de enlaces del footer interactivos y horizontales
            rx.hstack(
                rx.link(rx.text("HOME", color="#2C3639", size="2", cursor="pointer"), href="/", text_decoration="none"), 
                rx.link(rx.text("Sesiones", color="#2C3639", size="2", cursor="pointer"), href="/sesiones/horario", text_decoration="none"),
                rx.link(rx.text("Tipo de servicios", color="#2C3639", size="2", cursor="pointer"), href="/servicios", text_decoration="none"),
                rx.link(rx.text("Talleres", color="#2C3639", size="2", cursor="pointer"), href="/talleres", text_decoration="none"),
                rx.link(rx.text("Shop", color="#2C3639", size="2", cursor="pointer"), href="/shop", text_decoration="none"), 
                rx.link(rx.text("Acerca de", color="#2C3639", size="2", cursor="pointer"), href="/acerca-de", text_decoration="none"),
                rx.link(rx.text("Contacto", color="#2C3639", size="2", cursor="pointer"), href="/contacto", text_decoration="none"),
                rx.link(rx.text("Política de privacidad", color="#2C3639", size="2", cursor="pointer"), href="/politica-de-privacidad", text_decoration="none"),
                rx.link(rx.text("Términos y condiciones", color="#2C3639", size="2", cursor="pointer"), href="/terminos-y-condiciones", text_decoration="none"),
                spacing="5", justify="center", flex_wrap="wrap", width="100%", padding_bottom="30px",
            ),
            rx.hstack(
                rx.link(rx.html('<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#2C3639" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>'), href="https://www.facebook.com/tribusonoraconsciente369", is_external=True),
                rx.link(rx.html('<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#2C3639" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="20" x="2" y="2" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" x2="17.51" y1="6.5" y2="6.5"/></svg>'), href="https://www.instagram.com/tribusonoraconsciente/", is_external=True),
                spacing="5", justify="center", padding_bottom="40px",
            ),
            rx.vstack(
                rx.text("OPCIONES DE RESERVA Y PAGO", size="1", letter_spacing="0.15em", color="#A6A19A", font_weight="medium", margin_bottom="12px"),
                rx.text("ZELLE   •   BINANCE   •   PAYPAL   •   PAGO MÓVIL   •   TRANSFERENCIA BANCARIA", size="1", letter_spacing="0.12em", color="#2C3639", font_weight="medium", style={"font-family": "Times New Roman, serif"}),
                padding_top="25px", border_top="1px solid #EAE5DF", width="85%", max_width="700px", align="center",
            ),
            rx.flex(
                rx.text("© 2026, Tribu Sonora Consciente. Sitio de propiedad independiente desarrollado bajo arquitectura Full-Stack contacto jesus.buraglia@gmail.com. · ", size="1", color="#7F7F7F", text_align="center"),
                rx.text("Preferencias de cookies", size="1", color="#2C3639", font_weight="medium", text_decoration="underline", cursor="pointer", on_click=State.abrir_cookies, text_align="center"),
                flex_direction=rx.breakpoints(initial="column", sm="row"), justify_content="center", align_items="center", margin_top="20px", padding_bottom="35px", gap="1", padding_x="15px", width="100%",
            ),
            width="100%", background_color="#FAF6F0", align="center", spacing="1", padding_top="20px",
        ),

        # 5. MODAL DE COOKIES COMPARTIDO
        rx.dialog.root(
            rx.dialog.content(
                rx.flex(
                    rx.vstack(rx.heading("Preferencias de cookies y privacidad", size="5", color="#2C3639", style={"font-family": "Georgia, serif"}), margin_bottom="10px"),
                    rx.hstack(
                        rx.button("Aceptar todo", size="2", background_color="#8E6F54", color="#FFFFFF", font_weight="medium", cursor="pointer", on_click=State.aceptar_todo_cookies),
                        rx.button("Rechazar todo", size="2", variant="outline", color="#8E6F54", border_color="#8E6F54", font_weight="medium", cursor="pointer", on_click=State.rechazar_todo_cookies),
                        rx.button("Guardar mis opciones", size="2", background_color="#8E6F54", color="#FFFFFF", font_weight="medium", cursor="pointer", on_click=State.guardar_seleccion_cookies),
                        rx.box(rx.icon(tag="x", size=18, color="#2C3639", cursor="pointer", on_click=State.cerrar_cookies), padding="4px"),
                        spacing="3", align="center",
                    ),
                    width="100%", align_items="center", justify_content="between", border_bottom="1px solid #EAE5DF", padding_bottom="20px", flex_direction=rx.breakpoints(initial="column", md="row"), gap="4",
                ),
                rx.vstack(
                    rx.text("Tú controlas tus datos", size="3", font_weight="bold", color="#2C3639", margin_top="20px"),
                    rx.text("Obtén más información sobre las cookies que utilizamos y elige cuáles deseas permitir.", size="2", color="#7F7F7F", margin_bottom="15px"),
                    width="100%", align="start", spacing="1",
                ),
                rx.vstack(
                    rx.flex(rx.checkbox(checked=True, disabled=True, color_scheme="gray"), rx.vstack(rx.text("Requerido", size="2", font_weight="bold", color="#2C3639"), rx.text("Estas cookies son necesarias para que el sitio funcione correctamente.", size="2", color="#7F7F7F"), align="start", spacing="0"), gap="3", align="start", width="100%", padding_y="10px"),
                    rx.flex(rx.checkbox(checked=State.cookies_personalizacion, on_change=State.asignar_personalizacion, color_scheme="brown"), rx.vstack(rx.text("Personalización", size="2", font_weight="bold", color="#2C3639"), rx.text("Estas cookies almacenan información sobre tus acciones para personalizar tu próxima visita.", size="2", color="#7F7F7F"), align="start", spacing="0"), gap="3", align="start", width="100%", padding_y="10px"),
                    rx.flex(rx.checkbox(checked=State.cookies_marketing, on_change=State.asignar_marketing, color_scheme="brown"), rx.vstack(rx.text("Marketing", size="2", font_weight="bold", color="#2C3639"), rx.text("Nosotros y nuestros socios utilizamos estas cookies para optimizar las comunicaciones de marketing.", size="2", color="#7F7F7F"), align="start", spacing="0"), gap="3", align="start", width="100%", padding_y="10px"),
                    rx.flex(rx.checkbox(checked=State.cookies_analitica, on_change=State.asignar_analitica, color_scheme="brown"), rx.vstack(rx.text("Analítica", size="2", font_weight="bold", color="#2C3639"), rx.text("Estas cookies nos ayudan a comprender cómo interactúa usted con el sitio.", size="2", color="#7F7F7F"), align="start", spacing="0"), gap="3", align="start", width="100%", padding_y="10px"),
                    width="100%", spacing="2",
                ),
                background_color="#FAF6F0", max_width="850px", border_radius="6px", padding="30px", border="1px solid #EAE5DF",
            ),
            open=State.show_cookie_modal, 
        ),

        # 6. PANEL LATERAL DESLIZANTE DEL CARRITO (CART DRAWER - ESTILO MERCADO LIBRE / AMAZON)
        rx.cond(
            State.mostrar_carrito,
            rx.box(
                # Sombra / Overlay oscuro de fondo
                rx.box(
                    position="fixed",
                    top="0",
                    left="0",
                    width="100vw",
                    height="100vh",
                    background_color="rgba(0, 0, 0, 0.4)",
                    z_index="9998",
                    on_click=State.cerrar_carrito
                ),
                # Panel lateral que se desliza desde la derecha
                rx.box(
                    rx.vstack(
                        # Cabecera del Carrito con Campana de Notificaciones (Historial)
                        rx.vstack(
                            rx.hstack(
                                rx.heading("Tu Carrito", size="5", color="#2C3639", style={"font-family": "Georgia, serif"}),
                                rx.icon(tag="x", size=20, color="#2C3639", cursor="pointer", on_click=State.cerrar_carrito),
                                justify="between",
                                align="center",
                                width="100%"
                            ),
                            width="100%",
                            padding_bottom="15px",
                            border_bottom="1px solid #EAE5DF"
                        ),

                        # Cuerpo: Si el carrito está vacío vs. Si tiene productos
                        rx.cond(
                            State.carrito.length() == 0,
                            rx.vstack(
                                rx.icon(tag="shopping-cart", size=48, color="#C8C2BC"),
                                rx.text("Tu carrito está vacío", size="3", color="#7F7F7F"),
                                rx.button(
                                    "Explorar la tienda",
                                    size="2",
                                    background_color="#8E6F54",
                                    color="#FFFFFF",
                                    border_radius="0px",
                                    cursor="pointer",
                                    on_click=State.navegar_revista_principal
                                ),
                                spacing="3",
                                align="center",
                                padding_y="60px",
                                width="100%"
                            ),
                            rx.vstack(
                                rx.foreach(
                                    State.carrito,
                                    lambda item: rx.hstack(
                                        # 📸 FOTO DEL PRODUCTO (CLICABLE CON REDIRECCIÓN)
                                        rx.image(
                                            src=item["foto"], 
                                            width="65px", 
                                            height="65px", 
                                            object_fit="cover",
                                            cursor="pointer",
                                            _hover={"opacity": "0.85"},
                                            on_click=State.ir_a_producto_desde_carrito(item["id"])
                                        ),
                                        rx.vstack(
                                            # 🏷️ NOMBRE DEL PRODUCTO (CLICABLE CON REDIRECCIÓN)
                                            rx.text(
                                                item["nombre"], 
                                                size="2", 
                                                font_weight="bold", 
                                                color="#2C3639",
                                                cursor="pointer",
                                                _hover={"color": "#8E6F54"},
                                                on_click=State.ir_a_producto_desde_carrito(item["id"])
                                            ),

                                            rx.hstack(
                                                rx.text("$", size="2", color="#8E6F54", font_weight="medium"),
                                                rx.text(item["precio"], size="2", color="#8E6F54", font_weight="medium"),
                                                rx.text("USD", size="1", color="#8E6F54"),
                                                spacing="1"
                                            ),
                                            # Control de cantidad individual
                                            rx.hstack(
                                                rx.button("-", size="1", variant="ghost", color="#2C3639", on_click=lambda: State.decrementar_item_carrito(item["key"])),
                                                rx.text(item["cantidad"], size="2", color="#2C3639", padding_x="6px"),
                                                rx.button("+", size="1", variant="ghost", color="#2C3639", on_click=lambda: State.incrementar_item_carrito(item["key"])),
                                                align="center",
                                                border="1px solid #EAE5DF"
                                            ),
                                            align="start",
                                            spacing="1",
                                            width="100%"
                                        ),
                                        # Botón eliminar
                                        rx.icon(
                                            tag="trash-2", 
                                            size=16, 
                                            color="#A27B5C", 
                                            cursor="pointer", 
                                            _hover={"color": "#FF0000"},
                                            on_click=lambda: State.eliminar_del_carrito(item["key"])
                                        ),
                                        justify="between",
                                        align="center",
                                        width="100%",
                                        padding_y="12px",
                                        border_bottom="1px solid #EAE5DF"
                                    )
                                ),
                                width="100%",
                                max_height="55vh",
                                overflow_y="auto"
                            )
                        ),

                        # Pie del Carrito: Subtotal y Botón Checkout
                        rx.cond(
                            State.carrito.length() > 0,
                            rx.vstack(
                                rx.hstack(
                                    rx.text("Subtotal:", size="3", font_weight="bold", color="#2C3639"),
                                    rx.hstack(
                                        rx.text("$", size="4", font_weight="bold", color="#8E6F54"),
                                        rx.text(State.subtotal_carrito, size="4", font_weight="bold", color="#8E6F54"),
                                        rx.text("USD", size="2", color="#8E6F54"),
                                        spacing="1"
                                    ),
                                    justify="between",
                                    width="100%",
                                    padding_y="10px"
                                ),
                                rx.button(
                                    "Finalizar Compra",
                                    width="100%",
                                    height="48px",
                                    background_color="#8E6F54",
                                    color="#FFFFFF",
                                    border_radius="0px",
                                    font_weight="bold",
                                    cursor="pointer",
                                    _hover={"opacity": "0.9"},
                                    on_click=State.ir_a_checkout
                                ),
                                width="100%",
                                padding_top="15px",
                                border_top="1px solid #EAE5DF"
                            )
                        ),
                        width="100%",
                        height="100%",
                        justify="between"
                    ),
                    position="fixed",
                    top="0",
                    right="0",
                    width=rx.breakpoints(initial="85%", sm="380px"),
                    height="100vh",
                    background_color="#FAF6F0",
                    z_index="9999",
                    padding=rx.breakpoints(initial="15px", sm="25px"),
                    box_shadow="-6px 0px 20px rgba(0,0,0,0.2)",
                    overflow_y="auto"
                )
            )
        ),

        # 7. MODAL FLOTANTE DE BÚSQUEDA GLOBAL OMNICANAL
        modal_busqueda_global()
    )
def modal_busqueda_global() -> rx.Component:
    """Modal de Búsqueda Global Omnicanal en tiempo real."""
    return rx.dialog.root(
        rx.dialog.content(
            rx.vstack(
                # Campo de Entrada con Autoenfoque
                rx.hstack(
                    rx.icon(tag="search", size=22, color="#8E6F54"),
                    rx.input(
                        placeholder="Buscar cuencos, sesiones, talleres, servicios...",
                        value=State.busqueda_global_query,
                        on_change=State.set_busqueda_global_query,
                        width="100%",
                        size="3",
                        variant="soft",
                        color="#2C3639",
                        style={"font-size": "16px", "outline": "none"}
                    ),
                    rx.icon(
                        tag="x",
                        size=20,
                        color="#7F7F7F",
                        cursor="pointer",
                        on_click=State.cerrar_modal_busqueda_global
                    ),
                    width="100%",
                    align="center",
                    spacing="3"
                ),
                rx.divider(color_scheme="gray", margin_y="10px"),

                # Estado 1: Query vacía -> Sugerencias rápidas de Búsqueda
                rx.cond(
                    State.busqueda_global_query.strip() == "",
                    rx.vstack(
                        rx.text("Sugerencias de búsqueda rápida:", size="2", font_weight="bold", color="#7F7F7F"),
                        rx.hstack(
                            rx.badge("Cuencos", color_scheme="bronze", cursor="pointer", on_click=lambda: State.set_busqueda_global_query("Cuencos")),
                            rx.badge("Santiamen", color_scheme="bronze", cursor="pointer", on_click=lambda: State.set_busqueda_global_query("Santiamen")),
                            rx.badge("Terapia", color_scheme="bronze", cursor="pointer", on_click=lambda: State.set_busqueda_global_query("Terapia")),
                            rx.badge("Talleres", color_scheme="bronze", cursor="pointer", on_click=lambda: State.set_busqueda_global_query("Talleres")),
                            rx.badge("Didgeridoo", color_scheme="bronze", cursor="pointer", on_click=lambda: State.set_busqueda_global_query("Didgeridoo")),
                            flex_wrap="wrap",
                            spacing="2"
                        ),
                        padding_y="15px",
                        align="start",
                        width="100%"
                    ),
                    # Estado 2: Query con búsqueda activada
                    rx.cond(
                        State.total_resultados_busqueda_global == 0,
                        rx.vstack(
                            rx.icon(tag="search-x", size=40, color="#C8C2BC"),
                            rx.text(f"No encontramos resultados para '{State.busqueda_global_query}'", size="2", color="#7F7F7F"),
                            align="center",
                            padding_y="30px",
                            width="100%"
                        ),
                        rx.vstack(
                            # 🛒 PRODUCTOS DE LA TIENDA
                            rx.cond(
                                State.busqueda_resultados_productos.length() > 0,
                                rx.vstack(
                                    rx.hstack(
                                        rx.text("🛒 PRODUCTOS DE LA TIENDA", size="1", font_weight="bold", color="#8E6F54", letter_spacing="0.1em"),
                                        rx.badge(State.busqueda_resultados_productos.length(), color_scheme="brown", size="1"),
                                        spacing="2", align="center"
                                    ),
                                    rx.foreach(
                                        State.busqueda_resultados_productos,
                                        lambda p: rx.hstack(
                                            rx.image(src=p["foto_principal"], width="45px", height="45px", object_fit="cover", border_radius="6px"),
                                            rx.vstack(
                                                rx.text(p["nombre"], font_weight="bold", size="2", color="#2C3639"),
                                                rx.hstack(
                                                    rx.badge(p["categoria"], color_scheme="gray", size="1"),
                                                    rx.text(f"${p['precio']} USD", size="1", font_weight="bold", color="#8E6F54"),
                                                    spacing="2"
                                                ),
                                                align="start", spacing="0"
                                            ),
                                            justify="between", align="center", width="100%", padding="8px",
                                            border_radius="6px", cursor="pointer", _hover={"background_color": "#FAF6F0"},
                                            on_click=lambda: State.seleccionar_resultado_busqueda(f"/product/{p['id']}")
                                        )
                                    ),
                                    width="100%", align="start", spacing="2"
                                )
                            ),

                            # 🛖 TALLERES Y EVENTOS
                            rx.cond(
                                State.busqueda_resultados_talleres.length() > 0,
                                rx.vstack(
                                    rx.hstack(
                                        rx.text("🛖 TALLERES Y EVENTOS", size="1", font_weight="bold", color="#8E6F54", letter_spacing="0.1em"),
                                        rx.badge(State.busqueda_resultados_talleres.length(), color_scheme="brown", size="1"),
                                        spacing="2", align="center"
                                    ),
                                    rx.foreach(
                                        State.busqueda_resultados_talleres,
                                        lambda w: rx.hstack(
                                            rx.image(src=w["foto"], width="45px", height="45px", object_fit="cover", border_radius="6px"),
                                            rx.vstack(
                                                rx.text(w["titulo"], font_weight="bold", size="2", color="#2C3639"),
                                                rx.text(f"📍 {w['ubicacion']} • 📅 {w['fecha_texto']}", size="1", color="#7F7F7F"),
                                                align="start", spacing="0"
                                            ),
                                            justify="between", align="center", width="100%", padding="8px",
                                            border_radius="6px", cursor="pointer", _hover={"background_color": "#FAF6F0"},
                                            on_click=lambda: State.seleccionar_resultado_busqueda("/talleres")
                                        )
                                    ),
                                    width="100%", align="start", spacing="2"
                                )
                            ),

                            # 🧘‍♂️ SESIONES GRUPALES
                            rx.cond(
                                State.busqueda_resultados_sesiones.length() > 0,
                                rx.vstack(
                                    rx.hstack(
                                        rx.text("🧘‍♂️ SESIONES GRUPALES", size="1", font_weight="bold", color="#8E6F54", letter_spacing="0.1em"),
                                        rx.badge(State.busqueda_resultados_sesiones.length(), color_scheme="brown", size="1"),
                                        spacing="2", align="center"
                                    ),
                                    rx.foreach(
                                        State.busqueda_resultados_sesiones,
                                        lambda s: rx.hstack(
                                            rx.image(src=s["foto"], width="45px", height="45px", object_fit="cover", border_radius="6px"),
                                            rx.vstack(
                                                rx.text(s["nombre"], font_weight="bold", size="2", color="#2C3639"),
                                                rx.text(f"📍 {s['ubicacion']} • 📅 {s['fecha_texto']}", size="1", color="#7F7F7F"),
                                                align="start", spacing="0"
                                            ),
                                            justify="between", align="center", width="100%", padding="8px",
                                            border_radius="6px", cursor="pointer", _hover={"background_color": "#FAF6F0"},
                                            on_click=lambda: State.seleccionar_resultado_busqueda("/sesiones/horario")
                                        )
                                    ),
                                    width="100%", align="start", spacing="2"
                                )
                            ),

                            # ✨ SERVICIOS HOLÍSTICOS
                            rx.cond(
                                State.busqueda_resultados_servicios.length() > 0,
                                rx.vstack(
                                    rx.hstack(
                                        rx.text("✨ SERVICIOS HOLÍSTICOS", size="1", font_weight="bold", color="#8E6F54", letter_spacing="0.1em"),
                                        rx.badge(State.busqueda_resultados_servicios.length(), color_scheme="brown", size="1"),
                                        spacing="2", align="center"
                                    ),
                                    rx.foreach(
                                        State.busqueda_resultados_servicios,
                                        lambda serv: rx.hstack(
                                            rx.image(src=serv["foto"], width="45px", height="45px", object_fit="cover", border_radius="6px"),
                                            rx.vstack(
                                                rx.text(serv["nombre"], font_weight="bold", size="2", color="#2C3639"),
                                                rx.text(serv["descripcion"], size="1", color="#7F7F7F", max_width="350px", overflow="hidden", text_overflow="ellipsis", white_space="nowrap"),
                                                align="start", spacing="0"
                                            ),
                                            justify="between", align="center", width="100%", padding="8px",
                                            border_radius="6px", cursor="pointer", _hover={"background_color": "#FAF6F0"},
                                            on_click=lambda: State.seleccionar_resultado_busqueda("/servicios")
                                        )
                                    ),
                                    width="100%", align="start", spacing="2"
                                )
                            ),
                            width="100%",
                            spacing="4",
                            max_height="60vh",
                            overflow_y="auto"
                        )
                    )
                ),
                width="100%",
                spacing="3"
            ),
            background_color="#FFFFFF",
            padding="25px",
            border_radius="12px",
            max_width="550px"
        ),
        open=State.modal_busqueda_global_abierto,
        on_open_change=State.set_modal_busqueda_global_abierto
    )
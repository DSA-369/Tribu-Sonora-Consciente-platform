# sound_healing_platform/pages/shop.py
import reflex as rx

from sound_healing_platform.components.layout import plantilla_tribu
from sound_healing_platform.state import State


def tarjeta_producto_revista(producto: rx.Var) -> rx.Component:
    """Maqueta una tarjeta de producto con proporciones tipo revista en 4 columnas fluidas."""
    return rx.vstack(
        rx.box(
            rx.image(
                src=producto["foto_principal"],
                width="100%",
                height="340px",
                object_fit="cover",
                border_radius="0px",
                transition="transform 0.3s ease-in-out",
                _hover={"transform": "scale(1.02)"},
                cursor="pointer"
            ),
            rx.cond(
                producto["stock"] == 0,
                rx.box(
                    rx.text("Agotado", color="#FFFFFF", size="1", font_weight="bold", letter_spacing="0.05em"),
                    background_color="#8E6F54",
                    position="absolute", top="12px", left="12px", padding="4px 10px", z_index="10"
                )
            ),
            position="relative", overflow="hidden", width="100%"
        ),
        rx.heading(
            producto["nombre"], 
            size="3", 
            color="#2C3639", 
            font_weight="normal",
            style={"font-family": "Georgia, serif"}, margin_top="12px"
        ),
        rx.hstack(
            rx.text("$", color="#2C3639", size="2", font_weight="medium"),
            rx.text(producto["precio"], color="#2C3639", size="2", font_weight="medium"),
            rx.text("USD", color="#2C3639", size="2", font_weight="medium"),
            spacing="1", margin_top="2px"
        ),
        align="start",
        width=rx.breakpoints(initial="100%", sm="45%", md="23%"),
        padding_x="10px",
        margin_bottom="25px",
        cursor="pointer",
        on_click=rx.redirect(f"/product/{producto['id']}")
    )

def tarjeta_producto_ver_todo(producto: rx.Var) -> rx.Component:
    """Tarjeta adaptada a 3 columnas para el catálogo principal con filtros."""
    return rx.vstack(
        rx.box(
            rx.image(
                src=producto["foto_principal"],
                width="100%",
                height="290px",
                object_fit="cover",
                border_radius="0px",
                transition="transform 0.3s ease-in-out",
                _hover={"transform": "scale(1.02)"},
                cursor="pointer"
            ),
            rx.cond(
                producto["stock"] == 0,
                rx.box(
                    rx.text("Agotado", color="#FFFFFF", size="1", font_weight="bold", letter_spacing="0.05em"),
                    background_color="#8E6F54",
                    position="absolute", top="12px", left="12px", padding="4px 10px", z_index="10"
                )
            ),
            position="relative", overflow="hidden", width="100%"
        ),
        rx.cond(
            producto["proveedor"] != "",
            rx.text(
                producto["proveedor"],
                size="1",
                color="#7F7F7F",
                letter_spacing="0.1em",
                text_transform="uppercase",
                margin_top="10px"
            )
        ),
        rx.heading(
            producto["nombre"], 
            size="3", 
            color="#2C3639", 
            font_weight="normal",
            style={"font-family": "Georgia, serif"}, 
            margin_top="4px"
        ),
        rx.hstack(
            rx.text("$", color="#2C3639", size="2", font_weight="medium"),
            rx.text(producto["precio"], color="#2C3639", size="2", font_weight="medium"),
            rx.text("USD", color="#2C3639", size="2", font_weight="medium"),
            spacing="1", margin_top="2px"
        ),
        align="start",
        width=rx.breakpoints(initial="100%", sm="48%", md="31%"),
        padding_x="8px",
        margin_bottom="30px",
        cursor="pointer",
        on_click=rx.redirect(f"/product/{producto['id']}")
    )

def tarjeta_categoria_dinamica(cat: rx.Var) -> rx.Component:
    """Maqueta una tarjeta de categoría para el carrusel dinámico infinito."""
    return rx.vstack(
        rx.box(rx.image(src=cat["img"], width="240px", height="240px", object_fit="cover"), width="240px", overflow="hidden"),
        rx.hstack(
            rx.text(cat["name"], size="3", color="#2C3639", font_weight="normal", style={"font-family": "Georgia, serif"}), 
            rx.icon(tag="arrow-right", size=13, color="#2C3639"), 
            spacing="1", align="center", margin_top="14px"
        ),
        align="start", 
        width="240px", 
        padding_x="10px", 
        cursor="pointer", 
        _hover={"opacity": "0.80"},
        on_click=State.navegar_vista_categoria(cat["name"])
    )

def seccion_explorar_todos_los_productos() -> rx.Component:
    """Sección completa responsiva: Filtros fijos en PC y colapsables en Móvil."""
    intenciones_disponibles = [
        "Claridad y enfoque",
        "Terreno y restauración",
        "Corazón y conexión",
        "Descanso y sueño"
    ]

    return rx.vstack(
        rx.heading(
            "Explorar todos los productos", 
            size=rx.breakpoints(initial="5", md="7"), 
            color="#2C3639", 
            font_weight="normal", 
            style={"font-family": "Georgia, serif"},
            text_align="center",
            margin_bottom="25px"
        ),

        # BARRA CABECERA RESPONSIVA (CONTADOR, BOTÓN MÓVIL Y ORDENAMIENTO)
        rx.flex(
            rx.hstack(
                rx.text(
                    f"{State.total_productos_ver_todo_count} productos", 
                    size="2", 
                    color="#7F7F7F"
                ),
                # 📱 BOTÓN DE FILTROS SOLO VISIBLE EN MÓVILES
                rx.box(
                    rx.button(
                        rx.hstack(
                            rx.icon(tag="sliders-horizontal", size=14),
                            rx.text("Filtros", size="2"),
                            spacing="1",
                            align="center"
                        ),
                        variant="outline",
                        border_color="#2C3639",
                        color="#2C3639",
                        size="1",
                        border_radius="0px",
                        cursor="pointer",
                        on_click=State.toggle_filtros_mobile
                    ),
                    display=rx.breakpoints(initial="block", md="none")
                ),
                spacing="3",
                align="center",
                justify="between",
                width=rx.breakpoints(initial="100%", sm="auto")
            ),

            rx.hstack(
                rx.text("Ordenar por:", size="2", color="#7F7F7F"),
                rx.select(
                    ["Nombre: AZ", "Nombre: ZA", "Precio: Menor a Mayor", "Precio: Mayor a Menor"],
                    value=State.filtro_ordenamiento,
                    on_change=State.set_filtro_ordenamiento,
                    size="2",
                    variant="surface",
                    color="#2C3639"
                ),
                spacing="2",
                align="center",
                width=rx.breakpoints(initial="100%", sm="auto"),
                justify="between"
            ),

            flex_direction=rx.breakpoints(initial="column", sm="row"),
            justify="between",
            align="center",
            width="100%",
            margin_bottom="20px",
            padding_bottom="15px",
            border_bottom="1px solid #EAE5DF",
            gap="3"
        ),

        # CONTENEDOR PRINCIPAL
        rx.flex(
            # COLUMNA IZQUIERDA: BLOQUE DE FILTROS (STICKY EN PC, DESPLEGABLE EN MÓVIL)
            rx.cond(
                # En escritorio siempre se muestra (md="block"); en móvil depende de State.show_filtros_mobile
                State.show_filtros_mobile | rx.breakpoints(initial=False, md=True),
                rx.vstack(
                    # 1. RANGO DE PRECIOS
                    rx.vstack(
                        rx.text("Rango de precios", font_weight="bold", size="3", color="#2C3639", style={"font-family": "Georgia, serif"}),
                        rx.hstack(
                            rx.input(
                                placeholder="Mín",
                                value=State.filtro_precio_min,
                                on_change=State.set_filtro_precio_min,
                                width="85px",
                                size="1",
                                variant="surface"
                            ),
                            rx.text("-", color="#7F7F7F"),
                            rx.input(
                                placeholder="Máximo",
                                value=State.filtro_precio_max,
                                on_change=State.set_filtro_precio_max,
                                width="85px",
                                size="1",
                                variant="surface"
                            ),
                            spacing="2",
                            align="center"
                        ),
                        align="start",
                        spacing="2",
                        width="100%",
                        margin_bottom="20px"
                    ),

                    # 2. TIPO DE PRODUCTO (CATEGORÍAS)
                    rx.vstack(
                        rx.text("Tipo de producto", font_weight="bold", size="3", color="#2C3639", style={"font-family": "Georgia, serif"}),
                        rx.vstack(
                            rx.foreach(
                                State.lista_categorias_unicas,
                                lambda cat_nombre: rx.hstack(
                                    rx.checkbox(
                                        checked=State.filtro_categorias_ver_todo.contains(cat_nombre),
                                        on_change=lambda _: State.toggle_filtro_categoria_ver_todo(cat_nombre),
                                        color_scheme="brown",
                                        size="1"
                                    ),
                                    rx.text(
                                        cat_nombre, 
                                        size="2", 
                                        color="#2C3639", 
                                        cursor="pointer",
                                        on_click=lambda: State.toggle_filtro_categoria_ver_todo(cat_nombre)
                                    ),
                                    spacing="2",
                                    align="center"
                                )
                            ),
                            align="start",
                            spacing="2",
                            width="100%"
                        ),
                        align="start",
                        spacing="2",
                        width="100%",
                        margin_bottom="20px"
                    ),

                    # 3. INTENCIÓN
                    rx.vstack(
                        rx.text("Intención", font_weight="bold", size="3", color="#2C3639", style={"font-family": "Georgia, serif"}),
                        rx.vstack(
                            *[
                                rx.hstack(
                                    rx.checkbox(
                                        checked=State.filtro_intenciones_ver_todo.contains(intenc),
                                        on_change=lambda _, i=intenc: State.toggle_filtro_intencion_ver_todo(i),
                                        color_scheme="brown",
                                        size="1"
                                    ),
                                    rx.text(
                                        intenc, 
                                        size="2", 
                                        color="#2C3639", 
                                        cursor="pointer",
                                        on_click=lambda _, i=intenc: State.toggle_filtro_intencion_ver_todo(i)
                                    ),
                                    spacing="2",
                                    align="center"
                                )
                                for intenc in intenciones_disponibles
                            ],
                            align="start",
                            spacing="2",
                            width="100%"
                        ),
                        align="start",
                        spacing="2",
                        width="100%",
                        margin_bottom="25px"
                    ),

                    # 4. BOTÓN BORRAR TODOS LOS FILTROS
                    rx.button(
                        "Borrar todos los filtros",
                        variant="outline",
                        border_color="#7F7F7F",
                        color="#2C3639",
                        size="2",
                        border_radius="0px",
                        width="100%",
                        cursor="pointer",
                        on_click=State.limpiar_filtros_ver_todo
                    ),
                    align="start",
                    width=rx.breakpoints(initial="100%", md="240px"),
                    min_width="220px",
                    style={"position": rx.breakpoints(initial="static", md="sticky"), "top": "120px"},
                    padding_right=rx.breakpoints(initial="0px", md="20px"),
                    margin_bottom=rx.breakpoints(initial="25px", md="0px"),
                    background_color=rx.breakpoints(initial="#FAF6F0", md="transparent"),
                    padding=rx.breakpoints(initial="15px", md="0px"),
                    border=rx.breakpoints(initial="1px solid #EAE5DF", md="none")
                )
            ),

            # COLUMNA DERECHA: GRILLA DE PRODUCTOS
            rx.box(
                rx.cond(
                    State.productos_ver_todo_filtrados.length() == 0,
                    rx.vstack(
                        rx.icon(tag="package-open", size=48, color="#C8C2BC"),
                        rx.text("No hay productos que coincidan con los filtros seleccionados.", size="2", color="#7F7F7F", text_align="center"),
                        rx.button(
                            "Limpiar Filtros",
                            size="2",
                            background_color="#8E6F54",
                            color="#FFFFFF",
                            border_radius="0px",
                            cursor="pointer",
                            on_click=State.limpiar_filtros_ver_todo
                        ),
                        align="center",
                        spacing="3",
                        padding_y="60px",
                        width="100%"
                    ),
                    rx.flex(
                        rx.foreach(State.productos_ver_todo_filtrados, tarjeta_producto_ver_todo),
                        width="100%",
                        flex_direction=rx.breakpoints(initial="column", sm="row"),
                        flex_wrap="wrap",
                        justify="start",
                        gap="0"
                    )
                ),
                flex="1",
                width="100%"
            ),
            flex_direction=rx.breakpoints(initial="column", md="row"),
            width="100%",
            align_items="flex-start"
        ),
        width="100%",
        padding_y="20px"
    )

def seccion_revista_principal() -> rx.Component:
    """Dibuja el bloque editorial de la tienda con los 3 bloques y la sección de catálogo al final."""
    return rx.vstack(
        # 1. FILA: LOS MÁS VENDIDOS
        rx.vstack(
            rx.heading("LOS MÁS VENDIDOS", size="5", color="#2C3639", font_weight="normal", letter_spacing="0.12em", style={"font-family": "Georgia, serif"}, margin_bottom="35px"),
            rx.flex(
                rx.foreach(State.shop_mas_vendidos_revista, tarjeta_producto_revista),
                width="100%", flex_direction=rx.breakpoints(initial="column", sm="row"), flex_wrap="wrap", justify="center", gap="4"
            ),
            rx.button(
                "Ver todo", size="2", background_color="#8E6F54", color="#FFFFFF", font_weight="normal", border_radius="0px", padding_x="28px", cursor="pointer", margin_top="20px",
                on_click=State.navegar_vista_mas_vendidos
            ),
            width="100%", padding_y="30px", align="center"
        ),

        rx.center(rx.box(width="100%", height="1px", background_color="#EAE5DF"), width="100%", padding_y="25px"),

        # 2. FILA: FAVORITOS SELECCIONADOS
        rx.vstack(
            rx.heading("FAVORITOS SELECCIONADOS", size="5", color="#2C3639", font_weight="normal", letter_spacing="0.12em", style={"font-family": "Georgia, serif"}, margin_bottom="35px"),
            rx.flex(
                rx.foreach(State.shop_favoritos_revista, tarjeta_producto_revista),
                width="100%", flex_direction=rx.breakpoints(initial="column", sm="row"), flex_wrap="wrap", justify="center", gap="4"
            ),
            rx.button(
                "Ver todo", size="2", background_color="#8E6F54", color="#FFFFFF", font_weight="normal", border_radius="0px", padding_x="28px", cursor="pointer", margin_top="20px",
                on_click=State.navegar_vista_favoritos
            ),
            width="100%", padding_y="30px", align="center"
        ),

        rx.center(rx.box(width="100%", height="1px", background_color="#EAE5DF"), width="100%", padding_y="25px"),

        # 3. FILA: COMPRAR POR CATEGORÍA (Carrusel Infinito Dinámico)
        rx.vstack(
            rx.heading("COMPRAR POR CATEGORÍA", size="5", color="#2C3639", font_weight="normal", letter_spacing="0.12em", style={"font-family": "Georgia, serif"}, margin_bottom="45px"),
            rx.box(
                rx.hstack(
                    rx.foreach(State.categorias_unicas_carrusel, tarjeta_categoria_dinamica),
                    rx.foreach(State.categorias_unicas_carrusel, tarjeta_categoria_dinamica),
                    spacing="5",
                    style={
                        "animation": "infinito 25s linear infinite",
                        "width": "max-content",
                        "_hover": {"animation_play_state": "paused"}
                    }
                ),
                width="100%", 
                overflow="hidden", 
                padding_y="15px"
            ),
            width="100%", 
            padding_y="30px", 
            align="center"
        ),

        rx.center(rx.box(width="100%", height="1px", background_color="#EAE5DF"), width="100%", padding_y="25px"),

        # 4. FILA: EXPLORAR TODOS LOS PRODUCTOS (VISTA COMPLETA CON FILTROS LATERALES)
        seccion_explorar_todos_los_productos(),

        width="100%"
    )

def pantalla_galeria_limpia(titulo_seccion: str, origen_datos: rx.Var) -> rx.Component:
    """Estructura una visualización limpia a 4 columnas fluidas libre de barras laterales."""
    return rx.vstack(
        rx.button(
            rx.hstack(rx.icon(tag="arrow-left", size=14), rx.text("Volver a la Tienda Principal", size="2")),
            variant="ghost", color="#7F7F7F", cursor="pointer", margin_bottom="35px", align_self="start",
            on_click=State.navegar_revista_principal
        ),
        rx.heading(titulo_seccion, size="7", color="#2C3639", font_weight="light", letter_spacing="0.05em", style={"font-family": "Georgia, serif"}, margin_bottom="45px"),
        rx.flex(
            rx.foreach(origen_datos, tarjeta_producto_revista),
            width="100%", flex_direction=rx.breakpoints(initial="column", sm="row"), flex_wrap="wrap", justify="start", gap="0"
        ),
        width="100%"
    )

def shop_page() -> rx.Component:
    """Enrutador interno reactivo para alternar las vistas de la tienda."""
    return plantilla_tribu(
        rx.center(
            rx.vstack(
                rx.cond(
                    State.vista_shop == "revista",
                    seccion_revista_principal(),
                    rx.cond(
                        State.vista_shop == "ver_todo",
                        seccion_explorar_todos_los_productos(),
                        rx.cond(
                            State.vista_shop == "ver_mas_vendidos",
                            pantalla_galeria_limpia("TODOS LOS MÁS VENDIDOS", State.todos_los_mas_vendidos),
                            rx.cond(
                                State.vista_shop == "ver_favoritos",
                                pantalla_galeria_limpia("FAVORITOS SELECCIONADOS", State.todos_los_favoritos),
                                rx.cond(
                                    State.vista_shop == "ver_intencion",
                                    pantalla_galeria_limpia(State.intencion_seleccionada.upper(), State.productos_por_intencion_limpia),
                                    pantalla_galeria_limpia(State.categoria_seleccionada, State.productos_por_categoria_limpia)
                                )
                            )
                        )
                    )
                ),
                width="100%", max_width="1100px", align="center", padding_x="10px"
            ),
            width="100%", background_color="#FAF6F0", padding_y="50px"
        ),
        pagina_activa="shop"
    )
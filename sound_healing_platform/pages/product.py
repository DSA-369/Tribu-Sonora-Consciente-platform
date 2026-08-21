import reflex as rx

from sound_healing_platform.components.layout import plantilla_tribu
from sound_healing_platform.pages.shop import tarjeta_producto_revista
from sound_healing_platform.state import State


def galeria_imagenes() -> rx.Component:
    """Columna izquierda: Foto principal fiel al encuadre original + miniaturas cuadradas inferiores."""
    return rx.vstack(
        # Contenedor marco neutro para exhibir la foto completa sin recortes
        rx.center(
            rx.image(
                src=State.foto_principal,
                width="100%",
                height="480px",
                object_fit="contain",  # 👈 Mantiene la imagen 100% entera sin recortar bordes
                border_radius="0px"
            ),
            width="100%",
            height="480px",
            background_color="#F7F4F0", # Fondo suave que enmarca cualquier tipo de producto
            overflow="hidden",
            padding="15px"
        ),
        # Fila de miniaturas inferiores (si hay más de 1 foto)
        rx.cond(
            State.fotos_producto.length() > 1,
            rx.hstack(
                rx.foreach(
                    State.fotos_producto,
                    lambda img_url: rx.box(
                        rx.image(
                            src=img_url,
                            width="75px",
                            height="75px",
                            object_fit="cover",
                            cursor="pointer",
                            opacity=rx.cond(State.foto_principal == img_url, "1.0", "0.5"),
                            _hover={"opacity": "1.0"},
                            on_click=lambda: State.seleccionar_foto_principal(img_url)
                        ),
                        border=rx.cond(State.foto_principal == img_url, "1px solid #8E6F54", "1px solid transparent"),
                        padding="2px"
                    )
                ),
                spacing="3",
                wrap="wrap",
                margin_top="15px"
            )
        ),
        width=rx.breakpoints(initial="100%", md="50%"),
        align="start"
    )

def panel_informacion_producto() -> rx.Component:
    """Columna derecha: Título, Precio Dinámico, Selector de Variantes (Amazon style), Cantidad y Botones."""
    return rx.vstack(
        # Título del producto
        rx.heading(
            State.producto_detalle["nombre"],
            size="7",
            color="#2C3639",
            font_weight="normal",
            style={"font-family": "Georgia, serif"},
            margin_bottom="10px"
        ),
        
        # 🏷️ ETIQUETA Y DISEÑO DE "OFERTA RELÁMPAGO" ESTILO AMAZON
        rx.cond(
            State.porcentaje_descuento_activo > 0,
            rx.vstack(
                # Badge Rojo Oferta Relámpago
                rx.box(
                    rx.text("Oferta Relámpago", color="#FFFFFF", size="1", font_weight="bold"),
                    background_color="#CC0C39",
                    padding="4px 10px",
                    border_radius="4px",
                    margin_bottom="6px"
                ),
                # Porcentaje en Rojo + Precio de Oferta en Grande
                rx.hstack(
                    rx.text(f"-{State.porcentaje_descuento_activo}%", color="#CC0C39", size="6", font_weight="bold"),
                    rx.hstack(
                        rx.text("US$", color="#2C3639", size="3", font_weight="bold"),
                        rx.text(
                            rx.cond(
                                State.variantes_producto.length() > 0,
                                State.variante_seleccionada["precio"],
                                State.producto_detalle["precio"]
                            ),
                            color="#2C3639", 
                            size="7", 
                            font_weight="bold"
                        ),
                        spacing="1",
                        align="baseline"
                    ),
                    spacing="3",
                    align="center"
                ),
                # Precio recomendado tachado
                rx.hstack(
                    rx.text("Precio recomendado:", size="1", color="#565959"),
                    rx.text(
                        "US$",
                        size="1",
                        color="#565959",
                        style={"text_decoration": "line-through"}
                    ),
                    rx.text(
                        rx.cond(
                            State.variantes_producto.length() > 0,
                            State.variante_seleccionada["precio_anterior"],
                            State.producto_detalle["precio_anterior"]
                        ),
                        size="1",
                        color="#565959",
                        style={"text_decoration": "line-through"}
                    ),
                    spacing="1",
                    align="center"
                ),
                align="start",
                margin_bottom="15px"
            ),
            # Precio Normal (Cuando no hay oferta activa)
            rx.hstack(
                rx.text("$", color="#2C3639", size="5", font_weight="medium"),
                rx.text(
                    rx.cond(
                        State.variantes_producto.length() > 0,
                        State.variante_seleccionada["precio"],
                        State.producto_detalle["precio"]
                    ),
                    color="#2C3639", 
                    size="5", 
                    font_weight="medium"
                ),
                rx.text("USD", color="#2C3639", size="3", font_weight="medium"),
                spacing="1",
                margin_bottom="15px"
            )
        ),
        
        rx.text("Impuestos incluidos.", size="1", color="#7F7F7F", margin_bottom="20px"),
        
        # 🎨 SELECTOR VISUAL DE VARIANTES (Amazon / Mercado Libre Style)
        rx.cond(
            State.variantes_producto.length() > 0,
            rx.vstack(
                rx.hstack(
                    rx.text("Opción:", size="2", color="#2C3639", font_weight="bold"),
                    rx.text(State.variante_seleccionada["nombre"], size="2", color="#8E6F54", font_weight="medium"),
                    spacing="2"
                ),
                rx.hstack(
                    rx.foreach(
                        State.variantes_producto,
                        lambda v: rx.button(
                            v["nombre"],
                            size="2",
                            variant=rx.cond(
                                State.variante_seleccionada["nombre"] == v["nombre"],
                                "solid",
                                "outline"
                            ),
                            background_color=rx.cond(
                                State.variante_seleccionada["nombre"] == v["nombre"],
                                "#8E6F54",
                                "transparent"
                            ),
                            color=rx.cond(
                                State.variante_seleccionada["nombre"] == v["nombre"],
                                "#FFFFFF",
                                "#2C3639"
                            ),
                            border_color="#8E6F54",
                            border_radius="0px",
                            opacity=rx.cond(v["stock"], "1.0", "0.4"),
                            cursor=rx.cond(v["stock"], "pointer", "not-allowed"),
                            on_click=lambda: State.seleccionar_variante(v)
                        )
                    ),
                    spacing="2",
                    wrap="wrap"
                ),
                margin_bottom="25px",
                align="start"
            )
        ),

        # Descripciones
        rx.text(
            State.producto_detalle["descripcion"],
            color="#4A5568",
            size="3",
            line_height="1.7",
            margin_bottom="25px"
        ),
        
        # Selector de Cantidad
        rx.vstack(
            rx.hstack(
                rx.text("Cantidad", size="2", color="#2C3639", font_weight="medium"),
                rx.cond(
                    State.variantes_producto.length() > 0,
                    rx.text(f"({State.variante_seleccionada['stock']} disponibles)", size="1", color="#7F7F7F"),
                    rx.text(f"({State.producto_detalle['stock']} disponibles)", size="1", color="#7F7F7F")
                ),
                spacing="2",
                align="center"
            ),
            rx.hstack(
                rx.button(
                    "-",
                    variant="ghost",
                    color="#2C3639",
                    size="2",
                    on_click=State.decrementar_cantidad,
                    cursor="pointer"
                ),
                rx.text(State.cantidad_producto, color="#2C3639", size="3", padding_x="15px"),
                rx.button(
                    "+",
                    variant="ghost",
                    color="#2C3639",
                    size="2",
                    on_click=State.incrementar_cantidad,
                    cursor="pointer"
                ),
                border="1px solid #C8C2BC",
                padding="2px 10px",
                align="center"
            ),
            align="start",
            margin_bottom="25px"
        ),
        
        # Botones principales
        rx.vstack(
           rx.button(
                "Añadir al carrito",
                width="100%",
                height="48px",
                variant="outline",
                color="#8E6F54",
                border_color="#8E6F54",
                border_radius="0px",
                font_weight="medium",
                cursor="pointer",
                _hover={"background_color": "#FAF6F0"},
                # 🔗 CONEXIÓN ACTIVA CON EL CARRITO
                on_click=State.agregar_al_carrito
            ),
            rx.button(
                "Comprar Ahora",
                width="100%",
                height="48px",
                background_color="#5A31F4",
                color="#FFFFFF",
                border_radius="0px",
                font_weight="bold",
                cursor="pointer",
                _hover={"opacity": "0.9"},
                # 🚀 Redirección inmediata al checkout con el producto
                on_click=State.comprar_ahora
            ),
            rx.hstack(
                rx.icon(tag="share-2", size=14, color="#8E6F54"),
                rx.text("Compartir", size="2", color="#8E6F54", cursor="pointer"),
                spacing="2",
                align="center",
                margin_top="10px",
                cursor="pointer",
                # 📲 Apertura de la API de WhatsApp para compartir enlace
                on_click=State.compartir_producto_whatsapp
            
            ),

            width="100%",
            spacing="3",
            margin_bottom="30px"
        ),
        width=rx.breakpoints(initial="100%", md="50%"),
        align="start",
        padding_left=rx.breakpoints(initial="0px", md="30px")
    )

def seccion_recomendados() -> rx.Component:
    """Sección inferior: 'Quizás también te guste' con 4 tarjetas recomendadas."""
    return rx.cond(
        State.productos_recomendados.length() > 0,
        rx.vstack(
            rx.center(rx.box(width="100%", height="1px", background_color="#EAE5DF"), width="100%", padding_y="40px"),
            rx.vstack(
                rx.heading(
                    "Quizás también te guste",
                    size="6",
                    color="#2C3639",
                    font_weight="normal",
                    style={"font-family": "Georgia, serif"}
                ),
                rx.hstack(
                    rx.text(
                        State.producto_detalle["categoria"],
                        size="2",
                        color="#8E6F54",
                        font_weight="bold"
                    ),
                    rx.icon(tag="arrow-right", size=16, color="#8E6F54"),
                    spacing="1",
                    align="center",
                    cursor="pointer",
                    _hover={"opacity": "0.8", "transform": "translateX(2px)"},
                    transition="all 0.2s ease",
                    on_click=lambda: State.navegar_vista_categoria(State.producto_detalle["categoria"])
                ),
                align="start",
                spacing="2",
                width="100%",
                margin_bottom="35px"
            ),

            rx.flex(
                rx.foreach(State.productos_recomendados, tarjeta_producto_revista),
                width="100%",
                flex_direction=rx.breakpoints(initial="column", sm="row"),
                flex_wrap="wrap",
                justify="start",
                gap="4"
            ),
            width="100%"
        )
    )

# 📌 RUTA DINÁMICA: Registra /product/[id] y ejecuta la carga automática al entrar
@rx.page(route="/product/[id]", on_load=State.cargar_producto_por_id)
def product_page() -> rx.Component:
    """Vista principal con layout unificado de la Tribu."""
    return plantilla_tribu(
        rx.center(
            rx.vstack(
                # Botón superior 'Volver a la Tienda'
                rx.button(
                    rx.hstack(rx.icon(tag="arrow-left", size=14), rx.text("Volver a la Tienda Principal", size="2")),
                    variant="ghost",
                    color="#7F7F7F",
                    cursor="pointer",
                    margin_bottom="30px",
                    align_self="start",
                    on_click=State.navegar_revista_principal
                ),
                # Bloque de 2 columnas (Fotos | Info)
                rx.flex(
                    galeria_imagenes(),
                    panel_informacion_producto(),
                    width="100%",
                    flex_direction=rx.breakpoints(initial="column", md="row"),
                    align="start",
                    gap="6"
                ),
                # Bloque inferior (Recomendaciones)
                seccion_recomendados(),
                width="100%",
                max_width="1080px",
                padding_x="15px"
            ),
            width="100%",
            background_color="#FAF6F0",
            padding_y="40px"
        ),
        pagina_activa="shop"
    )
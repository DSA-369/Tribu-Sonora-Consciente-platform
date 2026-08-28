# sound_healing_platform/sound_healing_platform.py
import reflex as rx

from sound_healing_platform.components.layout import plantilla_tribu
from sound_healing_platform.pages.acerca_de import acerca_de_page
from sound_healing_platform.pages.admin import admin_page
from sound_healing_platform.pages.asistencia import asistencia_page
from sound_healing_platform.pages.checkout import vista_checkout
from sound_healing_platform.pages.contacto import contacto_page
from sound_healing_platform.pages.detalle_guia import detalle_guia_page
from sound_healing_platform.pages.gift_cards import gift_cards_page
from sound_healing_platform.pages.horario_sesiones import horario_sesiones_page
from sound_healing_platform.pages.login import login_page
from sound_healing_platform.pages.paquetes_sesiones import paquetes_sesiones_page
from sound_healing_platform.pages.privacidad import privacidad_page
from sound_healing_platform.pages.product import product_page
from sound_healing_platform.pages.rastreo import rastreo_page
from sound_healing_platform.pages.servicios import servicios_page
from sound_healing_platform.pages.shop import shop_page
from sound_healing_platform.pages.talleres import talleres_page
from sound_healing_platform.pages.terminos import terminos_page
from sound_healing_platform.state import State


def index() -> rx.Component:
    # Le indicamos a la plantilla que resalte "home"
    return plantilla_tribu(
        rx.vstack(
            # 1. SECCIÓN HERO (PORTADA ORIGINAL CON BOTONES RESPONSIVOS)
            rx.center(
                rx.flex(
                    rx.center(rx.image(src="/home_hero2.jpg", width="90%", height="auto", border_radius="8px"), width=rx.breakpoints(initial="100%", md="50%"), padding="20px"),
                    rx.vstack(
                        rx.heading("¿QUÉ PASARÍA SI PUDIÉRAMOS CAMBIAR NUESTRO ESTADO DE SER A UNA FRECUENCIA MÁS ALTA A TRAVÉS DEL SONIDO? ¿PUEDE EL MISMO PODER MEJORAR LA CURACIÓN O NUESTRO BIENESTAR? ¿PODRÍA TAMBIÉN SER EL CATALIZADOR PARA CREAR UN PLANETA MÁS COMPASIVO Y COOPERATIVO?", size="5", color="#2C3639", font_weight="medium", line_height="1.5", margin_bottom="15px", style={"font-family": "Georgia, serif"}),
                        rx.text("Somos un tejido de terapeutas sonoros que desde el 2019 estamos acompañando a elevar la vibración, aliviar el dolor físico, mental y espiritual, promoviendo la salud y el bienestar colectivo", size="4", color="#2C3639", font_weight="medium", line_height="1.5", margin_bottom="15px", style={"font-family": "Georgia, serif"}),
                        rx.text("Nuestra Terapia Vibracional o Sound Healing", size="4", color="#A27B5C", italic=True, margin_bottom="20px", style={"font-family": "Georgia, serif"}),
                        rx.vstack(
                            rx.text(rx.text.strong("Duración: "), "aproximadamente de 45 minutos a 1 hora.", color="#4B5563", size="3"),
                            rx.text(rx.text.strong("La experiencia: "), "un viaje energético de conexión, sensorialidad y autodescubrimiento.", color="#4B5563", size="3"),
                            rx.text(rx.text.strong("Los beneficios: "), "equilibrio holístico para cuerpo, mente y espíritu a través de la tecnología del sonido.", color="#4B5563", size="3"),
                            rx.text(rx.text.strong("La técnica: "), "inducido mediante la voz y nuestra variada selección de instrumentos ancestrales étnicos de alta frecuencia vibratoria.", color="#4B5563", size="3"),
                            align="start", spacing="3", width="100%",
                        ),
                        rx.flex(
                            rx.button(
                                "RESERVA UNA SESIÓN", 
                                size="3", 
                                background_color="#8E6F54", 
                                color="#FFFFFF", 
                                font_weight="bold", 
                                letter_spacing="0.05em", 
                                padding_x="24px", 
                                cursor="pointer", 
                                _hover={"background_color": "#73573F"}, 
                                width=rx.breakpoints(initial="100%", sm="auto"),
                                on_click=State.ir_a_horario_sesiones
                            ),
                            rx.button(
                                "CONSULTE LOS SERVICIOS", 
                                size="3", 
                                variant="outline", 
                                color="#8E6F54", 
                                border_color="#8E6F54", 
                                font_weight="bold", 
                                letter_spacing="0.05em", 
                                padding_x="24px", 
                                cursor="pointer", 
                                _hover={"background_color": "rgba(142, 111, 84, 0.05)"}, 
                                width=rx.breakpoints(initial="100%", sm="auto"),
                                on_click=rx.redirect("/servicios")
                            ),
                            flex_direction=rx.breakpoints(initial="column", sm="row"),
                            gap="6", 
                            margin_top="30px",
                            width="100%",
                            justify="start",
                            align_items="center"
                        ),
                        width=rx.breakpoints(initial="100%", md="50%"), align="start", padding="40px",
                    ),
                    width="100%", max_width="1200px", flex_direction=rx.breakpoints(initial="column", md="row"), align_items="center",
                ),
                width="100%", padding_y="60px", background_color="#FAF6F0",
            ),

            # 2. FRANJA DE EVENTOS DESTACADOS
            rx.vstack(
                rx.text("EVENTOS DESTACADOS", size="2", letter_spacing="0.2em", color="#7F7F7F", font_weight="medium", margin_bottom="25px"),
                rx.flex(
                    rx.foreach(State.eventos_destacados, lambda evento: rx.link(rx.cond(evento["logo"] != "", rx.image(src=evento["logo"], height="45px", width="auto", object_fit="contain"), rx.text(evento["nombre"], size="2", font_weight="medium", color="#2C3639", letter_spacing="0.05em", text_align="center", white_space="pre-line", style={"font-family": "Times New Roman, serif"}, _hover={"color": "#A27B5C", "transition": "color 0.2s"})), href=evento["url"], is_external=True, text_decoration="none")),
                    width="100%", max_width="1100px", flex_direction="row", flex_wrap="wrap", justify_content="space-around", align_items="center", gap="35px", 
                ),
                width="100%", padding_y="45px", border_top="1px solid #EAE5DF", border_bottom="1px solid #EAE5DF", background_color="#FDFBF9", align="center",
            ),

            # 3. GALERÍA ESTILO COLLAGE ASIMÉTRICO (Fondo Crema #FAF6F0)
            rx.center(
                rx.flex(
                    rx.vstack(
                        rx.image(src=State.imagenes_galeria[0], width="100%", height="auto", border_radius="4px"),
                        rx.image(src=State.imagenes_galeria[3], width="100%", height="auto", border_radius="4px"),
                        rx.image(src=State.imagenes_galeria[6], width="100%", height="auto", border_radius="4px"),
                        spacing="3", width="100%", flex="1",
                    ),
                    rx.vstack(
                        rx.image(src=State.imagenes_galeria[1], width="100%", height="auto", border_radius="4px"),
                        rx.image(src=State.imagenes_galeria[4], width="100%", height="auto", border_radius="4px"),
                        rx.image(src=State.imagenes_galeria[7], width="100%", height="auto", border_radius="4px"),
                        spacing="3", width="100%", flex="1",
                    ),
                    rx.vstack(
                        rx.image(src=State.imagenes_galeria[2], width="100%", height="auto", border_radius="4px"),
                        rx.image(src=State.imagenes_galeria[5], width="100%", height="auto", border_radius="4px"),
                        rx.image(src=State.imagenes_galeria[8], width="100%", height="auto", border_radius="4px"),
                        spacing="3", width="100%", flex="1",
                    ),
                    width="100%", max_width="1150px", flex_direction=rx.breakpoints(initial="column", md="row"), align_items="start", gap="16px", padding_x="20px",
                ),
                width="100%", padding_y="60px", background_color="#FAF6F0",
            ),

            # 4. FRANJA DE TESTIMONIOS
            rx.vstack(
                rx.heading("Testimonios", size="7", color="#2C3639", font_weight="normal", margin_bottom="40px", style={"font-family": "Georgia, serif"}),
                rx.flex(rx.foreach(State.testimonios, lambda item: rx.vstack(rx.text(item["texto"], size="3", color="#2C3639", text_align="center", line_height="1.6", italic=True, style={"font-family": "Georgia, serif"}), rx.vstack(rx.text(item["autor"], size="2", font_weight="medium", color="#2C3639", margin_top="15px"), rx.text(item["ciudad"], size="1", color="#7F7F7F", letter_spacing="0.05em"), spacing="0", align="center"), width=rx.breakpoints(initial="100%", md="30%"), align="center", spacing="2", padding="20px")), width="100%", max_width="1200px", flex_direction=rx.breakpoints(initial="column", md="row"), justify_content="space-between", align_items="start", gap="30px"),
                width="100%", padding_y="60px", border_top="1px solid #EAE5DF", border_bottom="1px solid #EAE5DF", background_color="#FDFBF9", align="center",
            ),

            # 5. FRANJA INTERACTIVA: FEED INFINITO DE INSTAGRAM
            rx.vstack(
                rx.text("SÍGUENOS EN INSTAGRAM @TRIBUSONORACONSCIENTE", size="1", letter_spacing="0.25em", color="#7F7F7F", font_weight="medium", margin_bottom="25px"),
                rx.box(rx.hstack(rx.foreach(State.feed_instagram, lambda post: rx.link(rx.image(src=post["foto"], width="220px", height="220px", object_fit="cover", _hover={"opacity": "0.85", "transition": "opacity 0.2s"}), href=post["url"], is_external=True)), rx.foreach(State.feed_instagram, lambda post: rx.link(rx.image(src=post["foto"], width="220px", height="220px", object_fit="cover", _hover={"opacity": "0.85", "transition": "opacity 0.2s"}), href=post["url"], is_external=True)), spacing="4", style={"animation": "infinito 25s linear infinite", "width": "max-content", "_hover": {"animation_play_state": "paused"}}), width="100%", overflow="hidden", padding_y="10px"),
                width="100%", padding_y="50px", background_color="#FDFBF9", border_bottom="1px solid #EAE5DF", align="center",
            ),
            spacing="0", width="100%",
        ),
        pagina_activa="home"
    )

app = rx.App()
app.add_page(index, route="/", title="Tribu Sonora Consciente", on_load=[State.cargar_datos_db, State.cargar_notificaciones_usuario])
app.add_page(contacto_page, route="/contacto", title="Contacto | Tribu Sonora Consciente")
app.add_page(acerca_de_page, route="/acerca-de", title="Acerca de | Tribu Sonora Consciente", on_load=State.cargar_datos_db)
app.add_page(detalle_guia_page, route="/biografia/[id]", title="Guía | Tribu Sonora Consciente", on_load=State.cargar_detalle_guia)
app.add_page(shop_page, route="/shop", title="Shop | Tribu Sonora Consciente", on_load=State.cargar_datos_db)
app.add_page(vista_checkout, route="/checkout", title="Checkout | Tribu Sonora Consciente", on_load=[State.cargar_metodos_pago, State.autocompletar_checkout_usuario])
app.add_page(rastreo_page, route="/rastreo", title="Rastrear Orden | Tribu Sonora Consciente")
app.add_page(servicios_page, route="/servicios", title="Tipo de Servicios | Tribu Sonora Consciente", on_load=State.cargar_datos_db)
app.add_page(talleres_page, route="/talleres", title="Talleres | Tribu Sonora Consciente", on_load=State.cargar_datos_db)
app.add_page(horario_sesiones_page, route="/sesiones/horario", title="Horario de Sesiones | Tribu Sonora Consciente", on_load=State.cargar_datos_db)
app.add_page(paquetes_sesiones_page, route="/sesiones/paquetes", title="Precios y Paquetes | Tribu Sonora Consciente")
app.add_page(asistencia_page, route="/asistencia/[token]", title="Control de Asistencia | Tribu Sonora Consciente", on_load=State.cargar_lista_asistencia_por_token)
app.add_page(admin_page, route="/admin", title="Panel Administrador | Tribu Sonora Consciente", on_load=[State.verificar_sesion_persistente, State.cargar_datos_admin, State.cargar_notificaciones_usuario])
app.add_page(login_page, route="/login", title="Iniciar Sesión | Tribu Sonora Consciente", on_load=[State.verificar_sesion_persistente, State.cargar_notificaciones_usuario])
app.add_page(privacidad_page, route="/politica-de-privacidad", title="Política de Privacidad | Tribu Sonora Consciente")
app.add_page(terminos_page, route="/terminos-y-condiciones", title="Términos y Condiciones | Tribu Sonora Consciente")
app.add_page(gift_cards_page, route="/tarjetas-de-regalo", title="Tarjetas de Regalo | Tribu Sonora Consciente")
app.add_page(product_page, route="/product/[id]", title="Producto | Tribu Sonora Consciente", on_load=State.cargar_producto_por_id)
# sound_healing_platform/pages/acerca_de.py
import reflex as rx

from sound_healing_platform.components.layout import plantilla_tribu
from sound_healing_platform.state import State


def acerca_de_page() -> rx.Component:
    return plantilla_tribu(
        rx.vstack(
            # CABECERA PRINCIPAL Y QUIÉNES SOMOS
            rx.center(
                rx.vstack(
                    rx.heading(
                        
                    ),
                    rx.text(
                        '"El Sonido como Puente hacia la Armonía. En Tribu Sonora Consciente entendemos la relajación profunda no como un lujo, sino como la base fundamental de la salud y el bienestar integral"',
                        size="4", 
                        color="#8E6F54", 
                        text_align="center", 
                        italic=True, 
                        max_width="750px", 
                        margin_top="15px", 
                        style={"font-family": "Georgia, serif"}
                    ),
                    rx.box(
                        rx.heading(
                            "QUIÉNES SOMOS", 
                            size="5", 
                            color="#2C3639", 
                            font_weight="normal", 
                            letter_spacing="0.1em", 
                            style={"font-family": "Georgia, serif"}, 
                            margin_y="25px",
                            text_align="center"
                        ),
                        rx.flex(
                            rx.vstack(
                                rx.text(
                                    "Nacemos de la convicción profunda de que la psique y el cuerpo humano poseen una capacidad innata para autorregularse, integrarse y reconstruirse. Somos Tribu Sonora Consciente, un equipo integrado por Danibeth, Jarold y Jesús, unidos por la vocación de facilitar espacios de presencia, contención y restauración somática a través del poder de la medicina sonora.",
                                    size="3", color="#4B5563", line_height="1.8"
                                ),
                                width=rx.breakpoints(initial="100%", md="48%"), align="start"
                            ),
                            rx.vstack(
                                rx.text(
                                    "Nuestra propuesta no nace únicamente del estudio técnico de la acústica, la neurobiología y la música; nace de la experiencia de vida. Entendemos la resiliencia porque hemos transitado nuestros propios fuegos, duelos y transformaciones. Conocemos de primera mano lo que significa convertir el cambio en presencia y la pérdida en un renovado propósito de servicio. Por ello, cada encuentro que facilitamos es sostenido con empatía real, sobriedad ética y una profunda humanidad.",
                                    size="3", color="#4B5563", line_height="1.8"
                                ),
                                width=rx.breakpoints(initial="100%", md="48%"), align="start"
                            ),
                            width="100%",
                            flex_direction=rx.breakpoints(initial="column", md="row"),
                            justify="between",
                            gap="6"
                        ),
                        width="100%",
                        margin_top="30px"
                    ),
                    width="100%", max_width="950px", align="center", padding_x="20px"
                ),
                width="100%", padding_y="70px", background_color="#FAF6F0"
            ),

            # Separación sutil
            rx.center(rx.box(width="85%", height="1px", background_color="#EAE5DF"), width="100%", background_color="#FAF6F0"),

            # SECCIÓN: NUESTRA FILOSOFÍA (id="filosofia")
            rx.center(
                rx.vstack(
                    rx.heading(
                        "NUESTRA FILOSOFÍA: EL SONIDO COMO MEDICINA", 
                        size="7", 
                        color="#2C3639", 
                        font_weight="normal", 
                        letter_spacing="0.08em", 
                        style={"font-family": "Georgia, serif"}, 
                        margin_bottom="15px",
                        text_align="center"
                    ),
                    rx.text(
                        "Entendemos la vibración como una herramienta de precisión para la salud integral del ser humano.",
                        size="3", color="#8E6F54", text_align="center", font_weight="medium", margin_bottom="40px"
                    ),
                    rx.flex(
                        rx.vstack(
                            rx.heading("La Lente Neurosomática", size="4", color="#2C3639", font_weight="semibold", style={"font-family": "Georgia, serif"}, margin_bottom="10px"),
                            rx.text(
                                "Las frecuencias armónicas de los cuencos de cuarzo, el soplo ancestral del didgeridoo y el pulso rítmico del tambor actúan directamente sobre el sistema nervioso autónomo. Al acallar la hiperactividad de la mente cotidiana, el sonido ayuda a reducir el estrés, liberar cargas atrapadas en el cuerpo y restaurar la coherencia cardíaca y cerebral.",
                                size="3", color="#4B5563", line_height="1.7"
                            ),
                            width=rx.breakpoints(initial="100%", md="48%"),
                            padding="25px",
                            background_color="#FFFFFF",
                            border_radius="8px",
                            border="1px solid #EAE5DF",
                            align="start"
                        ),
                        rx.vstack(
                            rx.heading("La Lente Ancestral y Ceremonial", size="4", color="#2C3639", font_weight="semibold", style={"font-family": "Georgia, serif"}, margin_bottom="10px"),
                            rx.text(
                                "Honramos la memoria del sonido como un lenguaje universal que trasciende las palabras. La resonancia actúa como un espejo del alma, abriendo un espacio sagrado donde es posible soltar el peso del pasado, sintonizar con la calma interior y reencontrar el sentido de pertenencia con la totalidad.",
                                size="3", color="#4B5563", line_height="1.7"
                            ),
                            width=rx.breakpoints(initial="100%", md="48%"),
                            padding="25px",
                            background_color="#FFFFFF",
                            border_radius="8px",
                            border="1px solid #EAE5DF",
                            align="start"
                        ),
                        width="100%",
                        flex_direction=rx.breakpoints(initial="column", md="row"),
                        justify="between",
                        gap="6"
                    ),

                    # GALERÍA DE 4 PILARES / HITOS VISUALES
                    rx.flex(
                        rx.vstack(
                            rx.image(src="/hito_raiz01.png", width="100%", height="140px", object_fit="cover"),
                            rx.heading("Sabiduría Ancestral", size="4", color="#2C3639", font_weight="semibold", style={"font-family": "Georgia, serif"}, margin_top="10px"),
                            rx.text("Honramos las raíces y la medicina natural, utilizando herramientas sonoras milenarias que reconectan al ser con su esencia primaria.", size="2", color="#7F7F7F", line_height="1.5"),
                            width=rx.breakpoints(initial="100%", sm="45%", md="23%"), align="start"
                        ),
                        rx.vstack(
                            rx.image(src="/hito_tech02.png", width="100%", height="140px", object_fit="cover"),
                            rx.heading("Tecnología del Sonido", size="4", color="#2C3639", font_weight="semibold", style={"font-family": "Georgia, serif"}, margin_top="10px"),
                            rx.text("Aplicamos frecuencias y armónicos diseñados para desacelerar las ondas cerebrales, estimular el nervio vago e inducir estados de relajación somática profunda.", size="2", color="#7F7F7F", line_height="1.5"),
                            width=rx.breakpoints(initial="100%", sm="45%", md="23%"), align="start"
                        ),
                        rx.vstack(
                            rx.image(src="/hito_acompaña03.png", width="100%", height="140px", object_fit="cover"),
                            rx.heading("Acompañamiento Consciente", size="4", color="#2C3639", font_weight="semibold", style={"font-family": "Georgia, serif"}, margin_top="10px"),
                            rx.text("Sostenemos espacios seguros e íntimos donde cada persona, sin importar su edad, puede liberar carga emocional, sanar y autorregular su sistema nervioso.", size="2", color="#7F7F7F", line_height="1.5"),
                            width=rx.breakpoints(initial="100%", sm="45%", md="23%"), align="start"
                        ),
                        rx.vstack(
                            rx.image(src="/hito_web04.png", width="100%", height="140px", object_fit="cover"),
                            rx.heading("Santuario Digital", size="4", color="#2C3639", font_weight="semibold", style={"font-family": "Georgia, serif"}, margin_top="10px"),
                            rx.text("Tu portal directo para acceder a sesiones privadas, eventos colectivos, talleres formativos e instrumentos rituales desde cualquier lugar..", size="2", color="#7F7F7F", line_height="1.5"),
                            width=rx.breakpoints(initial="100%", sm="45%", md="23%"), align="start"
                        ),
                        width="100%",
                        flex_direction=rx.breakpoints(initial="column", sm="row"),
                        flex_wrap="wrap",
                        justify="between",
                        gap="6",
                        margin_top="50px"
                    ),
                    width="100%", max_width="950px", align="center", padding_x="20px"
                ),
                id="filosofia",
                width="100%", padding_y="80px", background_color="#FAF6F0"
            ),

            # Separación sutil
            rx.center(rx.box(width="85%", height="1px", background_color="#EAE5DF"), width="100%", background_color="#FAF6F0"),

            # SECCIÓN: NUESTRO PROPÓSITO
            rx.center(
                rx.vstack(
                    rx.heading(
                        "NUESTRO PROPÓSITO", 
                        size="7", 
                        color="#2C3639", 
                        font_weight="normal", 
                        letter_spacing="0.1em", 
                        style={"font-family": "Georgia, serif"}, 
                        margin_bottom="15px",
                        text_align="center"
                    ),
                    rx.text(
                        "Existimos para ofrecer un refugio acústico seguro donde las personas puedan hacer una pausa, respirar y retornar a su centro.",
                        size="3", color="#8E6F54", text_align="center", font_weight="medium", max_width="750px", margin_bottom="45px"
                    ),
                    rx.flex(
                        rx.vstack(
                            rx.heading("Crear Comunidad", size="4", color="#2C3639", font_weight="semibold", style={"font-family": "Georgia, serif"}, margin_bottom="8px"),
                            rx.text(
                                "Establecer espacios continuos de encuentro donde la salud mental, emocional y espiritual sea accesible y cultivada de manera colectiva.",
                                size="2", color="#4B5563", line_height="1.6"
                            ),
                            width=rx.breakpoints(initial="100%", sm="48%", md="31%"),
                            align="start"
                        ),
                        rx.vstack(
                            rx.heading("Servicio y Contención", size="4", color="#2C3639", font_weight="semibold", style={"font-family": "Georgia, serif"}, margin_bottom="8px"),
                            rx.text(
                                "Acompañar tanto en momentos de celebración de la vida como en etapas de vulnerabilidad y reconstrucción social, llevando la vibración allí donde se necesite calma y firmeza.",
                                size="2", color="#4B5563", line_height="1.6"
                            ),
                            width=rx.breakpoints(initial="100%", sm="48%", md="31%"),
                            align="start"
                        ),
                        rx.vstack(
                            rx.heading("Facilitación Impecable", size="4", color="#2C3639", font_weight="semibold", style={"font-family": "Georgia, serif"}, margin_bottom="8px"),
                            rx.text(
                                "Sostener cada sesión con respeto absoluto por el proceso individual de cada participante, sin dogmatismos ni imposiciones, permitiendo que sea la propia sabiduría del cuerpo la que guíe la integración.",
                                size="2", color="#4B5563", line_height="1.6"
                            ),
                            width=rx.breakpoints(initial="100%", sm="48%", md="31%"),
                            align="start"
                        ),
                        width="100%",
                        flex_direction=rx.breakpoints(initial="column", sm="row"),
                        flex_wrap="wrap",
                        justify="between",
                        gap="6",
                        margin_bottom="50px"
                    ),

                    # BLOQUE DESTACADO DE MENSAJE DE CIERRE
                    rx.box(
                        rx.text(
                            '"No venimos a entregarte nada que no poseas ya. Venimos a tejer la atmósfera sonora para que recuerdes cómo escucharte, soltar lo que ya cumplió su ciclo y resurgir con solidez en tu vida cotidiana."',
                            size="4", 
                            color="#2C3639", 
                            italic=True, 
                            text_align="center", 
                            line_height="1.8",
                            style={"font-family": "Georgia, serif"}
                        ),
                        width="100%",
                        padding="35px 25px",
                        background_color="#EAE5DF",
                        border_radius="8px"
                    ),
                    width="100%", max_width="950px", align="center", padding_x="20px"
                ),
                width="100%", padding_y="80px", background_color="#FAF6F0"
            ),

            # Separación sutil
            rx.center(rx.box(width="85%", height="1px", background_color="#EAE5DF"), width="100%", background_color="#FAF6F0"),

            # SECCIÓN 3: CONOZCA A LOS GUÍAS (id="guias")
            rx.center(
                rx.vstack(
                    rx.heading("CONOCE A LOS GUÍAS", size="7", color="#2C3639", font_weight="normal", letter_spacing="0.1em", style={"font-family": "Georgia, serif"}, margin_bottom="45px"),
                    
                    # Cuadrícula horizontal de Guías - 100% Rectangulares
                    rx.flex(
                        rx.foreach(
                            State.guias_tribu,
                            lambda guia: rx.vstack(
                                rx.image(src=guia["foto"], width="100%", height="280px", object_fit="cover", border_radius="0px"),
                                rx.heading(guia["nombre"], size="4", color="#2C3639", font_weight="semibold", style={"font-family": "Georgia, serif"}, margin_top="15px"),
                                rx.text(guia["descripcion"], size="2", color="#7F7F7F", style={"font-family": "Georgia, serif"}, margin_top="4px"),
                                rx.link(
                                    rx.hstack(
                                        rx.text("Leer biografía", size="2", color="#8E6F54", font_weight="medium"),
                                        rx.icon(tag="arrow-right", size=12, color="#8E6F54"),
                                        spacing="1", align="center"
                                    ),
                                    href="/biografia/" + guia["id"],
                                    text_decoration="none",
                                    margin_top="12px"
                                ),
                                align="start",
                                width=rx.breakpoints(initial="100%", sm="48%", md="33%"),
                                padding_x="15px",
                                margin_bottom="30px"
                            )
                        ),
                        width="100%",
                        flex_direction=rx.breakpoints(initial="column", sm="row"),
                        flex_wrap="wrap",
                        justify="center",
                        gap="0"
                    ),
                    width="100%", max_width="950px", align="center", padding_x="5px"
                ),
                id="guias",
                width="100%", padding_y="80px", background_color="#FAF6F0",
            ),

            # Separación sutil
            rx.center(rx.box(width="85%", height="1px", background_color="#EAE5DF"), width="100%", background_color="#FAF6F0"),

            # SECCIÓN 4: CONOZCA NUESTROS ALIADOS (id="aliados")
            rx.center(
                rx.vstack(
                    rx.heading("CONOZCA NUESTROS ALIADOS", size="7", color="#2C3639", font_weight="normal", letter_spacing="0.1em", style={"font-family": "Georgia, serif"}, margin_bottom="30px"),
                    rx.text("Pronto compartiremos las maravillosas marcas, terapeutas y espacios aliados que expanden la vibración junto a nosotros.", size="3", color="#7F7F7F", text_align="center", max_width="600px"),
                    width="100%", max_width="950px", align="center", padding_x="20px"
                ),
                id="aliados",
                width="100%", padding_y="80px", background_color="#FAF6F0",
            ),

            # Separación sutil
            rx.center(rx.box(width="85%", height="1px", background_color="#EAE5DF"), width="100%", background_color="#FAF6F0"),

            # SECCIÓN 5: DIARIO / BITÁCORA DE INTEGRACIÓN (id="diario")
            rx.center(
                rx.vstack(
                    rx.heading(
                        "BITÁCORA DE INTEGRACIÓN",
                        size=rx.breakpoints(initial="6", sm="7"),
                        color="#2C3639",
                        font_weight="normal",
                        letter_spacing="0.1em",
                        style={"font-family": "Georgia, serif"},
                        margin_bottom="15px",
                        text_align="center"
                    ),
                    rx.text(
                        "Un espacio sagrado para compartir tus vivencias, procesar lo experimentado en las sesiones de sound healing y recibir acompañamiento personalizado de la Tribu.",
                        size="3",
                        color="#2C3639",
                        font_weight="medium",
                        text_align="center",
                        max_width="650px",
                        margin_bottom="35px"
                    ),
                    
                    # Formulario de Integración Terapéutica
                    rx.vstack(
                        rx.flex(
                            rx.input(
                                placeholder="Nombre completo *",
                                value=State.diario_nombre,
                                on_change=State.set_diario_nombre,
                                size="3",
                                flex="1",
                                color="#1A1A1A",
                                background_color="#FFFFFF",
                                border="1px solid #C8C2BC",
                                border_radius="8px",
                                style={
                                    "&::placeholder": {"color": "#4A5568 !important", "opacity": "1 !important"},
                                    "& input::placeholder": {"color": "#4A5568 !important", "opacity": "1 !important"}
                                },
                                width="100%"
                            ),
                            rx.input(
                                placeholder="Correo electrónico *",
                                value=State.diario_correo,
                                on_change=State.set_diario_correo,
                                size="3",
                                flex="1",
                                color="#1A1A1A",
                                background_color="#FFFFFF",
                                border="1px solid #C8C2BC",
                                border_radius="8px",
                                style={
                                    "&::placeholder": {"color": "#4A5568 !important", "opacity": "1 !important"},
                                    "& input::placeholder": {"color": "#4A5568 !important", "opacity": "1 !important"}
                                },
                                width="100%"
                            ),
                            width="100%",
                            gap="4",
                            flex_direction=rx.breakpoints(initial="column", sm="row"),
                        ),
                        rx.flex(
                            rx.input(
                                placeholder="Número de WhatsApp",
                                value=State.diario_telefono,
                                on_change=State.set_diario_telefono,
                                size="3",
                                flex="1",
                                color="#1A1A1A",
                                background_color="#FFFFFF",
                                border="1px solid #C8C2BC",
                                border_radius="8px",
                                style={
                                    "&::placeholder": {"color": "#4A5568 !important", "opacity": "1 !important"},
                                    "& input::placeholder": {"color": "#4A5568 !important", "opacity": "1 !important"}
                                },
                                width="100%"
                            ),
                            rx.input(
                                placeholder="Sesión a la que asististe",
                                value=State.diario_sesion,
                                on_change=State.set_diario_sesion,
                                size="3",
                                flex="1",
                                color="#1A1A1A",
                                background_color="#FFFFFF",
                                border="1px solid #C8C2BC",
                                border_radius="8px",
                                style={
                                    "&::placeholder": {"color": "#4A5568 !important", "opacity": "1 !important"},
                                    "& input::placeholder": {"color": "#4A5568 !important", "opacity": "1 !important"}
                                },
                                width="100%"
                            ),
                            width="100%",
                            gap="4",
                            margin_y="10px",
                            flex_direction=rx.breakpoints(initial="column", sm="row"),
                        ),
                        rx.text_area(
                            placeholder="Describe tu proceso: sensaciones físicas, emociones, visiones o dudas que hayan surgido durante o después del viaje sonoro...",
                            value=State.diario_mensaje,
                            on_change=State.set_diario_mensaje,
                            size="3",
                            width="100%",
                            height="140px",
                            color="#1A1A1A",
                            background_color="#FFFFFF",
                            border="1px solid #C8C2BC",
                            border_radius="8px",
                            style={
                                "&::placeholder": {"color": "#4A5568 !important", "opacity": "1 !important"},
                                "& textarea::placeholder": {"color": "#4A5568 !important", "opacity": "1 !important"}
                            }
                        ),
                        rx.hstack(
                            rx.checkbox(
                                checked=State.diario_privado,
                                on_change=State.set_diario_privado,
                                color_scheme="bronze"
                            ),
                            rx.text(
                                "Mantener esta consulta 100% privada entre los terapeutas y yo",
                                color="#2C3639",
                                font_weight="medium",
                                size="2"
                            ),
                            margin_top="10px",
                            align="center",
                            spacing="2"
                        ),
                        rx.button(
                            "Enviar Consulta de Integración",
                            background_color="#8E6F54",
                            color="#FFFFFF",
                            size="3",
                            padding_x="40px",
                            margin_top="20px",
                            cursor="pointer",
                            border_radius="8px",
                            width=rx.breakpoints(initial="100%", sm="auto"),
                            _hover={"background_color": "#73573F"},
                            on_click=State.enviar_consulta_diario
                        ),
                        width="100%",
                        max_width="750px",
                        align="center"
                    ),
                    width="100%",
                    max_width="950px",
                    align="center",
                    padding_x=rx.breakpoints(initial="16px", sm="24px")
                ),
                id="diario",
                width="100%",
                padding_y=rx.breakpoints(initial="50px", sm="80px"),
                background_color="#FAF6F0",
            ),

            spacing="0", width="100%",
        ),
        pagina_activa="acerca_de"
    )
# sound_healing_platform/pages/acerca_de.py
import reflex as rx

from sound_healing_platform.components.layout import plantilla_tribu
from sound_healing_platform.state import State


def acerca_de_page() -> rx.Component:
    return plantilla_tribu(
        rx.vstack(
            # SECCIÓN 1: NUESTRA FILOSOFÍA (id="filosofia")
            rx.center(
                rx.vstack(
                    rx.heading("NUESTRA FILOSOFÍA", size="8", color="#2C3639", font_weight="light", letter_spacing="0.15em", style={"font-family": "Georgia, serif"}),
                    rx.text(
                        '"El Sonido como Puente hacia la Armonía. En Tribu Sonora Consciente entendemos la relajación profunda no como un lujo, sino como la base fundamental de la salud y el bienestar integral"',
                        size="4", color="#A27B5C", text_align="center", italic=True, max_width="700px", margin_top="25px", style={"font-family": "Georgia, serif"}
                    ),
                    width="100%", max_width="950px", align="center", padding_x="20px"
                ),
                id="filosofia",
                width="100%", padding_y="80px", background_color="#FAF6F0",
            ),

            # Separación sutil
            rx.center(rx.box(width="85%", height="1px", background_color="#EAE5DF"), width="100%", background_color="#FAF6F0"),

            # SECCIÓN 2: HISTORIA (id="historia")
            rx.center(
                rx.vstack(
                    rx.heading("NUESTRA HISTORIA", size="7", color="#2C3639", font_weight="normal", letter_spacing="0.1em", style={"font-family": "Georgia, serif"}, margin_bottom="30px"),
                    
                    # Estructura de dos columnas tipo revista
                    rx.flex(
                        rx.vstack(
                            rx.text(
                                "El Origen de la Tribu. Antes de cruzar nuestras vidas, cada uno de nosotros transitó un camino individual de exploración holística. Jarold profundizó en la sanación a través del Reiki y la construcción artesanal del tambor chamánico; Danibeth se dedicó al estudio de las frecuencias de los cuencos de cuarzo, la lectura de oráculos e instrumentos ancestrales; y Jesús se sumergió en la cosmovisión, la medicina natural y las raíces de las culturas originarias de Suramérica.",
                                size="3", color="#4B5563", line_height="1.7"
                            ),
                            rx.text(
                                "En 2019, la ciudad de Caracas fue el punto de convergencia. Al reunirmos para facilitar una primera presentación colectiva, surgió la necesidad de definir nuestra identidad. En ese compartir comprendimos que habíamos conformado una familia unida por el propósito de ser canales conscientes para elevar la vibración del entorno. De esa certeza nació nuestro nombre: Tribu Sonora Consciente.",
                                size="3", color="#4B5563", line_height="1.7"
                            ),
                            width=rx.breakpoints(initial="100%", md="48%"), align="start", spacing="4"
                        ),
                        rx.vstack(
                            rx.text(
                                "Desde entonces, Jarold, Danibeth y Jesús nos consolidamos como los pilares fundamentales de este espacio. A lo largo de los años, hemos guiado innumerables sesiones individuales y grupales, talleres, inauguraciones, círculos de bienestar, voluntariados y ceremonias, posicionándonos como un referente de la sonoterapia en Venezuela.",
                                size="3", color="#4B5563", line_height="1.7"
                            ),
                            rx.text(
                                "Hoy estrenamos nuestra plataforma web como un santuario digital para acortar distancias con nuestra comunidad: un canal donde podrás explorar el universo del sound healing, reservar tus cupos, adquirir instrumentos y seguir transformando la vida a través de la frecuencia.",
                                size="3", color="#4B5563", line_height="1.7"
                            ),
                            width=rx.breakpoints(initial="100%", md="48%"), align="start", spacing="4"
                        ),
                        width="100%",
                        flex_direction=rx.breakpoints(initial="column", md="row"),
                        justify="between",
                        gap="6",
                        margin_bottom="60px"
                    ),

                    # Galería de hitos / Línea de tiempo (Imágenes locales desde assets)
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
                        gap="6"
                    ),
                    width="100%", max_width="950px", align="center", padding_x="20px"
                ),
                id="historia",
                width="100%", padding_y="80px", background_color="#FAF6F0",
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

            # SECCIÓN 5: DIARIO (id="diario")
            rx.center(
                rx.vstack(
                    rx.heading("DIARIO", size="7", color="#2C3639", font_weight="normal", letter_spacing="0.1em", style={"font-family": "Georgia, serif"}, margin_bottom="30px"),
                    rx.text("Un espacio de reflexión, escritos conscientes, novedades sobre sonoterapia y sabiduría ancestral en camino.", size="3", color="#7F7F7F", text_align="center", max_width="600px"),
                    width="100%", max_width="950px", align="center", padding_x="20px"
                ),
                id="diario",
                width="100%", padding_y="80px", background_color="#FAF6F0",
            ),

            spacing="0", width="100%",
        ),
        pagina_activa="acerca_de"
    )
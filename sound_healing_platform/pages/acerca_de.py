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
                        '"Un santuario de sonido, quietud y conexión. A través de la presencia, el ritual y la práctica suave, te guiamos de regreso a tu armonía interior."',
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
                                "Tribu Sonora Consciente fue creada como un santuario: un espacio para respirar, relajarse y reconectar con uno mismo. Enraizados en el poder sanador del sonido, se ha convertido en un lugar de encuentro para ceremonias, trabajo energético y reuniones comunitarias conscientes.",
                                size="3", color="#4B5563", line_height="1.7"
                            ),
                            rx.text(
                                "Nuestro estudio en Caracas irradia una energía suave: cálida, pacífica y profundamente acogedora. Cada detalle es intencional, diseñado para que te sientas seguro, apoyado y acompañado.",
                                size="3", color="#4B5563", line_height="1.7"
                            ),
                            width=rx.breakpoints(initial="100%", md="48%"), align="start", spacing="4"
                        ),
                        rx.vstack(
                            rx.text(
                                "Comenzó como un pequeño grupo de amigos que se reunían para baños de sonido y rituales suaves: un santuario de tranquilidad en medio de la ajetreada vida cotidiana. Con el tiempo, el espacio se convirtió en un estudio donde las personas acuden para descansar, reconocer y renovarse a través del sonido, el movimiento y la intención.",
                                size="3", color="#4B5563", line_height="1.7"
                            ),
                            width=rx.breakpoints(initial="100%", md="48%"), align="start"
                        ),
                        width="100%",
                        flex_direction=rx.breakpoints(initial="column", md="row"),
                        justify="between",
                        gap="6",
                        margin_bottom="60px"
                    ),

                    # Galería de hitos / Línea de tiempo (Corregido con placeholders estéticos)
                    rx.flex(
                        rx.vstack(
                            rx.image(src="https://images.unsplash.com/photo-1518241353330-0f7941c2d9b5?q=80&w=600&auto=format&fit=cover", width="100%", height="140px", object_fit="cover"),
                            rx.heading("2018 - La Semilla", size="4", color="#2C3639", font_weight="semibold", style={"font-family": "Georgia, serif"}, margin_top="10px"),
                            rx.text("Una pequeña reunión de meditación en grupo se transforma en una práctica sagrada arraigada en la sanación a través del sonido.", size="2", color="#7F7F7F", line_height="1.5"),
                            width=rx.breakpoints(initial="100%", sm="45%", md="23%"), align="start"
                        ),
                        rx.vstack(
                            rx.image(src="https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?q=80&w=600&auto=format&fit=cover", width="100%", height="140px", object_fit="cover"),
                            rx.heading("2020 - El primer estudio", size="4", color="#2C3639", font_weight="semibold", style={"font-family": "Georgia, serif"}, margin_top="10px"),
                            rx.text("Tribu Sonora abre su primer espacio físico, donde alimentó baños de sonido y círculos comunitarios.", size="2", color="#7F7F7F", line_height="1.5"),
                            width=rx.breakpoints(initial="100%", sm="45%", md="23%"), align="start"
                        ),
                        rx.vstack(
                            rx.image(src="https://images.unsplash.com/photo-1506126613408-eca07ce68773?q=80&w=600&auto=format&fit=cover", width="100%", height="140px", object_fit="cover"),
                            rx.heading("2022 - Lanzamiento de Ritual Corner", size="4", color="#2C3639", font_weight="semibold", style={"font-family": "Georgia, serif"}, margin_top="10px"),
                            rx.text("La tienda Ritual Corner ofrece a la comunidad tés artesanales, herramientas y artículos ceremoniales.", size="2", color="#7F7F7F", line_height="1.5"),
                            width=rx.breakpoints(initial="100%", sm="45%", md="23%"), align="start"
                        ),
                        rx.vstack(
                            rx.image(src="https://images.unsplash.com/photo-1517841905240-472988babdf9?q=80&w=600&auto=format&fit=cover", width="100%", height="140px", object_fit="cover"),
                            rx.heading("De 2024 a la actualidad", size="4", color="#2C3639", font_weight="semibold", style={"font-family": "Georgia, serif"}, margin_top="10px"),
                            rx.text("Tribu Sonora amplía su oferta con ejercicios de respiración, yoga yin, talleres y sesiones de sanación privadas.", size="2", color="#7F7F7F", line_height="1.5"),
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
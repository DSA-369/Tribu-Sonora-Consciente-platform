# sound_healing_platform/state.py
from typing import Any

import reflex as rx
import sqlalchemy as sa
import sqlmodel

# ==================================================================
# 🏛️ TABLAS DE BASE DE DATOS (SQLMODEL - ESTÁNDAR PROFESIONAL)
# ==================================================================

class InstagramPost(sqlmodel.SQLModel, table=True):
    """Modelo exacto y real para la tabla de Instagram en Supabase."""
    id: int | None = sqlmodel.Field(default=None, primary_key=True)
    foto: str
    url: str

class FeaturedEvent(sqlmodel.SQLModel, table=True):
    """Modelo exacto y real para la tabla de Eventos en Supabase."""
    id: int | None = sqlmodel.Field(default=None, primary_key=True)
    nombre: str
    logo: str
    url: str

class TribuGuide(sqlmodel.SQLModel, table=True):
    """Modelo adaptado para la Revista: ID, Nombre, Foto, Descripcion Corta y Biografia Larga."""
    id: int | None = sqlmodel.Field(default=None, primary_key=True)
    nombre: str
    foto: str
    descripcion: str
    biografia: str
class TribuService(sqlmodel.SQLModel, table=True):
    """Modelo exacto para la tabla de Servicios en Supabase."""
    __tablename__ = "tribu_services"
    id: int | None = sqlmodel.Field(default=None, primary_key=True)
    nombre: str
    foto: str
    descripcion: str
    is_active: bool = sqlmodel.Field(default=True)
    
class TribuWorkshop(sqlmodel.SQLModel, table=True):
    """Modelo exacto para la tabla de Talleres y Eventos en Supabase."""
    __tablename__ = "tribu_workshops"
    id: int | None = sqlmodel.Field(default=None, primary_key=True)
    titulo: str
    tipo: str
    foto: str
    facilitador: str
    descripcion: str
    fecha_texto: str
    hora_texto: str
    duracion_texto: str
    ubicacion: str
    precio: float
    moneda: str
    fecha_evento: str
    whatsapp_contacto: str | None = sqlmodel.Field(default=None)
    is_active: bool = sqlmodel.Field(default=True)

class TribuProduct(sqlmodel.SQLModel, table=True):
    """Modelo profesional para la tienda unificada y real en Supabase."""
    __tablename__ = "tribu_products"
    id: int | None = sqlmodel.Field(default=None, primary_key=True)
    nombre: str
    descripcion: str
    precio: float
    precio_anterior: float | None = sqlmodel.Field(default=None)
    stock: int
    is_best_seller: bool
    is_favorite: bool
    categoria: str
    proveedor: str | None = sqlmodel.Field(default=None)
    intencion: str | None = sqlmodel.Field(default=None)
    fotos: list[str] = sqlmodel.Field(default=[], sa_column=sa.Column(sa.JSON))
    variaciones: Any | None = sqlmodel.Field(default=None, sa_column=sa.Column(sa.JSON))
    is_active: bool

class TribuSession(sqlmodel.SQLModel, table=True):
    """Modelo exacto para la tabla de Sesiones Grupales Recurrentes en Supabase."""
    __tablename__ = "tribu_sessions"
    id: int | None = sqlmodel.Field(default=None, primary_key=True)
    nombre: str
    foto: str
    fotos: Any = sqlmodel.Field(default=[], sa_column=sa.Column(sa.JSON))
    ubicacion: str
    frecuencia_texto: str
    fecha_texto: str
    hora_texto: str
    hora_recepcion_texto: str | None = sqlmodel.Field(default="")
    inversion: float
    plazas_totales: int
    plazas_disponibles: int
    instagram_url: str
    recomendaciones: str
    checkin_token: str | None = sqlmodel.Field(default=None)
    patron_recurrencia: str | None = sqlmodel.Field(default="MANUAL")
    fecha_evento: str | None = sqlmodel.Field(default=None)
    is_active: bool = sqlmodel.Field(default=True)

class TribuSessionReservation(sqlmodel.SQLModel, table=True):
    """Modelo para reservas de sesiones grupales en Supabase con desglose de pago parcial."""
    __tablename__ = "tribu_session_reservations"
    id: int | None = sqlmodel.Field(default=None, primary_key=True)
    session_id: int
    nombre_cliente: str
    whatsapp_cliente: str
    cliente_email: str | None = None
    cupos: int = 1
    monto_total: float = 0.0
    porcentaje_pago: float = 100.0
    monto_pagado: float = 0.0
    monto_pendiente: float = 0.0
    estado: str = "PENDIENTE_PAGO"
    asistio: bool = False
    participantes_json: Any = sqlmodel.Field(default=[], sa_column=sa.Column(sa.JSON))
    cupon_codigo: str | None = sqlmodel.Field(default=None)
    metodo_pago: str | None = sqlmodel.Field(default=None)
    fecha_evento: str | None = sqlmodel.Field(default=None)

class TribuAdminUser(sqlmodel.SQLModel, table=True):
    """Modelo para usuarios administradores y facilitadores."""
    __tablename__ = "tribu_admin_users"
    id: int | None = sqlmodel.Field(default=None, primary_key=True)
    email: str
    password_hash: str
    nombre: str
    rol: str = "ADMIN"
    is_active: bool = True

class TribuUser(sqlmodel.SQLModel, table=True):
    """Modelo exacto para la tabla de clientes registrados en Supabase."""
    __tablename__ = "tribu_users"
    id: int | None = sqlmodel.Field(default=None, primary_key=True)
    email: str = sqlmodel.Field(index=True, unique=True)
    nombre: str
    apellido: str | None = None
    password: str
    telefono: str | None = None
    pais: str | None = "Venezuela"
    direccion: str | None = None
    apartamento: str | None = None
    ciudad: str | None = None
    codigo_postal: str | None = None
    is_active: bool = True

class TribuCart(sqlmodel.SQLModel, table=True):
    """Modelo para la persistencia del carrito de usuarios en Supabase."""
    __tablename__ = "tribu_carts"
    id: int | None = sqlmodel.Field(default=None, primary_key=True)
    user_id: int = sqlmodel.Field(index=True, unique=True)
    items_json: Any = sqlmodel.Field(default=[], sa_column=sa.Column(sa.JSON))
class TribuGiftCard(sqlmodel.SQLModel, table=True):
    """Modelo exacto para Vouchers de Experiencias y Gift Cards en Supabase."""
    __tablename__ = "tribu_gift_cards"
    id: int | None = sqlmodel.Field(default=None, primary_key=True)
    codigo: str = sqlmodel.Field(unique=True, index=True)
    tipo: str = "EXPERIENCIA"
    experiencia_nombre: str
    monto_equivalente: float
    comprador_nombre: str
    comprador_email: str
    comprador_telefono: str | None = None
    destinatario_nombre: str
    destinatario_email: str | None = None
    destinatario_whatsapp: str | None = None
    mensaje_personalizado: str | None = None
    estado: str = "PENDIENTE_PAGO"    
class TribuNotification(sqlmodel.SQLModel, table=True):
    """Modelo exacto para el sistema de notificaciones unificado en Supabase."""
    __tablename__ = "tribu_notifications"
    id: int | None = sqlmodel.Field(default=None, primary_key=True)
    destinatario_email: str | None = None
    es_admin: bool = False
    es_publico: bool = False
    titulo: str
    mensaje: str
    target_url: str = "/"
    leido: bool = False

class TribuCoupon(sqlmodel.SQLModel, table=True):
    """Modelo profesional para cupones y descuentos especiales negociados."""
    __tablename__ = "tribu_coupons"
    id: int | None = sqlmodel.Field(default=None, primary_key=True)
    codigo: str = sqlmodel.Field(unique=True, index=True)
    tipo: str = "PORCENTAJE"  # 'PORCENTAJE' o 'FIJO'
    valor: float = 0.0
    is_active: bool = True
    usos_maximos: int = 100
    usos_actuales: int = 0


# ==================================================================
# ⚙️ ESTADO DE LA APLICACIÓN (MÉTODOS Y VARIABLES DE CONTROL UI)
# ==================================================================

class State(rx.State):

    def enviar_correo_voucher_html(self, destinatario_email: str, destinatario_nombre: str, comprador_nombre: str, experiencia_nombre: str, codigo_voucher: str, mensaje_personal: str):
        """Envía el Voucher por correo HTML estándar usando smtplib en segundo plano."""
        import os
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        smtp_server = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
        smtp_port = int(os.environ.get("SMTP_PORT", "587"))
        smtp_user = os.environ.get("SMTP_USER", "")
        smtp_password = os.environ.get("SMTP_PASSWORD", "")

        if not smtp_user or not smtp_password:
            print("⚠️ SMTP no configurado en .env. Se omite envío de correo automático.")
            return

        msg = MIMEMultipart("alternative")
        msg["Subject"] = f"✨ Tu Voucher de Experiencia Tribu: {experiencia_nombre}"
        msg["From"] = f"Tribu Sonora Consciente <{smtp_user}>"
        msg["To"] = destinatario_email

        html_content = f"""
        <html>
          <body style="font-family: Georgia, serif; background-color: #FAF6F0; padding: 20px;">
            <div style="max-width: 600px; margin: auto; background-color: #FFFFFF; border: 2px solid #8E6F54; border-radius: 10px; padding: 30px;">
              <h2 style="color: #2C3639; text-align: center;">TRIBU SONORA CONSCIENTE</h2>
              <p style="text-align: center; color: #8E6F54; font-weight: bold;">VOUCHER DE EXPERIENCIA HOLÍSTICA</p>
              <hr style="border: 0; border-top: 1px solid #EAE5DF;">
              <p>Hola <strong>{destinatario_nombre}</strong>,</p>
              <p><strong>{comprador_nombre}</strong> te ha regalado una vivencia sagrada:</p>
              <div style="background-color: #FAF6F0; border-left: 4px solid #8E6F54; padding: 15px; margin: 20px 0;">
                <h3 style="margin: 0; color: #2C3639;">{experiencia_nombre}</h3>
                <p style="margin-top: 10px; color: #4A5568; font-style: italic;">"{mensaje_personal or 'Un regalo lleno de vibración y presencia.'}"</p>
              </div>
              <p style="text-align: center;">Tu Código de Canje Único:</p>
              <div style="text-align: center; margin: 20px 0;">
                <span style="background-color: #2C3639; color: #FFFFFF; font-size: 20px; font-weight: bold; letter-spacing: 2px; padding: 10px 20px; border-radius: 5px;">{codigo_voucher}</span>
              </div>
              <p style="font-size: 12px; color: #7F7F7F; text-align: center;">Válido por 6 meses. Presenta este código al agendar tu sesión por WhatsApp o en nuestra web.</p>
            </div>
          </body>
        </html>
        """
        msg.attach(MIMEText(html_content, "html"))

        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_user, smtp_password)
                server.sendmail(smtp_user, destinatario_email, msg.as_string())
            print(f"📧 Correo de Voucher enviado exitosamente a {destinatario_email}")
        except Exception as e:
            print(f"Error enviando correo SMTP: {e}")

    # ==================================================================
    # 1. LOGICA Y VARIABLES DEL HOME Y EQUIPO (DATA)
    # ==================================================================
    guias_tribu: list[dict[str, str]] = [
        {
            "id": "1", 
            "nombre": "DANIBETH", 
            "foto": "/guia_danibeth.png", 
            "descripcion": "Mujer Medicina mensajera de la vibración y guardiana de los cuencos sagrados.", 
            "biografia": "Biografía extendida de Danibeth..."
        },
        {
            "id": "2", 
            "nombre": "JESÚS BURAGLIA", 
            "foto": "/guia_jesus.png", 
            "descripcion": "Especialista de los Vientos y las medicinas de la tierra.", 
            "biografia": "Biografía extendida de Jesús..."
        },
        {
            "id": "3", 
            "nombre": "JAROLD GONZÁLEZ", 
            "foto": "/guia_jarol.png", 
            "descripcion": "Tejedor de espacios de sanación acústica profunda y vibración.", 
            "biografia": "Biografía extendida de Jarol..."
        }
    ]

    selected_guide: dict[str, str] = {}

    eventos_destacados: list[dict[str, str]] = [
        {"nombre": "SANTIAMEN WELLNESS\nHOUSE CLUB", "logo": "", "url": "https://www.instagram.com/reel/DX9teJFORp5/"},
        {"nombre": "ONVA", "logo": "", "url": "https://www.instagram.com/reel/DCfdFAvORkp/"},
        {"nombre": "CASA MORADA", "logo": "", "url": "https://www.instagram.com/reel/DLSUaMfOqUn/"},
        {"nombre": "EL RESETEO\nSensorial & Holistic\nExperience", "logo": "", "url": "https://www.instagram.com/p/DV31fnUjgnH/"},
        {"nombre": "PACHAMAMA PROYECTO", "logo": "", "url": "https://www.instagram.com/p/DZr4EnoDoTZ/"},
        {"nombre": "SUKHA FESTIVAL", "logo": "", "url": "https://www.instagram.com/reel/DK7W1t2uBmp/"},
        {"nombre": "LOS ASTROS\nVenevisión", "logo": "", "url": "https://www.instagram.com/reel/DXcp8KXlruy/"},
    ]

    imagenes_galeria: list[str] = [
        "/Galeria_foto1.jpg", "/Galeria_foto2d.jpg", "/Galeria_foto3j.jpg",
        "/Galeria_foto4.jpg", "/Galeria_foto5.jpg", "/Galeria_foto6.jpg",
        "/Galeria_foto7.jpg", "/Galeria_foto8.jpg", "/Galeria_foto9.jpg"
    ]

    feed_instagram: list[dict[str, str]] = [
        {"foto": "/ig_post1.png", "url": "https://www.instagram.com/p/CUszqYKBxQT/"}, 
        {"foto": "/ig_post2.png", "url": "https://www.instagram.com/reel/DKz3nEjupNb/"},
        {"foto": "/ig_post3.png", "url": "https://www.instagram.com/reel/DTqbo7YkRCL/"},
        {"foto": "/ig_post4.png", "url": "https://www.instagram.com/reel/DOEqBx2jqZO/"},
        {"foto": "/ig_post5.png", "url": "https://www.instagram.com/reel/DA3tW1BRN3n/"},
        {"foto": "/ig_post6.png", "url": "https://www.instagram.com/reel/C8azdQ1Nre9/"},
        {"foto": "/ig_post7.png", "url": "https://www.instagram.com/reel/DLnK6ZNuzbK/"},
        {"foto": "/ig_post8.png", "url": "https://www.instagram.com/p/DJpFV9FNlJI/"},
        {"foto": "/ig_post9.png", "url": "https://www.instagram.com/reel/DNbpD5-ulhq/"},
    ]

    testimonios: list[dict[str, str]] = [
        {
            "texto": '"Después de vivir la experiencia de la Tribu Sonora Consciente, puedo decir que es una vivencia transformadora y sensorial. Los implementos utilizados y el cuidado en cada detalle crean un espacio de profunda relajación y sanación."',
            "autor": "Mariana Kert", "ciudad": "Margarita, Venezuela"
        },
        {
            "texto": '"Verlos trabajar fue para mí un gran regalo para mi alma y mi espíritu. Su entrega, su conexión y su profesionalidad fueron para nuestro encuentro la cereza del pastel."',
            "autor": "Maria Luisa", "ciudad": "Caracas, Venezuela"
        },
        {
            "texto": '"Fue mi primera vez en una terapia de sonido y logré dar un paso importante. El trabajo con el sonido y la música facilita mucho la meditación."',
            "autor": "Maximiliano Catoni", "ciudad": "Caracas, Venezuela"
        }
    ]

    # ==================================================================
    # VARIABLES REACTIVAS Y NAVEGACIÓN DE LA TIENDA
    # ==================================================================
    productos_tribu: list[dict[str, Any]] = []
    servicios_tribu: list[dict[str, Any]] = []
    talleres_tribu: list[dict[str, Any]] = []
    sesiones_tribu: list[dict[str, Any]] = []

    # 🔍 BÚSQUEDA GLOBAL OMNICANAL EN EL NAVBAR
    modal_busqueda_global_abierto: bool = False
    busqueda_global_query: str = ""

    def set_modal_busqueda_global_abierto(self, val: bool):
        self.modal_busqueda_global_abierto = val

    def abrir_modal_busqueda_global(self):
        self.busqueda_global_query = ""
        self.modal_busqueda_global_abierto = True

    def cerrar_modal_busqueda_global(self):
        self.modal_busqueda_global_abierto = False

    def set_busqueda_global_query(self, val: str):
        self.busqueda_global_query = val

    @rx.var
    def busqueda_resultados_productos(self) -> list[dict[str, Any]]:
        q = self.busqueda_global_query.strip().lower()
        if not q:
            return []
        res = []
        for p in self.productos_tribu:
            if not p.get("is_active"):
                continue
            nombre = p.get("nombre", "").lower()
            cat = p.get("categoria", "").lower()
            desc = p.get("descripcion", "").lower()
            intenc = p.get("intencion", "").lower()
            prov = p.get("proveedor", "").lower()
            if q in nombre or q in cat or q in desc or q in intenc or q in prov:
                res.append(p)
        return res[:5]

    @rx.var
    def busqueda_resultados_talleres(self) -> list[dict[str, Any]]:
        q = self.busqueda_global_query.strip().lower()
        if not q:
            return []
        res = []
        for w in self.talleres_tribu:
            titulo = w.get("titulo", "").lower()
            desc = w.get("descripcion", "").lower()
            fac = w.get("facilitador", "").lower()
            ubi = w.get("ubicacion", "").lower()
            tipo = w.get("tipo", "").lower()
            if q in titulo or q in desc or q in fac or q in ubi or q in tipo:
                res.append(w)
        return res[:5]

    @rx.var
    def busqueda_resultados_sesiones(self) -> list[dict[str, Any]]:
        q = self.busqueda_global_query.strip().lower()
        if not q:
            return []
        res = []
        for s in self.sesiones_tribu:
            nom = s.get("nombre", "").lower()
            ubi = s.get("ubicacion", "").lower()
            frec = s.get("frecuencia_texto", "").lower()
            if q in nom or q in ubi or q in frec:
                res.append(s)
        return res[:5]

    @rx.var
    def busqueda_resultados_servicios(self) -> list[dict[str, Any]]:
        q = self.busqueda_global_query.strip().lower()
        if not q:
            return []
        res = []
        for s in self.servicios_tribu:
            nom = s.get("nombre", "").lower()
            desc = s.get("descripcion", "").lower()
            if q in nom or q in desc:
                res.append(s)
        return res[:5]

    @rx.var
    def total_resultados_busqueda_global(self) -> int:
        return (
            len(self.busqueda_resultados_productos)
            + len(self.busqueda_resultados_talleres)
            + len(self.busqueda_resultados_sesiones)
            + len(self.busqueda_resultados_servicios)
        )

    def seleccionar_resultado_busqueda(self, target_url: str):
        self.modal_busqueda_global_abierto = False
        self.busqueda_global_query = ""
        return rx.redirect(target_url)

    # 🔍 BÚSQUEDA Y FILTRADO DE PRODUCTOS EN ADMIN
    busqueda_producto_admin: str = ""

    def set_busqueda_producto_admin(self, val: str):
        self.busqueda_producto_admin = val

    @rx.var
    def productos_admin_filtrados(self) -> list[dict[str, Any]]:
        q = self.busqueda_producto_admin.strip().lower()
        if not q:
            return self.productos_tribu
        return [
            p for p in self.productos_tribu
            if q in p.get("nombre", "").lower() or q in p.get("categoria", "").lower() or q in p.get("proveedor", "").lower()
        ]

    def validar_email_formato(self, email: str) -> bool:
        """Valida que el correo tenga una estructura nombre@dominio.extensión."""
        import re
        patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return bool(re.match(patron, email.strip()))

    def formatear_whatsapp_numero(self, numero_raw: str, codigo_pais_defecto: str = "58") -> str:
        """Remueve ceros iniciales y garantiza el código de país (ej. 04243440461 -> 584243440461)."""
        solo_numeros = "".join(filter(str.isdigit, str(numero_raw)))
        if not solo_numeros:
            return ""
        # Si empieza con cero local (ej: 0424...), eliminar el cero inicial
        solo_numeros = solo_numeros.removeprefix("0")
        # Si no incluye el código de país (ej: longitud local de 10 dígitos), anteponerlo
        if len(solo_numeros) == 10:
            solo_numeros = f"{codigo_pais_defecto}{solo_numeros}"
        return solo_numeros

    def contactar_soporte_whatsapp(self):
        """Redirige al WhatsApp oficial con un mensaje en texto plano (sin iconos ni emojis)."""
        import urllib.parse
        num_wa = "584241359530"
        mensaje = "Hola Tribu Sonora Consciente. Necesito asistencia o soporte tecnico con mi cuenta."
        encoded = urllib.parse.quote(mensaje)
        return rx.redirect(f"https://wa.me/{num_wa}?text={encoded}", is_external=True)

    # Variables para el Modal de Reserva de Sesiones y Lightbox Galería
    modal_reserva_sesion_abierto: bool = False
    modal_lightbox_abierto: bool = False
    fotos_lightbox: list[str] = []
    indice_foto_lightbox: int = 0

    @rx.var
    def foto_lightbox_actual(self) -> str:
        """Devuelve la foto seleccionada actualmente en el visor flotante."""
        if self.fotos_lightbox and 0 <= self.indice_foto_lightbox < len(self.fotos_lightbox):
            return self.fotos_lightbox[self.indice_foto_lightbox]
        return ""

    def abrir_lightbox_galeria(self, lista_fotos: list, foto_inicial: str = ""):
        """Abre la galería acumulando todas las fotos disponibles o la foto de portada."""
        if isinstance(lista_fotos, list) and len(lista_fotos) > 0:
            self.fotos_lightbox = [f for f in lista_fotos if isinstance(f, str) and f.strip()]
        else:
            self.fotos_lightbox = [foto_inicial] if foto_inicial else []
        
        self.indice_foto_lightbox = 0
        self.modal_lightbox_abierto = True

    def cerrar_lightbox(self):
        self.modal_lightbox_abierto = False
        self.fotos_lightbox = []
        self.indice_foto_lightbox = 0

    def foto_siguiente_lightbox(self):
        if self.fotos_lightbox:
            self.indice_foto_lightbox = (self.indice_foto_lightbox + 1) % len(self.fotos_lightbox)

    def foto_anterior_lightbox(self):
        if self.fotos_lightbox:
            self.indice_foto_lightbox = (self.indice_foto_lightbox - 1 + len(self.fotos_lightbox)) % len(self.fotos_lightbox)
    sesion_seleccionada_reserva: dict[str, Any] = {}
    reserva_nombre_cliente: str = ""
    reserva_email_cliente: str = ""
    reserva_whatsapp_cliente: str = ""
    reserva_cantidad_cupos: int = 1
    reserva_participantes: list[str] = [""]
    reserva_porcentaje_pago: float = 0.0
    reserva_cupon_input: str = ""
    reserva_descuento_monto: float = 0.0
    reserva_cupon_aplicado_codigo: str = ""

    def set_reserva_porcentaje_pago(self, pct: float):
        val = float(pct)
        if self.reserva_porcentaje_pago == val:
            self.reserva_porcentaje_pago = 0.0
        else:
            self.reserva_porcentaje_pago = val

    def set_reserva_cupon_input(self, val: str):
        self.reserva_cupon_input = val

    @rx.var
    def reserva_monto_subtotal_calculado(self) -> float:
        inv = float(self.sesion_seleccionada_reserva.get("inversion", 0.0))
        return round(inv * self.reserva_cantidad_cupos, 2)

    @rx.var
    def reserva_monto_total_calculado(self) -> float:
        subtotal = self.reserva_monto_subtotal_calculado
        monto_final = max(0.0, subtotal - self.reserva_descuento_monto)
        return round(monto_final, 2)

    def aplicar_cupon_reserva(self):
        """Valida y aplica cupones porcentuales o montos fijos negociados."""
        cupon_clean = self.reserva_cupon_input.strip().upper()
        if not cupon_clean:
            self.reserva_descuento_monto = 0.0
            self.reserva_cupon_aplicado_codigo = ""
            return rx.toast.info("Cupón removido.")

        subtotal = self.reserva_monto_subtotal_calculado

        try:
            with rx.session() as session:
                db_cupon = session.exec(
                    sqlmodel.select(TribuCoupon).where(
                        TribuCoupon.codigo == cupon_clean,
                        TribuCoupon.is_active == True
                    )
                ).first()

                if db_cupon:
                    if db_cupon.usos_actuales >= db_cupon.usos_maximos:
                        return rx.toast.error("Este cupón ha alcanzado el límite de usos.")
                    
                    if db_cupon.tipo == "PORCENTAJE":
                        desc = round(subtotal * (db_cupon.valor / 100.0), 2)
                        msg = f"¡Cupón de {db_cupon.valor:.0f}% aplicado (-${desc:.2f} USD)!"
                    else:
                        desc = min(subtotal, float(db_cupon.valor))
                        msg = f"¡Cupón de descuento aplicado (-${desc:.2f} USD)!"

                    self.reserva_descuento_monto = desc
                    self.reserva_cupon_aplicado_codigo = db_cupon.codigo
                    return rx.toast.success(msg)

                # Fallback para Vouchers/GiftCards
                gc = session.exec(
                    sqlmodel.select(TribuGiftCard).where(
                        TribuGiftCard.codigo == cupon_clean,
                        TribuGiftCard.estado == "ACTIVA"
                    )
                ).first()

                if gc:
                    desc = min(subtotal, float(gc.monto_equivalente))
                    self.reserva_descuento_monto = desc
                    self.reserva_cupon_aplicado_codigo = gc.codigo
                    return rx.toast.success(f"¡Voucher '{gc.experiencia_nombre}' aplicado (-${desc:.2f} USD)!")

                self.reserva_descuento_monto = 0.0
                self.reserva_cupon_aplicado_codigo = ""
                return rx.toast.error("Código de cupón o descuento inválido.")
        except Exception as e:
            print(f"Error al aplicar cupón: {e}")
            return rx.toast.error("Error al verificar el cupón.")

    @rx.var
    def reserva_monto_pagado_calculado(self) -> float:
        total = self.reserva_monto_total_calculado
        return round(total * (self.reserva_porcentaje_pago / 100.0), 2)

    @rx.var
    def reserva_monto_pendiente_calculado(self) -> float:
        total = self.reserva_monto_total_calculado
        pagado = self.reserva_monto_pagado_calculado
        return round(total - pagado, 2)

    def set_reserva_email(self, val: str):
        self.reserva_email_cliente = val

    def set_reserva_whatsapp(self, val: str):
        self.reserva_whatsapp_cliente = val

    def set_reserva_nombre(self, val: str):
        self.reserva_nombre_cliente = val

    def actualizar_nombre_participante(self, idx: int, val: str):
        nuevos = list(self.reserva_participantes)
        if 0 <= idx < len(nuevos):
            nuevos[idx] = val
            self.reserva_participantes = nuevos
            if idx == 0:
                self.reserva_nombre_cliente = val

    # Variables para el Documento / Checklist Digital de Asistencia por Token
    sesion_asistencia_info: dict[str, Any] = {}
    lista_asistentes_sesion: list[dict[str, Any]] = []
    cargando_asistencia: bool = True
    busqueda_asistente: str = ""
    fechas_historicas_sesion: list[str] = []
    fecha_asistencia_seleccionada: str = ""

    def set_fecha_asistencia_seleccionada(self, fecha: str):
        self.fecha_asistencia_seleccionada = fecha
        self.cargar_lista_asistencia_por_token()

    def seleccionar_metodo_pago_asistencia(self, item_id: str, metodo: str):
        """Asigna o conmuta el método de pago seleccionado directamente en la lista de asistentes."""
        for a in self.lista_asistentes_sesion:
            if a["id"] == item_id:
                actual = a.get("metodo_pago", "")
                a["metodo_pago"] = "" if actual == metodo else metodo
                break

    def set_busqueda_asistente(self, val: str):
        self.busqueda_asistente = val

    @rx.var
    def lista_asistentes_filtrada(self) -> list[dict[str, Any]]:
        q = self.busqueda_asistente.strip().lower()
        if not q:
            return self.lista_asistentes_sesion
        return [
            a for a in self.lista_asistentes_sesion
            if q in a.get("nombre_cliente", "").lower() or q in a.get("whatsapp_cliente", "").lower()
        ]

    @rx.var
    def total_presentes_asistencia(self) -> int:
        return sum(a.get("cupos", 1) for a in self.lista_asistentes_sesion if a.get("asistio"))

    @rx.var
    def total_cupos_reservados_asistencia(self) -> int:
        return sum(a.get("cupos", 1) for a in self.lista_asistentes_sesion)
    
    # 🎛️ FILTROS Y NAVEGACIÓN DE CALENDARIO PARA TALLERES (SEMANA Y MES)
    filtro_vista_talleres: str = "Week"  # "Week" o "Month"
    filtro_facilitador: str = "FACILITADOR"
    filtro_ubicacion: str = "UBICACIÓN"
    filtro_etiqueta: str = "CATEGORÍA"
    filtro_solo_hoy: bool = False
    fecha_filtro_seleccionada: str = ""
    mes_filtro_seleccionado: str = ""
    semana_offset: int = 0
    anio_offset: int = 0

    def set_filtro_vista_talleres(self, vista: str):
        self.filtro_vista_talleres = vista
        if vista == "Week":
            self.mes_filtro_seleccionado = ""
        else:
            self.fecha_filtro_seleccionada = ""

    def semana_anterior(self):
        self.semana_offset -= 1

    def semana_siguiente(self):
        self.semana_offset += 1

    def anio_anterior(self):
        self.anio_offset -= 1

    def anio_siguiente(self):
        self.anio_offset += 1

    def set_filtro_facilitador(self, val: str):
        self.filtro_facilitador = val

    def set_filtro_ubicacion(self, val: str):
        self.filtro_ubicacion = val

    def set_filtro_etiqueta(self, val: str):
        self.filtro_etiqueta = val

    def filtrar_hoy(self):
        self.filtro_solo_hoy = not self.filtro_solo_hoy
        self.fecha_filtro_seleccionada = ""
        self.mes_filtro_seleccionado = ""

    def seleccionar_fecha_calendario(self, fecha_str: str):
        if self.fecha_filtro_seleccionada == fecha_str:
            self.fecha_filtro_seleccionada = ""
        else:
            self.fecha_filtro_seleccionada = fecha_str
            self.filtro_solo_hoy = False

    def seleccionar_mes_calendario(self, fecha_mes_str: str):
        if self.mes_filtro_seleccionado == fecha_mes_str:
            self.mes_filtro_seleccionado = ""
        else:
            self.mes_filtro_seleccionado = fecha_mes_str
            self.filtro_solo_hoy = False

    def limpiar_filtros_talleres(self):
        """Restablece los filtros al estado predeterminado MOSTRAR TODO."""
        self.filtro_facilitador = "FACILITADOR"
        self.filtro_ubicacion = "UBICACIÓN"
        self.filtro_etiqueta = "CATEGORÍA"
        self.filtro_solo_hoy = False
        self.fecha_filtro_seleccionada = ""
        self.mes_filtro_seleccionado = ""
        self.semana_offset = 0
        self.anio_offset = 0

    @rx.var
    def opciones_facilitadores(self) -> list[str]:
        facs = {t.get("facilitador") for t in self.talleres_tribu if t.get("facilitador")}
        return ["FACILITADOR"] + sorted(facs)

    @rx.var
    def opciones_ubicaciones(self) -> list[str]:
        ubis = {t.get("ubicacion") for t in self.talleres_tribu if t.get("ubicacion")}
        return ["UBICACIÓN"] + sorted(ubis)

    @rx.var
    def opciones_etiquetas(self) -> list[str]:
        etqs = {t.get("tipo") for t in self.talleres_tribu if t.get("tipo")}
        return ["CATEGORÍA"] + sorted(etqs)

    @rx.var
    def dias_semana_actual(self) -> list[dict[str, Any]]:
        from datetime import date, timedelta
        hoy = date.today()
        base_date = hoy + timedelta(weeks=self.semana_offset)
        idx_domingo = (base_date.weekday() + 1) % 7
        inicio_semana = base_date - timedelta(days=idx_domingo)
        
        dias_nombres = ["DOM", "LUN", "MAR", "MIÉ", "JUE", "VIE", "SÁB"]
        fechas_eventos = {str(t.get("fecha_evento")) for t in self.talleres_tribu if t.get("fecha_evento")}
        
        resultado = []
        for i in range(7):
            d = inicio_semana + timedelta(days=i)
            d_str = str(d)
            resultado.append({
                "dia_nombre": dias_nombres[i],
                "dia_num": str(d.day),
                "fecha": d_str,
                "es_hoy": (d == hoy),
                "tiene_eventos": (d_str in fechas_eventos)
            })
        return resultado

    @rx.var
    def meses_anio_actual(self) -> list[dict[str, Any]]:
        from datetime import date
        hoy = date.today()
        anio_base = hoy.year + self.anio_offset
        
        meses_nombres = ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"]
        fechas_meses_eventos = {str(t.get("fecha_evento"))[:7] for t in self.talleres_tribu if t.get("fecha_evento")}
        
        resultado = []
        for m_idx in range(1, 13):
            m_str = f"{m_idx:02d}"
            fecha_mes_key = f"{anio_base}-{m_str}"
            resultado.append({
                "mes_nombre": meses_nombres[m_idx - 1],
                "mes_num": m_str,
                "anio": str(anio_base),
                "fecha_mes": fecha_mes_key,
                "es_mes_actual": (hoy.year == anio_base and hoy.month == m_idx),
                "tiene_eventos": (fecha_mes_key in fechas_meses_eventos)
            })
        return resultado

    @rx.var
    def talleres_filtrados(self) -> list[dict[str, Any]]:
        from datetime import date
        hoy_str = str(date.today())
        
        resultado = []
        for t in self.talleres_tribu:
            if self.filtro_facilitador != "FACILITADOR" and t.get("facilitador") != self.filtro_facilitador:
                continue
            if self.filtro_ubicacion != "UBICACIÓN" and t.get("ubicacion") != self.filtro_ubicacion:
                continue
            if self.filtro_etiqueta != "CATEGORÍA" and t.get("tipo") != self.filtro_etiqueta:
                continue
            if self.filtro_solo_hoy and t.get("fecha_evento") != hoy_str:
                continue
            if self.fecha_filtro_seleccionada and t.get("fecha_evento") != self.fecha_filtro_seleccionada:
                continue
            if self.mes_filtro_seleccionado and not str(t.get("fecha_evento")).startswith(self.mes_filtro_seleccionado):
                continue

            resultado.append(t)
        return resultado

    def ir_a_biografia_facilitador(self, nombre_facilitador: str):
        nombre_clean = nombre_facilitador.strip().upper()
        guia_encontrado = next((g for g in self.guias_tribu if g["nombre"].upper() in nombre_clean or nombre_clean in g["nombre"].upper()), None)
        if guia_encontrado:
            return rx.redirect(f"/biografia/{guia_encontrado['id']}")
        return rx.redirect("/acerca-de")

    def agendar_taller(self, taller: dict):
        import urllib.parse
        num_raw = taller.get("whatsapp_contacto") or "584241359530"
        num_clean = "".join(filter(str.isdigit, str(num_raw))) or "584241359530"
        
        titulo = taller.get("titulo", "")
        mensaje = f"¡Hola Tribu Sonora! Me interesa reservar un cupo para: *{titulo}*"
        encoded = urllib.parse.quote(mensaje)
        return rx.redirect(f"https://wa.me/{num_clean}?text={encoded}", is_external=True)
    vista_shop: str = "revista"
    categoria_seleccionada: str = ""
    intencion_seleccionada: str = ""

    # 📱 CONTROL MÓVIL
    show_filtros_mobile: bool = False

    def toggle_filtros_mobile(self):
        self.show_filtros_mobile = not self.show_filtros_mobile

    # 🛍️ FILTROS Y ORDENAMIENTO PARA "VER TODO" (EXPLORAR TODOS LOS PRODUCTOS)
    filtro_precio_min: str = ""
    filtro_precio_max: str = ""
    filtro_categorias_ver_todo: list[str] = []
    filtro_intenciones_ver_todo: list[str] = []
    filtro_ordenamiento: str = "Nombre: AZ"

    def set_filtro_precio_min(self, val: str):
        self.filtro_precio_min = val

    def set_filtro_precio_max(self, val: str):
        self.filtro_precio_max = val

    def set_filtro_ordenamiento(self, val: str):
        self.filtro_ordenamiento = val

    def toggle_filtro_categoria_ver_todo(self, cat_nombre: str):
        nuevas = list(self.filtro_categorias_ver_todo)
        if cat_nombre in nuevas:
            nuevas.remove(cat_nombre)
        else:
            nuevas.append(cat_nombre)
        self.filtro_categorias_ver_todo = nuevas

    def toggle_filtro_intencion_ver_todo(self, intencion_nombre: str):
        nuevas = list(self.filtro_intenciones_ver_todo)
        if intencion_nombre in nuevas:
            nuevas.remove(intencion_nombre)
        else:
            nuevas.append(intencion_nombre)
        self.filtro_intenciones_ver_todo = nuevas

    def limpiar_filtros_ver_todo(self):
        self.filtro_precio_min = ""
        self.filtro_precio_max = ""
        self.filtro_categorias_ver_todo = []
        self.filtro_intenciones_ver_todo = []
        self.filtro_ordenamiento = "Nombre: AZ"
        return rx.toast.info("Se han restablecido todos los filtros.")

    def navegar_vista_ver_todo(self):
        self.vista_shop = "ver_todo"
        self.show_menu_shop = False
        return rx.redirect("/shop")

    @rx.var
    def productos_ver_todo_filtrados(self) -> list[dict[str, Any]]:
        res = [p for p in self.productos_tribu if p.get("is_active")]

        # 1. Filtro por Precio Mínimo
        if self.filtro_precio_min.strip():
            try:
                p_min = float(self.filtro_precio_min.strip())
                res = [p for p in res if float(p.get("precio", 0.0)) >= p_min]
            except ValueError:
                pass

        # 2. Filtro por Precio Máximo
        if self.filtro_precio_max.strip():
            try:
                p_max = float(self.filtro_precio_max.strip())
                res = [p for p in res if float(p.get("precio", 0.0)) <= p_max]
            except ValueError:
                pass

        # 3. Filtro por Categorías
        if self.filtro_categorias_ver_todo:
            cats_lower = [c.lower() for c in self.filtro_categorias_ver_todo]
            res = [p for p in res if p.get("categoria", "").lower() in cats_lower]

        # 4. Filtro por Intenciones
        if self.filtro_intenciones_ver_todo:
            ints_lower = [i.lower() for i in self.filtro_intenciones_ver_todo]
            res = [p for p in res if p.get("intencion", "").lower() in ints_lower]

        # 5. Ordenamiento
        if self.filtro_ordenamiento == "Nombre: AZ":
            res.sort(key=lambda x: str(x.get("nombre", "")).lower())
        elif self.filtro_ordenamiento == "Nombre: ZA":
            res.sort(key=lambda x: str(x.get("nombre", "")).lower(), reverse=True)
        elif self.filtro_ordenamiento == "Precio: Menor a Mayor":
            res.sort(key=lambda x: float(x.get("precio", 0.0)))
        elif self.filtro_ordenamiento == "Precio: Mayor a Menor":
            res.sort(key=lambda x: float(x.get("precio", 0.0)), reverse=True)

        return res

    @rx.var
    def total_productos_ver_todo_count(self) -> int:
        return len(self.productos_ver_todo_filtrados)

    @rx.var
    def shop_mas_vendidos_revista(self) -> list[dict[str, Any]]:
        return [p for p in self.productos_tribu if p.get("is_best_seller") and p.get("is_active")][:4]

    @rx.var
    def shop_favoritos_revista(self) -> list[dict[str, Any]]:
        return [p for p in self.productos_tribu if p.get("is_favorite") and p.get("is_active")][:4]

    @rx.var
    def todos_los_mas_vendidos(self) -> list[dict[str, Any]]:
        return [p for p in self.productos_tribu if p.get("is_best_seller") and p.get("is_active")]

    @rx.var
    def todos_los_favoritos(self) -> list[dict[str, Any]]:
        return [p for p in self.productos_tribu if p.get("is_favorite") and p.get("is_active")]

    @rx.var
    def productos_por_categoria_limpia(self) -> list[dict[str, Any]]:
        return [p for p in self.productos_tribu if p.get("categoria").lower() == self.categoria_seleccionada.lower() and p.get("is_active")]

    @rx.var
    def productos_por_intencion_limpia(self) -> list[dict[str, Any]]:
        return [p for p in self.productos_tribu if p.get("intencion") and p.get("intencion").lower() == self.intencion_seleccionada.lower() and p.get("is_active")]
    
    @rx.var
    def categorias_unicas_carrusel(self) -> list[dict[str, str]]:
        vistas = {}
        for p in self.productos_tribu:
            if p.get("is_active"):
                cat = p.get("categoria")
                if cat and cat not in vistas and p.get("foto_principal"):
                    vistas[cat] = p.get("foto_principal")
        return [{"name": name, "img": img} for name, img in vistas.items()]
    
    @rx.var
    def lista_categorias_unicas(self) -> list[str]:
        cats = {p.get("categoria") for p in self.productos_tribu if p.get("categoria")}
        return sorted(cats)

    @rx.var
    def lista_proveedores_unicos(self) -> list[str]:
        provs = {p.get("proveedor") for p in self.productos_tribu if p.get("proveedor")}
        return sorted(provs)
    
    def navegar_revista_principal(self):
        self.vista_shop = "revista"
        self.show_menu_shop = False
        return rx.redirect("/shop")

    def navegar_vista_mas_vendidos(self):
        self.vista_shop = "ver_mas_vendidos"
        self.show_menu_shop = False
        return rx.redirect("/shop")

    def navegar_vista_favoritos(self):
        self.vista_shop = "ver_favoritos"
        self.show_menu_shop = False
        return rx.redirect("/shop")

    def navegar_vista_categoria(self, nombre_cat: str):
        self.categoria_seleccionada = nombre_cat
        self.vista_shop = "ver_categoria"
        self.show_menu_shop = False
        return rx.redirect("/shop")

    def navegar_vista_intencion(self, intencion_nombre: str):
        self.intencion_seleccionada = intencion_nombre
        self.vista_shop = "ver_intencion"
        self.show_menu_shop = False
        return rx.redirect("/shop")
    
    # ==================================================================
    # 2. PRIVACIDAD, COOKIES, NEWSLETTER Y MENÚS DESPLEGABLES
    # ==================================================================
    email_newsletter: str = ""
    show_cookie_modal: bool = False
    cookies_personalizacion: bool = True
    cookies_marketing: bool = True
    cookies_analitica: bool = True

    show_menu_acerca_de: bool = False
    show_menu_sesiones: bool = False
    show_menu_shop: bool = False

    show_sub_intencion: bool = False
    show_sub_categoria: bool = False

    def asignar_email(self, nuevo_texto: str):
        self.email_newsletter = nuevo_texto

    def registrar_suscripcion(self):
        if self.email_newsletter.strip() != "":
            self.email_newsletter = ""
            return rx.toast.success("¡Gracias por unirte a nuestro tejido conectado!")

    def asignar_personalizacion(self, valor: bool):
        self.cookies_personalizacion = valor

    def asignar_marketing(self, valor: bool):
        self.cookies_marketing = valor

    def asignar_analitica(self, valor: bool):
        self.cookies_analitica = valor

    def abrir_cookies(self):
        self.show_cookie_modal = True

    def cerrar_cookies(self):
        self.show_cookie_modal = False

    def aceptar_todo_cookies(self):
        self.cookies_personalizacion = True
        self.cookies_marketing = True
        self.cookies_analitica = True
        self.show_cookie_modal = False
        return rx.toast.success("Se han aceptado todas las cookies de optimización.")

    def rechazar_todo_cookies(self):
        self.cookies_personalizacion = False
        self.cookies_marketing = False
        self.cookies_analitica = False
        self.show_cookie_modal = False
        return rx.toast.info("Se han rechazado las cookies opcionales.")

    def guardar_seleccion_cookies(self):
        self.show_cookie_modal = False
        return rx.toast.success("Preferencias de privacidad guardadas exitosamente.")

    def toggle_menu_acerca_de(self):
        self.show_menu_acerca_de = not self.show_menu_acerca_de
        if self.show_menu_acerca_de:
            self.show_menu_sesiones = False
            self.show_menu_shop = False

    def cerrar_menu_acerca_de(self):
        self.show_menu_acerca_de = False

    def toggle_menu_sesiones(self):
        self.show_menu_sesiones = not self.show_menu_sesiones
        if self.show_menu_sesiones:
            self.show_menu_acerca_de = False
            self.show_menu_shop = False

    def cerrar_menu_sesiones(self):
        self.show_menu_sesiones = False

    def toggle_menu_shop(self):
        self.show_menu_shop = not self.show_menu_shop
        if self.show_menu_shop:
            self.show_menu_acerca_de = False
            self.show_menu_sesiones = False
            self.show_sub_intencion = False
            self.show_sub_categoria = False

    def cerrar_menu_shop(self):
        self.show_menu_shop = False
        self.show_sub_intencion = False
        self.show_sub_categoria = False

    def toggle_sub_intencion(self):
        self.show_sub_intencion = not self.show_sub_intencion

    def toggle_sub_categoria(self):
        self.show_sub_categoria = not self.show_sub_categoria

    # ==================================================================
    # 3. VARIABLES Y MÉTODOS DEL FORMULARIO DE CONTACTO
    # ==================================================================
    nombre: str = ""
    correo: str = ""
    telefono: str = ""
    comentario: str = ""
    
    def asignar_nombre(self, valor: str):
        self.nombre = valor

    def asignar_correo(self, valor: str):
        self.correo = valor

    def asignar_telefono(self, valor: str):
        self.telefono = valor

    def asignar_comentario(self, valor: str):
        self.comentario = valor

    def enviar_formulario(self):
        if self.nombre.strip() == "" or self.correo.strip() == "":
            return rx.toast.error("Por favor, completa los campos requeridos (*)")
        self.nombre = ""
        self.correo = ""
        self.telefono = ""
        self.comentario = ""
        return rx.toast.success("¡Mensaje enviado con éxito! Nos comunicaremos pronto.")

    # ==================================================================
    # 4. HIDRATACIÓN DINÁMICA DESDE SUPABASE (DATA FETCHING)
    # ==================================================================
    def cargar_datos_db(self):
        with rx.session() as session:
            db_guides = session.exec(sqlmodel.select(TribuGuide)).all()
            if db_guides:
                self.guias_tribu = [
                    {
                        "id": str(g.id), 
                        "nombre": g.nombre, 
                        "foto": g.foto, 
                        "descripcion": g.descripcion, 
                        "biografia": g.biografia
                    } 
                    for g in db_guides
                ]

            db_posts = session.exec(sqlmodel.select(InstagramPost)).all()
            if db_posts:
                self.feed_instagram = [{"foto": post.foto, "url": post.url} for post in db_posts]
            
            db_events = session.exec(sqlmodel.select(FeaturedEvent)).all()
            if db_events:
                self.eventos_destacados = [
                    {"nombre": event.nombre, "logo": event.logo, "url": event.url} 
                    for event in db_events
                ]

            db_products = session.exec(sqlmodel.select(TribuProduct)).all()
            if db_products:
                self.productos_tribu = [
                    {
                      "id": p.id,
                      "nombre": p.nombre,
                      "descripcion": p.descripcion,
                      "precio": float(p.precio),
                      "stock": int(p.stock),
                      "is_best_seller": p.is_best_seller,
                      "is_favorite": p.is_favorite,
                      "categoria": p.categoria,
                      "proveedor": p.proveedor or "",
                      "intencion": p.intencion or "",
                      "foto_principal": p.fotos[0] if p.fotos and len(p.fotos) > 0 else "",
                      "fotos": p.fotos,
                      "is_active": p.is_active
                    }
                    for p in db_products
                ]

                db_services = session.exec(sqlmodel.select(TribuService).where(TribuService.is_active == True).order_by(TribuService.id)).all()
            if db_services:
                self.servicios_tribu = [
                    {
                        "id": s.id,
                        "nombre": s.nombre,
                        "foto": s.foto,
                        "descripcion": s.descripcion,
                        "is_active": s.is_active
                    }
                    for s in db_services
                ]

                db_workshops = session.exec(sqlmodel.select(TribuWorkshop).where(TribuWorkshop.is_active == True).order_by(TribuWorkshop.fecha_evento)).all()
            if db_workshops:
                self.talleres_tribu = [
                    {
                        "id": w.id,
                        "titulo": w.titulo,
                        "tipo": w.tipo,
                        "foto": w.foto,
                        "facilitador": w.facilitador,
                        "descripcion": w.descripcion,
                        "fecha_texto": w.fecha_texto,
                        "hora_texto": w.hora_texto,
                        "duracion_texto": w.duracion_texto,
                        "ubicacion": w.ubicacion,
                        "precio": float(w.precio),
                        "moneda": w.moneda,
                        "fecha_evento": str(w.fecha_evento),
                        "whatsapp_contacto": w.whatsapp_contacto or ""
                    }
                    for w in db_workshops
                ]

            from datetime import date
            db_sessions = session.exec(sqlmodel.select(TribuSession).where(TribuSession.is_active == True)).all()
            if db_sessions:
                hoy = date.today()
                actualizo = False
                for s in db_sessions:
                    if s.patron_recurrencia and s.patron_recurrencia != "MANUAL":
                        expirado = False
                        if not s.fecha_evento:
                            expirado = True
                        else:
                            try:
                                if date.fromisoformat(s.fecha_evento) < hoy:
                                    expirado = True
                            except ValueError:
                                expirado = True

                        if expirado:
                            proxima_f = self.calcular_proxima_fecha_recurrente(s.patron_recurrencia, hoy)
                            if proxima_f:
                                s.fecha_evento = str(proxima_f)
                                s.fecha_texto = proxima_f.strftime("%d/%m/%Y")
                                s.plazas_disponibles = s.plazas_totales
                                session.add(s)
                                actualizo = True

                if actualizo:
                    session.commit()

                # 🔄 ORDENAMIENTO DE PRIORIDAD POR FECHA MÁS CERCANA
                db_sessions.sort(key=lambda x: x.fecha_evento or "9999-12-31")

                self.sesiones_tribu = [
                    {
                        "id": s.id,
                        "nombre": s.nombre,
                        "foto": s.foto,
                        "fotos": s.fotos or [],
                        "ubicacion": s.ubicacion,
                        "frecuencia_texto": s.frecuencia_texto,
                        "fecha_texto": s.fecha_texto,
                        "hora_texto": s.hora_texto,
                        "hora_recepcion_texto": s.hora_recepcion_texto or "",
                        "inversion": float(s.inversion),
                        "plazas_totales": s.plazas_totales,
                        "plazas_disponibles": s.plazas_disponibles,
                        "instagram_url": s.instagram_url,
                        "recomendaciones": s.recomendaciones,
                        "checkin_token": s.checkin_token or "",
                        "patron_recurrencia": s.patron_recurrencia or "MANUAL",
                        "fecha_evento": s.fecha_evento or ""
                    }
                    for s in db_sessions
                ]

    def cargar_detalle_guia(self):
        guide_id = self.router.page.params.get("id")
        if guide_id:
            try:
                guide_id_int = int(guide_id)
                with rx.session() as session:
                    guide = session.get(TribuGuide, guide_id_int)
                    if guide:
                        self.selected_guide = {
                            "nombre": guide.nombre,
                            "foto": guide.foto,
                            "descripcion": guide.descripcion,
                            "biografia": guide.biografia
                        }
                    else:
                        fallback = next((g for g in self.guias_tribu if g["id"] == str(guide_id)), None)
                        if fallback:
                            self.selected_guide = fallback
            except Exception as e:
                print(f"Error cargando biografía: {e}")

    # ==================================================================
    # 5. LÓGICA DE PÁGINA DE DETALLE DE PRODUCTO (/product/[id])
    # ==================================================================
    producto_detalle: dict = {}
    fotos_producto: list[str] = []
    foto_principal: str = ""
    cantidad_producto: int = 1
    productos_recomendados: list[dict] = []
    
    variantes_producto: list[dict] = []
    variante_seleccionada: dict = {}

    def seleccionar_foto_principal(self, url: str):
        self.foto_principal = url

    def seleccionar_variante(self, variante: dict):
        if variante.get("stock", 0) <= 0:
            return rx.toast.info("Esta variante se encuentra agotada actualmente.")

        self.variante_seleccionada = variante
        self.cantidad_producto = 1

        if variante.get("foto"):
            self.foto_principal = variante.get("foto")

    def incrementar_cantidad(self):
        stock_max = self.variante_seleccionada.get("stock") if self.variante_seleccionada else self.producto_detalle.get("stock", 1)
        if self.cantidad_producto < stock_max:
            self.cantidad_producto += 1

    def decrementar_cantidad(self):
        if self.cantidad_producto > 1:
            self.cantidad_producto -= 1

    def cargar_producto_por_id(self):
        prod_id = self.router.page.params.get("id")
        if not prod_id:
            return
            
        try:
            self.cantidad_producto = 1
            prod_id_int = int(prod_id)
            
            with rx.session() as session:
                product = session.get(TribuProduct, prod_id_int)
                if product:
                    self.producto_detalle = {
                        "id": product.id,
                        "nombre": product.nombre,
                        "descripcion": product.descripcion,
                        "precio": float(product.precio),
                        "precio_anterior": float(product.precio_anterior) if product.precio_anterior else 0.0,
                        "stock": int(product.stock),
                        "categoria": product.categoria,
                        "is_active": product.is_active
                    }
                    
                    if product.fotos and len(product.fotos) > 0:
                        self.fotos_producto = list(product.fotos)
                    else:
                        self.fotos_producto = ["/favicon.ico"]
                        
                    self.foto_principal = self.fotos_producto[0]
                    
                    if product.variaciones and isinstance(product.variaciones, list) and len(product.variaciones) > 0:
                        self.variantes_producto = product.variaciones
                        disponible = next((v for v in product.variaciones if v.get("stock", 0) > 0), product.variaciones[0])
                        self.variante_seleccionada = disponible
                        if disponible.get("foto"):
                            self.foto_principal = disponible.get("foto")
                    else:
                        self.variantes_producto = []
                        self.variante_seleccionada = {}

                    rec_query = sqlmodel.select(TribuProduct).where(
                        TribuProduct.categoria == product.categoria,
                        TribuProduct.id != product.id,
                        TribuProduct.is_active == True
                    ).limit(4)
                    
                    db_recs = session.exec(rec_query).all()
                    self.productos_recomendados = [
                        {
                            "id": p.id,
                            "nombre": p.nombre,
                            "precio": float(p.precio),
                            "foto_principal": p.fotos[0] if p.fotos and len(p.fotos) > 0 else "",
                            "categoria": p.categoria
                        }
                        for p in db_recs
                    ]
        except Exception as e:
            print(f"Error cargando detalle del producto: {e}")

    # ==================================================================
    # 6. LÓGICA Y ESTADO DEL CARRITO DE COMPRAS Y NOTIFICACIONES
    # ==================================================================
    carrito: list[dict] = []
    mostrar_carrito: bool = False
    
    notificaciones_carrito: list[dict] = []
    mostrar_notificaciones_carrito: bool = False

    @rx.var
    def total_items_carrito(self) -> int:
        return sum(item.get("cantidad", 1) for item in self.carrito)

    @rx.var
    def subtotal_carrito(self) -> float:
        total = sum(item.get("precio", 0.0) * item.get("cantidad", 1) for item in self.carrito)
        return round(total, 2)

    @rx.var
    def porcentaje_descuento_activo(self) -> int:
        p_actual = self.variante_seleccionada.get("precio") if self.variante_seleccionada else self.producto_detalle.get("precio", 0.0)
        p_anterior = self.variante_seleccionada.get("precio_anterior") if self.variante_seleccionada else self.producto_detalle.get("precio_anterior", 0.0)
        
        if p_anterior and p_anterior > p_actual and p_actual > 0:
            return round(((p_anterior - p_actual) / p_anterior) * 100)
        return 0

    def toggle_notificaciones_carrito(self):
        self.mostrar_notificaciones_carrito = not self.mostrar_notificaciones_carrito

    def limpiar_notificaciones_carrito(self):
        self.notificaciones_carrito = []
        self.mostrar_notificaciones_carrito = False

    def registrar_notificacion(self, texto: str, tipo: str = "info"):
        self.notificaciones_carrito.insert(0, {
            "id": len(self.notificaciones_carrito) + 1,
            "texto": texto,
            "tipo": tipo
        })

    def sincronizar_y_validar_carrito(self):
        if not self.carrito:
            return

        prod_ids = list({item["id"] for item in self.carrito})
        
        try:
            with rx.session() as session:
                productos_db = session.exec(
                    sqlmodel.select(TribuProduct).where(TribuProduct.id.in_(prod_ids))
                ).all()
                
                prod_map = {p.id: p for p in productos_db}
                items_validados = []

                for item in self.carrito:
                    p_id = item["id"]
                    p_db = prod_map.get(p_id)

                    if not p_db or not p_db.is_active:
                        msg = f"El producto '{item['nombre']}' ya no está disponible."
                        self.registrar_notificacion(msg, "warning")
                        yield rx.toast.error(msg)
                        continue

                    precio_actual = float(p_db.precio)
                    precio_anterior = float(p_db.precio_anterior) if p_db.precio_anterior else 0.0
                    stock_actual = int(p_db.stock)

                    if item.get("variante") and p_db.variaciones:
                        variante_db = next((v for v in p_db.variaciones if v.get("nombre") == item["variante"]), None)
                        if variante_db:
                            precio_actual = float(variante_db.get("precio", precio_actual))
                            precio_anterior = float(variante_db.get("precio_anterior", precio_anterior))
                            stock_actual = int(variante_db.get("stock", 0))

                    if item["precio"] != precio_actual:
                        if precio_actual < item["precio"]:
                            msg = f"¡Oferta Relámpago! '{item['nombre']}' bajó de ${item['precio']} a ${precio_actual} USD."
                            self.registrar_notificacion(msg, "oferta")
                            yield rx.toast.info(msg)
                        else:
                            msg = f"El precio de '{item['nombre']}' se actualizó a ${precio_actual} USD."
                            self.registrar_notificacion(msg, "info")
                            yield rx.toast.warning(msg)
                        item["precio"] = precio_actual
                    
                    item["precio_anterior"] = precio_anterior

                    if stock_actual <= 0:
                        msg = f"'{item['nombre']}' se agotó y fue removido de tu carrito."
                        self.registrar_notificacion(msg, "warning")
                        yield rx.toast.error(msg)
                        continue

                    if item["cantidad"] > stock_actual:
                        msg = f"Ajustamos '{item['nombre']}' a {stock_actual} unid. por límite de stock."
                        self.registrar_notificacion(msg, "info")
                        yield rx.toast.warning(msg)
                        item["cantidad"] = stock_actual
                    
                    item["stock_max"] = stock_actual
                    items_validados.append(item)

                self.carrito = items_validados

        except Exception as e:
            print(f"Error sincronizando carrito con Supabase: {e}")

    def toggle_carrito(self):
        self.mostrar_carrito = not self.mostrar_carrito
        if self.mostrar_carrito:
            return self.sincronizar_y_validar_carrito()

    def cerrar_carrito(self):
        self.mostrar_carrito = False
        self.mostrar_notificaciones_carrito = False

    def ir_a_producto_desde_carrito(self, prod_id: int):
        self.mostrar_carrito = False
        self.mostrar_notificaciones_carrito = False
        return rx.redirect(f"/product/{prod_id}")    

    def agregar_al_carrito(self):
        if not self.producto_detalle:
            return
        
        prod_id = self.producto_detalle.get("id")
        nombre_base = self.producto_detalle.get("nombre")
        tiene_variante = bool(self.variante_seleccionada and self.variantes_producto)
        
        if tiene_variante:
            variante_nombre = self.variante_seleccionada.get("nombre", "")
            nombre_item = f"{nombre_base} - {variante_nombre}"
            precio = float(self.variante_seleccionada.get("precio", self.producto_detalle.get("precio", 0.0)))
            precio_anterior = float(self.variante_seleccionada.get("precio_anterior", self.producto_detalle.get("precio_anterior", 0.0)))
            stock_max = int(self.variante_seleccionada.get("stock", 0))
            foto = self.variante_seleccionada.get("foto") or self.foto_principal or "/favicon.ico"
            key = f"{prod_id}_{variante_nombre}"
        else:
            variante_nombre = ""
            nombre_item = nombre_base
            precio = float(self.producto_detalle.get("precio", 0.0))
            precio_anterior = float(self.producto_detalle.get("precio_anterior", 0.0))
            stock_max = int(self.producto_detalle.get("stock", 0))
            foto = self.foto_principal or "/favicon.ico"
            key = str(prod_id)

        cant = self.cantidad_producto

        if stock_max <= 0:
            return rx.toast.error("Este producto/variante se encuentra agotado actualmente.")

        existente = next((item for item in self.carrito if item["key"] == key), None)

        if existente:
            nueva_cant = existente["cantidad"] + cant
            if nueva_cant > stock_max:
                existente["cantidad"] = stock_max
                return rx.toast.warning(f"Se ajustó al límite de stock disponible ({stock_max} unid.)")
            else:
                existente["cantidad"] = nueva_cant
        else:
            self.carrito.append({
                "key": key,
                "id": prod_id,
                "nombre": nombre_item,
                "variante": variante_nombre,
                "precio": precio,
                "precio_anterior": precio_anterior,
                "foto": foto,
                "cantidad": cant,
                "stock_max": stock_max
            })

        self.mostrar_carrito = True
        self.guardar_carrito_db()
        return rx.toast.success(f"¡{nombre_item} agregado al carrito!")
        

    def eliminar_del_carrito(self, key: str):
        self.carrito = [item for item in self.carrito if item["key"] != key]
        self.guardar_carrito_db()

    def incrementar_item_carrito(self, key: str):
        for item in self.carrito:
            if item["key"] == key:
                if item["cantidad"] < item["stock_max"]:
                    item["cantidad"] += 1
                    self.guardar_carrito_db()
                else:
                    return rx.toast.warning(f"Límite de stock alcanzado ({item['stock_max']} unid.)")
                break

    def decrementar_item_carrito(self, key: str):
        for item in self.carrito:
            if item["key"] == key:
                if item["cantidad"] > 1:
                    item["cantidad"] -= 1
                    self.guardar_carrito_db()
                else:
                    self.eliminar_del_carrito(key)
                break

# =========================================================================
    # 🔔 SISTEMA DE NOTIFICACIONES UNIFICADO Y REDIRECCIÓN INTELIGENTE
    # =========================================================================
    notificaciones_lista: list[dict[str, Any]] = []
    show_popover_notificaciones: bool = False

    def toggle_menu_notificaciones(self):
        self.show_popover_notificaciones = not self.show_popover_notificaciones
        if self.show_popover_notificaciones:
            self.cargar_notificaciones_usuario()

    def cerrar_menu_notificaciones(self):
        self.show_popover_notificaciones = False

    @rx.var
    def total_notificaciones_no_leidas(self) -> int:
        return sum(1 for n in self.notificaciones_lista if not n.get("leido"))

    def cargar_notificaciones_usuario(self):
        """Carga notificaciones según el rol: Admin, Cliente logueado o visitante Público."""
        try:
            with rx.session() as session:
                if self.admin_logged_in:
                    # Notificaciones destinadas al Administrador
                    query = sqlmodel.select(TribuNotification).where(
                        (TribuNotification.es_admin == True) | (TribuNotification.es_publico == True)
                    ).order_by(TribuNotification.id.desc()).limit(15)
                elif self.user_logged_in and self.usuario_datos.get("email"):
                    u_email = self.usuario_datos.get("email", "").strip().lower()
                    # Notificaciones privadas del Cliente + Anuncios Públicos
                    query = sqlmodel.select(TribuNotification).where(
                        (sa.func.lower(TribuNotification.destinatario_email) == u_email) | (TribuNotification.es_publico == True)
                    ).order_by(TribuNotification.id.desc()).limit(15)
                else:
                    # Visitante no registrado (Solo anuncios públicos)
                    query = sqlmodel.select(TribuNotification).where(
                        TribuNotification.es_publico == True
                    ).order_by(TribuNotification.id.desc()).limit(10)

                db_nots = session.exec(query).all()
                self.notificaciones_lista = [
                    {
                        "id": n.id,
                        "titulo": n.titulo,
                        "mensaje": n.mensaje,
                        "target_url": n.target_url,
                        "leido": n.leido
                    }
                    for n in db_nots
                ]
        except Exception as e:
            print(f"Error cargando notificaciones: {e}")

    def clic_notificacion_redireccionar(self, notif_id: int, target_url: str):
        """Marca la notificación como leída y redirige al destino exacto."""
        try:
            with rx.session() as session:
                db_n = session.get(TribuNotification, notif_id)
                if db_n:
                    db_n.leido = True
                    session.add(db_n)
                    session.commit()
        except Exception as e:
            print(f"Error actualizando leido: {e}")

        self.show_popover_notificaciones = False
        self.cargar_notificaciones_usuario()

        if target_url.startswith("admin_tab_"):
            tab_target = target_url.replace("admin_tab_", "")
            self.admin_tab_activa = tab_target
            return rx.redirect("/admin#seccion-admin-panel")
        
        target = f"{target_url}#seccion-login-perfil" if target_url == "/login" else target_url
        return rx.redirect(target)

    def crear_notificacion_db(self, titulo: str, mensaje: str, target_url: str, destinatario_email: str | None = None, es_admin: bool = False, es_publico: bool = False):
        """Método auxiliar interno para registrar notificaciones en Supabase."""
        try:
            with rx.session() as session:
                nueva_n = TribuNotification(
                    destinatario_email=destinatario_email,
                    es_admin=es_admin,
                    es_publico=es_publico,
                    titulo=titulo,
                    mensaje=mensaje,
                    target_url=target_url,
                    leido=False
                )
                session.add(nueva_n)
                session.commit()
        except Exception as e:
            print(f"Error registrando notificación en BD: {e}")

    # =========================================================================
    # 🎁 ESTADO Y LÓGICA DE TARJETAS DE REGALO / VOUCHERS DE EXPERIENCIAS
    # =========================================================================
    experiencias_disponibles: list[dict[str, Any]] = [
        {
            "id": "exp_1",
            "nombre": "Pase para Sesión Grupal de Sonoterapia",
            "descripcion": "Un viaje de inmersión acústica profunda con cuencos, didgeridoo y vientos en nuestras sesiones semanales.",
            "precio": 20.0,
            "badge": "MÁS POPULAR"
        },
        {
            "id": "exp_2",
            "nombre": "Ritual & Taller Sonoro en Pareja",
            "descripcion": "Espacio sagrado de reconexión, armonización de chakras y sanación acústica compartida.",
            "precio": 45.0,
            "badge": "EXPERIENCIA EN DUO"
        },
        {
            "id": "exp_3",
            "nombre": "Pase Doble para Ceremónia / Concierto Holístico",
            "descripcion": "Entrada doble para nuestros conciertos vivenciales y ceremonias de sonido de la Tribu.",
            "precio": 60.0,
            "badge": "EVENTO ESPECIAL"
        },
        {
            "id": "exp_4",
            "nombre": "Sesión Individual Privada con Terapeuta Aliado",
            "descripcion": "Atención personalizada de 90 minutos enfocada en la restauración energética y vibracional.",
            "precio": 80.0,
            "badge": "VIP & PRIVADO"
        }
    ]

    gc_experiencia_seleccionada: str = "Pase para Sesión Grupal de Sonoterapia"
    gc_monto_experiencia: float = 20.0
    gc_para_nombre: str = ""
    gc_de_nombre: str = ""
    gc_destinatario_email: str = ""
    gc_destinatario_whatsapp: str = ""
    gc_mensaje: str = ""

    def seleccionar_experiencia_gc(self, exp_nombre: str, precio: float):
        self.gc_experiencia_seleccionada = exp_nombre
        self.gc_monto_experiencia = precio

    def set_gc_para_nombre(self, val: str): self.gc_para_nombre = val
    def set_gc_de_nombre(self, val: str): self.gc_de_nombre = val
    def set_gc_destinatario_email(self, val: str): self.gc_destinatario_email = val
    def set_gc_destinatario_whatsapp(self, val: str): self.gc_destinatario_whatsapp = val
    def set_gc_mensaje(self, val: str): self.gc_mensaje = val

    def agregar_voucher_al_carrito(self):
        if not self.gc_para_nombre.strip() or not self.gc_de_nombre.strip():
            return rx.toast.error("Por favor completa los nombres de quien regala y quien recibe.")

        import uuid
        codigo_gen = f"TRIBU-{uuid.uuid4().hex[:6].upper()}"
        
        item_voucher = {
            "key": f"voucher_{codigo_gen}",
            "id": 9999,
            "nombre": f"Voucher: {self.gc_experiencia_seleccionada}",
            "variante": f"Para: {self.gc_para_nombre} | Código: {codigo_gen}",
            "precio": self.gc_monto_experiencia,
            "precio_anterior": 0.0,
            "foto": "https://ufjkeqqwgyauzujrbfcv.supabase.co/storage/v1/object/public/portfolio/logo%20tribu.png",
            "cantidad": 1,
            "stock_max": 10,
            "es_voucher": True,
            "voucher_data": {
                "codigo": codigo_gen,
                "experiencia": self.gc_experiencia_seleccionada,
                "para": self.gc_para_nombre,
                "de": self.gc_de_nombre,
                "destinatario_email": self.gc_destinatario_email,
                "destinatario_whatsapp": self.gc_destinatario_whatsapp,
                "mensaje": self.gc_mensaje
            }
        }
        
        self.carrito.append(item_voucher)
        self.mostrar_carrito = True
        return rx.toast.success(f"¡Voucher '{self.gc_experiencia_seleccionada}' agregado al carrito!")
    
    # =========================================================================
    # 🛒 ESTADO Y VARIABLES PARA EL CHECKOUT / PROCESAMIENTO DE ORDEN
    # =========================================================================

       
    def llenar_datos_prueba_checkout(self):
        """Llena automáticamente todos los campos del checkout con datos de prueba."""
        self.checkout_nombre = "Jesús"
        self.checkout_apellido = "Buraglia"
        self.checkout_email = "jesus.prueba@tribusonora.com"
        self.checkout_telefono = "+584123445369"
        self.checkout_pais = "Venezuela"
        self.checkout_direccion = "Av. Principal de Las Mercedes, Edif. Tribu"
        self.checkout_apartamento = "Piso 3, Apto 3B"
        self.checkout_ciudad = "Caracas"
        self.checkout_codigo_postal = "1060"
        self.checkout_cupon = "TRIBU10"
        self.numero_referencia = "REF-987654"
        return rx.toast.info("🧪 Formulario cargado con datos de prueba.")

    checkout_email: str = ""
    checkout_newsletter: bool = True
    checkout_nombre: str = ""
    checkout_apellido: str = ""
    checkout_pais: str = "Venezuela"
    checkout_direccion: str = ""
    checkout_apartamento: str = ""
    checkout_ciudad: str = ""
    checkout_codigo_postal: str = ""
    checkout_telefono: str = ""

    checkout_cupon: str = ""
    checkout_cupon_aplicado_codigo: str = ""
    descuento_cupon_monto: float = 0.0
    costo_envio: float = 0.0

    # 3. Métodos de Pago P2P y Comprobante
    metodo_pago_seleccionado: str = "pago_movil"  # 'pago_movil', 'zelle', 'binance', 'paypal', 'transferencia'
    numero_referencia: str = ""
    comprobante_path: str = ""
    comprobante_filename: str = ""
    comprobante_cargado: bool = False

    async def handle_upload(self, files: list[rx.UploadFile]):
        """Procesa el archivo temporal en el buffer de Reflex guardando el nombre del archivo."""
        if files:
            file = files[0]
            upload_data = await file.read()
            
            upload_dir = rx.get_upload_dir()
            file_path = upload_dir / file.filename
            
            with open(file_path, "wb") as f:
                f.write(upload_data)
            
            self.comprobante_filename = file.filename
            self.comprobante_cargado = True

    def limpiar_comprobante(self):
        """Limpia el comprobante actual para permitir al usuario cambiar la imagen."""
        self.comprobante_filename = ""
        self.comprobante_cargado = False

    @rx.var
    def total_checkout(self) -> float:
        try:
            subtotal = float(self.subtotal_carrito)
        except ValueError:
            subtotal = 0.0
        total = subtotal - self.descuento_cupon_monto + self.costo_envio
        return max(0.0, round(total, 2))

    def seleccionar_metodo_pago(self, metodo: str):
        self.metodo_pago_seleccionado = metodo

    def set_checkout_email(self, val: str):
        self.checkout_email = val

    def set_checkout_nombre(self, val: str):
        self.checkout_nombre = val

    def set_checkout_apellido(self, val: str):
        self.checkout_apellido = val

    def set_checkout_pais(self, val: str):
        self.checkout_pais = val

    def set_checkout_direccion(self, val: str):
        self.checkout_direccion = val

    def set_checkout_apartamento(self, val: str):
        self.checkout_apartamento = val

    def set_checkout_ciudad(self, val: str):
        self.checkout_ciudad = val

    def set_checkout_codigo_postal(self, val: str):
        self.checkout_codigo_postal = val

    def set_checkout_telefono(self, val: str):
        self.checkout_telefono = val

    def set_checkout_cupon(self, val: str):
        self.checkout_cupon = val

    def set_numero_referencia(self, val: str):
        self.numero_referencia = val

    def aplicar_cupon(self):
        """Valida y aplica cupones dinámicos de Supabase o Vouchers en el checkout del Shop."""
        cupon_clean = self.checkout_cupon.strip().upper()
        if not cupon_clean:
            self.descuento_cupon_monto = 0.0
            self.checkout_cupon_aplicado_codigo = ""
            return rx.toast.info("Cupón removido.")

        try:
            subtotal = float(self.subtotal_carrito)
        except ValueError:
            subtotal = 0.0

        try:
            with rx.session() as session:
                db_cupon = session.exec(
                    sqlmodel.select(TribuCoupon).where(
                        TribuCoupon.codigo == cupon_clean,
                        TribuCoupon.is_active == True
                    )
                ).first()

                if db_cupon:
                    if db_cupon.usos_actuales >= db_cupon.usos_maximos:
                        self.descuento_cupon_monto = 0.0
                        self.checkout_cupon_aplicado_codigo = ""
                        return rx.toast.error("Este cupón ya fue utilizado o ha expirado.")

                    if db_cupon.tipo == "PORCENTAJE":
                        desc = round(subtotal * (db_cupon.valor / 100.0), 2)
                        msg = f"¡Cupón de {db_cupon.valor:.0f}% aplicado (-${desc:.2f} USD)!"
                    else:
                        desc = min(subtotal, float(db_cupon.valor))
                        msg = f"¡Cupón de descuento aplicado (-${desc:.2f} USD)!"

                    self.descuento_cupon_monto = desc
                    self.checkout_cupon_aplicado_codigo = db_cupon.codigo
                    return rx.toast.success(msg)

                # Fallback para Vouchers / Gift Cards
                gc = session.exec(
                    sqlmodel.select(TribuGiftCard).where(
                        TribuGiftCard.codigo == cupon_clean,
                        TribuGiftCard.estado == "ACTIVA"
                    )
                ).first()

                if gc:
                    desc = min(subtotal, float(gc.monto_equivalente))
                    self.descuento_cupon_monto = desc
                    self.checkout_cupon_aplicado_codigo = gc.codigo
                    return rx.toast.success(f"¡Voucher '{gc.experiencia_nombre}' aplicado (-${desc:.2f} USD)!")

                self.descuento_cupon_monto = 0.0
                self.checkout_cupon_aplicado_codigo = ""
                return rx.toast.error("Código de cupón o descuento inválido o inactivo.")
        except Exception as e:
            print(f"Error al validar cupón en checkout: {e}")
            self.descuento_cupon_monto = 0.0
            self.checkout_cupon_aplicado_codigo = ""
            return rx.toast.error("Error al verificar el cupón.")

    def set_checkout_newsletter(self, checked: bool):
        self.checkout_newsletter = checked

    def autocompletar_checkout_usuario(self):
        """Carga automáticamente los datos de contacto y dirección guardados del usuario en Supabase."""
        if not self.user_logged_in or not self.usuario_datos.get("id"):
            return
        u_id = self.usuario_datos.get("id")
        try:
            with rx.session() as session:
                db_user = session.get(TribuUser, u_id)
                if db_user:
                    if db_user.email: self.checkout_email = db_user.email
                    if db_user.nombre: self.checkout_nombre = db_user.nombre
                    if db_user.apellido: self.checkout_apellido = db_user.apellido
                    if db_user.telefono: self.checkout_telefono = db_user.telefono
                    if db_user.pais: self.checkout_pais = db_user.pais
                    if db_user.direccion: self.checkout_direccion = db_user.direccion
                    if db_user.apartamento: self.checkout_apartamento = db_user.apartamento
                    if db_user.ciudad: self.checkout_ciudad = db_user.ciudad
                    if db_user.codigo_postal: self.checkout_codigo_postal = db_user.codigo_postal
        except Exception as e:
            print(f"Error autocompletando datos de usuario: {e}")

    def ir_a_checkout(self):
        self.mostrar_carrito = False
        self.mostrar_notificaciones_carrito = False
        self.autocompletar_checkout_usuario()
        return rx.redirect("/checkout")

    def comprar_ahora(self):
        """Añade el producto actual al carrito y redirige inmediatamente al checkout (con validación de stock)."""
        stock_max = self.variante_seleccionada.get("stock") if self.variante_seleccionada else self.producto_detalle.get("stock", 0)
        if stock_max <= 0:
            return rx.toast.error("Este producto/variante se encuentra agotado actualmente.")
            
        self.agregar_al_carrito()
        return self.ir_a_checkout()

    def compartir_producto_whatsapp(self):
        """Genera el enlace dinámico de WhatsApp para compartir el producto actual."""
        import urllib.parse
        prod_id = self.producto_detalle.get("id", "")
        prod_nombre = self.producto_detalle.get("nombre", "")
        
        # Enlace dinámico directo al producto
        link_producto = f"https://tribusonoraconsciente.com/product/{prod_id}"
        
        mensaje = (
            f"Mira lo que tienen disponible en la plataforma web de Tribu Sonora Consciente: "
            f"*{prod_nombre}*\n{link_producto}"
        )
        encoded_msg = urllib.parse.quote(mensaje)
        return rx.redirect(f"https://wa.me/?text={encoded_msg}", is_external=True)
    
    # -------------------------------------------------------------------------
    # 💳 MÉTODOS DE PAGO DINÁMICOS Y CONEXIÓN SUPABASE
    # -------------------------------------------------------------------------
    def get_supabase_client(self):
        """Inicializa y retorna el cliente oficial de Supabase con fallback de URL de proyecto."""
        import os

        from supabase import create_client

        # URL oficial de tu proyecto en Supabase Cloud
        url = os.environ.get("SUPABASE_URL", "https://ufjkeqqwgyauzujrbfcv.supabase.co")
        key = os.environ.get("SUPABASE_SERVICE_KEY", os.environ.get("SUPABASE_KEY", os.environ.get("SUPABASE_ANON_KEY", "")))

        if not url or not key:
            print("⚠️ AVISO: Agrega SUPABASE_KEY o SUPABASE_ANON_KEY a tu archivo .env para habilitar el Storage.")
            return None

        try:
            return create_client(url, key)
        except Exception as e:
            print(f"Error inicializando cliente de Supabase: {e}")
            return None

    metodos_pago_db: list[dict] = [
        {
            "id": 1,
            "tipo": "pago_movil",
            "titulo": "Pago Móvil (Bolívares)",
            "icono": "smartphone",
            "detalles_texto": "• Banco: Mercantil (0105)\n• Cédula: V-19.876.543\n• Teléfono: 0412-3690000\n• Tasa: Oficial BCV del día."
        },
        {
            "id": 2,
            "tipo": "zelle",
            "titulo": "Zelle (USD)",
            "icono": "dollar_sign",
            "detalles_texto": "• Correo Zelle: pagos@tribusonoraconsciente.com\n• Titular: Tribu Sonora Consciente LLC"
        },
        {
            "id": 3,
            "tipo": "binance",
            "titulo": "Binance Pay (USDT)",
            "icono": "wallet",
            "detalles_texto": "• Binance Pay ID: 284910381\n• Email: binance@tribusonoraconsciente.com"
        },
        {
            "id": 4,
            "tipo": "paypal",
            "titulo": "PayPal",
            "icono": "globe",
            "detalles_texto": "• Cuenta: paypal@tribusonoraconsciente.com\n• Nota: Enviar monto neto."
        },
        {
            "id": 5,
            "tipo": "transferencia",
            "titulo": "Transferencia Bancaria",
            "icono": "building_2",
            "detalles_texto": "• Banco Mercantil - Cta. Corriente\n• Nro: 0105-0123-45-1234567890\n• RIF: J-50123456-0"
        }
    ]

    def cargar_metodos_pago(self):
        try:
            client = self.get_supabase_client()
            if client:
                res = client.table("tribu_payment_methods").select("*").eq("activo", True).execute()
                if res.data and len(res.data) > 0:
                    self.metodos_pago_db = res.data
        except Exception as e:
            print(f"Error cargando métodos de pago desde Supabase: {e}")

    # -------------------------------------------------------------------------
    # 🚀 PROCESAMIENTO DE LA ORDEN Y WHATSAPP
    # -------------------------------------------------------------------------
    async def procesar_orden(self, files: list[rx.UploadFile]):
        """
        Procesa la compra: valida campos, guarda la imagen del capture,
        registra la orden en Supabase con el 3% silencioso y redirige a WhatsApp.
        """
        # 1. Validaciones de campos obligatorios
        if not self.carrito:
            yield rx.toast.error("Tu carrito está vacío. Agrega productos antes de finalizar.")
            return

        if not self.checkout_nombre.strip() or not self.checkout_apellido.strip():
            yield rx.toast.error("Por favor, ingresa tu Nombre y Apellido.")
            return

        contacto_valido = self.checkout_email.strip() or self.checkout_telefono.strip()
        if not contacto_valido:
            yield rx.toast.error("Ingresa un correo electrónico o teléfono móvil de contacto.")
            return

        if not self.numero_referencia.strip():
            yield rx.toast.error("Por favor, ingresa el Número de Referencia o Confirmación del pago.")
            return

        if not self.comprobante_cargado and (not files or len(files) == 0):
            yield rx.toast.error("Es obligatorio adjuntar la captura/comprobante del pago.")
            return

        # 2. Subida oficial a Supabase Storage (Bucket: 'comprobantes')
        comprobante_url = ""
        try:
            upload_dir = rx.get_upload_dir()
            temp_file_path = upload_dir / self.comprobante_filename if self.comprobante_filename else None
            
            file_bytes = b""
            if temp_file_path and temp_file_path.exists():
                with open(temp_file_path, "rb") as f:
                    file_bytes = f.read()
            elif files and len(files) > 0:
                file_bytes = await files[0].read()
                if not self.comprobante_filename:
                    self.comprobante_filename = files[0].filename

            if file_bytes:
                    client = self.get_supabase_client()
                    if client:
                        clean_ref = "".join(filter(str.isalnum, self.numero_referencia))
                        storage_filename = f"ref_{clean_ref}_{self.comprobante_filename}"
                        
                        # Detección dinámica del Content-Type según la extensión del archivo
                        ext = self.comprobante_filename.lower()
                        if ext.endswith((".jpg", ".jpeg")):
                            mime_type = "image/jpeg"
                        elif ext.endswith(".webp"):
                            mime_type = "image/webp"
                        elif ext.endswith(".pdf"):
                            mime_type = "application/pdf"
                        else:
                            mime_type = "image/png"

                        # Subida al Bucket de Supabase especificando Content-Type y Upsert
                        client.storage.from_("comprobantes").upload(
                            path=storage_filename,
                            file=file_bytes,
                            file_options={
                                "upsert": "true",
                                "content-type": mime_type
                            }
                        )
                        
                        # Generación de la URL Pública Oficial en la nube
                        comprobante_url = client.storage.from_("comprobantes").get_public_url(storage_filename)
        except Exception as e:
            print(f"Error subiendo comprobante a Supabase Storage: {e}")
            comprobante_url = f"Referencia: {self.numero_referencia}"

        # 3. Cálculo Silencioso de la Comisión (3% Interno)
        total_monto = float(self.total_checkout)
        comision_3percent = round(total_monto * 0.03, 2)

        # 4. Inserción de la orden en Supabase (tribu_orders) y actualización de perfil
        try:
            with rx.session() as session:
                # Guardar/Actualizar perfil de dirección en tribu_users si está logueado
                if self.user_logged_in and self.usuario_datos.get("id"):
                    u_id = self.usuario_datos.get("id")
                    db_u = session.get(TribuUser, u_id)
                    if db_u:
                        db_u.nombre = self.checkout_nombre.strip().capitalize()
                        if self.checkout_apellido:
                            db_u.apellido = self.checkout_apellido.strip().capitalize()
                        if self.checkout_telefono:
                            db_u.telefono = self.checkout_telefono.strip()
                        if self.checkout_pais:
                            db_u.pais = self.checkout_pais
                        if self.checkout_direccion:
                            db_u.direccion = self.checkout_direccion.strip()
                        if self.checkout_apartamento:
                            db_u.apartamento = self.checkout_apartamento.strip()
                        if self.checkout_ciudad:
                            db_u.ciudad = self.checkout_ciudad.strip()
                        if self.checkout_codigo_postal:
                            db_u.codigo_postal = self.checkout_codigo_postal.strip()
                        session.add(db_u)
                items_resumen = [
                    {
                        "nombre": item.get("nombre"),
                        "cantidad": item.get("cantidad"),
                        "precio": item.get("precio"),
                        "variante": item.get("variante", "")
                    }
                    for item in self.carrito
                ]

                # Guardar registros de Vouchers en tribu_gift_cards
                for item in self.carrito:
                    if item.get("es_voucher") and item.get("voucher_data"):
                        v_data = item.get("voucher_data")
                        nuevo_v = TribuGiftCard(
                            codigo=v_data.get("codigo"),
                            tipo="EXPERIENCIA",
                            experiencia_nombre=v_data.get("experiencia"),
                            monto_equivalente=float(item.get("precio", 0.0)),
                            comprador_nombre=f"{self.checkout_nombre} {self.checkout_apellido}".strip(),
                            comprador_email=self.checkout_email,
                            comprador_telefono=self.checkout_telefono,
                            destinatario_nombre=v_data.get("para"),
                            destinatario_email=v_data.get("destinatario_email"),
                            destinatario_whatsapp=v_data.get("destinatario_whatsapp"),
                            mensaje_personalizado=v_data.get("mensaje"),
                            estado="PENDIENTE_PAGO"
                        )
                        session.add(nuevo_v)
                
                import json
                sql_insert = sa.text("""
                    INSERT INTO tribu_orders (
                        cliente_email, cliente_nombre, cliente_apellido, cliente_telefono,
                        cliente_pais, cliente_direccion, cliente_ciudad, cliente_codigo_postal,
                        metodo_pago, numero_referencia, comprobante_url,
                        monto_subtotal, monto_descuento, monto_total, comision_plataforma,
                        estado, items_json, cupon_codigo
                    ) VALUES (
                        :email, :nombre, :apellido, :telefono,
                        :pais, :direccion, :ciudad, :cp,
                        :metodo, :ref, :comprobante,
                        :subtotal, :descuento, :total, :comision,
                        'PENDING_VERIFICATION', :items, :cupon
                    )
                """)

                session.execute(sql_insert, {
                    "email": self.checkout_email,
                    "nombre": self.checkout_nombre,
                    "apellido": self.checkout_apellido,
                    "telefono": self.checkout_telefono,
                    "pais": self.checkout_pais,
                    "direccion": self.checkout_direccion,
                    "ciudad": self.checkout_ciudad,
                    "cp": self.checkout_codigo_postal,
                    "metodo": self.metodo_pago_seleccionado,
                    "ref": self.numero_referencia,
                    "comprobante": comprobante_url,
                    "subtotal": float(self.subtotal_carrito),
                    "descuento": float(self.descuento_cupon_monto),
                    "total": total_monto,
                    "comision": comision_3percent,
                    "items": json.dumps(items_resumen),
                    "cupon": self.checkout_cupon_aplicado_codigo if self.checkout_cupon_aplicado_codigo else None
                })

                # 🎟️ Sumar +1 uso al cupón de compra y desactivarlo si aplica
                if self.checkout_cupon_aplicado_codigo:
                    db_cupon = session.exec(
                        sqlmodel.select(TribuCoupon).where(
                            TribuCoupon.codigo == self.checkout_cupon_aplicado_codigo.strip().upper()
                        )
                    ).first()
                    if db_cupon:
                        db_cupon.usos_actuales += 1
                        if db_cupon.usos_actuales >= db_cupon.usos_maximos:
                            db_cupon.is_active = False
                        session.add(db_cupon)

                session.commit()

                # Limpiar estado del cupón
                self.checkout_cupon = ""
                self.checkout_cupon_aplicado_codigo = ""
                self.descuento_cupon_monto = 0.0
        except Exception as err:
            print(f"Aviso guardando en BD (Continuando a WhatsApp): {err}")

        # 5. Generación del Mensaje Estructurado para WhatsApp
        import urllib.parse
        
        NUMERO_WHATSAPP_REAL = "584241359530"  # 📲 Número oficial de prueba
        metodo_nombre = self.metodo_pago_seleccionado.replace("_", " ").title()
        
        # Generación dinámica de la lista de productos y cantidades desde el carrito
        lineas_productos = [
            f"• *{item.get('cantidad', 1)}x* {item.get('nombre')}"
            for item in self.carrito
        ]
        texto_productos = "\n".join(lineas_productos)

        link_comprobante_texto = f" *Comprobante:* {comprobante_url}\n" if comprobante_url else ""

        mensaje_wa = (
            f"¡Hola Tribu Sonora Consciente! \n\n"
            f"Acabo de realizar la confirmación de mi orden:\n"
            f"{texto_productos}\n\n"
            f"Por un total de: *${total_monto} USD*\n\n"
            f" *Cliente:* {self.checkout_nombre} {self.checkout_apellido}\n"
            f" *Contacto:* {self.checkout_telefono or self.checkout_email}\n"
            f" *Método de Pago:* {metodo_nombre}\n"
            f" *Nro. Referencia:* {self.numero_referencia}\n"
            f" *Ubicación:* {self.checkout_ciudad}, {self.checkout_pais}\n\n"
            f"{link_comprobante_texto}\n"
            f"Quedo a la espera de la verificación de mi orden. ¡Muchas gracias!"
        )
        
        encoded_msg = urllib.parse.quote(mensaje_wa)
        whatsapp_url = f"https://wa.me/{NUMERO_WHATSAPP_REAL}?text={encoded_msg}"

        # 6. Limpieza de carrito, estado de comprobante y redirección
        self.carrito = []
        self.numero_referencia = ""
        self.comprobante_cargado = False
        self.comprobante_filename = ""

        self.crear_notificacion_db(
            titulo="🛒 Nuevo Pedido Recibido",
            mensaje=f"Pedido por ${total_monto} USD de {self.checkout_nombre} {self.checkout_apellido}.",
            target_url="admin_tab_pedidos",
            es_admin=True
        )
        
        yield rx.toast.success("¡Orden procesada con éxito! Redirigiendo a WhatsApp...")
        yield rx.redirect(whatsapp_url, is_external=True)

    # -------------------------------------------------------------------------
    # 🔍 RASTREO DE ÓRDENES
    # -------------------------------------------------------------------------
    rastreo_contacto: str = ""
    rastreo_referencia: str = ""
    ordenes_encontradas: list[dict] = []
    busqueda_realizada: bool = False

    def set_rastreo_contacto(self, val: str):
        self.rastreo_contacto = val

    def set_rastreo_referencia(self, val: str):
        self.rastreo_referencia = val

    def buscar_orden_rastreo(self):
        contacto_clean = self.rastreo_contacto.strip().lower()
        ref_clean = self.rastreo_referencia.strip().lower()

        if not contacto_clean or not ref_clean:
            self.ordenes_encontradas = []
            self.busqueda_realizada = True
            return rx.toast.error("Por favor completa ambos campos para realizar la búsqueda.")

        try:
            client = self.get_supabase_client()
            if client:
                res = client.table("tribu_orders").select("*").ilike("numero_referencia", f"%{ref_clean}%").execute()
                if res.data:
                    filtradas = [
                        o for o in res.data
                        if contacto_clean in str(o.get("cliente_email", "")).lower()
                        or contacto_clean in str(o.get("cliente_telefono", "")).lower()
                    ]
                    self.ordenes_encontradas = filtradas
                else:
                    self.ordenes_encontradas = []
                
                self.busqueda_realizada = True
                if not self.ordenes_encontradas:
                    rx.toast.info("No encontramos ninguna orden con esos datos exactos.")
        except Exception as e:
            print(f"Error rastreando orden: {e}")
            self.busqueda_realizada = True
            rx.toast.error("Ocurrió un error al consultar el servidor.")

    # =========================================================================
    # 🧘‍♂️ LÓGICA DE RESERVA Y CONTROL DE PLAZAS DE SESIONES
    # =========================================================================
    def abrir_modal_reserva_sesion(self, sesion: dict):
        if sesion.get("plazas_disponibles", 0) <= 0:
            return rx.toast.error("Esta sesión se encuentra totalmente agotada.")
            
        self.sesion_seleccionada_reserva = sesion
        self.reserva_cantidad_cupos = 1
        self.reserva_porcentaje_pago = 0.0

        # Autocompletado si el usuario tiene sesión activa
        if self.user_logged_in:
            nom = self.usuario_datos.get("nombre", "")
            ape = self.usuario_datos.get("apellido", "")
            nombre_auto = f"{nom} {ape}".strip()
            self.reserva_nombre_cliente = nombre_auto
            self.reserva_email_cliente = self.usuario_datos.get("email", "")
            self.reserva_participantes = [nombre_auto]
        else:
            self.reserva_participantes = [""]
        self.reserva_porcentaje_pago = 0.0

        self.modal_reserva_sesion_abierto = True

    def cerrar_modal_reserva_sesion(self):
        self.modal_reserva_sesion_abierto = False
        self.reserva_nombre_cliente = ""
        self.reserva_email_cliente = ""
        self.reserva_whatsapp_cliente = ""
        self.reserva_cantidad_cupos = 1
        self.reserva_participantes = [""]

    def incrementar_cupos_reserva(self):
        max_disp = self.sesion_seleccionada_reserva.get("plazas_disponibles", 1)
        if self.reserva_cantidad_cupos < max_disp:
            self.reserva_cantidad_cupos += 1
            self.reserva_participantes.append("")
        else:
            rx.toast.warning(f"Límite alcanzado: solo quedan {max_disp} cupos disponibles.")

    def decrementar_cupos_reserva(self):
        if self.reserva_cantidad_cupos > 1:
            self.reserva_cantidad_cupos -= 1
            if len(self.reserva_participantes) > 1:
                self.reserva_participantes.pop()

    def confirmar_reserva_sesion(self):
        if not self.reserva_nombre_cliente.strip():
            return rx.toast.error("Por favor, ingresa tu Nombre y Apellido.")

        email_final = self.reserva_email_cliente.strip().lower() or (self.usuario_datos.get("email", "").lower() if self.user_logged_in else "")
        if not email_final or not self.validar_email_formato(email_final):
            return rx.toast.error("Ingresa un correo electrónico válido (ejemplo: nombre@dominio.com)")

        wa_clean = self.formatear_whatsapp_numero(self.reserva_whatsapp_cliente)
        if not wa_clean or len(wa_clean) < 10:
            return rx.toast.error("Ingresa un número de WhatsApp válido con el formato de tu país.")
        
        self.reserva_whatsapp_cliente = f"+{wa_clean}"

        sesion_id = self.sesion_seleccionada_reserva.get("id")
        cupos_reservar = self.reserva_cantidad_cupos
        monto_total = self.reserva_monto_total_calculado
        monto_pagado = self.reserva_monto_pagado_calculado
        monto_pendiente = self.reserva_monto_pendiente_calculado
        pct_pago = self.reserva_porcentaje_pago

        reserva_id_creada = None
        checkin_token_sesion = self.sesion_seleccionada_reserva.get("checkin_token", "")

        try:
            with rx.session() as session:
                db_session = session.get(TribuSession, sesion_id)
                if not db_session or not db_session.is_active:
                    return rx.toast.error("La sesión seleccionada ya no está disponible.")

                if db_session.plazas_disponibles < cupos_reservar:
                    return rx.toast.error(f"Lo sentimos, solo quedan {db_session.plazas_disponibles} cupos.")

                # Construir lista estructurada con nombres exactos de participantes
                lista_part_json = []
                nombres_participantes_lista = []
                for i in range(cupos_reservar):
                    p_nombre = self.reserva_participantes[i].strip() if i < len(self.reserva_participantes) else ""
                    if not p_nombre:
                        p_nombre = self.reserva_nombre_cliente.strip() if i == 0 else f"{self.reserva_nombre_cliente.strip()} (Acompañante {i+1})"
                    
                    lista_part_json.append({
                        "index": i,
                        "nombre": p_nombre,
                        "asistio": False
                    })
                    nombres_participantes_lista.append(p_nombre)

                # Estado inicial de la reserva: siempre entra como PENDIENTE_PAGO para auditoría del admin
                estado_res = "PENDIENTE_PAGO"

                nueva_reserva = TribuSessionReservation(
                 session_id=sesion_id,
                 nombre_cliente=self.reserva_nombre_cliente.strip(),
                 cliente_email=email_final,
                 whatsapp_cliente=self.reserva_whatsapp_cliente.strip(),
                 cupos=cupos_reservar,
                 monto_total=monto_total,
                 porcentaje_pago=pct_pago,
                 monto_pagado=monto_pagado,
                 monto_pendiente=monto_pendiente,
                 estado=estado_res,
                 asistio=False,
                 participantes_json=lista_part_json,
                 cupon_codigo=self.reserva_cupon_aplicado_codigo if self.reserva_cupon_aplicado_codigo else None,
                 fecha_evento=db_session.fecha_evento
             )
                session.add(nueva_reserva)

                # 🎟️ Sumar +1 uso al cupón y desactivarlo si llegó al límite
                if self.reserva_cupon_aplicado_codigo:
                    db_cupon = session.exec(
                        sqlmodel.select(TribuCoupon).where(
                            TribuCoupon.codigo == self.reserva_cupon_aplicado_codigo.strip().upper()
                        )
                    ).first()
                    if db_cupon:
                        db_cupon.usos_actuales += 1
                        if db_cupon.usos_actuales >= db_cupon.usos_maximos:
                            db_cupon.is_active = False
                        session.add(db_cupon)

                session.commit()
                session.refresh(nueva_reserva)
                reserva_id_creada = nueva_reserva.id

                # Limpiar variables temporales del cupón en el estado reactivo
                self.reserva_cupon_input = ""
                self.reserva_cupon_aplicado_codigo = ""
                self.reserva_descuento_monto = 0.0

        except Exception as e:
            print(f"Error registrando reserva en Supabase: {e}")
            return rx.toast.error("Ocurrió un error al registrar tu solicitud.")

        # 1. Construir desglose de participantes para el mensaje de WhatsApp
        texto_acompanantes = ""
        if len(nombres_participantes_lista) > 1:
            lineas_p = [f"   • {idx+1}. {nom}" for idx, nom in enumerate(nombres_participantes_lista)]
            texto_acompanantes = "\n *Lista de Participantes:*\n" + "\n".join(lineas_p)
        else:
            texto_acompanantes = f"\n *Participante Principal:* {nombres_participantes_lista[0]}"

        # 2. Resumen financiero de abono e importe pendiente
        if pct_pago == 0.0:
            texto_pago_resumen = (
                f" *Abono Inicial:* Por convenir / negociar vía WhatsApp\n"
                f" *Monto Total de la Sesión:* ${monto_total:.2f} USD"
            )
        elif pct_pago < 100.0:
            texto_pago_resumen = (
                f" *Abono Inicial ({pct_pago:.0f}%):* ${monto_pagado:.2f} USD\n"
                f" *Monto Pendiente en Puerta:* ${monto_pendiente:.2f} USD (Total: ${monto_total:.2f} USD)"
            )
        else:
            texto_pago_resumen = f" *Monto Total:* ${monto_total:.2f} USD (Pago 100%)"

        import urllib.parse
        NUMERO_TRIBU = "584241359530"
        
        nombre_sesion = self.sesion_seleccionada_reserva.get("nombre", "")
        fecha = self.sesion_seleccionada_reserva.get("fecha_texto", "")
        hora = self.sesion_seleccionada_reserva.get("hora_texto", "")
        ubicacion = self.sesion_seleccionada_reserva.get("ubicacion", "")

        mensaje = (
            f"¡Hola Tribu Sonora Consciente! ✨\n\n"
            f"Solicitud de Reserva Registrada:\n"
            f" *{nombre_sesion}*\n"
            f" *Lugar:* {ubicacion}\n"
            f" *Fecha:* {fecha} ({hora})\n"
            f" *Asistente Principal:* {self.reserva_nombre_cliente}\n"
            f"{texto_acompanantes}\n"
            f" *Contacto:* {self.reserva_whatsapp_cliente}\n"
            f" *Cupos solicitados:* {cupos_reservar}\n"
            f"{texto_pago_resumen}\n\n"
            f"Solicito los datos para realizar el pago y confirmar formalmente mis cupos. ¡Gracias!"
        )

        encoded_msg = urllib.parse.quote(mensaje)
        wa_url = f"https://wa.me/{NUMERO_TRIBU}?text={encoded_msg}"

        # 3. Enviar correo electrónico en segundo plano con Código QR de verificación
        if email_final and reserva_id_creada:
            qr_data = f"https://sound-healing-platform-neon-sun.reflex.run/asistencia/{checkin_token_sesion}?reserva={reserva_id_creada}"
            qr_image_url = f"https://api.qrserver.com/v1/create-qr-code/?size=250x250&data={urllib.parse.quote(qr_data)}"
            
            # Reutilizamos enviar_correo_voucher_html o función interna de notificación SMTP
            print(f"📧 Ticket QR generado para {email_final}: {qr_image_url}")

        self.cerrar_modal_reserva_sesion()
        self.crear_notificacion_db(
            titulo="🧘‍♀️ Nueva Reserva de Sesión",
            mensaje=f"Solicitud de {self.reserva_nombre_cliente} ({cupos_reservar} cupos, Pendiente: ${monto_pendiente:.2f}).",
            target_url="admin_tab_reservas",
            es_admin=True
        )
        yield rx.toast.success("¡Solicitud enviada con éxito! Redirigiendo a WhatsApp...")
        yield rx.redirect(wa_url, is_external=True)

    # =========================================================================
    # 📑 LÓGICA DE ASISTENCIA Y CHECK-IN POR TOKEN (DOCUMENTO COMPARTIBLE)
    # =========================================================================
    def abrir_lista_asistencia_admin(self, sesion: dict):
        """Redirige directamente al checklist de asistencia de la sesión seleccionada."""
        token = sesion.get("checkin_token", "")
        if not token:
            return rx.toast.error("Esta sesión aún no posee un token de asistencia generado.")
        return rx.redirect(f"/asistencia/{token}")

    def compartir_asistencia_whatsapp(self, sesion: dict):
        """Genera el enlace del checklist de asistencia y abre WhatsApp sin íconos ni emojis."""
        token = sesion.get("checkin_token", "")
        nombre_sesion = sesion.get("nombre", "")

        if not token:
            return rx.toast.error("Esta sesión aún no posee un token de asistencia generado.")

        # URL oficial del proyecto en producción
        BASE_URL = "https://sound-healing-platform-neon-sun.reflex.run"
        link_asistencia = f"{BASE_URL}/asistencia/{token}"

        # Estructura del texto limpia de íconos o emojis
        mensaje = f"Check List de asistencia a la session: {nombre_sesion}\n{link_asistencia}"

        import urllib.parse
        encoded_msg = urllib.parse.quote(mensaje)
        wa_url = f"https://api.whatsapp.com/send?text={encoded_msg}"

        return rx.redirect(wa_url, is_external=True)

    def cargar_lista_asistencia_por_token(self):
        self.cargando_asistencia = True
        token = self.router.page.params.get("token")
        if not token:
            self.cargando_asistencia = False
            return

        try:
            with rx.session() as session:
                db_session = session.exec(
                    sqlmodel.select(TribuSession).where(TribuSession.checkin_token == token)
                ).first()

                if not db_session:
                    self.sesion_asistencia_info = {}
                    self.lista_asistentes_sesion = []
                    self.fechas_historicas_sesion = []
                    return

                self.sesion_asistencia_info = {
                    "id": db_session.id,
                    "nombre": db_session.nombre,
                    "ubicacion": db_session.ubicacion,
                    "fecha_texto": db_session.fecha_texto,
                    "hora_texto": db_session.hora_texto,
                    "plazas_totales": db_session.plazas_totales,
                    "foto": db_session.foto
                }

                # Consulta de todas las fechas con reservas registradas para esta sesión
                todas_fechas_db = session.exec(
                    sqlmodel.select(TribuSessionReservation.fecha_evento)
                    .where(TribuSessionReservation.session_id == db_session.id)
                    .distinct()
                ).all()

                fechas_unicas = [f for f in todas_fechas_db if f]
                if db_session.fecha_evento and db_session.fecha_evento not in fechas_unicas:
                    fechas_unicas.append(db_session.fecha_evento)
                fechas_unicas.sort(reverse=True)
                self.fechas_historicas_sesion = fechas_unicas

                # Filtrar por la fecha seleccionada o por la fecha activa por defecto
                fecha_filtro = self.fecha_asistencia_seleccionada or db_session.fecha_evento

                reservas_db = session.exec(
                    sqlmodel.select(TribuSessionReservation)
                    .where(
                        TribuSessionReservation.session_id == db_session.id,
                        TribuSessionReservation.fecha_evento == fecha_filtro
                    )
                    .order_by(TribuSessionReservation.id.desc())
                ).all()

                asistentes_desglosados = []
                for r in reservas_db:
                    parts = r.participantes_json if isinstance(r.participantes_json, list) and len(r.participantes_json) > 0 else [{"index": 0, "nombre": r.nombre_cliente, "asistio": r.asistio}]
                    cant_cupos = max(1, r.cupos)
                    monto_pend_individual = float(getattr(r, "monto_pendiente", 0.0) / cant_cupos)

                    for p in parts:
                        asistentes_desglosados.append({
                            "id": f"{r.id}_{p.get('index', 0)}",
                            "reserva_id": r.id,
                            "part_index": p.get("index", 0),
                            "nombre_cliente": p.get("nombre", r.nombre_cliente),
                            "whatsapp_cliente": r.whatsapp_cliente,
                            "cupos": 1,
                            "monto_total": float(r.monto_total / cant_cupos),
                            "monto_pendiente": monto_pend_individual,
                            "porcentaje_pago": float(getattr(r, "porcentaje_pago", 100.0)),
                            "estado": r.estado,
                            "asistio": p.get("asistio", False),
                            "metodo_pago": getattr(r, "metodo_pago", "") or ""
                        })

                self.lista_asistentes_sesion = asistentes_desglosados

        except Exception as e:
            print(f"Error cargando lista de asistencia por token: {e}")
        finally:
            self.cargando_asistencia = False

    def toggle_asistencia_participante(self, item_id: str):
        """Alterna asistencia individual, liquide deuda al 100% si se seleccionó método de pago y persiste en Supabase."""
        from sqlalchemy.orm.attributes import flag_modified
        try:
            parts_keys = str(item_id).split("_")
            reserva_id = int(parts_keys[0])
            part_index = int(parts_keys[1]) if len(parts_keys) > 1 else 0
            metodo_pago = next((a.get("metodo_pago", "") for a in self.lista_asistentes_sesion if a["id"] == item_id), "")

            with rx.session() as session:
                reserva = session.get(TribuSessionReservation, reserva_id)
                if reserva:
                    parts = list(reserva.participantes_json) if isinstance(reserva.participantes_json, list) else []
                    if not parts:
                        parts = [{"index": 0, "nombre": reserva.nombre_cliente, "asistio": reserva.asistio}]

                    nombre_toast = reserva.nombre_cliente
                    nuevo_estado = False

                    for p in parts:
                        if p.get("index", 0) == part_index:
                            p["asistio"] = not p.get("asistio", False)
                            nuevo_estado = p["asistio"]
                            nombre_toast = p.get("nombre", reserva.nombre_cliente)
                            break

                    reserva.participantes_json = list(parts)
                    reserva.asistio = all(p.get("asistio", False) for p in parts)

                    # Si el participante tenía deuda y se seleccionó un método de pago en puerta
                    m_total = float(reserva.monto_total)
                    m_pend = float(getattr(reserva, "monto_pendiente", 0.0))
                    pago_registrado = False

                    if nuevo_estado and m_pend > 0 and metodo_pago:
                        reserva.porcentaje_pago = 100.0
                        reserva.monto_pagado = m_total
                        reserva.monto_pendiente = 0.0
                        reserva.estado = "CONFIRMADO"
                        reserva.metodo_pago = metodo_pago.upper()
                        pago_registrado = True

                    flag_modified(reserva, "participantes_json")
                    flag_modified(reserva, "asistio")

                    session.add(reserva)
                    session.commit()

                    # Actualización síncrona de todas las tarjetas asociadas a esta reserva
                    for a in self.lista_asistentes_sesion:
                        if a["reserva_id"] == reserva_id and pago_registrado:
                            a["porcentaje_pago"] = 100.0
                            a["monto_pendiente"] = 0.0
                            a["estado"] = "CONFIRMADO"
                        if a["id"] == item_id:
                            a["asistio"] = nuevo_estado

                    if pago_registrado:
                        rx.toast.success(f"💳 Pago del 100% registrado vía {metodo_pago.upper()} para {reserva.nombre_cliente}")

                    pend_actual = 0.0 if pago_registrado else m_pend
                    if nuevo_estado and pend_actual > 0:
                        return rx.toast.warning(f"⚠️ {nombre_toast} ingresó pero TIENE PAGO PENDIENTE de ${pend_actual:.2f} USD")
                    
                    estado_txt = "marcado como presente 🟢" if nuevo_estado else "desmarcado ⚪"
                    return rx.toast.info(f"{nombre_toast} {estado_txt}")
        except Exception as e:
            print(f"Error actualizando asistencia individual en Supabase: {e}")
            return rx.toast.error("Ocurrió un error al guardar la asistencia en el servidor.")
        
    # =========================================================================
    # 🔐 PANEL DE ADMINISTRACIÓN Y CONTROL DE RESERVAS
    # =========================================================================
    admin_logged_in: bool = False
    admin_email_input: str = ""
    admin_pass_input: str = ""
    admin_tab_activa: str = "reservas"  # 'reservas', 'sesiones', 'productos'

    # 🎟️ Variables y Métodos CRUD de Cupones Administrables
    cupones_admin_list: list[dict[str, Any]] = []
    edit_cupon_codigo: str = ""
    edit_cupon_tipo: str = "PORCENTAJE"  # 'PORCENTAJE' o 'FIJO'
    edit_cupon_valor: float = 0.0
    edit_cupon_usos_maximos: int = 1

    def set_edit_cupon_codigo(self, val: str):
        self.edit_cupon_codigo = val.upper()

    def set_edit_cupon_tipo(self, val: str):
        self.edit_cupon_tipo = val

    def set_edit_cupon_valor(self, val: str):
        try:
            self.edit_cupon_valor = float(val) if val else 0.0
        except ValueError:
            pass

    def set_edit_cupon_usos_maximos(self, val: str):
        try:
            self.edit_cupon_usos_maximos = int(val) if val else 1
        except ValueError:
            pass

    def crear_cupon_especial_admin(self):
        """Crea cupones negociados o promocionales directamente en la BD."""
        cod = self.edit_cupon_codigo.strip().upper()
        if not cod or self.edit_cupon_valor <= 0:
            return rx.toast.error("Ingresa un código válido y un valor mayor a 0.")

        try:
            with rx.session() as session:
                nuevo = TribuCoupon(
                    codigo=cod,
                    tipo=self.edit_cupon_tipo,
                    valor=self.edit_cupon_valor,
                    usos_maximos=self.edit_cupon_usos_maximos,
                    is_active=True
                )
                session.add(nuevo)
                session.commit()
                self.edit_cupon_codigo = ""
                self.edit_cupon_valor = 0.0
                self.cargar_datos_admin()
                return rx.toast.success(f"¡Cupón {cod} creado exitosamente!")
        except Exception as e:
            print(f"Error al crear cupón: {e}")
            return rx.toast.error("El código ya existe o falló la conexión.")

    def toggle_estado_cupon_admin(self, cupon_id: int):
        """Activa o desactiva un cupón desde el panel admin."""
        try:
            with rx.session() as session:
                c = session.get(TribuCoupon, cupon_id)
                if c:
                    c.is_active = not c.is_active
                    session.add(c)
                    session.commit()
                    self.cargar_datos_admin()
                    return rx.toast.info("Estado del cupón actualizado.")
        except Exception as e:
            print(f"Error en toggle cupon: {e}")

    # Variables de Formulario CRUD para Sesiones Grupales
    modal_editor_sesion_abierto: bool = False
    sesion_id_edicion: int | None = None
    edit_sesion_nombre: str = ""
    edit_sesion_patron_recurrencia: str = "MANUAL"
    edit_sesion_foto: str = ""
    edit_sesion_ubicacion: str = ""
    edit_sesion_frecuencia: str = ""
    edit_sesion_fecha: str = ""
    edit_sesion_hora: str = ""
    edit_sesion_hora_recepcion: str = ""
    edit_sesion_inversion: float = 0.0
    edit_sesion_plazas_totales: int = 15
    edit_sesion_plazas_disponibles: int = 15
    edit_sesion_instagram: str = ""
    edit_sesion_recomendaciones: str = ""

    # Variables de Formulario CRUD para Productos y Stock
    modal_editor_producto_abierto: bool = False
    def set_modal_editor_producto_abierto(self, val: bool):
        self.modal_editor_producto_abierto = val

    def set_modal_editor_taller_abierto(self, val: bool):
        self.modal_editor_taller_abierto = val

    def set_modal_editor_servicio_abierto(self, val: bool):
        self.modal_editor_servicio_abierto = val
    producto_id_edicion: int | None = None
    edit_prod_nombre: str = ""
    edit_prod_proveedor: str = ""
    edit_prod_descripcion: str = ""
    edit_prod_precio: float = 0.0
    edit_prod_stock: int = 0
    edit_prod_categoria: str = "Cuencos"
    edit_prod_intencion: str = ""
    edit_prod_foto: str = ""
    edit_prod_fotos: list[str] = []
    edit_prod_is_best_seller: bool = False
    edit_prod_is_favorite: bool = False

    def set_edit_prod_nombre(self, val: str): self.edit_prod_nombre = val
    def set_edit_prod_proveedor(self, val: str): self.edit_prod_proveedor = val
    def set_edit_prod_intencion(self, val: str): 
        self.edit_prod_intencion = "" if val == "Ninguna" else val
    def set_edit_prod_descripcion(self, val: str): self.edit_prod_descripcion = val
    def set_edit_prod_precio(self, val: str):
        try:
            self.edit_prod_precio = float(val) if val != "" else 0.0
        except ValueError:
            pass
    def set_edit_prod_stock(self, val: str):
        try:
            self.edit_prod_stock = int(val) if val != "" else 0
        except ValueError:
            pass
    def set_edit_prod_categoria(self, val: str): self.edit_prod_categoria = val
    def set_edit_prod_foto(self, val: str): self.edit_prod_foto = val
    def set_edit_prod_is_best_seller(self, val: bool): self.edit_prod_is_best_seller = val

    def agregar_url_foto_manual(self):
        """Añade una URL ingresada manualmente a la lista de fotos del producto."""
        if self.edit_prod_foto.strip():
            url = self.edit_prod_foto.strip()
            if url not in self.edit_prod_fotos:
                self.edit_prod_fotos.append(url)
            self.edit_prod_foto = ""
            return rx.toast.info("URL agregada a la galería del producto.")

    def eliminar_foto_producto(self, url: str):
        """Remueve una foto específica de la lista."""
        self.edit_prod_fotos = [f for f in self.edit_prod_fotos if f != url]
        return rx.toast.info("Foto removida de la lista.")
    def set_edit_prod_is_favorite(self, val: bool): self.edit_prod_is_favorite = val
    # Variables de Formulario CRUD para Talleres y Eventos
    modal_editor_taller_abierto: bool = False
    taller_id_edicion: int | None = None
    edit_taller_titulo: str = ""
    edit_taller_tipo: str = "Taller"
    edit_taller_foto: str = ""
    edit_taller_facilitador: str = "Tribu Sonora Consciente"
    edit_taller_descripcion: str = ""
    edit_taller_fecha_texto: str = ""
    edit_taller_hora_texto: str = ""
    edit_taller_duracion_texto: str = "2 horas"
    edit_taller_ubicacion: str = ""
    edit_taller_precio: float = 0.0
    edit_taller_moneda: str = "USD"
    edit_taller_fecha_evento: str = ""
    edit_taller_whatsapp: str = ""

    def set_edit_taller_titulo(self, val: str): self.edit_taller_titulo = val
    def set_edit_taller_tipo(self, val: str): self.edit_taller_tipo = val
    def set_edit_taller_foto(self, val: str): self.edit_taller_foto = val
    def set_edit_taller_facilitador(self, val: str): self.edit_taller_facilitador = val
    def set_edit_taller_descripcion(self, val: str): self.edit_taller_descripcion = val
    def set_edit_taller_fecha_texto(self, val: str): self.edit_taller_fecha_texto = val
    def set_edit_taller_hora_texto(self, val: str): self.edit_taller_hora_texto = val
    def set_edit_taller_duracion_texto(self, val: str): self.edit_taller_duracion_texto = val
    def set_edit_taller_ubicacion(self, val: str): self.edit_taller_ubicacion = val
    def set_edit_taller_precio(self, val: str):
        try:
            self.edit_taller_precio = float(val) if val != "" else 0.0
        except ValueError:
            pass
    def set_edit_taller_moneda(self, val: str): self.edit_taller_moneda = val
    def set_edit_taller_fecha_evento(self, val: str): self.edit_taller_fecha_evento = val
    def set_edit_taller_whatsapp(self, val: str): self.edit_taller_whatsapp = val
    # Variables de Formulario CRUD para Servicios
    modal_editor_servicio_abierto: bool = False
    servicio_id_edicion: int | None = None
    edit_servicio_nombre: str = ""
    edit_servicio_foto: str = ""
    edit_servicio_descripcion: str = ""

    def set_edit_servicio_nombre(self, val: str): self.edit_servicio_nombre = val
    def set_edit_servicio_foto(self, val: str): self.edit_servicio_foto = val
    def set_edit_servicio_descripcion(self, val: str): self.edit_servicio_descripcion = val
    def set_edit_sesion_nombre(self, val: str): self.edit_sesion_nombre = val
    def set_edit_sesion_patron_recurrencia(self, val: str): self.edit_sesion_patron_recurrencia = val
    def set_edit_sesion_foto(self, val: str): self.edit_sesion_foto = val
    def set_edit_sesion_ubicacion(self, val: str): self.edit_sesion_ubicacion = val
    def set_edit_sesion_frecuencia(self, val: str): self.edit_sesion_frecuencia = val
    def set_edit_sesion_fecha(self, val: str): self.edit_sesion_fecha = val
    def set_edit_sesion_hora(self, val: str): self.edit_sesion_hora = val
    def set_edit_sesion_hora_recepcion(self, val: str): self.edit_sesion_hora_recepcion = val
    def set_edit_sesion_inversion(self, val: str):
        try:
            self.edit_sesion_inversion = float(val) if val and str(val).strip() else 0.0
        except ValueError:
            self.edit_sesion_inversion = 0.0

    def set_edit_sesion_plazas_totales(self, val: str):
        try:
            self.edit_sesion_plazas_totales = int(val) if val and str(val).strip() else 0
        except ValueError:
            self.edit_sesion_plazas_totales = 0
    def set_edit_sesion_plazas_disponibles(self, val: int): self.edit_sesion_plazas_disponibles = val
    def set_edit_sesion_instagram(self, val: str): self.edit_sesion_instagram = val
    def set_edit_sesion_recomendaciones(self, val: str): self.edit_sesion_recomendaciones = val

    @rx.var
    def lista_patrones_recurrencia_disponibles(self) -> list[str]:
        """Genera dinámicamente las combinaciones posibles de días de la semana y órdenes."""
        ordenes = ["PRIMER", "SEGUNDO", "TERCER", "CUARTO", "ULTIMO"]
        dias = ["LUNES", "MARTES", "MIERCOLES", "JUEVES", "VIERNES", "SABADO", "DOMINGO"]
        opciones = ["MANUAL"]
        for d in dias:
            for o in ordenes:
                opciones.append(f"{o}_{d}")
        return opciones

    # Listas registradas para el administrador
    reservas_admin_list: list[dict[str, Any]] = []
    ordenes_admin_list: list[dict[str, Any]] = []
    sesiones_admin_list: list[dict[str, Any]] = []

    def set_admin_email(self, val: str):
        self.admin_email_input = val

    def set_admin_pass(self, val: str):
        self.admin_pass_input = val

    def set_admin_tab(self, tab: str):
        self.admin_tab_activa = tab

    def login_admin(self):
        # Credenciales maestras de desarrollo/administración
        if self.admin_email_input.strip() == "admin@tribusonora.com" and self.admin_pass_input.strip() == "tribu369":
            self.admin_logged_in = True
            self.admin_pass_input = ""
            rx.toast.success("Bienvenido al Panel Administrador")
            return self.cargar_datos_admin()
        else:
            return rx.toast.error("Credenciales incorrectas")

    
    def cargar_datos_admin(self):
        try:
            with rx.session() as session:
                # 1. Cargar reservas de sesiones
                query_res = sa.text("""
                    SELECT r.id, r.session_id, r.nombre_cliente, r.whatsapp_cliente, 
                           r.cupos, r.monto_total, r.estado, r.asistio, s.nombre as sesion_nombre, s.fecha_texto,
                           COALESCE(r.porcentaje_pago, 100.0) as porcentaje_pago,
                           COALESCE(r.monto_pagado, r.monto_total) as monto_pagado,
                           COALESCE(r.monto_pendiente, 0.0) as monto_pendiente,
                           r.fecha_evento
                    FROM tribu_session_reservations r
                    JOIN tribu_sessions s ON r.session_id = s.id
                    ORDER BY r.id DESC
                """)
                res = session.execute(query_res).fetchall()
                self.reservas_admin_list = [
                    {
                        "id": row[0],
                        "session_id": row[1],
                        "nombre_cliente": row[2],
                        "whatsapp_cliente": row[3],
                        "cupos": row[4],
                        "monto_total": float(row[5]),
                        "estado": row[6],
                        "asistio": row[7],
                        "sesion_nombre": row[8],
                        "fecha_texto": row[9],
                        "porcentaje_pago": float(row[10]),
                        "monto_pagado": float(row[11]),
                        "monto_pendiente": float(row[12]),
                        "fecha_evento": row[13] or row[9]
                    }
                    for row in res
                ]

                # 2. Cargar órdenes de productos y vouchers
                query_ord = sa.text("""
                    SELECT id, numero_referencia, cliente_nombre, cliente_apellido, cliente_email,
                           cliente_telefono, monto_total, metodo_pago, estado, comprobante_url, items_json
                    FROM tribu_orders
                    ORDER BY id DESC
                """)
                res_ord = session.execute(query_ord).fetchall()
                import json
                self.ordenes_admin_list = [
                    {
                        "id": row[0],
                        "referencia": row[1],
                        "cliente_nombre": f"{row[2]} {row[3]}".strip(),
                        "cliente_email": row[4],
                        "cliente_telefono": row[5],
                        "monto_total": float(row[6]),
                        "metodo_pago": str(row[7]).replace("_", " ").title(),
                        "estado": row[8],
                        "comprobante_url": row[9] or "",
                        "items": json.loads(row[10]) if isinstance(row[10], str) else (row[10] or [])
                    }
                    for row in res_ord
                ]

                # 3. Cargar sesiones grupales ordenadas por fecha próxima
                db_sessions_admin = session.exec(
                    sqlmodel.select(TribuSession)
                ).all()
                db_sessions_admin.sort(key=lambda x: x.fecha_evento or "9999-12-31")
                self.sesiones_admin_list = [
                    {
                        "id": s.id,
                        "nombre": s.nombre,
                        "foto": s.foto,
                        "ubicacion": s.ubicacion,
                        "frecuencia_texto": s.frecuencia_texto,
                        "fecha_texto": s.fecha_texto,
                        "hora_texto": s.hora_texto,
                        "hora_recepcion_texto": s.hora_recepcion_texto or "",
                        "inversion": float(s.inversion),
                        "plazas_totales": s.plazas_totales,
                        "plazas_disponibles": s.plazas_disponibles,
                        "instagram_url": s.instagram_url,
                        "recomendaciones": s.recomendaciones,
                        "checkin_token": s.checkin_token or "",
                        "is_active": s.is_active
                    }
                    for s in db_sessions_admin
                ]

                # 4. Cargar cupones de descuento
                cupones_db = session.exec(sqlmodel.select(TribuCoupon)).all()
                self.cupones_admin_list = [
                    {
                        "id": c.id,
                        "codigo": c.codigo,
                        "tipo": c.tipo,
                        "valor": c.valor,
                        "is_active": c.is_active,
                        "usos_maximos": c.usos_maximos,
                        "usos_actuales": c.usos_actuales,
                        "agotado": c.usos_actuales >= c.usos_maximos
                    }
                    for c in cupones_db
                ]
        except Exception as e:
            print(f"Error cargando datos admin: {e}")
    def cambiar_porcentaje_reserva_admin(self, reserva_id: int, nuevo_pct: float):
        """Permite al administrador cambiar el % reservado desde el panel y recalculación de montos."""
        try:
            with rx.session() as session:
                reserva = session.get(TribuSessionReservation, reserva_id)
                if reserva:
                    pct = float(nuevo_pct)
                    m_total = float(reserva.monto_total)
                    m_pagado = round(m_total * (pct / 100.0), 2)
                    m_pend = round(m_total - m_pagado, 2)

                    reserva.porcentaje_pago = pct
                    reserva.monto_pagado = m_pagado
                    reserva.monto_pendiente = m_pend

                    session.add(reserva)
                    session.commit()

                    self.cargar_datos_admin()
                    self.cargar_lista_asistencia_por_token()
                    return rx.toast.success(f"Reserva de {reserva.nombre_cliente} actualizada a {pct:.0f}% (Pendiente: ${m_pend:.2f} USD)")
        except Exception as e:
            print(f"Error cambiando porcentaje de reserva admin: {e}")
            return rx.toast.error("Error al actualizar el porcentaje de la reserva.")
        
    def aprobar_reserva_sesion(self, reserva_id: int):
        """Aprueba el pago, marca como CONFIRMADO y descuenta definitivamente los cupos."""
        try:
            with rx.session() as session:
                reserva = session.get(TribuSessionReservation, reserva_id)
                if not reserva:
                    return rx.toast.error("Reserva no encontrada.")

                if reserva.estado == "CONFIRMADO":
                    return rx.toast.info("Esta reserva ya se encuentra confirmada.")

                db_session = session.get(TribuSession, reserva.session_id)
                if not db_session:
                    return rx.toast.error("Sesión asociada no encontrada.")

                if db_session.plazas_disponibles < reserva.cupos:
                    return rx.toast.error(f"No hay suficientes cupos disponibles ({db_session.plazas_disponibles} restantes).")

                # Desactivar cupón si alcanzó el máximo de usos al ser aprobado
                if reserva.cupon_codigo:
                    db_cupon = session.exec(
                        sqlmodel.select(TribuCoupon).where(TribuCoupon.codigo == reserva.cupon_codigo)
                    ).first()
                    if db_cupon and db_cupon.usos_actuales >= db_cupon.usos_maximos:
                        db_cupon.is_active = False
                        session.add(db_cupon)

                # Actualizar estado de la reserva y descontar plazas
                reserva.estado = "CONFIRMADO"
                db_session.plazas_disponibles -= reserva.cupos

                session.add(reserva)
                session.add(db_session)
                session.commit()

                self.cargar_datos_admin()
                self.cargar_datos_db()

                # Cargar lista de cupones
                cupones_db = session.exec(sqlmodel.select(TribuCoupon)).all()
                self.cupones_admin_list = [
                    {
                        "id": c.id,
                        "codigo": c.codigo,
                        "tipo": c.tipo,
                        "valor": c.valor,
                        "is_active": c.is_active,
                        "usos_maximos": c.usos_maximos,
                        "usos_actuales": c.usos_actuales,
                        "agotado": c.usos_actuales >= c.usos_maximos
                    }
                    for c in cupones_db
                ]

                # Notificación estructurada con formato dinámico para WhatsApp
                num_wa = "".join(filter(str.isdigit, reserva.whatsapp_cliente))
                cupos_txt = f"{reserva.cupos} cupo" if reserva.cupos == 1 else f"{reserva.cupos} cupos"

                # Formateo dinámico de hora de recepción y montos
                hora_recepcion = db_session.hora_recepcion_texto or ""
                if hora_recepcion and "recepción" not in hora_recepcion.lower():
                    hora_recepcion_str = f"Hora de recepción: {hora_recepcion}"
                else:
                    hora_recepcion_str = hora_recepcion or "Hora de recepción: Por confirmar"

                m_pagado_num = float(reserva.monto_pagado)
                m_pend_num = float(reserva.monto_pendiente)
                m_pagado = f"{int(m_pagado_num)}" if m_pagado_num.is_integer() else f"{m_pagado_num:.2f}"
                m_pend = f"{int(m_pend_num)}" if m_pend_num.is_integer() else f"{m_pend_num:.2f}"
                metodo_txt = f" ({reserva.metodo_pago.upper()})" if getattr(reserva, "metodo_pago", None) else ""

                mensaje = (
                    f"Hola {reserva.nombre_cliente}. El pago ha sido verificado con exito. "
                    f"Tu reserva para la sesion '{db_session.nombre}' ha sido CONFIRMADA ({cupos_txt}). "
                    f"Te esperamos en la fecha pautada ({db_session.fecha_texto}), {hora_recepcion_str}. "
                    f"Iniciamos a las ({db_session.hora_texto}).\n\n"
                    f" *Abono Inicial ({reserva.porcentaje_pago:.0f}%): ${m_pagado}{metodo_txt} ,  Monto Pendiente en Puerta: (${m_pend})* "
                    f"Muchas gracias por ser parte de la Tribu.\n"
                    f"Estamos emocionados de reencontrarnos"
                )

                import urllib.parse
                encoded = urllib.parse.quote(mensaje)
                wa_url = f"https://wa.me/{num_wa}?text={encoded}" if num_wa else ""

                yield rx.toast.success("Reserva APROBADA y cupos descontados con éxito.")
                if wa_url:
                    yield rx.redirect(wa_url, is_external=True)

        except Exception as e:
            print(f"Error aprobando reserva: {e}")
            yield rx.toast.error("Error al procesar la aprobación.")

    def rechazar_reserva_sesion(self, reserva_id: int):
        """Marca una reserva como RECHAZADO sin alterar inventario de cupos."""
        try:
            with rx.session() as session:
                reserva = session.get(TribuSessionReservation, reserva_id)
                if reserva:
                    reserva.estado = "RECHAZADO"
                    session.add(reserva)
                    session.commit()
                    self.cargar_datos_admin()
                    return rx.toast.info(f"Reserva de {reserva.nombre_cliente} cancelada/rechazada.")
        except Exception as e:
            print(f"Error rechazando reserva: {e}")
            return rx.toast.error("Error al rechazar la reserva.")

    def aprobar_orden_producto(self, orden_id: int):
        """Aprueba pedido, descuenta stock, activa Gift Cards y dispara notificación y correo."""
        try:
            with rx.session() as session:
                query = sa.text("SELECT id, cliente_email, items_json, estado FROM tribu_orders WHERE id = :id")
                ord_db = session.execute(query, {"id": orden_id}).fetchone()

                if not ord_db:
                    return rx.toast.error("Pedido no encontrado.")

                if ord_db[3] == "COMPLETADO":
                    return rx.toast.info("Este pedido ya fue confirmado previamente.")

                import json
                items = json.loads(ord_db[2]) if isinstance(ord_db[2], str) else (ord_db[2] or [])
                u_email = ord_db[1]

                # Descontar stock de productos físicos
                for item in items:
                    p_id = item.get("id")
                    cant = int(item.get("cantidad", 1))
                    if p_id and p_id != 9999:
                        db_p = session.get(TribuProduct, p_id)
                        if db_p:
                            db_p.stock = max(0, db_p.stock - cant)
                            session.add(db_p)

                # Activar Tarjetas de Regalo y enviar email
                vouchers = session.exec(
                    sqlmodel.select(TribuGiftCard).where(
                        TribuGiftCard.comprador_email == u_email,
                        TribuGiftCard.estado == "PENDIENTE_PAGO"
                    )
                ).all()

                for gc in vouchers:
                    gc.estado = "ACTIVA"
                    session.add(gc)
                    target_email = gc.destinatario_email or gc.comprador_email
                    self.enviar_correo_voucher_html(
                        destinatario_email=target_email,
                        destinatario_nombre=gc.destinatario_nombre,
                        comprador_nombre=gc.comprador_nombre,
                        experiencia_nombre=gc.experiencia_nombre,
                        codigo_voucher=gc.codigo,
                        mensaje_personal=gc.mensaje_personalizado
                    )

                # Consumir / Invalidar cupón usado en el pedido
                query_cupon = sa.text("SELECT cupon_codigo FROM tribu_orders WHERE id = :id")
                res_c = session.execute(query_cupon, {"id": orden_id}).fetchone()
                if res_c and res_c[0]:
                    cod_usado = res_c[0]
                    db_cupon = session.exec(
                        sqlmodel.select(TribuCoupon).where(TribuCoupon.codigo == cod_usado)
                    ).first()
                    if db_cupon:
                        db_cupon.usos_actuales += 1
                        if db_cupon.usos_actuales >= db_cupon.usos_maximos:
                            db_cupon.is_active = False
                        session.add(db_cupon)

                session.execute(
                    sa.text("UPDATE tribu_orders SET estado = 'COMPLETADO' WHERE id = :id"),
                    {"id": orden_id}
                )
                session.commit()

                # Notificación privada para la cuenta del cliente
                self.crear_notificacion_db(
                    titulo="¡Tu compra ha sido aprobada! 📦",
                    mensaje="Tu pedido ha sido verificado con éxito. Revisa tus detalles en 'Mi Cuenta Tribu'.",
                    target_url="/login",
                    destinatario_email=u_email
                )

                self.cargar_datos_admin()
                self.cargar_datos_db()
                return rx.toast.success("Pedido APROBADO: Stock descontado y Vouchers activados.")
        except Exception as e:
            print(f"Error aprobando orden: {e}")
            return rx.toast.error("Ocurrió un error al aprobar el pedido.")

    def rechazar_orden_producto(self, orden_id: int):
        """Rechaza un pedido y notifica al cliente."""
        try:
            with rx.session() as session:
                query = sa.text("SELECT id, cliente_email FROM tribu_orders WHERE id = :id")
                ord_db = session.execute(query, {"id": orden_id}).fetchone()

                if ord_db:
                    session.execute(
                        sa.text("UPDATE tribu_orders SET estado = 'RECHAZADO' WHERE id = :id"),
                        {"id": orden_id}
                    )
                    session.commit()

                    self.crear_notificacion_db(
                        titulo="Actualización de tu pedido ⚠️",
                        mensaje="Tu pago no pudo ser verificado. Por favor contacta soporte vía WhatsApp.",
                        target_url="/login",
                        destinatario_email=ord_db[1]
                    )

                    self.cargar_datos_admin()
                    return rx.toast.info("Pedido marcado como RECHAZADO.")
        except Exception as e:
            print(f"Error rechazando orden: {e}")
            return rx.toast.error("Error al rechazar el pedido.")
        

    # -------------------------------------------------------------------------
    # 📝 MÉTODOS CRUD DE SESIONES GRUPALES PARA ADMINISTRADOR
    # -------------------------------------------------------------------------
    def calcular_proxima_fecha_recurrente(self, patron: str, fecha_ref=None):
        """Calcula dinámicamente cualquier patrón ORDEN_DIA (ej. PRIMER_LUNES, ULTIMO_VIERNES)."""
        import calendar
        from datetime import date, timedelta

        if not patron or patron == "MANUAL" or "_" not in patron:
            return None

        if fecha_ref is None:
            fecha_ref = date.today()

        partes = patron.upper().split("_")
        if len(partes) != 2:
            return None

        orden, dia_nombre = partes[0], partes[1]

        dias_map = {
            "LUNES": 0, "MARTES": 1, "MIERCOLES": 2, "JUEVES": 3,
            "VIERNES": 4, "SABADO": 5, "DOMINGO": 6
        }
        if dia_nombre not in dias_map:
            return None

        target_weekday = dias_map[dia_nombre]

        def obtener_fecha_mes(year: int, month: int):
            primer_dia = date(year, month, 1)
            dias_hasta_target = (target_weekday - primer_dia.weekday()) % 7
            primer_target = primer_dia + timedelta(days=dias_hasta_target)

            if orden == "PRIMER":
                return primer_target
            elif orden == "SEGUNDO":
                return primer_target + timedelta(days=7)
            elif orden == "TERCER":
                return primer_target + timedelta(days=14)
            elif orden == "CUARTO":
                return primer_target + timedelta(days=21)
            elif orden == "ULTIMO":
                num_dias = calendar.monthrange(year, month)[1]
                ultimo_dia = date(year, month, num_dias)
                dias_atras = (ultimo_dia.weekday() - target_weekday) % 7
                return ultimo_dia - timedelta(days=dias_atras)
            return None

        candidata = obtener_fecha_mes(fecha_ref.year, fecha_ref.month)
        if candidata and candidata >= fecha_ref:
            return candidata

        sig_year = fecha_ref.year + 1 if fecha_ref.month == 12 else fecha_ref.year
        sig_month = 1 if fecha_ref.month == 12 else fecha_ref.month + 1
        return obtener_fecha_mes(sig_year, sig_month)

    def abrir_modal_nueva_sesion(self):
        """Abre el modal limpio para crear una nueva sesión grupal."""
        self.sesion_id_edicion = None
        self.edit_sesion_nombre = ""
        self.edit_sesion_patron_recurrencia = "MANUAL"
        self.edit_sesion_foto = "/Galeria_foto1.jpg"
        self.edit_sesion_ubicacion = ""
        self.edit_sesion_frecuencia = "Todos los Jueves"
        self.edit_sesion_fecha = ""
        self.edit_sesion_hora = "6:00 PM a 7:00 PM"
        self.edit_sesion_hora_recepcion = "5:00 PM"
        self.edit_sesion_inversion = 20.0
        self.edit_sesion_plazas_totales = 15
        self.edit_sesion_plazas_disponibles = 15
        self.edit_sesion_instagram = ""
        self.edit_sesion_recomendaciones = "Traer ropa cómoda, hidratación y mat de yoga o manta."
        self.modal_editor_sesion_abierto = True

    def abrir_modal_editar_sesion(self, sesion: dict):
        """Carga los datos de una sesión existente para editarla."""
        self.sesion_id_edicion = sesion.get("id")
        self.edit_sesion_nombre = sesion.get("nombre", "")
        self.edit_sesion_patron_recurrencia = sesion.get("patron_recurrencia", "MANUAL")
        self.edit_sesion_foto = sesion.get("foto", "")
        self.edit_sesion_ubicacion = sesion.get("ubicacion", "")
        self.edit_sesion_frecuencia = sesion.get("frecuencia_texto", "")
        self.edit_sesion_fecha = sesion.get("fecha_texto", "")
        self.edit_sesion_hora = sesion.get("hora_texto", "")
        self.edit_sesion_hora_recepcion = sesion.get("hora_recepcion_texto", "5:00 PM")
        self.edit_sesion_inversion = float(sesion.get("inversion", 0.0))
        self.edit_sesion_plazas_totales = int(sesion.get("plazas_totales", 15))
        self.edit_sesion_plazas_disponibles = int(sesion.get("plazas_disponibles", 15))
        self.edit_sesion_instagram = sesion.get("instagram_url", "")
        self.edit_sesion_recomendaciones = sesion.get("recomendaciones", "")
        self.modal_editor_sesion_abierto = True

    def set_modal_editor_sesion_abierto(self, val: bool):
        self.modal_editor_sesion_abierto = val

    def cerrar_modal_editor_sesion(self):
        self.modal_editor_sesion_abierto = False

    def guardar_sesion_db(self):
        """Guarda o actualiza la sesión en Supabase con auto-cálculo de fecha si aplica."""
        if not self.edit_sesion_nombre.strip() or not self.edit_sesion_ubicacion.strip():
            return rx.toast.error("Por favor completa el Nombre y la Ubicación de la sesión.")

        import uuid
        fecha_ev = None
        if self.edit_sesion_patron_recurrencia != "MANUAL":
            proxima = self.calcular_proxima_fecha_recurrente(self.edit_sesion_patron_recurrencia)
            if proxima:
                fecha_ev = str(proxima)
                if not self.edit_sesion_fecha.strip():
                    self.edit_sesion_fecha = proxima.strftime("%d/%m/%Y")

        try:
            with rx.session() as session:
                if self.sesion_id_edicion:
                    db_sesion = session.get(TribuSession, self.sesion_id_edicion)
                    if db_sesion:
                        db_sesion.nombre = self.edit_sesion_nombre.strip()
                        db_sesion.patron_recurrencia = self.edit_sesion_patron_recurrencia
                        db_sesion.foto = self.edit_sesion_foto.strip()
                        db_sesion.ubicacion = self.edit_sesion_ubicacion.strip()
                        db_sesion.frecuencia_texto = self.edit_sesion_frecuencia.strip()
                        db_sesion.fecha_texto = self.edit_sesion_fecha.strip()
                        db_sesion.fecha_evento = fecha_ev or db_sesion.fecha_evento
                        db_sesion.hora_texto = self.edit_sesion_hora.strip()
                        db_sesion.hora_recepcion_texto = self.edit_sesion_hora_recepcion.strip()
                        db_sesion.inversion = self.edit_sesion_inversion
                        db_sesion.plazas_totales = self.edit_sesion_plazas_totales
                        db_sesion.plazas_disponibles = self.edit_sesion_plazas_disponibles
                        db_sesion.instagram_url = self.edit_sesion_instagram.strip()
                        db_sesion.recomendaciones = self.edit_sesion_recomendaciones.strip()
                        session.add(db_sesion)
                        rx.toast.success("Sesión actualizada exitosamente.")
                else:
                    token_nuevo = f"checkin_{uuid.uuid4().hex[:10]}"
                    nueva_sesion = TribuSession(
                        nombre=self.edit_sesion_nombre.strip(),
                        patron_recurrencia=self.edit_sesion_patron_recurrencia,
                        foto=self.edit_sesion_foto.strip() or "/Galeria_foto1.jpg",
                        ubicacion=self.edit_sesion_ubicacion.strip(),
                        frecuencia_texto=self.edit_sesion_frecuencia.strip(),
                        fecha_texto=self.edit_sesion_fecha.strip(),
                        fecha_evento=fecha_ev,
                        hora_texto=self.edit_sesion_hora.strip(),
                        hora_recepcion_texto=self.edit_sesion_hora_recepcion.strip() or "5:00 PM",
                        inversion=self.edit_sesion_inversion,
                        plazas_totales=self.edit_sesion_plazas_totales,
                        plazas_disponibles=self.edit_sesion_plazas_totales,
                        instagram_url=self.edit_sesion_instagram.strip(),
                        recomendaciones=self.edit_sesion_recomendaciones.strip(),
                        checkin_token=token_nuevo,
                        is_active=True
                    )
                    session.add(nueva_sesion)
                    rx.toast.success("Nueva sesión creada exitosamente.")

                session.commit()
                self.modal_editor_sesion_abierto = False
                self.cargar_datos_db()
        except Exception as e:
            print(f"Error guardando sesión en Supabase: {e}")
            return rx.toast.error("Ocurrió un error al guardar en la base de datos.")

    def toggle_estado_sesion_db(self, sesion_id: int):
        """Cambia el estado de la sesión entre Activa (Visible) e Inactiva (Oculta)."""
        try:
            with rx.session() as session:
                db_s = session.get(TribuSession, sesion_id)
                if db_s:
                    db_s.is_active = not db_s.is_active
                    session.add(db_s)
                    session.commit()
                    self.cargar_datos_admin()
                    self.cargar_datos_db()
                    estado_txt = "activada (visible en la web)" if db_s.is_active else "ocultada/desactivada"
                    return rx.toast.info(f"Sesión {estado_txt}.")
        except Exception as e:
            print(f"Error cambiando estado de la sesión: {e}")
            return rx.toast.error("Error al actualizar el estado de la sesión.")

    def generar_nuevo_token_asistencia(self, sesion_id: int):
        """Genera un nuevo token único de asistencia por si se necesita renovar."""
        
        import uuid
        nuevo_token = f"checkin_{uuid.uuid4().hex[:10]}"
        try:
            with rx.session() as session:
                db_s = session.get(TribuSession, sesion_id)
                if db_s:
                    db_s.checkin_token = nuevo_token
                    session.add(db_s)
                    session.commit()
                    self.cargar_datos_db()
                    return rx.toast.success("¡Nuevo token de asistencia generado con éxito!")
        except Exception as e:
            print(f"Error generando token de asistencia: {e}")
            return rx.toast.error("Error al generar el token.")
    # -------------------------------------------------------------------------
    # 🛒 MÉTODOS CRUD DE PRODUCTOS Y CONTROL DE STOCK
    # -------------------------------------------------------------------------
    def abrir_modal_nuevo_producto(self):
        """Limpia el formulario y abre el modal para registrar un nuevo producto."""
        self.producto_id_edicion = None
        self.edit_prod_nombre = ""
        self.edit_prod_proveedor = ""
        self.edit_prod_descripcion = ""
        self.edit_prod_precio = 0.0
        self.edit_prod_stock = 10
        self.edit_prod_categoria = "Cuencos"
        self.edit_prod_intencion = ""
        self.edit_prod_foto = ""
        self.edit_prod_fotos = ["/ig_post1.png"]
        self.edit_prod_is_best_seller = False
        self.edit_prod_is_favorite = False
        self.modal_editor_producto_abierto = True

    def abrir_modal_editar_producto(self, prod: dict):
        """Carga los datos de un producto existente en el formulario."""
        self.producto_id_edicion = prod.get("id")
        self.edit_prod_nombre = prod.get("nombre", "")
        self.edit_prod_proveedor = prod.get("proveedor", "")
        self.edit_prod_descripcion = prod.get("descripcion", "")
        self.edit_prod_precio = float(prod.get("precio", 0.0))
        self.edit_prod_stock = int(prod.get("stock", 0))
        self.edit_prod_categoria = prod.get("categoria", "")
        self.edit_prod_intencion = prod.get("intencion", "")
        self.edit_prod_foto = ""
        self.edit_prod_fotos = list(prod.get("fotos", [])) if prod.get("fotos") else ([prod.get("foto_principal")] if prod.get("foto_principal") else [])
        self.edit_prod_is_best_seller = bool(prod.get("is_best_seller", False))
        self.edit_prod_is_favorite = bool(prod.get("is_favorite", False))
        self.modal_editor_producto_abierto = True

    def cerrar_modal_editor_producto(self):
        self.modal_editor_producto_abierto = False

    def guardar_producto_db(self):
        """Crea o actualiza el registro en la tabla tribu_products de Supabase."""
        if not self.edit_prod_nombre.strip() or self.edit_prod_precio <= 0:
            return rx.toast.error("Por favor ingresa un nombre válido y un precio mayor a $0 USD.")

        fotos_finales = [f for f in self.edit_prod_fotos if f.strip()]
        if not fotos_finales and self.edit_prod_foto.strip():
            fotos_finales = [self.edit_prod_foto.strip()]
        if not fotos_finales:
            fotos_finales = ["/ig_post1.png"]

        try:
            with rx.session() as session:
                if self.producto_id_edicion:
                    db_p = session.get(TribuProduct, self.producto_id_edicion)
                    if db_p:
                        db_p.nombre = self.edit_prod_nombre.strip()
                        db_p.descripcion = self.edit_prod_descripcion.strip()
                        db_p.precio = self.edit_prod_precio
                        db_p.stock = self.edit_prod_stock
                        db_p.categoria = self.edit_prod_categoria.strip()
                        db_p.proveedor = self.edit_prod_proveedor.strip()
                        db_p.intencion = self.edit_prod_intencion.strip()
                        db_p.fotos = fotos_finales
                        db_p.is_best_seller = self.edit_prod_is_best_seller
                        db_p.is_favorite = self.edit_prod_is_favorite
                        session.add(db_p)
                        rx.toast.success("Producto actualizado exitosamente.")
                else:
                    nuevo_p = TribuProduct(
                        nombre=self.edit_prod_nombre.strip(),
                        descripcion=self.edit_prod_descripcion.strip(),
                        precio=self.edit_prod_precio,
                        stock=self.edit_prod_stock,
                        categoria=self.edit_prod_categoria.strip() or "General",
                        proveedor=self.edit_prod_proveedor.strip(),
                        intencion=self.edit_prod_intencion.strip(),
                        fotos=fotos_finales,
                        is_best_seller=self.edit_prod_is_best_seller,
                        is_favorite=self.edit_prod_is_favorite,
                        is_active=True
                    )
                    session.add(nuevo_p)
                    rx.toast.success("Nuevo producto guardado en la tienda.")

                session.commit()
                self.modal_editor_producto_abierto = False
                self.cargar_datos_db()
        except Exception as e:
            print(f"Error guardando producto en Supabase: {e}")
            return rx.toast.error("Ocurrió un error al guardar en la base de datos.")

    def toggle_estado_producto_db(self, prod_id: int):
        """Conmuta la visibilidad (is_active) de un producto."""
        try:
            with rx.session() as session:
                db_p = session.get(TribuProduct, prod_id)
                if db_p:
                    db_p.is_active = not db_p.is_active
                    session.add(db_p)
                    session.commit()
                    self.cargar_datos_db()
                    estado_txt = "activado" if db_p.is_active else "ocultado"
                    return rx.toast.info(f"Producto {estado_txt}.")
        except Exception as e:
            print(f"Error cambiando estado del producto: {e}")
            return rx.toast.error("Error al actualizar el producto.")
    async def subir_foto_producto(self, files: list[rx.UploadFile]):
        """Sube una o varias fotos del producto a Supabase Storage y las agrega a la lista de imágenes."""
        if files:
            client = self.get_supabase_client()
            if not client:
                yield rx.toast.error("Error conectando con Supabase Storage.")
                return

            subidas = 0
            import uuid
            for file in files:
                file_bytes = await file.read()
                ext = file.filename.split(".")[-1].lower() if "." in file.filename else "png"
                storage_filename = f"prod_{uuid.uuid4().hex[:8]}.{ext}"
                mime_type = f"image/{'jpeg' if ext in ['jpg', 'jpeg'] else ext}"
                try:
                    client.storage.from_("comprobantes").upload(
                        path=storage_filename,
                        file=file_bytes,
                        file_options={"upsert": "true", "content-type": mime_type}
                    )
                    public_url = client.storage.from_("comprobantes").get_public_url(storage_filename)
                    if public_url not in self.edit_prod_fotos:
                        self.edit_prod_fotos.append(public_url)
                    subidas += 1
                except Exception as e:
                    print(f"Error subiendo foto de producto: {e}")

            if subidas > 0:
                yield rx.toast.success(f"{subidas} foto(s) subida(s) a Supabase con éxito.")
            else:
                yield rx.toast.error("Error al subir las imágenes a Supabase.")
    def cambiar_stock_rapido(self, prod_id: int, delta: int):
        """Suma o resta existencias directamente desde la tarjeta del panel."""
        try:
            with rx.session() as session:
                db_p = session.get(TribuProduct, prod_id)
                if db_p:
                    nuevo_stock = max(0, db_p.stock + delta)
                    db_p.stock = nuevo_stock
                    session.add(db_p)
                    session.commit()
                    self.cargar_datos_db()
                    return rx.toast.info(f"Stock actualizado a {nuevo_stock} unid.")
        except Exception as e:
            print(f"Error modificando inventario: {e}")
            return rx.toast.error("Error al modificar el stock.")

        # -------------------------------------------------------------------------
    # 🛖 MÉTODOS CRUD DE TALLERES Y EVENTOS
    # -------------------------------------------------------------------------
    def abrir_modal_nuevo_taller(self):
        """Abre el modal para registrar un nuevo taller."""
        self.taller_id_edicion = None
        self.edit_taller_titulo = ""
        self.edit_taller_tipo = "Taller"
        self.edit_taller_foto = "/Galeria_foto2d.jpg"
        self.edit_taller_facilitador = "Tribu Sonora Consciente"
        self.edit_taller_descripcion = ""
        self.edit_taller_fecha_texto = ""
        self.edit_taller_hora_texto = "6:00 PM"
        self.edit_taller_duracion_texto = "2 horas"
        self.edit_taller_ubicacion = ""
        self.edit_taller_precio = 30.0
        self.edit_taller_moneda = "USD"
        self.edit_taller_fecha_evento = ""
        self.edit_taller_whatsapp = "584241359530"
        self.modal_editor_taller_abierto = True

    def abrir_modal_editar_taller(self, taller: dict):
        """Carga los datos de un taller existente para editarlo."""
        self.taller_id_edicion = taller.get("id")
        self.edit_taller_titulo = taller.get("titulo", "")
        self.edit_taller_tipo = taller.get("tipo", "Taller")
        self.edit_taller_foto = taller.get("foto", "")
        self.edit_taller_facilitador = taller.get("facilitador", "")
        self.edit_taller_descripcion = taller.get("descripcion", "")
        self.edit_taller_fecha_texto = taller.get("fecha_texto", "")
        self.edit_taller_hora_texto = taller.get("hora_texto", "")
        self.edit_taller_duracion_texto = taller.get("duracion_texto", "")
        self.edit_taller_ubicacion = taller.get("ubicacion", "")
        self.edit_taller_precio = float(taller.get("precio", 0.0))
        self.edit_taller_moneda = taller.get("moneda", "USD")
        self.edit_taller_fecha_evento = str(taller.get("fecha_evento", ""))
        self.edit_taller_whatsapp = taller.get("whatsapp_contacto", "")
        self.modal_editor_taller_abierto = True

    def cerrar_modal_editor_taller(self):
        self.modal_editor_taller_abierto = False

    def guardar_taller_db(self):
        """Guarda o actualiza el registro en tribu_workshops en Supabase."""
        if not self.edit_taller_titulo.strip() or not self.edit_taller_ubicacion.strip():
            return rx.toast.error("Por favor completa el Título y la Ubicación del taller.")

        try:
            with rx.session() as session:
                if self.taller_id_edicion:
                    db_w = session.get(TribuWorkshop, self.taller_id_edicion)
                    if db_w:
                        db_w.titulo = self.edit_taller_titulo.strip()
                        db_w.tipo = self.edit_taller_tipo.strip()
                        db_w.foto = self.edit_taller_foto.strip()
                        db_w.facilitador = self.edit_taller_facilitador.strip()
                        db_w.descripcion = self.edit_taller_descripcion.strip()
                        db_w.fecha_texto = self.edit_taller_fecha_texto.strip()
                        db_w.hora_texto = self.edit_taller_hora_texto.strip()
                        db_w.duracion_texto = self.edit_taller_duracion_texto.strip()
                        db_w.ubicacion = self.edit_taller_ubicacion.strip()
                        db_w.precio = self.edit_taller_precio
                        db_w.moneda = self.edit_taller_moneda.strip()
                        db_w.fecha_evento = self.edit_taller_fecha_evento.strip()
                        db_w.whatsapp_contacto = self.edit_taller_whatsapp.strip()
                        session.add(db_w)
                        rx.toast.success("Taller actualizado exitosamente.")
                else:
                    nuevo_w = TribuWorkshop(
                        titulo=self.edit_taller_titulo.strip(),
                        tipo=self.edit_taller_tipo.strip() or "Taller",
                        foto=self.edit_taller_foto.strip() or "/Galeria_foto2d.jpg",
                        facilitador=self.edit_taller_facilitador.strip() or "Tribu Sonora Consciente",
                        descripcion=self.edit_taller_descripcion.strip(),
                        fecha_texto=self.edit_taller_fecha_texto.strip(),
                        hora_texto=self.edit_taller_hora_texto.strip(),
                        duracion_texto=self.edit_taller_duracion_texto.strip(),
                        ubicacion=self.edit_taller_ubicacion.strip(),
                        precio=self.edit_taller_precio,
                        moneda=self.edit_taller_moneda.strip() or "USD",
                        fecha_evento=self.edit_taller_fecha_evento.strip(),
                        whatsapp_contacto=self.edit_taller_whatsapp.strip(),
                        is_active=True
                    )
                    session.add(nuevo_w)
                    rx.toast.success("Nuevo taller registrado con éxito.")

                session.commit()
                self.modal_editor_taller_abierto = False
                self.cargar_datos_db()
        except Exception as e:
            print(f"Error guardando taller en Supabase: {e}")
            return rx.toast.error("Ocurrió un error al guardar el taller en la base de datos.")

    def toggle_estado_taller_db(self, taller_id: int):
        """Conmuta la visibilidad (is_active) de un taller."""
        try:
            with rx.session() as session:
                db_w = session.get(TribuWorkshop, taller_id)
                if db_w:
                    db_w.is_active = not db_w.is_active
                    session.add(db_w)
                    session.commit()
                    self.cargar_datos_db()
                    estado_txt = "activado" if db_w.is_active else "ocultado"
                    return rx.toast.info(f"Taller {estado_txt}.")
        except Exception as e:
            print(f"Error conmutando estado del taller: {e}")
            return rx.toast.error("Error al actualizar el taller.")

        # -------------------------------------------------------------------------
    # ✨ MÉTODOS CRUD DE SERVICIOS
    # -------------------------------------------------------------------------
    def abrir_modal_nuevo_servicio(self):
        """Abre el modal para registrar un nuevo servicio."""
        self.servicio_id_edicion = None
        self.edit_servicio_nombre = ""
        self.edit_servicio_foto = "/Galeria_foto1.jpg"
        self.edit_servicio_descripcion = ""
        self.modal_editor_servicio_abierto = True

    def abrir_modal_editar_servicio(self, servicio: dict):
        """Carga los datos de un servicio existente para editarlo."""
        self.servicio_id_edicion = servicio.get("id")
        self.edit_servicio_nombre = servicio.get("nombre", "")
        self.edit_servicio_foto = servicio.get("foto", "")
        self.edit_servicio_descripcion = servicio.get("descripcion", "")
        self.modal_editor_servicio_abierto = True

    def cerrar_modal_editor_servicio(self):
        self.modal_editor_servicio_abierto = False

    def guardar_servicio_db(self):
        """Guarda o actualiza el registro en tribu_services en Supabase."""
        if not self.edit_servicio_nombre.strip():
            return rx.toast.error("Por favor ingresa el Nombre del servicio.")

        try:
            with rx.session() as session:
                if self.servicio_id_edicion:
                    db_s = session.get(TribuService, self.servicio_id_edicion)
                    if db_s:
                        db_s.nombre = self.edit_servicio_nombre.strip()
                        db_s.foto = self.edit_servicio_foto.strip()
                        db_s.descripcion = self.edit_servicio_descripcion.strip()
                        session.add(db_s)
                        rx.toast.success("Servicio actualizado exitosamente.")
                else:
                    nuevo_s = TribuService(
                        nombre=self.edit_servicio_nombre.strip(),
                        foto=self.edit_servicio_foto.strip() or "/Galeria_foto1.jpg",
                        descripcion=self.edit_servicio_descripcion.strip(),
                        is_active=True
                    )
                    session.add(nuevo_s)
                    rx.toast.success("Nuevo servicio registrado con éxito.")

                session.commit()
                self.modal_editor_servicio_abierto = False
                self.cargar_datos_db()
        except Exception as e:
            print(f"Error guardando servicio en Supabase: {e}")
            return rx.toast.error("Ocurrió un error al guardar el servicio en la base de datos.")

    def toggle_estado_servicio_db(self, servicio_id: int):
        """Conmuta la visibilidad (is_active) de un servicio."""
        try:
            with rx.session() as session:
                db_s = session.get(TribuService, servicio_id)
                if db_s:
                    db_s.is_active = not db_s.is_active
                    session.add(db_s)
                    session.commit()
                    self.cargar_datos_db()
                    estado_txt = "activado" if db_s.is_active else "ocultado"
                    return rx.toast.info(f"Servicio {estado_txt}.")
        except Exception as e:
            print(f"Error conmutando estado del servicio: {e}")
            return rx.toast.error("Error al actualizar el servicio.")
        
    # =========================================================================
    # 🔑 AUTENTICACIÓN UNIFICADA, CARRITO EN LA NUBE E HISTORIAL
    # =========================================================================
    auth_token: str = rx.Cookie(name="tribu_auth_token")
    user_logged_in: bool = False
    usuario_datos: dict[str, Any] = {}
    
    auth_email_input: str = ""
    auth_nombre_input: str = ""
    auth_apellido_input: str = ""
    auth_pass_input: str = ""
    auth_newsletter: bool = True
    auth_modo: str = "login"  # 'login' o 'registro'

    # Historial de Usuario
    historial_ordenes_usuario: list[dict[str, Any]] = []
    historial_reservas_usuario: list[dict[str, Any]] = []
    perfil_tab_activa: str = "compras"  # 'compras' o 'reservas'

    def set_perfil_tab(self, tab: str):
        self.perfil_tab_activa = tab

    def set_auth_email(self, val: str):
        self.auth_email_input = val

    def set_auth_nombre(self, val: str):
        self.auth_nombre_input = val

    def set_auth_apellido(self, val: str):
        self.auth_apellido_input = val

    def set_auth_pass(self, val: str):
        self.auth_pass_input = val

    def set_auth_newsletter(self, checked: bool):
        self.auth_newsletter = checked

    def set_auth_modo(self, modo: str):
        self.auth_modo = modo

    @rx.var
    def nombre_usuario_activo(self) -> str:
        if self.admin_logged_in:
            return "Admin"
        if self.user_logged_in and self.usuario_datos.get("nombre"):
            return self.usuario_datos.get("nombre")
        return ""

    def guardar_carrito_db(self):
        """Guarda el estado del carrito en la tabla 'tribu_carts' de Supabase para usuarios logueados."""
        if not self.user_logged_in or not self.usuario_datos.get("id"):
            return
        
        u_id = self.usuario_datos.get("id")
        try:
            with rx.session() as session:
                db_cart = session.exec(
                    sqlmodel.select(TribuCart).where(TribuCart.user_id == u_id)
                ).first()

                if db_cart:
                    db_cart.items_json = self.carrito
                    session.add(db_cart)
                else:
                    nuevo_cart = TribuCart(
                        user_id=u_id,
                        items_json=self.carrito
                    )
                    session.add(nuevo_cart)
                session.commit()
        except Exception as e:
            print(f"Error guardando carrito en Supabase: {e}")

    def cargar_y_fusionar_carrito_db(self):
        """Carga el carrito guardado en Supabase y lo fusiona con ítems agregados como invitado."""
        if not self.user_logged_in or not self.usuario_datos.get("id"):
            return

        u_id = self.usuario_datos.get("id")
        try:
            with rx.session() as session:
                db_cart = session.exec(
                    sqlmodel.select(TribuCart).where(TribuCart.user_id == u_id)
                ).first()

                if db_cart and db_cart.items_json:
                    db_items = db_cart.items_json if isinstance(db_cart.items_json, list) else []
                    
                    # Fusión inteligente de carritos
                    keys_locales = {item["key"] for item in self.carrito}
                    for db_item in db_items:
                        if db_item.get("key") not in keys_locales:
                            self.carrito.append(db_item)
                    
                    # Actualizar Supabase con la fusión final
                    self.guardar_carrito_db()
        except Exception as e:
            print(f"Error cargando y fusionando carrito desde Supabase: {e}")

    def cargar_historial_usuario(self):
        """Consulta el historial de compras y reservas del cliente autenticado."""
        if not self.user_logged_in or not self.usuario_datos.get("email"):
            self.historial_ordenes_usuario = []
            self.historial_reservas_usuario = []
            return

        u_email = self.usuario_datos.get("email", "").strip().lower()

        try:
            with rx.session() as session:
                # 1. Cargar Órdenes de Compra
                query_ordenes = sa.text("""
                    SELECT id, numero_referencia, monto_total, metodo_pago, estado, created_at, items_json, comprobante_url
                    FROM tribu_orders
                    WHERE LOWER(cliente_email) = :email
                    ORDER BY id DESC
                """)
                res_o = session.execute(query_ordenes, {"email": u_email}).fetchall()
                
                import json
                self.historial_ordenes_usuario = [
                    {
                        "id": row[0],
                        "referencia": row[1],
                        "monto_total": float(row[2]),
                        "metodo_pago": str(row[3]).replace("_", " ").title(),
                        "estado": row[4],
                        "fecha": str(row[5])[:10] if row[5] else "Reciente",
                        "items": json.loads(row[6]) if isinstance(row[6], str) else (row[6] or []),
                        "comprobante_url": row[7] or ""
                    }
                    for row in res_o
                ]

                # 2. Cargar Reservas de Sesiones (Filtrado estricto por correo electrónico)
                query_reservas = sa.text("""
                    SELECT r.id, s.nombre, s.fecha_texto, s.hora_texto, s.ubicacion, r.cupos, r.monto_total, r.estado, r.asistio
                    FROM tribu_session_reservations r
                    JOIN tribu_sessions s ON r.session_id = s.id
                    WHERE LOWER(r.cliente_email) = :email
                    ORDER BY r.id DESC
                """)
                res_r = session.execute(query_reservas, {"email": u_email}).fetchall()

                self.historial_reservas_usuario = [
                    {
                        "id": row[0],
                        "sesion_nombre": row[1],
                        "fecha_texto": row[2],
                        "hora_texto": row[3],
                        "ubicacion": row[4],
                        "cupos": row[5],
                        "monto_total": float(row[6]),
                        "estado": row[7],
                        "asistio": row[8]
                    }
                    for row in res_r
                ]
        except Exception as e:
            print(f"Error cargando historial de usuario: {e}")

    def scroll_a_horario_sesiones(self):
        """Ejecuta un scroll suave hacia la sección de horario de sesiones una vez montado el DOM."""
        return rx.call_script(
            "setTimeout(() => { document.getElementById('seccion-horarios-sesiones')?.scrollIntoView({behavior: 'smooth', block: 'start'}); }, 200);"
        )

    def scroll_a_login_perfil(self):
        """Ejecuta un scroll suave hacia la sección de login/perfil una vez montado el DOM."""
        return rx.call_script(
            "setTimeout(() => { document.getElementById('seccion-login-perfil')?.scrollIntoView({behavior: 'smooth', block: 'start'}); }, 200);"
        )

    def scroll_a_admin_panel(self):
        """Ejecuta un scroll suave hacia la sección del panel de administración una vez montado el DOM."""
        return rx.call_script(
            "setTimeout(() => { document.getElementById('seccion-admin-panel')?.scrollIntoView({behavior: 'smooth', block: 'start'}); }, 200);"
        )

    def ir_a_horario_sesiones(self):
        """Redirige directamente al Horario de Sesiones desde cualquier punto con ancla Hash."""
        self.cerrar_menu_sesiones()
        return rx.redirect("/sesiones/horario#seccion-horarios-sesiones")

    def ir_a_login(self):
        """Redirige centralizadamente a la vista unificada de inicio de sesión con ancla Hash."""
        self.show_menu_sesiones = False
        self.show_menu_shop = False
        self.show_menu_acerca_de = False
        return rx.redirect("/login#seccion-login-perfil")

    def verificar_sesion_persistente(self):
        """Verifica la cookie de sesión, recarga el carrito de Supabase y el historial."""
        if self.auth_token == "ADMIN_TOKEN_TRIBU":
            self.admin_logged_in = True
            self.user_logged_in = False
            self.cargar_datos_admin()
        elif self.auth_token.startswith("USER_"):
            email = self.auth_token.replace("USER_", "").strip().lower()
            try:
                with rx.session() as session:
                    db_user = session.exec(
                        sqlmodel.select(TribuUser).where(TribuUser.email == email)
                    ).first()

                    if db_user and db_user.is_active:
                        self.admin_logged_in = False
                        self.user_logged_in = True
                        self.usuario_datos = {
                            "id": db_user.id,
                            "email": db_user.email,
                            "nombre": db_user.nombre,
                            "apellido": db_user.apellido or ""
                        }
                        self.cargar_y_fusionar_carrito_db()
                        self.cargar_historial_usuario()
                    else:
                        self.logout_user()
            except Exception as e:
                print(f"Error verificando sesión en Supabase: {e}")
        else:
            self.admin_logged_in = False
            self.user_logged_in = False
            self.usuario_datos = {}

    def procesar_autenticacion(self):
        """Valida credenciales, sincroniza el carrito en la nube y carga el historial."""
        email = self.auth_email_input.strip().lower()
        password = self.auth_pass_input.strip()

        if not email or not password:
            return rx.toast.error("Por favor completa el correo y la contraseña.")

        # 1. VERIFICACIÓN DE ADMINISTRADOR
        if email == "admin@tribusonora.com" and password == "tribu369":
            self.admin_logged_in = True
            self.user_logged_in = False
            self.auth_token = "ADMIN_TOKEN_TRIBU"
            self.auth_pass_input = ""
            self.auth_email_input = ""
            self.cargar_datos_admin()
            rx.toast.success("Bienvenido Administrador")
            return rx.redirect("/admin")

        # 2. PROCESAMIENTO DE CLIENTES REGULARES
        try:
            with rx.session() as session:
                if self.auth_modo == "registro":
                    if not self.auth_nombre_input.strip():
                        return rx.toast.error("Por favor ingresa tu Nombre para registrarte.")

                    usuario_existente = session.exec(
                        sqlmodel.select(TribuUser).where(TribuUser.email == email)
                    ).first()

                    if usuario_existente:
                        return rx.toast.error("Este correo ya se encuentra registrado. Cambia a 'Iniciar Sesión'.")

                    nuevo_usuario = TribuUser(
                        email=email,
                        nombre=self.auth_nombre_input.strip().capitalize(),
                        apellido=self.auth_apellido_input.strip().capitalize() if self.auth_apellido_input else None,
                        password=password,
                        is_active=True
                    )
                    session.add(nuevo_usuario)
                    session.commit()
                    session.refresh(nuevo_usuario)

                    self.user_logged_in = True
                    self.admin_logged_in = False
                    self.auth_token = f"USER_{email}"
                    self.usuario_datos = {
                        "id": nuevo_usuario.id,
                        "email": nuevo_usuario.email,
                        "nombre": nuevo_usuario.nombre,
                        "apellido": nuevo_usuario.apellido or ""
                    }
                    rx.toast.success(f"¡Registro exitoso! Bienvenido a la Tribu, {nuevo_usuario.nombre}.")

                else:
                    db_user = session.exec(
                        sqlmodel.select(TribuUser).where(
                            TribuUser.email == email,
                            TribuUser.password == password
                        )
                    ).first()

                    if not db_user:
                        return rx.toast.error("Correo o contraseña incorrectos.")

                    if not db_user.is_active:
                        return rx.toast.error("Tu cuenta se encuentra inactiva.")

                    self.user_logged_in = True
                    self.admin_logged_in = False
                    self.auth_token = f"USER_{email}"
                    self.usuario_datos = {
                        "id": db_user.id,
                        "email": db_user.email,
                        "nombre": db_user.nombre,
                        "apellido": db_user.apellido or ""
                    }
                    rx.toast.success(f"¡Bienvenido de nuevo, {db_user.nombre}!")

                # Sincronizar carrito e historial
                self.cargar_y_fusionar_carrito_db()
                self.cargar_historial_usuario()

                self.auth_pass_input = ""
                self.auth_email_input = ""
                self.auth_nombre_input = ""
                self.auth_apellido_input = ""

                if self.auth_newsletter:
                    self.email_newsletter = email
                    self.registrar_suscripcion()

                return rx.redirect("/")

        except Exception as e:
            print(f"Error procesando autenticación en Supabase: {e}")
            return rx.toast.error("Ocurrió un error al conectar con el servidor.")

    def logout_admin(self):
        self.admin_logged_in = False
        self.auth_token = ""
        rx.toast.info("Sesión de administración cerrada")
        return rx.redirect("/")

    def logout_user(self):
        self.user_logged_in = False
        self.usuario_datos = {}
        self.carrito = []  # Limpieza del carrito local al cerrar sesión
        self.historial_ordenes_usuario = []
        self.historial_reservas_usuario = []
        self.auth_token = ""
        rx.toast.info("Sesión cerrada correctamente")
        return rx.redirect("/")
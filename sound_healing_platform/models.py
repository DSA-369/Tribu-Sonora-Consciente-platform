from typing import Any
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
    requiere_correo_obligatorio: bool = sqlmodel.Field(default=False)
    requiere_porcentaje_obligatorio: bool = sqlmodel.Field(default=False)
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


class TribuClientNote(sqlmodel.SQLModel, table=True):
    """Notas internas y etiquetas personalizadas del facilitador por cliente."""
    __tablename__ = "tribu_client_notes"
    id: int | None = sqlmodel.Field(default=None, primary_key=True)
    whatsapp_cliente: str = sqlmodel.Field(unique=True, index=True)
    etiqueta: str = sqlmodel.Field(default="NUEVO")
    notas_internas: str | None = None
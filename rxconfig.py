import reflex as rx
import os
from dotenv import load_dotenv

# 1. Cargamos de forma segura las variables de tu archivo oculto .env
load_dotenv()

# URL de respaldo con el driver explícito postgresql+psycopg2
URL_SUPABASE_RESPALDO = "postgresql+psycopg2://postgres.ufjkeqqwgyauzujrbfcv:Tribuweb369@aws-1-us-east-2.pooler.supabase.com:5432/postgres?sslmode=require"

config = rx.Config(
    app_name="sound_healing_platform",
    # 2. Dejamos que Reflex maneje las rutas de la API de forma automática tanto local como en nube
    db_url=os.getenv("DATABASE_URL", URL_SUPABASE_RESPALDO),
    plugins=[
        rx.plugins.SitemapPlugin(),
    ]
)
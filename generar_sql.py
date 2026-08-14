# generar_sql.py
import re
import urllib.parse
import json

# Tu lista real y exacta de 54 archivos extraída con PowerShell
archivos_medios = [
    "Aceites_De-Andalucia.jpg.jpg",
    "Aceites_doTerra-Menta.jpg.jpg",
    "Aceites_doTerra-Protective.jpg.jpg",
    "Alimentos para el Alma_Cacao-Abkkao.jpg.jpg",
    "Alimentos para el Alma_Cacao-El-Molino-Verde.jpg.jpg",
    "Alimentos para el Alma_Infusiones-Flor-Azul.jpg.jpg",
    "Alimentos para el Alma_Infusiones-Vriadas.jpg.jpg",
    "Alimentos para el Alma_Kefir-Bulgaros.jpg.jpg",
    "Alimentos para el Alma_Kefir-de-Agua.jpg.jpg",
    "Alimentos para el Alma_Sal-Marina-Rosada-Beneficios.jpg.jpg",
    "Alimentos para el Alma_Sal-Marina-Rosada.jpg.jpg",
    "Cartas_Oraculos-de-Angeles.jpg.jpg",
    "Cartas_Tarod.jpg (2).jpg",
    "Cartas_Tarod.jpg (3).jpg",
    "Cartas_Tarod.jpg.jpg",
    "Confort_hamaca-de-aire-Azul.jpg.jpg",
    "Confort_hamaca-de-aire-Naranja.jpg.jpg",
    "Confort_Tapa-Ojos.jpg (2).jpg",
    "Confort_Tapa-Ojos.jpg.jpg",
    "Confort_Yoga-Block-corcho.jpg.jpg",
    "Confort_Yoga-Block.jpg.jpg",
    "Confort_Yoga-Mat.jpg (2).jpg",
    "Confort_Yoga-Mat.jpg.jpg",
    "Cristales_Amatista-Blancos.jpg.jpg",
    "Cristales_Amatista-Morado.jpg.jpg",
    "Cristales_Cuarzo-Cristal.jpg (2).webp",
    "Cristales_Cuarzo-Cristal.jpg (3).webp",
    "Cristales_Cuarzo-Cristal.jpg.webp",
    "Cristales_Ojo-de-Tigre.jpg.png",
    "Cristales_Verde.jpg.jpg",
    "Instrumentos_Cuencos-Cuarzo-blanco.jpg.jpg",
    "Instrumentos_Cuencos-Cuarzo-colors.jpg",
    "Instrumentos_Cuencos-tibetanos.jpg.jpg",
    "Instrumentos_didgeridoo.jpg.jpg",
    "Instrumentos_Flauta-Ocarina-Bird.jpg.jpg",
    "Instrumentos_Flauta-Ocarina-Bird2.jpg.jpg",
    "Instrumentos_Gong-DB.jpg.jpg",
    "Instrumentos_Gong-Sabian.jpg.jpg",
    "Instrumentos_HandPan.jpg.jpg",
    "Instrumentos_Semillas-Somaticas.jpg.jpg",
    "Libros_conversaciones-con-dios-1.jpg.jpg",
    "Libros_conversaciones-con-dios-2.jpg.jpg",
    "Libros_conversaciones-con-dios-3.jpg.jpg",
    "Libros_El-Hombre-que-vendio-su-ferrari.jpg.jpg",
    "Libros_El-Secreto.jpg.jpg",
    "Libros_los-4-Acuerdos.jpg.jpg",
    "Sahumerio_Hiervas-limpieza-Canela.jpg.jpg",
    "Sahumerio_Hiervas-limpieza-Variado.jpg.jpg",
    "Sahumerio_Incienso-Palo-Santo.jpg.jpg",
    "Sahumerio_incienso-Varios.jpg.jpg",
    "Sahumerio_Palo-Santo.jpg.jpg",
    "Sahumerio_Salvia-Blanca-Beneficios.jpg.webp",
    "Sahumerio_Salvia-Blanca.jpg (2).webp",
    "Sahumerio_Salvia-Blanca.jpg.webp"
]

# URL Base pública de tu almacenamiento en Supabase Storage
URL_BASE_STORAGE = "https://ufjkeqqwgyauzujrbfcv.supabase.co/storage/v1/object/public/productos-tribu/"

productos_agrupados = {}

for nombre_archivo in archivos_medios:
    if "_" not in nombre_archivo:
        continue
    
    # 1. Extraemos la categoría (todo antes del guion bajo)
    categoria, resto = nombre_archivo.split("_", 1)
    
    # 2. Eliminamos extensiones (.jpg, .webp, .png, etc., incluso las duplicadas)
    nombre_limpio = re.sub(r'\.(jpg|jpeg|png|webp|gif).*$', '', resto, flags=re.IGNORECASE)
    
    # 3. Aplicamos la regla de agrupación para detectar duplicados (2), (3) o números finales
    # Esto convertirá "Tarod (2)" o "Flauta2" a una clave base única
    clave_base = re.sub(r'(\s*\(\d+\))|(\d+)$', '', nombre_limpio).strip()
    
    # 4. Formateamos el nombre legible para mostrar en la web
    nombre_legible = clave_base.replace("-", " ").title()
    
    # 5. Construimos la URL en la nube codificando los espacios a %20
    url_publica = f"{URL_BASE_STORAGE}{urllib.parse.quote(nombre_archivo)}"
    
    # Creamos una clave única por combinación de categoría y producto
    id_unico = (categoria, clave_base)
    
    if id_unico not in productos_agrupados:
        productos_agrupados[id_unico] = {
            "nombre": nombre_legible,
            "categoria": categoria,
            "fotos": []
        }
    
    # Agregamos la foto a la lista de ese mismo producto
    productos_agrupados[id_unico]["fotos"].append(url_publica)

# 6. Comenzamos a estructurar el script SQL definitivo
sql_output = "-- SCRIPT AUTOMÁTICO DE POBLACIÓN DE DATOS REALEZ\n"
sql_output += "TRUNCATE TABLE public.tribu_products RESTART IDENTITY;\n\n"
sql_output += "INSERT INTO public.tribu_products (nombre, descripcion, precio, stock, is_best_seller, is_favorite, categoria, fotos, is_active) \nVALUES \n"

valores_sql = []
contador_aux = 0

for item in productos_agrupados.values():
    # Asignamos valores variables de forma automática para simular una tienda real
    contador_aux += 1
    precio_simulado = round(15.0 + (contador_aux * 3.5), 2)
    stock_simulado = 0 if contador_aux % 5 == 0 else 10 + contador_aux
    is_best = "true" if contador_aux % 2 == 0 else "false"
    is_fav = "true" if contador_aux % 3 == 0 else "false"
    
    # Escapamos comillas simples en los nombres por si acaso
    nombre_sql = item["nombre"].replace("'", "''")
    descripcion_sql = f"Artículo premium de la colección de {item['categoria']}. Diseñado especialmente para tus espacios de meditación, armonización sutil y conexión holística."
    fotos_json = json.dumps(item["fotos"])
    
    linea = f"('{nombre_sql}', '{descripcion_sql}', {precio_simulado}, {stock_simulado}, {is_best}, {is_fav}, '{item['categoria']}', '{fotos_json}'::jsonb, true)"
    valores_sql.append(linea)

sql_output += ",\n".join(valores_sql) + ";"

# 7. Escribimos el resultado en un archivo SQL local
with open("importar_productos.sql", "w", encoding="utf-8") as f:
    f.write(sql_output)

print("¡Éxito total! El archivo 'importar_productos.sql' ha sido generado con todos tus productos consolidados.")
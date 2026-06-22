import os
from pathlib import Path


DIRECTORIO_BASE = Path(__file__).resolve().parent


class Configuracion:
    """Configuración central del proyecto.

    Coloca tu clave de Google Maps en CLAVE_API_GOOGLE. Para que todas las
    funciones trabajen, habilita Maps JavaScript API, Places API,
    Geocoding API y Routes API en el mismo proyecto de Google Cloud.
    """

    CLAVE_API_GOOGLE = os.environ.get(
        "GOOGLE_API_KEY",
        "AIzaSyBI7-JK1Ll0OQGwG7n0tTdkQAYRDN4f094",
    )

    TIPO_VEHICULO_PREDETERMINADO = "GASOLINE"
    PRECIO_GASOLINA_MXN = 23.99
    RENDIMIENTO_PREDETERMINADO_KM_L = 14.0

    ARCHIVO_ZONAS = DIRECTORIO_BASE / "data" / "zonas_rojas.json"
    TIEMPO_ESPERA_GOOGLE_SEGUNDOS = 35

    SERVIDOR = "0.0.0.0"
    PUERTO = int(os.environ.get("PORT", 5000))
    DEPURACION = os.environ.get("FLASK_ENV", "production").lower() != "production"

    JSON_SORT_KEYS = False
    JSON_AS_ASCII = False

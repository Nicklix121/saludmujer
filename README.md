# Salud mujer

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/Nicklix121/saludmujer.git
cd saludmujer
```


**Windows:**
```bash
python -m venv env
env\Scripts\activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

O instalar manualmente:

```bash
pip install django djangorestframework djongo djangorestframework-simplejwt pymongo
```

---

## Configuración de la base de datos (MongoDB)

En `settings.py`, asegúrate de configurar:

Paso 1:  eliminar esta lineas
```python
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'nombre_de_tu_base',
    }
}
```
Paso 2:  agregar estas lineas para conectarse con MOGO DB

```python

from mongoengine import connect

connect(
    db='nombre_de_tu_base',
    host='localhost',
    port= numero_de_puerto
)
```

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

```python
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'nombre_de_tu_base',
    }
}
```

---

## Migraciones y ejecución

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

## Autenticación JWT

### Obtener token:

```http
POST /api/token/
{
  "username": "usuario",
  "password": "contraseña"
}
```

### Usar token:

Agregar en los headers:

```
Authorization: Bearer <access_token>
```

---

## Endpoints principales

| Método | URL               | Acción             |
|--------|-------------------|--------------------|
| GET    | /patients/        | Listar pacientes   |
| POST   | /patient/         | Crear paciente     |
| GET    | /patient/<id>     | Ver paciente       |
| PUT    | /patient/<id>     | Actualizar paciente|
| DELETE | /patient/<id>     | Eliminar paciente  |

---

## Notas

- Las respuestas son en formato JSON.
- JWT es requerido para acceder a la mayoría de los endpoints.

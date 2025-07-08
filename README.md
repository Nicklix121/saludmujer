# Salud Mujer

Proyecto de backend para la plataforma SaludMujer.cl, enfocado en el manejo de pacientes mediante una API RESTful con autenticación JWT y base de datos MongoDB.

---

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/Nicklix121/saludmujer.git
```

### 2. Crear y activar entorno virtual

**Windows:**
```bash
python -m venv env
env\Scripts\activate
cd saludmujer
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

**O instalar manualmente:**
```bash
pip install django djangorestframework djongo djangorestframework-simplejwt pymongo mongoengine
```

---

## 🛠️ Configuración de base de datos (MongoDB)

En `settings.py`, agrega al final:

```python
from mongoengine import connect

connect(
    db='saludmujer_db',
    host='localhost',
    port=27017
)
```

---

## 🔐 Autenticación JWT

### 🔸 Registro de usuario (POST)

**URL:** `/api/register/`  
**Método:** `POST`  
**Body (JSON):**

```json
{
  "username": "nuevo_usuario",
  "email": "correo@example.com",
  "password": "contraseña_segura"
}
```

---

### 🔸 Obtener tokens JWT (POST)

**URL:** `/api/token/`  
**Método:** `POST`  
**Body (JSON):**

```json
{
  "username": "nuevo_usuario",
  "password": "contraseña_segura"
}
```

**Respuesta esperada:**

```json
{
  "refresh": "token_refresh...",
  "access": "token_access..."
}
```

Usa el token `access` para autenticar llamadas a la API agregando en los headers:

```
Authorization: Bearer <token_access>
```

---

## 📡 Endpoints de pacientes

### 🔹 Crear paciente (POST)

**URL:** `/patient/`  
**Método:** `POST`  
**Requiere autenticación JWT**

**Body (JSON):**

```json
{
  "first_name": "Camila",
  "last_name": "Rojas",
  "run": "12345678-9",
  "email": "camila@example.com",
  "phone": "+56912345678",
  "birth_date": "1992-05-10",
  "gender": "F",
  "region": "Región Metropolitana",
  "city": "Santiago",
  "address": "Calle Falsa 123",
  "health_provider": "Fonasa"
}
```

---

### 🔹 Listar pacientes (GET)

**URL:** `/patients/`  
**Método:** `GET`  
**Requiere autenticación JWT**

**Respuesta esperada:**

```json
[
  {
    "id": "665aa1234567...",
    "first_name": "Camila",
    "last_name": "Rojas",
    "run": "12345678-9",
    ...
  }
]
```


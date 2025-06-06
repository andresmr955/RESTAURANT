# 🧠 Plan del Proyecto: Sistema de Gestión de Tareas para Restaurante

## 🎯 Objetivo General
Crear una aplicación web para gestionar empleados en un restaurante, registrar el tiempo de trabajo y asignar tareas por parte de un administrador.

---

## 👥 Roles de Usuario

### 👤 Administrador
- Crear cuentas de empleados.
- Asignar tareas a empleados.
- Ver historial de tareas completadas.
- Medir productividad con base en tiempos.

### 👨‍🍳 Empleado
- Iniciar sesión.
- Ver tareas asignadas.
- Marcar tareas como completadas.
- Registrar hora de inicio y fin por tarea.

---

## ✅ Funcionalidades MVP (Producto Mínimo Viable)

- [ ] Registro e inicio de sesión seguro.
- [ ] Panel de control diferente para admin y empleado.
- [ ] Asignación y visualización de tareas.
- [ ] Registro de tiempo trabajado.
- [ ] Reporte de productividad.

---

## 🛠️ Tecnologías

| Área          | Herramienta          |
|---------------|----------------------|
| Backend       | Python (Flask)       |
| Frontend      | HTML, CSS, Bootstrap |
| Base de Datos | SQLite (luego PostgreSQL) |
| Login         | Flask-Login          |
| Seguridad     | Werkzeug Security    |
| Despliegue    | (Futuro) Render o Heroku |

---

## 🗂️ Estructura del Proyecto

/app
/static # Archivos CSS, JS
/templates # Archivos HTML
init.py # Inicialización de Flask
models.py # Modelos de SQLAlchemy
routes.py # Rutas del servidor
forms.py # Formularios WTForms (opcional)
config.py # Configuración general
run.py # Punto de entrada principal
requirements.txt # Dependencias



---

## 🧮 Diseño de Base de Datos (Modelo inicial)

### 🧑 Usuario
- id (int, PK)
- nombre (string)
- email (string, único)
- password (hashed)
- rol (string: 'admin' o 'empleado')

### 📋 Tarea
- id (int, PK)
- título (string)
- descripción (text)
- asignada_a (FK a Usuario)
- estado (string: pendiente, en progreso, completada)
- tiempo_inicio (datetime)
- tiempo_fin (datetime)

---

## 📅 Próximos pasos

1. [ ] Crear entorno virtual e instalar Flask.
2. [ ] Configurar archivo `__init__.py` con la app Flask.
3. [ ] Definir modelos en `models.py`.
4. [ ] Crear base de datos inicial.
5. [ ] Implementar registro e inicio de sesión.


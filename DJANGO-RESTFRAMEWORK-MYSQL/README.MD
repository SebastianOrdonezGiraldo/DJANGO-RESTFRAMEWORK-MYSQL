# Crea y Prueba una REST API con Django REST Framework y MySQL

Este proyecto implementa una REST API para gestionar empresas utilizando Django REST Framework (DRF) y MySQL como base de datos. Se incluye un modelo llamado **Company** que permite almacenar el nombre, sitio web y año de fundación de cada empresa, y se proveen endpoints para realizar operaciones CRUD.

## Características

- **Modelo Company:** Define los siguientes campos:
  - `name`: Nombre de la empresa.
  - `website`: URL del sitio web.
  - `foundation`: Año de fundación (valor entero positivo).
- **Serialización:** Se utiliza un `ModelSerializer` para transformar instancias del modelo en JSON y viceversa.
- **Endpoints CRUD:** Implementados mediante un ViewSet y enrutados con el router por defecto de DRF.
- **Base de Datos MySQL:** Configurada en `settings.py` para trabajar con MySQL.

## Requisitos

- **Python 3.8+**
- **Django 5.1.7**
- **Django REST Framework**
- **MySQL Server**
- **mysqlclient** (u otro conector compatible)
- **pip** y opcionalmente **virtualenv**

## Instalación y Configuración

1. **Clonar el repositorio:**

   ```bash
   git clone <https://github.com/SebastianOrdonezGiraldo/DJANGO-RESTFRAMEWORK-MYSQL.git>
   cd <DJANGO-RESTFRAMEWORK-MYSQL>
   ```

2. **Crear y activar un entorno virtual:**

   - En Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - En Linux/macOS:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instalar las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar la Base de Datos en `settings.py`:**

   Asegúrate de que la configuración en el diccionario `DATABASES` se corresponda con tus credenciales locales:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'django_restframework',
           'USER': 'root',
           'PASSWORD': 'root',
           'HOST': 'localhost',
           'PORT': '3308',
           'OPTIONS': {
               'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
           },
       }
   }
   ```

5. **Realizar las migraciones:**

   ```bash
   python manage.py migrate
   ```

6. **Iniciar el servidor de desarrollo:**

   ```bash
   python manage.py runserver
   ```

   La API estará disponible en:  
   [http://127.0.0.1:8000/api/v1/companies/](http://127.0.0.1:8000/api/v1/companies/)

## Uso de la API

### Endpoints Disponibles

- **Listar todas las empresas:**
  - `GET /api/v1/companies/`

- **Obtener detalles de una empresa:**
  - `GET /api/v1/companies/<id>/`

- **Crear una nueva empresa:**
  - `POST /api/v1/companies/`
  - **Ejemplo de payload JSON:**
    ```json
    {
      "name": "Empresa Ejemplo",
      "website": "https://ejemplo.com",
      "foundation": 2000
    }
    ```

- **Actualizar una empresa:**
  - `PUT /api/v1/companies/<id>/`

- **Eliminar una empresa:**
  - `DELETE /api/v1/companies/<id>/`

## Estructura del Proyecto

- **api/models.py:**  
  Define el modelo `Company` con sus atributos y el método `__str__`.

- **api/serializer.py:**  
  Contiene el `CompanySerializer` que hereda de `serializers.ModelSerializer` y utiliza todos los campos del modelo.

- **api/views.py:**  
  Implementa el `CompanyViewSet` basado en `viewsets.ModelViewSet`, proporcionando las operaciones CRUD automáticamente.

- **api/urls.py:**  
  Define el enrutamiento de la API utilizando el `DefaultRouter` de DRF, registrando el ViewSet de Company.

- **drf_mysql/settings.py:**  
  Configuración global del proyecto, incluida la conexión a la base de datos MySQL.

- **drf_mysql/urls.py:**  
  Incluye la URL para el panel de administración y la integración de las rutas de la API.

## Pruebas

Para ejecutar las pruebas del proyecto, usa el siguiente comando:

```bash
python manage.py test
```

## Contribuciones

Si deseas contribuir al proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tu nueva funcionalidad:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. Realiza tus cambios y haz commit:
   ```bash
   git commit -m "Agrega nueva funcionalidad"
   ```
4. Envía tu rama al repositorio remoto:
   ```bash
   git push origin feature/nueva-funcionalidad
   ```
5. Abre un Pull Request para integrar tus cambios.

## Licencia

Este proyecto se distribuye bajo la [Licencia MIT](LICENSE).

## Contacto

Para consultas o sugerencias, puedes contactarme a través de [sordonez0181@cue.edu.co]().

---

¡Disfruta desarrollando y probando tu REST API con Django REST Framework y MySQL!


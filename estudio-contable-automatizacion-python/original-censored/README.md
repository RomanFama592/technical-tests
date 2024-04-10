# PRUEBA PARA PUESTO LIDER EN AUTOMATIZACIONES

### Cualquier duda o problema, comuníquese via correo electrónico a famaroman@gmail.com

## Indices

- [**Instalación y Ejecución**](#explicacion-instalación-y-ejecución)
   - [**Requisitos**](#requisitos)
   - [**Archivos necesarios en Google Drive**](#archivos-necesarios-en-google-drive)
   - [**Explicación**](#explicación)

<!-- TODO: Seguir los indices -->

## Explicacion, Instalación y Ejecución

### - _Requisitos:_

Asegúrate de cumplir con los siguientes requisitos antes de comenzar:

- Git instalado en tu sistema.
- Python 3.11 instalado en tu sistema.
- Tener el archivo JSON con el ID de cliente OAuth 2.0.
   - [Pagina sobre las API´s de Google](https://console.cloud.google.com/)

### - _Archivos necesarios en Google Drive:_

__TENER EN CUENTA:__ Asegúrese de que los nombres de los clientes sean consistentes entre archivos.
Ademas los nombres de las columnas tienen que ser exactos a como se especificaron acá para evitar errores no manejados actualmente. Por ultimo no tener archivos con el mismo nombre o que esten en la papelera y version anterior eliminada ya que se pueden generar conflictos.


#### Celdas correspondiente en cada tabla:

| A1 | B1 | C1 | D1 |
|----|----|----|----|
| A2 | B2 | C2 | D2 |
| A3 | B3 | C3 | D3 |

#### Google Sheet "Ingresos":

| Clientes | Ingresos | Detalle  |
|----------|----------|----------|
| cliente1 | 10000    | detalle1 |
| cliente2 | 20000    | detalle2 |

#### Google Sheet "Emails":

| Clientes | Emails             |
|----------|--------------------|
| cliente1 | cliente1@gmail.com |
| cliente2 | cliente2@gmail.com |

#### Google Sheet "Gastos":

| Clientes | Gastos_Operativos | Impuestos | Otros_Gastos |
|----------|-------------------|-----------|--------------|
| cliente1 | 10000             | 1000      | 20000        |
| cliente2 | 20000             | 2000      | 15000        |

<p align="right"><a href="#top">Back to top 🔼</a></p>
<br>

### Explicación

La aplicación, una vez que termine la autenticación de una cuenta de Google, procederá a buscar en la carpeta especificada los archivos necesarios ("Emails", "Ingresos", "Gastos") para empezar a hacer el análisis de balance de cada cliente de la última hoja de cada archivo. Si falta alguna de estas, el proceso no comenzará. Una vez finalizado este proceso y habiendo notificado a cada cliente de que están gastando más de lo que ingresan, es cuando se procede al análisis de la categoría de cada cliente, creando el archivo "Monotributo Categorías" si no existe, el cual contendrá varias hojas, todas correspondientes al año del análisis y tendrá este formato:

| Clientes | Categorias |
|----------|------------|
| cliente1 | A          |
| cliente2 | C          |

Una vez subida la información de todos los clientes, así es como se daría por finalizada la ejecución del programa.

<p align="right"><a href="#top">Back to top 🔼</a></p>
<br>

### Pasos para la Ejecución

Es esencial tener preparados los archivos del paso anterior para el perfecto funcionamiento del programa

Sigue estos pasos para clonar el repositorio, configurar el entorno virtual y ejecutar el programa:

1. **Clonar el Repositorio**

   Abre tu terminal y ejecuta el siguiente comando para clonar el repositorio desde GitHub:

   ```shell
   git clone [URL_DEL_REPOSITORIO]
   ```

   Sustituye `[URL_DEL_REPOSITORIO]` por la URL real de tu repositorio en GitHub.

2. **Acceder al Directorio del Proyecto**

   Cambia al directorio del proyecto recién clonado:

   ```shell
   cd [nombre_del_directorio]
   ```

   Sustituye `[nombre_del_directorio]` por el nombre real de la carpeta creada al clonar el repositorio.

3. **Instalar pipenv**

   Si no tienes `pipenv` instalado, puedes hacerlo con el siguiente comando:

   ```shell
   pip install pipenv
   ```

4. **Activar el Entorno Virtual**

   Activa el entorno virtual con el siguiente comando:

   ```shell
   pipenv shell
   ```

5. **Crear un Entorno Virtual e Instalar Dependencias**

   Ejecuta el siguiente comando para crear un entorno virtual y automáticamente instalar las dependencias del proyecto:

   ```shell
   pipenv install
   ```

6. **Cree su `.env` en la raiz del proyecto**

   Usar el `.env.example` para crear su propio .env .

7. **Ejecutar el Programa**

   Finalmente, ejecuta el programa con el siguiente comando:

   ```shell
   py index.py
   ```

8. **Iniciar sesion en la cuenta de Google dode tiene los Sheets**

   Despues de iniciar, se abrira una pestaña en su navegador predeterminado para permitirle inciar sesion y autorizar a la aplicacion.

Con estos pasos, habrás configurado el entorno de desarrollo y ejecutado tu programa con exito.

<p align="right"><a href="#top">Back to top 🔼</a></p>
<br>

## Respuestas a las sus preguntas

### __¿Cómo mejorarías este sistema si tuvieses una semana más para trabajar en él?__

Si tuviera una semana más para trabajar en este sistema, consideraría las siguientes mejoras:

**Automatización programada:** Implementaría automatización programada utilizando CRON en Unix o el Programador de tareas en Windows para ejecutar el código a intervalos mensuales.

**Problema con el calculo del monotributo:** Actualmente hay un error en el calculo de las categorias cual se calcula en base a los ingresos mensuales y no de forma anual. No creo tener problema en solucionarlo, solamente necesito un poco tiempo.

**Refactorización de código:** Dividiría el código en módulos y/o entidades separadas para mejorar organización, legibilidad y reusabilidad, facilitando el mantenimiento y la colaboración con otros desarrolladores.

**Notificaciones via email:** Reutilizando el mismo sistema que me permite enviarle emails a los clientes para notificar de errores y/o problemas.

**Manejo de errores robusto:** Mejoraría el manejo de errores para aumentar la robustez del sistema frente a situaciones inesperadas, como problemas de conexión a Google Sheets o errores en la lógica.

**Ampliar sistemas de autenticación:** Implementaría un sistema de autenticación automático para acceder a cuentas de Google o exploraría opciones de la API.

**Utilizar Docker:** Expandiría la compatibilidad con diferentes sistemas y hostings mediante Docker.

<p align="right"><a href="#top">Back to top 🔼</a></p>
<br>

### __Otras cosas que podria hacer con mas de una semana para trabajar en este proyecto__

**Unit Testing:** Escribiría pruebas para cada componente crítico del sistema, garantizando su funcionamiento y evitando futuros errores.

**Base de datos SQLite:** Crearía una base de datos SQLite en Google Drive para gestionar datos sin manipulación manual en Google Sheets, evitando errores.

**Interfaz de usuario:** Teniendo en cuenta lo anterior, desarrollaría una interfaz web para cargar datos de gastos e ingresos y consultar categorizaciones, haciéndolo accesible para usuarios no técnicos.

<p align="right"><a href="#top">Back to top 🔼</a></p>
<br>

### __¿Dónde harías deploy de esta solución y cómo automatizarías su ejecución cada mes?__

Haría el deploy de esta solución en un servidor o máquina virtual en la nube, como **Amazon Web Services (AWS)** o **Google Cloud Platform (GCP)**. Esto garantiza que la solución esté disponible las 24 horas del día y pueda ejecutarse automáticamente.
Si ya cuenta con un servidor propio utilizaria ese.

Para automatizar su ejecución cada mes, utilizaría **Programador de Tareas de Windows** o su equivalente **CRON de Linux**.

<p align="right"><a href="#top">Back to top 🔼</a></p>
<br>
# Portfolio QA — Bernardo López

[![Tests](https://github.com/Bernylop14/portfolio-qa/actions/workflows/test.yml/badge.svg)](https://github.com/Bernylop14/portfolio-qa/actions/workflows/test.yml)

Soy Bernardo López (Berny). Vengo de la cetrería de altanería, donde llevo 
desde 2021 colaborando con **Ayama Segutel**, la empresa detrás de 
**Ayama Elite** — aplicación móvil y sistema de hardware GPS para cetrería — 
probando sus productos sobre el terreno, reportando fallos y proponiendo 
mejoras junto a su equipo de desarrollo. Esos años me dieron un conocimiento 
profundo de cómo se comporta este hardware en condiciones reales, y un 
instinto fuerte para encontrar casos límite.

Decidí dar el salto a QA profesional porque la calidad de un producto me 
importa de verdad: no me conformo con que algo "funcione más o menos", y 
prefiero agotar todas las opciones antes de dar un problema por imposible. 
Trabajo de forma autónoma, intento resolver las cosas por mí mismo antes 
de pedir ayuda, aunque cuando el equipo rema en la misma dirección, 
trabajar codo con codo no es ningún problema. Lo que más valoro es 
trabajar con un equipo comprometido con la calidad.

> **Nota:** todo el código de este repositorio (Python) corresponde a mi 
> documentación y automatización de testing. Ayama Elite, la app que pruebo, 
> es una aplicación móvil nativa para iOS y Android con su propio stack de 
> frontend, independiente del código que aquí veas.

## Qué incluye

- **Testing manual**: plan de pruebas, casos de prueba y reporte de bugs
- **Gestión de bugs y verificación en Jira**: dos funciones distintas — verificación de mejoras y desarrollos nuevos antes de su puesta en producción, y reporte/seguimiento del ciclo de vida completo de bugs ya en producción, de apertura a cierre
- **API testing (Postman)**: peticiones y verificación de respuestas
- **Automatización (pytest)**: tests unitarios, fixtures, mocks y tests de integración
- **Automatización web (Playwright)**: tests end-to-end de UX&UI sobre un entorno real de navegador
- **CI/CD (GitHub Actions)**: pipeline que instala dependencias, descarga los navegadores de Playwright y ejecuta automáticamente toda la suite (pytest + Playwright) en cada cambio subido al repositorio (ver insignia arriba)

## Documentos

- [Plan de Pruebas](01_Plan_de_Pruebas_Ayama_Elite.pdf) — Planificación 
  estratégica de las pruebas: objetivo, alcance, estrategia, recursos y riesgos.
- [Caso de Prueba y Bug Report](02_Caso_de_prueba_Pointer_Élite.pdf) — 
  Caso de prueba funcional documentado y reporte de un bug real, 
  con evidencia fotográfica.

## Evidencias en herramientas reales

- [Jira — Tablero Kanban, verificación de mejoras y gestión de bugs](evidencias_jira/) — 
  Proyecto real donde verifico desarrollos antes de su puesta en producción 
  y documento bugs movidos a través de su ciclo de vida 
  (Idea → To Do → In Progress → In Review → Done).
- [Postman — Pruebas de API](evidencias_postman/) — Peticiones 
  GET y POST con verificación de códigos de estado.

## Automatización (pytest)

Tests automatizados en Python usando pytest, aplicados sobre la lógica de Ayama Elite:

- **Parametrize**: validación de edad de halcón con análisis de valores límite (0, 1, 30, 31)
- **Fixtures**: datos de prueba reutilizables (halcón de prueba)
- **Fixtures con yield**: setup y teardown simulando conexión/desconexión con el receptor
- **Mock**: simulación de señal del receptor sin depender del hardware físico
- **Test de integración**: peticiones HTTP reales con `requests`, validando status code y estructura de respuesta

Archivos: [`automation/ayama_funciones.py`](automation/ayama_funciones.py) · [`automation/test_ayama_funciones.py`](automation/test_ayama_funciones.py) · [evidencia de ejecución](automation/evidencia_pytest.txt)

## Automatización web (Playwright)

### SauceDemo Checkout Flow — Automatización E2E con Playwright

Suite end-to-end sobre una aplicación web real (entorno de práctica público), 
cubriendo el recorrido completo de un usuario, no solo una pantalla suelta:

- **Login**: Happy path y Unhappy path (usuario válido, usuario bloqueado, contraseña incorrecta), con `parametrize`
- **Carrito**: añadir un producto y verificar tanto el cart badge (contador) como su contenido
- **Checkout completo**: relleno de formulario de envío y verificación del mensaje de confirmación del pedido
- **Logout**: cierre de sesión y verificación de vuelta a la pantalla de login
- **`expect()` de Playwright**: aserciones (y acciones) con auto-espera integrada, evitando tests inestables (*flaky*) sin necesidad de esperas explícitas manuales

Archivos: [`automation/test_web.py`](automation/test_web.py)

> Este conjunto de tests se ejecuta tanto en local como dentro del pipeline de CI (GitHub Actions), en una máquina limpia que descarga los navegadores de Playwright en cada ejecución (ver `.github/workflows/test.yml`).
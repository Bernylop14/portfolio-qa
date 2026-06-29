# Portfolio QA — Bernardo López

[![Tests](https://github.com/Bernylop14/portfolio-qa/actions/workflows/test.yml/badge.svg)](https://github.com/Bernylop14/portfolio-qa/actions/workflows/test.yml)

Documentación de testing real sobre **Ayama Elite** (aplicación móvil 
y sistema de hardware GPS para cetrería), basada en aproximadamente 
un año de experiencia como tester del producto en colaboración 
directa con el equipo de desarrollo.

## Qué incluye

- **Testing manual**: plan de pruebas, casos de prueba y reporte de bugs
- **Gestión de bugs (Jira)**: ciclo de vida real de incidencias, de apertura a cierre
- **API testing (Postman)**: peticiones y verificación de respuestas
- **Automatización (pytest)**: tests unitarios, fixtures, mocks y tests de integración
- **Automatización web (Playwright)**: tests end-to-end de UI sobre un entorno real de navegador
- **CI/CD (GitHub Actions)**: pipeline que instala dependencias, descarga los navegadores de Playwright y ejecuta automáticamente toda la suite (pytest + Playwright) en cada cambio subido al repositorio (ver insignia arriba)

## Documentos

- [Plan de Pruebas](01_Plan_de_Pruebas_Ayama_Elite.pdf) — Planificación 
  estratégica de las pruebas: objetivo, alcance, estrategia, recursos y riesgos.
- [Caso de Prueba y Bug Report](02_Caso_de_prueba_Pointer_Élite.pdf) — 
  Caso de prueba funcional documentado y reporte de un bug real, 
  con evidencia fotográfica.

## Evidencias en herramientas reales

- [Jira — Tablero Kanban y gestión de bugs](evidencias_jira/) — 
  Proyecto real con bugs documentados y movidos a través de su 
  ciclo de vida (Idea → To Do → In Progress → In Review → Done).
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

- **Login**: camino feliz y camino de error (usuario válido, usuario bloqueado, contraseña incorrecta), con `parametrize`
- **Carrito**: añadir un producto y verificar tanto el contador del carrito como su contenido
- **Checkout completo**: relleno de formulario de envío y verificación del mensaje de confirmación del pedido
- **Logout**: cierre de sesión y verificación de vuelta a la pantalla de login
- **`expect()` de Playwright**: aserciones (y acciones) con auto-espera integrada, evitando tests inestables (*flaky*) sin necesidad de esperas explícitas manuales

Archivos: [`automation/test_web.py`](automation/test_web.py)

> Este conjunto de tests se ejecuta tanto en local como dentro del pipeline de CI (GitHub Actions), en una máquina limpia que descarga los navegadores de Playwright en cada ejecución (ver `.github/workflows/test.yml`).

## Sobre el contexto

Ayama Elite es una aplicación comercial real para el seguimiento 
GPS de halcones, usada en cetrería de altanería y competición. 
Durante mi colaboración como tester realicé pruebas de campo, 
reporte y verificación de bugs, y pruebas de estrés en condiciones 
límite de señal y hardware.

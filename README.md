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
- **CI/CD (GitHub Actions)**: los tests se ejecutan automáticamente en cada cambio subido al repositorio (ver insignia arriba)

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

Tests end-to-end sobre una aplicación web real (entorno de práctica público), 
simulando el comportamiento de un usuario en el navegador:

- **Interacción real con la UI**: relleno de formularios y clics simulados
- **Parametrize aplicado a UI**: un mismo test cubre varios escenarios de login (usuario válido, usuario bloqueado, contraseña incorrecta)
- **`expect()` de Playwright**: aserciones que esperan automáticamente a que la página reaccione, evitando tests inestables (*flaky*)
- **Cobertura de camino feliz y camino de error**: login exitoso y mensajes de error visibles ante credenciales inválidas

Archivos: [`automation/test_web.py`](automation/test_web.py)

## Sobre el contexto

Ayama Elite es una aplicación comercial real para el seguimiento 
GPS de halcones, usada en cetrería de altanería y competición. 
Durante mi colaboración como tester realicé pruebas de campo, 
reporte y verificación de bugs, y pruebas de estrés en condiciones 
límite de señal y hardware.

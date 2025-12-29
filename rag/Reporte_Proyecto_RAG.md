Informe de Investigación: Análisis Sociológico de la Gen Z mediante IA (RAG)
1. Introducción
Este proyecto representa la culminación de la Unidad 3, donde se ha desarrollado un sistema de Generación Aumentada por Recuperación (RAG). El objetivo es analizar cómo la Generación Z experimenta la crisis de sentido y la pérdida de autonomía en un mundo dominado por algoritmos. A diferencia de un análisis estadístico simple, este sistema permite "interrogar" a los datos y obtener respuestas fundamentadas en la filosofía contemporánea.

2. Metodología y Stack Tecnológico
El sistema fue construido íntegramente en Python, utilizando una arquitectura de inteligencia artificial local para garantizar la privacidad y el control total de los datos.

Infraestructura Técnica:
Lenguaje: Python 3.10

Modelo de Lenguaje (LLM): Llama 3 .

Motor de Vectores: ChromaDB Base de datos vectorial persistente.

Procesamiento de Lenguaje: LangChain (para el pipeline de recuperación y generación).

Dataset: 5,200 registros de discursos digitales de la Gen Z.

1. Arquitectura del Sistema 
El código implementado sigue un flujo de trabajo de cuatro etapas:

Ingesta Semántica: Se cargan 5,200 registros. Cada texto se fusiona con su tema para enriquecer el contexto.

Vectorización (Embeddings): Mediante modelos matemáticos, cada post se convierte en un vector en un espacio de n-dimensiones.

Persistencia en Disco: Se implementó una base de datos en el directorio ./db_investigacion. Esto permite que el sistema cargue los datos de forma instantánea tras la primera indexación.

Recuperación por Similitud Coseno: Al realizar una pregunta, el sistema busca los 5 fragmentos con mayor "proximidad semántica" en el dataset antes de generar la respuesta.

4. Auditoría de Datos y Evidencia de Bots
Antes del análisis, se ejecutó un script de detección de duplicados para asegurar la calidad de la investigación:

Total de Registros: 5,200.

Hallazgo: Se detectó una alta tasa de mensajes repetidos .

Interpretación: Esto evidencia la existencia de "cámaras de eco" o actividad de bots que estandarizan el discurso de la crisis existencial en redes sociales.



1. Implementación del Marco Filosófico
El sistema fue programado mediante Prompt Engineering para actuar como un investigador experto, aplicando cuatro ejes teóricos:

Zygmunt Bauman: Para analizar la fragilidad de los vínculos (Identidad Líquida).

Byung-Chul Han: Para estudiar el agotamiento digital (Sociedad del Rendimiento).

Michel Foucault: Para interpretar el control algorítmico (Panóptico Digital).

Martin Heidegger: Para comprender la transformación del ser a través de la técnica.

1. Análisis Documentado con Evidencia 
Caso 1: Autonomía vs. Algoritmos (Pregunta 02)
Evidencia RAG: El sistema recuperó múltiples menciones sobre cómo plataformas como TikTok y Netflix moldean el comportamiento. Análisis: La IA concluyó que la autonomía se vuelve "difusa". Bajo la lente de Foucault, el algoritmo no es una herramienta, sino un régimen de vigilancia que normaliza los deseos del usuario.

Caso 2: El Vacío Existencial (Pregunta 01)
Evidencia RAG: Frases detectadas: "No sé qué hacer con mi vida, pero quiero compartirlo en Instagram". Análisis: Esto confirma la tesis de Bauman. La Gen Z busca validación en lo efímero para llenar un vacío que la propia fluidez digital genera.

1. Conclusiones
La investigación demuestra que la tecnología RAG es una herramienta poderosa para las ciencias sociales. Los hallazgos sugieren que la Gen Z vive en una "crisis de sentido tecnificada". La conclusión final es que, mientras la IA siga decidiendo nuestras preferencias, la autonomía humana seguirá siendo una construcción performativa y no una libertad real.

Desarrollado por: Miguel Angel Silva Garcia Materia: Inteligencia Artificial - Unidad 3 Fecha: Diciembre 2025


import pandas as pd
import os
import sys
from tqdm import tqdm
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# --- CONFIGURACIÓN DE INVESTIGACIÓN ---
archivo_csv = 'dataset.csv'
modelo = "llama3"
persist_dir = "./db_investigacion"
num_registros = 5200  

# 1. CARGA DE DATOS
print(f"---  SISTEMA RAG: PROYECTO GEN Z ---")
if not os.path.exists(archivo_csv):
    print(f"Error: No encontré el archivo {archivo_csv}")
    sys.exit()

df = pd.read_csv(archivo_csv).head(num_registros)
textos = (df['tema'] + ": " + df['texto']).tolist()

# 2. CONFIGURAR CEREBRO (EMBEDDINGS Y VECTOR STORE)
embeddings = OllamaEmbeddings(model=modelo)

if os.path.exists(persist_dir):
    print("✓ Cargando memoria persistente desde disco...")
    vectorstore = Chroma(persist_directory=persist_dir, embedding_function=embeddings)
else:
    print(f" creando nueva base de datos vectorial ({num_registros} registros)...")
    vectorstore = Chroma(persist_directory=persist_dir, embedding_function=embeddings)
    # Agregar textos con barra de progreso
    for i in tqdm(range(len(textos)), desc="Indexando registros"):
        vectorstore.add_texts(texts=[textos[i]])
    print("✓ Memoria guardada con éxito en 'db_investigacion'.")

retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

# 3. PROMPT DE INVESTIGACIÓN (MARCO FILOSÓFICO AJUSTADO)
template = """Eres un Investigador Sociológico experto. Responde de forma clara, técnica y profesional en ESPAÑOL.

REGLAS DE FORMATO:
- Usa minúsculas y mayúsculas correctamente. NO USES MAYÚSCULAS SOSTENIDAS.
- No repitas párrafos. Si ya dijiste una idea, pasa a la siguiente.
- Al final de cada análisis de autor, incluye una CITA BIBLIOGRÁFICA real de sus libros.

MARCOS TEÓRICOS:
- Zygmunt Bauman (Identidad Líquida)
- Byung-Chul Han (Cultura del Rendimiento)
- Michel Foucault (Vigilancia)
- Martin Heidegger (Tecnificación)

CONTEXTO DEL DATASET:
{context}

PREGUNTA: {question}

ANÁLISIS INTERPRETATIVO:"""

prompt = ChatPromptTemplate.from_template(template)

# 4. CONFIGURACIÓN DEL MODELO (EQUILIBRIO PARA EVITAR ERRORES)
llm = OllamaLLM(
    model=modelo,
    temperature=0.2,     
    repeat_penalty=2.2,   
    num_predict=450,
    top_k=20,
    top_p=0.9
)


chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# 5. LISTA OFICIAL DE LAS 20 PREGUNTAS DEL PROYECTO
preguntas_proyecto = [
    "¿Qué expresiones utiliza la Gen Z para describir el vacío existencial en redes sociales?",
    "¿Cómo influyen los algoritmos de recomendación en la construcción de su identidad?",
    "¿Qué emociones aparecen con mayor frecuencia cuando se habla de burnout o presión digital?",
    "¿La Gen Z percibe la autonomía como algo propio o como algo condicionado por la tecnología?",
    "¿Qué diferencias hay entre discursos auténticos vs discursos performativos en TikTok?",
    "¿Existen patrones de lenguaje que indiquen crisis de sentido o desorientación vital?",
    "¿Cómo se refleja la idea de 'identidad líquida' en los datos recuperados?",
    "¿Qué menciones aparecen sobre libertad, control o manipulación algorítmica?",
    "¿Se observan señales de que los algoritmos crean deseos o hábitos?",
    "¿Qué temas predominan en la conversación digital sobre propósito de vida?",
    "¿Hay evidencia de rechazo a los metarrelatos o valores tradicionales?",
    "¿Cómo aparece la figura del 'yo digital' en los textos analizados?",
    "¿Qué ejemplos concretos muestran pérdida del pensamiento crítico por la burbuja de filtros?",
    "¿Existen contrastes entre la visión que la Gen Z tiene de sí misma y lo que los datos sugieren?",
    "¿Qué rol juega la hiperconectividad en la ansiedad o depresión mencionada?",
    "¿Se observan patrones que apoyen las ideas de Byung-Chul Han sobre autoexplotación?",
    "¿Cómo interpretaría Foucault el régimen de vigilancia algorítmica detectado?",
    "¿Qué evidencias hay de que la tecnología 'desoculta' y transforma la vida según Heidegger?",
    "¿El espacio público digital está debilitado como afirma Habermas?",
    "¿Cuáles son los principales miedos, frustraciones y esperanzas de la Gen Z frente al futuro?"
]

# 6. MENÚ INTERACTIVO
def menu():
    while True:
        print("\n" + "═"*60)
        print("   MENÚ DE INVESTIGACIÓN RAG - PROYECTO GEN Z")
        print("═"*60)
        for i, p in enumerate(preguntas_proyecto):
            print(f"{i+1:02d}. {p}")
        print("00. SALIR")
        print("═"*60)
        
        try:
            opcion = int(input("Seleccione el número de pregunta (1-20): "))
            if opcion == 0:
                print("Saliendo del sistema...")
                break
            if 1 <= opcion <= 20:
                q = preguntas_proyecto[opcion-1]
                print(f"\n[PROCESANDO PREGUNTA {opcion}]...")
                respuesta = chain.invoke(q)
                print(f"\n--- RESULTADO DE INVESTIGACIÓN ---\n\n{respuesta}\n")
                input("Presione ENTER para continuar...")
            else:
                print("Opción fuera de rango.")
        except ValueError:
            print("Entrada inválida. Use números.")

if __name__ == "__main__":
    menu()
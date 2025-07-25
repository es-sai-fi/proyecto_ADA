import random

def generateData(K, M, Nmin, Nmax, mode="min"):
  assert mode in ["min", "max", "random"]
  
  participants = []
  questionBlocks = []
  participantId = 1

  for _ in range(K):
    block = []
    
    for _ in range(M):
      if mode == "min":
        numParticipants = Nmin
      elif mode == "max":
        numParticipants = Nmax
      else:
        numParticipants = random.randint(Nmin, Nmax)

      questionParticipants = list(range(participantId, participantId + numParticipants))
      participantId += numParticipants
      block.append(questionParticipants)
      
      for pid in questionParticipants:
        name = f"Persona {pid}"
        expertise = random.randint(0, 10)
        opinion = random.randint(0, 10)
        participants.append(f"{name}, Experticia: {expertise}, Opinión: {opinion}")
        
    questionBlocks.append(block)

  return participants, questionBlocks

def formatOutput(participants, questionBlocks):
  lines = []
  
  for p in participants:
    lines.append("\n")
    lines.append(p)

  for block in questionBlocks:
    for question in block:
      lines.append("\n")
      lines.append("\n")
      lines.append("\n")
      lines.append("{" + ", ".join(map(str, question)) + "}")
      
  return "".join(lines)
  
# Parámetros test 4 (Muchos temas)
K = 10 # Número de temas
M = 50 # Número de preguntas por tema
Nmin = 1 # Mínimo número de encuestados por pregunta
Nmax = 3 # Máximo número de encuestados por pregunta
mode = "random" # Modo de generación
path = "tests/Test4.txt" # Ruta donde guardar el output

participants, questionBlocks = generateData(K, M, Nmin, Nmax, mode)
formattedText = formatOutput(participants, questionBlocks)

with open(path, "w", encoding="utf-8") as f:
  f.write(formattedText)

# Parámetros test 5 (Mismo K, mayor M)
K = 10 # Número de temas
M = 100 # Número de preguntas por tema
Nmin = 1 # Mínimo número de encuestados por pregunta
Nmax = 3 # Máximo número de encuestados por pregunta
mode = "random" # Modo de generación
path = "tests/Test5.txt" # Ruta donde guardar el output

participants, questionBlocks = generateData(K, M, Nmin, Nmax, mode)
formattedText = formatOutput(participants, questionBlocks)

with open(path, "w", encoding="utf-8") as f:
  f.write(formattedText)
# Parámetros test 6 (Numeros Grandes)
K = 100 # Número de temas
M = 50 # Número de preguntas por tema
Nmin = 10 # Mínimo número de encuestados por pregunta
Nmax = 30 # Máximo número de encuestados por pregunta
mode = "random" # Modo de generación
path = "tests/Test6.txt" # Ruta donde guardar el output

participants, questionBlocks = generateData(K, M, Nmin, Nmax, mode)
formattedText = formatOutput(participants, questionBlocks)

with open(path, "w", encoding="utf-8") as f:
  f.write(formattedText)

# Parámetros test 7 (Pocos temas con alto N)
K = 5 # Número de temas
M = 5 # Número de preguntas por tema
Nmin = 100 # Mínimo número de encuestados por pregunta
Nmax = 150 # Máximo número de encuestados por pregunta
mode = "random" # Modo de generación
path = "tests/Test7.txt" # Ruta donde guardar el output

participants, questionBlocks = generateData(K, M, Nmin, Nmax, mode)
formattedText = formatOutput(participants, questionBlocks)

with open(path, "w", encoding="utf-8") as f:
  f.write(formattedText)

# Parámetros test 8 (Muchos temas,muchos estudiantes)
K = 200 # Número de temas
M = 100 # Número de preguntas por tema
Nmin = 20 # Mínimo número de encuestados por pregunta
Nmax = 50 # Máximo número de encuestados por pregunta
mode = "random" # Modo de generación
path = "tests/Test4.txt" # Ruta donde guardar el output


participants, questionBlocks = generateData(K, M, Nmin, Nmax, mode)
formattedText = formatOutput(participants, questionBlocks)

with open(path, "w", encoding="utf-8") as f:
  f.write(formattedText)
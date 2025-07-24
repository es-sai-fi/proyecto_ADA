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
  
# Parámetros
K = 2
M = 2
Nmin = 3
Nmax = 5
mode = "random"
path = "tests/Test4.txt"

participants, questionBlocks = generateData(K, M, Nmin, Nmax, mode)
formattedText = formatOutput(participants, questionBlocks)

with open(path, "w", encoding="utf-8") as f:
  f.write(formattedText)
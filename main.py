from classes import *

def parseAndCreateObjets(filename):
  participants = []
  questions = []
  topics = []

  with open(filename, "r", encoding="utf-8") as file:
    lines = [line.strip() for line in file]

  # Separar líneas en bloques
  participantLines = []
  questionBlocks = []
  currentBlock = []

  # Leer líneas: primero participantes, luego bloques de preguntas
  parsingQuestions = False
  for line in lines:
    if line.startswith("{") and line.endswith("}"):
      parsingQuestions = True
      currentBlock.append(line)
    elif parsingQuestions:
      if currentBlock:
        questionBlocks.append(currentBlock)
        currentBlock = []
      if line.startswith("{"):
        currentBlock.append(line)
    elif line.strip():
      participantLines.append(line)

  if currentBlock:
    questionBlocks.append(currentBlock)

  # Crear objetos Participant
  for line in participantLines:
    try:
      name, data = line.split(", Experticia:")
      expertise, opinion = map(int, data.strip().split(", Opinión:"))
      participants.append(Participant(name.strip(), opinion, expertise))
    except Exception as e:
      print(f"Error procesando participante: {line} -> {e}")

  # Crear temas y preguntas
  for block in questionBlocks:
    blockQuestions = []  # Preguntas solo de este tema
    for line in block:
      ids = list(map(int, line.strip("{}").split(",")))
      questionParticipants = [participants[i - 1] for i in ids]
      question = Question(questionParticipants)
      questions.append(question)         # Añadir al listado global
      blockQuestions.append(question)    # Añadir al tema
    topics.append(Topic(blockQuestions))

  return Survey(topics, questions, participants)

if __name__ == "__main__":
  """
  participants = []
  questions = []
  topics = []
  
  participants.append(Participant("Sofia García", 1, 6))
  participants.append(Participant("Alejandro Torres", 7, 10))
  participants.append(Participant("Valentina Rodriguez", 9, 0))
  participants.append(Participant("Juan Lopéz", 10, 1))
  participants.append(Participant("Martina Martinez", 7, 0))
  participants.append(Participant("Sebastián Pérez", 8, 9))
  participants.append(Participant("Camila Fernández", 2, 7))
  participants.append(Participant("Mateo González", 4, 7))
  participants.append(Participant("Isabella Díaz", 7, 5))
  participants.append(Participant("Daniel Ruiz", 2, 9))
  participants.append(Participant("Luciana Sánchez", 1, 7))
  participants.append(Participant("Lucas Vásquez", 6, 8))
  
  questions.append(Question([participants[9], participants[1]]))
  questions.append(Question([participants[0], participants[8], participants[11], participants[5]]))
  questions.append(Question([participants[10], participants[7], participants[6]]))
  questions.append(Question([participants[2], participants[3], participants[4]]))
  
  topics.append(Topic([questions[0], questions[1]]))
  topics.append(Topic([questions[2], questions[3]]))
  
  survey = Survey(topics, questions, participants)
  survey.execute()
  """
  
  filename = "Test1.txt"
  
  survey = parseAndCreateObjets(filename)
  survey.execute()
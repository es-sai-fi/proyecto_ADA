from array_sol_classes import *

def parseAndCreateSurvey(filename):
  participants = []
  questions = []
  topics = []

  with open(filename, "r", encoding="utf-8") as file:
    lines = [line.strip() for line in file]

  participantLines = []
  questionBlocks = []
  currentBlock = []

  # Lectura de lineas
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

  # Crear participantes
  for line in participantLines:
    try:
      name, data = line.split(", Experticia:")
      expertise, opinion = map(int, data.strip().split(", Opinión:"))
      participants.append(ArrayParticipant(name.strip(), expertise, opinion))
    except Exception as e:
      print(f"Error procesando participante: {line} -> {e}")

  # Crear temas y preguntas
  for block in questionBlocks:
    blockQuestions = []
    for line in block:
      ids = list(map(int, line.strip("{}").split(",")))
      questionParticipants = [participants[i - 1] for i in ids]
      question = ArrayQuestion(questionParticipants)
      questions.append(question)
      blockQuestions.append(question)
    topics.append(ArrayTopic(blockQuestions))

  return ArraySurvey(topics, questions, participants)

if __name__ == "__main__":
  filename = "Test1.txt"
  
  survey = parseAndCreateSurvey(filename)
  survey.execute()
from core.array_sol_classes import *
from core.tree_sol_classes import *
import time

def parseAndCreateArraySurvey(filename):
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
    topicQuestions = []
    for line in block:
      ids = list(map(int, line.strip("{}").split(",")))
      questionParticipants = [participants[i - 1] for i in ids]
      question = ArrayQuestion(questionParticipants)
      questions.append(question)
      topicQuestions.append(question)
    topics.append(ArrayTopic(topicQuestions))

  return ArraySurvey(topics, questions, participants)

def parseAndCreateTreeSurvey(path):
  participantsAux = []
  questionsAux = []
  topicsAux = []

  with open(path, "r", encoding="utf-8") as file:
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
      participantsAux.append(TreeParticipant(name.strip(), expertise, opinion))
    except Exception as e:
      print(f"Error procesando participante: {line} -> {e}")

  # Crear temas y preguntas
  for block in questionBlocks:
    topicQuestionsAux = []
    for line in block:
      ids = list(map(int, line.strip("{}").split(",")))
      questionParticipantsAux = [participantsAux[i - 1] for i in ids]
      question = TreeQuestion(questionParticipantsAux)
      questionsAux.append(question)
      topicQuestionsAux.append(question)
    topicsAux.append(TreeTopic(topicQuestionsAux))

  return TreeSurvey(topicsAux, questionsAux, participantsAux)

if __name__ == "__main__":
  path = "tests/Test1.txt"
  solution = 1
  
  if solution:
    start = time.time()
    treeSurvey = parseAndCreateTreeSurvey(path)
    treeSurvey.execute()
    end = time.time()
    print(f"Tiempo (BSTs): {end - start}")
  else:
    start = time.time()
    arraySurvey = parseAndCreateArraySurvey(path)
    arraySurvey.execute()
    end = time.time()
    print(f"Tiempo (Arrays): {end - start}")
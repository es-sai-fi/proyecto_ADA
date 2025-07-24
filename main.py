import time
import os
from core.array_sol_classes import *
from core.tree_sol_classes import *

def parseAndCreateArraySurvey(inputPath):
  participants = []
  questions = []
  topics = []

  with open(inputPath, "r", encoding="utf-8") as file:
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
  print("Configuración de ejecución")
  mode = int(input("Modo de ejecución (0: todos los tests, 1: solo el test dado): ").strip())
  
  if mode:
    inputPath = input("Ruta del test (ej. tests/Test1.txt): ").strip()
    solution = int(input("Solución a usar (0: Arrays, 1: BSTs): ").strip())
    
    if solution:
      treeSurvey = parseAndCreateTreeSurvey(inputPath)
      start = time.time()
      treeSurvey.execute()
      end = time.time()
      print(f"Tiempo (BST): {end - start}")
    else:
      arraySurvey = parseAndCreateArraySurvey(inputPath)
      start = time.time()
      arraySurvey.execute()
      end = time.time()
      print(f"Tiempo (Array): {end - start}")
  else:
    testFolder = "tests"
    testFiles = [f for f in os.listdir(testFolder) if f.endswith(".txt")]

    for i, filename in enumerate(testFiles, 1):
        inputPath = os.path.join(testFolder, filename)
        outputPathArray = f"Results{i}Array.txt"
        outputPathBST = f"Results{i}BST.txt"
        
        # Sol. Array
        arraySurvey = parseAndCreateArraySurvey(inputPath)
        start0 = time.time()
        arraySurvey.setOutputPath(outputPathArray)
        arraySurvey.execute()
        end0 = time.time()
        
        # Sol. BST
        treeSurvey = parseAndCreateTreeSurvey(inputPath)
        start1 = time.time()
        treeSurvey.setOutputPath(outputPathBST)
        treeSurvey.execute()
        end1 = time.time()
        
        print(f"\nTest{i}:")
        print(f"Tiempo (Array): {end0 - start0}")
        print(f"Tiempo (BST): {end1 - start1}")
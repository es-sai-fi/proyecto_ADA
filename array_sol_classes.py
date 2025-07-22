from auxiliar_functions import *

class ArrayParticipant:
  _identifierCounter = 1
  
  def __init__(self, name, expertise, opinion):
    self.identifier = ArrayParticipant._identifierCounter
    self.name = name
    self.expertise = expertise
    self.opinion = opinion
    ArrayParticipant._identifierCounter += 1
    
  def __str__(self):
    return f"({self.identifier}, Nombre: '{self.name}', Experticia: {self.expertise}, Opinión: {self.opinion})"
    
class ArrayQuestion:
  _identifierCounter = 1
  
  def __init__(self, participants):
    self.identifier = ArrayQuestion._identifierCounter
    self.participants = participants
    ArrayQuestion._identifierCounter += 1
    
  def setPrintIdentifier(self, printIdentifier):
    self.printIdentifier = printIdentifier
    
  def _sort(self):
    self.participants = mergeSort(self.participants, participantComparer)  
  
  def _calcData(self):
    self.numOfParticipants = len(self.participants)
    self.opinionMean = self._opinionMean()
    self.expertiseMean = self._expertiseMean()
    self.opinionMode = self._opinionMode()
    self.opinionMedian = self._opinionMedian()
    self.extremism = self._extremism()
    self.consensus = self._consensus()
    
  def _consensus(self):
    count = 0
    
    for participant in self.participants:
      if participant.opinion == self.opinionMode:
        count += 1
        
    return count / self.numOfParticipants
    
  def _extremism(self):
    count = 0
    
    for participant in self.participants:
      if participant.opinion == 0 or participant.opinion == 10:
        count += 1
        
    return count / self.numOfParticipants
    
  def _opinionMode(self):
    opinionMode = self.participants[0].opinion
    maxCount = 1
    current = self.participants[0].opinion
    count = 1

    for i in range(1, self.numOfParticipants):
      if self.participants[i].opinion == current:
        count += 1
      else:
        if count > maxCount:
          maxCount = count
          opinionMode = current
        elif count == maxCount:
          if current < opinionMode:
            opinionMode = current
        current = self.participants[i].opinion
        count = 1

    if count > maxCount:
      opinionMode = current
    elif count == maxCount:
      if current < opinionMode:
        opinionMode = current
          
    return opinionMode
  
  def _opinionMedian(self):
    if self.numOfParticipants % 2 == 1:
      return self.participants[self.numOfParticipants // 2].opinion
    else:
      i = self.numOfParticipants // 2
      
      if self.participants[i - 1].opinion < self.participants[i].opinion:
        return self.participants[i - 1].opinion
      
      return self.participants[i].opinion
      
  def _opinionMean(self):
    acc = 0
      
    for participant in self.participants:
      acc += participant.opinion
        
    return acc / self.numOfParticipants
  
  def _expertiseMean(self):
    acc = 0
      
    for participant in self.participants:
      acc += participant.expertise
        
    return acc / self.numOfParticipants   
  
class ArrayTopic:
  _identifierCounter = 1
  
  def __init__(self, questions):
    self.identifier = ArrayTopic._identifierCounter
    self.questions = questions
    ArrayTopic._identifierCounter += 1
    
    for i, question in enumerate(questions, 1):
      question.setPrintIdentifier(f"{self.identifier}.{i}")
      
    
  def _sort(self):
     self.questions = mergeSort(self.questions, questionComparer)
    
  def _calcData(self):
    self.totalNumOfParticipants = self._totalNumOfParticipants()
    self.opinionMeanOfMeans = self._opinionMeanOfMeans()
    self.expertiseMeanOfMeans = self._expertiseMeanOfMeans()
      
  def _totalNumOfParticipants(self):
    acc = 0
    
    for question in self.questions:
      acc += question.numOfParticipants
    
    return acc

  def _opinionMeanOfMeans(self):
    acc = 0
    
    for question in self.questions:
      acc += question.opinionMean
      
    return acc / len(self.questions)

  def _expertiseMeanOfMeans(self):
    acc = 0
    
    for question in self.questions:
      acc += question.expertiseMean
      
    return acc / len(self.questions)
    
class ArraySurvey:
  def __init__(self, topics, questions, participants):
    self.topics = topics
    self.questions = questions
    self.participants = participants
    
  def execute(self):
    self._sortQuestionParticipants()
    self._calcData()
    self._sortTopicQuestions()
    self._sort()
    self._calcAdditionalData()
    self._printSolution()
  
  def _printSolution(self):
    outputLines = []

    outputLines.append("Resultados de la encuesta:")
    outputLines.append("")
    for topic in self.topics:
      outputLines.append(f"[{topic.opinionMeanOfMeans:.2f}] Tema {topic.identifier}:")
      for question in topic.questions:
        participantIds = ", ".join(str(p.identifier) for p in question.participants)
        outputLines.append(f"\t[{question.opinionMean:.2f}] Pregunta {question.printIdentifier}: ({participantIds})")
      outputLines.append("")

    outputLines.append("Lista de encuestados:")
    for participant in self.participants:
      outputLines.append(f"\t{participant}")
    outputLines.append("")

    outputLines.append("Resultados:")
    outputLines.append(f"\tPregunta con mayor promedio de opinión: [{self.questionHighestOpinionMean.opinionMean:.2f}] Pregunta: {self.questionHighestOpinionMean.printIdentifier}")
    outputLines.append(f"\tPregunta con menor promedio de opinión: [{self.questionLowestOpinionMean.opinionMean:.2f}] Pregunta: {self.questionLowestOpinionMean.printIdentifier}")
    outputLines.append(f"\tPregunta con mayor promedio de experticia: [{self.questionHighestExpertiseMean.expertiseMean:.2f}] Pregunta: {self.questionHighestExpertiseMean.printIdentifier}")
    outputLines.append(f"\tPregunta con menor promedio de experticia: [{self.questionLowestExpertiseMean.expertiseMean:.2f}] Pregunta: {self.questionLowestExpertiseMean.printIdentifier}")
    outputLines.append(f"\tPregunta con mayor mediana de opinión: [{self.questionHighestOpinionMedian.opinionMedian}] Pregunta: {self.questionHighestOpinionMedian.printIdentifier}")
    outputLines.append(f"\tPregunta con menor mediana de opinión: [{self.questionLowestOpinionMedian.opinionMedian}] Pregunta: {self.questionLowestOpinionMedian.printIdentifier}")
    outputLines.append(f"\tPregunta con mayor moda de opinión: [{self.questionHighestOpinionMode.opinionMode}] Pregunta: {self.questionHighestOpinionMode.printIdentifier}")
    outputLines.append(f"\tPregunta con menor moda de opinión: [{self.questionLowestOpinionMode.opinionMode}] Pregunta: {self.questionLowestOpinionMode.printIdentifier}")
    outputLines.append(f"\tPregunta con mayor extremismo: [{self.questionHighestExtremism.extremism:.2f}] Pregunta: {self.questionHighestExtremism.printIdentifier}")
    outputLines.append(f"\tPregunta con mayor consenso: [{self.questionHighestConsensus.consensus:.2f}] Pregunta: {self.questionHighestConsensus.printIdentifier}")

    result_text = "\n".join(outputLines)

    with open("Results.txt", "w", encoding="utf-8") as f:
      f.write(result_text)

  def _calcAdditionalData(self):
    self.questionHighestOpinionMean = self._calcHighestOpinionMean()
    self.questionLowestOpinionMean = self._calcLowestOpinionMean()
    self.questionHighestExpertiseMean = self._calcHighestExpertiseMean()
    self.questionLowestExpertiseMean = self._calcLowestExpertiseMean()
    self.questionHighestOpinionMedian = self._calcHighestOpinionMedian()
    self.questionLowestOpinionMedian = self._calcLowestOpinionMedian()
    self.questionHighestOpinionMode = self._calcHighestOpinionMode()
    self.questionLowestOpinionMode = self._calcLowestOpinionMode()
    self.questionHighestExtremism = self._calcHighestExtremism()
    self.questionHighestConsensus = self._calcHighestConsensus()
    
  def _calcHighestOpinionMean(self):
    questionAux = self.questions[0]
    highest = questionAux.opinionMean

    for question in self.questions:
      if question.opinionMean > highest:
        questionAux = question
        highest = question.opinionMean
      elif question.opinionMean == highest:
        if question.identifier < questionAux.identifier:
          questionAux = question

    return questionAux

  def _calcLowestOpinionMean(self):
    questionAux = self.questions[0]
    lowest = questionAux.opinionMean

    for question in self.questions:
      if question.opinionMean < lowest:
        questionAux = question
        lowest = question.opinionMean
      elif question.opinionMean == lowest:
        if question.identifier < questionAux.identifier:
          questionAux = question
          
    return questionAux
  
  def _calcHighestExpertiseMean(self):
    questionAux = self.questions[0]
    highest = questionAux.expertiseMean

    for question in self.questions:
      if question.expertiseMean > highest:
        questionAux = question
        highest = question.expertiseMean
      elif question.expertiseMean == highest:
        if question.identifier < questionAux.identifier:
          questionAux = question
          
    return questionAux

  def _calcLowestExpertiseMean(self):
    questionAux = self.questions[0]
    lowest = questionAux.expertiseMean

    for question in self.questions:
      if question.expertiseMean < lowest:
        questionAux = question
        lowest = question.expertiseMean
      elif question.expertiseMean == lowest:
        if question.identifier < questionAux.identifier:
          questionAux = question
          
    return questionAux

  def _calcHighestOpinionMedian(self):
    questionAux = self.questions[0]
    highest = questionAux.opinionMedian

    for question in self.questions:
      if question.opinionMedian > highest:
        questionAux = question
        highest = question.opinionMedian
      elif question.opinionMedian == highest:
        if question.identifier < questionAux.identifier:
          questionAux = question
          
    return questionAux

  def _calcLowestOpinionMedian(self):
    questionAux = self.questions[0]
    lowest = questionAux.opinionMedian

    for question in self.questions:
      if question.opinionMedian < lowest:
        questionAux = question
        lowest = question.opinionMedian
      elif question.opinionMedian == lowest:
        if question.identifier < questionAux.identifier:
          questionAux = question
          
    return questionAux

  def _calcHighestOpinionMode(self):
    questionAux = self.questions[0]
    highest = -1

    for question in self.questions:
      if question.opinionMode > highest:
        questionAux = question
        highest = question.opinionMode
      elif question.opinionMode == highest:
        if question.identifier < questionAux.identifier:
          questionAux = question
          
    return questionAux

  def _calcLowestOpinionMode(self):
    questionAux = self.questions[0]
    lowest = 11

    for question in self.questions:
      if question.opinionMode < lowest:
        questionAux = question
        lowest = question.opinionMode
      elif question.opinionMode == lowest:
        if question.identifier < questionAux.identifier:
          questionAux = question
          
    return questionAux

  def _calcHighestExtremism(self):
    questionAux = self.questions[0]
    highest = questionAux.extremism

    for question in self.questions:
      if question.extremism > highest:
        questionAux = question
        highest = question.extremism
      elif question.extremism == highest:
        if question.identifier < questionAux.identifier:
          questionAux = question
          
    return questionAux

  def _calcHighestConsensus(self):
    questionAux = self.questions[0]
    highest = questionAux.consensus

    for question in self.questions:
      if question.consensus > highest:
        questionAux = question
        highest = question.consensus
      elif question.consensus == highest:
        if question.identifier < questionAux.identifier:
          questionAux = question
          
    return questionAux
    
  def _calcData(self):
    for question in self.questions:
      question._calcData()
      
    for topic in self.topics:
      topic._calcData()
  
  def _sortQuestionParticipants(self):
    for question in self.questions:
      question._sort()
      
  def _sortTopicQuestions(self):
    for topic in self.topics:
      topic._sort()

  def _sort(self):
    self.topics = mergeSort(self.topics, topicListComparer)
    self.participants = mergeSort(self.participants, participantListComparer)
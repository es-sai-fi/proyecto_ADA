from auxiliar_functions import *

class Tree:
  def __init__(self, root, nodes):
    self.root = root
    self.nodes = nodes
  
class Node:
  def __init__(self, parent, left, right, key):
    self.parent = parent
    self.left = left
    self.right = right
    self.key = key

class Participant:
  _identifierCounter = 1
  
  def __init__(self, name, expertise, opinion):
    self.identifier = Participant._identifierCounter
    self.name = name
    self.expertise = expertise
    self.opinion = opinion
    Participant._identifierCounter += 1
    
  def __str__(self):
    return str(self.identifier)
    
class Question:
  _identifierCounter = 1
  
  def __init__(self, participants):
    self.identifier = Question._identifierCounter
    self.participants = participants
    Question._identifierCounter += 1
    
  def _sort(self):
    self.participants = mergeSort(self.participants, participantComparer)  
  
  def _calcData(self):
    self.numOfParticipants = len(self.participants)
    self.opinionMean = self._opinionMean()
    self.expertiseMean = self._expertiseMean()
    self.mode = self._mode()
    self.median = self._median()
    self.extremism = self._extremism()
    self.consensus = self._consensus()
    
  def _consensus(self):
    count = 0
    
    for participant in self.participants:
      if participant.opinion == self.mode:
        count += 1
        
    return count / self.numOfParticipants
    
  def _extremism(self):
    count = 0
    
    for participant in self.participants:
      if participant.opinion == 0 or participant.opinion == 1:
        count += 1
        
    return count / self.numOfParticipants
    
  def _mode(self):
    mode = self.participants[0].opinion
    max_count = 1
    current = self.participants[0].opinion
    count = 1

    for i in range(1, self.numOfParticipants):
      if self.participants[i].opinion == current:
        count += 1
      else:
        if count > max_count:
          max_count = count
          mode = current
        current = self.participants[i].opinion
        count = 1

    if count > max_count:
      mode = current

    return mode
  
  def _median(self):
    if self.numOfParticipants % 2 == 1:
      return self.participants[self.numOfParticipants // 2].opinion
    else:
      i = self.numOfParticipants // 2
      return (self.participants[i - 1].opinion + self.participants[i].opinion) / 2
      
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
  
  def __str__(self):
    participant_ids = ", ".join(str(p) for p in self.participants)
    return f"[{self.opinionMean:.2f}] Pregunta {self.identifier}: ({participant_ids})"
  
class Topic:
  _identifierCounter = 1
  
  def __init__(self, questions):
    self.identifier = Topic._identifierCounter
    self.questions = questions
    Topic._identifierCounter += 1
    
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
  
  def __str__(self):
    question_lines = "\n\t" + "\n\t".join(str(q) for q in self.questions)
    return f"[{self.opinionMeanOfMeans:.2f}] Tema {self.identifier}: {question_lines}"
    
class Survey:
  def __init__(self, topics, questions, participants):
    self.topics = topics
    self.questions = questions
    self.participants = participants
    
  def execute(self):
    self._sortQuestionParticipants()
    self._calcData() # La mediana requiere que los participantes estén ordenados
    self._sortTopicQuestions()
    self._sort()
    self._calcAdditionalData()
    self._printSolution()
  
  def _printSolution(self):
    for topic in self.topics:
      print(str(topic))

    print()
    print(f"Pregunta con mayor promedio: {self.questionHighestMean.identifier}")
    print(f"Pregunta con menor promedio: {self.questionLowestMean.identifier}")
    print(f"Pregunta con mayor mediana: {self.questionHighestMedian.identifier}")
    print(f"Pregunta con menor mediana: {self.questionLowestMedian.identifier}")
    print(f"Pregunta con mayor moda: {self.questionHighestMode.identifier}")
    print(f"Pregunta con menor moda: {self.questionLowestMode.identifier}")
    print(f"Pregunta con mayor extremismo: {self.questionHighestExtremism.identifier}")
    print(f"Pregunta con mayor consenso: {self.questionHighestconsensus.identifier}")

    
  def _calcAdditionalData(self):
    self.questionHighestMean = self._calcHighestMean()
    self.questionLowestMean = self._calcLowestMean()
    self.questionHighestMedian = self._calcHighestMedian()
    self.questionLowestMedian = self._calcLowestMedian()
    self.questionHighestMode = self._calcHighestMode()
    self.questionLowestMode = self._calcLowestMode()
    self.questionHighestExtremism = self._calcHighestExtremism()
    self.questionHighestconsensus = self._calcHighestconsensus()
    
  def _calcHighestMean(self):
    question_aux = self.questions[0]
    highest = question_aux.opinionMean

    for question in self.questions:
      if question.opinionMean > highest:
        question_aux = question
        highest = question.opinionMean

    return question_aux

  def _calcLowestMean(self):
    question_aux = self.questions[0]
    lowest = question_aux.opinionMean

    for question in self.questions:
      if question.opinionMean < lowest:
        question_aux = question
        lowest = question.opinionMean

    return question_aux

  def _calcHighestMedian(self):
    question_aux = self.questions[0]
    highest = question_aux.median

    for question in self.questions:
      if question.median > highest:
        question_aux = question
        highest = question.median

    return question_aux

  def _calcLowestMedian(self):
    question_aux = self.questions[0]
    lowest = question_aux.median

    for question in self.questions:
      if question.median < lowest:
        question_aux = question
        lowest = question.median

    return question_aux

  def _calcHighestMode(self):
    question_aux = self.questions[0]
    highest = question_aux.mode

    for question in self.questions:
      if question.mode > highest:
        question_aux = question
        highest = question.mode

    return question_aux

  def _calcLowestMode(self):
    question_aux = self.questions[0]
    lowest = question_aux.mode

    for question in self.questions:
      if question.mode < lowest:
        question_aux = question
        lowest = question.mode

    return question_aux

  def _calcHighestExtremism(self):
    question_aux = self.questions[0]
    highest = question_aux.extremism

    for question in self.questions:
      if question.extremism > highest:
        question_aux = question
        highest = question.extremism

    return question_aux

  def _calcHighestconsensus(self):
    question_aux = self.questions[0]
    highest = question_aux.consensus

    for question in self.questions:
      if question.consensus > highest:
        question_aux = question
        highest = question.consensus

    return question_aux
    
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
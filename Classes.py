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
    
class Question:
  _identifierCounter = 1
  
  def __init__(self, participants):
    self.identifier = Question._identifierCounter
    self.participants = participants
    Question._identifierCounter += 1
    
  def _sort(self):
    self.participants = mergeSort(self.participants, participantComparer)  
  
  def _calcAuxData(self):
    self.numOfParticipants = len(self.participants)
    self.opinionMean = self._opinionMean()
    self.expertiseMean = self._expertiseMean()
      
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
  
class Topic:
  _identifierCounter = 1
  
  def __init__(self, questions):
    self.identifier = Topic._identifierCounter
    self.questions = questions
    Topic._identifierCounter += 1
    
  def _sort(self):
     self.questions = mergeSort(self.questions, questionComparer)
    
  def _calcAuxData(self):
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
    
class Survey:
  def __init__(self, topics, questions, participants):
    self.topics = topics
    self.questions = questions
    self.participants = participants
    
  def execute(self):
    self._calcAuxData()
    self._execSorting()
    self._calcAdditionalData()
    self._printSolution()
    
  def _calcAdditionalData():
    pass
  
  def _printSolution():
    pass
    
  def _calcAuxData(self):
    for question in self.questions:
      question._calcAuxData()
      
    for topic in self.topics:
      topic._calcAuxData()
  
  def _execSorting(self):
    for question in self.questions:
      question._sort()
    
    for topic in self.topics:
      topic._sort()
      
    self._sort()
    
  def _sort(self):
    self.topics = mergeSort(self.topics, topicListComparer)
    self.participants = mergeSort(self.participants, participantListComparer)
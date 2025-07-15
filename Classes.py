def participantListComparer(a, b):
  if a.expertise == b.expertise:
    return a.identifier > b.identifier
  else:
    return a.expertise > b.expertise
  
def mergeSort(arr, comparer):
  if len(arr) <= 1:
    return arr
    
  midIndex = len(arr) // 2
  left = mergeSort(arr[:midIndex], comparer)
  right = mergeSort(arr[midIndex:], comparer)
    
  return merge(left, right, comparer)

def merge(left, right, comparer):
  result = []
  i, j = 0
    
  while i < len(left) and j < len(right):
    a = left[i]
    b = right[j]
      
    if comparer(a, b):
      result.append(a)
      i += 1
    else:
      result.append(b)
      j += 1
      
  while i < len(left):
    result.append(left[i])
    i += 1
      
  while j < len(right):
    result.append(right[j])  
    j += 1  
      
  return result

class ParticipantArray:
  def __init__(self, elements):
    self.elements = elements
    self.size = len(elements)
    self.opinionMean = self._getOpinionMean()
    self.experiseMean = self._getExperticeMean()
    self.sort()
  
  def sort(self):
    self.elements = mergeSort(self.elements, self._comparer)
    
  def _comparer(self, a, b):
    # Si hay empate en opinión
    if a.opinion == b.opinion:
      # Si hay empate en experticia
      if a.expertise == b.expertise:
        return a.identifier > b.identifier
      else:
        return a.expertise > b.expertise
    else:
      return a.opinion > b.opinion
    
  def _getOpinionMean(self):
    acc = 0
    
    for element in self.elements:
      acc += element.opinion
      
    return acc / self.size
  
  def _getExperticeMean(self):
    acc = 0
    
    for element in self.elements:
      acc += element.expertise
      
    return acc / self.size   
   
class QuestionArray:
  def __init__(self, elements):
    self.elements = elements
    self.size = len(elements)
    self.totalNumOfParticipants = self.getTotalNumOfParticipants()
    self.opinionMeanOfMeans = self.getOpinionMeanOfMeans()
    self.expertiseMeanOfMeans = self.getExpertiseMeanOfMeans()
    self.sort()
  
  def sort(self):
    self.elements = mergeSort(self.elements, self._comparer)
    
  def getTotalNumOfParticipants(self):
    acc = 0
    
    for element in self.elements:
      acc += element.numOfParticipants
    
    return acc
    
  def _comparer(self, a, b):
    # Si hay empate en promedio de opinión
    if a.opinion == b.opinion:
      # Si hay empate en promedio de experticia
      if a.expertise == b.expertise:
        return a.identifier > b.identifier
      else:
        return a.expertise > b.expertise
    else:
      return a.opinion > b.opinion
  
  def _getOpinionMeanOfMeans(self):
    acc = 0
    
    for element in self.elements:
      acc += element.opinionMean
      
    return acc / self.size
  
  def _getExpertiseMeanOfMeans(self):
    acc = 0
    
    for element in self.elements:
      acc += element.expertiseMean
      
    return acc / self.size

class Tree:
  def __init__(self, root, nodes):
    self.root = root
    self.nodes = nodes
    
  def getSize(self):
    pass
  
  def getOpinionMean(self):
    pass
  
  def getExperticeMean(self):
    pass
  
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
    self.numOfParticipants = participants.size
    self.opinionMean = participants.opinionMean
    self.expertiseMean = participants.expertiseMean
    Question._identifierCounter += 1
  
class Topic:
  _identifierCounter = 1
  
  def __init__(self, questions):
    self.identifier = Topic._identifierCounter
    self.questions = questions
    self.totalNumOfParticipants = questions.totalNumOfParticipants
    self.opinionMeanOfMeans = questions.opinionMeanOfMeans
    self.expertiseMeanOfMeans = questions.expertiseMeanOfMeans
    Topic._identifierCounter += 1
    
class SurveyController:
  def __init__(self, topics, participants):
    self.topics = topics
    
  def sort(self):
    self.topics = mergeSort(self.topics, self._topicListComparer)
    self.participants = mergeSort(self.participants, self._participantListComparer)
    
  def printInfo(self):
    pass    
    
  def _topicListComparer(self, a, b):
    # Si hay empate en promedio de promedios de opinión
    if a.opinionMeanOfMeans == b.opinionMeanOfMeans:
      # Si hay empate en promedio de promedios de experticia
      if a.expertiseMeanOfMeans == b.expertiseMeanOfMeans:
        return a.totalNumOfParticipants > b.totalNumOfParticipants
      else:
        return a.expertiseMeanOfMeans > b.expertiseMeanOfMeans
    else:
      return a.opinionMeanOfMeans > b.opinionMeanOfMeans
    
  def _participantListComparer(self, a, b):
    # Si hay empate en promedio de experticia
    if a.expertise == b.expertise:
      return a.identifier > b.identifier
    else:
      return a.expertise > b.expertise
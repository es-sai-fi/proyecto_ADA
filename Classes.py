class ParticipantArray:
  def __init__(self, elements):
    self.elements = elements
    self.size = self.getSize()
    
  def getSize(self):
    count = 0
    
    for _ in self.elements:
      count += 1
      
    return count
    
  def getOpinionMean(self):
    sum = 0
    
    for element in self.elements:
      sum += element.opinion
      
    return sum/self.size
  
  def getExperticeMean(self):
    sum = 0
    
    for element in self.elements:
      sum += element.expertise
      
    return sum/self.size
  
class QuestionArray:
  def __init__(self, elements):
    self.elements = elements
    
  def getSize(self):
    count = 0
    
    for _ in self.elements:
      count += 1
      
    return count
  
  def getOpinionMean(self):
    sum = 0
    
    for element in self.elements:
      sum += element.opinionMean
      
    return sum/self.size
  
  def getExperticeMean(self):
    sum = 0
    
    for element in self.elements:
      sum += element.expertiseMean
      
    return sum/self.size

class Tree:
  def __init__(self, root, nodes):
    self.root = root
    self.nodes = nodes
    
  def getNumOfParticipants(self):
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
  def __init__(self, participants):
    self.participants = participants
    self.participantsSize = participants.size
    self.opinionMean = participants.getOpinionMean()
    self.expertiseMean = participants.getExpertiseMean()
  
class Topic:
  def __init__(self, questions):
    self.questions = questions
    self.participants = questions.size
    self.opinionMeanOfMeans = questions.getOpinionMean()
    self.expertiseMeanOfMeans = questions.getExpertiseMean()
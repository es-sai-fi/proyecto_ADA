class ParticipantArray:
  def __init__(self, elements):
    self.elements = elements
    
  def getNumOfParticipants(self):
    pass
  
  def getOpinionMean(self):
    pass
  
  def getExperticeLevelMean(self):
    pass
  
class QuestionArray:
  def __init__(self, elements):
    self.elements = elements
    
  def getNumOfParticipants(self):
    pass
  
  def getOpinionMean(self):
    pass
  
  def getExperticeLevelMean(self):
    pass

class Tree:
  def __init__(self, root, nodes):
    self.root = root
    self.nodes = nodes
    
  def getNumOfParticipants(self):
    pass
  
  def getOpinionMean(self):
    pass
  
  def getExperticeLevelMean(self):
    pass
  
class Node:
  def __init__(self, parent, left, right, key):
    self.parent = parent
    self.left = left
    self.right = right
    self.key = key

class Participant:
  def __init__(self, name, expertiseLevel, opinion):
    self.name = name
    self.expertiseLevel = expertiseLevel
    self.opinion = opinion
    
class Question:
  def __init__(self, participants):
    self.participants = participants
    self.participantsSize = participants.getNumOfParticipants()
    self.opinionMean = participants.getOpinionMean()
    self.expertiseLevelMean = participants.getExpertiseLevelMean()
  
class Topic:
  def __init__(self, questions):
    self.questions = questions
    self.participants = questions.getNumOfParticipants()
    self.opinionMeanOfMeans = questions.getOpinionMean()
    self.expertiseLevelMeanOfMeans = questions.getExpertiseLevelMean()
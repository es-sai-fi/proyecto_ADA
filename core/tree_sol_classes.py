from core.auxiliar_functions import *

class ParticipantTree:
  def __init__(self, root=None):
    self.root = root
  
  def treeInsert(self, node):
    y = None
    x = self.root
    
    while x != None:
      y = x
      
      if participantComparer(node.key, x.key):
        x = x.left
      else:
        x = x.right
    
    node.parent = y

    if y is None:
      self.root = node
    else:
      if participantComparer(node.key, y.key):
        y.left = node
      else:
        y.right = node
        
  def countParticipants(self):
    count = 0
    current = self.root

    while current:
      if current.left is None:
          count += 1
          current = current.right
      else:
        pre = current.left
        
        while pre.right and pre.right != current:
          pre = pre.right

        if pre.right is None:
          pre.right = current
          current = current.left
        else:
          pre.right = None
          count += 1
          current = current.right

    return count
  
class QuestionTree:
  def __init__(self, root=None):
    self.root = root
  
  def treeInsert(self, node):
    y = None
    x = self.root
    
    while x != None:
      y = x
      
      if questionComparer(node.key, x.key):
        x = x.left
      else:
        x = x.right
    
    node.parent = y

    if y is None:
      self.root = node
    else:
      if questionComparer(node.key, y.key):
        y.left = node
      else:
        y.right = node
        

  
  def countQuestions(self):
    count = 0
    current = self.root

    while current:
      if current.left is None:
          count += 1
          current = current.right
      else:
        pre = current.left
        
        while pre.right and pre.right != current:
          pre = pre.right

        if pre.right is None:
          pre.right = current
          current = current.left
        else:
          pre.right = None
          count += 1
          current = current.right

    return count
 
class TopicTree:
  def __init__(self, root=None):
    self.root = root
  
  def treeInsert(self, node):
    y = None
    x = self.root
    
    while x != None:
      y = x
      
      if topicListComparer(node.key, x.key):
        x = x.left
      else:
        x = x.right
    
    node.parent = y

    if y is None:
      self.root = node
    else:
      if topicListComparer(node.key, y.key):
        y.left = node
      else:
        y.right = node
  
class Node:
  def __init__(self, key, parent=None, left=None, right=None):
    self.key = key
    self.parent = parent
    self.left = left
    self.right = right

class TreeParticipant:
  _identifierCounter = 1
  
  def __init__(self, name, expertise, opinion):
    self.identifier = TreeParticipant._identifierCounter
    self.name = name
    self.expertise = expertise
    self.opinion = opinion
    TreeParticipant._identifierCounter += 1
    
  def __str__(self):
    return f"({self.identifier}, Nombre: '{self.name}', Experticia: {self.expertise}, Opinión: {self.opinion})"
    
class TreeQuestion:
  _identifierCounter = 1
  
  def __init__(self, participantsAux):
    self.identifier = TreeQuestion._identifierCounter
    self.participantsAux = participantsAux
    self.participantTree = ParticipantTree()
    TreeQuestion._identifierCounter += 1
  
  def setPrintIdentifier(self, printIdentifier):
    self.printIdentifier = printIdentifier
  
  def _initTree(self):
    self.participantTree = ParticipantTree()
    for participant in self.participantsAux:
      self.participantTree.treeInsert(Node(participant))   
    self._calcData() 
    
    
  def _calcData(self):
    self.numOfParticipants = self.participantTree.countParticipants()
    self.opinionMean = self._calcOpinionMean()
    self.expertiseMean = self._calcExpertiseMean()
    self.opinionMode = self._calcOpinionMode()
    self.opinionMedian = self._calcOpinionMedian()
    self.extremism = self._calcExtremism()
    self.consensus = self._calcConsensus()

  def _calcOpinionMean(self):
    acc = 0
    current = self.participantTree.root

    while current:
      if current.left is None:
        acc += current.key.opinion
        current = current.right
      else:
        pre = current.left
        
        while pre.right and pre.right != current:
          pre = pre.right

        if pre.right is None:
          pre.right = current
          current = current.left
        else:
          pre.right = None
          acc += current.key.opinion
          current = current.right

    return acc / self.numOfParticipants     
  
  def _calcExpertiseMean(self):
    acc = 0
    current = self.participantTree.root

    while current:
      if current.left is None:
        acc += current.key.expertise
        current = current.right
      else:
        pre = current.left
        
        while pre.right and pre.right != current:
          pre = pre.right

        if pre.right is None:
          pre.right = current
          current = current.left
        else:
          pre.right = None
          acc += current.key.expertise
          current = current.right

    return acc / self.numOfParticipants    
  
  def _calcOpinionMode(self):
    current = self.participantTree.root
    prevValue = None
    currentCount = 0
    maxCount = 0
    mode = None

    while current:
      if current.left is None:
        val = current.key.opinion

        if val == prevValue:
          currentCount += 1
        else:
          currentCount = 1
          prevValue = val

        if currentCount > maxCount:
          maxCount = currentCount
          mode = val
        elif currentCount == maxCount:
          if val < mode:
            mode = val

        current = current.right

      else:
        pre = current.left
        
        while pre.right and pre.right != current:
          pre = pre.right

        if pre.right is None:
          pre.right = current
          current = current.left
        else:
          pre.right = None
          val = current.key.opinion

          if val == prevValue:
            currentCount += 1
          else:
            currentCount = 1
            prevValue = val

          if currentCount > maxCount:
            maxCount = currentCount
            mode = val
          elif currentCount == maxCount:
            if val < mode:
              mode = val

          current = current.right

    return mode

  def _calcOpinionMedian(self):
    total = self.numOfParticipants
    current = self.participantTree.root
    count = 0
    median1 = None
    median2 = None
    isEven = (total % 2 == 0)
    middle1 = total // 2
    middle2 = middle1 + 1 

    while current:
      if current.left is None:
        count += 1
        if count == middle1:
          median1 = current.key.opinion
        if count == middle2:
          median2 = current.key.opinion
          break
        current = current.right
      else:
        pre = current.left
        while pre.right and pre.right != current:
          pre = pre.right

        if pre.right is None:
          pre.right = current
          current = current.left
        else:
          pre.right = None
          count += 1
          if count == middle1:
            median1 = current.key.opinion
          if count == middle2:
            median2 = current.key.opinion
            break
          current = current.right

    if isEven:
      if median1 < median2:
        return median1
      else:
        return median2
    else:
      return median2
    
  def _calcExtremism(self):
    acc = 0
    current = self.participantTree.root

    while current:
      if current.left is None:
        if current.key.opinion == 0 or current.key.opinion == 10:
          acc += 1
        current = current.right
      else:
        pre = current.left
        
        while pre.right and pre.right != current:
          pre = pre.right

        if pre.right is None:
          pre.right = current
          current = current.left
        else:
          pre.right = None
          if current.key.opinion == 0 or current.key.opinion == 10:
            acc += 1
          current = current.right

    return acc / self.numOfParticipants 
  
  def _calcConsensus(self):
    acc = 0
    current = self.participantTree.root

    while current:
      if current.left is None:
        if current.key.opinion == self.opinionMode:
          acc += 1
        current = current.right
      else:
        pre = current.left
        
        while pre.right and pre.right != current:
          pre = pre.right

        if pre.right is None:
          pre.right = current
          current = current.left
        else:
          pre.right = None
          if current.key.opinion == self.opinionMode:
            acc += 1
          current = current.right

    return acc / self.numOfParticipants 
  
class TreeTopic:
  _identifierCounter = 1
  
  def __init__(self, questionsAux):
    self.identifier = TreeTopic._identifierCounter
    self.questionsAux = questionsAux
    TreeTopic._identifierCounter += 1
  
  def _initTree(self):
    self.questionTree = QuestionTree()
    for i, question in enumerate(self.questionsAux, 1):
      question.setPrintIdentifier(f"{self.identifier}.{i}")
      self.questionTree.treeInsert(Node(question))
    self._calcData()
        
  def _calcData(self):
    self.totalNumOfParticipants = self._calcTotalNumOfParticipants()
    self.numOfQuestions = self.questionTree.countQuestions()
    self.opinionMeanOfMeans = self._calcOpinionMeanOfMeans()
    self.expertiseMeanOfMeans = self._calcExpertiseMeanOfMeans()
    
  def _calcTotalNumOfParticipants(self):
    total = 0
    current = self.questionTree.root

    while current:
      if current.left is None:
        total += current.key.participantTree.countParticipants()
        current = current.right
      else:
        pre = current.left
        
        while pre.right and pre.right != current:
          pre = pre.right

        if pre.right is None:
          pre.right = current
          current = current.left
        else:
          pre.right = None
          total += current.key.participantTree.countParticipants()
          current = current.right

    return total    
     
  def _calcOpinionMeanOfMeans(self):
    acc = 0
    current = self.questionTree.root

    while current:
      if current.left is None:
        acc += current.key.opinionMean
        current = current.right
      else:
        pre = current.left
        
        while pre.right and pre.right != current:
          pre = pre.right

        if pre.right is None:
          pre.right = current
          current = current.left
        else:
          pre.right = None
          acc += current.key.opinionMean
          current = current.right

    return acc / self.numOfQuestions     
  
  def _calcExpertiseMeanOfMeans(self):
    acc = 0
    current = self.questionTree.root

    while current:
      if current.left is None:
        acc += current.key.expertiseMean
        current = current.right
      else:
        pre = current.left
        
        while pre.right and pre.right != current:
          pre = pre.right

        if pre.right is None:
          pre.right = current
          current = current.left
        else:
          pre.right = None
          acc += current.key.expertiseMean
          current = current.right

    return acc / self.numOfQuestions     
 
class TreeSurvey:
  def __init__(self, topicsAux, questionsAux, participantsAux, outputPath="Results.txt"):
    self.topicsAux = topicsAux
    self.questionsAux = questionsAux
    self.participantsAux = participantsAux
    self.outputPath = outputPath
  
  def execute(self):
    self._initTrees() # Crea los árboles para cada topic y question
    self._calcData()
    self._printSolution()
    
  def setOutputPath(self, outputPath):
    self.outputPath = outputPath
  
  def _initTrees(self):
    self.topicTree = TopicTree()
    self.questionTree = QuestionTree()
    self.participantTree = ParticipantTree()
    for participant in self.participantsAux:
      self.participantTree.treeInsert(Node(participant))
    for question in self.questionsAux:
      question._initTree()
      self.questionTree.treeInsert(Node(question))
    for topic in self.topicsAux:
      topic._initTree()
      self.topicTree.treeInsert(Node(topic))
  
  def _printSolution(self):
    outputLines = []

    outputLines.append("Resultados de la encuesta (BSTs):")
    outputLines.append("")
    for topic in self.topicsAux:
      outputLines.append(f"[{topic.opinionMeanOfMeans:.2f}] Tema {topic.identifier}:")
      for question in topic.questionsAux:
        participantIds = ", ".join(str(p.identifier) for p in question.participantsAux)
        outputLines.append(f"\t[{question.opinionMean:.2f}] Pregunta {question.printIdentifier}: ({participantIds})")
      outputLines.append("")

    outputLines.append("Lista de encuestados:")
    for participant in self.participantsAux:
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

    resultText = "\n".join(outputLines)

    with open(self.outputPath, "w", encoding="utf-8") as f:
      f.write(resultText)

  def _calcData(self):
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
    current = self.questionTree.root
    bestQuestion = None
    highest = -1

    while current:
      if current.left is None:
        q = current.key
        if q.opinionMean > highest:
          bestQuestion = q
          highest = q.opinionMean
        elif q.opinionMean == highest and q.identifier < bestQuestion.identifier:
          bestQuestion = q
        current = current.right
      else:
        pre = current.left
        
        while pre.right and pre.right != current:
          pre = pre.right

        if pre.right is None:
          pre.right = current
          current = current.left
        else:
          pre.right = None
          q = current.key
          if q.opinionMean > highest:
            bestQuestion = q
            highest = q.opinionMean
          elif q.opinionMean == highest and q.identifier < bestQuestion.identifier:
            bestQuestion = q
          current = current.right

    return bestQuestion 
  
  def _calcLowestOpinionMean(self):
    current = self.questionTree.root
    bestQuestion = None
    lowest = 11

    while current:
      if current.left is None:
        q = current.key
        if q.opinionMean < lowest:
          bestQuestion = q
          lowest = q.opinionMean
        elif q.opinionMean == lowest and q.identifier < bestQuestion.identifier:
          bestQuestion = q
        current = current.right
      else:
        pre = current.left
        
        while pre.right and pre.right != current:
          pre = pre.right

        if pre.right is None:
          pre.right = current
          current = current.left
        else:
          pre.right = None
          q = current.key
          if q.opinionMean < lowest:
            bestQuestion = q
            lowest = q.opinionMean
          elif q.opinionMean == lowest and q.identifier < bestQuestion.identifier:
            bestQuestion = q
          current = current.right

    return bestQuestion 
  
  def _calcHighestExpertiseMean(self):
    current = self.questionTree.root
    bestQuestion = None
    highest = -1

    while current:
      if current.left is None:
        q = current.key
        if q.expertiseMean > highest:
          bestQuestion = q
          highest = q.expertiseMean
        elif q.expertiseMean == highest and q.identifier < bestQuestion.identifier:
          bestQuestion = q
        current = current.right
      else:
        pre = current.left
        
        while pre.right and pre.right != current:
          pre = pre.right

        if pre.right is None:
          pre.right = current
          current = current.left
        else:
          pre.right = None
          q = current.key
          if q.expertiseMean > highest:
            bestQuestion = q
            highest = q.expertiseMean
          elif q.expertiseMean == highest and q.identifier < bestQuestion.identifier:
            bestQuestion = q
          current = current.right

    return bestQuestion 
  
  def _calcLowestExpertiseMean(self):
    current = self.questionTree.root
    bestQuestion = None
    lowest = 11

    while current:
      if current.left is None:
        q = current.key
        if q.expertiseMean < lowest:
          bestQuestion = q
          lowest = q.expertiseMean
        elif q.expertiseMean == lowest and q.identifier < bestQuestion.identifier:
          bestQuestion = q
        current = current.right
      else:
        pre = current.left
        
        while pre.right and pre.right != current:
          pre = pre.right

        if pre.right is None:
          pre.right = current
          current = current.left
        else:
          pre.right = None
          q = current.key
          if q.expertiseMean < lowest:
            bestQuestion = q
            lowest = q.expertiseMean
          elif q.expertiseMean == lowest and q.identifier < bestQuestion.identifier:
            bestQuestion = q
          current = current.right

    return bestQuestion 
  
  def _calcHighestOpinionMedian(self):
    current = self.questionTree.root
    bestQuestion = None
    highest = -1

    while current:
      if current.left is None:
        q = current.key
        if q.opinionMedian > highest:
          bestQuestion = q
          highest = q.opinionMedian
        elif q.opinionMedian == highest and q.identifier < bestQuestion.identifier:
          bestQuestion = q
        current = current.right
      else:
        pre = current.left
        
        while pre.right and pre.right != current:
          pre = pre.right

        if pre.right is None:
          pre.right = current
          current = current.left
        else:
          pre.right = None
          q = current.key
          if q.opinionMedian > highest:
            bestQuestion = q
            highest = q.opinionMedian
          elif q.opinionMedian == highest and q.identifier < bestQuestion.identifier:
            bestQuestion = q
          current = current.right

    return bestQuestion 
  
  def _calcLowestOpinionMedian(self):
    current = self.questionTree.root
    bestQuestion = None
    lowest = 11
    
    while current:
      if current.left is None:
        q = current.key
        if q.opinionMedian < lowest:
          bestQuestion = q
          lowest = q.opinionMedian
        elif q.opinionMedian == lowest and q.identifier < bestQuestion.identifier:
          bestQuestion = q
        current = current.right
      else:
        pre = current.left
        
        while pre.right and pre.right != current:
          pre = pre.right

        if pre.right is None:
          pre.right = current
          current = current.left
        else:
          pre.right = None
          q = current.key
          if q.opinionMedian < lowest:
            bestQuestion = q
            lowest = q.opinionMedian
          elif q.opinionMedian == lowest and q.identifier < bestQuestion.identifier:
            bestQuestion = q
          current = current.right

    return bestQuestion 
  
  def _calcHighestOpinionMode(self):
    current = self.questionTree.root
    bestQuestion = None
    highest = -1

    while current:
      if current.left is None:
        q = current.key
        if q.opinionMode > highest:
          bestQuestion = q
          highest = q.opinionMode
        elif q.opinionMode == highest and q.identifier < bestQuestion.identifier:
          bestQuestion = q
        current = current.right
      else:
        pre = current.left
        
        while pre.right and pre.right != current:
          pre = pre.right

        if pre.right is None:
          pre.right = current
          current = current.left
        else:
          pre.right = None
          q = current.key
          if q.opinionMode > highest:
            bestQuestion = q
            highest = q.opinionMode
          elif q.opinionMode == highest and q.identifier < bestQuestion.identifier:
            bestQuestion = q
          current = current.right

    return bestQuestion 
  
  def _calcLowestOpinionMode(self):
    current = self.questionTree.root
    bestQuestion = None
    lowest = 11

    while current:
      if current.left is None:
        q = current.key
        if q.opinionMode < lowest:
          bestQuestion = q
          lowest = q.opinionMode
        elif q.opinionMode == lowest and q.identifier < bestQuestion.identifier:
          bestQuestion = q
        current = current.right
      else:
        pre = current.left
        
        while pre.right and pre.right != current:
          pre = pre.right

        if pre.right is None:
          pre.right = current
          current = current.left
        else:
          pre.right = None
          q = current.key
          if q.opinionMode < lowest:
            bestQuestion = q
            lowest = q.opinionMode
          elif q.opinionMode == lowest and q.identifier < bestQuestion.identifier:
            bestQuestion = q
          current = current.right

    return bestQuestion 

  def _calcHighestExtremism(self):
    current = self.questionTree.root
    bestQuestion = None
    highest = -1

    while current:
      if current.left is None:
        q = current.key
        if q.extremism > highest:
          bestQuestion = q
          highest = q.extremism
        elif q.extremism == highest and q.identifier < bestQuestion.identifier:
          bestQuestion = q
        current = current.right
      else:
        pre = current.left
        
        while pre.right and pre.right != current:
          pre = pre.right

        if pre.right is None:
          pre.right = current
          current = current.left
        else:
          pre.right = None
          q = current.key
          if q.extremism > highest:
            bestQuestion = q
            highest = q.extremism
          elif q.extremism == highest and q.identifier < bestQuestion.identifier:
            bestQuestion = q
          current = current.right

    return bestQuestion 

  def _calcHighestConsensus(self):
    current = self.questionTree.root
    bestQuestion = None
    highest = -1

    while current:
      if current.left is None:
        q = current.key
        if q.consensus > highest:
          bestQuestion = q
          highest = q.consensus
        elif q.consensus == highest and q.identifier < bestQuestion.identifier:
          bestQuestion = q
        current = current.right
      else:
        pre = current.left
        
        while pre.right and pre.right != current:
          pre = pre.right

        if pre.right is None:
          pre.right = current
          current = current.left
        else:
          pre.right = None
          q = current.key
          if q.consensus > highest:
            bestQuestion = q
            highest = q.consensus
          elif q.consensus == highest and q.identifier < bestQuestion.identifier:
            bestQuestion = q
          current = current.right

    return bestQuestion 
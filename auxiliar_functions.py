# Merge Sort

def mergeSort(arr, comparer):
  if len(arr) <= 1:
    return arr
    
  midIndex = len(arr) // 2
  left = mergeSort(arr[:midIndex], comparer)
  right = mergeSort(arr[midIndex:], comparer)
    
  return merge(left, right, comparer)

def merge(left, right, comparer):
  result = []
  i, j = 0, 0
    
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

# Comparers

def participantComparer(a, b):
  # Si hay empate en opinión
  if a.opinion == b.opinion:
    # Si hay empate en experticia
    if a.expertise == b.expertise:
      return a.identifier > b.identifier
    else:
      return a.expertise > b.expertise
  else:
    return a.opinion > b.opinion

def questionComparer(a, b):
  # Si hay empate en promedio de opinión
  if a.opinionMean == b.opinionMean:
    # Si hay empate en promedio de experticia
    if a.expertiseMean == b.expertiseMean:
      return a.identifier < b.identifier
    else:
      return a.expertiseMean > b.expertiseMean
  else:
    return a.opinionMean > b.opinionMean

def topicListComparer(a, b):
  # Si hay empate en promedio de promedios de opinión
  if a.opinionMeanOfMeans == b.opinionMeanOfMeans:
    # Si hay empate en promedio de promedios de experticia
    if a.expertiseMeanOfMeans == b.expertiseMeanOfMeans:
      return a.totalNumOfParticipants > b.totalNumOfParticipants
    else:
      return a.expertiseMeanOfMeans > b.expertiseMeanOfMeans
  else:
    return a.opinionMeanOfMeans > b.opinionMeanOfMeans
  
def participantListComparer(a, b):
  # Si hay empate en promedio de experticia
  if a.expertise == b.expertise:
    return a.identifier > b.identifier
  else:
    return a.expertise > b.expertise
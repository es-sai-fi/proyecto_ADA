from classes import *

if __name__ == "__main__":
  participants = []
  questions = []
  topics = []
  
  participants.append(Participant("Sofia García", 1, 6))
  participants.append(Participant("Alejandro Torres", 7, 10))
  participants.append(Participant("Valentina Rodriguez", 9, 0))
  participants.append(Participant("Juan Lopéz", 10, 1))
  participants.append(Participant("Martina Martinez", 7, 0))
  participants.append(Participant("Sebastián Pérez", 8, 9))
  participants.append(Participant("Camila Fernández", 2, 7))
  participants.append(Participant("Mateo González", 4, 7))
  participants.append(Participant("Isabella Díaz", 7, 5))
  participants.append(Participant("Daniel Ruiz", 2, 9))
  participants.append(Participant("Luciana Sánchez", 1, 7))
  participants.append(Participant("Lucas Vásquez", 6, 8))
  
  questions.append(Question([participants[9], participants[1]]))
  questions.append(Question([participants[0], participants[8], participants[11], participants[5]]))
  questions.append(Question([participants[10], participants[7], participants[6]]))
  questions.append(Question([participants[2], participants[3], participants[4]]))
  
  topics.append(Topic([questions[0], questions[1]]))
  topics.append(Topic([questions[2], questions[3]]))
  
  survey = Survey(topics, questions, participants)
  survey.execute()
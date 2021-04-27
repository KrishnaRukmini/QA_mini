from  albert import*
import distilbert import*
import bert import*
def question_answering():
  question = str(input("Enter your question: "))
  context = str(input("Enter the context for the question: "))
  model = input("Enter the model you want to use for fetching the answer \n 1: Albert 2: DistilBert 3.Bert")
  if model == 1:
    answer = albert(question,answer)
  if model == 2:
    answer = distilbert(question,answer)
  if answer == 3:
    answer = bert(question,answer)
    return answer

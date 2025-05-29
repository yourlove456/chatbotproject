import pandas as pd
import numpy as np
import Levenshtein

class SimpleChatBot:
    def __init__(self, filepath):
        self.questions, self.answers = self.load_data(filepath)

    def load_data(self, filepath):
        data = pd.read_csv(filepath)
        questions = data['Q'].tolist()  # 질문열만 뽑아 파이썬 리스트로 저장
        answers = data['A'].tolist()   # 답변열만 뽑아 파이썬 리스트로 저장
        return questions, answers

    def find_best_answer(self, input_sentence):
        distances = [Levenshtein.distance(input_sentence, q) for q in self.questions] # 유사도를 레벤슈타인 거리로 구하기
        best_index = int(np.argmin(distances)) # 가장 유사한 인덱스 구하기
        return self.answers[best_index] # 유사한 인덱스 답 채택

# CSV 파일 경로 지정
filepath = 'ChatbotData.csv'

# 간단한 챗봇 인스턴스 생성
chatbot = SimpleChatBot(filepath)

# '종료'라는 단어가 입력될 때까지 챗봇과의 대화를 반복
while True:
    input_sentence = input('You: ')
    if input_sentence.lower() == '종료':
        break
    response = chatbot.find_best_answer(input_sentence)
    print('Chatbot:', response)

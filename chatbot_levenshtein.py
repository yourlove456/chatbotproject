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

    def calculate_similarity(self, input_sentence):
        distances = [Levenshtein.distance(input_sentence, q) for q in self.questions] # 입력 문장과 각 질문 간의 레벤슈타인 거리를 계산하여 리스트로 반환
        return distances

    def find_best_match_index(self, distances):
        return int(np.argmin(distances)) # 거리 리스트에서 가장 유사한 질문의 인덱스를 반환

    def get_answer_by_index(self, index):
        return self.answers[index] # 인덱스를 받아 해당하는 답변을 반환

    def find_best_answer(self, input_sentence):
        distances = self.calculate_similarity(input_sentence) # 1. 유사도를 레벤슈타인 거리로 구하기
        best_index = self.find_best_match_index(distances) # 2. 가장 유사한 인덱스 구하기
        return self.get_answer_by_index(best_index) # 3. 유사한 인덱스 답 채택

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

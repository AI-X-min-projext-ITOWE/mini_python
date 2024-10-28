from abc import ABC, abstractmethod


class factory(ABC):


    # 모델 객체 생성
    @staticmethod
    @abstractmethod
    def create_detector(model_path: str):
        pass
from abc import ABC, abstractmethod


class DetectionModel(ABC):

    # 모델 객체 생성
    @staticmethod
    @abstractmethod
    def detection(model_path: str):
        pass
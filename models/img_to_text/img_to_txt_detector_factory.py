from models.factory import factory


class img_to_txt_detector_factory(factory):

    @staticmethod
    def create_detector(model_path: str): # -> vision.FaceDetector: 리턴 타입이 뭔지 미리 알려줌
        # base_options = python.BaseOptions(model_asset_path=model_path)
        # options = vision.FaceDetectorOptions(base_options=base_options)
        # return vision.FaceDetector.create_from_options(options)
        pass
# mini_python



##install
>>conda create -n sum_insect python=3.12
>>conda activate sum_insect<br>
>>conda install -c conda-forge tesseract pytesseract<br>
>>conda install -c conda-forge tesseract-data-eng<br>
>>pip install --no-cache-dir --upgrade -r requirements.txt<br>

## API 명세서
>> #### 이미지 요청
>> url : /images?from_lang=4&to_lang=0&is_summary=false&is_speech=false
>> body : file

>>| 요청 변수명 | 타입 | 필수 여부 | 기본값 | 설명 |
>>|-------|-------|-------|-------|-------|
>>| file | Binary | Y | - |번역할 이미지를 넣으세요.|
>>| from_lang | int | Y | - |0:한국 1:중국 2:일본 3:스페인 4:영어|
>>| to_lang | int | Y | - |0:한국 1:중국 2:일본 3:스페인 4:영어|
>>| is_summary | boolean | Y | - |요약 선택|
>>| is_speech | boolean | Y | - |음성 선택|

>> #### 텍스트 요청
>> url : /text?from_lang=4&to_lang=0&is_summary=false&is_speech=false
>> body : text

>>| 요청 변수명 | 타입 | 필수 여부 | 기본값 | 설명 |
>>|-------|-------|-------|-------|-------|
>>| text | String | Y | - |번역할 텍스트를 넣으세요.|
>>| from_lang | int | Y | - |0:한국 1:중국 2:일본 3:스페인 4:영어|
>>| to_lang | int | Y | - |0:한국 1:중국 2:일본 3:스페인 4:영어|
>>| is_summary | boolean | Y | - |요약 선택|
>>| is_speech | boolean | Y | - |음성 선택|

# Han2Jamo

한글 to 자모로 바꿔주는 가장 빠르고 편리한 라이브러리

## Installation

```
pip install han2jamo
```

## Usage

```python
hand2jamo = Han2Jamo()

# 한글문장 -> 자모 : str
han2jamo.str_to_jamo("안녕 내 이름은 뽀로로야")
>> "ㅇㅏㄴㄴㅕㅇ ㄴㅐ ㅇㅣㄹㅡㅁㅇㅡㄴ ㅃㅗㄹㅗㄹㅗㅇㅑ"

# 자모 -> 한글문장 복원
hand2jamo.jamo_to_str("ㅇㅏㄴㄴㅕㅇ ㄴㅐ ㅇㅣㄹㅡㅁㅇㅡㄴ ㅃㅗㄹㅗㄹㅗㅇㅑ")
>> "안녕 내 이름은 뽀로로야"

# 한글 한글자 -> 자모
hand2jamo.char_to_jamo("꾹")
>> ("ㄲ", "ㅜ", "ㄱ")

## 자모 -> 한글 한글자 복원
hand2jamo.jamo_to_char("ㄲㅜㄱ")
>> "꾹"

```
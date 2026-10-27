
# Python 프롬프트 관리자 프로그램 발표 자료

## 1. 프로젝트 주제

### Python으로 자주 사용하는 프롬프트를 저장하고 관리하는 프로그램 만들기

최근 AI 도구를 사용할 때 비슷한 프롬프트를 반복해서 입력하는 경우가 많습니다.

예를 들어:

- 블로그 글 작성 프롬프트
- 코드 리뷰 프롬프트
- 번역 프롬프트
- 공부 요약 프롬프트
- 발표 자료 생성 프롬프트

이런 프롬프트들을 매번 다시 작성하는 것은 비효율적입니다.

그래서 이번 프로젝트에서는 Python을 사용해  
**프롬프트를 저장, 불러오기, 수정, 삭제할 수 있는 간단한 관리 프로그램**을 만들었습니다.

---

## 2. 프로젝트 목표

이 프로그램의 목표는 다음과 같습니다.

1. 자주 사용하는 프롬프트를 이름과 함께 저장한다.
2. 저장된 프롬프트 목록을 확인한다.
3. 원하는 프롬프트를 이름으로 불러온다.
4. 기존 프롬프트를 수정한다.
5. 필요 없는 프롬프트를 삭제한다.
6. 프로그램을 종료해도 데이터가 유지되도록 JSON 파일에 저장한다.

---

## 3. 사용한 기술

### Python

프로그램의 전체 로직을 작성하는 데 사용했습니다.

### JSON

프롬프트 데이터를 파일로 저장하기 위해 사용했습니다.

JSON은 데이터를 다음과 같은 형태로 저장할 수 있습니다.

```json
{
    "코드 리뷰": "너는 시니어 개발자야. 아래 코드를 리뷰해줘.",
    "블로그 작성": "너는 전문 블로그 작가야. 주제에 맞게 글을 작성해줘."
}
```

Python의 딕셔너리와 구조가 비슷해서 사용하기 쉽습니다.

---

## 4. 프로그램의 핵심 구조

프로그램은 크게 두 부분으로 나뉩니다.

```text
1. PromptManager 클래스
   - 프롬프트 저장, 불러오기, 수정, 삭제 기능 담당

2. main 함수
   - 사용자에게 메뉴를 보여주고 입력을 받는 부분
```

---

## 5. PromptManager 클래스

`PromptManager` 클래스는 프롬프트 데이터를 관리하는 역할을 합니다.

```python
class PromptManager:
    def __init__(self, file_path="prompts.json"):
        self.file_path = file_path
        self.prompts = self.load_prompts()
```
<img width="535" height="428" alt="image" src="https://github.com/user-attachments/assets/5d1b8b77-62a0-4fc0-8ac8-a134165a384d" />

### 설명

- `file_path`는 프롬프트를 저장할 JSON 파일 이름입니다.
- 기본 파일 이름은 `prompts.json`입니다.
- 프로그램이 시작되면 기존에 저장된 프롬프트를 불러옵니다.

---

## 6. JSON 파일에서 데이터 불러오기

```python
def load_prompts(self):
    if not os.path.exists(self.file_path):
        return {}

    with open(self.file_path, "r", encoding="utf-8") as file:
        return json.load(file)
```

### 설명

이 함수는 JSON 파일에서 저장된 프롬프트를 불러옵니다.

만약 `prompts.json` 파일이 없다면 빈 딕셔너리 `{}`를 반환합니다.

즉, 처음 실행할 때 파일이 없어도 오류가 나지 않도록 처리했습니다.

---

## 7. JSON 파일에 데이터 저장하기

```python
def save_prompts(self):
    with open(self.file_path, "w", encoding="utf-8") as file:
        json.dump(self.prompts, file, ensure_ascii=False, indent=4)
```

### 설명

현재 저장된 프롬프트 목록을 JSON 파일에 저장하는 함수입니다.

여기서 중요한 부분은 다음과 같습니다.

```python
ensure_ascii=False
```

이 옵션을 사용하면 한글이 깨지지 않고 저장됩니다.

```python
indent=4
```

이 옵션은 JSON 파일을 보기 좋게 정리해서 저장합니다.

---

## 8. 프롬프트 추가 기능

```python
def add_prompt(self, name, content):
    if name in self.prompts:
        print(f"'{name}' 프롬프트가 이미 존재합니다.")
        return

    self.prompts[name] = content
    self.save_prompts()
    print(f"'{name}' 프롬프트가 저장되었습니다.")
```

### 설명

사용자가 입력한 이름과 내용을 딕셔너리에 저장합니다.

예를 들어:

```python
name = "코드 리뷰"
content = "너는 시니어 개발자야. 아래 코드를 리뷰해줘."
```

이렇게 입력하면 내부적으로는 다음처럼 저장됩니다.

```python
{
    "코드 리뷰": "너는 시니어 개발자야. 아래 코드를 리뷰해줘."
}
```

이미 같은 이름이 있으면 중복 저장을 막습니다.

---

## 9. 프롬프트 목록 보기

```python
def list_prompts(self):
    if not self.prompts:
        print("저장된 프롬프트가 없습니다.")
        return

    print("\n저장된 프롬프트 목록:")
    for name in self.prompts:
        print(f"- {name}")
```

### 설명

현재 저장된 프롬프트의 이름만 출력합니다.

예시 출력:

```text
저장된 프롬프트 목록:
- 코드 리뷰
- 블로그 작성
- 영어 번역
```

---

## 10. 프롬프트 불러오기

```python
def get_prompt(self, name):
    return self.prompts.get(name)
```

### 설명

사용자가 입력한 이름에 해당하는 프롬프트 내용을 불러옵니다.

예를 들어 `"코드 리뷰"`를 입력하면 해당 프롬프트 내용이 출력됩니다.

---

## 11. 프롬프트 수정 기능

```python
def update_prompt(self, name, new_content):
    if name not in self.prompts:
        print(f"'{name}' 프롬프트를 찾을 수 없습니다.")
        return

    self.prompts[name] = new_content
    self.save_prompts()
    print(f"'{name}' 프롬프트가 수정되었습니다.")
```

### 설명

기존에 저장된 프롬프트의 내용을 새 내용으로 바꿉니다.

수정한 뒤에는 반드시 `save_prompts()`를 호출해서 JSON 파일에 반영합니다.

---

## 12. 프롬프트 삭제 기능

```python
def delete_prompt(self, name):
    if name not in self.prompts:
        print(f"'{name}' 프롬프트를 찾을 수 없습니다.")
        return

    del self.prompts[name]
    self.save_prompts()
    print(f"'{name}' 프롬프트가 삭제되었습니다.")
```

### 설명

사용자가 입력한 이름의 프롬프트를 삭제합니다.

삭제 후에도 JSON 파일에 다시 저장해서 데이터가 유지됩니다.

---

## 13. 사용자 메뉴 만들기

처음에는 클래스만 작성했기 때문에 프로그램을 실행해도 아무 화면이 나오지 않았습니다.

그 이유는 실제로 실행되는 코드가 없었기 때문입니다.

그래서 `main()` 함수를 만들어 사용자 메뉴를 추가했습니다.

```python
def main():
    manager = PromptManager()

    while True:
        print("\n===== 프롬프트 관리자 =====")
        print("1. 프롬프트 추가")
        print("2. 프롬프트 목록 보기")
        print("3. 프롬프트 불러오기")
        print("4. 프롬프트 수정")
        print("5. 프롬프트 삭제")
        print("0. 종료")

        choice = input("메뉴를 선택하세요: ")
```

### 설명

`while True`를 사용해서 사용자가 종료를 선택하기 전까지 메뉴가 계속 반복됩니다.

---

## 14. 메뉴 선택 처리

```python
if choice == "1":
    name = input("프롬프트 이름: ")
    content = input("프롬프트 내용: ")
    manager.add_prompt(name, content)
```

사용자가 `1`을 입력하면 프롬프트를 추가합니다.

```python
elif choice == "2":
    manager.list_prompts()
```

사용자가 `2`를 입력하면 저장된 프롬프트 목록을 보여줍니다.

```python
elif choice == "0":
    print("프로그램을 종료합니다.")
    break
```

사용자가 `0`을 입력하면 반복문을 종료하고 프로그램을 끝냅니다.

---

## 15. 프로그램 실행 시작 코드

```python
if __name__ == "__main__":
    main()
```

이 코드는 매우 중요합니다.

의미는 다음과 같습니다.

> 이 Python 파일을 직접 실행했을 때 `main()` 함수를 실행하라.

처음에 프로그램을 실행했을 때 아무것도 뜨지 않았던 이유는  
이런 실행 코드가 없었기 때문입니다.

클래스만 정의하면 Python은 클래스를 읽고 바로 종료합니다.

---

## 16. 실행 결과 예시

프로그램을 실행하면 다음과 같은 화면이 나옵니다.

```text
===== 프롬프트 관리자 =====
1. 프롬프트 추가
2. 프롬프트 목록 보기
3. 프롬프트 불러오기
4. 프롬프트 수정
5. 프롬프트 삭제
0. 종료
메뉴를 선택하세요:
```

예를 들어 `1`을 입력하면:

```text
프롬프트 이름: 코드 리뷰
프롬프트 내용: 너는 시니어 개발자야. 아래 코드를 리뷰해줘.
'코드 리뷰' 프롬프트가 저장되었습니다.
```

그다음 `2`를 입력하면:

```text
저장된 프롬프트 목록:
- 코드 리뷰
```

---

## 17. 처음 발생한 문제와 해결 방법

### 발생한 문제

프로그램을 실행했을 때 터미널에 다음과 같은 내용만 나오고 아무 일도 일어나지 않았습니다.

```text
PS C:\Users\user\AppData\Local\Programs\Microsoft VS Code>
```

### 원인

Python 코드에 클래스만 있고 실제 실행 코드가 없었기 때문입니다.

즉, 프로그램은 오류 없이 실행되었지만  
사용자에게 보여줄 메뉴나 입력 코드가 없어서 바로 종료된 것입니다.

### 해결 방법

`main()` 함수를 만들고, 아래 코드를 추가했습니다.

```python
if __name__ == "__main__":
    main()
```

그 결과 메뉴가 출력되고 사용자가 직접 프로그램을 조작할 수 있게 되었습니다.

---

## 18. 전체 프로그램 기능 요약

| 기능 | 설명 |
|---|---|
| 프롬프트 추가 | 이름과 내용을 입력해 저장 |
| 목록 보기 | 저장된 프롬프트 이름 확인 |
| 프롬프트 불러오기 | 이름으로 저장된 내용 출력 |
| 프롬프트 수정 | 기존 프롬프트 내용 변경 |
| 프롬프트 삭제 | 필요 없는 프롬프트 제거 |
| JSON 저장 | 프로그램 종료 후에도 데이터 유지 |

<img width="330" height="217" alt="image" src="https://github.com/user-attachments/assets/afecdb85-f04f-4bcb-8245-aa2503ad90c3" />

---

## 19. 이 프로젝트를 통해 배운 점

이번 프로젝트를 통해 다음 내용을 배울 수 있었습니다.

1. Python 클래스를 사용해 기능을 구조화하는 방법
2. JSON 파일을 이용해 데이터를 저장하는 방법
3. `input()`을 사용해 사용자 입력을 받는 방법
4. `while` 반복문으로 메뉴 프로그램을 만드는 방법
5. 파일이 없을 때 오류가 나지 않도록 처리하는 방법
6. 프로그램 실행 시작점인 `if __name__ == "__main__"`의 역할

---

## 20. 개선할 수 있는 점

현재 프로그램은 기본적인 프롬프트 관리 기능을 제공합니다.

앞으로 다음과 같은 기능을 추가할 수 있습니다.

### 1. 검색 기능

프롬프트 이름이나 내용에 특정 단어가 포함된 항목을 찾을 수 있습니다.

예:

```text
검색어 입력: 코드
검색 결과:
- 코드 리뷰
- 코드 설명
```

### 2. 태그 기능

프롬프트마다 태그를 붙일 수 있습니다.

예:

```text
코드 리뷰 - coding
블로그 작성 - writing
공부 요약 - study
```

### 3. 생성 날짜, 수정 날짜 저장

프롬프트가 언제 만들어졌고 언제 수정되었는지 기록할 수 있습니다.

### 4. SQLite 데이터베이스 사용

프롬프트가 많아지면 JSON 대신 데이터베이스를 사용할 수 있습니다.

### 5. GUI 또는 웹 페이지로 확장

터미널이 아니라 버튼과 입력창이 있는 프로그램으로 발전시킬 수 있습니다.

---

## 21. 발표 마무리 멘트

이번 프로젝트에서는 Python을 사용해 자주 사용하는 AI 프롬프트를 저장하고 관리하는 프로그램을 만들었습니다.

처음에는 클래스만 작성해서 실행해도 아무 화면이 나오지 않는 문제가 있었지만,  
`main()` 함수와 실행 코드를 추가해서 사용자가 직접 조작할 수 있는 메뉴 프로그램으로 완성했습니다.

이 프로그램은 JSON 파일을 사용하기 때문에 프로그램을 종료해도 데이터가 유지됩니다.

앞으로 검색 기능, 태그 기능, 날짜 기록 기능 등을 추가하면 더 실용적인 프롬프트 관리 도구로 발전시킬 수 있습니다.


## 추가된 내용

<img width="535" height="173" alt="image" src="https://github.com/user-attachments/assets/40783926-23ee-469b-ace7-f67f8f507b4b" />

위의 사진을 통해서 github에 readme 파일 뿐만 아니라 json 파일과 함께 올려서 평가자도 프로그램을 같이 확인할 수 있도록 만들었다.

import json
import os


class PromptManager:
    def __init__(self, file_path="prompts.json"):
        self.file_path = file_path
        self.prompts = self.load_prompts()

    def load_prompts(self):
        """JSON 파일에서 프롬프트를 불러옵니다."""
        if not os.path.exists(self.file_path):
            return {}

        with open(self.file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def save_prompts(self):
        """프롬프트를 JSON 파일에 저장합니다."""
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(self.prompts, file, ensure_ascii=False, indent=4)

    def add_prompt(self, name, content):
        if name in self.prompts:
            print(f"'{name}' 프롬프트가 이미 존재합니다.")
            return

        self.prompts[name] = content
        self.save_prompts()
        print(f"'{name}' 프롬프트가 저장되었습니다.")

    def get_prompt(self, name):
        return self.prompts.get(name)

    def list_prompts(self):
        if not self.prompts:
            print("저장된 프롬프트가 없습니다.")
            return

        print("\n저장된 프롬프트 목록:")
        for name in self.prompts:
            print(f"- {name}")

    def update_prompt(self, name, new_content):
        if name not in self.prompts:
            print(f"'{name}' 프롬프트를 찾을 수 없습니다.")
            return

        self.prompts[name] = new_content
        self.save_prompts()
        print(f"'{name}' 프롬프트가 수정되었습니다.")

    def delete_prompt(self, name):
        if name not in self.prompts:
            print(f"'{name}' 프롬프트를 찾을 수 없습니다.")
            return

        del self.prompts[name]
        self.save_prompts()
        print(f"'{name}' 프롬프트가 삭제되었습니다.")


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

        if choice == "1":
            name = input("프롬프트 이름: ")
            content = input("프롬프트 내용: ")
            manager.add_prompt(name, content)

        elif choice == "2":
            manager.list_prompts()

        elif choice == "3":
            name = input("불러올 프롬프트 이름: ")
            prompt = manager.get_prompt(name)

            if prompt is None:
                print("해당 프롬프트를 찾을 수 없습니다.")
            else:
                print("\n--- 프롬프트 내용 ---")
                print(prompt)

        elif choice == "4":
            name = input("수정할 프롬프트 이름: ")
            new_content = input("새 프롬프트 내용: ")
            manager.update_prompt(name, new_content)

        elif choice == "5":
            name = input("삭제할 프롬프트 이름: ")
            manager.delete_prompt(name)

        elif choice == "0":
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 선택입니다. 다시 입력해주세요.")


if __name__ == "__main__":
    main()
import os
import re



subdirectories = [name for name in os.listdir(".") if os.path.isdir(os.path.join(".", name))]

for i in os.listdir("."):
    if i in subdirectories and i != ".git":
        for textfile in os.listdir("./"+i):
            file_path = "./"+i+"/"+textfile
            with open(file_path, "r", encoding="utf-8") as input_file:
                content = input_file.read()
            content_with_br = content.replace("\n", "<br>")
            with open(file_path, "w", encoding="utf-8") as output_file:
                output_file.write(content_with_br)
    # if filename.endswith(".txt"):
    #     # 원래 파일의 전체 경로를 생성합니다.
    #     original_path = os.path.join(directory, filename)
        
    #     # 파일 이름에서 숫자만 추출합니다.
    #     numbers = re.findall(r'\d+', filename)
    #     if numbers:
    #         # 가장 첫 번째로 발견되는 숫자를 새 파일명으로 사용합니다.
    #         new_name = f"{numbers[0]}.txt"
        
    #         # 새 파일의 전체 경로를 생성합니다.
    #         new_path = os.path.join(directory, new_name)
            
    #         # 파일 이름을 변경합니다.
    #         os.rename(original_path, new_path)

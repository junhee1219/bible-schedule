import os

# 특정 폴더 지정 (예: 'my_folder')
folder_path = 'joshua'

# 폴더 내의 모든 파일을 순회
for filename in os.listdir(folder_path):
    # .txt 파일만 대상으로 함
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)
        
        # 파일 읽기
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # 줄바꿈을 <br>로 대체
        content = content.replace('\n', '<br>')
        
        # 파일 다시 쓰기
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

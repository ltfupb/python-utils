import os
import shutil
from tkinter import filedialog

path = filedialog.askdirectory() # 경로 입력
if not path:
    exit() # 취소

os.chdir(path) # 디렉토리 변경
files = os.listdir()

print(f'항목 {len(files)}개 발견')
confirm = input('정리하시겠습니까? (y/n)') # 승인 여부
if confirm.lower() != 'y':
    exit()



log = open('log.txt', 'w') # 로그

for i in files:
    if os.path.isdir(i):
        log.write(f'"{i}" is folder\n')
        continue # 폴더인 경우, 건너뜀

    extension = os.path.splitext(i)[1][1:]

    if extension == '':
        log.write(f'"{i}" has no extension\n')
        continue # 확장자가 없을 경우, 건너뜀

    os.makedirs(name=extension, exist_ok=True) # 폴더 생성
    dst = os.path.join(extension, i) # 이동 경로
    shutil.move(i, dst) # 파일 이동
    log.write(f'"{i}" has moved to {extension}\n')

log.close()

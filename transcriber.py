import whisper
import os
import sys

accepted_extensions = ['mp3', 'mp4', 'mpeg', 'mpga', 'm4a', 'wav', 'webm']

#=============================================================================================
all_audios = os.listdir('audios')
for file in all_audios:
    os.rename(os.path.join('audios', file), os.path.join('audios', file.replace(' ', '_')))
all_audios = os.listdir('audios')
#=============================================================================================

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.symtem('clear')

def header():
    print("=" * 50)
    print('|', 'CONVERSOR DE AUDIO -> TEXTO'.center(46), '|')
    print("=" * 50)
    print('Escolha o arquivo que será transcrito')
    print("=" * 50)
    for i, audio in enumerate(all_audios):
        print(f'[{i}] - {audio}')
    print('=' * 50)

def returnOption():
    try:
        clear()
        header()
        option = int(input('Sua opção>>> '))
    except:
        option = returnOption()
        return int(option)
    else:
        return int(option)

def transcribe(file_path):
    model = whisper.load_model('small')
    result = model.transcribe(file_path)
    return result['text']

#=====================================
option = returnOption()
while option > len(all_audios) - 1:
    option = returnOption()
#======================================

fileName = all_audios[option]
ext = fileName.split('.')[1]
if ext not in accepted_extensions:
    print('Formato não suportado!')
    sys.exit()

file_path = os.path.join('audios', fileName)

print('=' * 50)
print('Transcrição iniciada, aguarde a finalização...')
print('=' * 50)
text = transcribe(file_path)
outputFileName = all_audios[option].split('.')
outputFileName = str(outputFileName[0]) + '.txt'
with open(os.path.join('output', outputFileName),'wt+', encoding='utf-8') as outputFile:
    outputFile.write(text)
print('=' * 50)
print(f'Transcrição concluída, resultado em output/{outputFileName}')
print('=' * 50)
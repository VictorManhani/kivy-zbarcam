# kivy-zbarcam
Kivy Zbarcam e XCamera ajustados para compilar no
android com o Python 3.8.

# usei esse manual de referência:
https://github.com/kivy-garden/garden.zbarcam

0º Editei os arquivos xcamera e o zbarcam e 
deixei eles disponíveis na pasta do projeto.

1º instalei as dependencias necessarias pelo terminal:
```
pip3 install python-opencv
pip3 install pyzbar
```

2º Verifique se abre o programa no seu pc com o comando no terminal 
dentro da pasta do projeto:
```
python3 main.py

# ou

py main.py
```

3º Pegue a pasta do zbarcam no kivy.gardem.zbarcam e deixe junto com o main.py,
conforme a estrutura desse código.

4º Configurei o buildozer.spec (note que é pra deixar comentado o garden):
```
requirements = kivy==1.11.1, Pillow==7.0.0, libiconv, libzbar, pyzbar==0.1.8
# garden_requirements = xcamera
android.permissions = CAMERA
android.api = 29
android.ndk = 19c
```

5º Quando rodar o comando, poderá ocorrer erros:
```
sudo buildozer -v android debug run
```

6º Caso ocorrer erros instale essas dependencias no seu linux de build:
```
sudo apt-get install python3-venv
sudo apt-get install -y gettext
```

7º Apague o .buildozer gerado na pasta do seu projeto:

8º Rode novamente o comando, provavelmente irá funcionar, porém não irá abrir o app:
```
buildozer -v android debug run

adb logcat -s "python"
```
abra o app no celular e verifique a última saída do comando acima no terminal,
poderá funcionar ou dar um erro de falta de um arquivo chamado icons.ttf.

9º Por fim, poderá dar erro novamente, então abra esta pasta de projeto e nesse caminho
```
.buildozer\android\platform\build-armeabi-v7a\build\python-installs\myapp\kivy\data
```
coloque o arquivo ```icons.ttf``` que está na pasta files do projeto.

10º Rode novamente os comandos:
```
# Build, Deploy and Run a App
buildozer android debug deploy run

# Open the inspect
adb logcat -s "python"
```

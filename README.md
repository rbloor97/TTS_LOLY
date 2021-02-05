# TTS_LOLY

Guia de usuario para ambiente WSL 18.04 o Linux 18.04:

### Index
* [Configurar el ambiente operativo](#configurar-el-ambiente-operativo)
* [Descargar los modelos preentrenados](#descargar-los-modelos-preentrenados)
* [Instalar requerimientos](#instalar-requerimientos)
* [Sintetizar](#sintetizar)
* [Repositorios externos](#repositorios-externos)
* [Errores comunes](#errores-comunes)

## CONFIGURAR EL AMBIENTE OPERATIVO

Descargar e instalar anconda para Linux 18.04:

https://www.how2shout.com/how-to/install-anaconda-wsl-windows-10-ubuntu-linux-app.html

Crear un ambiente

```
	$ conda create -n tfe2 python=3.6
	$ conda activate tfe2
```

## DESCARGAR LOS MODELOS PREENTRENADOS

Español
Tacotron 2 (55 k):
https://drive.google.com/file/d/1JSC0jbdnOi4igCYTnDBdMGXIsp2VeKj9/view

Colocar el modelo en una nueva carpeta `TTS_LOLY/logs-Tacotron/taco_pretrained`

LPCNet:
https://drive.google.com/file/d/1dDKyTB_7QUoQvtf5EyGHwhUioOLBrjxF/view?usp=sharing

Colocar el modelo en la carpeta `TTS_LOLY/LPCNET`

## INSTALAR REQUERIMIENTOS

Intalar:
```
  $ sudo apt-get install -y libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg libav-tools

  $ sudo apt-get install portaudio19-dev python-pyaudio python3-pyaudio
```
Instalar gcc
```
	$ sudo apt-get install gcc
	$ sudo apt-get install g++
```
Numpy 
```
	$ pip install numpy==1.17.0
  ```
Instalar Tensorflow = 1.15
```
	$ pip install tensorflow==1.15 
```
Instalar requerimientos.txt
```	
  $ pip install -r requirements.txt
```

## SINTETIZAR

En el archivo sentences.txt se escriben las oraciones que se desean sintetizar.

Ejecutar script
```	
  $ bash script.sh
```
## Repositorios externos

Esta implementación esta basada en los siguientes repositorios:
* [carlfm01/Tacotron-2](https://github.com/carlfm01/Tacotron-2)
* [Rayhane-mamah/Tacotron-2](https://github.com/Rayhane-mamah/Tacotron-2)

## Errores comunes

TypeError: create_target_machine() got an unexpected keyword argument 'jitdebug'
```	
  $ pip install -U llvmlite==0.32.1
```
ModuleNotFoundError: No module named 'numpy.testing.decorators'
```
	$ pip uninstall numpy 
  $ pip install numpy==1.17.0
  ```

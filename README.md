# LOGFISHH - Logs Forensic Investigator SSH

			       |||      |||
			       | |  __  | |
		|-|_____-----/   |_|  |_|   \-----_____|-|
		|_|_________{   }|  (^) |{  }__________|_|
		 ||          |_| |   ^  | |_|          ||
		 |              \|  /\  |/              |
		 |               \ |--| /               |
		 =               \ |__| /               =
		 +               \      /               +
				  \    /
				  \    /
				   \  /
				   \  /
				   \  /
				   \  /       LOGFISHH 1.0 - Logs Forensic Investigator SSH
				   \  /                            Developer :@svelizdonoso       
				   \  /             GitHub: https://github.com/SVelizDonoso
				    \/                              Mail:cyslabs@gmail.com        
                                                           
                                                     
    Use: python logfissh.py --file /var/log/auth.log
         python logfissh.py --file /var/log/auth.log --animation 
         python logfissh.py --file /var/log/auth.log --webm 
    Options: 
         python logfissh.py -h


   
 # Descripción
Este script tiene por objetivo ayudar a realizar análisis forense de logs en servicios ssh, el fin es poder ayudar al investigador a tener un medio, por el cual pueda realizar consultas a los Logs y determinar posibles ataques.
Los logs que son posibles parsear con este script son:

 ```sh
----  /var/log/secure
----  /var/log/auth.log
```

 # Instalación
 
 Para hacer funcionar este script se debe instalar los siguientes paquetes:
 ```sh
 sudo apt-get install gource
 sudo apt-get install ffmpeg
 ```
Luego descargamos el script en nuestro Kali Linux 2018
```sh
git clone https://github.com/SVelizDonoso/logfishh.git
cd logfishh
python logfishh.py 
```
# Opciones
 ```sh
 root@kali:~/Desktop/logfissh# python logfissh.py -h

			       |||      |||
			       | |  __  | |
		|-|_____-----/   |_|  |_|   \-----_____|-|
		|_|_________{   }|  (^) |{  }__________|_|
		 ||          |_| |   ^  | |_|          ||
		 |              \|  /\  |/              |
		 |               \ |--| /               |
		 =               \ |__| /               =
		 +               \      /               +
				  \    /
				  \    /
				   \  /
				   \  /
				   \  /
				   \  /       LOGFISHH 1.0 - Logs Forensic Investigator SSH
				   \  /                            Developer :@svelizdonoso       
				   \  /             GitHub: https://github.com/SVelizDonoso
				    \/                              Mail:cyslabs@gmail.com        
                                                           
                                                     
    Use: python logfissh.py --file /var/log/auth.log
     	 python logfissh.py --file /var/log/auth.log --animation 
	 python logfissh.py --file /var/log/auth.log --webm 
    Options: 
	 python logfissh.py -h


    
usage: logfissh.py [-h] [-f FILE] [-a] [-v] [--version]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  File Logs
  -a, --animation       Animation logs access
  -v, --webm            output animation to .webm
  --version             show program's version number and exit

 ```
 
 # Uso de la Herramienta
 
Para el uso básico de la herramienta para obtener un reporte HTML necesitamos agregar el parámetro --file
 ```sh
 python logfissh.py --file /var/log/auth.log
 ```
Para el uso básico de la herramienta para obtener un reporte HTML  y una animación de las solicitudes Accept y Fail, necesitamos agregar el parámetro --animate
 ```sh
 python logfissh.py --file /var/log/auth.log --animation
 ```
 Para el uso básico de la herramienta para obtener un reporte HTML y grabar un video de las solicitudes Accept y Fail, necesitamos agregar el parámetro --webm
 ```sh
 python logfissh.py --file /var/log/auth.log --webm
 ```
# Reporte HTML
<img src="https://image.ibb.co/ek2gaq/KALI-2018-2018-10-26-22-41-50.png" >

# Imagen Video Animación
<img src="https://image.ibb.co/nbCdoA/KALI-2018-2018-10-26-22-45-56.png" >
<img src="https://image.ibb.co/eQs01V/KALI-2018-2018-10-26-22-46-59.png" >
<img src="https://image.ibb.co/jpkL1V/KALI-2018-2018-10-26-22-47-09.png" >
 
# Advertencia
Este software se creo SOLAMENTE para fines educativos. No soy responsable de su uso. Úselo con extrema precaución.

# Autor
@svelizdonoso https://github.com/SVelizDonoso/



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
python logfishh.py -h
```
 
 

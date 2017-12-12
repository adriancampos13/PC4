# Universidad Interamericana de Panama
# Programacion IV
# Proyecto Final - ***** Ahorrador de Espacio en Python *****

# Integrantes:
#   Adrian Campos


"""
Descripción:
Este programa sube una carpeta especifica, al almacenamiento de Google Drive.
    Comprime la carpeta en un archivo usando llamadas al sistema, luego carga el archivo.
"""

from __future__ import print_function
import httplib2
import os
import time
from apiclient import discovery
from apiclient.http import MediaFileUpload
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from oauth2client.service_account import ServiceAccountCredentials


try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None


# nombre de la carpeta en la unidad, si no está presente: creará una nueva
GDRIVE_FOLDER_NAME = "PG4_Proyecto"

# El directorio de la carpeta en la que desea hacer una copia de seguridad
# Ejemplo: se está comprimiendo la carpeta 'PG4_Proyecto'
# El archivo #Zip se coloca en el mismo directorio que este script
# Zipped file se eliminará después de ser cargado
FOLDER_TO_ZIP_DIRECTORY= "/home/acampos/PycharmProjects/test/"

# Dirección de correo electrónico del destinatario de la carpeta que se va a compartir
# actualmente solo comparte con una dirección de correo electrónico por llamada
# Asegúrese de deletrearlo correctamente
NOTIFICATION_EMIAL_ADDRESS = "adriancampos13@gmail.com"

# Esto le dice a Google qué el servicio API está tratando de usar (estamos usando la unidad)
# Si está realizando una copia de seguridad en Google Drive, no cambie esto.
SCOPES = 'https://www.googleapis.com/auth/drive'

# Esto apunta al archivo de clave JSON para la cuenta de servicio
# que se debio haber descargado el archivo al crear tu cuenta de servicio
# Debería estar en el mismo directorio que este script
KEY_FILE_NAME = 'ProyectoFinalPG4-20b2ec4f353a.json'
########################################################################################
########################################################################################

def callback(request_id, response, exception):
    if exception:
        # Handle error
        print(exception)
    else:
        print("Permission Id: %s" % response.get('id'))


def get_service():
    """Obtiene el servicio que se comunica con una API de Google.
    Returns:
      Un servicio que está conectado a la API especificada.
    """
    print("Acquiring credentials...")
    credentials = ServiceAccountCredentials.from_json_keyfile_name(filename=KEY_FILE_NAME, scopes=SCOPES)

    # Tiene que verificar las credenciales con los servidores de Google
    print("Authorizing...")
    http = credentials.authorize(httplib2.Http())

    # Construye el objeto de servicio para usar con cualquier API
    print("Acquiring service...")
    service = discovery.build(serviceName="drive", version="v3", credentials=credentials)

    print("Service acquired!\n")
    return service

def getIDfromName(service, name):
    """Obtiene el primer elemento con el nombre especificado en Google Drive
    y devuelve su ID único
	Retorna:
		itemID, the unique ID for said Google Drive item name provided
		None (null value), if file not found
    """
    print("Looking for item with name of: "+name)
    results = service.files().list(q="name='"+name+"'", pageSize=1, fields="files(id, name)").execute()
    items = results.get('files', [])
    if not items:
        print("Item not found...\n")
        return None
    itemID = items[0]['id']
    print("Acquired item id: "+itemID+" for item called: "+items[0]['name']+"\n")
    return itemID

def createNewFolder(service,  name):
    """Creará una nueva carpeta en la raíz del Google Drive suministrado
    Retorna:
        El nuevo ID de carpeta o el ID de la carpeta ya existente
    """
    folderID = getIDfromName(service=service, name=name)
    if folderID is not None:
        return folderID

    folder_metadata = {
        'name' : name,
        'mimeType' : 'application/vnd.google-apps.folder'
    }

    folder = service.files().create(body=folder_metadata, fields='id, name').execute()
    folderID = folder.get('id')
    print('Folder Creation Complete')
    print('Folder Name: %s' % folder.get('name'))
    print('Folder ID: %s \n' % folder.get('id'))
    return folderID

def getTimestampLabel():
	"""Crea y devuelve una cadena de marca de tiempo legible;
    utilizado para nombrar los archivos y carpetas
	"""
	return "BACKUP_"+time.strftime("%x").replace("/","-")+"_"+time.strftime("%X")+"_"+str(int(round(time.time())))

def createNewTimestampedFolder(service):
    """Crea una carpeta con el nombre en la hora ejecutada.
    """
    name = getTimestampLabel()
    createNewFolder(service=service, name=name)

def uploadFileToFolder(service, folderID, fileName):
	"""Carga el archivo a la id de la carpeta especificada en el Google Drive
    Retorna:
    fileID, una cadena de identificación del archivo cargado
	"""
	print("Uploading file to: "+folderID)
	file_metadata = {
  		'name' : fileName,
  		'parents': [ folderID ]
	}
	media = MediaFileUpload(fileName, resumable=True)
	file = service.files().create(body=file_metadata, media_body=media, fields='name,id').execute()
	fileID = file.get('id')
	print('File ID: %s ' % fileID)
	print('File Name: %s \n' % file.get('name'))

	return fileID

def createZIPfileBackup(directory):
	"""Crea un archivo ZIP en el directorio de trabajo actual
    Utiliza llamadas a funciones del sistema porque son más fáciles
    Retorna:
    zipFileName, el nombre del archivo zip que se creó
	"""
	print("Creating ZIP folder to upload...")
	fileName = getTimestampLabel()
	zipFileName = fileName+".zip"
	os.system("zip -r "+zipFileName+" "+directory)
	print("ZIP folder created: "+zipFileName+"\n")
	return zipFileName

def removeZIP(zipFileName):
	"""Se deshace de la carpeta zip que creamos
    Utiliza llamadas a funciones del sistema porque son más fáciles.
	"""
	print("Removing ZIP folder from system...")
	os.system("rm "+zipFileName)
	print("ZIP file "+zipFileName+" removed from local system! :D\n")

def shareFileWithEmail(service, fileID, emailAddress):
    """Comparte el archivo especificado por correo electrónico
    Otorga privilegios de 'escritura' por defecto, lo que permite a
    uno para eliminar el contenido de la carpeta, pero no la misma carpeta.
    """
    print("Sharing file with email: "+emailAddress)
    batch = service.new_batch_http_request(callback=callback)
    user_permission = {
        'type': 'user',
        'role': 'writer',
        'emailAddress': emailAddress
    }
    batch.add(service.permissions().create(
        fileId=fileID,
        body=user_permission,
        fields='id',
    ))
    batch.execute()
    print("Sharing complete!\n")

def main():
    print("Starting filesystem backup...\n")
    service = get_service()

    #obtiene la ID de la carpeta donde almacenaremos las copias de seguridad
    folderID = createNewFolder(service=service,name=GDRIVE_FOLDER_NAME)
    
    #crea el archivo ZIP de dicho directorio
    zipFileName = createZIPfileBackup(FOLDER_TO_ZIP_DIRECTORY)

    #carga el archivo en la carpeta de Google Drive
    uploadFileToFolder(service=service, folderID=folderID, fileName=zipFileName)

    #elimina el zip file que se creó en el mismo directorio de estos archivos
    removeZIP(zipFileName = zipFileName)

    # comparte la carpeta en la que se encuentra la copia de seguridad
    # sirve como una notificación de que se ha completado una copia de seguridad
    shareFileWithEmail(service=service, fileID=folderID, emailAddress=NOTIFICATION_EMIAL_ADDRESS)
					                        
    print("Filesystem backup complete...\n")

if __name__ == '__main__':
    main()

            
import os
from azure.storage.blob import BlobServiceClient
import streamlit as st
from utils.Config import Config

def upload_blob(file, file_name):
    try:
        # Criar o cliente do Blob Service
        blob_service_client = BlobServiceClient.from_connection_string(Config.AZURE_STORAGE_CONNECTION_STRING)
        # container_client = blob_service_client.get_container_client(container="cartoes", blob=file_name)
        container_client = blob_service_client.get_container_client(container="cartoes")


        # Criar o cliente do blob
        blob_client = container_client.get_blob_client(blob=file_name)

        # Upload do arquivo
        blob_client.upload_blob(file, overwrite=True)
        st.success(f"Arquivo '{file_name}' enviado com sucesso ao Blob Storage!")

        return blob_client.url
    except Exception as e:
        st.error(f"Erro ao enviar o arquivo: {e}")
        return None
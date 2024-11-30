import streamlit as st
from services.blob_service import upload_blob
from services.credit_card_service import analyze_credit_card


def configure_interface():
    st.title("Upload de arquivos DIO desafio 1 - Azure fake docs")
    upload_file = st.file_uploader("Escolha um arquivo", type=["png", "jpeg", "jpg"])

    if upload_file is not None:
        file_name = upload_file.name

        blob_url = upload_blob(upload_file, file_name)
        if blob_url:
            st.write(f"Arquivo {file_name} enviado para o blob com sucesso {blob_url}")

            credit_card_info = analyze_credit_card(blob_url)
            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.write(f"Erro ao enviar o arquivo {file_name} para o blob.")



def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption="Imagem enviada", use_column_width=True)
    st.write("Resultado da validacao:")
    if credit_card_info and credit_card_info["card_name"]:
        st.markdown(f"<h1 style='color: green;'>Cartão Válido</h1>", unsafe_allow_html=True)
        st.write(f"Nome do titular {credit_card_info['card_name']}")
        st.write(f"Banco EMissor {credit_card_info['bank_name']}")
        st.write(f"Data de validade {credit_card_info['expiry_date']}")
    else:
        st.markdown(f"<h1 style='color: red;'>Cartão Inválido</h1>", unsafe_allow_html=True)
        st.write("Este nao é um cartao de credito valido")



    st.write("Informacoes de cartao de credito encontrada:")
    st.write(credit_card_info)

if __name__ == "__main__":
    configure_interface()
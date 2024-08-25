from discord import SyncWebhook
import streamlit as st

webhook = SyncWebhook.from_url(
    "https://discord.com/api/webhooks/1277107363064840192/KWXgWbbfVh96SlUbYCRLwdkBdx24P6zoZ39zsFjSe87CYVkUtc7Ufw8qheoUlsyMqJ-j"
)
# webhook.send("This is a test message.")

st.title("Robux Giá Rẻ")

Name = st.text_input("Tên")
Email = st.text_input("Email")
Acc = st.text_input("Nhập tên acc Roblox")
Num = st.text_input("Số lượng Robux yêu cầu")

if st.button("Yêu cầu"):

    webhook.send(
        f"""
       ### New Request
    =================================
    Name: {Name}
    Email: {Email}
    Roblox account: {Acc}
    Request: {Num} R$
    """
    )

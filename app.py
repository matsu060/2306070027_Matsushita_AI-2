import streamlit as st
from country_api import get_country_info

st.title("🌍 国情報検索アプリ")

country_name = st.text_input("国名を入力してください（例: japan, france, brazil）")

if st.button("検索"):
    info = get_country_info(country_name)

    if info:
        st.subheader(info["name"])
        st.image(info["flag"], width=150)
        st.write(f"🏙 首都: {info['capital']}")
        st.write(f"👥 人口: {info['population']:,}")
        st.write(f"🌏 地域: {info['region']}")
    else:
        st.error("国情報を取得できませんでした。")

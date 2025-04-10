from dotenv import load_dotenv
import os
import streamlit as st
from langchain.llms import OpenAI

# .envファイルから環境変数を読み込む
load_dotenv()

# OpenAI APIキーを取得
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    st.error("OpenAI APIキーが設定されていません。環境変数にAPIキーを設定してください。")
else:
    # LangChainのOpenAI LLMを初期化
    llm = OpenAI(temperature=0.7, openai_api_key=OPENAI_API_KEY)

    st.title("生成AI質問アプリ")

    st.write("##### 生成AIを活用して質問に専門家が応答致します")

    # 専門家を選択
    selected_item = st.radio(
        "専門家を選択してください。",
        ["恋愛の専門家", "ビジネスの専門家", "健康の専門家"]
    )

    # ユーザーからの入力
    input_message = st.text_input(label="質問を入力してください。")

    st.divider()

    # 実行ボタン
    if st.button("実行"):
        st.divider()

        if input_message:
            # 各専門家に応じたプロンプトを生成
            if selected_item == "恋愛の専門家":
                prompt = f"あなたは恋愛の専門家です。以下の質問に答えてください: {input_message}"
            elif selected_item == "ビジネスの専門家":
                prompt = f"あなたはビジネスの専門家です。以下の質問に答えてください: {input_message}"
            elif selected_item == "健康の専門家":
                prompt = f"あなたは健康の専門家です。以下の質問に答えてください: {input_message}"

            # LLMに質問を送信して回答を取得
            with st.spinner("回答を生成中..."):
                try:
                    response = llm(prompt)
                    st.write(f"**{selected_item}からの回答:** {response}")
                except Exception as e:
                    st.error(f"エラーが発生しました: {e}")
        else:
            st.error("質問を入力してください。")
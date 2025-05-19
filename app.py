# app.py
import streamlit as st

questions = {
    "1章": {
        "question": "生成AIとは何かについて、正しいものはどれ？",
        "options": ["感情を持つ", "完全に自律思考する", "学習データに基づいて生成する", "画像生成専用である"],
        "answer": "学習データに基づいて生成する",
        "explanation": "生成AIは事前に学習した大量のデータを元に文章や画像などを生成します。"
    }
}

st.title("📘 PEP試験 四択問題アプリ")

chapter = st.selectbox("章を選択してください", list(questions.keys()))
q = questions[chapter]

st.subheader(q["question"])
selected = st.radio("選択肢", q["options"])

if st.button("回答する"):
    if selected == q["answer"]:
        st.success("✅ 正解です！")
    else:
        st.error("❌ 不正解です。")
    st.markdown(f"📝 解説：{q['explanation']}")

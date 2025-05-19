import streamlit as st
import random

# 章ごとの問題（難易度付き）
questions = {
    "1章": {
        "初級": [
            {
                "question": "生成AIとは何かについて、正しいものはどれ？",
                "options": ["感情を持つ", "完全に自律思考する", "学習データに基づいて生成する", "画像生成専用である"],
                "answer": "学習データに基づいて生成する",
                "explanation": "生成AIは事前に学習した大量のデータを元に文章や画像などを生成します。"
            }
        ],
        "中級": []
    },
    "2章": {
        "初級": [
            {
                "question": "LLM（大規模言語モデル）の特徴として正しいものはどれ？",
                "options": ["少量のデータで学習する", "人間の感情を模倣する", "膨大なデータとパラメータを持つ", "画像を分類する専用"],
                "answer": "膨大なデータとパラメータを持つ",
                "explanation": "LLMは非常に大規模なデータセットとパラメータを用いることで、文脈理解や生成能力を高めています。"
            }
        ],
        "中級": []
    }
}

st.title("📘 PEP試験 四択問題アプリ")

# 初期化
if "chapter" not in st.session_state:
    st.session_state.chapter = "ランダム"
if "difficulty" not in st.session_state:
    st.session_state.difficulty = "初級"
if "current_question" not in st.session_state:
    st.session_state.current_question = None

# UI入力
chapter_options = list(questions.keys()) + ["ランダム"]
chapter = st.selectbox("章を選択してください（ランダムも可）", chapter_options, index=chapter_options.index(st.session_state.chapter))
difficulty = st.radio("難易度を選択してください", ["初級", "中級"], index=["初級", "中級"].index(st.session_state.difficulty))

st.session_state.chapter = chapter
st.session_state.difficulty = difficulty

# 次の問題を生成
if st.button("次の問題") or st.session_state.current_question is None:
    available_chapters = list(questions.keys())
    selected_chapter = random.choice(available_chapters) if chapter == "ランダム" else chapter

    if difficulty in questions[selected_chapter] and questions[selected_chapter][difficulty]:
        st.session_state.selected_chapter = selected_chapter
        st.session_state.current_question = random.choice(questions[selected_chapter][difficulty])
        st.session_state.answered = False
    else:
        st.warning("⚠️ 選択された章・難易度の問題が見つかりませんでした。別の組み合わせを選んでください。")
        st.stop()

q = st.session_state.current_question

st.subheader(f"【{st.session_state.selected_chapter}・{difficulty}】{q['question']}")
choice = st.radio("選択肢を選んでください", q["options"], key=q["question"])

if st.button("回答"):
    st.session_state.answered = True
    if choice == q["answer"]:
        st.success("✅ 正解です！")
    else:
        st.error("❌ 不正解です。")
    st.markdown(f"**解説：** {q['explanation']}")

if st.session_state.answered:
    st.info("💡 '次の問題'ボタンで再挑戦できます")


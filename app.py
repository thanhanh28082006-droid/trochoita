import streamlit as st
import time

# --- CẤU HÌNH TRANG ---
st.set_page_config(page_title="Giải mã Thông điệp", page_icon="💎", layout="wide")

# --- DỮ LIỆU CÂU HỎI (9 Câu Tiếng Anh) ---
QUESTIONS = [
    {
        "id": 1,
        "word": "CHÚC",
        "question": "The new apartment is very ______, with large windows and modern furniture.",
        "options": ["A. resident", "B. comfortable", "C. solution", "D. engineer"],
        "answer": "B. comfortable"
    },
    {
        "id": 2,
        "word": "THẦY",
        "question": "A person who designs buildings and houses is called an ______.",
        "options": ["A. architect", "B. resident", "C. engineer", "D. owner"],
        "answer": "A. architect"
    },
    {
        "id": 3,
        "word": "VÀ",
        "question": "The apartment is small, ______ it has everything we need.",
        "options": ["A. and", "B. or", "C. so", "D. but"],
        "answer": "D. but"
    },
    {
        "id": 4,
        "word": "CÁC",
        "question": "You can live in the city ______ move to the countryside.",
        "options": ["A. but", "B. so", "C. or", "D. and"],
        "answer": "C. or"
    },
    {
        "id": 5,
        "word": "BẠN",
        "question": "The house is close to the city center, ______ it is easy to travel to work.",
        "options": ["A. so", "B. but", "C. or", "D. and"],
        "answer": "A. so"
    },
    {
        "id": 6,
        "word": "MỘT",
        "question": "Which sentence uses “and” correctly?",
        "options": ["A. The house is beautiful and comfortable.", "B. The house is expensive and we couldn't afford it.", "C. It was raining and we stayed home because of it.", "D. You can walk and take a bus."],
        "answer": "A. The house is beautiful and comfortable."
    },
    {
        "id": 7,
        "word": "NGÀY",
        "question": "Which sentence best shows contrast?",
        "options": ["A. The house is large, and it has a garden.", "B. The house is expensive, but it is very luxurious.", "C. You can rent an apartment or buy a house.", "D. It was raining, so we stayed inside."],
        "answer": "B. The house is expensive, but it is very luxurious."
    },
    {
        "id": 8,
        "word": "TỐT",
        "question": "The word “luxury” is closest in meaning to:",
        "options": ["A. A basic necessity", "B. Something expensive and comfortable", "C. A person living in a house", "D. A problem that needs solving"],
        "answer": "B. Something expensive and comfortable"
    },
    {
        "id": 9,
        "word": "LÀNH",
        "question": "Choose the sentence with the best conjunction:<br><br><i>The house is far from the city center. ______, it is quiet and peaceful.</i>",
        "options": ["A. And", "B. Or", "C. But", "D. So"],
        "answer": "C. But"
    }
]

# --- KHỞI TẠO SESSION STATE ---
if 'revealed_words' not in st.session_state:
    st.session_state.revealed_words = [False] * 9 # Có 9 chữ cái
if 'game_won' not in st.session_state:
    st.session_state.game_won = False

# --- HÀM XỬ LÝ DIALOG CÂU HỎI ---
@st.dialog("🎯 THỬ THÁCH TIẾNG ANH", width="large")
def show_question_modal(idx):
    q_data = QUESTIONS[idx]
    
    # State quản lý trạng thái trong modal
    if f"q_status_{idx}" not in st.session_state:
        st.session_state[f"q_status_{idx}"] = "playing"
    
    st.markdown(f"<div class='question-text'>{q_data['question']}</div>", unsafe_allow_html=True)
    
    if st.session_state[f"q_status_{idx}"] == "correct":
        st.success("🎉 TUYỆT VỜI! BẠN ĐÃ TRẢ LỜI ĐÚNG. Chữ cái đã được mở!")
        time.sleep(2)
        st.rerun()
    else:
        if st.session_state[f"q_status_{idx}"] == "wrong":
            st.error("❌ Bạn trả lời sai rồi! Bạn chọn lại đi.")
            
        ans_cols = st.columns(2)
        for i, option in enumerate(q_data['options']):
            with ans_cols[i % 2]:
                if st.button(option, key=f"opt_{idx}_{i}", use_container_width=True):
                    if option == q_data['answer']:
                        st.session_state[f"q_status_{idx}"] = "correct"
                        st.session_state.revealed_words[idx] = True
                        st.rerun()
                    else:
                        st.session_state[f"q_status_{idx}"] = "wrong"
                        st.rerun()

# --- CSS TÙY CHỈNH (NỀN XANH NƯỚC BIỂN SANG TRỌNG) ---
st.markdown("""
<style>
    /* Màu nền tổng thể - Xanh nước biển siêu nhạt */
    .stApp { background-color: #E3F2FD; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    
    /* Container viền trắng nổi bật */
    .white-container { background-color: #FFFFFF; border-radius: 20px; padding: 25px; box-shadow: 0 8px 20px rgba(25, 118, 210, 0.15); margin-bottom: 20px; position: relative; }
    
    /* Font chữ câu hỏi */
    .question-text { font-size: 24px; color: #1a1a1a; text-align: center; margin-bottom: 30px; font-weight: 600; line-height: 1.5; }
    
    /* Ô chữ - Đổ dải màu xanh biển sáng */
    .word-box { display: flex; justify-content: center; align-items: center; height: 80px; background: linear-gradient(135deg, #1E88E5, #1565C0); color: white; border-radius: 15px; font-size: 20px; font-weight: bold; box-shadow: 0 4px 10px rgba(21, 101, 192, 0.3); }
    .word-hidden { background: #E0E0E0; color: #9E9E9E; box-shadow: none;}
    
    /* Nút bấm làm mềm mại */
    div.stButton > button { border-radius: 15px; font-weight: bold; height: 60px; font-size: 16px !important; border: 1px solid #BBDEFB; transition: 0.3s; }
    div.stButton > button:hover { border-color: #1E88E5; color: #1565C0; background-color: #F3E5F5; }
    
    /* Tiêu đề chính */
    .main-title { text-align: center; color: #1565C0; font-size: 40px; font-weight: 900; margin-bottom: 30px; text-transform: uppercase; text-shadow: 2px 2px 4px rgba(21, 101, 192, 0.2); }
</style>
""", unsafe_allow_html=True)

# --- GIAO DIỆN CHÍNH ---
st.markdown('<div class="main-title">🔍 TRÒ CHƠI GIẢI MÃ THÔNG ĐIỆP BÍ MẬT 💙</div>', unsafe_allow_html=True)

st.markdown('<div class="white-container">', unsafe_allow_html=True)
cols = st.columns(9) # Chia thành 9 cột cho 9 chữ
for i, col in enumerate(cols):
    with col:
        if st.session_state.revealed_words[i]:
            st.markdown(f'<div class="word-box">{QUESTIONS[i]["word"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="word-box word-hidden">?</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.subheader("🎯 Chọn câu hỏi để giải mã")
btn_cols = st.columns(9) # 9 nút bấm
for i, b_col in enumerate(btn_cols):
    with b_col:
        btn_label = f"Câu {i+1}" if not st.session_state.revealed_words[i] else "✅"
        if st.button(btn_label, key=f"btn_{i}", disabled=st.session_state.revealed_words[i]):
            show_question_modal(i)

# --- HIỆU ỨNG CHIẾN THẮNG THEO CONCEPT XANH ---
if all(st.session_state.revealed_words):
    st.balloons()
    st.markdown("""
    <style>
    @keyframes fall {
        0% { transform: translateY(-10vh) rotate(0deg); opacity: 1;}
        100% { transform: translateY(100vh) rotate(360deg); opacity: 0;}
    }
    .flower { position: fixed; font-size: 30px; z-index: 9999; top: -10vh; animation: fall linear forwards; }
    </style>
    <script>
    const flowers = ['💎', '🌟', '✨', '🎓', '💙', '📚']; // Icons học tập & sang trọng
    for(let i=0; i<60; i++) {
        let f = document.createElement('div');
        f.className = 'flower';
        f.innerText = flowers[Math.floor(Math.random() * flowers.length)];
        f.style.left = Math.random() * 100 + 'vw';
        f.style.animationDuration = (Math.random() * 3 + 2) + 's';
        f.style.animationDelay = Math.random() * 2 + 's';
        document.body.appendChild(f);
    }
    </script>
    """, unsafe_allow_html=True)
    st.success("🎉 XUẤT SẮC! BẠN ĐÃ GIẢI MÃ THÀNH CÔNG TOÀN BỘ THÔNG ĐIỆP!")

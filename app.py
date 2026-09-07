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
    status_key = f"q_status_{idx}"
    if status_key not in st.session_state:
        st.session_state[status_key] = "playing"
    
    st.markdown(f"<div class='question-text'>{q_data['question']}</div>", unsafe_allow_html=True)
    
    # Tạo một không gian trống (placeholder) để nhét thông báo lỗi vào
    error_msg_placeholder = st.empty()
    
    # Nếu trạng thái đang là sai, hiện thông báo lỗi lên
    if st.session_state[status_key] == "wrong":
        error_msg_placeholder.markdown("<div class='error-message'>❌ Sai rồi! Bạn hãy đọc kỹ và chọn lại đáp án nhé.</div>", unsafe_allow_html=True)
            
    ans_cols = st.columns(2)
    for i, option in enumerate(q_data['options']):
        with ans_cols[i % 2]:
            if st.button(option, key=f"opt_{idx}_{i}", use_container_width=True):
                if option == q_data['answer']:
                    st.session_state[status_key] = "correct"
                    st.session_state.revealed_words[idx] = True
                    # Tắt tab ngay lập tức và lật chữ bên ngoài màn hình chính
                    st.rerun() 
                else:
                    st.session_state[status_key] = "wrong"
                    # Bắn thông báo lỗi vào không gian trống mà KHÔNG DÙNG lệnh tắt tab
                    error_msg_placeholder.markdown("<div class='error-message'>❌ Sai rồi! Bạn hãy đọc kỹ và chọn lại đáp án nhé.</div>", unsafe_allow_html=True)

# --- CSS TÙY CHỈNH (SANG TRỌNG, BÓNG BẨY) ---
st.markdown("""
<style>
    /* Màu nền tổng thể - Gradient pha trộn cực sang trọng */
    .stApp { background: linear-gradient(135deg, #e3f2fd, #e8eaf6, #bbdefb); font-family: 'Segoe UI', Tahoma, Geneva, sans-serif; }
    
    /* Container viền trắng hiệu ứng kính (Glassmorphism) */
    .white-container { 
        background-color: rgba(255, 255, 255, 0.75); 
        backdrop-filter: blur(15px); 
        border-radius: 25px; 
        padding: 35px; 
        box-shadow: 0 20px 40px rgba(21, 101, 192, 0.15); 
        border: 1px solid rgba(255,255,255,0.9); 
        margin-bottom: 25px; 
    }
    
    /* Font chữ câu hỏi to, sắc nét, màu biển sâu */
    .question-text { 
        font-size: 34px; 
        color: #0D47A1; 
        text-align: center; 
        margin-bottom: 30px; 
        font-weight: 800; 
        line-height: 1.5; 
        text-shadow: 1px 1px 3px rgba(0,0,0,0.1); 
    }
    
    /* Banner báo lỗi siêu đẹp ngay trong tab */
    .error-message { 
        background: linear-gradient(90deg, #ffeb3b, #ffc107); 
        color: #b71c1c; 
        padding: 15px; 
        border-radius: 15px; 
        text-align: center; 
        font-size: 24px; 
        font-weight: bold; 
        margin-bottom: 25px; 
        border-left: 8px solid #d32f2f; 
        box-shadow: 0 4px 15px rgba(211, 47, 47, 0.3);
    }
    
    /* Ô chữ - Hiệu ứng Glossy 3D siêu bóng bẩy, chữ khổng lồ */
    .word-box { 
        display: flex; justify-content: center; align-items: center; 
        height: 110px; 
        background: linear-gradient(145deg, #42a5f5, #1565C0); 
        color: white; 
        border-radius: 20px; 
        font-size: 42px; 
        font-weight: 900; 
        box-shadow: inset 0px 6px 12px rgba(255,255,255,0.6), 0px 12px 25px rgba(21, 101, 192, 0.5); 
        text-shadow: 2px 2px 6px rgba(0,0,0,0.5); 
        border: 2px solid #90caf9; 
        margin: 5px; 
    }
    .word-hidden { 
        background: linear-gradient(145deg, #ffffff, #eeeeee); 
        color: #bdbdbd; 
        box-shadow: inset 0px 5px 10px rgba(255,255,255,1), 0px 8px 15px rgba(0,0,0,0.1); 
        border: 2px solid #e0e0e0; 
        text-shadow: none;
    }
    
    /* Nút bấm làm to ra, hiệu ứng đổ bóng mượt mà */
    div.stButton > button { 
        border-radius: 20px; 
        font-weight: 800; 
        height: 85px; 
        font-size: 24px !important; 
        border: 2px solid #90caf9; 
        background: linear-gradient(to bottom, #ffffff, #e3f2fd); 
        color: #0D47A1; 
        box-shadow: 0 6px 15px rgba(21, 101, 192, 0.15); 
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1); 
        white-space: normal; 
    }
    div.stButton > button:hover { 
        border-color: #1565C0; 
        color: white; 
        background: linear-gradient(145deg, #1E88E5, #0D47A1); 
        box-shadow: 0 10px 25px rgba(13, 71, 161, 0.5); 
        transform: translateY(-5px); 
    }
    
    /* Tiêu đề chính */
    .main-title { 
        text-align: center; 
        font-size: 50px; 
        font-weight: 900; 
        margin-bottom: 40px; 
        text-transform: uppercase; 
        background: linear-gradient(to right, #1565C0, #D81B60, #1565C0); 
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent; 
        text-shadow: 3px 3px 8px rgba(0,0,0,0.15); 
    }
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

# --- KHU VỰC DÀNH CHO NGƯỜI CHƠI ĐOÁN TRƯỚC THÔNG ĐIỆP ---
st.markdown("<br><br>", unsafe_allow_html=True)
col_empty1, col_guess, col_empty2 = st.columns([1, 2, 1])
with col_guess:
    st.markdown("<div style='text-align: center; font-size: 28px; font-weight: 800; color: #0D47A1; margin-bottom: 15px;'>💡 Bạn đã tìm ra thông điệp?</div>", unsafe_allow_html=True)
    if st.button("🌟 LẬT MỞ TOÀN BỘ THÔNG ĐIỆP NGAY 🌟", key="btn_reveal_all", use_container_width=True):
        st.session_state.revealed_words = [True] * 9
        st.rerun()

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

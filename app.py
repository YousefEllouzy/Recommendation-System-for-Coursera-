import pickle
import streamlit as st
import time
from sklearn.metrics.pairwise import cosine_similarity

# تحميل بيانات الدورات
courses_list = pickle.load(open('courses.pkl', 'rb'))

# تحميل الـ TF-IDF vectorizer و الـ TF-IDF vectors
with open('tfidf_vectorizer.pkl', 'rb') as f:
    tfidf_vectorizer = pickle.load(f)

with open('tfidf_vectors.pkl', 'rb') as f:
    tfidf_vectors = pickle.load(f)

# حساب التشابه باستخدام cosine similarity
similarity = cosine_similarity(tfidf_vectors)

# دالة التوصية
def recommend(course):
    index = courses_list[courses_list['course_name'] == course].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_course_names = []
    for i in distances[1:7]:  # أخذ أول 6 دورات مشابهة
        course_name = courses_list.iloc[i[0]].course_name
        recommended_course_names.append(course_name)
    return recommended_course_names

# إعداد واجهة المستخدم (UI) باستخدام Streamlit
st.markdown(f"""
    <style>
    body {{
        font-family: 'Poppins', sans-serif;
        margin: 0;
        padding: 0;
        background: linear-gradient(45deg, #1a73e8, #f39c12);
    }}
    .main {{
        padding: 50px;
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        animation: fadeIn 2s ease-out;
        background-color: rgba(255, 255, 255, 0.8);
    }}
    .title {{
        font-size: 50px;
        font-weight: bold;
        color: #1a73e8;
        text-align: center;
        margin-bottom: 20px;
        animation: slideInFromTop 1s ease-out;
    }}
    .subtitle {{
        font-size: 22px;
        font-weight: 500;
        color: #444;
        text-align: center;
        margin-bottom: 40px;
        animation: slideInFromBottom 1s ease-out;
    }}
    .recommendation-title {{
        font-size: 28px;
        font-weight: bold;
        color: #f39c12;
        margin-top: 40px;
        animation: fadeIn 2s ease-out;
    }}
    .stButton>button {{
        background-color: #1a73e8;
        color: white;
        padding: 12px 24px;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        font-weight: bold;
        animation: bounceButton 1s ease-in-out infinite;
    }}
    .stButton>button:hover {{
        background-color: #1669c1;
        transform: scale(1.1);
        transition: transform 0.3s ease, background-color 0.3s ease;
    }}
    .course-card {{
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        text-align: center;
        transition: transform 0.3s ease-in-out, box-shadow 0.3s ease;
        animation: fadeInCard 1s ease-out;
        margin: 10px;
    }}
    .course-card:hover {{
        transform: scale(1.05);
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.2);
    }}
    .course-card h3 {{
        margin: 0;
        color: #333;
        font-size: 18px;
        font-weight: 600;
    }}
    .course-card p {{
        color: #666;
        font-size: 14px;
        margin-top: 10px;
    }}
    .footer {{
        text-align: center;
        margin-top: 50px;
        font-size: 16px;
        color: #444;
        animation: fadeInFooter 2s ease-out;
        padding: 20px 0;
    }}
    .footer .copyright {{
        font-size: 14px;
        color: #666;
        margin-bottom: 10px;
    }}
    .footer .signature {{
        font-size: 16px;
        font-style: italic;
        margin-top: 5px;
        color: #f39c12;
    }}
    .stSelectbox {{
        width: 100%;
        font-size: 24px;
        padding: 10px;
        margin-bottom: 20px;
        border: 2px solid #1a73e8;
        border-radius: 8px;
        background: linear-gradient(135deg, #1a73e8, #f39c12);
        color: white;
    }}
    .stSelectbox select {{
        font-size: 22px;
    }}
    .stLabel {{
        font-size: 28px;
        font-weight: bold;
    }}
    @keyframes fadeIn {{
        0% {{ opacity: 0; }}
        100% {{ opacity: 1; }}
    }}
    @keyframes slideInFromTop {{
        0% {{ transform: translateY(-100%); }}
        100% {{ transform: translateY(0); }}
    }}
    @keyframes slideInFromBottom {{
        0% {{ transform: translateY(100%); }}
        100% {{ transform: translateY(0); }}
    }}
    @keyframes fadeInCard {{
        0% {{ opacity: 0; }}
        100% {{ opacity: 1; }}
    }}
    @keyframes fadeInFooter {{
        0% {{ opacity: 0; }}
        100% {{ opacity: 1; }}
    }}
    </style>
""", unsafe_allow_html=True)

time.sleep(1)

st.markdown("<div class='main'>", unsafe_allow_html=True)
st.markdown("<h1 class='title'>Coursera Smart Course Finder</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Explore courses tailored to your interests from thousands of options on Coursera Smart Course Finder!</p>", unsafe_allow_html=True)

course_list = courses_list['course_name'].values
selected_course = st.selectbox("Choose a course you're interested in:", course_list, key="course_select", label_visibility="visible")

if st.button('Show Recommended Courses'):
    st.markdown("<h3 class='recommendation-title'>Recommended Courses for You:</h3>", unsafe_allow_html=True)
    recommended_course_names = recommend(selected_course)
    
    columns = st.columns(3)
    
    for i, course in enumerate(recommended_course_names):
        with columns[i % 3]:
            st.markdown(f"""
            <div class='course-card'>
                <h3>{course}</h3>
                <p>Description for {course}...</p>
            </div>
            """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("""
    <div class="footer">
        <p class="copyright">&copy; 2024 Your Name. All Rights Reserved.</p>
        <p class="signature">Designed by Yousef Ellouzey</p>
    </div>
""", unsafe_allow_html=True)

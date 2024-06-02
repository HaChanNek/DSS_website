import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import base64

# Đọc dữ liệu
file_path = '/Users/___tt.h_/PycharmProjects/pythonProject/hotel_booking.csv'
data = pd.read_csv(file_path)

# Đường dẫn tới các tệp logo và hình nền
logo_path = '/Users/___tt.h_/PycharmProjects/pythonProject/logo-dlg-hotel-danang.png'
background_path = '/Users/___tt.h_/PycharmProjects/pythonProject/aboutbanner.jpg'

# Tạo base64 từ hình ảnh để sử dụng trong CSS
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Lấy base64 của hình nền và logo
bg_img_base64 = get_base64_of_bin_file(background_path)
logo_base64 = get_base64_of_bin_file(logo_path)

# Thiết lập giao diện Streamlit
st.set_page_config(page_title="WELCOME TO DLG HOTEL'S DASHBOARD REPORT", page_icon=":hotel:", layout="wide")

# Custom CSS để thay đổi màu nền và làm mờ hình nền
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/jpg;base64,{bg_img_base64}) no-repeat center center fixed;
        background-size: cover;
    }}
    .main {{
        background: RGBA( 240, 255, 255, 1 ); /* Nền trắng với độ trong suốt */
        padding: 20px;
        border-radius: 10px;
    }}
    .sidebar .sidebar-content {{
        background-color: #C6E2FF;
    }}
    h1 {{
        color: #00274d;
        text-align: center;
    }}
    .centered-text {{
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        color: #00274d;
    }}
    .logo-container {{
        text-align: center;
        margin-top: 20px;
    }}
    .logo {{
        width: 150px;  /* Điều chỉnh kích thước logo ở đây */
    }}
    .banner {{
        position: relative;
        width: 100%;
        text-align: center;
        margin-bottom: 20px;
    }}
    .banner img {{
        width: 100%;
        height: auto;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Thêm logo ở trên cùng
st.markdown(
    f"""
    <div class="logo-container">
        <img src="data:image/png;base64,{logo_base64}" alt="Logo" class="logo">
    </div>
    """,
    unsafe_allow_html=True
)

# Thêm banner
st.markdown(
    f"""
    <div class="banner">
        <img src="data:image/jpg;base64,{bg_img_base64}" alt="Banner">
    </div>
    """,
    unsafe_allow_html=True
)

# Tiêu đề chính của trang
st.markdown("<h1>WELCOME TO DLG HOTEL'S DASHBOARD REPORT</h1>", unsafe_allow_html=True)

# Chức năng đầu tiên
st.sidebar.title("Report Options")
report_option = st.sidebar.radio("Choose Report", ("Cancellation Report", "Survey Report"))

if report_option == "Cancellation Report":
    st.markdown("<div class='centered-text'>Visualizations to Summarize the following key customer characteristics</div>", unsafe_allow_html=True)

    # Tạo cột cho các biểu đồ
    col1, col2 = st.columns(2)

    # Distribution of Booking Cancellations
    with col1:
        if st.checkbox("Distribution of Booking Cancellations"):
            fig, ax = plt.subplots()
            sns.countplot(x='is_canceled', data=data, palette='pastel', ax=ax)
            ax.set_title('Distribution of Booking Cancellations', fontsize=16)
            ax.set_xlabel('Cancellation Status', fontsize=12)
            ax.set_ylabel('Frequency', fontsize=12)
            st.pyplot(fig)

    # Lead Time Distribution
    with col2:
        if st.checkbox("Lead Time Distribution"):
            fig, ax = plt.subplots()
            sns.histplot(data['lead_time'], bins=50, kde=True, color='skyblue', ax=ax)
            ax.set_title('Lead Time Distribution', fontsize=16)
            ax.set_xlabel('Lead Time (days)', fontsize=12)
            ax.set_ylabel('Frequency', fontsize=12)
            st.pyplot(fig)

    # Distribution of Weekend and Week Nights Stays
    col3, col4 = st.columns(2)
    with col3:
        if st.checkbox("Distribution of Weekend and Week Nights Stays"):
            fig, ax = plt.subplots()
            data[['stays_in_weekend_nights', 'stays_in_week_nights']].plot(kind='hist', bins=50, alpha=0.5, ax=ax,
                                                                           color=['lightcoral', 'lightskyblue'])
            ax.set_title('Distribution of Weekend and Week Nights Stays', fontsize=16)
            ax.set_xlabel('Number of Nights', fontsize=12)
            ax.set_ylabel('Frequency', fontsize=12)
            st.pyplot(fig)

    # Distribution of Number of Adults, Children, and Babies
    with col4:
        if st.checkbox("Distribution of Number of Adults, Children, and Babies"):
            fig, ax = plt.subplots()
            data[['adults', 'children', 'babies']].plot(kind='hist', bins=50, alpha=0.5, ax=ax,
                                                        color=['lightgreen', 'lightpink', 'lightblue'])
            ax.set_title('Distribution of Number of Adults, Children, and Babies', fontsize=16)
            ax.set_xlabel('Number of People', fontsize=12)
            ax.set_ylabel('Frequency', fontsize=12)
            st.pyplot(fig)

    # Market Segment Distribution
    col5, col6 = st.columns(2)
    with col5:
        if st.checkbox("Market Segment Distribution"):
            fig, ax = plt.subplots()
            sns.countplot(x='market_segment', data=data, palette='muted', ax=ax)
            ax.set_title('Market Segment Distribution', fontsize=16)
            ax.set_xlabel('Market Segment', fontsize=12)
            ax.set_ylabel('Frequency', fontsize=12)
            plt.xticks(rotation=45)
            st.pyplot(fig)

    # Total Special Requests Distribution
    with col6:
        if st.checkbox("Total Special Requests Distribution"):
            fig, ax = plt.subplots()
            sns.countplot(x='total_of_special_requests', data=data, palette='pastel', ax=ax)
            ax.set_title('Total Special Requests Distribution', fontsize=16)
            ax.set_xlabel('Number of Special Requests', fontsize=12)
            ax.set_ylabel('Frequency', fontsize=12)
            st.pyplot(fig)

elif report_option == "Survey Report":
    st.markdown("<div class='centered-text'>Survey Report</div>", unsafe_allow_html=True)

    survey_option = st.radio("Choose Survey Report", ("Cancellation Report", "Rebooking Report"))

    def display_images_from_folder(folder_path, columns=3):
        images = [img for img in os.listdir(folder_path) if img.endswith('.png')]
        total_images = len(images)
        rows = total_images // columns + int(total_images % columns > 0)

        for row in range(rows):
            cols = st.columns(columns)
            for col in range(columns):
                index = row * columns + col
                if index < total_images:
                    image_path = os.path.join(folder_path, images[index])
                    with cols[col]:
                        st.image(image_path, caption=images[index][:-4])

    if survey_option == "Cancellation Report":
        st.markdown("<div class='centered-text'>Cancellation Report</div>", unsafe_allow_html=True)
        display_images_from_folder('/Users/___tt.h_/PycharmProjects/pythonProject/Cancellation', columns=3)

    elif survey_option == "Rebooking Report":
        st.markdown("<div class='centered-text'>Rebooking Report</div>", unsafe_allow_html=True)
        display_images_from_folder('/Users/___tt.h_/PycharmProjects/pythonProject/Rebooking test', columns=3)

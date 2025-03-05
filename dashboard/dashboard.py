import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load data
day_df = pd.read_csv("data/day.csv")
hour_df = pd.read_csv("data/hour.csv")

# Konversi kolom tanggal
day_df["dteday"] = pd.to_datetime(day_df["dteday"])
hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])

# Sidebar
st.sidebar.image(
    "https://img.freepik.com/free-vector/bike-sharing-abstract-concept-illustration_335657-3741.jpg?t=st=1741176107~exp=1741179707~hmac=cddbe4c22d9a1832927337e248390713d92163f94f05ff79497bda8729ca5325&w=900",
    use_container_width=True
)

st.sidebar.header("📅 Filter Waktu")

# Pilih bulan & tahun
month_list = sorted(day_df["dteday"].dt.month.unique())
year_list = sorted(day_df["dteday"].dt.year.unique())

selected_month = st.sidebar.selectbox("Pilih Bulan:", month_list, index=0)
selected_year = st.sidebar.selectbox("Pilih Tahun:", year_list, index=0)

# Pilih jam (hanya untuk data per jam)
selected_hour = st.sidebar.slider("Pilih Jam:", min_value=0, max_value=23, value=(0, 23))

# Filter data berdasarkan bulan & tahun
filtered_day_df = day_df[
    (day_df["dteday"].dt.month == selected_month) &
    (day_df["dteday"].dt.year == selected_year)
]

filtered_hour_df = hour_df[
    (hour_df["dteday"].dt.month == selected_month) &
    (hour_df["dteday"].dt.year == selected_year) &
    (hour_df["hr"] >= selected_hour[0]) &
    (hour_df["hr"] <= selected_hour[1])
]

# Header
st.title("🚴‍♂️ Dashboard Bike Sharing 🚲")
st.write("Analisis penggunaan sepeda berdasarkan cuaca, hari kerja, dan jam.")

# Tabs untuk berbagai analisis
tab1, tab2, tab3 = st.tabs(["🌤 Pengaruh Cuaca", "📆 Pola Harian", "🕒 Pola Jam"])

# **🌤 Analisis Pengaruh Cuaca**
with tab1:
    st.subheader("🌤 Pengaruh Cuaca terhadap Penggunaan Sepeda")

    # Boxplot Cuaca vs Jumlah Pengguna Sepeda
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(x="weathersit", y="cnt", data=filtered_day_df, palette="coolwarm", ax=ax)
    ax.set_xticklabels(["Cerah", "Berawan", "Hujan/Salju"])
    ax.set_xlabel("Kondisi Cuaca")
    ax.set_ylabel("Jumlah Pengguna Sepeda")
    st.pyplot(fig)

# **📆 Pola Penggunaan Sepeda Berdasarkan Hari Kerja & Akhir Pekan**
with tab2:
    st.subheader("📆 Pola Penggunaan Sepeda: Hari Kerja vs Akhir Pekan")

    # Boxplot Hari Kerja vs Akhir Pekan
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(x="workingday", y="cnt", data=filtered_day_df, palette="Set2", ax=ax)
    ax.set_xticklabels(["Akhir Pekan", "Hari Kerja"])
    ax.set_xlabel("Kategori")
    ax.set_ylabel("Jumlah Pengguna Sepeda")
    st.pyplot(fig)

# **🕒 Pola Penggunaan Sepeda Berdasarkan Jam**
with tab3:
    st.subheader("🕒 Pola Penggunaan Sepeda Berdasarkan Jam")

    # Line Chart Pola Jam
    fig = px.line(filtered_hour_df.groupby("hr")["cnt"].mean().reset_index(), x="hr", y="cnt", markers=True)
    fig.update_layout(xaxis_title="Jam", yaxis_title="Jumlah Pengguna Sepeda")
    st.plotly_chart(fig)

# Menjalankan Streamlit
if __name__ == "__main__":
    st.sidebar.success("Pilih tab untuk melihat analisis lebih lanjut")  

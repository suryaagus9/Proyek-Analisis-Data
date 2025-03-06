import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
all_df = pd.read_csv("dashboard/main_data.csv")

# Sidebar
st.sidebar.image(
    "https://img.freepik.com/free-vector/bike-sharing-abstract-concept-illustration_335657-3741.jpg",
    use_container_width=True
)

st.sidebar.header("📅 Filter Waktu")

# Pilih rentang tanggal
min_date = pd.to_datetime(all_df["dteday"].min())
max_date = pd.to_datetime(all_df["dteday"].max())
date_range = st.sidebar.date_input("Pilih Rentang Tanggal:", [min_date, max_date], min_value=min_date, max_value=max_date)

# Pilih bulan & tahun dengan opsi "Semua"
month_list = ["Semua"] + sorted(all_df["mnth"].unique().tolist())

# Konversi tahun dari angka ke label yang sesuai
year_mapping = {0: "2011", 1: "2012"}
year_list = ["Semua"] + [year_mapping[y] for y in sorted(all_df["yr"].unique())]

selected_month = st.sidebar.selectbox("Pilih Bulan:", month_list, index=0)
selected_year = st.sidebar.selectbox("Pilih Tahun:", year_list, index=0)

# Pilih jam
selected_hour = st.sidebar.slider("Pilih Jam:", min_value=0, max_value=23, value=(0, 23))

# Filter data berdasarkan rentang tanggal, bulan & tahun
all_df["dteday"] = pd.to_datetime(all_df["dteday"])
filtered_df = all_df[
    (all_df["dteday"] >= pd.to_datetime(date_range[0])) & 
    (all_df["dteday"] <= pd.to_datetime(date_range[1])) & 
    (all_df["hr"] >= selected_hour[0]) & (all_df["hr"] <= selected_hour[1])
]

if selected_month != "Semua":
    filtered_df = filtered_df[filtered_df["mnth"] == int(selected_month)]

if selected_year != "Semua":
    filtered_df = filtered_df[filtered_df["yr"] == int([k for k, v in year_mapping.items() if v == selected_year][0])]


# Header
st.title("🚴‍♂️ Dashboard Bike Sharing 🚲")
st.write("Analisis penggunaan sepeda berdasarkan cuaca, musim, hari kerja, dan jam.")

# Pengaruh Kondisi Cuaca terhadap Jumlah Pengguna Sepeda
st.subheader("🌦 Pengaruh Cuaca terhadap Penggunaan Sepeda")
weather_data = filtered_df.groupby("weathersit")["cnt"].mean().reset_index()
weather_labels = {1: "Cerah", 2: "Berawan", 3: "Hujan/Salju"}
fig = px.bar(weather_data, x="weathersit", y="cnt", text_auto=True, color="cnt", labels={"weathersit": "Kondisi Cuaca", "cnt": "Jumlah Pengguna Sepeda"}, color_continuous_scale="blues")
fig.update_xaxes(tickmode="array", tickvals=[1, 2, 3], ticktext=list(weather_labels.values()))
st.plotly_chart(fig)

# Pengaruh Musim terhadap Jumlah Pengguna Sepeda
st.subheader("🌤 Pengaruh Musim terhadap Penggunaan Sepeda")
season_data = filtered_df.groupby("season")["cnt"].mean().reset_index()
season_labels = {1: "Semi", 2: "Panas", 3: "Gugur", 4: "Dingin"}
fig = px.bar(season_data, x="season", y="cnt", text_auto=True, color="cnt", labels={"season": "Musim", "cnt": "Jumlah Pengguna Sepeda"}, color_continuous_scale="blues")
fig.update_xaxes(tickmode="array", tickvals=[1, 2, 3, 4], ticktext=list(season_labels.values()))
st.plotly_chart(fig)

# Pengguna Sepeda Berdasarkan Hari Kerja vs Akhir Pekan
st.subheader("📆 Pola Penggunaan Sepeda Berdasarkan Hari Kerja & Akhir Pekan")
workingday_data = filtered_df.groupby("workingday")["cnt"].mean().reset_index()
workingday_labels = {0: "Akhir Pekan", 1: "Hari Kerja"}
fig = px.bar(workingday_data, x="workingday", y="cnt", text_auto=True, color="workingday", labels={"workingday": "Kategori Hari", "cnt": "Jumlah Pengguna Sepeda"}, color_continuous_scale="blues")
fig.update_xaxes(tickmode="array", tickvals=[0, 1], ticktext=list(workingday_labels.values()))
st.plotly_chart(fig)


# Perbandingan Hari Kerja vs Akhir Pekan dalam Penggunaan Sepeda
st.subheader("📊 Perbandingan Pola Penggunaan Sepeda Pada Hari Kerja & Akhir Pekan")
workingday_hour_data = filtered_df.groupby(["hr", "workingday"])["cnt"].mean().reset_index()
workingday_labels = {0: "Akhir Pekan", 1: "Hari Kerja"}  
fig = px.line(
    workingday_hour_data, 
    x="hr", 
    y="cnt", 
    color="workingday", 
    labels={"hr": "Jam", "cnt": "Jumlah Pengguna Sepeda", "workingday": "Kategori Hari"},
    color_discrete_map={0: "red", 1: "blue"},
    category_orders={"workingday": [0, 1]} 
)
fig.for_each_trace(lambda t: t.update(name=workingday_labels[int(t.name)]))  
st.plotly_chart(fig)


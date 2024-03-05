import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

sns.set(style='dark')

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
st.set_option('deprecation.showPyplotGlobalUse', False)

all_df = pd.read_csv("all_df.csv")

st.title("Brazilian E-commerce Data Dashboard")

st.subheader("The Dataset")
st.dataframe(data=all_df, width=500, height=150)

st.subheader("Pertanyaan 1: Wilayah geografis mana yang paling banyak ditempati customer ?")
# Your existing code
state_customer_counts = all_df.groupby(by="customer_state")["customer_id"].nunique().sort_values(ascending=False)
# Plot the bar chart
plt.figure(figsize=(12, 6))
sns.barplot(x=state_customer_counts.index, y=state_customer_counts.values, palette="viridis")
plt.xlabel("Customer State")
plt.ylabel("Number of Unique Customers")
plt.xticks(rotation=45, ha="right")

# Display the plot using Streamlit
st.pyplot()

# Group by customer_city and count unique customer_ids
city_customer_counts = all_df.groupby(by="customer_city")["customer_id"].nunique().sort_values(ascending=False)
top_10_cities = city_customer_counts.head(10)
# Plot the bar chart
plt.figure(figsize=(12, 6))
sns.barplot(x=top_10_cities.index, y=top_10_cities.values, palette="viridis")
plt.xlabel("Customer City")
plt.ylabel("Number of Unique Customers")
plt.xticks(rotation=45, ha="right")

# Display the plot using Streamlit
st.pyplot()




st.subheader("Pertanyaan 2: Wilayah geografis mana yang memiliki jumlah order terbanyak ?")
state_order_counts = all_df.groupby(by="customer_state")["order_id"].nunique().sort_values(ascending=False)
# Plot the bar chart
plt.figure(figsize=(12, 6))
sns.barplot(x=state_order_counts.index, y=state_order_counts.values, palette="viridis")
plt.title("Number of Unique Orders by State")
plt.xlabel("Customer State")
plt.ylabel("Number of Unique Orders")
plt.xticks(rotation=45, ha="right")
# Display the plot in Streamlit
st.pyplot()


# Your existing code
state_order_counts = all_df.groupby(by="customer_state")["order_id"].nunique().sort_values(ascending=False)

# Plot the bar chart
plt.figure(figsize=(12, 6))
sns.barplot(x=state_order_counts.index, y=state_order_counts.values, palette="viridis")
plt.title("Number of Unique Orders by State")
plt.xlabel("Customer State")
plt.ylabel("Number of Unique Orders")
plt.xticks(rotation=45, ha="right")

# Display the plot using Streamlit
st.pyplot()

st.write("""dari pertanyaan 1 dan 2 kita dapat 
         melihat adanya korelasi antara banyaknya 
         customer di suatu wilayah dengan jumlah 
         order di wilayah tersebut.""")


st.subheader("Pertanyaan 3: Produk apa yang memiliki penjualan tertinggi ?")
category_summary = all_df.groupby(by="Product_Category").agg({
    "order_id": "nunique",
    "order_item_id": "sum",
    "price": "sum"
}).sort_values(by="price", ascending=False)

# Plot the bar chart
plt.figure(figsize=(14, 6))
sns.barplot(x=category_summary.index, y=category_summary["price"], palette="viridis")
plt.title("Total Order Items by Product Category (Sorted)")
plt.xlabel("Product Category")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45, ha="right")

# Display the plot using Streamlit
st.pyplot()

category_summary = all_df.groupby(by="Product_Category").agg({
    "order_id": "nunique",
    "order_item_id": "sum",
    "price": "sum"
}).sort_values(by="price", ascending=False)

# Plot the bar chart
plt.figure(figsize=(14, 6))
sns.barplot(x=category_summary.index, y=category_summary["price"], palette="viridis")
plt.title("Total Revenue by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45, ha="right")

# Display the plot using Streamlit
st.pyplot()


st.write("""
kesimpulanya walaupun suatu produk memiliki jumlah order yang paling banyak belum tentu dia yang menghasilkan keuntungan yang paling tinggi. 
dan jika kita ingin memasuki e-commerce kita bisa berjualan dengan product kategori yang memiliki jumlah order dan menghasilkan keuntungan yang paling tinggi.
""")

st.subheader("Pertanyaan 4: Seberapa besar kemungkinan suatu order sukses ?")
# Group by order_status and count unique order_ids
order_status_counts = all_df.groupby(by="order_status")["order_id"].nunique()
total_orders = order_status_counts.sum()
percentage_values = (order_status_counts / total_orders) * 100

# Plot the bar chart with percentages
plt.figure(figsize=(10, 6))
ax = sns.barplot(x=order_status_counts.index, y=order_status_counts.values, palette="viridis", hue=order_status_counts.index, dodge=False)

for p, percentage in zip(ax.patches, percentage_values):
    height = p.get_height()
    width = p.get_width()
    x, y = p.get_xy() 

    # Check if height is valid
    if height > 0:
        ax.annotate(f'{height} ({percentage:.1f}%)', (x + width / 2., height),
                    ha='center', va='center', xytext=(0, 10), textcoords='offset points')

# Remove the legend
ax.legend().set_visible(False)

plt.xlabel("Order Status")
plt.ylabel("Number of Unique Orders")
plt.xticks(rotation=45, ha="right")

# Display the plot using Streamlit
st.pyplot()

st.write("""
    Pada dataset brazilian e-commerce dari tahun 2016 hingga 2018 ini, menunjukan bahwa 97% orders sukses sampi ketangan pembeli, 1.1 persen sedang dalam proses pengiriman, 0.6%\ orders di cancel dan unvailable, 0.3% sedang di tahap invoiced dan proses administrasi, dan 0.01% sisanya ada pada tahap create & approved.
bisa kita simpulkan bahwa kemungkinan orders sukses hingga sampai ketangan pembeli sangat besar yaitu 97%, dan kemungkinan order di cancel itu sangat kecil 0.6%. dan sisanya sedang dalam proses.
""")

st.caption('Faishal Syams Afif Copyright (c) 2023')

text = st.text_area('Feedback')
st.write('Feedback: ', text)

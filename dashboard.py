sns.set(style='dark')

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

all_df = pd.read_csv("all_df.csv")
st.title("Brazilian E-commerce Data Dashboard")

st.subheader("The Dataset")
st.dataframe(data=all_df, width=500, height=150)

st.subheader("Wilayah geografis yang paling banyak ditempati customer")
state_customer_counts = all_df.groupby(by="customer_state")["customer_id"].nunique().sort_values(ascending=False)
# Plot the bar chart
plt.figure(figsize=(12, 6))
sns.barplot(x=state_customer_counts.index, y=state_customer_counts.values, palette="viridis")
plt.title("Number of Unique Customers by State")
plt.xlabel("Customer State")
plt.ylabel("Number of Unique Customers")
plt.xticks(rotation=45, ha="right")

# Display the plot in Streamlit
st.pyplot()

st.caption('Faishal Syams Afif Copyright (c) 2023')

text = st.text_area('Feedback')
st.write('Feedback: ', text)

import streamlit as st
import pandas as pd
import plotly.express as px


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Diwali Sales Dashboard",
    layout="wide"
)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("Diwali Sales & Customer Insights")

st.write(
    "An interactive dashboard for exploring customer behavior, "
    "sales performance, geographic markets, and product trends."
)


# --------------------------------------------------
# LOAD DATASET
# --------------------------------------------------

df = pd.read_csv(
    "Diwali Sales Data.csv",
    encoding="latin1"
)


# --------------------------------------------------
# SIDEBAR FILTERS
# --------------------------------------------------

st.sidebar.header("Dashboard Filters")


# Gender
gender_options = ["All"] + sorted(
    df["Gender"].dropna().unique().tolist()
)

selected_gender = st.sidebar.selectbox(
    "Gender",
    gender_options
)


# Age Group
age_options = ["All"] + sorted(
    df["Age Group"].dropna().unique().tolist()
)

selected_age = st.sidebar.selectbox(
    "Age Group",
    age_options
)


# State
state_options = ["All"] + sorted(
    df["State"].dropna().unique().tolist()
)

selected_state = st.sidebar.selectbox(
    "State",
    state_options
)


# Marital Status
marital_options = ["All"] + sorted(
    df["Marital_Status"].dropna().unique().tolist()
)

selected_marital = st.sidebar.selectbox(
    "Marital Status",
    marital_options
)


# Occupation
occupation_options = ["All"] + sorted(
    df["Occupation"].dropna().unique().tolist()
)

selected_occupation = st.sidebar.selectbox(
    "Occupation",
    occupation_options
)


# Product Category
category_options = ["All"] + sorted(
    df["Product_Category"].dropna().unique().tolist()
)

selected_category = st.sidebar.selectbox(
    "Product Category",
    category_options
)


# --------------------------------------------------
# APPLY FILTERS
# --------------------------------------------------

filtered_df = df.copy()


if selected_gender != "All":
    filtered_df = filtered_df[
        filtered_df["Gender"] == selected_gender
    ]


if selected_age != "All":
    filtered_df = filtered_df[
        filtered_df["Age Group"] == selected_age
    ]


if selected_state != "All":
    filtered_df = filtered_df[
        filtered_df["State"] == selected_state
    ]


if selected_marital != "All":
    filtered_df = filtered_df[
        filtered_df["Marital_Status"] == selected_marital
    ]


if selected_occupation != "All":
    filtered_df = filtered_df[
        filtered_df["Occupation"] == selected_occupation
    ]


if selected_category != "All":
    filtered_df = filtered_df[
        filtered_df["Product_Category"] == selected_category
    ]


# --------------------------------------------------
# OVERALL SALES PERFORMANCE
# --------------------------------------------------

st.header("Overall Sales Performance")

total_sales = filtered_df["Amount"].sum()
total_orders = filtered_df["Orders"].sum()
unique_customers = filtered_df["User_ID"].nunique()
unique_products = filtered_df["Product_ID"].nunique()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Sales",
    f"₹{total_sales:,.0f}"
)

col2.metric(
    "Total Orders",
    f"{total_orders:,}"
)

col3.metric(
    "Customers",
    f"{unique_customers:,}"
)

col4.metric(
    "Products",
    f"{unique_products:,}"
)


st.divider()


# --------------------------------------------------
# CUSTOMER ANALYSIS
# --------------------------------------------------

st.header("Customer Analysis")


# Gender

st.subheader("Sales by Gender")

gender_sales = (
    filtered_df
    .groupby("Gender")["Amount"]
    .sum()
    .reset_index()
    .sort_values("Amount", ascending=False)
)

fig_gender = px.bar(
    gender_sales,
    x="Gender",
    y="Amount",
    title="Total Sales by Gender",
    labels={
        "Gender": "Gender",
        "Amount": "Total Sales"
    }
)

st.plotly_chart(
    fig_gender,
    use_container_width=True
)


# Age Group

st.subheader("Sales by Age Group")

age_sales = (
    filtered_df
    .groupby("Age Group")["Amount"]
    .sum()
    .reset_index()
    .sort_values("Amount", ascending=False)
)

fig_age = px.bar(
    age_sales,
    x="Age Group",
    y="Amount",
    title="Total Sales by Age Group",
    labels={
        "Age Group": "Age Group",
        "Amount": "Total Sales"
    }
)

st.plotly_chart(
    fig_age,
    use_container_width=True
)


# Marital Status

st.subheader("Sales by Marital Status")

marital_sales = (
    filtered_df
    .groupby("Marital_Status")["Amount"]
    .sum()
    .reset_index()
)

fig_marital = px.bar(
    marital_sales,
    x="Marital_Status",
    y="Amount",
    title="Total Sales by Marital Status",
    labels={
        "Marital_Status": "Marital Status",
        "Amount": "Total Sales"
    }
)

st.plotly_chart(
    fig_marital,
    use_container_width=True
)


# Occupation

st.subheader("Top 10 Occupations by Sales")

occupation_sales = (
    filtered_df
    .groupby("Occupation")["Amount"]
    .sum()
    .reset_index()
    .sort_values("Amount", ascending=False)
    .head(10)
)

fig_occupation = px.bar(
    occupation_sales.sort_values("Amount"),
    x="Amount",
    y="Occupation",
    orientation="h",
    title="Top 10 Occupations by Sales",
    labels={
        "Amount": "Total Sales",
        "Occupation": "Occupation"
    }
)

st.plotly_chart(
    fig_occupation,
    use_container_width=True
)


st.divider()


# --------------------------------------------------
# GEOGRAPHIC ANALYSIS
# --------------------------------------------------

st.header("Geographic Analysis")

st.subheader("Top 10 States by Sales")

state_sales = (
    filtered_df
    .groupby("State")["Amount"]
    .sum()
    .reset_index()
    .sort_values("Amount", ascending=False)
    .head(10)
)

fig_state = px.bar(
    state_sales.sort_values("Amount"),
    x="Amount",
    y="State",
    orientation="h",
    title="Top 10 States by Sales",
    labels={
        "Amount": "Total Sales",
        "State": "State"
    }
)

st.plotly_chart(
    fig_state,
    use_container_width=True
)


st.divider()


# --------------------------------------------------
# PRODUCT ANALYSIS
# --------------------------------------------------

st.header("Product Analysis")


# Product Category

st.subheader("Sales by Product Category")

category_sales = (
    filtered_df
    .groupby("Product_Category")["Amount"]
    .sum()
    .reset_index()
    .sort_values("Amount", ascending=False)
)

fig_category = px.bar(
    category_sales,
    x="Product_Category",
    y="Amount",
    title="Total Sales by Product Category",
    labels={
        "Product_Category": "Product Category",
        "Amount": "Total Sales"
    }
)

st.plotly_chart(
    fig_category,
    use_container_width=True
)


# Products

st.subheader("Top 10 Products by Sales")

product_sales = (
    filtered_df
    .groupby("Product_ID")["Amount"]
    .sum()
    .reset_index()
    .sort_values("Amount", ascending=False)
    .head(10)
)

fig_product = px.bar(
    product_sales.sort_values("Amount"),
    x="Amount",
    y="Product_ID",
    orientation="h",
    title="Top 10 Products by Sales",
    labels={
        "Amount": "Total Sales",
        "Product_ID": "Product"
    }
)

st.plotly_chart(
    fig_product,
    use_container_width=True
)


st.divider()


# --------------------------------------------------
# DATASET PREVIEW
# --------------------------------------------------

st.header("Dataset Preview")

st.dataframe(
    filtered_df.head(20),
    use_container_width=True
)

# --------------------------------------------------
# BUSINESS INSIGHTS
# --------------------------------------------------

st.header("Business Insights")

st.write(
    "The dashboard provides insights into customer behavior, "
    "geographic performance, and product demand based on the selected filters."
)

# Highest-selling gender
if not gender_sales.empty:
    top_gender = gender_sales.iloc[0]["Gender"]
    st.write(
        f"Highest sales by gender: {top_gender}"
    )

# Highest-selling age group
if not age_sales.empty:
    top_age = age_sales.iloc[0]["Age Group"]
    st.write(
        f"Highest sales by age group: {top_age}"
    )

# Highest-selling state
if not state_sales.empty:
    top_state = state_sales.iloc[0]["State"]
    st.write(
        f"Highest sales among the displayed states: {top_state}"
    )

# Highest-selling occupation
if not occupation_sales.empty:
    top_occupation = occupation_sales.iloc[-1]["Occupation"]
    st.write(
        f"Highest sales among the displayed occupations: {top_occupation}"
    )

# Highest-selling product category
if not category_sales.empty:
    top_category = category_sales.iloc[0]["Product_Category"]
    st.write(
        f"Highest sales by product category: {top_category}"
    )

# Highest-selling product
if not product_sales.empty:
    top_product = product_sales.iloc[-1]["Product_ID"]
    st.write(
        f"Highest-selling product among the displayed products: {top_product}"
    )

    # --------------------------------------------------
# DOWNLOAD FILTERED DATA
# --------------------------------------------------

st.header("Download Filtered Data")

csv_data = filtered_df.to_csv(index=False)

st.download_button(
    label="Download Filtered Dataset",
    data=csv_data,
    file_name="filtered_diwali_sales.csv",
    mime="text/csv"
)
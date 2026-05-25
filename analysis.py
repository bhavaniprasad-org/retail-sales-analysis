import pandas as pd
import plotly.express as px


def generate_charts(file_path):

    df = pd.read_csv(file_path, encoding="latin1")

    # Chart 1 — Sales by Category
    sales_by_category = df.groupby("Category")["Sales"].sum().reset_index()

    fig1 = px.bar(
        sales_by_category,
        x="Category",
        y="Sales",
        title="Sales by Category"
    )

    category_chart = fig1.to_html(full_html=False)

    # Chart 2 — Profit by Region
    profit_by_region = df.groupby("Region")["Profit"].sum().reset_index()

    fig2 = px.bar(
        profit_by_region,
        x="Region",
        y="Profit",
        title="Profit by Region"
    )

    profit_chart = fig2.to_html(full_html=False)

    # Chart 3 — Sales by Segment
    segment_sales = df.groupby("Segment")["Sales"].sum().reset_index()

    fig3 = px.pie(
        segment_sales,
        names="Segment",
        values="Sales",
        title="Sales by Segment"
    )

    segment_chart = fig3.to_html(full_html=False)

    return category_chart, profit_chart, segment_chart
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
athletes = pd.read_csv("data/athlete_events.csv")
regions = pd.read_csv("data/noc_regions.csv")

# Data preprocessing
def data_preprocessor():
    global athletes, regions
    df = pd.merge(athletes, regions, on="NOC")
    df.drop_duplicates(inplace=True)
    df["Medal"].fillna("No_Medal", inplace=True)
    summer = df[df["Season"] == "Summer"]
    winter = df[df["Season"] == "Winter"]
    return summer, winter

# Remove duplicate rows
def duplicate_rows_remover(df1, df2):
    df1 = df1.drop_duplicates(subset=["Team", "NOC", "Games", "Year", "City", "Sport", "Event"])
    df2 = df2.drop_duplicates(subset=["Team", "NOC", "Games", "Year", "City", "Sport", "Event"])
    return df1, df2

# Calculate medal tally
def medal_tally_calculator(df):
    medal_counts = df.groupby(["NOC", "Medal"]).size().reset_index(name="count")
    medal_pivot = medal_counts.pivot(index="NOC", columns="Medal", values="count").fillna(0).astype(int)
    if "No_Medal" in medal_pivot.columns:
        medal_pivot.drop(columns="No_Medal", inplace=True)
    medal_pivot["Total_medal"] = medal_pivot[["Gold", "Silver", "Bronze"]].sum(axis=1)
    return medal_pivot

# Country-wise medal search
def country_wise_search(noc, pivot_table):
    if noc in pivot_table.index:
        details = {
            "Gold": pivot_table.loc[noc, "Gold"],
            "Silver": pivot_table.loc[noc, "Silver"],
            "Bronze": pivot_table.loc[noc, "Bronze"],
            "Total Medal": pivot_table.loc[noc, "Total_medal"]
        }
        return details
    else:
        st.write("No NOC exists")

# Plot medals for a given year and country
def plot_medals(year, country, df):
    medals_count = df.groupby(["Year", "region", "Medal"]).size().unstack(fill_value=0).reset_index()
    medals_count["Total_Medal"] = medals_count["Gold"] + medals_count["Silver"] + medals_count["Bronze"]
    filtered_df = medals_count[(medals_count["Year"] == year) & (medals_count["region"] == country)]
    if not filtered_df.empty:
        gold = filtered_df["Gold"].values[0]
        silver = filtered_df["Silver"].values[0]
        bronze = filtered_df["Bronze"].values[0]
        total_medal = filtered_df["Total_Medal"].values[0]
        fig, ax = plt.subplots()
        medals = ["Gold", "Silver", "Bronze", "Total_Medals"]
        counts = [gold, silver, bronze, total_medal]
        ax.bar(medals, counts, color=["gold", "silver", "brown", "green"])
        st.pyplot(fig)
    else:
        st.write(f"No data available for {country} in {year}")

# Analyze medals over the years for a given country
def year_analysis(country, df):
    medals_count = df.groupby(["Year", "region", "Medal"]).size().unstack(fill_value=0).reset_index()
    medals_count["Total_Medal"] = medals_count["Gold"] + medals_count["Silver"] + medals_count["Bronze"]
    filtered_df = medals_count[medals_count["region"] == country]
    fig, ax = plt.subplots()
    ax.plot(filtered_df["Year"], filtered_df["Gold"], color="gold", label="GOLD", marker="o", linestyle="-")
    ax.plot(filtered_df["Year"], filtered_df["Silver"], color="silver", label="SILVER", marker="o", linestyle="-")
    ax.plot(filtered_df["Year"], filtered_df["Bronze"], color="brown", label="BRONZE", marker="o", linestyle="-")
    ax.plot(filtered_df["Year"], filtered_df["Total_Medal"], color="green", label="TOTAL MEDALS", marker="o", linestyle="-")
    ax.legend()
    st.pyplot(fig)

# Streamlit UI
st.title("Olympics Data Analysis")

# Preprocess data
summer, winter = data_preprocessor()

# Display options
season = st.selectbox("Select Season", ["Summer", "Winter"])
df = summer if season == "Summer" else winter

# Display medal tally
st.header("Medal Tally")
noc = st.text_input("Enter NOC (e.g., USA, CHN, IND):").upper()
pivot_table = medal_tally_calculator(df)
if noc:
    details = country_wise_search(noc, pivot_table)
    if details:
        st.write(details)

# Display medals plot for selected year and country
st.header("Medals Plot")
year = st.slider("Select Year", int(df["Year"].min()), int(df["Year"].max()))
country = st.text_input("Enter Country for Medal Plot (e.g., USA, China):")
if country:
    plot_medals(year, country, df)

# Display medals trend over the years for a selected country
st.header("Medals Trend Over Years")
country_trend = st.text_input("Enter Country for Year Analysis (e.g., USA, China):")
if country_trend:
    year_analysis(country_trend, df)

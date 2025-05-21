# unemployment_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

def main():
    # Load the dataset
    df = pd.read_csv("Unemployment_in_India.csv")
    df.columns = df.columns.str.strip()


    # Convert 'Date' to datetime and extract year and month
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month

    # Rename columns for easier access
    df.rename(columns={
        'Region': 'State',
        'Estimated Unemployment Rate (%)': 'Unemployment Rate',
        'Estimated Employed': 'Employed',
        'Estimated Labour Participation Rate (%)': 'Labour Participation Rate'
    }, inplace=True)

    # Print basic info
    print("Data Summary:")
    print(df.head())
    print(df.info())
    print("Missing values:\n", df.isnull().sum())

    # Overall unemployment trend by year
    yearly_unemployment = df.groupby('Year')['Unemployment Rate'].mean().reset_index()
    sns.lineplot(x='Year', y='Unemployment Rate', data=yearly_unemployment, marker='o')
    plt.title('Average Unemployment Rate in India (Yearly)')
    plt.xlabel('Year')
    plt.ylabel('Unemployment Rate (%)')
    plt.savefig('yearly_unemployment_trend.png')
    plt.show()

    # Top 5 states with highest average unemployment
    top_states = df.groupby('State')['Unemployment Rate'].mean().sort_values(ascending=False).head(5)
    print("Top 5 states with highest average unemployment rate:")
    print(top_states)

    # Plot trends for those top states
    plt.figure()
    for state in top_states.index:
        state_df = df[df['State'] == state]
        sns.lineplot(x='Date', y='Unemployment Rate', data=state_df, label=state)
    plt.title('Unemployment Rate Trends for Top 5 States')
    plt.xlabel('Date')
    plt.ylabel('Unemployment Rate (%)')
    plt.legend()
    plt.savefig('top_states_trend.png')
    plt.show()

    # Heatmap of unemployment rate by state and year
    heatmap_data = df.groupby(['State', 'Year'])['Unemployment Rate'].mean().unstack()
    plt.figure(figsize=(14, 10))
    sns.heatmap(heatmap_data, annot=True, fmt=".1f", cmap="coolwarm")
    plt.title('Heatmap of Unemployment Rate by State and Year')
    plt.savefig('state_year_heatmap.png')
    plt.show()

    # Save cleaned data
    df.to_csv("cleaned_unemployment_india.csv", index=False)

    print("Analysis complete. Plots saved to current folder.")

if __name__ == "__main__":
    main()

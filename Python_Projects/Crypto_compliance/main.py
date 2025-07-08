import pandas as pd
import matplotlib.pyplot as plt
import json

def load_data(path):
    """Load the token data from a CSV file"""
    return pd.read_csv(path)

def detect_price_volatility(df, threshold=0.05):
    """Detects price volatility using rolling standard deviation"""
    df['return'] = df['price'].pct_change()
    df['volatility'] = df['return'].rolling(7).std()
    df['price_flag'] = df['volatility'] > threshold
    return df

def detect_volume_spikes(df, multiplier=2.0):
    """Detects unusual spikes in trade volume"""
    df['avg_volume'] = df['volume'].rolling(5).mean()
    df['volume_flag'] = df['volume'] > (df['avg_volume'] * multiplier)
    return df

def assign_risk_level(df):
    """Assigns a compliance risk level based on price and volume alerts"""
    df['risk_score'] = df[['price_flag', 'volume_flag']].sum(axis=1)
    df['risk_level'] = df['risk_score'].apply(
        lambda x: "High" if x == 2 else "Moderate" if x == 1 else "Low"
    )
    return df

def export_to_json(df, filename="compliance_report.json"):
    """Exports flagged dates and risk levels to a JSON file"""
    flagged = df[df['risk_level'] != "Low"]
    report = flagged[['date', 'price', 'volume', 'risk_level']].to_dict(orient='records')
    with open(filename, 'w') as f:
        json.dump(report, f, indent=4)
    print(f"\n Compliance report saved to {filename}")

def plot_price_and_volume(df):
    """Plots both price and volume over time"""
    fig, ax1 = plt.subplots()

    ax1.set_xlabel('Date')
    ax1.set_ylabel('Price', color='tab:blue')
    ax1.plot(df['date'], df['price'], color='tab:blue', marker='o', label='Price')
    ax1.tick_params(axis='y', labelcolor='tab:blue')
    plt.xticks(rotation=45)

    ax2 = ax1.twinx()
    ax2.set_ylabel('Volume', color='tab:red')
    ax2.plot(df['date'], df['volume'], color='tab:red', marker='x', linestyle='--', label='Volume')
    ax2.tick_params(axis='y', labelcolor='tab:red')

    fig.tight_layout()
    plt.title("Token Price and Volume Trend")
    plt.grid()
    plt.show()

def main():
    # Load data
    df = load_data(r"C:\Users\HP\source\repos\Python_Practice\Python_Projects\Crypto_compliance\sample_token_data.csv")

    # Run analyses
    df = detect_price_volatility(df)
    df = detect_volume_spikes(df)
    df = assign_risk_level(df)

    # Show alerts
    print("\n Risk Alerts:")
    for _, row in df.iterrows():
        if row['risk_level'] != "Low":
            print(f"{row['date']} - Risk Level: {row['risk_level']}")

    # Export to JSON
    export_to_json(df)

    # Plot
    plot_price_and_volume(df)

if __name__ == "__main__":
    main()

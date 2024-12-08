from scipy.stats import zscore

def handle_missing_values(df):
    df['GHI'] = df['GHI'].fillna(df['GHI'].mean())
    df.dropna(subset=['Timestamp'], inplace=True)
    return df

def detect_outliers(df):
    z_scores = zscore(df[['GHI', 'DNI', 'DHI']])
    df['outlier'] = (abs(z_scores) > 3).any(axis=1)
    return df




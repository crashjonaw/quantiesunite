MINDMAP = {
    "concepts": [
        {"title": "Series & DataFrame", "points": [
            "Series: 1D labelled array (like a column)",
            "DataFrame: 2D table with rows and columns",
            "Create: pd.DataFrame({'col1': [...], 'col2': [...]})",
        ]},
        {"title": "Reading & Writing Data", "points": [
            "pd.read_csv('file.csv'), df.to_csv('out.csv')",
            "pd.read_excel(), pd.read_json(), pd.read_sql()",
            "df.head(), df.info(), df.describe() for quick inspection",
        ]},
        {"title": "Selection & Filtering", "points": [
            "Column: df['col'] or df.col",
            "Row by label: df.loc[label], by index: df.iloc[pos]",
            "Boolean filter: df[df['age'] > 30]",
        ]},
        {"title": "Aggregation & Grouping", "points": [
            "df.groupby('col').mean() — split-apply-combine",
            "Aggregations: .sum(), .count(), .min(), .max(), .agg()",
            "Pivot tables: pd.pivot_table(df, values, index, columns)",
        ]},
        {"title": "Data Cleaning", "points": [
            "Missing values: .isna(), .fillna(), .dropna()",
            "Duplicates: .duplicated(), .drop_duplicates()",
            "Type conversion: .astype(), pd.to_datetime()",
        ]},
    ],
    "formulas": [],
    "tips": [
        "Always inspect data first: df.shape, df.dtypes, df.describe()",
        "Use .loc for label-based indexing, .iloc for integer-position indexing",
        "Chain operations with method chaining: df.query(...).groupby(...).agg(...)",
    ],
}

import pandas as pd

def get_dataframe():
    urls = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSSFEzwj9erdFwLIxBSLhvBTffcJHX8xpmaebnwqWYkij3DywsUOTZmFvs4QZgOazMi--z9JCFLS_Qt/pub?output=csv"
    df = pd.read_csv(urls)
    return df

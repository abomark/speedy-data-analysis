import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')


class Gather:
    '''
    Responsibility: Automation of gathering data
    '''

    def __init__(self):
        pass

    def gather(self, path):
        return pd.read_csv(path)

    def organize():
        '''
        responsible for returning path format
        '''
        pass

    # todo: one function for each import format


class Assess:
    '''
    Responsibility: Making sure that cleaning and analysis later on is easier
    '''

    def __init__(self):
        pass

    def print_columns(self, df):
        for column in df.columns:
            print(column)

    def print_random_rows(self, df):
        print(df.sample(n=10))

    def print_shape(self, df):
        print(df.shape)

    def print_describe(self, df):
        print(df.describe())

    def understand_data(self, df):
        print("Columns in the dataset are:\n")
        df.print_columns()

        print("\nThe shape is:\n")
        df.print_shape()

        print("\nSummary of numeric variables:\n")
        df.print_describe()

    ''' QUALITY ISSUES '''

    # Completeness
    def check_missing(self, df):
        print("Are there any missing rows?:\n")

        print("\nAre there any missing columns? (subjective inspection):\n")
        for column in df.columns:
            print(column)

        print("\nAre there any missing values?:\n")
        print(df.isna().sum())

        # plot missing rows
        na_counts = df.isna().sum()
        base_color = sns.color_palette()[0]
        sns.barplot(na_counts.index.values, na_counts, color=base_color)

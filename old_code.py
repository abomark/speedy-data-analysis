import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')


class Analyse:
    def __init__(self, name, data):
        self.data = data
        self.df = pd.read_csv(self.data)

        self.datasets = {name: pd.read_csv(self.data)}

    ''' Understanding the data '''

    def print_columns(self):
        for column in self.df.columns:
            print(column)

    def print_shape(self):
        print(self.df.shape)

    def print_describe(self):
        print(self.df.describe())

    def understand_data(self):
        print("Columns in the dataset are:\n")
        self.print_columns()

        print("\nThe shape is:\n")
        self.print_shape()

        print("\nSummary of numeric variables:\n")
        self.print_describe()

    ''' TODO '''

    def plot_hist(self, arr1, arr2, label1, label2):
        plt.hist(arr1, color='r', alpha=0.5, label=label1)
        plt.hist(arr2, color='b', alpha=0.5, label=label2)
        plt.legend()
        plt.show()

    def plot_hist_uni(self, arr1, label):
        plt.hist(arr1, color='r', alpha=0.5, label=label)
        plt.legend()
        plt.show()


class Wrangle(Analyse):
    def __init__(self, name, data):
        Analyse.__init__(self, name, data)
        # self.staffnumber = staffnum

    def print_columns(self):
        for column in self.df.columns:
            print(column)

    ''' QUALITY PROBLEMS'''

    def plot_missing(self):
        na_counts = self.df.isna().sum()
        base_color = sns.color_palette()[0]
        sns.barplot(na_counts.index.values, na_counts, color=base_color)

    def print_missing(self):
        print(self.df.isna().sum())

    def drop_missing(self):
        self.df.dropna(inplace=True)

    def print_duplicates(self):
        print(self.df[self.df.duplicated()])

    def drop_duplicates(self):
        self.df = self.df.drop_duplicates()

    def subset_columns(self, columns):
        self.df = self.df[columns]

    '''TIDY PROBLEMS'''


class Explore():
    pass

    # TODO: df groupby('sex').Survival.mean().plot(kind='bar');


if __name__ == '__main__':
    # a = Analyse('tmdb-movies.csv')
    # a.print_columns()

    w = Wrangle(name='tmdb', data='tmdb-movies.csv')
    # print(w.df.head())

    print(w.datasets['tmdb'].head())

'''
    w.subset_columns(['popularity', 'runtime', 'budget', 'director'])
    w.understand_data()

    # Handle missing
    w.print_missing()
    w.drop_missing()
    w.print_missing()

    # Handle duplicates
    w.print_duplicates()
    w.drop_duplicates()
    w.print_duplicates()
'''

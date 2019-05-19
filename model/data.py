class Container:
    '''
    Responsibility: Container for data sets
    '''

    def __init__(self):
        self.datasets = []

    def print_datasets(self):
        print(self.datasets)

        #self.df = pd.read_csv(self.data)
        #self.datasets = {name: pd.read_csv(self.data)}

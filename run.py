from controller.wrangle import Gather
from controller.wrangle import Assess
from model.data import Container


def main():
    # Instansiate
    c = Container()
    g = Gather()
    a = Assess()

    # Gather
    df = g.gather("data/tmdb-movies.csv")
    c.datasets.append(df)

    # Assess
    a.print_columns(c.datasets[0])
    a.print_shape(c.datasets[0])
    a.print_describe(c.datasets[0])

    # Check values
    a.print_random_rows(c.datasets[0])

    # Quality issues
    #   Missing
    a.check_missing(c.datasets[0])


    # print(gathered)
    # print(sets)
    # print(sets.print_datasets)
    # c.print_datasets()
    # a.print_columns(sets.)
if __name__ == '__main__':
    main()

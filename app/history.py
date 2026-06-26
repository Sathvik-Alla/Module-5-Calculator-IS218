import pandas as pd


class History:
    def __init__(self):
        self.df = pd.DataFrame(columns=["operation", "a", "b", "result"])

    def add(self, calculation):
        self.df.loc[len(self.df)] = [
            calculation.operation,
            calculation.a,
            calculation.b,
            calculation.result,
        ]

    def save(self, filename="history.csv"):
        self.df.to_csv(filename, index=False)

    def load(self, filename="history.csv"):
        try:
            self.df = pd.read_csv(filename)
        except FileNotFoundError:
            self.df = pd.DataFrame(columns=["operation", "a", "b", "result"])

    def clear(self):
        self.df = self.df.iloc[0:0]

    def show(self):
        return self.df
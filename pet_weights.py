#!/usr/bin/env python

from datetime import date
from pathlib import Path

import fire
import hvplot
import hvplot.pandas
import numpy as np
import pandas as pd
import toml

confpath = Path.home() / ".pet_weights_conf.toml"
if confpath.exists():
    conf = toml.load(confpath)
else:
    print(f"No config file found. Created {confpath}")
    conf = {}
    with confpath.open("w") as f:
        toml.dump(conf, f)


class PetWeights:
    @property
    def datapath(self):
        return Path(conf["datapath"])

    def setup(self):
        path = Path(input("Path to existing records: ")).expanduser()
        if not path.exists():
            print("That path does not exist. Exiting...")
        else:
            conf["datapath"] = str(path)
            with confpath.open("w") as f:
                toml.dump(conf, f)

    def list_records(self, name: str = None):
        """List records in your database.
        
        Parameters
        ----------
        name : str, optional
            Name of the Pet. Data will be filtered for this name.

        Returns
        -------
        prints out the data to the console

        """
        df = pd.read_csv(self.datapath)
        if name is not None:
            df = df[df.Pet == name]
        print(df)

    def add_record(self, name):
        today = date.today()
        both = float(input("Both weights: "))
        mine = float(input("Your weight: "))
        weight = both - mine
        print("Measured weight:", weight)

        df = pd.read_csv(self.datapath)
        d = {"date": today.isoformat(), "weight [kg]": weight, "Pet": name}
        df = df.append(d, ignore_index=True)
        df.to_csv(self.datapath, index=False)

    def plot(self, name: str = None):
        df = pd.read_csv(self.datapath, parse_dates=['date']).set_index('date')
        if name is not None:
            df = df[df.Pet == name]
            p = df.hvplot(x='date', y='weight [kg]', kind='line')
        else:
            p = df.hvplot(x='date', y='weight [kg]', by='Pet')
        hvplot.show(p.opts(show_grid=True))

def main():
    fire.Fire(PetWeights)


if __name__ == "__main__":
    fire.Fire(PetWeights)

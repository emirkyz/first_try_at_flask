from flask import Flask
import random


def futbol():
    formalar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    oyuncular = dict(
        o1="1",
        o2="2",
        o3="3",
        o4="4",
        o5="5",
        o6="6",
        o7="7",
        o8="8",
        o9="9",
        o10="10",
        o11="11",
    )

    # 1.ci rasgele, diğerler varsa alsın yoksa rasgele

    iyi_sonuc = 0
    kotu_sonuc = 0
    for _ in range(200):
        formalar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        oyuncular = dict(
            o1="1",
            o2="2",
            o3="3",
            o4="4",
            o5="5",
            o6="6",
            o7="7",
            o8="8",
            o9="9",
            o10="10",
            o11="11",
        )
        for i in range(1, len(formalar)):
            if i == 1:
                choice = random.randint(1, 11)
                if choice == int(oyuncular[f"o{i}"]):
                    iyi_sonuc += 1
                else:
                    formalar.remove(choice)
                    oyuncular.pop(f"o{i}")
            else:
                if int(oyuncular[f"o{i}"]) in formalar:
                    formalar.remove(int(oyuncular[f"o{i}"]))
                    oyuncular.pop(f"o{i}")
                else:
                    choice2 = random.choice(formalar)
                    formalar.remove(choice2)
                    oyuncular.pop(f"o{i}")
        liste = list(oyuncular)[-1]
        if formalar[-1] == 11 and int(oyuncular[liste]) == 11:
            iyi_sonuc += 1
        else:
            kotu_sonuc += 1
    sonuc = iyi_sonuc / (iyi_sonuc + kotu_sonuc)
    return sonuc

app = Flask(__name__)
import numpy as np

a = np.array([1, 2, 3])


@app.route('/')
def hello_world():  # put application's code here
    return str(futbol())


if __name__ == '__main__':
    app.run()


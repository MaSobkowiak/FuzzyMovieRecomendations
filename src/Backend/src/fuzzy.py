import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from fuzzy_vals import POPULARITY, BUDGET, RELEASE, RUNTIME, VOTE


def get_fuzzy(year, budget, mood, duration, vote, popularity, objects_list):

    # Stworzenie uniwersum
    f_year = ctrl.Antecedent(np.arange(1960, 2022, 1), "year")
    f_budget = ctrl.Antecedent(np.arange(0, 500000, 1), "budget")
    # f_mood = ctrl.Antecedent(np.arange(0.7, 8.2, 0.1), "mood")
    f_duration = ctrl.Antecedent(np.arange(4.0, 15.0, 0.1), "duration")
    f_vote = ctrl.Antecedent(np.arange(4.0, 15.0, 0.1), "vote")
    f_popularity = ctrl.Antecedent(np.arange(4.0, 15.0, 0.1), "popularity")

    f_year["old"] = fuzz.trimf(
        f_year.universe, RELEASE["old"])
    f_year["between"] = fuzz.trimf(
        f_year.universe, RELEASE["between"])
    f_year["new"] = fuzz.trimf(
        f_year.universe, RELEASE["new"])

    f_budget["low"] = fuzz.trimf(f_budget.universe, BUDGET["low"])
    f_budget["high"] = fuzz.trimf(f_budget.universe, BUDGET["high"])

    # f_mood["sad"] = fuzz.trimf(f_mood.universe, settings.ENGINE_CAPACITY["sad"])
    # f_mood["happy"] = fuzz.trimf(f_mood.universe, settings.ENGINE_CAPACITY["happy"])

    f_duration["short"] = fuzz.trimf(
        f_duration.universe, RUNTIME["short"])
    f_duration["long"] = fuzz.trimf(
        f_duration.universe, RUNTIME["long"])

    f_vote["low"] = fuzz.trimf(f_vote.universe, VOTE["low"])
    f_vote["medium"] = fuzz.trimf(f_vote.universe, VOTE["medium"])
    f_vote["high"] = fuzz.trimf(f_vote.universe, VOTE["high"])

    f_popularity["low"] = fuzz.trimf(
        f_popularity.universe, POPULARITY["low"])
    f_popularity["medium"] = fuzz.trimf(
        f_popularity.universe, POPULARITY["medium"])
    f_popularity["high"] = fuzz.trimf(
        f_popularity.universe, POPULARITY["high"])

    # Obliczanie przynaleznosci danego obiektu do podanych danych kwerendy i tworzenie przefiltrowanej listy
    end_object_list = []
    for movie in objects_list:

        comparator = []
        comparator.append(
            fuzz.interp_membership(
                f_year.universe,
                f_year[str(year)].mf,
                movie.release_date,
            )
        )
        comparator.append(
            fuzz.interp_membership(
                f_budget.universe,
                f_budget[str(budget)].mf,
                movie.budget,
            )
        )
        # comparator.append(
        #     fuzz.interp_membership(
        #         f_mood.universe,
        #         f_mood[str(mood)].mf,
        #         movie.genres,
        #     )
        # )
        comparator.append(
            fuzz.interp_membership(
                f_duration.universe,
                f_duration[str(duration)].mf,
                movie.runtime,
            )
        )
        comparator.append(
            fuzz.interp_membership(
                f_vote.universe,
                f_vote[str(vote)].mf,
                movie.vote_average,
            )
        )
        comparator.append(
            fuzz.interp_membership(
                f_popularity.universe,
                f_popularity[str(popularity)].mf,
                movie.popularity,
            )
        )
        if comparator and min(comparator) > 0.7:
            end_object_list.append(movie)

    return end_object_list

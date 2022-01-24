from tkinter.messagebox import NO
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from .fuzzy_vals import POPULARITY, BUDGET, RELEASE, RUNTIME, VOTE
from .models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_fuzzy(year, budget, mood, duration, vote, popularity, movie):

    f_year = ctrl.Antecedent(np.arange(1960, 2022, 1), "year")
    f_budget = ctrl.Antecedent(np.arange(0, 500000, 1), "budget")
    # f_mood = ctrl.Antecedent(np.arange(0.7, 8.2, 0.1), "mood")
    f_duration = ctrl.Antecedent(np.arange(4.0, 15.0, 0.1), "duration")
    f_vote = ctrl.Antecedent(np.arange(4.0, 15.0, 0.1), "vote")
    f_popularity = ctrl.Antecedent(np.arange(4.0, 500.0, 0.1), "popularity")

    f_year["low"] = fuzz.trimf(
        f_year.universe, RELEASE["low"])
    f_year["medium"] = fuzz.trimf(
        f_year.universe, RELEASE["medium"])
    f_year["high"] = fuzz.trimf(
        f_year.universe, RELEASE["high"])

    f_budget["low"] = fuzz.trimf(f_budget.universe, BUDGET["low"])
    f_budget["medium"] = fuzz.trimf(f_budget.universe, BUDGET["medium"])
    f_budget["high"] = fuzz.trimf(f_budget.universe, BUDGET["high"])

    # f_mood["sad"] = fuzz.trimf(f_mood.universe, settings.ENGINE_CAPACITY["sad"])
    # f_mood["happy"] = fuzz.trimf(f_mood.universe, settings.ENGINE_CAPACITY["happy"])

    f_duration["low"] = fuzz.trimf(
        f_duration.universe, RUNTIME["low"])
    f_duration["medium"] = fuzz.trimf(
        f_duration.universe, RUNTIME["medium"])
    f_duration["high"] = fuzz.trimf(
        f_duration.universe, RUNTIME["high"])

    f_vote["low"] = fuzz.trimf(f_vote.universe, VOTE["low"])
    f_vote["medium"] = fuzz.trimf(f_vote.universe, VOTE["medium"])
    f_vote["high"] = fuzz.trimf(f_vote.universe, VOTE["high"])

    f_popularity["low"] = fuzz.trimf(
        f_popularity.universe, POPULARITY["low"])

    f_popularity["medium"] = fuzz.trimf(
        f_popularity.universe, POPULARITY["medium"])

    f_popularity["high"] = fuzz.trimf(
        f_popularity.universe, POPULARITY["high"])

    comparator = []
    comparator.append(
        fuzz.interp_membership(
            f_year.universe,
            f_year[str(year)].mf,
            movie.release_date.year,
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

    return comparator

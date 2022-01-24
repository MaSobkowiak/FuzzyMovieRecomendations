BUDGET = {
    "low": [0, 1000, 100000],
    "medium": [90000, 124955000, 250000000],
    "high": [20000000, 55000000, 380000000]
}

POPULARITY = {
    "low": [0, 3, 6],
    "medium": [5, 10, 12],
    "high": [10, 15, 547]
}

RELEASE = {
    "low": [1874, 1930, 1960],
    "medium": [1950, 2000, 2005],
    "high": [2001, 2010, 2020]
}

RUNTIME = {
    "low": [0, 20, 60],
    "medium": [70, 90, 130],
    "high": [110, 150, 1256]
}

VOTE = {
    "low": [0, 2, 5],
    "medium": [2, 6, 8],
    "high": [7, 9, 10]
}
COMPOUNDS = {
    "RELEASE": 0.3,
    "RUNTIME": 0.25,
    "VOTE": 0.25,
    "POPULARITY": 0.2,
}
COMPOUNDS_WITH_BUDGET = {
    "RELEASE": 0.3,
    "RUNTIME": 0.25,
    "VOTE": 0.25,
    "POPULARITY": 0.1,
    "BUDGET": 0.1,
}

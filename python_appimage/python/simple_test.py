from io import StringIO

import cyclopts
import great_tables
import hy
import marimo  # TODO: have a single test script for WASM and appimages using marimo.
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import polars as pl
import pytest
import sympy as sp
import xarray as xr
from boltons.iterutils import chunked
from hypothesis import given, settings
from hypothesis import strategies as st
from parsimonious.grammar import Grammar
from plumbum import local
from ptpython.repl import PythonRepl
from pydantic import BaseModel
from pyparsing import Word, alphas
from quantiphy import Quantity, as_real, render
from rich.console import Console
from scipy.optimize import minimize
from sexpdata import dumps, loads
from toolz import curry


def test_cyclopts():
    app = cyclopts.App()

    @app.command
    def greet(name: str = "world") -> str:
        return f"hello {name}"

    assert app["greet"] is not None


def test_polars():

    df = pl.DataFrame({"x": [1, 2, 3], "y": [4.0, 5.0, 6.0]})
    assert df.shape == (3, 2)
    assert df["x"].sum() == 6


def test_xarray():

    da = xr.DataArray([1.0, 2.0, 3.0], dims=["x"])
    assert float(da.mean()) == pytest.approx(2.0)


def test_plotly():

    fig = go.Figure(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]))
    assert fig.data[0].x == (1, 2, 3)


def test_pydantic():

    class Point(BaseModel):
        x: float
        y: float

    p = Point(x=1, y=2)
    assert p.x == 1.0


def test_scipy():

    result = minimize(lambda x: (x[0] - 1) ** 2, x0=[0.0])
    assert result.x[0] == pytest.approx(1.0, abs=1e-4)


def test_sympy():

    x = sp.Symbol("x")
    assert sp.diff(x**3, x) == 3 * x**2


def test_quantiphy():

    q = Quantity("1MHz")
    assert q == 1e6

    period = Quantity("Tclk = 10ns -- clock period")
    assert period.name == "Tclk"
    assert period.units == "s"
    assert period.desc == "clock period"

    assert as_real("1.5 kHz") == 1500.0
    assert render(1e-5, "Ohms") == "10 uOhms"


def test_psf_utils():
    import psf_utils

    assert hasattr(psf_utils, "PSF")


def test_rich():
    buf = StringIO()
    Console(file=buf, highlight=False).print("ok")
    assert "ok" in buf.getvalue()


def test_parsimonious():

    g = Grammar(r'greeting = "hello"')
    assert g["greeting"].parse("hello")


def test_boltons():

    assert list(chunked([1, 2, 3, 4], 2)) == [[1, 2], [3, 4]]


def test_toolz():

    add = curry(lambda a, b: a + b)
    assert add(1)(2) == 3


def test_plumbum():

    out = local["echo"]("hi").strip()
    assert out == "hi"


def test_hypothesis():
    @given(st.integers(min_value=0, max_value=100))
    @settings(max_examples=10)
    def always_positive(n):
        assert n >= 0

    always_positive()


def test_numpy():
    assert np.dot([1, 2], [3, 4]) == 11


def test_pandas():

    df = pd.DataFrame({"a": [1, 2, 3]})
    assert df["a"].sum() == 6


def test_ptpython():

    assert PythonRepl is not None


def test_sexpdata():

    basic_list = loads('("a" "b")')
    assert basic_list == ["a", "b"]
    assert dumps(basic_list) == '("a" "b")'


def test_pyparsing():

    greet = Word(alphas) + "," + Word(alphas) + "!"
    hello = "Hello, World!"
    assert list(greet.parse_string(hello)) == ["Hello", ",", "World", "!"]


def test_hy():

    assert hy.eval(hy.read_many("(setv x 1) (+ x 1)")) == 2


def test_versions():

    for mod in (great_tables, marimo):
        assert getattr(mod, "__version__", None) is not None, (
            f"{mod.__name__}: no __version__"
        )


# Note: This test script was initially authored by: Claude, but has since been verified and modified by
# me.

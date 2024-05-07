from typing import Any
from bs4 import BeautifulSoup
import pandas as pd
import requests

try:
    from requests_html import HTMLSession
except Exception:
    pass


def force_float(elt) -> float | Any:
    try:
        return float(elt)
    except:
        return elt


def get_calls(ticker, date=None) -> Any:
    """
    Extracts call option table for input ticker and expiration date.
    :param ticker:
    :param date:
    """

    options_chain = get_options_chain(ticker, date)
    return options_chain["calls"]


def get_puts(ticker, date=None) -> Any:
    """
    Extracts put option table for input ticker and expiration date.
    :param ticker:
    :param date:
    """

    options_chain = get_options_chain(ticker, date)
    return options_chain["puts"]


def get_expiration_dates(ticker) -> list[str] | list:
    """
    Scrapes the expiration dates from each option chain for input ticker.
    :param ticker: str - Ticker symbol of the stock/option.
    :param list: list of expiration dates as strings
    """

    try:
        # assuming build_options_url is a function that constructs the URL for the options page
        site = build_options_url(ticker)
        session = HTMLSession()
        response = session.get(site)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")
        options = soup.select("div.itm")  # adjust selector on actual html structure

        dates = [option.text.strip() for option in options if option.text.strip() != ""]
        return dates
    except Exception as e:
        print(f"An error occured: {e}")
        return []
    finally:
        session.close()


def build_options_url(ticker, date=None) -> Any:
    """
    Constructions the URL pointing to options chain.
    """
    url = "https://finance.yahoo.com/quote/" + ticker + "/options?p=" + ticker

    if date is not None:
        url = url + "&date=" + str(int(pd.Timestamp(date).timestamp()))

    return url


def get_options_chain(ticker, date=None, raw=True, headers=None) -> Any:
    """
    Fetch options data for the given ticker and expiration date.
    :param ticker str - Stock ticker symbol
    :param date: str - Optional, the expiration date to retrieve options for
    :param raw: bool - If False, format certain columns of data
    :param headers: dict - HTTP headers to use for the request
    :return dict: - Dictionary containing DataFrame for calls and puts
    """
    if headers is None:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
    try:
        site = build_options_url(ticker, date)
        response = requests.get(site, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        tables = soup.find_all("table")
        dataframes = [pd.read_html(str(table)) for table in tables]

        if len(dataframes) == 1:
            calls = dataframes[0][0].copy()
            puts = pd.DataFrame(columns=calls.columns)
        elif len(dataframes) > 1:
            calls, puts = dataframes[0][0].copy(), dataframes[1][0].copy()

        # Optionally clean and format the data
        if not raw:
            for df in (calls, puts):
                # clean and convert data as necessary
                df["% Change"] = (
                    df["% Change"]
                    .str.replace("%", "")
                    .str.replace("-", "0")
                    .astype(float)
                    / 100
                )
                df["Volume"] = (
                    df["Volume"]
                    .str.replace("-", "0")
                    .replace(",", "", regex=True)
                    .astype(int)
                )
                df["Open Interest"] = (
                    df["Open Interest"]
                    .str.replace("-", "0")
                    .replace(",", "", regex=True)
                    .astype(int)
                )
        return {"calls": calls, "puts": puts}

    except Exception as e:
        print(f"An error occured: {e}")  # debug: print any error that occurs
        return {"calls": pd.DataFrame(), "puts": pd.DataFrame()}
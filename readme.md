##Compare house prices in the Netherlands

This is a simple Streamlit app where you can compare Dutch house prices per country section (LD), province (PV) or municipality/city within the year 1995 until 2019.

The data is from the Statistics Netherlands ([CBS](https://www.cbs.nl/en-gb)). It uses the Statistics Netherlands opendata API client for Python ([cbsodata](https://pypi.org/project/cbsodata/)).

It also uses [streamlit-echarts](https://github.com/andfanilo/streamlit-echarts) for theming the chart. You can theme your own chart with the ECharts [theme-builder](https://echarts.apache.org/en/theme-builder.html), download/copy the theme and past it in the theme.json file.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/mvs12/cbs-houseprices-streamlit/app/)

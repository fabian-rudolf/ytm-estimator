# Yield to Maturity (YTM) Estimator

Yield to Maturity (YTM) is a fundamental concept in bond investing. It's the internal rate of return earned by an investor who buys the bond today at the market price, assuming that the bond is held until maturity.

However, calculating YTM can be a bit tricky as it involves solving a complex equation. This YTM Estimator aims to simplify this process through an easy-to-use web application.

## Features
- **User-friendly interface**: Just input your bond parameters like price, coupon rate, face value, years to maturity and get the estimated YTM instantly.
- **Accurate estimation**: We use numerical approximation methods to estimate the YTM, which provides a high level of accuracy.
- **Real-time calculation**: As soon as you input the bond parameters, the YTM is calculated in real time. No need to hit 'calculate' or wait.

## Usage
Just visit the running web app demo hosted [here](https://ytmestimator-1-z6391136.deta.app/).

## Project Structure
The codebase is structured as follows:
- `main.py`: This is the main script where we have defined our FastAPI application and the endpoint to calculate the YTM.
- `templates/index.html`: This single-page includes sections for the input parameters, the result output and a self-documenting explanation of bond parameters.

## Contributing
Contributions to the YTM Estimator are welcomed. If you have a feature request, bug report, or proposal for improvement, please open an issue on our GitHub repo.

# VIX Futures Forecasting

## Project Overview

This repository represents a personal project by Divija Balasankula, driven by my passion for financial markets and extending beyond a course project in my Financial Mathematics program at NC State University. The project focuses on forecasting the CBOE Volatility Index (VIX), often called the "fear index," to understand and predict market volatility dynamics using advanced time series and machine learning models. By modeling VIX futures, the project aims to provide actionable insights for trading strategies, leveraging both traditional time series models (SARIMA, SARIMAX, GARCH) and exploring the potential of machine learning techniques (ensemble methods, deep learning, gradient boosting). The work includes data analysis, model calibration, performance evaluation, and the development of volatility-based trading strategies.

**Contact**: Divija Balasankula (drbalasa@ncsu.edu)

## Objectives

- Analyze historical VIX and S&P 500 option data to understand market volatility dynamics.
- Implement and compare time series models (SARIMA, SARIMAX, GARCH) for VIX futures forecasting.
- Explore machine learning models to capture non-linear patterns in VIX data.
- Evaluate model performance using metrics such as RMSE, MAE, and R-squared.
- Develop and propose trading strategies based on VIX forecasts, focusing on options and futures.
- Share findings through detailed Medium articles for broader dissemination.

## Background: The VIX

The CBOE Volatility Index (VIX), introduced in 1993, measures market expectations of near-term volatility based on the implied volatilities of S&P 500 index options. Known as the "fear gauge," it reflects investor sentiment and is widely used to anticipate market movements. VIX futures, which this project forecasts, allow investors to trade expected volatility, making accurate modeling critical for risk management and trading.

## Methodology

### Data Collection
- **Data Sources**: Historical VIX index data, VIX futures prices, and S&P 500 option prices.
- **Exogenous Variables**: Economic indicators (e.g., interest rates, inflation data, market indices) for SARIMAX modeling.
- **Preprocessing**: Cleaning and normalizing data to handle missing values, outliers, and non-stationarity.

### Models Implemented

1. **Time Series Models**:
   - **SARIMA (Seasonal Autoregressive Integrated Moving Average)**:
     - Captures trends and seasonality in VIX data.
     - Parameters: Order (p, d, q) and seasonal order (P, D, Q, s) tuned via grid search.
   - **SARIMAX (SARIMA with Exogenous Variables)**:
     - Extends SARIMA by incorporating external factors (e.g., S&P 500 returns, macroeconomic indicators).
     - Improves forecasting by accounting for exogenous influences on volatility.
   - **GARCH (Generalized Autoregressive Conditional Heteroskedasticity)**:
     - Models volatility clustering, a hallmark of financial time series.
     - Combined with SARIMAX to create a SARIMAX-GARCH model, capturing both VIX levels and volatility dynamics.

2. **Machine Learning Models** (Exploratory):
   - **Ensemble Methods**: Random Forests and Gradient Boosting (e.g., XGBoost) to capture non-linear relationships.
   - **Deep Learning**: Recurrent Neural Networks (RNNs) and Long Short-Term Memory (LSTM) networks for sequential data modeling.
   - **Feature Engineering**: Incorporates lagged VIX values, S&P 500 returns, and economic indicators as features.

### Model Performance Metrics
- **Root Mean Squared Error (RMSE)**: Measures average prediction error.
- **Mean Absolute Error (MAE)**: Quantifies absolute deviations in forecasts.
- **R-squared**: Assesses the proportion of variance explained by the model.

**Key Results**:
- The SARIMAX-GARCH model showed significant improvements in residual analysis and forecasting accuracy compared to standalone SARIMA.
- Forecasted VIX levels for the near term: mean of 20.11, median of 19.70 (compared to current trading value of 15.27), indicating rising volatility expectations.
- Machine learning models are under exploration to further enhance accuracy, particularly for capturing non-linear patterns.

### Trading Strategies
Based on the forecasted VIX increase (mean: 20.11, median: 19.70) and insights from my Medium articles ([The Art and Science of VIX Analysis](https://medium.com/@divijarao.b/the-art-and-science-of-vix-analysis-f0e2ae7de16e) and [The VIX Saga Continues](https://medium.com/@divijarao.b/the-vix-saga-continues-unraveling-market-volatility-with-advanced-time-series-models-cf2339251299)), the following trading strategies are proposed:

1. **Long Straddle**:
   - **Rationale**: The forecasted VIX increase suggests heightened market volatility, ideal for a long straddle on S&P 500 options.
   - **Strategy**: Buy both a call and a put option on the S&P 500 with the same strike price and expiration date. This benefits from large price movements in either direction, capitalizing on the expected volatility spike.
   - **Implementation**: Target at-the-money (ATM) options with near-term expirations to align with the VIX forecast horizon.

2. **Long Strangle**:
   - **Rationale**: Similar to the straddle, but with lower cost due to out-of-the-money (OTM) options, suitable for high volatility expectations.
   - **Strategy**: Purchase an OTM call and an OTM put on the S&P 500 with the same expiration. This strategy profits from significant market moves while reducing premium costs.
   - **Implementation**: Select strike prices slightly OTM to balance cost and potential payoff, based on VIX forecast confidence intervals.

3. **Long VIX Call Options**:
   - **Rationale**: Direct exposure to rising VIX levels, as predicted by the models, makes VIX call options attractive.
   - **Strategy**: Buy VIX call options with strike prices near or above the forecasted mean (20.11). This strategy profits if the VIX rises as expected, leveraging the "fear index" directly.
   - **Implementation**: Choose options with expirations matching the forecast period (e.g., 1-3 months) and monitor VIX futures term structure for optimal entry points.

4. **VIX Futures Spread**:
   - **Rationale**: The VIX futures term structure often exhibits contango or backwardation, which can be exploited alongside the forecast.
   - **Strategy**: If the term structure is in contango (longer-dated futures priced higher), consider a calendar spread by going long near-term VIX futures and short longer-term futures, expecting convergence as volatility rises.
   - **Implementation**: Analyze the VIX futures curve and enter spreads when the forecast aligns with a steep contango, adjusting positions based on model updates.

5. **Hedging with VIX ETFs**:
   - **Rationale**: VIX-related exchange-traded funds (ETFs) like VXX provide a liquid way to hedge equity portfolios against predicted volatility spikes.
   - **Strategy**: Allocate a portion of the portfolio to long positions in VIX ETFs when the model predicts rising VIX levels. This hedges against potential equity market downturns.
   - **Implementation**: Use VXX or similar ETFs, scaling position size based on portfolio risk and VIX forecast confidence.

**Note**: These strategies carry significant financial risk. Thorough backtesting and risk management are essential before deployment.

## Repository Structure
```
vix-futures-forecasting/
├── data/
│   ├── vix_historical.csv       # Historical VIX index and futures data
│   └── exogenous_data.csv       # Economic indicators for SARIMAX
├── src/
│   ├── sarima_model.py          # SARIMA model implementation
│   ├── sarimax_model.py         # SARIMAX model implementation
│   ├── garch_model.py           # GARCH and SARIMAX-GARCH models
│   ├── ml_models.py             # Machine learning models (Random Forest, XGBoost, LSTM)
│   └── analysis.py              # Data preprocessing and performance metrics
├── notebooks/
│   └── vix_forecasting.ipynb    # Jupyter notebook for visualization and analysis
├── results/
│   └── model_performance.csv    # Model performance metrics and forecasts
└── README.md                    # Project documentation
```

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/vix-futures-forecasting.git
   cd vix-futures-forecasting
   ```

2. **Set Up Python Environment**:
   - Requires Python 3.8+.
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Example `requirements.txt`:
     ```
     numpy
     pandas
     scipy
     statsmodels
     arch
     scikit-learn
     xgboost
     tensorflow
     matplotlib
     ```

3. **Data Preparation**:
   - Place VIX historical data in `data/vix_historical.csv` (columns: date, VIX close, futures prices).
   - Place exogenous variables (e.g., S&P 500 returns, interest rates) in `data/exogenous_data.csv`.
   - Ensure data is preprocessed for stationarity and missing values.

4. **Run Analysis**:
   - Execute model scripts:
     ```bash
     python src/sarimax_model.py
     ```
   - Visualize results using the Jupyter notebook:
     ```bash
     jupyter notebook notebooks/vix_forecasting.ipynb
     ```

## Usage

1. **Data Preprocessing**:
   - Use `src/analysis.py` to clean and prepare VIX and exogenous data.
   - Example: Handle missing values and test for stationarity using Augmented Dickey-Fuller (ADF) test.

2. **Model Calibration**:
   - Run `src/sarima_model.py` and `src/sarimax_model.py` to tune SARIMA/SARIMAX parameters via grid search.
   - Use `src/garch_model.py` to fit the SARIMAX-GARCH model, calibrating volatility parameters.
   - Experiment with `src/ml_models.py` for machine learning-based forecasts.

3. **Forecasting**:
   - Generate VIX forecasts using calibrated models.
   - Example: Forecast VIX for the next 1-3 months using SARIMAX-GARCH and visualize in `notebooks/vix_forecasting.ipynb`.

4. **Trading Strategy Implementation**:
   - Use forecast outputs to implement strategies like long straddles or VIX call options.
   - Backtest strategies using historical data to assess profitability and risk.

## Results
- **Forecast**: The SARIMAX-GARCH model predicts a VIX increase to a mean of 20.11 and median of 19.70, compared to the current value of 15.27, suggesting rising market volatility.
- **Model Performance**: SARIMAX-GARCH outperforms SARIMA in residual analysis and forecasting accuracy, though limitations remain due to market unpredictability.
- **Trading Implications**: The forecasted volatility spike supports strategies like long straddles, strangles, VIX calls, futures spreads, and ETF hedging.

## Related Blog Posts
As part of this project, I authored two Medium articles to share my findings:
1. [The Art and Science of VIX Analysis](https://medium.com/@divijarao.b/the-art-and-science-of-vix-analysis-f0e2ae7de16e): Introduces VIX modeling concepts and initial time series results.
2. [The VIX Saga Continues: Unraveling Market Volatility with Advanced Time Series Models](https://medium.com/@divijarao.b/the-vix-saga-continues-unraveling-market-volatility-with-advanced-time-series-models-cf2339251299): Explores advanced models and trading strategy implications.

## Future Work
- Enhance SARIMAX-GARCH with additional exogenous variables (e.g., geopolitical events, sentiment data).
- Develop and test machine learning models (e.g., LSTM, XGBoost) for improved forecasting accuracy.
- Expand trading strategies to include dynamic portfolio optimization and risk parity approaches.
- Validate models with additional datasets, such as international volatility indices (e.g., VSTOXX).
- Incorporate real-time data feeds for live forecasting and trading.

## Contact
For questions or collaboration, reach out to:
- Divija Balasankula: drbalasa@ncsu.edu

## Acknowledgments
- Institution: NC State University, Financial Mathematics Department
- Inspiration: My coursework and personal interest in financial market dynamics

---

**Note**: This project is for educational purposes. Trading strategies involve significant financial risk and should be thoroughly backtested and validated before implementation.

# Basic tests for our financial sentiment project

def test_pandas_import():
    """Test pandas can be imported"""
    import pandas as pd
    assert pd.__version__ is not None

def test_numpy_import():
    """Test numpy can be imported"""
    import numpy as np
    assert np.__version__ is not None

def test_sentiment_function():
    """Test our sentiment function works"""
    from textblob import TextBlob
    
    # Positive headline
    positive = TextBlob("record breaking profits amazing growth")
    assert positive.sentiment.polarity > 0
    
    # Negative headline
    negative = TextBlob("terrible losses bankruptcy failure")
    assert negative.sentiment.polarity < 0
    
    print("✅ Sentiment function works correctly!")

def test_daily_return_calculation():
    """Test daily return calculation"""
    import pandas as pd
    import numpy as np
    
    # Create sample stock data
    prices = pd.Series([100, 102, 98, 105, 101])
    returns = prices.pct_change() * 100
    
    # First return should be NaN
    assert np.isnan(returns.iloc[0])
    
    # Second return should be 2%
    assert abs(returns.iloc[1] - 2.0) < 0.01
    
    print("✅ Daily return calculation works!")
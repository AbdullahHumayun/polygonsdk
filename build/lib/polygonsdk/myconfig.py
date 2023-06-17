from datetime import datetime, timedelta

YOUR_STOCKSERA_KEY="msKBHbxk.98WJ6HB4AlO49mSUcSBiIYqPxVwSOIcT"
# Date and Time - import these to easily create date parameters for different functions such as option aggregates, stock aggregates.
today = datetime.today().date()  # Current date
now = datetime.now()  # Current date and time
today_str = today.strftime('%Y-%m-%d')  # Current date as string
five_days_ago = now - timedelta(days=5)  # Five days ago from current date and time
five_days_ago_str = five_days_ago.strftime('%Y-%m-%d')  # Five days ago as string
two_days_from_now = now + timedelta(days=2)  # Two days from now
two_days_from_now_str = two_days_from_now.strftime('%Y-%m-%d')  # Two days from now as string
five_days_from_now = now + timedelta(days=5)  # Five days from now
five_days_from_now_str = five_days_from_now.strftime('%Y-%m-%d')  # Five days from now as string
thirty_days_ago = now - timedelta(days=30)  # Thirty days ago from current date and time
thirty_days_ago_str = thirty_days_ago.strftime("%Y-%m-%d")  # Thirty days ago as string
thirty_days = now + timedelta(days=30)  # Thirty days ago from current date and time
thirty_days_from_now_str = thirty_days.strftime("%Y-%m-%d")  # Thirty days ago as string
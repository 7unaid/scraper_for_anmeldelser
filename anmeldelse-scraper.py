import requests
from bs4 import BeautifulSoup
import pandas as pd
import openai

# Konfigurerer OpenAI
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Skraper data
url = 'https://www.scrapethissite.com/pages/forms/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Får tak i tabellen
rows = soup.find_all('tr', class_='team')

data = []

for row in rows:
    # Extract relevant data
    state = row.find('td', class_='name').text.strip()
    wins = int(row.find('td', class_='wins').text.strip())
    losses = int(row.find('td', class_='losses').text.strip())
    data.append({'state': state, 'wins': wins, 'losses': losses})

# Samler dataen
df = pd.DataFrame(data)

# Grupperer på bakgrunn av delstat og antall win/loss
grouped_df = df.groupby('state').sum()
grouped_df['win_loss_ratio'] = grouped_df['wins'] / grouped_df['losses']

# Sorterer
grouped_df = grouped_df.sort_values(by='win_loss_ratio', ascending=False)

# Printer
print("State Win/Loss Ratios:")
print(grouped_df)

"""

summary_prompt = "Based on the win/loss ratios in the data below, which state is worth investing in? \n\n"

for index, row in grouped_df.iterrows():
    summary_prompt += f"State: {index}, Wins: {row['wins']}, Losses: {row['losses']}, Win/Loss Ratio: {row['win_loss_ratio']:.2f}\n"

# Bruker ChatGPT til å oppsummere
response = openai.Completion.create(
    engine="gpt-3.5-turbo",
    prompt=summary_prompt,
    max_tokens=150
)

    summary = response.choices[0].text.strip()

    # Resultatet
    print("ChatGPT Summary:\n", summary)

    # Loggfører oppsummeringen
    with open("chatgpt_summary_log.txt", "a") as logfile:
        logfile.write("ChatGPT Summary:\n")
        logfile.write(summary + "\n")
        logfile.write("-" * 40 + "\n")

"""

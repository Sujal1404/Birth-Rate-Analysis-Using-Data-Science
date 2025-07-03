import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load dataset
data = pd.read_csv('birth_rate_dataset.csv')

# Basic info
print(data.head())
print(data.describe())

# Plot trend
sns.lineplot(x='Year', y='BirthRate', data=data[data['Country'] == 'India'])
plt.title('Birth Rate Trend in India')
plt.show()

# Correlation heatmap
sns.heatmap(data.corr(), annot=True)
plt.show()

# Regression: Predict birth rate from GDP and urban population
X = data[['GDP_per_Capita', 'Urban_Population_Percent']]
y = data['BirthRate']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model = LinearRegression()
model.fit(X_train, y_train)
print("Model R² Score:", model.score(X_test, y_test))

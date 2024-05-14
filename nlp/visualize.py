import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm

file_path = 'data/american/data.xlsx'
df = pd.read_excel(file_path)
df['Revenue'] = pd.to_numeric(df['Revenue'], errors='coerce')
df['Assets'] = pd.to_numeric(df['Assets'], errors='coerce')
df = df.dropna(subset=['Revenue', 'Assets'], inplace=True)
df['NTEE_First_Char'] = df['NTEE Code'].astype(str).str[0]
df['NTEE_First_Char'] = df['NTEE_First_Char'].replace('', 'Z') # Z is for unknown sectors
print("Made dataframe")

# Create a histogram of the revenue data
plt.figure(figsize=(10, 6))
bin_edges = [0, 4999, 9999, 24999, 99999, 499999, 999999, 4999999, 9999999, 49999999]
counts, bins, patches = plt.hist(df['Revenue'], bins=bin_edges, color='skyblue', edgecolor='black')
plt.xticks(bins, labels=[f'{int(bins[i])}-{int(bins[i+1])}' for i in range(len(bins)-1)])
plt.title('Histogram of Revenue')
plt.xlabel('Revenue')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
print("Finished histogram of revenues")

# Create a box plot of the revenue data
plt.figure(figsize=(10, 6))
plt.boxplot(df['Revenue'], vert=False)
plt.title('Box Plot of Revenue')
plt.xlabel('Revenue')
plt.grid(True)
plt.show()
print("Finished box plots of revenues")

# Create a pie chart showing nonprofit sectors
# labels = 'A: Arts, Culture, and Humanities', 'B: Education', 'C: Environment', 'D: Animal-Related', 'E: Health Care', "F: Mental Health and Crisis Intervention", "G: Voluntary Health Associations & Medical Disciplines", "H: Medical Research", "I: Crime & Legal-Related", "J: Employment", "K: Food, Agriculture & Nutrition", "L: Housing & Shelter", "M: Public Safety, Disaster Preparedness & Relief", "N: Recreation & Sports", "O: Youth Development", "P: Human Services", "Q: International, Foreign Affairs & National Security", "R: Civil Rights, Social Action & Advocacy", "S: Community Improvement & Capacity Building", "T: Philanthropy, Voluntarism & Grantmaking Foundations", "U: Science & Technology", "V: Social Science", "W: Public & Societal Benefit", "X: Religion-Related", "Y: Mutual & Membership Benefit", "Z: Unknown"
ntee_counts = df['NTEE_First_Char'].value_counts()
plt.figure(figsize=(10, 8))
plt.pie(ntee_counts, labels=ntee_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart of NTEE Codes')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
print("Finished pie charts of nonprofit sectors")

# Perform regression analysis between assets and revenues 
X = df['Assets']
y = df['Revenue']  
model = sm.OLS(y, X).fit()
print(model.summary())
plt.figure(figsize=(10, 6))
plt.scatter(df['Assets'], df['Revenue'], alpha=0.5, label='Data points')
plt.plot(df['Assets'], model.predict(X), color='red', label='Regression Line')
plt.title('Regression Analysis and Scatter Plot (No Constant)')
plt.xlabel('Assets ($)')
plt.ylabel('Revenue ($)')
plt.legend()
plt.grid(True)
plt.show()
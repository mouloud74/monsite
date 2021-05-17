# importer la librairie pandas pour traiter les données
import pandas as pd

# Lecture du dataset titanic assigné à la variable data
data = pd.read_csv('titanic.csv')
# Le nombre de lignes et de colonnes
print(f'Le nombre de ligne est : {data.shape[0]}')
print(f'Le nombre de colonnes est : {data.shape[1]}')
print(data.shape)

# Les noms des colonnes
list(data.columns)

# Les types des colonnes
for col in data.columns :
    print(f'{col:-<50}{data[col].dtype}')

# Statisiques des variables numériques
data.describe()
# Description des variables catégorical
data.describe(include=[object])

# Visualisation
# Importer matplotlib avec l'utilisation du style seaborn
import matplotlib.pyplot as plt
plt.style.use('seaborn')
# Fréquences des ages
data.age.hist(figsize = (12,8), bins = 40 )
plt.title("AGE", fontsize = 15)
plt.xlabel("age", fontsize = 13)
plt.ylabel("frequences", fontsize = 13)
plt.title('Frequences des ages',fontsize=15)
plt.show()

# Distribution des survivants
import warnings
warnings.simplefilter('ignore')
plt.rcParams['figure.figsize']=(5,3)
import seaborn as sns
sns.countplot(data['survived'])
plt.title('La distribution des survivants',fontsize=15)
plt.show()

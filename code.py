import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Load data of 8 tapioca pearl formulations with textural properties
file = 'PCA_TS(new)2.xlsx' 

# Load all columns
try:
    data = pd.read_excel(file, usecols=None)  
except Exception as e:
    print(f"Error loading file: {e}")
    exit()

# Check for missing values
if data.isnull().sum().sum() > 0:
    print("Warning: Missing values detected. Consider imputing or removing them.")
    print(data.isnull().sum())

# Define textural properties and hydrocolloid variables
textural_properties = ['Hardness', 'Cohesiveness', 'Chewiness']
features = ['Agar', 'Konjac', 'HAG', 'LAG', 'Iota', 'Kappa']
name = "Tapioca Starch"  

# Split the data
X = data[textural_properties]
Y = data[features]  

# Standardize the dataset
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  

# Apply PCA
try:
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
except Exception as e:
    print(f"PCA failed: {e}")
    exit()

# Compute PCA correlation factors (loadings)
pc_correlations = pd.DataFrame(pca.components_.T, index=textural_properties, columns=['PC1', 'PC2'])
print("\nPCA Loadings (Correlations of Features with Principal Components):")
print(pc_correlations)

# Explained variance
explained_variance = pca.explained_variance_ratio_
print(f"\nTotal Explained Variance: {sum(explained_variance):.2f}")

# Get PCA loadings
loadings = pca.components_.T * np.sqrt(pca.explained_variance_)
loading_df = pd.DataFrame(loadings, columns=['PC1', 'PC2'], index=textural_properties)

# Biplot
plt.figure(figsize=(10, 7))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c='blue', s=50, label='Samples')

# Annotate samples
for i, txt in enumerate(data['Sample']):
    plt.annotate(txt, (X_pca[i, 0], X_pca[i, 1]), fontsize=9)

# Plot the loadings (arrows for textural properties)
for property, (x, y) in zip(textural_properties, zip(loading_df['PC1'], loading_df['PC2'])):
    plt.arrow(0, 0, x, y, color='r', alpha=0.75, head_width=0.05)
    plt.text(x * 1.2, y * 1.2, property, color='g', ha='center', va='center', fontsize=9)

# Plot settings
plt.axhline(0, color='gray', lw=1)
plt.axvline(0, color='gray', lw=1)
plt.xlabel(f'PC1 ({explained_variance[0]*100:.2f}%)')
plt.ylabel(f'PC2 ({explained_variance[1]*100:.2f}%)')
plt.title(f'PCA Biplot of Textural Properties for {name}')
plt.grid()
plt.show()

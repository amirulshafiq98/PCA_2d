![Logo](https://www.capecrystalbrands.com/cdn/shop/articles/hydrocolloid-methylcellulose-795485.jpg?v=1696824498)

# Project Background
Understanding the sensory properties of food products is crucial in food science and consumer research. This project applies Principal Component Analysis (PCA) to analyse the textural properties of 8 tapioca pearl formulations, helping to identify which combination of hydrocolloids could retain the textural metrics using the texture profile analysis (TPA).

# Data Structure
The dataset includes 8 different tapioca pearl formulations with the following attributes. Below is how data is stored in the excel file:

<p align="center">
  <img src="https://github.com/user-attachments/assets/98847516-58c3-49cd-acc9-b1293cc19513">
</p>

### Textural Properties (Sensory Attributes)
- Hardness (N)

- Cohesiveness

- Chewiness (N)

### Hydrocolloids Used in Formulations (%w/w)
- Agar

- Konjac

- HAG (High Acyl Gellan Gum)

- LAG (Low Acyl Gellan Gum)

- Iota Carrageenan

- Kappa Carrageenan
  

# Executive Summary
### Overview:
After plotting the PCA chart, it was evident that the combinations from TS8 and TS7 were the best ones to use as both had the highest values from PC1 which correlated with chewiness (0.97) and hardness (0.83). Since the correlation factor was low for cohesiveness (0.26), this made TS8 and TS7 the best combinations that could retain the textural properties of tapioca boba pearls. While the correlating factor along PC2 placed cohesiveness as the most significant (0.96), the hardness had a negative correlation (-0.56) resulting in both TS4 and TS5 not being able to retain the textural properties as well as TS8 and TS7. In conclusion, TS8 had a higher hardness and chewiness value than TS7, but TS7 is slightly more cohesive than TS8.

### Code
Python librabries used in this project are: 
- scikit_learn
- pandas
- numpy
- matplotlib

The first part of the code was to check for blank rows and ensure that the data is read properly<br/>

<p align="center">
  <img src="https://github.com/user-attachments/assets/24a11581-484a-45e3-92f3-774cd07bac6a">
</p>

The next part of is to scale the values using standard scaler as they were all in different units. This is also the part where I fit the values into a a PCA format before plotting the graph<br/>

<p align="center">
  <img src="https://github.com/user-attachments/assets/4139b906-8dfc-49c1-9807-ee732772fdcc">
</p>

Finally, I plotted the graphs using matplotlib along with the explained variances for each of the principal components<br/>

<p align="center">
  <img src="https://github.com/user-attachments/assets/4564eda4-881f-47e6-8881-a2f7c7f8d988">
</p>

### PCA Implementation:
- Standardised textural property values using StandardScalar to ensure compatibility
- Applied PCA (Principal Component Analysis) to reduce dimensionality while retaining key information highlighting trends

<p align="center">
  <img src="https://github.com/user-attachments/assets/0f15c7dd-7927-406d-926c-75647e973bb2">
</p>

### Correlation factor and Feature Influence:

- Extracted principal components (PC1) and (PC2), which explain the majority of variance in sensory attributes
- Calculated correlation factors (loadings) to determine how each textural property influences the principal components
- Visualised results using a biplot, showcasing both sample distribution and feature influence

<p align="center">
  <img src="https://github.com/user-attachments/assets/3af09b7b-a1d4-4a42-b849-ba4b46c05962">
</p>

# Recommendations
- If a softer chew is desired, then basing the formulation off TS7 and TS8 would be ideal
- For better cohesiveness, formulations with high PC2 values should be tested further like TS4 and TS5
- Once formulation is finalised, conduct sensory analysis to determine if consumer preference aligns with PCA analysis

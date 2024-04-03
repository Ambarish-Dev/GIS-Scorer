import matplotlib.pyplot as plt

# Dummy data for GIS scores
gis_scores = [0.1, 0.3, 0.2, 0.15, 0.25]  # Example percentages for grades 0 to 4+

# Calculate total GIS
total_gis = sum(score * grade for grade, score in enumerate(gis_scores))

# Visualization
plt.bar(range(len(gis_scores)), gis_scores, tick_label=['0', '1+', '2+', '3+', '4+'])
plt.title('Distribution of GIS Scores')
plt.xlabel('GIS Score')
plt.ylabel('Percentage of Glomeruli')
plt.show()

print(f"Total GIS: {total_gis}")

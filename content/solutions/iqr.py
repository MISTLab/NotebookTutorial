# Now let's find the medium and interquartile range
med = sp.median(d)
iqr = [ np.percentile(d, 25) , np.percentile(d, 75) ]

# Plot the data with this summary
plt.hist(d, 15)
plt.plot(med, m_y, "ro")
plt.plot(iqr, [m_y] * 2, "r--");

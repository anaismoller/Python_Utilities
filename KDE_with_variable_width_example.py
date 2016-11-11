from KDE_utils import solve_kde

'''
Implementation:
KDE for data points with variable errors

gaussians will have a fixed width "b" + a variable width dependent on errors
'''

# Silverman's (1986) rule of thumb for fixed bandwidth
b = 1.06 * np.std(data) / np.power(len(data),1 / 5)

#for sampling the gaussians
xlist = np.linspace(min(data) - 2,max(data) + 2,300)  # Adjust as needed

x = data
sigma = data_error
kde_array = solve_kde(xlist,x,sigma,b)
kde_vector_data = np.sum(np.sum(kde_array,axis=2),axis=1)

#show result
plt.plot(xlist,kde_vector_data,color='red',label='data')
plt.show()
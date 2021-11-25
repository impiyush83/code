# # implementation for expectation maximization algorithm passing data, no of clusters and epsilon and no_of_iterations
# # This implementation is same as done in first question the only change here is we are running it for 20 times
# # for each cluster and returing a list of points and posterior probability where data converges in each iteration
# # and also the number of times while loop runs for data convergence
#
# import numpy as np
# import pandas as pd
# import copy
#
# def expectation_maximization(D, k, epsilon, no_iterations):
#     # finding no of rows and no of columns without classifier in data
#     n = len(D)
#     d = len(D[0])
#
#     # Making empty list of all the data required for analysis probability means and no of iterations
#     probabilities = []
#     means = []
#     iterations = []
#
#     # for itertating 20 times
#     for iteration in range(no_iterations):
#
#         # Doing all initialising in every iteration
#         # Making an empty posterior_probability array list of dimension(no_of_clusters(k) * no_of_rows of data(n))
#         posterior_probability = np.empty((k, n))
#
#         # Taking k different mean which is k random points from Data
#         mean = np.array([np.array(D[np.random.randint(0, n)]) for i in range(k)])
#
#         # Making an Empty array of the same dimension as mean
#         new_mean = np.empty((k, d))
#
#         # Making a list of k priors initially taking 1/k
#         priors = np.array(np.full(k, 1 / k))
#
#         # Initially setting error to 1
#         error = 1
#
#         # Initialising initial covariance matrix as identity matrix
#         cov_mat = np.array([np.identity(d) for i in range(k)])
#
#         # Intialisting t as 0 its number of iteration data set takes to converge
#         t = 0
#
#         # Running while loop till error become less than epsilon
#         while error >= epsilon:
#
#             # increasing t every time
#             t += 1
#
#             # Calculation probability distribution for each cluster and setting it in posterier probability
#     for cluster in range(k):
#         pdf = multivariate_normal.pdf(
#             D,
#             mean=mean[cluster],
#             cov=cov_mat[cluster],
#             allow_singular=True
#         )
#     posterior_probability[cluster] = np.matmul(pdf.reshape(n, 1),
#                                                priors[cluster].reshape(1))
#
#     # Calculating Total sum of posterier probability for each point
#     # and then dividing the posterier probability in each cluster by it
#     for row in range(n):
#         total = 0
#     for cluster in range(k):
#         total += posterior_probability[cluster][row]
#     for cluster in range(k):
#         posterior_probability[cluster][row] = posterior_probability[cluster][
#                                                   row] / total
#
#     # Iterating through each cluster to reestimate mean, covariance matrix and priors
#     for cluster in range(k):
#
#     # Calculating total_posterior_probability in ith cluster
#     total_posterior_probability = np.sum(
#         posterior_probability[cluster]) + epsilon
#
#     # Caculating new mean for ith cluster by multiplying each column with posterior probability
#     # and dividing it by total_posterior_probability in ith cluster
#     new_mean[cluster] = np.matmul(posterior_probability[cluster].reshape(1, n),
#                                   D) / total_posterior_probability
#
#     # Calculating the ith prior diving total_posterior_probability by total number of rows
#     priors[cluster] = total_posterior_probability / n
#
#     # Making an empty numerator array for calculating new covariance for particular cluster
#     numerator = np.zeros((d, d))
#
#     # Iterating through each row finding it difference from new mean and multiplting it by its transpose
#     # and add summing up all numberators and then dividing it by total_posterior_probability in ith cluster
#     for row in range(n):
#         difference = np.subtract(D[row], new_mean[cluster]).reshape((d, 1))
#     mul = posterior_probability[cluster][row] * np.matmul(difference,
#                                                           np.transpose(
#                                                               difference))
#     numerator += mul
#     cov_mat[cluster] = numerator / total_posterior_probability
#
#     # Calculating error by finding mean square in new and old mean
#     error = mean_squared_error(mean, new_mean)
#
#     # Making mean as new mean by making deep copy
#     mean = copy.deepcopy(new_mean)
#
#     # apeending probability, means and iterations to list
#     probabilities.append(posterior_probability)
#     means.append(mean)
#     iterations.append(t)
#
#     # returning all the list
#     return (means, probabilities, iterations)
#
# if __name__ == "__main__":
#
#     # reading Ionosphere data which is without any header so setting as None
#     ionosphere_df = pd.read_csv('ionosphere.data', header=None)
#
#     # Converting data frame as numpy array by removing last columns of data frame
#     D = ionosphere_df.iloc[:, :-1].to_numpy()
#
#     # Finding actual mean point of each category in data set to find error
#     true_mean = np.array([list(ionosphere_df[ionosphere_df[34] == 'g'].mean()),
#                           list(ionosphere_df[ionosphere_df[34] == 'b'].mean())])
#
#
#     # Initialising errors list which will be multi-dimensional list for storing error percent for each cluster
#     errors_cluster = []
#
#     # Initialising iteration list which will be multi-dimensional list for storing no of iteration for each cluster
#     iteration_cluster = []
#
#     # list of no of clusters
#     clusters = [2, 3, 4, 5]
#
#     # Iterating through each cluster and passing it into function
#     for cluster in clusters:
#         (means, probabilities, iterations) = expectation_maximization(D, cluster,
#                                                                   0.00001, 20)
#         errors = []
#
#         # finding prediction of cluster depending upon posterior probability of each point in each cluster
#         predictions = [np.argmax(posterior_probability, axis=0) for
#                    posterior_probability in probabilities]
#
#         # going through mean for each iteration in list
#         for j in range(len(means)):
#
#             # initialising error as 0
#             error = 0
#
#             # setting mean as mean points of specific iteration
#             mean = means[j]
#
#             # Iterating through each mean point
#             for i in range(len(mean)):
#
#                 # Calculating the eucledian distance of mean points wrt to true mean points
#                 temp = true_mean[0] - mean[i]
#                 sum_sq = np.dot(temp.T, temp)
#                 eucl1 = np.sqrt(sum_sq)
#                 temp = true_mean[1] - mean[i]
#                 sum_sq = np.dot(temp.T, temp)
#                 eucl2 = np.sqrt(sum_sq)
#
#                 # findinding index of point in this particular cluster
#                 indices = [index for index, element in enumerate(predictions[j]) if
#                     element == i]
#
#                 # depending upon eucledian distance setting cluster value
#                 cluster = 'b'
#                 if eucl1 < eucl2:
#                     cluster = 'g'
#
#                 # going through each index checking predicted and actual cluster are same, if not increasing error
#         for index in indices:
#             if ionosphere_df.iloc[index, -1] != cluster:
#                 error += 1
#
#         # Appending error to the list
#         errors.append(error * 100 / len(D))
#
#         # appending whole error to error_cluster
#         errors_cluster.append(errors)
#
#         # Appending no of iterations to list
#         iteration_cluster.append(iterations)
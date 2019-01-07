"""
@Author: tushushu
@Date: 2019-01-04 15:35:11
"""
from np.linalg import eig
import heapq


class PCA(object):
    """Principal component analysis (PCA)

    Arguments:
        n_components {int} -- Number of components to keep.
        eigen_vectors {array} -- The eigen vectors according to
        top n_components large eigen values.
    """

    def __init__(self):
        self.n_components = None
        self.eigen_vectors = None

    def _normalize(self, X):
        """Normalize the data by mean subtraction.

        Arguments:
            X {array} -- m * n array with int or float.

        Returns:
            array -- m * n array with int or float.
        """

        return X - X.mean(axis=0)

    def _get_covariance(self, X):
        """Calculate the covariance matrix.

        Arguments:
            X {array} -- m * n array with int or float.

        Returns:
            array -- n * n array with int or float.
        """

        return X.T.dot(X)

    def _get_top_eigen_vectors(self, X, n_components):
        """The eigen vectors according to top n_components large eigen values.

        Arguments:
            X {array} -- n * n array with int or float.
            n_components {int} -- Number of components to keep.

        Returns:
            array -- n * k array with int or float.
        """

        # Calculate eigen values and eigen vectors of covariance matrix.
        eigen_values, eigen_vectors = eig(X)
        # The indexes of top n_components large eigen values.
        indexes = heapq.nlargest(n_components, eigen_values)
        return eigen_vectors[indexes].T

    def fit(self, X, n_components):
        """Fit the model with X.

        Arguments:
            X {array} -- m * n array with int or float.
            n_components {int} -- Number of components to keep.
        """

        X_norm = self._normalize(X)
        X_cov = self._get_covariance(X_norm)
        self.n_components = n_components
        self.eigen_vectors = self._get_top_eigen_vectors(X_cov, n_components)

    def transform(self, X):
        """Apply the dimensionality reduction on X.

        Arguments:
            X {array} -- m * n array with int or float.

        Returns:
            array -- n * k array with int or float.
        """

        return X.dot(self.eigen_vectors)

    def fit_trasform(self, X, n_components):
        """Fit the model with X and apply the dimensionality reduction on X.

        Arguments:
            X {array} -- m * n array with int or float.
            n_components {int} -- Number of components to keep.

        Returns:
            array -- n * k array with int or float.
        """

        self.fit(X, n_components)
        return self.transform(X)

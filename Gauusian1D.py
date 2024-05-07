# gaussian 1D
import numpy as np


class Gaussian1D:
    def __init__(self, mu, sigma2):
        self.mu = mu
        self.sigma2 = np.sqrt(sigma2)
        super(self).__init__(1)

    def log_pdf(self, x, *args, **kwargs):
        """
        log probability density function
        x.shape = (m, 1)
        returns array of (m, ) elements
        """
        out = -((x - self.mu) ** 2) / (2 * self.sigma**2) - 0.5 * np.log(
            2 * np.pi * self.sigma**2
        )
        return out[:, 0]

    def grad_x_log_pdf(self, x, *args, **kwargs):
        """
        x.shape is (m, 1)
        returns array of (m, 1) elements
        """
        out = -(x - self.mu) / self.sigma**2
        return out

    def hess_x_log_pdf(self, x, *args, **kwargs):
        out = -np.ones(x.shape[0]) / self.sigma**2
        return out[:, np.newaxis, np.newaxis]

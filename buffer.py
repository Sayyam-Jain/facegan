import numpy as np

class Buffer(object):
  def __init__(self, config, rng):
    self.rng = rng
    self.buffer_size = config.buffer_size
    self.batch_size = config.batch_size

    self.image_dims = [
      config.input_scale_size,
      config.input_scale_size,
      3,
    ]

    self.idx = 0
    self.data = np.zeros([self.buffer_size] + self.image_dims)

  def push(self, batches):
    batch_size = len(batches)
    if self.idx + batch_size > self.buffer_size:
      random_idx1 = self.rng.choice(self.idx, int(self.batch_size/2))
      random_idx2 = self.rng.choice(batch_size, int(self.batch_size/2))
      self.data[random_idx1] = batches[random_idx2]
    else:
      self.data[self.idx:self.idx+batch_size] = batches
      self.idx += batch_size

  def sample(self, n=None):
    #assert self.idx > n, "not enough data is pushed"
    if n is None:
      n = int( self.batch_size/2,)
    if n < self.idx:
      random_idx = self.rng.choice(self.idx, n)
      return self.data[random_idx]
    else:
      return np.random.rand(int( self.batch_size/2), self.image_dims[0], self.image_dims[1], self.image_dims[2])

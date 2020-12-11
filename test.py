import os.path, time

print("Last modified: %s" % time.ctime(os.path.getmtime("C:/Users/Elliott/Downloads/Photos - Copy/f0a3169434bc27ddf5fb118e8bfce9b93ff18cce.mp4")))
print("Created: %s" % time.ctime(os.path.getctime("C:/Users/Elliott/Downloads/Photos - Copy/f0a3169434bc27ddf5fb118e8bfce9b93ff18cce.mp4")))
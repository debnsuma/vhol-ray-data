# actor_counter.py
import ray
import numpy as np
import time

ray.init()

# 1. Define the stateful service as a Python Class
@ray.remote
class PixelCounter:
    # The internal state is defined in __init__
    def __init__(self):
        self.total_pixels = 0

    # A method to mutate (update) the internal state
    def add(self, num_pixels: int):
        self.total_pixels += num_pixels

    # A method to retrieve the internal state
    def get_total(self) -> int:
        return self.total_pixels

# 2. Modify the Task to use the Actor Handle
@ray.remote
def process_image_with_actor(image: np.ndarray, counter_actor: "ActorHandle"):
    # This task calls the Actor's add method remotely
    counter_actor.add.remote(image.size)
    time.sleep(1)
    # The image processing logic is here, but omitted for simplicity

# --- Main Script ---
images = [np.random.randint(0, 255, (10, 10, 3)) for _ in range(8)]
image_size = images[0].size
expected_total = image_size * len(images) # 8 * 300 = 2400

# 3. Create a single instance (the Actor Handle)
counter = PixelCounter.remote()

# 4. Launch 8 parallel tasks, passing the Actor Handle to each
task_refs = [process_image_with_actor.remote(img, counter) for img in images]

# Wait for all the image processing tasks to complete
ray.get(task_refs)

# 5. Retrieve the final state from the Actor
final_total_ref = counter.get_total.remote()
final_total = ray.get(final_total_ref)

print(f"Expected total pixels: {expected_total}")
print(f"Actual total from actor: {final_total}")

ray.shutdown()
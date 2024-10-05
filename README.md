AES-CTR 128 Manim CUDA Animation
This project contains a Manim animation demonstrating the AES-CTR 128 encryption process and explains why using CUDA is a great option for this process. The animation visually represents the key steps involved in AES-CTR 128 encryption, showcasing how the algorithm operates efficiently in a parallelized manner using CUDA.

Why Use CUDA?
CUDA (Compute Unified Device Architecture) is a parallel computing platform developed by NVIDIA. It allows the AES-CTR mode of encryption to be processed more efficiently by running on the GPU in parallel rather than sequentially on a CPU.

Benefits of CUDA for AES-CTR 128 Encryption:
Parallel Processing: CUDA leverages the CTR mode of AES encryption, where each block can be encrypted independently, allowing for parallel execution.
Efficiency: By processing multiple blocks simultaneously, CUDA significantly reduces encryption time.
Scalability: CUDA's architecture is highly scalable, making it ideal for handling large datasets.

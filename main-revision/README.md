# 1. Deep Learning Primitives (From Scratch)


* **2D Convolution (`Conv2D`):** Implement the forward pass. You must accurately handle edge padding, strides, and ideally, implement the `im2col` transformation to show how convolutions are converted into efficient matrix multiplications.
* **Multi-Head Self-Attention:** Write the scaled dot-product attention mechanism. Be ready to discuss the computational complexity differences between dense attention and the sparse attention mechanisms you are researching.
* **Numerically Stable Softmax:** Write the Softmax function. To prevent floating-point overflow when exponentiating large numbers, you must implement the trick of subtracting the maximum value from the array first.
* **Normalization Layers:** Code Layer Normalization and Batch Normalization. Explain the mathematical differences and why one is favored in Transformers while the other dominates CNNs.
* **Activation Functions & Derivatives:** Implement ReLU, GELU, or Swish, along with their analytical derivatives for the backward pass.

# 2. CUDA & Hardware-Aware Algorithms (C++)

These questions test your ability to write code that actually runs fast on a GPU, leveraging your understanding of SIMT and memory constraints.

* **Tiled Matrix Multiplication (GEMM):** Write a CUDA kernel for matrix multiplication. You will need to demonstrate the use of shared memory tiling to minimize slow global memory fetches.
* **Parallel Reductions:** Implement a parallel sum or max reduction. The interviewer will specifically look for how you avoid warp divergence and utilize warp-level intrinsics for peak efficiency.
* **Tensor Striding:** Given an N-dimensional tensor's shape and strides, write a C++ function to map an N-dimensional coordinate to its flat 1D memory offset.
* **Low-Level Manipulation:** Reverse the bits of a 32-bit integer without using a loop, testing your comfort with bitwise operations and register-level logic.

# 3. Optimization & Backpropagation Math

* **Implement Adam Optimizer:** Write the parameter update step for Adam from memory. You need the formulas for the first moment (momentum), second moment (RMSProp), and their respective bias corrections.
* **Manual Backpropagation:** Given a small custom Multi-Layer Perceptron (MLP) or a specific loss function (like Binary Cross-Entropy), manually derive the gradients using the chain rule on the whiteboard.

# 4. Standard DSA with DL

* **Topological Sort (Directed Acyclic Graph):** Find the optimal execution order of nodes. *The DL Twist:* If the nodes represent neural network layers in a computation graph, how does this algorithm dictate memory allocation and scheduling?
* **LRU Cache:** Implement using a Hash Map and Doubly Linked List. *The Systems Twist:* How do you make this thread-safe? How do hardware caches differ from this software implementation?
* **Merge / Non-Overlapping Intervals:** *The DL Twist:* Apply this logic to GPU stream scheduling or memory allocation chunks to prevent overlaps in a high-throughput pipeline.
* **Binary Search in Rotated Array:** *The Systems Twist:* How does cache locality impact the performance of your search if the array exceeds the L1/L2 cache size?

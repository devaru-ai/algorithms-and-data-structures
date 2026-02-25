# 1. Deep Learning Primitives (From Scratch)


* **2D Convolution (`Conv2D`):** Implement the forward pass. You must accurately handle edge padding, strides, and ideally, implement the `im2col` transformation to show how convolutions are converted into efficient matrix multiplications.
* **Multi-Head Self-Attention:** Write the scaled dot-product attention mechanism. Be ready to discuss the computational complexity differences between dense attention and the sparse attention mechanisms you are researching.
* **Numerically Stable Softmax:** Write the Softmax function. To prevent floating-point overflow when exponentiating large numbers, you must implement the trick of subtracting the maximum value from the array first.
* **Normalization Layers:** Code Layer Normalization and Batch Normalization. Explain the mathematical differences and why one is favored in Transformers while the other dominates CNNs.
* **Activation Functions & Derivatives:** Implement ReLU, GELU, or Swish, along with their analytical derivatives for the backward pass.

# 2. Optimization & Backpropagation Math

* **Implement Adam Optimizer:** Write the parameter update step for Adam from memory. You need the formulas for the first moment (momentum), second moment (RMSProp), and their respective bias corrections.
* **Manual Backpropagation:** Given a small custom Multi-Layer Perceptron (MLP) or a specific loss function (like Binary Cross-Entropy), manually derive the gradients using the chain rule on the whiteboard.


# Practice

# 1. The "Chain Rule" Engine (Mini-Autograd)

If you can implement a tiny version of a computational graph, you prove you understand how PyTorch actually works under the hood.

* **The Coding Task:** Write a simple `Tensor` class that supports an addition and a multiplication, and a `.backward()` method that recursively propagates gradients.

* **The Goal:** Show you understand that `grad_input = grad_output * local_derivative`.
  
* **Whiteboard Pitch:** Draw a graph with nodes $A$ and $B$ leading to $C$. Show how the gradient flows backward through the edges using the multivariate chain rule.


# 2. Weight Initialization & The "Vanishing Gradient" Code

Standard initialization (like setting weights to 0) kills deep networks. You need to be able to code **Xavier (Glorot) or He Initialization**.

* **The Coding Task:** Write the function to initialize a weight matrix of shape $(in-dim, out-dim)$.
  
## **He Init (for ReLU):**
 $\text{std} = \sqrt{2 / \text{fan\\_in}}$
 
## **Xavier (for Sigmoid/Tanh):**
$\text{std} = \sqrt{2 / (\text{fan\\_in} + \text{fan\\_out})}$

* **Why it matters:** In an interview, they might ask: "Why is my model not training?" You need to show that if weights are too small, gradients vanish (go to 0); if too large, they explode (go to NaN).


# 3. Optimizer Logic (SGD with Momentum & Adam)

Backprop only gives you the *direction* to move. The Optimizer decides *how far* to move.

* **The Coding Task:** Implement **Adam** from scratch. It’s the most common interview coding question for this level.
* **The Key Equations to Code:**
1. **First Moment ($m$):** Moving average of gradients (Momentum).
2. **Second Moment ($v$):** Moving average of *squared* gradients (RMSProp).
3. **Bias Correction:** Adjusting $m$ and $v$ because they start at 0.


* **The Whiteboard Pitch:** Explain why Adam is better for sparse gradients (relevant to your research!)—the $v$ term scales the learning rate for each parameter individually.


# Fun Problems

* **Option A:** Write the **Adam Optimizer** code (highly recommended for NVIDIA).
* **Option B:** Write a **Mini-Autograd** (The most "Big Brain" way to show you understand backprop).
* **Option C:** Write a **Full Training Loop** that combines your Normalization, Activations, and Softmax into a single "Step".




# 3. CUDA & Hardware-Aware Algorithms (C++)

These questions test your ability to write code that actually runs fast on a GPU, leveraging your understanding of SIMT and memory constraints.

* **Tiled Matrix Multiplication (GEMM):** Write a CUDA kernel for matrix multiplication. You will need to demonstrate the use of shared memory tiling to minimize slow global memory fetches.
* **Parallel Reductions:** Implement a parallel sum or max reduction. The interviewer will specifically look for how you avoid warp divergence and utilize warp-level intrinsics for peak efficiency.
* **Tensor Striding:** Given an N-dimensional tensor's shape and strides, write a C++ function to map an N-dimensional coordinate to its flat 1D memory offset.
* **Low-Level Manipulation:** Reverse the bits of a 32-bit integer without using a loop, testing your comfort with bitwise operations and register-level logic.


# 4. Standard DSA with DL

* **Topological Sort (Directed Acyclic Graph):** Find the optimal execution order of nodes. *The DL Twist:* If the nodes represent neural network layers in a computation graph, how does this algorithm dictate memory allocation and scheduling?
* **LRU Cache:** Implement using a Hash Map and Doubly Linked List. *The Systems Twist:* How do you make this thread-safe? How do hardware caches differ from this software implementation?
* **Merge / Non-Overlapping Intervals:** *The DL Twist:* Apply this logic to GPU stream scheduling or memory allocation chunks to prevent overlaps in a high-throughput pipeline.
* **Binary Search in Rotated Array:** *The Systems Twist:* How does cache locality impact the performance of your search if the array exceeds the L1/L2 cache size?

Since you have already covered the "Architectural Primitives," the next logical step for an NVIDIA-level interview is to move into **Optimization, System Design, and Training Dynamics**. NVIDIA specifically cares about how these models interact with the GPU and how they behave during large-scale training.


# 5. The Fused Kernel Logic (Triton/CUDA Style)

Explain the **logic of a Fused Bias-ReLU or Fused Softmax**.

* **The Problem:** In standard PyTorch, `ReLU(Linear(x) + bias)` involves three separate kernel launches and three trips to Global Memory.
* **The Coding Task:** Write the pseudo-code for a single loop that loads a tile of data into SRAM, adds the bias, applies ReLU, and writes back only once.
* **Why NVIDIA cares:** This is exactly how they achieve 2x–5x speedups in the `Apex` or `TransformerEngine` libraries.

# 6. Distributed Training: Data Parallelism (DP) vs. Distributed Data Parallel (DDP)

You need to be able to code the **All-Reduce** logic and explain the communication overhead.

* **The Coding Task:** Implement a simplified version of the **Parameter Server** or **Ring All-Reduce** algorithm. How do gradients get averaged across 8 GPUs?
* **Whiteboard Challenge:** Draw the "Ring" and show how chunks of gradients are passed around. Prove that the communication cost is independent of the number of GPUs ($O(\text{size of model})$).

# 7. Mixed Precision Training (FP16/BF16)

NVIDIA’s Tensor Cores are built for half-precision. You must understand **Loss Scaling**.

* **The Problem:** FP16 has a narrow range. Small gradients can "underflow" to zero.
* **The Coding Task:** Write a training loop that implements **Dynamic Loss Scaling**.
1. Multiply loss by a large factor ($S$).
2. Backpropagate.
3. Check gradients for `Inf/NaN`.
4. If safe, unscale $(\text{grad} / S)$ and update weights.

## This is the difference between a model that converges and one that crashes on an H100.


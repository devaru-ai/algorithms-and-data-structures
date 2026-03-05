
## 🔥 PRIORITY TIERS

1. **Must-master (High probability of being asked)**

   * Softmax + cross-entropy derivation
   * Attention (scaled dot-product, multi-head)
   * Backprop / gradient flow / vanishing/exploding gradients
   * Optimization (SGD, Adam, momentum, weight decay)
   * Residual connections + LayerNorm
   * Memory & system reasoning (FP16/BF16, mixed precision, gradient checkpointing)
   * Practical debugging (diverging loss, plateau, overfitting)

2. **Medium probability**

   * CNN concepts (receptive field, dilation, residual nets)
   * Generalization theory (flat vs sharp minima, double descent)
   * Regularization techniques (dropout, L1/L2, label smoothing)
   * Positional encodings (absolute & relative)

3. **Nice-to-know / low probability**

   * Generative models (autoencoders, diffusion, autoregressive)
   * Transformer variants (sparse, local, global)
   * Advanced distributed system hacks (pipeline parallelism deep details)

---

# 🧠 LAYER-BY-LAYER PREP

### **Layer 1 — Mathematical Foundations (ML + DL core)**

**Topics to Cover:**

* Linear Algebra: matrix multiplication, norms, rank, overparameterization
* Probability: MLE, MAP, KL divergence, cross-entropy vs entropy, expectation, variance scaling
* Optimization: gradient descent, convex vs non-convex, saddle points, Hessian intuition

**Sample Questions:**

* Derive gradient of cross-entropy loss
* What is KL divergence and how does it relate to cross-entropy?
* Explain why overparameterized linear models can still generalize

**Tips:**

* Focus on reasoning over proofs
* Practice derivations on whiteboard

---

### **Layer 2 — Core Neural Network Mechanics**

**Topics to Cover:**

* Forward pass & backprop (chain rule)
* Activations: ReLU, GELU, Sigmoid, Tanh
* Initialization: Xavier, He
* Residual connections
* Normalization: BatchNorm vs LayerNorm
* Vanishing/exploding gradients

**Sample Questions:**

* Why ReLU reduces vanishing gradients
* How residual connections allow deep networks to train
* Why LayerNorm is preferred in transformers

**Tips:**

* Derive simple backprop on paper
* Be able to explain gradient flow through deep networks

---

### **Layer 3 — Transformers / Modern Architectures**

**Topics to Cover:**

* Scaled dot-product attention (derivation, gradient, √d scaling)
* Multi-head attention (why, shapes, pros/cons)
* Positional encodings (absolute vs relative)
* Encoder vs Decoder (masking, KV cache)
* Residual + LayerNorm in transformers
* Memory & computational complexity (O(n²), sequence scaling)
* Scaling hacks: mixed precision, checkpointing, sparse attention

**Sample Questions:**

* Explain why QK^T is divided by √d_k
* How does sequence length affect memory in attention?
* Why multi-head attention improves expressivity

**Tips:**

* Whiteboard derivations of attention
* Draw shapes and memory usage
* Explain system trade-offs clearly

---

### **Layer 4 — Training Dynamics & Generalization**

**Topics to Cover:**

* Overparameterization
* Sharp vs flat minima
* Implicit regularization (SGD noise)
* Optimizer behavior: SGD vs Adam
* Double descent & bias-variance
* Regularization: L1/L2, dropout, label smoothing
* Learning rate effects & scheduling

**Sample Questions:**

* Why large models generalize well despite overfitting capacity
* Why Adam sometimes generalizes worse than SGD
* Explain effect of dropout / label smoothing

**Tips:**

* Use intuitive drawings (loss landscapes)
* Connect optimizer → trajectory → generalization

---

### **Layer 5 — Scaling & Systems (NVIDIA-specific)**

**Topics to Cover:**

* Precision: FP32, FP16, BF16, loss scaling
* Memory: parameters, activations, optimizer states
* Gradient checkpointing
* Parallelism: data, model, pipeline
* Communication vs compute tradeoffs
* Attention memory optimizations (FlashAttention, sparse)
* KV cache & inference optimizations

**Sample Questions:**

* How to reduce memory usage by 40%
* Explain mixed precision and why it helps
* How does all-reduce work in data parallel training

**Tips:**

* Draw system diagrams
* Calculate memory for small examples, then scale
* Explain practical trade-offs

---

### **Layer 6 — Practical Debugging & Engineering Thinking**

**Topics to Cover:**

* Training diverges → LR, gradient explosion, initialization, FP16 issues
* Loss plateau → learning rate, saturation, data issues
* Overfitting → regularization, data, model size
* Batch size effects → LR scaling
* Structured debugging workflow

**Sample Questions:**

* Training loss → NaN: what do you check?
* Attention outputs → NaN: what do you debug?
* Loss plateaus early: possible causes?


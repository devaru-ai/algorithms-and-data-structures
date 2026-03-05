
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


---


# 🏗️ FULL BLOCK-BASED DEEP LEARNING + ML PREP


## **Block 1 — Softmax + Cross-Entropy Derivation**

**Layers covered:** Layer 1 (Math) + Layer 2 (NN Mechanics)

**Contents:**

* Derive ∂L/∂z for cross-entropy + softmax → result: ∂L/∂z = ŷ - y
* Explain:

  * Softmax saturation → vanishing gradients
  * Why logits are used instead of probabilities
  * Numerical stability → Log-Sum-Exp trick
* Optional mini-derivation: backprop through a linear layer

**Sample Questions:**

* Derive softmax gradient
* Why cross-entropy with logits is stable
* What happens to gradient if prediction is extremely confident

**Goal:** Be able to write and explain derivations **without hesitation** on a whiteboard

---

## **Block 2 — Attention & Transformer Mechanics**

**Layers covered:** Layer 3 (Transformers), Layer 2 (NN Mechanics)

**Contents:**

* Scaled dot-product attention: softmax(QK^T / √d_k) V
* Why divide by √d? → variance scaling
* Multi-head attention → shapes, benefits
* Residual + LayerNorm → gradient flow
* Positional encodings → absolute vs relative
* Complexity: O(n²) time, O(n²) memory

**Sample Questions:**

* Explain QK^T/√d mathematically
* Why multi-head improves representation
* How memory scales with sequence length
* How would you reduce memory (sparse attention, FlashAttention, checkpointing)

**Goal:** Be able to explain attention **mechanically, mathematically, and memory-wise**

---

## **Block 3 — Optimization & Training Dynamics**

**Layers covered:** Layer 4 (Training Dynamics) + Layer 2 (NN Mechanics)

**Contents:**

* Optimizers:

  * SGD → generalization
  * Adam → faster convergence
  * Momentum & RMSProp intuition
* Vanishing/exploding gradients → chain rule, activation derivatives
* Residual connections → gradient bypass
* Flat vs sharp minima → impact on generalization
* Implicit regularization in SGD

**Sample Questions:**

* Why Adam may generalize worse than SGD
* Explain sharp vs flat minima
* How residuals stabilize training
* Why learning rate scheduling matters

**Goal:** Be able to reason **why a model trains well or fails to generalize**

---

## **Block 4 — Systems & Scaling (NVIDIA-specific)**

**Layers covered:** Layer 5 (Scaling & Systems) + touches Layer 6

**Contents:**

* Precision: FP32 / FP16 / BF16, loss scaling
* Memory: parameters vs activations vs optimizer states
* Gradient checkpointing
* Data parallelism → all-reduce
* Model / pipeline parallelism
* Compute-bound vs memory-bound analysis
* Attention memory & optimizations (FlashAttention, sparse attention)

**Sample Questions:**

* How to reduce memory by 40%
* Explain mixed precision workflow
* How all-reduce works in multi-GPU training
* Why attention layers are memory-heavy

**Goal:** Be able to **reason about GPU hardware and distributed training**

---

## **Block 5 — Practical Debugging / Engineering Thinking**

**Layers covered:** Layer 6

**Contents:**

* Training divergence → LR, gradients, initialization, precision
* Loss plateau → LR too low, saturated activations, poor architecture
* Overfitting → regularization, data augmentation, model size
* Batch size scaling → LR adjustment
* Structured debugging checklist → inputs → forward → loss → gradients → optimizer → data

**Sample Questions:**

* Loss → NaN: what do you check?
* Attention outputs → NaN: debug steps
* Plateauing loss → causes and fixes

**Goal:** Be able to explain **structured reasoning in 30–60 seconds per scenario**

---

## **Block 6 — CNN / Vision Concepts**

**Layers covered:** Layer 3 (Architectures), optional Layer 4

**Contents:**

* Convolution math
* Receptive field growth
* Dilation
* Residual networks → why they train deeper
* Feature hierarchy → why deeper networks generalize
* Regularization / normalization for CNNs

**Sample Questions:**

* How receptive field grows with depth
* Why residual connections help CNNs
* What dilation does

**Goal:** Solidify **CV concepts** if interviewing for vision-heavy teams

---

## **Block 7 — Probability, Statistics & ML Fundamentals**

**Layers covered:** Layer 1 + Layer 4

**Contents:**

* KL divergence, cross-entropy, entropy
* MLE vs MAP
* Bias-variance tradeoff
* Double descent (conceptually)
* Expectation, variance, variance scaling

**Sample Questions:**

* Difference between cross-entropy and KL divergence
* Why overparameterized models can still generalize
* How label smoothing affects bias/variance

**Goal:** Be able to **reason probabilistically about model outputs**

---

## **Block 8 — Hero Project Deep Dive**

**Layers covered:** Layer 6 + some Layer 3/4

**Contents:**

* Explain your project end-to-end
* Architecture choice + bottlenecks
* Metrics / baselines
* Scaling your model → 10x data, 10x parameters
* System considerations (GPU clusters, memory)
* Debugging scenarios encountered

**Sample Questions:**

* Why did training diverge in your project?
* How would you scale to multi-GPU?
* How do you know it’s not overfitting?

**Goal:** Be able to **explain your project like a research engineer**, with systems awareness

---

# 🏆 SUMMARY OF BLOCKS TO LAYERS

| Block | Layer(s) Covered              |
| ----- | ----------------------------- |
| 1     | Layer 1 + 2                   |
| 2     | Layer 3 + 2                   |
| 3     | Layer 4 + 2                   |
| 4     | Layer 5 + 6                   |
| 5     | Layer 6                       |
| 6     | Layer 3 + 4 (CV)              |
| 7     | Layer 1 + 4 (ML fundamentals) |
| 8     | Layer 6 + Layer 3/4 (Project) |

---
